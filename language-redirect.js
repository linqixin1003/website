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
    
    // 确定目标语言
    const targetLang = urlLang || savedLang;
    
    // 检查目标语言是否有效
    if (!languageMap[targetLang]) {
        return;
    }
    
    // 获取当前页面的语言代码
    const pathParts = path.split('/');
    const currentPageLang = pathParts[1];
    
    // 如果当前页面语言与目标语言不匹配，进行跳转
    if (currentPageLang !== targetLang && languageMap[currentPageLang]) {
        // 构建新的URL路径
        pathParts[1] = targetLang;
        const newPath = pathParts.join('/');
        
        // 保持URL参数
        const newUrl = window.location.origin + newPath + window.location.search;
        
        // 执行跳转
        window.location.replace(newUrl);
        return;
    }
    
    // 如果URL中没有语言参数但localStorage中有，更新localStorage
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