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
    
    // 确定目标语言
    const targetLang = urlLang || savedLang;
    
    // 检查目标语言是否有效
    if (!languageMap[targetLang]) {
        return;
    }
    
    // 获取当前页面的语言代码
    const pathParts = path.split('/');
    const currentPageLang = pathParts[1];
    
    // 处理根目录页面（如 /pet-care.html?lang=ru）
    if (path.startsWith('/') && path.includes('.html') && !languageMap[currentPageLang]) {
        // 如果URL参数指定了非英文语言，检查对应语言版本是否存在
        if (urlLang && urlLang !== 'en' && languageMap[urlLang]) {
            const fileName = path.substring(1); // 去掉开头的 /
            
            // 检查是否为知识分类页面（这些页面可能没有多语言版本）
            const categoryPages = ['birdwatching.html', 'pet-care.html', 'scientific-wonders.html', 'ecology.html', 'cultural-symbolism.html', 'knowledge.html'];
            const isKnowledgePage = categoryPages.some(page => fileName === page);
            
            if (!isKnowledgePage) {
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
            } else {
                // 对于分类页面，只保存语言设置，不进行重定向
                localStorage.setItem('selectedLanguage', urlLang);
                
                // 移除URL中的lang参数以避免重复处理
                if (urlLang) {
                    const newParams = new URLSearchParams(window.location.search);
                    newParams.delete('lang');
                    const queryString = newParams.toString();
                    const newUrl = window.location.origin + path + (queryString ? '?' + queryString : '');
                    
                    // 使用replaceState来更新URL而不重新加载页面
                    window.history.replaceState({}, '', newUrl);
                }
            }
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

// 页面加载时执行语言检测
document.addEventListener('DOMContentLoaded', function() {
    handleLanguageRedirect();
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