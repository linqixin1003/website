"""Synchronize the inline recovery handler which must work when locale.js is unreachable."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = re.compile(r'(?:    <script data-guide-bootstrap>.*?</script>\n)?    <script defer src="([^"]*locale\.js)"(?: onload="guideScriptLoaded\(\)")?(?: onerror="guideScriptFailed\(this\)")?></script>', re.S)

BOOTSTRAP = """    <script data-guide-bootstrap>
      const guideRequested = new URLSearchParams(location.search).get("lang");
      if (guideRequested) document.documentElement.style.visibility = "hidden";
      function guideScriptLoaded() { document.documentElement.style.visibility = ""; }
      function guideScriptFailed(original) {
        const retryScript = document.createElement("script");
        const retryUrl = new URL(original.src);
        retryUrl.searchParams.set("retry", "1");
        retryScript.src = retryUrl;
        retryScript.onload = guideScriptLoaded;
        retryScript.onerror = () => {
          const showRecovery = () => {
            const labels = LABELS;
            const tag = (guideRequested || document.documentElement.lang || "en").replace(/_/g, "-").toLowerCase();
            const base = tag.split("-")[0];
            const alias = {iw:"he", in:"id", tl:"fil", no:"nb"}[base];
            const code = base === "zh" ? (/hant|tw|hk|mo/.test(tag) ? "zh-hant-tw" : "zh-hans") : (alias || base);
            const [message, label] = labels[code] || labels.en;
            const panel = document.createElement("section");
            panel.className = "locale-recovery";
            panel.lang = code;
            panel.dir = "auto";
            const button = document.createElement("button");
            button.type = "button";
            button.textContent = label;
            button.onclick = () => location.reload();
            const notice = document.createElement("p");
            notice.textContent = message;
            panel.append(notice, button);
            if (guideRequested) {
              document.title = label;
              document.body.replaceChildren(panel);
            } else {
              document.body.prepend(panel);
            }
            document.documentElement.style.visibility = "";
          };
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", showRecovery, {once:true});
          else showRecovery();
        };
        const load = () => document.head.append(retryScript);
        if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", load, {once:true});
        else load();
      }
    </script>"""

def sync(check):
    source = (ROOT / "locale.js").read_text()
    labels, _ = json.JSONDecoder().raw_decode(source.split("const recoveryLanguages = ", 1)[1])
    button_labels = {code.lower(): values[1:] for code, values in labels.items()}
    inline = BOOTSTRAP.replace("LABELS", json.dumps(button_labels, ensure_ascii=False, separators=(",", ":")))
    for page in [ROOT / "index.html", *sorted((ROOT / "en").rglob("*.html")), *sorted((ROOT / "zh").rglob("*.html"))]:
        original = page.read_text()
        updated, count = SCRIPT.subn(lambda m: inline + '\n    <script defer src="' + m[1] + '" onload="guideScriptLoaded()" onerror="guideScriptFailed(this)"></script>', original)
        if count != 1:
            raise ValueError(f"Expected one locale script in {page}")
        if original != updated:
            if check:
                raise ValueError(f"Run sync_guide_bootstrap.py to update {page}")
            page.write_text(updated)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    sync(parser.parse_args().check)
