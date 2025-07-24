# BirdAiSnap 本地部署指南

## 快速开始

### 方法一：使用 Python 脚本（推荐）

```bash
python3 start-server.py
```

### 方法二：使用 Bash 脚本（macOS/Linux）

```bash
./start-server.sh
```

### 方法三：手动启动

```bash
# Python 3
python3 -m http.server 8000

# 或者 Python 2
python -m SimpleHTTPServer 8000
```

## 访问地址

启动服务器后，在浏览器中访问：

- **主页**: http://localhost:8000/index.html
- **知识中心**: http://localhost:8000/knowledge.html
- **观鸟指南**: http://localhost:8000/knowledge/birdwatching.html

## 功能验证

### ✅ "More Bird Knowledge" 跳转功能

1. 打开主页 `http://localhost:8000/index.html`
2. 滚动到 "Core Features" 部分
3. 点击 "More Bird Knowledge" 卡片
4. 应该会跳转到知识中心页面 `knowledge.html`

### ✅ 多语言切换

- 点击右上角的语言切换按钮
- 支持中英文切换
- "More Bird Knowledge" 在中文模式下显示为 "更多鸟类知识"

### ✅ 移动端适配

- 项目已包含移动端优化
- 响应式设计适配不同屏幕尺寸

## 项目结构

```
.
├── index.html              # 主页
├── knowledge.html          # 知识中心
├── styles.css             # 主样式
├── knowledge.css          # 知识中心样式
├── mobile-styles.css      # 移动端样式
├── mobile-enhancement.css # 移动端增强样式
├── script.js              # 主脚本
├── mobile-interactions.js # 移动端交互
├── knowledge/             # 知识文章目录
│   ├── birdwatching.html
│   └── birdwatching/      # 详细文章
├── start-server.py        # Python 部署脚本
├── start-server.sh        # Bash 部署脚本
└── README-DEPLOYMENT.md   # 本文件
```

## 开发说明

### 修改内容后

1. 保存文件
2. 刷新浏览器即可看到更改
3. 无需重启服务器

### 停止服务器

按 `Ctrl+C` 停止服务器

### 端口冲突

如果端口 8000 被占用：

1. 修改脚本中的 `PORT` 变量
2. 或者关闭占用端口的其他程序

## 故障排除

### 问题：点击 "More Bird Knowledge" 没有反应

**解决方案**：
1. 检查浏览器控制台是否有 JavaScript 错误
2. 确认 `script.js` 文件加载正常
3. 验证 `openKnowledgeCenter()` 函数是否定义

### 问题：页面样式显示异常

**解决方案**：
1. 检查 CSS 文件是否正确加载
2. 清除浏览器缓存
3. 确认所有样式文件都在正确位置

### 问题：移动端显示异常

**解决方案**：
1. 检查移动端样式文件是否加载
2. 验证 viewport meta 标签设置
3. 测试不同屏幕尺寸

## 生产部署

对于生产环境，建议使用：

- **Nginx** 作为静态文件服务器
- **Apache** HTTP 服务器
- **GitHub Pages** 或其他静态托管服务

## 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **样式**: 响应式设计，移动端优化
- **功能**: 多语言支持，动态内容加载
- **部署**: 静态文件服务器

## 联系信息

如有问题，请联系：lingjuetech@gmail.com