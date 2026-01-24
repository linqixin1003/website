# 首页鼠标悬停效果移除规范 (Homepage Hover Removal Specification)

## 1. 核心需求
**移除首页所有鼠标悬停 (hover) 效果**，以彻底解决用户反馈的"闪屏"问题。

**背景**:
- 用户报告鼠标悬停在卡片上时出现闪屏。
- 之前已移除无限循环动画，但 hover 触发的布局变化（transform, box-shadow, opacity）似乎在特定设备上仍引起重绘/回流导致的闪烁。
- 用户明确要求"鼠标上去的效果全部去掉" (Remove all mouse hover effects)。

## 2. 范围 (Scope)
主要针对 `index.html` 及其引用的 CSS 文件和 JS 文件。
重点关注交互元素：
- `.app-card` (应用卡片)
- `.feature-card` (特性卡片)
- `.btn` (按钮)
- `.app-icon` (Hero区域图标)
- `.review-card` (评论卡片)

## 3. 技术方案 (Technical Implementation)

### 3.1 移除的 CSS 属性
在 `:hover` 伪类中，移除以下触发重绘/合成的属性：
- `transform` (translate, scale, rotate)
- `box-shadow` (阴影变化)
- `opacity` (透明度变化)
- `border-color` (如果引起布局抖动)
- `background` (如果涉及复杂渐变重绘)

### 3.2 JavaScript 交互移除
- **Magnetic Buttons**: 移除按钮的磁吸效果 (`mousemove` 监听器)。
- **3D Icons**: 移除 Hero 区域图标的 3D 倾斜效果 (`mousemove` 监听器)。

### 3.3 保留的交互提示
为了保证基本的可用性，保留：
- `cursor: pointer` (鼠标手型)
- 简单的 `color` 变化 (纯色文字变色，风险最低)
- *注意*：如果用户要求"全部去掉"，则尽可能连颜色变化也移除，或者只保留极其微小的变化。鉴于"闪屏"通常由 GPU 层变化引起，优先移除 transform/shadow/opacity。

### 3.4 受影响文件及具体修改

#### `app-cards-3d.css` (重灾区)
- 移除 `.app-card:hover` 的 `transform` (位移/缩放)。
- 移除 `.app-card:hover` 的 `box-shadow` (发光/阴影)。
- 移除 `.app-card:hover .app-icon-large` 的旋转/放大。
- 移除 `.app-card:hover::after/::before` 的 opacity 变化。
- 移除 `.app-card:hover .app-features span` 的样式变化。

#### `styles.css`
- 移除 `.feature-card:hover` 的上浮和阴影。
- 移除 `.btn-primary:hover` 的上浮和阴影。
- 移除 `.nav-menu a:hover` 的复杂下划线动画 (保留文字变色)。

#### `hero-enhanced.css`
- 移除 `.apps-showcase.enhanced .app-icon:hover` 的 3D 翻转效果。
- 移除 `.btn.enhanced:hover` 的光效动画。

#### `reviews-carousel.css`
- 移除 `.review-card:hover` 的上浮效果。

#### `script.js`
- 删除/注释掉 "Magnetic Buttons" 和 "3D App Icons" 相关的 `addEventListener` 代码。

## 4. 验证标准 (Verification)
1.  **无位移**: 鼠标经过卡片时，卡片像素级静止，不应有任何位置移动。
2.  **无闪烁**: 快速在多个卡片间移动鼠标，屏幕不应出现闪烁或白屏。
3.  **可点击**: 鼠标指针仍应变为手型 (`cursor: pointer`)。

## 5. 执行计划
1.  **Step 1**: 清理 `script.js` 中的 JS 交互。
2.  **Step 2**: 清理 `app-cards-3d.css` (优先级最高)。
3.  **Step 3**: 清理 `styles.css` 中的卡片和按钮 hover。
4.  **Step 4**: 清理 `hero-enhanced.css` 和 `reviews-carousel.css`。
5.  **Step 5**: 提交代码并请求用户测试。
