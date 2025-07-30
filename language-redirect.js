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
    
    // 如果URL中有lang参数，使用它并更新localStorage，然后重定向到纯路径
    if (urlLang && languageMap[urlLang]) {
        localStorage.setItem('selectedLanguage', urlLang);
        
        // 构建纯路径URL（移除查询参数）
        const pathParts = path.split('/');
        if (pathParts.length > 1) {
            pathParts[1] = urlLang;
            const newPath = pathParts.join('/');
            const newUrl = window.location.origin + newPath;
            
            // 重定向到纯路径版本
            // 禁用强制重定向，尊重用户直接访问意图

            // window.location.replace(newUrl);
            return;
        }
    }
    
    // 获取当前页面的语言代码
    const pathParts = path.split('/');
    const currentPageLang = pathParts[1];
    
    // 如果当前页面有有效的语言代码，更新localStorage
    if (languageMap[currentPageLang]) {
        // 用户直接访问了特定语言页面，更新localStorage为当前语言
        localStorage.setItem('selectedLanguage', currentPageLang);
        console.log(`Language updated to: ${currentPageLang}`);
    }
    
    // 不再进行自动语言跳转，尊重用户的直接访问意图
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
});

// 为返回按钮添加正确的语言路径
function goBackWithLanguage() {
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    let backUrl;
    
    if (currentLang === 'en') {
        backUrl = '/knowledge.html';
    } else {
        backUrl = `/${currentLang}/knowledge.html`;
    }
    
    // 禁用强制重定向，尊重用户直接访问意图

    
    // window.location.href = backUrl;
}
