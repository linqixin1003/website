(function() {
    const LANGUAGES = {
        'en': { name: 'English', flag: '🇺🇸' },
        'zh': { name: '中文', flag: '🇨🇳' },
        'es': { name: 'Español', flag: '🇪🇸' },
        'fr': { name: 'Français', flag: '🇫🇷' },
        'de': { name: 'Deutsch', flag: '🇩🇪' },
        'it': { name: 'Italiano', flag: '🇮🇹' },
        'pt': { name: 'Português', flag: '🇵🇹' },
        'ja': { name: '日本語', flag: '🇯🇵' },
        'ko': { name: '한국어', flag: '🇰🇷' },
        'ru': { name: 'Русский', flag: '🇷🇺' }
    };

    const DEFAULT_LANG = 'en';
    const STORAGE_KEY = 'happy_poop_lang';

    function getStoredLanguage() {
        return localStorage.getItem(STORAGE_KEY) || DEFAULT_LANG;
    }

    function setStoredLanguage(lang) {
        localStorage.setItem(STORAGE_KEY, lang);
        updateLinks(lang);
        updateSwitcherUI(lang);
    }

    function updateLinks(lang) {
        const links = document.querySelectorAll('a[href*="still-alive-tips/"]');
        links.forEach(link => {
            const href = link.getAttribute('href');
            let newHref = href;
            
            // Check if it already has a language prefix
            const match = href.match(/^([a-z]{2})\/still-alive-tips\//);
            
            if (match) {
                // Has prefix (e.g. zh/still-alive-tips/...)
                if (lang === 'en') {
                    // Remove prefix for English (assuming English is at root still-alive-tips/)
                    newHref = href.replace(/^([a-z]{2})\//, '');
                } else {
                    // Replace prefix with new lang
                    newHref = href.replace(/^([a-z]{2})\//, `${lang}/`);
                }
            } else if (href.startsWith('still-alive-tips/')) {
                // No prefix (English/Root)
                if (lang !== 'en') {
                    // Add prefix
                    newHref = `${lang}/${href}`;
                }
                // If lang is en, leave as is
            }
            
            link.setAttribute('href', newHref);
        });
    }

    function createSwitcherUI() {
        const currentLang = getStoredLanguage();
        
        const container = document.createElement('div');
        container.className = 'hp-lang-switcher';
        
        const button = document.createElement('button');
        button.className = 'hp-lang-btn';
        button.innerHTML = `<span class="hp-lang-flag">${LANGUAGES[currentLang].flag}</span> <span class="hp-lang-code">${currentLang.toUpperCase()}</span>`;
        
        const dropdown = document.createElement('div');
        dropdown.className = 'hp-lang-dropdown';
        
        Object.keys(LANGUAGES).forEach(lang => {
            const item = document.createElement('div');
            item.className = 'hp-lang-item';
            if (lang === currentLang) item.classList.add('active');
            item.innerHTML = `<span class="hp-lang-flag">${LANGUAGES[lang].flag}</span> ${LANGUAGES[lang].name}`;
            item.onclick = () => {
                setStoredLanguage(lang);
                dropdown.classList.remove('show');
            };
            dropdown.appendChild(item);
        });
        
        button.onclick = (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('show');
        };
        
        document.addEventListener('click', () => {
            dropdown.classList.remove('show');
        });
        
        container.appendChild(button);
        container.appendChild(dropdown);
        
        // Check for mobile header placement
        const mobileHeader = document.querySelector('.header-top');
        let isMobile = false;
        
        if (mobileHeader) {
            isMobile = true;
            mobileHeader.appendChild(container);
        } else {
            document.body.appendChild(container);
        }
        
        // Add Styles
        const style = document.createElement('style');
        style.textContent = `
            .hp-lang-switcher {
                font-family: 'Inter', sans-serif;
                position: relative;
                z-index: 1000;
            }
            
            /* Fixed positioning for non-mobile pages */
            body > .hp-lang-switcher {
                position: fixed;
                top: 20px;
                right: 20px;
            }
            
            .hp-lang-btn {
                background: white;
                border: 1px solid rgba(0,0,0,0.1);
                padding: 8px 12px;
                border-radius: 20px;
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 6px;
                font-weight: 600;
                color: #1C1C1E;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                transition: all 0.2s ease;
                font-size: 13px;
            }
            
            /* Mobile specific button style */
            .header-top .hp-lang-btn {
                background: rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
                color: white;
                box-shadow: none;
                backdrop-filter: blur(4px);
            }
            
            .header-top .hp-lang-btn:hover {
                background: rgba(255,255,255,0.3);
            }
            
            .hp-lang-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(0,0,0,0.12);
            }
            
            .hp-lang-dropdown {
                position: absolute;
                top: 100%;
                right: 0;
                margin-top: 8px;
                background: white;
                border-radius: 16px;
                padding: 8px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.15);
                display: none;
                min-width: 160px;
                max-height: 400px;
                overflow-y: auto;
                z-index: 1001;
            }
            
            /* Ensure dropdown text is dark even in mobile header */
            .header-top .hp-lang-dropdown {
                color: #1C1C1E;
            }
            
            .hp-lang-dropdown.show {
                display: block;
                animation: hpFadeIn 0.2s ease;
            }
            
            @keyframes hpFadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .hp-lang-item {
                padding: 10px 16px;
                border-radius: 10px;
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 14px;
                color: #1C1C1E;
                transition: background 0.2s;
            }
            
            .hp-lang-item:hover {
                background: #F2F2F7;
            }
            
            .hp-lang-item.active {
                background: #F2F2F7;
                font-weight: 600;
                color: #7C3AED;
            }
            
            .hp-lang-flag {
                font-size: 18px;
            }
        `;
        document.head.appendChild(style);
    }

    function updateSwitcherUI(lang) {
        const btn = document.querySelector('.hp-lang-btn');
        if (btn) {
            btn.innerHTML = `<span class="hp-lang-flag">${LANGUAGES[lang].flag}</span> <span class="hp-lang-code">${lang.toUpperCase()}</span>`;
        }
        
        const items = document.querySelectorAll('.hp-lang-item');
        items.forEach(item => {
            if (item.textContent.includes(LANGUAGES[lang].name)) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    }

    // Initialize
    document.addEventListener('DOMContentLoaded', () => {
        createSwitcherUI();
        updateLinks(getStoredLanguage());
    });
})();
