# 多语言文章系统使用指南

## 概述

本系统为BirdAiSnap网站的50篇文章提供了完整的T1国家多语言支持，包括10种语言版本。

## 支持的语言

- **en** - English (英语) - 默认语言
- **zh** - 中文 (Chinese)
- **ja** - 日本語 (Japanese)
- **ko** - 한국어 (Korean)
- **de** - Deutsch (German)
- **fr** - Français (French)
- **es** - Español (Spanish)
- **it** - Italiano (Italian)
- **pt** - Português (Portuguese)
- **ru** - Русский (Russian)

## 文章分类

系统包含5个分类，每个分类10篇文章：

1. **birdwatching** - 观鸟指南 (10篇)
2. **scientific-wonders** - 科学奇迹 (10篇)
3. **pet-care** - 宠物护理 (10篇)
4. **ecology** - 生态学 (10篇)
5. **knowledge** - 知识中心 (10篇)

## URL结构

### 英语版本（默认）
```
/category/01-article.html
/category/02-article.html
...
/category/10-article.html
```

### 其他语言版本
```
/{language-code}/category/01-article.html
/{language-code}/category/02-article.html
...
/{language-code}/category/10-article.html
```

## 使用示例

### 1. 直接访问URL

```bash
# 英语版本
https://yoursite.com/scientific-wonders/01-article.html

# 中文版本
https://yoursite.com/zh/scientific-wonders/01-article.html

# 日语版本
https://yoursite.com/ja/scientific-wonders/01-article.html
```

### 2. App API调用

```javascript
// 获取单篇文章
const article = await BirdAiSnapAPI.getArticle('scientific-wonders', '01', 'zh');

// 获取分类文章列表
const articles = await BirdAiSnapAPI.getArticleList('birdwatching', 'ja');

// 获取所有文章
const allArticles = await BirdAiSnapAPI.getAllArticles('ko');

// 检测用户语言
const userLanguage = BirdAiSnapAPI.detectLanguage();
```

### 3. 语言切换

```javascript
// 使用语言路由器切换语言
languageRouter.switchLanguage('zh');

// 获取当前语言
const currentLang = languageRouter.currentLanguage;
```

## 回退机制

如果请求的语言版本不存在，系统会自动回退到英语版本：

1. 首先尝试加载请求的语言版本
2. 如果不存在，自动回退到英语版本
3. 如果英语版本也不存在，返回404错误

## 文件结构

```
website/
├── birdwatching/           # 英语版本观鸟文章
├── scientific-wonders/     # 英语版本科学文章
├── pet-care/              # 英语版本宠物护理文章
├── ecology/               # 英语版本生态学文章
├── knowledge/             # 英语版本知识文章
├── zh/                    # 中文版本
│   ├── birdwatching/
│   ├── scientific-wonders/
│   ├── pet-care/
│   ├── ecology/
│   └── knowledge/
├── ja/                    # 日语版本
├── ko/                    # 韩语版本
├── de/                    # 德语版本
├── fr/                    # 法语版本
├── es/                    # 西班牙语版本
├── it/                    # 意大利语版本
├── pt/                    # 葡萄牙语版本
├── ru/                    # 俄语版本
├── language-router.js     # 语言路由器
├── api-router.js         # API路由处理器
└── .htaccess             # URL重写规则
```

## 开发指南

### 添加新文章

1. 在对应的英语分类目录中创建文章
2. 运行生成脚本为所有语言创建版本：

```bash
python3 generate-multilingual-articles.py
```

### 添加新语言

1. 在 `language-router.js` 中添加语言代码
2. 在 `generate-multilingual-articles.py` 中添加翻译
3. 重新运行生成脚本

### 自定义翻译

编辑 `generate-multilingual-articles.py` 中的 `ARTICLE_TRANSLATIONS` 字典来自定义翻译内容。

## 性能优化

- 使用 `.htaccess` 进行URL重写和缓存控制
- 支持Gzip压缩
- 静态文件缓存策略
- 按需加载语言资源

## 统计信息

- **总文章数**: 500篇 (50篇 × 10种语言)
- **分类数**: 5个
- **语言数**: 10种
- **文件大小**: 约50MB (所有语言版本)

## 注意事项

1. 英语版本作为默认和回退语言
2. 所有多语言文件都包含语言切换功能
3. URL结构遵循SEO最佳实践
4. 支持移动端响应式设计
5. 包含完整的导航和页脚翻译

## 测试

可以通过以下方式测试多语言功能：

```bash
# 启动本地服务器
python3 start-server.py

# 访问不同语言版本
http://localhost:8000/scientific-wonders/01-article.html
http://localhost:8000/zh/scientific-wonders/01-article.html
http://localhost:8000/ja/scientific-wonders/01-article.html
```