// 语言重定向脚本
(function() {
    // 获取URL参数
    function getUrlParameter(name) {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
        var results = regex.exec(location.search);
        return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
    }
    
    // 语言代码映射
    const languageMap = {
        'ko': 'ko',
        'de': 'de', 
        'en': 'en',
        'es': 'es',
        'fr': 'fr',
        'it': 'it',
        'ja': 'ja',
        'pt': 'pt',
        'ru': 'ru',
        'zh': 'zh'
    };
    
    // 获取当前页面名称
    function getCurrentPageName() {
        const path = window.location.pathname;
        const fileName = path.split('/').pop();
        return fileName || 'index.html';
    }
    
    // 执行重定向
    function performRedirect() {
        const langParam = getUrlParameter('lang');
        
        if (langParam && languageMap[langParam]) {
            const currentPage = getCurrentPageName();
            const currentPath = window.location.pathname;
            
            // 检查是否已经在对应语言目录中
            if (!currentPath.startsWith('/' + langParam + '/')) {
                // 构建新的URL
                let newUrl;
                if (currentPage === 'index.html' || currentPage === '') {
                    newUrl = '/' + langParam + '/';
                } else {
                    newUrl = '/' + langParam + '/' + currentPage;
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
        }
    }
    
    // 页面加载完成后执行重定向
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', performRedirect);
    } else {
        performRedirect();
    }
})();