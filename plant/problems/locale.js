/* Pages use the same relative paths in both source languages. Dictionary
 * generation runs at publication time; the reader only contacts this site. */
(() => {
  "use strict";
  const guide = new URL(".", document.currentScript.src);
  const current = new URL(location.href);
  const relative = current.pathname.slice(guide.pathname.length);
  const templateLocale = relative.split("/")[0];
  const isLanding = relative === "" || relative === "index.html";
  const requested = current.searchParams.get("lang");
  const captionNote = "Resized and converted to WebP";

  async function readJSON(path) {
    const response = await fetch(new URL(path, guide));
    if (!response.ok) throw new Error("Language data unavailable");
    return response.json();
  }

  function resolveLanguage(value, languages) {
    if (!value) return templateLocale === "zh" ? "zh-Hans" : "en";
    const tag = value.replace(/_/g, "-").toLowerCase();
    const exact = Object.keys(languages).find(key => key.toLowerCase() === tag);
    if (exact) return exact;
    if (/^zh($|-)/.test(tag)) return /(?:hant|tw|hk|mo)/.test(tag) ? "zh-Hant-TW" : "zh-Hans";
    const base = tag.split("-")[0];
    const aliases = {iw:"he", in:"id", tl:"fil", no:"nb"};
    return aliases[base] || (Object.prototype.hasOwnProperty.call(languages, base) ? base : "en");
  }

  function destination(code, page) {
    const url = new URL((code === "zh-Hans" ? "zh/" : "en/") + page, guide);
    for (const [key, value] of current.searchParams) {
      if (key !== "lang") url.searchParams.append(key, value);
    }
    if (code !== "en" && code !== "zh-Hans") url.searchParams.set("lang", code);
    url.hash = current.hash;
    return url;
  }

  function renderChooser(languages, selected, page, label) {
    const header = document.querySelector("header");
    if (!header) return;
    const picker = document.createElement("select");
    picker.setAttribute("aria-label", label);
    picker.style.cssText = "font:inherit;max-width:48%;min-height:2.75rem;border:1px solid #b2bdb6;border-radius:.45rem;background:white;color:#205b42;padding:.25rem .45rem";
    for (const [code, name] of Object.entries(languages)) {
      const option = document.createElement("option");
      option.lang = code;
      option.dir = "auto";
      option.value = code;
      option.textContent = name;
      option.selected = code === selected;
      picker.append(option);
    }
    picker.addEventListener("change", () => {
      const next = destination(picker.value, page);
      picker.value = selected;
      location.assign(next);
    });
    window.addEventListener("pageshow", () => { picker.value = selected; });
    const previous = header.querySelector("a[lang]");
    if (previous) previous.replaceWith(picker);
    else header.append(picker);
  }

  function renderLanding(languages) {
    const nav = document.querySelector("nav");
    if (!nav) return;
    const fragment = document.createDocumentFragment();
    for (const [code, name] of Object.entries(languages)) {
      const link = document.createElement("a");
      link.className = "item";
      link.href = destination(code, "index.html");
      link.lang = link.hreflang = code;
      link.dir = "auto";
      link.textContent = name;
      fragment.append(link);
    }
    nav.replaceChildren(fragment);
  }

  function localize(dictionary, code) {
    const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      const element = node.parentElement;
      if (!element || element.closest("script,style,select,a[lang],footer a")) continue;
      const key = node.nodeValue.trim();
      if (!key) continue;
      if (element.closest("figcaption") && key !== "Photo source") {
        for (const note of [captionNote, "some rights reserved"]) {
          if (key.includes(note) && dictionary[note]) {
            node.nodeValue = node.nodeValue.replace(note, () => dictionary[note]);
          }
        }
        continue;
      }
      if (Object.prototype.hasOwnProperty.call(dictionary, key)) node.nodeValue = node.nodeValue.replace(key, () => dictionary[key]);
    }
    for (const element of document.querySelectorAll("[alt],[aria-label]")) {
      for (const attr of ["alt", "aria-label"]) {
        const key = element.getAttribute(attr);
        if (key && Object.prototype.hasOwnProperty.call(dictionary, key)) element.setAttribute(attr, dictionary[key]);
      }
    }
    document.documentElement.lang = code;
    document.documentElement.dir = ["ar","he","fa","ur"].includes(code) ? "rtl" : "ltr";
    for (const link of document.querySelectorAll("a[href]")) {
      const url = new URL(link.href);
      if (url.origin === guide.origin && url.pathname.startsWith(guide.pathname + "en/") &&
          url.pathname.endsWith(".html") && !link.hasAttribute("lang")) {
        url.searchParams.set("lang", code);
        link.href = url;
      }
    }
  }

  async function start() {
    const languages = await readJSON("locales/languages.json");
    const code = resolveLanguage(requested, languages);
    if (isLanding) {
      if (requested) location.replace(destination(code, "index.html"));
      else renderLanding(languages);
      return;
    }
    if (!["en", "zh"].includes(templateLocale)) return;
    const page = relative.slice(templateLocale.length + 1) || "index.html";
    if ((code === "zh-Hans") !== (templateLocale === "zh")) {
      location.replace(destination(code, page));
      return;
    }
    let label = code === "zh-Hans" ? "语言" : "Language";
    if (code !== "en" && code !== "zh-Hans") {
      const dictionary = await readJSON("locales/" + code + ".json");
      localize(dictionary, code);
      label = dictionary.Language || label;
    }
    renderChooser(languages, code, page, label);
  }

  start().catch(error => {
    console.warn("Plant guide language loading failed", error);
    document.documentElement.dataset.localeError = "true";
  });
})();
