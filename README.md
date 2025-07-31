# BirdAiSnap - 多语言鸟类观察学习平台

## 🌟 项目简介

BirdAiSnap是一个专业的多语言鸟类观察学习平台，为全球鸟类爱好者提供高质量的教育内容和实用指导。

## 🌍 多语言支持

我们的平台支持8种语言，为全球用户提供母语级学习体验：

- 🇺🇸 **英语** - 专业增强版本
- 🇨🇳 **中文** - 原版完整内容
- 🇰🇷 **韩语** - 高质量翻译
- 🇫🇷 **法语** - 专业级翻译
- 🇩🇪 **德语** - 专业级翻译
- 🇯🇵 **日语** - 专业级翻译
- 🇵🇹 **葡萄牙语** - 完整翻译
- 🇷🇺 **俄语** - 基础翻译

## 📚 内容模块

### 🔍 鸟类观察 (Birdwatching)
- 入门指南
- 必备设备
- 识别技巧
- 最佳观察地点
- 季节性指导
- 摄影技巧
- 行为观察
- 鸣声识别
- 伦理与保护
- 记录保持

### 🌿 生态学 (Ecology)
- 栖息地与生态系统
- 食物网与食物链
- 迁徙模式
- 繁殖生态学
- 气候变化影响
- 城市生态学
- 保护生物学
- 岛屿生物地理学
- 授粉与种子传播
- 群落动态

### 🐦 宠物护理 (Pet Care)
- 选择合适的鸟类
- 营养与喂养
- 住房与环境
- 健康与兽医护理
- 训练与行为
- 繁殖与生殖
- 紧急急救
- 季节性护理
- 丰富活动
- 老年鸟类护理

### 🔬 科学奇观 (Scientific Wonders)
- 鸟类飞行力学
- 磁导航
- 蜂鸟力学
- 鸟类智能
- 羽毛结构
- 鸟类视觉
- 蛋发育
- 鸟类交流
- 迁徙生理学
- 生物力学

## 🚀 部署信息

### GitHub Pages 自动部署
本网站已配置 GitHub Actions 自动部署到 GitHub Pages：

- **部署地址**: `https://[你的用户名].github.io/website/`
- **自动部署**: 每次推送到 `main` 或 `master` 分支时自动更新
- **CDN加速**: 全球CDN分发，访问速度快
- **HTTPS支持**: 自动启用HTTPS安全连接

### 部署步骤

1. **推送代码到GitHub**:
   ```bash
   git add .
   git commit -m "Deploy website"
   git push origin main
   ```

2. **启用GitHub Pages**:
   - 进入仓库设置 (Settings)
   - 找到 "Pages" 选项
   - 在 "Source" 中选择 "GitHub Actions"
   - 保存设置

3. **查看部署状态**:
   - 在仓库的 "Actions" 标签页查看部署进度
   - 部署成功后，网站将在几分钟内生效

### 本地开发
```bash
# 克隆仓库
git clone https://github.com/[你的用户名]/website.git
cd website

# 启动本地服务器
python3 -m http.server 8000

# 访问网站
open http://localhost:8000
```

### URL重定向系统
网站配置了智能重定向系统，支持以下URL格式：

**旧格式** (自动重定向):
- `https://birdid.net/knowledge/01-beginners-guide.html?lang=en`
- `https://birdid.net/birdwatching/02-essential-equipment.html?lang=zh`

**新格式** (推荐使用):
- `https://birdid.net/en/knowledge/01-beginners-guide.html`
- `https://birdid.net/zh/birdwatching/02-essential-equipment.html`

重定向规则：
- 支持所有8种语言 (en, zh, ko, ja, de, fr, es, it, pt, ru)
- 覆盖所有内容模块 (knowledge, birdwatching, pet-care, ecology, scientific-wonders)
- 自动301重定向，SEO友好

### 自定义域名
已配置自定义域名：`birdid.net`
- DNS记录已正确配置
- 支持HTTPS安全连接
- 全球CDN加速访问
# BirdAiSnap - 多语言鸟类观察学习平台

