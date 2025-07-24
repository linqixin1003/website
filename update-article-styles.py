#!/usr/bin/env python3
"""
批量更新所有文章文件，添加图片样式和脚本引用
"""

import os
from pathlib import Path
import re

def update_article_file(file_path, language='en'):
    """更新单个文章文件"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 确定路径前缀
        if language == 'en':
            css_path = 'article-images.css'
            js_path = 'image-loader.js'
        else:
            css_path = '../article-images.css'
            js_path = '../image-loader.js'
        
        # 检查是否已经包含了样式文件
        if 'article-images.css' in content:
            return True  # 已经更新过了
        
        # 查找CSS引用位置并添加
        css_pattern = r'(<link rel="stylesheet" href="knowledge\.css">)'
        css_replacement = f'\\1\\n    <link rel="stylesheet" href="{css_path}">'
        content = re.sub(css_pattern, css_replacement, content)
        
        # 查找JS引用位置并添加
        js_pattern = r'(<script src="script\.js"></script>)'
        js_replacement = f'\\1\\n    <script src="{js_path}"></script>'
        content = re.sub(js_pattern, js_replacement, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"    ❌ 错误: {file_path} - {e}")
        return False

def update_all_articles():
    """更新所有文章文件"""
    
    print("🎨 开始更新所有文章的样式引用...")
    print("=" * 60)
    
    updated_count = 0
    total_count = 0
    
    # 分类列表
    categories = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
    
    # 语言列表
    languages = {
        'en': '',
        'zh': 'zh/',
        'ja': 'ja/',
        'ko': 'ko/',
        'de': 'de/',
        'fr': 'fr/',
        'es': 'es/',
        'it': 'it/',
        'pt': 'pt/',
        'ru': 'ru/'
    }
    
    for category in categories:
        print(f"\\n📁 处理分类: {category.upper()}")
        
        # 处理每篇文章（01-10）
        for i in range(1, 11):
            article_id = f"{i:02d}"
            
            # 更新所有语言版本
            for lang_code, lang_prefix in languages.items():
                if lang_code == 'en':
                    file_path = Path(f"{category}/{article_id}-article.html")
                else:
                    file_path = Path(f"{lang_prefix}{category}/{article_id}-article.html")
                
                if file_path.exists():
                    total_count += 1
                    if update_article_file(file_path, lang_code):
                        updated_count += 1
                        print(f"  ✅ {file_path}")
                    else:
                        print(f"  ❌ {file_path}")
    
    print(f"\\n📊 更新完成: {updated_count}/{total_count} 个文件")

def main():
    print("🚀 开始批量更新文章样式引用...")
    print("=" * 60)
    
    update_all_articles()
    
    print("\\n" + "=" * 60)
    print("🎉 文章样式更新完成！")
    print("\\n📋 完成的任务:")
    print("  ✅ 为所有文章添加了图片样式引用")
    print("  ✅ 为所有文章添加了图片加载脚本引用")
    print("  ✅ 处理了所有语言版本的路径")

if __name__ == "__main__":
    main()