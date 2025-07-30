// 多语言路由系统
// 支持T1国家语言：英语、中文、日语、韩语、德语、法语、西班牙语、意大利语、葡萄牙语、俄语

const supportedLanguages = {
    'en': 'English',
    'zh': '中文',
    'ja': '日本語',
    'ko': '한국어',
    'de': 'Deutsch',
    'fr': 'Français',
    'es': 'Español',
    'it': 'Italiano',
    'pt': 'Português',
    'ru': 'Русский'
};

// 语言检测和路由
class LanguageRouter {
    constructor() {
        this.currentLanguage = this.detectLanguage();
        this.fallbackLanguage = 'en';
    }

    // 检测当前语言
    detectLanguage() {
        // 1. 从URL路径检测语言代码
        const pathLang = this.getLanguageFromPath();
        if (pathLang && supportedLanguages[pathLang]) {
            return pathLang;
        }

        // 2. 从localStorage获取用户偏好
        const savedLang = localStorage.getItem('preferred-language');
        if (savedLang && supportedLanguages[savedLang]) {
            return savedLang;
        }

        // 3. 从浏览器语言检测
        const browserLang = this.getBrowserLanguage();
        if (browserLang && supportedLanguages[browserLang]) {
            return browserLang;
        }

        // 4. 默认返回英语
        return this.fallbackLanguage;
    }

    // 从URL路径获取语言代码
    getLanguageFromPath() {
        const path = window.location.pathname;
        const matches = path.match(/\/([a-z]{2})\//);
        return matches ? matches[1] : null;
    }

    // 获取浏览器语言
    getBrowserLanguage() {
        const lang = navigator.language || navigator.userLanguage;
        return lang ? lang.substring(0, 2).toLowerCase() : null;
    }

    // 构建多语言URL
    buildLanguageUrl(basePath, language = null) {
        const lang = language || this.currentLanguage;
        
        // 如果是英语，不添加语言前缀
        if (lang === 'en') {
            return basePath;
        }
        
        // 其他语言添加语言前缀
        return `/${lang}${basePath}`;
    }

    // 获取文章的多语言URL
    getArticleUrl(category, articleId, language = null) {
        const lang = language || this.currentLanguage;
        const basePath = `/${category}/${articleId}.html`;
        
        if (lang === 'en') {
            return basePath;
        }
        
        return `/${lang}${basePath}`;
    }

    // 切换语言
    switchLanguage(newLanguage) {
        if (!supportedLanguages[newLanguage]) {
            console.warn(`Unsupported language: ${newLanguage}`);
            return;
        }

        // 保存用户偏好
        localStorage.setItem('preferred-language', newLanguage);
        
        // 获取当前页面路径（去除语言前缀）
        const currentPath = this.getCurrentBasePath();
        
        // 构建新的URL
        const newUrl = this.buildLanguageUrl(currentPath, newLanguage);
        
        // 跳转到新URL
        // 禁用强制重定向，尊重用户直接访问意图

        // window.location.href = newUrl;
    }

    // 获取当前页面的基础路径（去除语言前缀）
    getCurrentBasePath() {
        let path = window.location.pathname;
        
        // 移除语言前缀
        const langMatch = path.match(/^\/([a-z]{2})(\/.*)?$/);
        if (langMatch && supportedLanguages[langMatch[1]]) {
            path = langMatch[2] || '/';
        }
        
        return path;
    }

    // 检查文章是否存在指定语言版本
    async checkArticleExists(category, articleId, language) {
        const url = this.getArticleUrl(category, articleId, language);
        
        try {
            const response = await fetch(url, { method: 'HEAD' });
            return response.ok;
        } catch (error) {
            return false;
        }
    }

    // 加载文章内容（如果不存在则回退到英语）
    async loadArticle(category, articleId, language = null) {
        const lang = language || this.currentLanguage;
        
        // 首先尝试加载指定语言版本
        const exists = await this.checkArticleExists(category, articleId, lang);
        
        if (exists) {
            return this.getArticleUrl(category, articleId, lang);
        }
        
        // 如果不存在，回退到英语版本
        console.log(`Article not found in ${lang}, falling back to English`);
        return this.getArticleUrl(category, articleId, 'en');
    }

    // 获取语言选择器HTML
    getLanguageSelectorHTML() {
        const options = Object.entries(supportedLanguages)
            .map(([code, name]) => {
                const selected = code === this.currentLanguage ? 'selected' : '';
                return `<option value="${code}" ${selected}>${name}</option>`;
            })
            .join('');

        return `
            <select id="languageSelector" onchange="languageRouter.switchLanguage(this.value)">
                ${options}
            </select>
        `;
    }
}

// 全局实例
const languageRouter = new LanguageRouter();

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', function() {
    // 更新语言选择器
    const langSelector = document.getElementById('languageSelector');
    if (langSelector) {
        langSelector.value = languageRouter.currentLanguage;
    }
    
    // 更新当前语言显示
    const currentLangDisplay = document.getElementById('currentLang');
    if (currentLangDisplay) {
        currentLangDisplay.textContent = supportedLanguages[languageRouter.currentLanguage];
    }
});

// 导出供其他脚本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { LanguageRouter, supportedLanguages };
} else {
    window.LanguageRouter = LanguageRouter;
    window.languageRouter = languageRouter;
    window.supportedLanguages = supportedLanguages;
}