## 🌟 项目简介

BirdAiSnap是一个专业的多语言鸟类观察学习平台，为全球鸟类爱好者提供高质量的教育内容和实用指导。

## 🌍 多语言支持

我们的平台支持8种语言，为全球用户提供母语级学习体验：

- 🇺🇸 **英语** - 专业增强版本
- 🇨🇳 **中文** - 原版完整内容
- 🇰🇷 **韩语** - 高质量翻译
- 🇫🇷 **法语** - 专业级翻译
- 🇩🇪 **德语** - 专业级翻译
- 🇯🇵 **日语** - 专业级翻译
- 🇵🇹 **葡萄牙语** - 完整翻译
- 🇷🇺 **俄语** - 基础翻译

## 📚 内容模块

### 🔍 鸟类观察 (Birdwatching)
- 入门指南
- 必备设备
- 识别技巧
- 最佳观察地点
- 季节性指导
- 摄影技巧
- 行为观察
- 鸣声识别
- 伦理与保护
- 记录保持

### 🌿 生态学 (Ecology)
- 栖息地与生态系统
- 食物网与食物链
- 迁徙模式
- 繁殖生态学
- 气候变化影响
- 城市生态学
- 保护生物学
- 岛屿生物地理学
- 授粉与种子传播
- 群落动态

### 🐦 宠物护理 (Pet Care)
- 选择合适的鸟类
- 营养与喂养
- 住房与环境
- 健康与兽医护理
- 训练与行为
- 繁殖与生殖
- 紧急急救
- 季节性护理
- 丰富活动
- 老年鸟类护理

### 🔬 科学奇观 (Scientific Wonders)
- 鸟类飞行力学
- 磁导航
- 蜂鸟力学
- 鸟类智能
- 羽毛结构
- 鸟类视觉
- 蛋发育
- 鸟类交流
- 迁徙生理学
- 生物力学

## 🚀 部署信息

### GitHub Pages 自动部署
本网站已配置 GitHub Actions 自动部署到 GitHub Pages：

- **部署地址**: `https://[你的用户名].github.io/website/`
- **自动部署**: 每次推送到 `main` 或 `master` 分支时自动更新
- **CDN加速**: 全球CDN分发，访问速度快
- **HTTPS支持**: 自动启用HTTPS安全连接

### 部署步骤

1. **推送代码到GitHub**:
   ```bash
   git add .
   git commit -m "Deploy website"
   git push origin main
   ```

2. **启用GitHub Pages**:
   - 进入仓库设置 (Settings)
   - 找到 "Pages" 选项
   - 在 "Source" 中选择 "GitHub Actions"
   - 保存设置

3. **查看部署状态**:
   - 在仓库的 "Actions" 标签页查看部署进度
   - 部署成功后，网站将在几分钟内生效

### 本地开发
```bash
# 克隆仓库
git clone https://github.com/[你的用户名]/website.git
cd website

# 启动本地服务器
python3 -m http.server 8000

# 访问网站
open http://localhost:8000
```

# BirdAiSnap - 多语言鸟类观察学习平台

## 🌟 项目简介

BirdAiSnap是一个专业的多语言鸟类观察学习平台，为全球鸟类爱好者提供高质量的教育内容和实用指导。

## 🌍 多语言支持

我们的平台支持8种语言，为全球用户提供母语级学习体验：

- 🇺🇸 **英语** - 专业增强版本
- 🇨🇳 **中文** - 原版完整内容
- 🇰🇷 **韩语** - 高质量翻译
- 🇫🇷 **法语** - 专业级翻译
- 🇩🇪 **德语** - 专业级翻译
- 🇯🇵 **日语** - 专业级翻译
- 🇵🇹 **葡萄牙语** - 完整翻译
- 🇷🇺 **俄语** - 基础翻译

## 📚 内容模块

### 🔍 鸟类观察 (Birdwatching)
- 入门指南
- 必备设备
- 识别技巧
- 最佳观察地点
- 季节性指导
- 摄影技巧
- 行为观察
- 鸣声识别
- 伦理与保护
- 记录保持

