# Schema 验证直接链接

点击以下链接直接在 Google Rich Results Test 中验证每个页面：

---

## 🔗 一键验证链接

### 1. 首页 (index.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2F
```
[👉 点击验证首页](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2F)

**预期 Schema**: Organization, WebSite, SoftwareApplication x5, FAQPage

---

### 2. BirdAiSnap (bird-app.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fbird-app.html
```
[👉 点击验证 BirdAiSnap](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fbird-app.html)

**预期 Schema**: BreadcrumbList, SoftwareApplication, HowTo, FAQPage

---

### 3. RockAiSnap (rock-app.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Frock-app.html
```
[👉 点击验证 RockAiSnap](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Frock-app.html)

**预期 Schema**: BreadcrumbList, SoftwareApplication, HowTo, FAQPage

---

### 4. MushroomAiSnap (mushroom-app.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fmushroom-app.html
```
[👉 点击验证 MushroomAiSnap](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fmushroom-app.html)

**预期 Schema**: BreadcrumbList, SoftwareApplication, HowTo, FAQPage

---

### 5. InsectAiSnap (insect-app.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Finsect-app.html
```
[👉 点击验证 InsectAiSnap](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Finsect-app.html)

**预期 Schema**: BreadcrumbList, SoftwareApplication, HowTo, FAQPage

---

### 6. Still Alive? (still-alive.html)
```
https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fstill-alive.html
```
[👉 点击验证 Still Alive](https://search.google.com/test/rich-results?url=https%3A%2F%2Fbirdid.net%2Fstill-alive.html)

**预期 Schema**: BreadcrumbList, SoftwareApplication, FAQPage

---

## ✅ 验证检查清单

| 页面 | 验证状态 | 发现的错误 | 修复状态 |
|------|---------|-----------|---------|
| 首页 | ☐ 通过 / ☐ 有错误 | | |
| BirdAiSnap | ☐ 通过 / ☐ 有错误 | | |
| RockAiSnap | ☐ 通过 / ☐ 有错误 | | |
| MushroomAiSnap | ☐ 通过 / ☐ 有错误 | | |
| InsectAiSnap | ☐ 通过 / ☐ 有错误 | | |
| Still Alive | ☐ 通过 / ☐ 有错误 | | |

---

## 🔧 常见错误及修复

### 1. "Missing field" 错误
- **原因**: Schema 缺少必填字段
- **修复**: 添加缺失的字段到 JSON-LD

### 2. "Invalid value" 错误
- **原因**: 字段值格式不正确
- **修复**: 检查日期格式、URL 格式等

### 3. "Unrecognized type" 警告
- **原因**: 使用了非标准 Schema 类型
- **影响**: 通常可忽略，不影响基本功能

---

## 📊 备用验证工具

如果 Google Rich Results Test 不可用，可以使用：

1. **Schema.org Validator**: https://validator.schema.org/
2. **Structured Data Linter**: http://linter.structured-data.org/
3. **Yandex Structured Data Validator**: https://webmaster.yandex.com/tools/microtest/

---

*创建时间: 2026-01-24*
