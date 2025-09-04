// 通用语言检测和跳转脚本
// 用于所有文章页面的语言继承功能

// 语言映射表
const languageMap = {
    'en': 'en',
    'zh': 'zh', 
    'ko': 'ko',
    'ja': 'ja',
    'de': 'de',
    'fr': 'fr',
    'es': 'es',
    'it': 'it',
    'pt': 'pt',
    'ru': 'ru'
};

// 检测并处理语言跳转
function handleLanguageRedirect() {
    const path = window.location.pathname;
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    const savedLang = localStorage.getItem('selectedLanguage') || 'en';
    
    // 检查是否是语言子目录格式的URL
    const pathParts = path.split('/');
    const potentialLangCode = pathParts[1];
    
    // 如果是语言子目录格式，保持当前URL（不重定向）
    if (languageMap[potentialLangCode]) {
        // 保存语言设置
        localStorage.setItem('selectedLanguage', potentialLangCode);
        console.log(`Language detected from URL: ${potentialLangCode}`);
        // 不重定向，保持当前子目录格式的URL
        return;
    }
    
    // 如果URL中有lang参数，使用它并更新localStorage
    if (urlLang && languageMap[urlLang]) {
        localStorage.setItem('selectedLanguage', urlLang);
        console.log(`Language set from URL parameter: ${urlLang}`);
    } else {
        // 如果没有lang参数，但有保存的语言设置，添加lang参数
        if (savedLang && savedLang !== 'en') {
            const newUrl = window.location.origin + path + (path.includes('?') ? '&' : '?') + 'lang=' + savedLang;
            window.location.replace(newUrl);
            return;
        }
    }
}

// 检查文件是否存在
async function fileExists(url) {
    try {
        const response = await fetch(url, { method: 'HEAD' });
        return response.ok;
    } catch (error) {
        return false;
    }
}

// 页面加载时执行语言检测
document.addEventListener('DOMContentLoaded', function() {
    handleLanguageRedirect();
    
    // 为返回按钮添加语言参数（如果存在）
    const backButton = document.querySelector('.back-button');
    if (backButton) {
        backButton.addEventListener('click', function(e) {
            e.preventDefault();
            goBackWithLanguage();
        });
    }
    
    // 为所有内部链接添加当前语言参数
    addLanguageToLinks();
    
    // 为语言切换器添加事件监听
    setupLanguageSwitcher();
});

// 为返回按钮添加正确的语言路径
function goBackWithLanguage() {
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    let backUrl = '/knowledge.html';
    
    if (currentLang !== 'en') {
        backUrl += '?lang=' + currentLang;
    }
    
    window.location.href = backUrl;
}

// 设置语言切换器
function setupLanguageSwitcher() {
    const languageSwitchers = document.querySelectorAll('.language-switcher a, .language-selector a');
    if (languageSwitchers.length === 0) return;
    
    languageSwitchers.forEach(link => {
        link.addEventListener('click', async function(e) {
            e.preventDefault();
            const lang = this.getAttribute('data-lang');
            if (!lang || !languageMap[lang]) return;
            
            localStorage.setItem('selectedLanguage', lang);
            
            // 获取当前页面的基本路径（不包含语言代码）
            let basePath = window.location.pathname;
            const pathParts = basePath.split('/');
            if (pathParts.length > 1 && languageMap[pathParts[1]]) {
                pathParts.splice(1, 1); // 移除语言代码部分
                basePath = pathParts.join('/');
            }
            
            // 构建新的URL - 优先使用子目录格式
            let newUrl;
            if (lang === 'en') {
                newUrl = window.location.origin + basePath;
            } else {
                // 优先尝试子目录格式
                const subDirUrl = window.location.origin + '/' + lang + basePath;
                const exists = await fileExists(subDirUrl);
                if (exists) {
                    newUrl = subDirUrl;
                } else {
                    // 如果子目录格式不存在，尝试查询参数格式
                    newUrl = window.location.origin + basePath + (basePath.includes('?') ? '&' : '?') + 'lang=' + lang;
                }
            }
            
            window.location.href = newUrl;
        });
    });
}

// 为页面上的所有内部链接添加语言参数
function addLanguageToLinks() {
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    if (currentLang === 'en') return; // 英语是默认语言，不需要添加参数
    
    const links = document.querySelectorAll('a[href]');
    links.forEach(async link => {
        const href = link.getAttribute('href');
        
        // 只处理内部链接，不处理外部链接、锚点链接和已有lang参数的链接
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.includes('lang=')) {
            // 检查链接是否包含语言子目录
            const hrefParts = href.split('/');
            if (hrefParts.length > 1 && languageMap[hrefParts[1]]) {
                // 移除语言子目录
                hrefParts.splice(1, 1);
                let newHref = hrefParts.join('/');
                
                // 添加lang参数
                newHref += (newHref.includes('?') ? '&' : '?') + 'lang=' + currentLang;
                
                // 优先尝试子目录格式
                const subDirUrl = '/' + currentLang + hrefParts.join('/');
                const subDirExists = await fileExists(window.location.origin + subDirUrl);
                if (subDirExists) {
                    link.setAttribute('href', subDirUrl);
                } else {
                    // 如果子目录格式不存在，尝试查询参数格式
                    const exists = await fileExists(window.location.origin + newHref);
                    if (exists) {
                        link.setAttribute('href', newHref);
                    }
                }
            } else {
                // 构建查询参数格式的URL
                const newHref = href + (href.includes('?') ? '&' : '?') + 'lang=' + currentLang;
                
                // 优先尝试子目录格式
                const subDirUrl = '/' + currentLang + href;
                const subDirExists = await fileExists(window.location.origin + subDirUrl);
                if (subDirExists) {
                    link.setAttribute('href', subDirUrl);
                } else {
                    // 如果子目录格式不存在，尝试查询参数格式
                    const exists = await fileExists(window.location.origin + newHref);
                    if (exists) {
                        link.setAttribute('href', newHref);
                    }
                }
            }
        }
    });
}
