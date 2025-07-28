// 语言重定向脚本 - 西班牙语版本
(function() {
    // 检查当前页面语言是否与用户偏好匹配
    const currentLang = 'es';
    const savedLang = localStorage.getItem('selectedLanguage') || 'en';
    
    // 如果用户偏好的语言与当前页面语言不匹配，进行重定向
    if (savedLang !== currentLang && savedLang !== 'es') {
        const currentPath = window.location.pathname;
        const pathParts = currentPath.split('/').filter(part => part.length > 0);
        
        if (pathParts.length > 1 && pathParts[0] === 'es') {
            // 替换语言代码
            pathParts[0] = savedLang;
            const newPath = '/' + pathParts.join('/');
            const newUrl = window.location.origin + newPath + window.location.search;
            
            // 重定向到用户偏好的语言版本
            window.location.href = newUrl;
        }
    }
})();