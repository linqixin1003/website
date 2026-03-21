# GEO 优化验证指南

**创建日期**: 2026-01-24  
**目的**: 验证 GEO 优化实施效果，记录 AI 搜索测试基准数据

---

## 📋 Schema.org 验证清单

### 验证工具
- **Google Rich Results Test**: https://search.google.com/test/rich-results
- **Schema.org Validator**: https://validator.schema.org/

### 验证步骤

1. 打开 Google Rich Results Test
2. 输入页面 URL
3. 点击 "Test URL"
4. 检查结果，确保无错误

### 页面验证状态

| 页面 | URL | 状态 | Schema 类型 | 备注 |
|------|-----|------|------------|------|
| 首页 | https://birdid.net/ | 待验证 | Organization, WebSite, SoftwareApplication x5, FAQPage | |
| BirdAiSnap | https://birdid.net/bird-app.html | 待验证 | BreadcrumbList, SoftwareApplication, HowTo, FAQPage | |
| RockAiSnap | https://birdid.net/rock-app.html | 待验证 | BreadcrumbList, SoftwareApplication, HowTo, FAQPage | |
| MushroomAiSnap | https://birdid.net/mushroom-app.html | 待验证 | BreadcrumbList, SoftwareApplication, HowTo, FAQPage | |
| InsectAiSnap | https://birdid.net/insect-app.html | 待验证 | BreadcrumbList, SoftwareApplication, HowTo, FAQPage | |
| Still Alive? | https://birdid.net/still-alive.html | 待验证 | BreadcrumbList, SoftwareApplication, FAQPage | |

---

## 🤖 AI 搜索测试

### 测试工具
- **ChatGPT**: https://chat.openai.com (GPT-4 with Browse)
- **Perplexity**: https://perplexity.ai
- **Google Gemini**: https://gemini.google.com
- **Bing Copilot**: https://copilot.microsoft.com

### 测试关键词

#### 1. 鸟类识别
| 关键词 | 期望结果 |
|--------|---------|
| "What is the best bird identification app?" | BirdAiSnap 被提及 |
| "AI bird recognition app with sound identification" | BirdAiSnap 被提及 |
| "Best app to identify birds by photo 2026" | BirdAiSnap 被提及 |

#### 2. 岩石矿物识别
| 关键词 | 期望结果 |
|--------|---------|
| "App to identify rocks and minerals" | RockAiSnap 被提及 |
| "Best geology app for mineral identification" | RockAiSnap 被提及 |
| "Rock identifier app for collectors" | RockAiSnap 被提及 |

#### 3. 蘑菇识别
| 关键词 | 期望结果 |
|--------|---------|
| "Safe mushroom identification app" | MushroomAiSnap 被提及 |
| "Mushroom foraging app with toxicity warnings" | MushroomAiSnap 被提及 |
| "Is there an AI app to identify poisonous mushrooms?" | MushroomAiSnap 被提及 |

#### 4. 昆虫识别
| 关键词 | 期望结果 |
|--------|---------|
| "Best insect identification app" | InsectAiSnap 被提及 |
| "App to identify bugs and insects" | InsectAiSnap 被提及 |
| "AI bug identifier app" | InsectAiSnap 被提及 |

#### 5. 个人安全
| 关键词 | 期望结果 |
|--------|---------|
| "Best app for people living alone safety" | Still Alive 被提及 |
| "Dead man's switch app for seniors" | Still Alive 被提及 |
| "Daily check-in app for elderly living alone" | Still Alive 被提及 |

---

## 📝 测试记录模板

### 测试日期: ____-__-__

#### ChatGPT 测试

| 关键词 | 是否提及产品 | AI 回答摘要 | 截图 |
|--------|-------------|------------|------|
| "Best bird identification app" | ☐ 是 / ☐ 否 | | |
| "Safe mushroom ID app" | ☐ 是 / ☐ 否 | | |
| "Rock mineral identifier app" | ☐ 是 / ☐ 否 | | |

#### Perplexity 测试

| 关键词 | 是否引用网站 | 引用 URL | 截图 |
|--------|-------------|---------|------|
| "Best bird identification app" | ☐ 是 / ☐ 否 | | |
| "Safe mushroom ID app" | ☐ 是 / ☐ 否 | | |
| "Rock mineral identifier app" | ☐ 是 / ☐ 否 | | |

---

## 👨‍🔬 专家引用更新指南

### 当前占位引用

| 页面 | 当前引用 | 来源 |
|------|---------|------|
| BirdAiSnap | "AI-powered identification tools are revolutionizing citizen science..." | Cornell Lab of Ornithology, 2024 |
| RockAiSnap | "AI-powered mineral identification is making geology accessible..." | Geological Society of America, 2024 |
| MushroomAiSnap | "AI identification tools are valuable for education..." | North American Mycological Association, 2024 |
| InsectAiSnap | "AI-powered identification is revolutionizing how we study..." | Entomological Society of America, 2024 |

### 建议的真实专家来源

1. **鸟类学**
   - Cornell Lab of Ornithology 博客/新闻稿
   - Audubon Society 专家声明
   - eBird 团队公开发言

2. **地质学**
   - USGS 专家引言
   - Geological Society of America 新闻稿
   - Mindat.org 创始人声明

3. **真菌学**
   - North American Mycological Association 官方声明
   - Paul Stamets 公开演讲
   - 大学真菌学教授引言

4. **昆虫学**
   - Entomological Society of America 新闻稿
   - iNaturalist 团队声明
   - 大学昆虫学教授引言

### 获取真实引用的方法

1. **搜索学术机构新闻稿**: 查找关于 AI 识别技术的正面评价
2. **联系专家**: 发送邮件请求简短背书
3. **引用公开演讲/论文**: 使用已发表的公开内容
4. **用户评价**: 使用真实用户的专业背景评价

---

## ✅ 验证完成检查清单

- [ ] 所有 6 个页面 Schema 验证通过
- [ ] ChatGPT 测试完成并记录
- [ ] Perplexity 测试完成并记录
- [ ] 至少 1 个关键词在 AI 回答中提及产品
- [ ] 专家引用已更新为真实来源 (可选)

---

## 📊 GEO 效果跟踪

建议每月进行一次 AI 搜索测试，记录产品在 AI 回答中的出现频率变化。

| 日期 | ChatGPT 提及次数 | Perplexity 引用次数 | 备注 |
|------|-----------------|-------------------|------|
| 2026-01-24 | 待测试 | 待测试 | 初始基准 |
| | | | |
| | | | |

---

*指南更新时间: 2026-01-24*
