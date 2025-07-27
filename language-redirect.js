<<<<<<< HEAD
// 语言重定向脚本
(function() {
    // 获取URL参数
    function getUrlParameter(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    }
    
    // 支持的语言列表
    const supportedLanguages = ['ko', 'de', 'en', 'es', 'fr', 'it', 'ja', 'pt', 'ru', 'zh'];
    
    // 获取lang参数
    const langParam = getUrlParameter('lang');
    
    if (langParam && supportedLanguages.includes(langParam)) {
        // 获取当前页面路径
        const currentPath = window.location.pathname;
        const currentFilename = currentPath.split('/').pop();
        
        // 检查是否已经在目标语言目录中
        const pathParts = currentPath.split('/');
        const currentLangInPath = pathParts[1];
        
        // 如果当前路径已经包含目标语言，则不重定向
        if (currentLangInPath === langParam) {
            return;
        }
        
        // 构建新的URL
        let newUrl;
        if (currentPath === '/' || currentPath === '/index.html') {
            // 主页重定向
            newUrl = `/${langParam}/index.html`;
        } else {
            // 其他页面重定向
            newUrl = `/${langParam}/${currentFilename}`;
        }
        
        // 保留其他查询参数（除了lang参数）
        const urlParams = new URLSearchParams(window.location.search);
        urlParams.delete('lang');
        const remainingParams = urlParams.toString();
        
        if (remainingParams) {
            newUrl += '?' + remainingParams;
        }
        
        // 执行重定向
        window.location.replace(newUrl);
=======
// 通用语言检测和跳转脚本
// 支持URL参数形式的语言切换重定向到对应语言目录

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
    
    // 检查是否从knowledge.html跳转过来，如果是则继承其语言设置
    const referrer = document.referrer;
    let inheritedLang = null;
    if (referrer && referrer.includes('knowledge.html')) {
        try {
            // 从referrer URL中提取语言参数
            const referrerUrl = new URL(referrer);
            inheritedLang = referrerUrl.searchParams.get('lang') || savedLang;
        } catch (e) {
            inheritedLang = savedLang;
        }
    }
    
    // 确定目标语言：URL参数 > 继承语言 > 保存的语言
    const targetLang = urlLang || inheritedLang || savedLang;
    
    // 检查目标语言是否有效
    if (!languageMap[targetLang]) {
        return;
>>>>>>> ab010a4f01f19276ffe9ff04457e6acaf3a295ad
    }
    
    // 获取当前页面的语言代码
    const pathParts = path.split('/');
    const currentPageLang = pathParts[1];
    
    // 处理根目录页面（如 /pet-care.html?lang=ru）
    if (path.startsWith('/') && path.includes('.html') && !languageMap[currentPageLang]) {
        const fileName = path.substring(1); // 去掉开头的 /
        
        // 检查是否为知识分类页面
        const categoryPages = ['birdwatching.html', 'pet-care.html', 'scientific-wonders.html', 'ecology.html', 'cultural-symbolism.html', 'knowledge.html'];
        const isKnowledgePage = categoryPages.some(page => fileName === page);
        
        if (isKnowledgePage) {
            // 对于分类页面，应用语言设置
            const finalLang = targetLang;
            
            // 保存语言设置
            localStorage.setItem('selectedLanguage', finalLang);
            
            // 如果有URL参数，移除它以避免重复处理
            if (urlLang) {
                const newParams = new URLSearchParams(window.location.search);
                newParams.delete('lang');
                const queryString = newParams.toString();
                const newUrl = window.location.origin + path + (queryString ? '?' + queryString : '');
                
                // 使用replaceState来更新URL而不重新加载页面
                window.history.replaceState({}, '', newUrl);
            }
            
            // 应用语言设置
            applyLanguageSettings(finalLang);
            
        } else if (urlLang && urlLang !== 'en' && languageMap[urlLang]) {
            // 对于非分类页面，尝试重定向到语言目录
            const newPath = '/' + urlLang + '/' + fileName;
            
            // 移除lang参数，因为已经通过路径表示语言
            const newParams = new URLSearchParams(window.location.search);
            newParams.delete('lang');
            const queryString = newParams.toString();
            const newUrl = window.location.origin + newPath + (queryString ? '?' + queryString : '');
            
            // 保存语言设置并跳转
            localStorage.setItem('selectedLanguage', urlLang);
            window.location.replace(newUrl);
            return;
        }
    }
    
    // 处理已在语言目录中的页面
    if (languageMap[currentPageLang]) {
        // 如果当前页面语言与目标语言不匹配，进行跳转
        if (currentPageLang !== targetLang) {
            // 构建新的URL路径
            pathParts[1] = targetLang;
            const newPath = pathParts.join('/');
            
            // 保持URL参数
            const newUrl = window.location.origin + newPath + window.location.search;
            
            // 执行跳转
            window.location.replace(newUrl);
            return;
        }
    }
    
    // 如果URL中有语言参数，保存到localStorage
    if (urlLang && languageMap[urlLang]) {
        localStorage.setItem('selectedLanguage', urlLang);
    }
}

// 应用语言设置的函数
function applyLanguageSettings(lang) {
    // 确保语言有效
    if (!languageMap[lang]) {
        lang = 'en';
    }
    
    // 延迟应用语言设置，确保页面完全加载
    setTimeout(() => {
        // 应用翻译
        if (window.translatePage && typeof window.translatePage === 'function') {
            window.translatePage(lang);
        }
        
        // 更新语言切换器显示
        updateLanguageSwitcher(lang);
        
        // 触发自定义事件，通知其他脚本语言已更改
        const event = new CustomEvent('languageChanged', { detail: { language: lang } });
        document.dispatchEvent(event);
        
        console.log('语言设置已应用:', lang);
    }, 300);
}

// 更新语言切换器显示
function updateLanguageSwitcher(lang) {
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement && window.languages && window.languages[lang]) {
        currentLangElement.textContent = window.languages[lang].code;
    }
    
    // 更新选中状态
    const langOptions = document.querySelectorAll('.lang-option');
    langOptions.forEach(option => {
        option.classList.remove('active');
        if (window.languages && window.languages[lang] && option.innerHTML.includes(window.languages[lang].code)) {
            option.classList.add('active');
        }
    });
}

// 检查分类页面是否需要应用语言设置
function checkCategoryPageLanguage() {
    const path = window.location.pathname;
    const fileName = path.split('/').pop();
    const categoryPages = ['scientific-wonders.html', 'pet-care.html', 'ecology.html', 'cultural-symbolism.html'];
    
    if (categoryPages.includes(fileName)) {
        const savedLang = localStorage.getItem('selectedLanguage') || 'en';
        
        // 检查是否从knowledge.html跳转过来
        const referrer = document.referrer;
        let inheritedLang = null;
        if (referrer && referrer.includes('knowledge.html')) {
            try {
                const referrerUrl = new URL(referrer);
                inheritedLang = referrerUrl.searchParams.get('lang');
            } catch (e) {
                // 忽略错误
            }
        }
        
        const targetLang = inheritedLang || savedLang;
        
        if (targetLang && targetLang !== 'en' && languageMap[targetLang]) {
            console.log('检测到分类页面，应用语言设置:', targetLang);
            localStorage.setItem('selectedLanguage', targetLang);
            applyLanguageSettings(targetLang);
        }
    }
}

// 页面加载时执行语言检测
document.addEventListener('DOMContentLoaded', function() {
    handleLanguageRedirect();
    
    // 额外检查分类页面的语言设置
    setTimeout(() => {
        checkCategoryPageLanguage();
    }, 100);
});

// 为返回按钮添加语言参数
function goBackWithLanguage() {
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    const backUrl = 'knowledge.html?lang=' + currentLang;
    window.location.href = backUrl;
}

// 如果页面有返回按钮，为其添加点击事件
document.addEventListener('DOMContentLoaded', function() {
    const backButton = document.querySelector('.back-button');
    if (backButton) {
        backButton.addEventListener('click', function(e) {
            e.preventDefault();
            goBackWithLanguage();
        });
    }
});