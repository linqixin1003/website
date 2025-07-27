// 语言配置和翻译内容
const languages = {
    'en': { 
        name: 'English', 
        flag: '🇺🇸', 
        code: 'EN',
        translations: {
            'nav.home': 'Home',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
            'features.title': 'Core Features',
            'about.title': 'About BirdAiSnap',
            'contact.title': 'Contact Us'
        }
    },
    'zh': { 
        name: '中文', 
        flag: '🇨🇳', 
        code: 'ZH',
        translations: {
            'nav.home': '首页',
            'nav.features': '功能特色',
            'nav.about': '关于我们',
            'nav.contact': '联系我们',
            'hero.title': '智能识别，拍摄发现',
            'hero.description': 'BirdAiSnap是一款AI驱动的智能识别应用，帮助您快速识别周围的鸟类，探索自然世界的奥秘。',
            'hero.download': '立即下载',
            'hero.learn': '了解更多',
            'features.title': '核心功能',
            'about.title': '关于BirdAiSnap',
            'contact.title': '联系我们'
        }
    },
    'ko': { 
        name: '한국어', 
        flag: '🇰🇷', 
        code: 'KO',
        translations: {
            'nav.home': '홈',
            'nav.features': '기능',
            'nav.about': '소개',
            'nav.contact': '연락처',
            'hero.title': '지능형 인식, 촬영 및 발견',
            'hero.description': 'BirdAiSnap은 AI 기반 지능형 인식 애플리케이션으로, 주변 조류를 빠르게 식별하고 자연 세계의 신비를 탐구할 수 있게 해줍니다.',
            'hero.download': '지금 다운로드',
            'hero.learn': '더 알아보기',
            'features.title': '핵심 기능',
            'about.title': 'BirdAiSnap 소개',
            'contact.title': '연락처'
        }
    },
    'ja': { 
        name: '日本語', 
        flag: '🇯🇵', 
        code: 'JA',
        translations: {
            'nav.home': 'ホーム',
            'nav.features': '機能',
            'nav.about': '概要',
            'nav.contact': 'お問い合わせ',
            'hero.title': 'インテリジェント認識、撮影と発見',
            'hero.description': 'BirdAiSnapは、AI駆動のインテリジェント認識アプリケーションで、周囲の鳥類を迅速に識別し、自然界の神秘を解き明かします。',
            'hero.download': '今すぐダウンロード',
            'hero.learn': '詳細を見る',
            'features.title': 'コア機能',
            'about.title': 'BirdAiSnapについて',
            'contact.title': 'お問い合わせ'
        }
    },
    'de': { 
        name: 'Deutsch', 
        flag: '🇩🇪', 
        code: 'DE',
        translations: {
            'nav.home': 'Startseite',
            'nav.features': 'Funktionen',
            'nav.about': 'Über uns',
            'nav.contact': 'Kontakt',
            'hero.title': 'Intelligente Erkennung, Aufnahme und Entdeckung',
            'hero.description': 'BirdAiSnap ist eine KI-gestützte intelligente Erkennungsanwendung, die eine schnelle Vogelidentifikation in Ihrer Umgebung ermöglicht und die Geheimnisse der Natur enthüllt.',
            'hero.download': 'Jetzt herunterladen',
            'hero.learn': 'Mehr erfahren',
            'features.title': 'Kernfunktionen',
            'about.title': 'Über BirdAiSnap',
            'contact.title': 'Kontaktieren Sie uns'
        }
    },
    'fr': { 
        name: 'Français', 
        flag: '🇫🇷', 
        code: 'FR',
        translations: {
            'nav.home': 'Accueil',
            'nav.features': 'Fonctionnalités',
            'nav.about': 'À propos',
            'nav.contact': 'Contact',
            'hero.title': 'Reconnaissance intelligente, capture et découverte',
            'hero.description': 'BirdAiSnap est une application de reconnaissance intelligente alimentée par IA qui permet une identification rapide des oiseaux dans votre environnement tout en dévoilant les mystères du monde naturel.',
            'hero.download': 'Télécharger maintenant',
            'hero.learn': 'En savoir plus',
            'features.title': 'Fonctionnalités principales',
            'about.title': 'À propos de BirdAiSnap',
            'contact.title': 'Contactez-nous'
        }
    },
    'es': { 
        name: 'Español', 
        flag: '🇪🇸', 
        code: 'ES',
        translations: {
            'nav.home': 'Inicio',
            'nav.features': 'Características',
            'nav.about': 'Acerca de',
            'nav.contact': 'Contacto',
            'hero.title': 'Reconocimiento inteligente, captura y descubrimiento',
            'hero.description': 'BirdAiSnap es una aplicación de reconocimiento inteligente impulsada por IA que permite la identificación rápida de aves en su entorno mientras revela los misterios del mundo natural.',
            'hero.download': 'Descargar ahora',
            'hero.learn': 'Saber más',
            'features.title': 'Características principales',
            'about.title': 'Acerca de BirdAiSnap',
            'contact.title': 'Contáctanos'
        }
    },
    'it': { 
        name: 'Italiano', 
        flag: '🇮🇹', 
        code: 'IT',
        translations: {
            'nav.home': 'Home',
            'nav.features': 'Caratteristiche',
            'nav.about': 'Chi siamo',
            'nav.contact': 'Contatto',
            'hero.title': 'Riconoscimento intelligente, cattura e scoperta',
            'hero.description': 'BirdAiSnap è un\'applicazione di riconoscimento intelligente alimentata da IA che consente l\'identificazione rapida degli uccelli nel vostro ambiente rivelando i misteri del mondo naturale.',
            'hero.download': 'Scarica ora',
            'hero.learn': 'Scopri di più',
            'features.title': 'Caratteristiche principali',
            'about.title': 'Chi è BirdAiSnap',
            'contact.title': 'Contattaci'
        }
    },
    'pt': { 
        name: 'Português', 
        flag: '🇵🇹', 
        code: 'PT',
        translations: {
            'nav.home': 'Início',
            'nav.features': 'Recursos',
            'nav.about': 'Sobre',
            'nav.contact': 'Contato',
            'hero.title': 'Reconhecimento inteligente, captura e descoberta',
            'hero.description': 'BirdAiSnap é uma aplicação de reconhecimento inteligente alimentada por IA que permite identificação rápida de aves no seu ambiente enquanto revela os mistérios do mundo natural.',
            'hero.download': 'Baixar agora',
            'hero.learn': 'Saiba mais',
            'features.title': 'Recursos principais',
            'about.title': 'Sobre BirdAiSnap',
            'contact.title': 'Entre em contato'
        }
    },
    'ru': { 
        name: 'Русский', 
        flag: '🇷🇺', 
        code: 'RU',
        translations: {
            'nav.home': 'Главная',
            'nav.features': 'Функции',
            'nav.about': 'О нас',
            'nav.contact': 'Контакты',
            'hero.title': 'Интеллектуальное распознавание, съемка и открытие',
            'hero.description': 'BirdAiSnap - это приложение интеллектуального распознавания на основе ИИ, которое обеспечивает быструю идентификацию птиц в вашем окружении, раскрывая тайны природного мира.',
            'hero.download': 'Скачать сейчас',
            'hero.learn': 'Узнать больше',
            'features.title': 'Основные функции',
            'about.title': 'О BirdAiSnap',
            'contact.title': 'Свяжитесь с нами'
        }
    }
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

// 翻译页面内容
function translatePage(langCode) {
    const translations = languages[langCode].translations;
    if (!translations) return;

    // 翻译导航菜单
    const navItems = {
        'nav.home': 'nav a[href="#home"]',
        'nav.features': 'nav a[href="#features"]', 
        'nav.about': 'nav a[href="#about"]',
        'nav.contact': 'nav a[href="#contact"]'
    };

    Object.keys(navItems).forEach(key => {
        const element = document.querySelector(navItems[key]);
        if (element && translations[key]) {
            element.textContent = translations[key];
        }
    });

    // 翻译主要内容区域
    const contentSelectors = {
        'hero.title': '.hero h1, .hero-title',
        'hero.description': '.hero p, .hero-description', 
        'hero.download': '.download-btn, .btn-download',
        'hero.learn': '.learn-btn, .btn-learn',
        'features.title': '#features h2, .features-title',
        'about.title': '#about h2, .about-title',
        'contact.title': '#contact h2, .contact-title'
    };

    Object.keys(contentSelectors).forEach(key => {
        const elements = document.querySelectorAll(contentSelectors[key]);
        if (translations[key]) {
            elements.forEach(element => {
                if (element) {
                    element.textContent = translations[key];
                }
            });
        }
    });

    console.log('页面内容已翻译为:', languages[langCode].name);
}

// 切换语言
function switchLanguage(langCode) {
    if (!languages[langCode]) return;
    
    currentLang = langCode;
    
    // 更新下拉菜单显示
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = languages[langCode].code;
    }

    // 更新选中状态
    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.remove('active');
    });
    
    const activeOption = Array.from(document.querySelectorAll('.lang-option')).find(option => 
        option.innerHTML.includes(languages[langCode].code)
    );
    if (activeOption) {
        activeOption.classList.add('active');
    }

    // 关闭下拉菜单
    const dropdown = document.querySelector('.lang-dropdown');
    if (dropdown) {
        dropdown.classList.remove('active');
    }

    // 翻译页面内容
    translatePage(langCode);

    console.log('切换到语言:', languages[langCode].name);
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, creating language dropdown...');
    setTimeout(() => {
        createLanguageDropdown();
    }, 100);
});