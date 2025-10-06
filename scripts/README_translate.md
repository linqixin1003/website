# 蘑菇文章翻译脚本使用说明

## 功能特点

- ✅ 使用 Deepseek API 进行高质量翻译
- ✅ 批量处理所有文章
- ✅ 自动跳过已翻译的文件（支持断点续传）
- ✅ 失败自动重试（最多3次）
- ✅ 安全的API密钥管理（通过环境变量）
- ✅ 进度显示和统计
- ✅ 错误处理和日志

## 安装依赖

```bash
pip install requests
```

## 配置API密钥

**⚠️ 重要：请勿在代码中硬编码API密钥！**

### 方法1：设置环境变量（推荐）

**Windows PowerShell:**
```powershell
$env:DEEPSEEK_API_KEY = "your-api-key-here"
```

**Linux/Mac:**
```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

### 方法2：创建配置文件

创建 `.env` 文件（记得添加到 .gitignore）：
```
DEEPSEEK_API_KEY=your-api-key-here
```

然后安装 python-dotenv 并在脚本开头添加：
```python
from dotenv import load_dotenv
load_dotenv()
```

## 使用方法

### 1. 基本使用（翻译为英文）

```bash
cd C:\Users\Administrator\Documents\website
python scripts/translate_mushroom_articles.py
```

### 2. 自定义配置

编辑脚本中的配置区：

```python
# 翻译配置
SOURCE_LANG = "zh"  # 源语言
TARGET_LANG = "en"  # 目标语言：en, es, fr, de, ja, ko 等
SOURCE_DIR = Path("mushroom/zh")
TARGET_DIR = Path("mushroom/en")  # 根据目标语言修改

# API参数
TEMPERATURE = 0.3  # 0-1，越低越准确一致
MAX_TOKENS = 4000  # 最大输出长度
```

### 3. 翻译为其他语言

修改脚本配置后运行：

```python
# 翻译为西班牙语
TARGET_LANG = "es"
TARGET_DIR = Path("mushroom/es")

# 翻译为法语
TARGET_LANG = "fr"
TARGET_DIR = Path("mushroom/fr")

# 翻译为日语
TARGET_LANG = "ja"
TARGET_DIR = Path("mushroom/ja")
```

## 输出示例

```
============================================================
🍄 蘑菇文章翻译脚本 (Deepseek API)
============================================================

📖 源语言: zh
🌍 目标语言: en
📂 源目录: mushroom/zh
📂 目标目录: mushroom/en
🤖 模型: deepseek-chat

📁 找到 55 个文件待翻译

开始翻译...

[1/55] mushroom-identification/01-beginners-guide-mushroom-identification.txt
   🔄 翻译中... (8523 字符)
   ✅ 翻译完成 -> mushroom/en/mushroom-identification/01-beginners-guide-mushroom-identification.txt

[2/55] mushroom-identification/02-essential-field-equipment.txt
   ⏭️  已存在，跳过

...

============================================================
📊 翻译完成统计：
   ✅ 成功: 50
   ⏭️  跳过: 3
   ❌ 失败: 2
   📝 总计: 55
============================================================
```

## 目录结构

翻译后的文件将保持与源文件相同的目录结构：

```
mushroom/
├── zh/                          # 中文（源）
│   ├── mushroom-identification/
│   ├── mushroom-safety/
│   ├── mushroom-ecology/
│   ├── culinary-mushrooms/
│   └── mushroom-science/
└── en/                          # 英文（目标）
    ├── mushroom-identification/
    ├── mushroom-safety/
    ├── mushroom-ecology/
    ├── culinary-mushrooms/
    └── mushroom-science/
```

## 注意事项

1. **API费用**：Deepseek API按token计费，55篇文章翻译可能产生一定费用，请注意控制
2. **网络稳定**：确保网络连接稳定，脚本支持断点续传
3. **文件备份**：首次运行前建议备份源文件
4. **质量检查**：翻译完成后建议抽查几篇文章的质量
5. **API限流**：脚本已内置延迟（1秒/文件），如遇限流可增加延迟

## 高级用法

### 只翻译特定模块

修改 `get_all_source_files()` 函数：

```python
def get_all_source_files():
    # 只翻译 mushroom-identification 模块
    txt_files = list(SOURCE_DIR.glob("mushroom-identification/*.txt"))
    return sorted(txt_files)
```

### 调整翻译质量

```python
# 更精确的翻译（较慢）
TEMPERATURE = 0.1

# 更创意的翻译（可能不一致）
TEMPERATURE = 0.7
```

### 批量翻译多种语言

创建批处理脚本：

```bash
# translate_all.sh
for lang in en es fr de ja ko
do
    echo "Translating to $lang..."
    # 修改脚本配置并运行
    python scripts/translate_mushroom_articles.py --lang $lang
done
```

## 故障排除

### 问题1：API密钥错误
```
❌ 错误：未配置 DEEPSEEK_API_KEY
```
**解决**：按照"配置API密钥"部分设置环境变量

### 问题2：翻译失败
```
❌ API返回错误 401: Unauthorized
```
**解决**：检查API密钥是否正确，是否过期

### 问题3：网络超时
```
❌ 请求异常: timeout
```
**解决**：检查网络连接，脚本会自动重试

### 问题4：quota exceeded（配额超限）
**解决**：等待配额重置或升级API套餐

## 联系和反馈

如有问题或建议，请提交issue或联系开发者。

---

**祝您翻译顺利！🍄✨**

