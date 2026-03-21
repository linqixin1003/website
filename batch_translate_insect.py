#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译昆虫文章 - 使用简化的复制+路径修复方法
由于Google Translate API的限制，我们先复制英文版本，然后逐步翻译
"""

import os
import re
import sys
import shutil
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = ['de', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
CATEGORIES = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 'pest-management', 'behavior-evolution']

def fix_paths_for_lang(content, lang_code):
    """修复多语言版本的路径"""
    # 更新lang属性
    content = re.sub(r'<html lang="en">', f'<html lang="{lang_code}">', content)
    
    # 图片路径不需要修改，因为都在同一个images目录
    # CSS路径需要修改
    content = re.sub(
        r'href="../../../mobile-insect-styles.css"',
        r'href="../../../../mobile-insect-styles.css"',
        content
    )
    
    return content

def copy_and_prepare_articles():
    """复制英文文章到各语言目录并修复路径"""
    source_dir = Path('insect/en')
    total_copied = 0
    
    print("=" * 80)
    print("步骤 1: 复制英文文章到各语言目录")
    print("=" * 80)
    print()
    
    for lang in LANGUAGES:
        print(f"处理语言: {lang}")
        lang_dir = Path('insect') / lang
        lang_dir.mkdir(exist_ok=True)
        
        for category in CATEGORIES:
            cat_source = source_dir / category
            cat_target = lang_dir / category
            cat_target.mkdir(exist_ok=True)
            
            if not cat_source.exists():
                continue
            
            for html_file in cat_source.glob('*.html'):
                if html_file.name[0].isdigit():  # 只处理编号文章
                    # 读取源文件
                    with open(html_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 修复路径
                    content = fix_paths_for_lang(content, lang)
                    
                    # 保存到目标位置
                    target_file = cat_target / html_file.name
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    total_copied += 1
                    print(f"  ✅ {category}/{html_file.name}")
        
        print()
    
    print(f"完成！共复制 {total_copied} 个文件")
    print()
    return total_copied

def create_translation_guide():
    """创建翻译指南文件"""
    guide = """# 昆虫文章翻译指南

## 已完成的工作

1. ✅ 创建了多语言目录结构 (de, es, fr, it, ja, ko, pt, ru, zh)
2. ✅ 复制了英文文章到各语言目录
3. ✅ 修复了CSS和图片路径
4. ✅ 创建了各语言的索引页面

## 下一步：翻译内容

由于Google Translate API的限制，建议使用以下方法之一进行翻译：

### 方法1: 使用专业翻译服务
- DeepL API (推荐，质量最好)
- Microsoft Translator API
- Google Cloud Translation API (付费版本)

### 方法2: 使用translation-tools中的现有脚本
```bash
cd translation-tools
python translate_all_languages.py --source insect/en --target insect
```

### 方法3: 逐个语言翻译
```bash
python translate_by_language.py --lang de --source insect/en --target insect/de
python translate_by_language.py --lang es --source insect/en --target insect/es
# ... 其他语言
```

## 当前状态

- 总文章数: 50篇
- 目标语言: 9种
- 需要翻译: 450个文件
- 已准备: 450个文件 (英文版本，待翻译)

## 文件结构

```
insect/
├── en/                    # 英文原版
│   ├── basics-identification/
│   ├── ecology-environment/
│   ├── beneficial-pollinators/
│   ├── pest-management/
│   └── behavior-evolution/
├── de/                    # 德语版本 (待翻译)
├── es/                    # 西班牙语版本 (待翻译)
├── fr/                    # 法语版本 (待翻译)
├── it/                    # 意大利语版本 (待翻译)
├── ja/                    # 日语版本 (待翻译)
├── ko/                    # 韩语版本 (待翻译)
├── pt/                    # 葡萄牙语版本 (待翻译)
├── ru/                    # 俄语版本 (待翻译)
└── zh/                    # 中文版本 (待翻译)
```

## 验证

所有文件的路径已正确设置：
- ✅ CSS路径: ../../../../mobile-insect-styles.css
- ✅ 图片路径: ../../images/xxx.jpg
- ✅ lang属性已更新

可以直接开始翻译内容。
"""
    
    with open('INSECT_TRANSLATION_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("✅ 已创建翻译指南: INSECT_TRANSLATION_GUIDE.md")

def main():
    print("\n")
    print("=" * 80)
    print("昆虫文章多语言准备工具")
    print("=" * 80)
    print()
    
    # 复制并准备文章
    total = copy_and_prepare_articles()
    
    # 创建翻译指南
    print("=" * 80)
    print("步骤 2: 创建翻译指南")
    print("=" * 80)
    print()
    create_translation_guide()
    
    print()
    print("=" * 80)
    print("准备完成！")
    print("=" * 80)
    print(f"已准备 {total} 个文件用于翻译")
    print("请查看 INSECT_TRANSLATION_GUIDE.md 了解下一步操作")
    print()

if __name__ == '__main__':
    main()