### 🌿 生态学 (Ecology)
- 栖息地与生态系统
- 食物网与食物链
- 迁徙模式
- 繁殖生态学
- 气候变化影响
- 城市生态学
- 保护生物学
- 岛屿生物地理学
- 授粉与种子传播
- 群落动态

### 🐦 宠物护理 (Pet Care)
- 选择合适的鸟类
- 营养与喂养
- 住房与环境
- 健康与兽医护理
- 训练与行为
- 繁殖与生殖
- 紧急急救
- 季节性护理
- 丰富活动
- 老年鸟类护理

### 🔬 科学奇观 (Scientific Wonders)
- 鸟类飞行力学
- 磁导航
- 蜂鸟力学
- 鸟类智能
- 羽毛结构
- 鸟类视觉
- 蛋发育
- 鸟类交流
- 迁徙生理学
- 生物力学

## 🚀 部署信息

### GitHub Pages 自动部署
本网站已配置 GitHub Actions 自动部署到 GitHub Pages：

- **部署地址**: `https://[你的用户名].github.io/website/`
- **自动部署**: 每次推送到 `main` 或 `master` 分支时自动更新
- **CDN加速**: 全球CDN分发，访问速度快
- **HTTPS支持**: 自动启用HTTPS安全连接

### 部署步骤

1. **推送代码到GitHub**:
   ```bash
   git add .
   git commit -m "Deploy website"
   git push origin main
   ```

2. **启用GitHub Pages**:
   - 进入仓库设置 (Settings)
   - 找到 "Pages" 选项
   - 在 "Source" 中选择 "GitHub Actions"
   - 保存设置

3. **查看部署状态**:
   - 在仓库的 "Actions" 标签页查看部署进度
   - 部署成功后，网站将在几分钟内生效

### 本地开发
```bash
# 克隆仓库
git clone https://github.com/[你的用户名]/website.git
cd website

# 启动本地服务器
python3 -m http.server 8000

# 访问网站
open http://localhost:8000
```

### 自定义域名 (可选)
如果你有自定义域名，可以：
1. 在仓库根目录创建 `CNAME` 文件
2. 在文件中写入你的域名 (如: `example.com`)
3. 在域名提供商处配置DNS记录指向GitHub Pages

## 🎯 特色功能

### 专业翻译质量
- **母语级翻译**: 所有主要语言版本均达到母语级质量
- **专业术语统一**: 建立完整的多语言鸟类学术语词典
- **文化适应性**: 符合各语言文化表达习惯

### 响应式设计
- **移动优先**: 完美适配手机、平板、桌面设备
- **现代UI**: 简洁美观的用户界面
- **快速加载**: 优化的资源加载和缓存策略

### 交互体验
- **进度跟踪**: 阅读进度可视化
- **导航便捷**: 直观的页面导航和返回功能
- **视觉丰富**: 精美的鸟类图片和图标

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **样式**: 现代CSS Grid和Flexbox布局
- **图标**: Emoji和自定义图标
- **部署**: GitHub Pages + GitHub Actions
- **版本控制**: Git

## 📈 项目统计

- **总文件数**: 200+ HTML文件
- **翻译覆盖**: 8种语言
- **内容模块**: 4大主要模块
- **专业文章**: 40+ 专业指导文章
- **代码质量**: 高质量HTML/CSS/JS代码

## 🤝 贡献指南

欢迎为项目做出贡献！您可以：

1. **报告问题**: 在Issues中报告bug或提出建议
2. **改进翻译**: 帮助改进现有翻译质量
3. **添加内容**: 贡献新的鸟类观察内容
4. **优化代码**: 改进网站性能和用户体验

## 📄 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 📞 联系我们

- **GitHub**: https://github.com/linqixin1003/website
- **Issues**: https://github.com/linqixin1003/website/issues

---

**BirdAiSnap** - 让鸟类观察变得简单而专业 🦅✨