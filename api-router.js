// API路由处理器 - 用于App访问
// 处理多语言文章请求和回退机制

class ApiRouter {
    constructor() {
        this.supportedLanguages = ['en', 'zh', 'ja', 'ko', 'de', 'fr', 'es', 'it', 'pt', 'ru'];
        this.categories = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge'];
        this.articlesPerCategory = 10;
    }

    // 处理文章请求
    async handleArticleRequest(category, articleId, language = 'en') {
        // 验证参数
        if (!this.categories.includes(category)) {
            throw new Error(`Invalid category: ${category}`);
        }

        const articleNum = parseInt(articleId);
        if (isNaN(articleNum) || articleNum < 1 || articleNum > this.articlesPerCategory) {
            throw new Error(`Invalid article ID: ${articleId}`);
        }

        // 标准化语言代码
        const lang = this.normalizeLanguageCode(language);
        
        // 构建文章路径
        const articlePath = this.buildArticlePath(category, articleId, lang);
        
        // 检查文章是否存在
        const exists = await this.checkArticleExists(articlePath);
        
        if (exists) {
            return {
                success: true,
                language: lang,
                path: articlePath,
                fallback: false
            };
        }

        // 如果不存在，回退到英语版本
        const fallbackPath = this.buildArticlePath(category, articleId, 'en');
        const fallbackExists = await this.checkArticleExists(fallbackPath);
        
        if (fallbackExists) {
            return {
                success: true,
                language: 'en',
                path: fallbackPath,
                fallback: true,
                originalLanguage: lang
            };
        }

        // 如果英语版本也不存在，返回错误
        throw new Error(`Article not found: ${category}/${articleId}`);
    }

    // 标准化语言代码
    normalizeLanguageCode(language) {
        if (!language) return 'en';
        
        const lang = language.toLowerCase().substring(0, 2);
        return this.supportedLanguages.includes(lang) ? lang : 'en';
    }

    // 构建文章路径
    buildArticlePath(category, articleId, language) {
        const paddedId = articleId.toString().padStart(2, '0');
        
        if (language === 'en') {
            return `/${category}/${paddedId}-article.html`;
        }
        
        return `/${language}/${category}/${paddedId}-article.html`;
    }

    // 检查文章是否存在
    async checkArticleExists(path) {
        try {
            const response = await fetch(path, { method: 'HEAD' });
            return response.ok;
        } catch (error) {
            return false;
        }
    }

    // 获取文章列表
    async getArticleList(category, language = 'en') {
        if (!this.categories.includes(category)) {
            throw new Error(`Invalid category: ${category}`);
        }

        const lang = this.normalizeLanguageCode(language);
        const articles = [];

        for (let i = 1; i <= this.articlesPerCategory; i++) {
            const articleId = i.toString().padStart(2, '0');
            
            try {
                const result = await this.handleArticleRequest(category, articleId, lang);
                articles.push({
                    id: articleId,
                    category: category,
                    language: result.language,
                    path: result.path,
                    fallback: result.fallback,
                    url: `${window.location.origin}${result.path}`
                });
            } catch (error) {
                console.warn(`Failed to load article ${category}/${articleId}:`, error.message);
            }
        }

        return articles;
    }

    // 获取所有分类的文章
    async getAllArticles(language = 'en') {
        const lang = this.normalizeLanguageCode(language);
        const allArticles = {};

        for (const category of this.categories) {
            try {
                allArticles[category] = await this.getArticleList(category, lang);
            } catch (error) {
                console.warn(`Failed to load category ${category}:`, error.message);
                allArticles[category] = [];
            }
        }

        return allArticles;
    }

    // 语言检测
    detectLanguage() {
        // 1. 从URL参数检测
        const urlParams = new URLSearchParams(window.location.search);
        const urlLang = urlParams.get('lang');
        if (urlLang) {
            return this.normalizeLanguageCode(urlLang);
        }

        // 2. 从localStorage检测
        const savedLang = localStorage.getItem('preferred-language');
        if (savedLang) {
            return this.normalizeLanguageCode(savedLang);
        }

        // 3. 从浏览器语言检测
        const browserLang = navigator.language || navigator.userLanguage;
        if (browserLang) {
            return this.normalizeLanguageCode(browserLang);
        }

        // 4. 默认英语
        return 'en';
    }

    // 生成API响应
    generateApiResponse(data, success = true, message = '') {
        return {
            success: success,
            message: message,
            timestamp: new Date().toISOString(),
            data: data
        };
    }
}

// 全局API路由实例
const apiRouter = new ApiRouter();

// 导出供其他脚本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ApiRouter;
} else {
    window.ApiRouter = ApiRouter;
    window.apiRouter = apiRouter;
}

// 示例API端点
window.addEventListener('DOMContentLoaded', function() {
    // 为App提供的API端点示例
    window.BirdAiSnapAPI = {
        // 获取文章
        async getArticle(category, articleId, language) {
            try {
                const result = await apiRouter.handleArticleRequest(category, articleId, language);
                return apiRouter.generateApiResponse(result);
            } catch (error) {
                return apiRouter.generateApiResponse(null, false, error.message);
            }
        },

        // 获取文章列表
        async getArticleList(category, language) {
            try {
                const result = await apiRouter.getArticleList(category, language);
                return apiRouter.generateApiResponse(result);
            } catch (error) {
                return apiRouter.generateApiResponse(null, false, error.message);
            }
        },

        // 获取所有文章
        async getAllArticles(language) {
            try {
                const result = await apiRouter.getAllArticles(language);
                return apiRouter.generateApiResponse(result);
            } catch (error) {
                return apiRouter.generateApiResponse(null, false, error.message);
            }
        },

        // 检测语言
        detectLanguage() {
            return apiRouter.detectLanguage();
        },

        // 获取支持的语言列表
        getSupportedLanguages() {
            return apiRouter.supportedLanguages;
        },

        // 获取分类列表
        getCategories() {
            return apiRouter.categories;
        }
    };
});