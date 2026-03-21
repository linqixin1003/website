
function getLanguageFromUrl() {
    const path = window.location.pathname;
    const parts = path.split("/");
    // Check if first part is a lang code
    if (parts.length > 1 && ["de", "fr", "es", "it", "pt", "ja", "ko", "ru", "zh"].includes(parts[1])) {
        return parts[1];
    }
    return "en";
}

function updateArticleLinks() {
    const lang = getLanguageFromUrl();
    if (lang === "en") return; // Default links are already English

    const cards = document.querySelectorAll(".read-link");
    cards.forEach(link => {
        const href = link.getAttribute("href");
        if (href && href.startsWith("still-alive-tips/")) {
            // Modify link to point to language specific version
            // from: still-alive-tips/article.html
            // to: lang/still-alive-tips/article.html
            link.setAttribute("href", lang + "/" + href);
        }
    });
}

// Simple language switcher logic could go here if UI element existed
document.addEventListener("DOMContentLoaded", updateArticleLinks);

