# 首页鼠标悬停效果移除 - 任务清单 (Tasks)

## 📦 Phase 1: JavaScript 交互清理 (Priority: High)
JavaScript 的 `mousemove` 事件监听器会高频触发重绘，是闪屏的高风险源。

- [ ] **Task 1.1**: 移除 `script.js` 中的 "Magnetic Buttons" (磁性按钮) 逻辑。
  - *Target*: `script.js`
  - *Action*: 删除/注释 `mousemove` 监听器。
- [ ] **Task 1.2**: 移除 `script.js` 中的 "3D App Icons" (3D 图标悬停) 逻辑。
  - *Target*: `script.js`
  - *Action*: 删除/注释 `mousemove` 监听器。

## 📦 Phase 2: CSS 悬停效果清理 - 核心组件 (Priority: High)
应用卡片是首页最主要的交互区域。

- [ ] **Task 2.1**: 清理 `app-cards-3d.css` 中的 hover 效果。
  - *Target*: `app-cards-3d.css`
  - *Action*: 移除 `.app-card:hover` 的 `transform`, `box-shadow`。
  - *Action*: 移除 `.app-icon-large`, `.app-status`, `.btn-download` 等子元素的 hover 变化。
- [ ] **Task 2.2**: 清理 `styles.css` 中残留的 app-card hover 定义。
  - *Target*: `styles.css`
  - *Action*: 确保 `.app-card:hover` 没有任何 transform/shadow 属性。

## 📦 Phase 3: CSS 悬停效果清理 - 辅助组件 (Priority: Medium)
其他 UI 组件的悬停效果。

- [ ] **Task 3.1**: 清理 `styles.css` 中的通用 hover 效果。
  - *Target*: `styles.css`
  - *Action*: 移除 `.feature-card:hover`, `.btn-primary:hover`, `.nav-menu a:hover` 的动画。
- [ ] **Task 3.2**: 清理 `hero-enhanced.css` 中的 hover 效果。
  - *Target*: `hero-enhanced.css`
  - *Action*: 移除 `.btn.enhanced:hover`, `.app-icon:hover` 的 3D 效果。
- [ ] **Task 3.3**: 清理 `reviews-carousel.css` 中的 hover 效果。
  - *Target*: `reviews-carousel.css`
  - *Action*: 移除 `.review-card:hover` 的位移。

## 📦 Phase 4: 验证与提交
- [ ] **Task 4.1**: 运行 linter 检查语法错误。
- [ ] **Task 4.2**: 提交代码并推送到远端。
