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

  // Bootstrap labels stay available even if the language dictionary cannot load.
  const recoveryLanguages = {
    "af": ["Afrikaans", "Netwerkfout, probeer asseblief weer!", "Probeer weer"],
    "am": ["አማርኛ", "የአውታረ መረብ ስህተት፣ እባክዎን እንደገና ይሞክሩ!", "እንደገና ሞክር"],
    "ar": ["العربية", "خطأ في الشبكة، يرجى المحاولة مرة أخرى!", "إعادة المحاولة"],
    "az": ["azərbaycan", "Şəbəkə xətası, xahiş edirik, yenidən cəhd edin!", "Təkrar cəhd et"],
    "be": ["беларуская", "Памылка сеткі, калі ласка, паспрабуйце яшчэ раз!", "Паўтарыць"],
    "bg": ["български", "Мрежова грешка, моля опитайте отново!", "Опитай отново"],
    "bn": ["বাংলা", "নেটওয়ার্ক ত্রুটি, অনুগ্রহ করে আবার চেষ্টা করুন!", "পুনরায় চেষ্টা করুন"],
    "ca": ["català", "Error de xarxa, si us plau, provi de nou!", "Torna a intentar"],
    "cs": ["čeština", "Chyba site, zkuste to znovu", "Zkusit znovu"],
    "da": ["dansk", "Netværksfejl, prøv igen!", "Prøv igen"],
    "de": ["Deutsch", "Netzwerkfehler, bitte erneut versuchen", "Erneut versuchen"],
    "el": ["Ελληνικά", "σφάλμα δικτύου, δοκιμάστε ξανά!", "Επανάληψη"],
    "en": ["English", "Network error, please try again!", "Retry"],
    "es": ["español", "Error de red, ¡inténtalo de nuevo!", "Reintentar"],
    "et": ["eesti", "Võrguviga, palun proovige uuesti!", "Proovi uuesti"],
    "eu": ["euskara", "Sare akatsa, mesedez saiatu berriro!", "Saiatu berriro"],
    "fa": ["فارسی", "خطای شبکه، لطفاً دوباره تلاش کنید!", "تلاش مجدد"],
    "fi": ["suomi", "verkkovirhe, yritä uudelleen!", "Yritä uudelleen"],
    "fil": ["Filipino", "Error sa network, pakiusap subukan muli!", "Subukan muli"],
    "fr": ["français", "Erreur réseau, veuillez réessayer !", "Réessayer"],
    "gl": ["galego", "Erro de rede, por favor inténtao de novo!", "Reintentar"],
    "gu": ["ગુજરાતી", "નેટવર્ક ભૂલ, કૃપા કરીને ફરીથી પ્રયાસ કરો!", "ફરી પ્રયાસ કરો"],
    "he": ["עברית", "שגיאת רשת, נא לנסות שוב!", "נסה שוב"],
    "hi": ["हिन्दी", "नेटवर्क त्रुटि, कृपया पुनः प्रयास करें!", "पुनः प्रयास"],
    "hr": ["hrvatski", "Mrežna greška, molimo pokušajte ponovo!", "Pokušaj ponovno"],
    "hu": ["magyar", "Hálózati hiba, kérjük, próbálja újra!", "Újra"],
    "hy": ["հայերեն", "Ցանցային սխալ, խնդրում ենք կրկին փորձել!", "Կրկին փորձել"],
    "id": ["Indonesia", "Kesalahan jaringan, silakan coba lagi!", "Coba Lagi"],
    "is": ["íslenska", "Netvill, vinsamlegast reyndu aftur!", "Reyna aftur"],
    "it": ["italiano", "Errore di rete, riprova!", "Riprova"],
    "ja": ["日本語", "ネットワークエラー、もう一度お試しください！", "再試行"],
    "ka": ["ქართული", "ქსელის შეცდომა, გთხოვთ, კვლავ სცადოთ!", "ხელახლა ცდა"],
    "kk": ["қазақ тілі", "Желілік қате, қайта тырыңыз!", "Қайталау"],
    "km": ["ខ្មែរ", "កំហុសបណ្តាញ សូមព្យាយាមម្តងទៀត!", "ព្យាយាមម្តងទៀត"],
    "kn": ["ಕನ್ನಡ", "ನೆಟ್‌ವರ್ಕ್ ದೋಷ, ದಯವಿಟ್ಟು ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ!", "ಮರುಪ್ರಯತ್ನಿಸಿ"],
    "ko": ["한국어", "네트워크 오류, 다시 시도해주세요!", "재시도"],
    "ky": ["кыргызча", "Тармактык ката, кайрадан аракет кылыңыз!", "Кайра аракет"],
    "lt": ["lietuvių", "Tinklo klaida, prašome bandyti dar kartą!", "Bandyti dar kartą"],
    "mk": ["македонски", "Мрежна грешка, ве молиме обидете се повторно!", "Обиди се повторно"],
    "ml": ["മലയാളം", "പിണ്ണിപ്പിന്റെ പിശക്, ദയവായി വീണ്ടും ശ്രമിക്കുക!", "വീണ്ടും ശ്രമിക്കുക"],
    "mn": ["монгол", "Сүлжээний алдаа, дахин оролд!", "Дахин оролдох"],
    "mr": ["मराठी", "नेटवर्क त्रुटी, कृपया पुन्हा प्रयत्न करा!", "पुन्हा प्रयत्न करा"],
    "ms": ["Melayu", "Ralat rangkaian, sila cuba lagi!", "Cuba lagi"],
    "nb": ["norsk bokmål", "nettverksfeil, prøv igjen!", "Prøv igjen"],
    "ne": ["नेपाली", "नेटवर्क त्रुटि, कृपया पुन: प्रयास गर्नुहोस्!", "पुन: प्रयास"],
    "nl": ["Nederlands", "netwerkfout, probeer het opnieuw!", "Opnieuw"],
    "pl": ["polski", "błąd sieci, spróbuj ponownie!", "Ponów"],
    "pt": ["português", "Erro de rede, tente novamente", "Tentar novamente"],
    "ru": ["русский", "Ошибка сети, попробуйте еще раз!", "Повторить"],
    "si": ["සිංහල", "ජාල දෝෂයක්, කරුණාකර නැවත උත්සාහ කරන්න!", "නැවත උත්සාහ කරන්න"],
    "sk": ["slovenčina", "chyba siete, skúste znovu!", "Opakovať"],
    "sq": ["shqip", "Gabim në rrjet, ju lutemi provoni përsëri!", "Riprovo"],
    "sr": ["српски", "Грешка мреже, покушајте поново!", "Pokušaj ponovo"],
    "sv": ["svenska", "Natverksfel, forsok igen", "Försök igen"],
    "ta": ["தமிழ்", "நெட்வொர்க் பிழை, தயவுசெய்து மீண்டும் முயற்சி செய்யுங்கள்!", "மீண்டும் முயற்சி"],
    "te": ["తెలుగు", "నెట్‌వర్క్ లోపం, దయచేసి మళ్లీ ప్రయత్నించండి!", "మళ్ళీ ప్రయత్నించండి"],
    "th": ["ไทย", "เครือข่ายผิดพลาด โปรดลองอีกครั้ง!", "ลองใหม่"],
    "tr": ["Türkçe", "ağ hatası, lütfen tekrar deneyin!", "Tekrar Dene"],
    "uk": ["українська", "Помилка мережі, спробуйте ще раз!", "Повторити"],
    "ur": ["اردو", "نیٹ ورک کی خرابی، براہ کرم دوبارہ کوشش کریں!", "دوبارہ کوشش کریں"],
    "vi": ["Tiếng Việt", "lỗi mạng, vui lòng thử lại!", "Thử lại"],
    "zh-Hans": ["简体中文", "网络错误，请重试！", "重试"],
    "zh-Hant-TW": ["中文（繁體，台灣）", "網路錯誤，請重試！", "重試"],
    "zu": ["isiZulu", "Iphutha lwenethiwekhi, sicela uzame futhi!", "Zama futhi"]
  };

  async function readDictionary(code, requiredText) {
    const url = new URL("locales/" + code + ".json", guide);
    for (let attempt = 0; attempt < 2; attempt++) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 8000);
      try {
        const response = await fetch(url, {cache: attempt ? "reload" : "no-cache", signal: controller.signal});
        if (!response.ok) throw new Error("Dictionary HTTP " + response.status);
        const dictionary = await response.json();
        if (requiredText.some(key => typeof dictionary?.[key] !== "string" || !dictionary[key].trim())) {
          throw new Error("Invalid language dictionary");
        }
        return dictionary;
      } catch (error) {
        if (attempt) throw error;
      } finally {
        clearTimeout(timer);
      }
      await new Promise(resolve => setTimeout(resolve, 350));
    }
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
    return picker;
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
    const languages = Object.fromEntries(Object.entries(recoveryLanguages).map(([code, labels]) => [code, labels[0]]));
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
    const translated = code !== "en" && code !== "zh-Hans";
    const picker = renderChooser(languages, code, page, translated ? languages[code] : code === "en" ? "Language" : "语言");
    if (!translated) return;

    const main = document.querySelector("main");
    const html = document.documentElement;
    const [name, errorMessage, retryLabel] = recoveryLanguages[code];
    const panel = document.createElement("section");
    panel.className = "locale-recovery";
    panel.lang = code;
    panel.dir = ["ar","he","fa","ur"].includes(code) ? "rtl" : "ltr";
    const progress = document.createElement("progress");
    progress.setAttribute("aria-label", name);
    panel.append(progress);
    main.before(panel);
    main.hidden = true;
    const originalTitle = document.title;
    const requiredText = ["Language", originalTitle, ...Array.from(
      main.querySelectorAll("h1, h2, p, .item span, .item small"),
      element => element.textContent.trim()
    ).filter(Boolean)];
    document.title = name;
    try {
      const dictionary = await readDictionary(code, requiredText);
      document.title = originalTitle;
      localize(dictionary, code);
      if (picker) picker.setAttribute("aria-label", dictionary.Language || name);
      main.hidden = false;
      panel.remove();
    } catch (error) {
      console.warn("Plant guide language loading failed", code, error);
      html.dataset.localeError = "true";
      panel.setAttribute("role", "alert");
      const message = document.createElement("p");
      message.textContent = errorMessage;
      const retry = document.createElement("button");
      retry.type = "button";
      retry.textContent = retryLabel;
      retry.addEventListener("click", () => location.reload());
      panel.replaceChildren(message, retry);
      if (picker) panel.append(picker);
    }
  }

  start();
})();
