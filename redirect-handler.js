// 通用重定向处理脚本
(function() {
    'use strict';
    
    // 检查当前URL是否需要重定向
    function checkAndRedirect() {
        const currentPath = window.location.pathname;
        const urlParams = new URLSearchParams(window.location.search);
        const lang = urlParams.get('lang');
        
        // 如果没有语言参数，不需要重定向
        if (!lang) return;
        
        // 定义需要重定向的路径模式
        const redirectPatterns = [
            { pattern: /^\/knowledge\/(.+)\.html$/, target: '/{lang}/knowledge/{file}.html' },
            { pattern: /^\/birdwatching\/(.+)\.html$/, target: '/{lang}/birdwatching/{file}.html' },
            { pattern: /^\/pet-care\/(.+)\.html$/, target: '/{lang}/pet-care/{file}.html' },
            { pattern: /^\/ecology\/(.+)\.html$/, target: '/{lang}/ecology/{file}.html' },
            { pattern: /^\/scientific-wonders\/(.+)\.html$/, target: '/{lang}/scientific-wonders/{file}.html' },
            { pattern: /^\/knowledge\.html$/, target: '/{lang}/knowledge.html' },
            { pattern: /^\/birdwatching\.html$/, target: '/{lang}/birdwatching.html' },
            { pattern: /^\/pet-care\.html$/, target: '/{lang}/pet-care.html' },
            { pattern: /^\/ecology\.html$/, target: '/{lang}/ecology.html' },
            { pattern: /^\/scientific-wonders\.html$/, target: '/{lang}/scientific-wonders.html' }
        ];
        
        // 检查每个模式
        for (const { pattern, target } of redirectPatterns) {
            const match = currentPath.match(pattern);
            if (match) {
                let newUrl = target.replace('{lang}', lang);
                if (match[1]) {
                    newUrl = newUrl.replace('{file}', match[1]);
                }
                
                console.log(`重定向: ${currentPath}?lang=${lang} -> ${newUrl}`);
                window.location.replace(newUrl);
                return;
            }
        }
    }
    
    // 页面加载时检查重定向
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkAndRedirect);
    } else {
        checkAndRedirect();
    }
})();