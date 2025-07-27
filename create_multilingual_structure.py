#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建完整的10种语言目录结构和文件
为pet-care页面创建所有语言版本的支持文件
"""

import os
import shutil
from pathlib import Path

# 支持的语言列表
LANGUAGES = ['zh', 'en', 'it', 'ja', 'ru', 'fr', 'de', 'es', 'pt', 'ko']

# 需要创建的目录结构
DIRECTORIES = [
    'pet-care',
    'knowledge', 
    'birdwatching',
    'scientific-wonders',
    'ecology',
    'conservation'
]

def create_language_directories():
    """创建所有语言的目录结构"""
    print("🌍 开始创建多语言目录结构...")
    
    for lang in LANGUAGES:
        lang_dir = Path(lang)
        
        # 如果语言目录不存在，创建它
        if not lang_dir.exists():
            lang_dir.mkdir()
            print(f"✅ 创建语言目录: {lang}/")
        
        # 为每种语言创建子目录
        for directory in DIRECTORIES:
            sub_dir = lang_dir / directory
            if not sub_dir.exists():
                sub_dir.mkdir(parents=True)
                print(f"✅ 创建子目录: {lang}/{directory}/")

def copy_pet_care_files():
    """复制pet-care文件到所有语言目录"""
    print("\n📁 开始复制pet-care文件...")
    
    # 基础语言目录（已存在的）
    base_dirs = ['zh', 'en', 'it']
    
    for lang in LANGUAGES:
        if lang in base_dirs:
            continue  # 跳过已存在的目录
            
        lang_pet_care = Path(lang) / 'pet-care'
        
        # 从英文版本复制文件作为模板
        en_pet_care = Path('en') / 'pet-care'
        
        if en_pet_care.exists():
            # 获取所有HTML文件
            for html_file in en_pet_care.glob('*.html'):
                target_file = lang_pet_care / html_file.name
                if not target_file.exists():
                    shutil.copy2(html_file, target_file)
                    print(f"✅ 复制文件: {target_file}")

def create_index_files():
    """为每种语言创建索引文件"""
    print("\n📄 创建语言索引文件...")
    
    # 语言名称映射
    language_names = {
        'zh': '中文',
        'en': 'English',
        'it': 'Italiano', 
        'ja': '日本語',
        'ru': 'Русский',
        'fr': 'Français',
        'de': 'Deutsch',
        'es': 'Español',
        'pt': 'Português',
        'ko': '한국어'
    }
    
    for lang in LANGUAGES:
        index_file = Path(lang) / 'index.html'
        if not index_file.exists():
            # 创建简单的索引页面
            content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BirdAiSnap - {language_names[lang]}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            text-align: center;
            padding: 50px 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2E8B57;
            margin-bottom: 30px;
        }}
        .nav-links {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .nav-link {{
            display: block;
            padding: 15px 20px;
            background: #2E8B57;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            transition: background 0.3s ease;
        }}
        .nav-link:hover {{
            background: #1e5f3f;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>BirdAiSnap - {language_names[lang]}</h1>
        <p>Welcome to BirdAiSnap {language_names[lang]} version</p>
        
        <div class="nav-links">
            <a href="pet-care/" class="nav-link">Pet Care</a>
            <a href="knowledge/" class="nav-link">Knowledge</a>
            <a href="birdwatching/" class="nav-link">Birdwatching</a>
            <a href="scientific-wonders/" class="nav-link">Scientific Wonders</a>
            <a href="ecology/" class="nav-link">Ecology</a>
            <a href="conservation/" class="nav-link">Conservation</a>
        </div>
        
        <p style="margin-top: 30px;">
            <a href="../pet-care.html">← Back to Main Pet Care Page</a>
        </p>
    </div>
</body>
</html>"""
            
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 创建索引文件: {index_file}")

def main():
    """主函数"""
    print("🚀 开始创建完整的10种语言支持结构...")
    
    # 创建目录结构
    create_language_directories()
    
    # 复制pet-care文件
    copy_pet_care_files()
    
    # 创建索引文件
    create_index_files()
    
    print(f"\n🎉 完成! 已为以下 {len(LANGUAGES)} 种语言创建支持结构:")
    for lang in LANGUAGES:
        print(f"  • {lang}")
    
    print("\n📋 创建的目录结构:")
    for lang in LANGUAGES:
        for directory in DIRECTORIES:
            print(f"  {lang}/{directory}/")
    
    print("\n✨ 多语言结构创建完成!")

if __name__ == "__main__":
    main()