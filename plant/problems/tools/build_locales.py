"""Build static plant-guide translations. Run after editing the English pages.

Python 3, standard library. Existing dictionary entries are reused; an interrupted
run can resume. --check only reports missing text, and never contacts a provider.
"""
import argparse
import concurrent.futures
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"
SOURCE = ROOT / "en"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())
PROVIDER_CODES = {"fil": "tl", "nb": "no", "zh-Hant-TW": "zh-TW"}
CAPTION = "Resized and converted to WebP"


class SourceText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.entries = {"Language", "Photo source", "some rights reserved", CAPTION}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append((tag, attrs))
        for key in ("alt", "aria-label"):
            if attrs.get(key):
                self.entries.add(attrs[key].strip())

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        text = data.strip()
        if not text or not re.search("[A-Za-z]", text):
            return
        tags = {t for t, _ in self.stack}
        if tags & {"script", "style", "figcaption"} or any(
            t == "a" and "lang" in attrs for t, attrs in self.stack
        ):
            return
        if "footer" in tags and "a" in tags:
            return
        self.entries.add(text)


def translate_batch(code, entries):
    payload = dict(client="gtx", sl="en", tl=PROVIDER_CODES.get(code, code), dt="t", q="\n".join(entries))
    url = "https://translate.googleapis.com/translate_a/single?" + urlencode(payload)
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"User-Agent": "PlantGuide-localization/1.0"}), timeout=22) as response:
                parts = json.load(response)[0]
            translation = "".join(part[0] for part in parts if part and isinstance(part[0], str))
            lines = [line.strip() for line in translation.splitlines()]
            if len(lines) == len(entries) and all(lines):
                result = dict(zip(entries, lines))
                if len(entries) > 1:
                    for source, translated in result.items():
                        if copied_prose(source, translated):
                            result[source] = translate_batch(code, [source])[source]
                elif copied_prose(entries[0], lines[0]):
                    raise ValueError(f"Provider returned source prose unchanged: {entries[0]}")
                return result
            if len(entries) == 1 and translation.strip():
                return {entries[0]: translation.strip()}
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    middle = len(entries) // 2
    if not middle:
        raise ValueError(f"Empty translation for {code}: {entries!r}")
    return {**translate_batch(code, entries[:middle]), **translate_batch(code, entries[middle:])}


def copied_prose(source, translation):
    return len(source) > 30 and source.casefold() == translation.casefold()


def chunks(entries):
    batch = []
    length = 0
    for entry in entries:
        encoded = len(urlencode({"q": entry}))
        if batch and length + encoded > 4800:
            yield batch
            batch, length = [], 0
        batch.append(entry)
        length += encoded + 3
    if batch:
        yield batch


def save(path, data):
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    temp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--languages", nargs="+")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    available = json.loads((LOCALES / "languages.json").read_text())
    # The WebView needs these names and recovery controls before it can fetch a dictionary.
    script = (ROOT / "locale.js").read_text()
    recovery, _ = json.JSONDecoder().raw_decode(script.split("const recoveryLanguages = ", 1)[1])
    if ({code: labels[0] for code, labels in recovery.items()} != available or
            any(len(labels) != 3 or not all(labels) for labels in recovery.values())):
        parser.error("Sync the language names and recovery labels in locale.js with languages.json")
    codes = args.languages or [code for code in available if code not in {"en", "zh-Hans"}]
    glossary_path = LOCALES / "glossary.json"
    glossary = json.loads(glossary_path.read_text()) if glossary_path.exists() else {}
    source = SourceText()
    for path in sorted(SOURCE.rglob("*.html")):
        source.feed(path.read_text())
        source.close()
        source.stack.clear()
    def build(code):
        if code not in available or code in {"en","zh-Hans"}:
            raise ValueError(f"Unsupported dictionary locale {code}")
        path = LOCALES / (code + ".json")
        data = json.loads(path.read_text()) if path.exists() else {}
        overrides = {key: value for key, value in glossary.get(code, {}).items() if key in source.entries}
        data = {key: value for key, value in data.items() if not copied_prose(key, value)}
        missing = sorted(source.entries - data.keys())
        if args.check:
            if missing:
                print(f"{code}: {len(missing)} missing", flush=True)
            mismatches = [key for key, value in overrides.items() if data.get(key) != value]
            if mismatches:
                print(f"{code}: {len(mismatches)} glossary mismatches", flush=True)
            return not missing and not mismatches
        data.update(overrides)
        for batch in chunks(sorted(source.entries - data.keys())):
            data.update(translate_batch(code, batch))
            save(path, data)
        save(path, {key: data[key] for key in sorted(source.entries)})
        print(f"{code}: {len(source.entries)} entries ({len(missing)} new)", flush=True)
        return True
    success = True
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(build, code): code for code in codes}
        for future in concurrent.futures.as_completed(futures):
            try:
                success &= future.result()
            except Exception as error:
                print(f"{futures[future]}: {error}", file=sys.stderr, flush=True)
                success = False
    if args.check and success:
        print(f"Verified {len(codes)} dictionaries against {len(source.entries)} source strings.")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
