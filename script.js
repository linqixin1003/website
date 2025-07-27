// 语言配置
const languages = {
    'en': { name: 'English', flag: '🇺🇸', code: 'EN' },
    'zh': { name: '中文', flag: '🇨🇳', code: 'ZH' },
    'ko': { name: '한국어', flag: '🇰🇷', code: 'KO' },
    'ja': { name: '日本語', flag: '🇯🇵', code: 'JA' },
    'de': { name: 'Deutsch', flag: '🇩🇪', code: 'DE' },
    'fr': { name: 'Français', flag: '🇫🇷', code: 'FR' },
    'es': { name: 'Español', flag: '🇪🇸', code: 'ES' },
    'it': { name: 'Italiano', flag: '🇮🇹', code: 'IT' },
    'pt': { name: 'Português', flag: '🇵🇹', code: 'PT' },
    'ru': { name: 'Русский', flag: '🇷🇺', code: 'RU' }
};

let currentLang = 'en';

// 创建语言下拉菜单
function createLanguageDropdown() {
    const languageSwitcher = document.querySelector('.language-switcher');
    if (!languageSwitcher) {
        console.log('Language switcher container not found');
        return;
    }

    const dropdown = document.createElement('div');
    dropdown.className = 'lang-dropdown';

    const button = document.createElement('button');
    button.className = 'lang-btn';
    button.innerHTML = `
        <span class="lang-icon">🌐</span>
        <span class="lang-text">Language</span>
        <span id="currentLang">${languages[currentLang].code}</span>
        <span class="dropdown-arrow">▼</span>
    `;

    const menu = document.createElement('div');
    menu.className = 'lang-menu';

    Object.keys(languages).forEach(langCode => {
        const option = document.createElement('div');
        option.className = `lang-option ${langCode === currentLang ? 'active' : ''}`;
        option.innerHTML = `
            <span class="flag">${languages[langCode].flag}</span>
            <span class="name">${languages[langCode].name}</span>
            <span class="code">${languages[langCode].code}</span>
        `;
        option.addEventListener('click', () => switchLanguage(langCode));
        menu.appendChild(option);
    });

    dropdown.appendChild(button);
    dropdown.appendChild(menu);
    languageSwitcher.appendChild(dropdown);

    button.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdown.classList.toggle('active');
    });

    document.addEventListener('click', () => {
        dropdown.classList.remove('active');
    });

    console.log('Language dropdown created successfully');
}

// 切换语言
function switchLanguage(langCode) {
    if (!languages[langCode]) return;
    
    currentLang = langCode;
    
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = languages[langCode].code;
    }

    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.remove('active');
    });
    
    const activeOption = Array.from(document.querySelectorAll('.lang-option')).find(option => 
        option.innerHTML.includes(languages[langCode].code)
    );
    if (activeOption) {
        activeOption.classList.add('active');
    }

    const dropdown = document.querySelector('.lang-dropdown');
    if (dropdown) {
        dropdown.classList.remove('active');
    }

    console.log('切换到语言:', languages[langCode].name);
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, creating language dropdown...');
    setTimeout(() => {
        createLanguageDropdown();
    }, 100);
});