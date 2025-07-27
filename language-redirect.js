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
    }
})();