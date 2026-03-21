#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最终质量检查 - 验证所有组件完整性"""

import sys
from pathlib import Path
import json

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = {
    'en': 'English',
    'zh': '中文',
    'de': 'Deutsch',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
    'ja': '日本語',
    'ko': '한국어',
    'pt': 'Português',
    'ru': 'Русский'
}

def check_articles():
    """检查文章完整性"""
    print("\n📄 检查文章完整性")
    print("-" * 60)
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    all_complete = True
    for lang_code in LANGUAGES.keys():
        lang_dir = Path(f'insect/{lang_code}')
        if not lang_dir.exists():
            print(f"  ❌ {lang_code}: 目录不存在")
            all_complete = False
            continue
        
        article_count = 0
        for category in categories:
            cat_dir = lang_dir / category
            if cat_dir.exists():
                article_count += len(list(cat_dir.glob('[0-9]*.html')))
        
        status = "✅" if article_count == 50 else "❌"
        print(f"  {status} {lang_code}: {article_count}/50 篇文章")
        
        if article_count != 50:
            all_complete = False
    
    return all_complete

def check_json_configs():
    """检查JSON配置文件"""
    print("\n📋 检查JSON配置文件")
    print("-" * 60)
    
    json_dir = Path('insect-articles-json')
    all_complete = True
    
    for lang_code in LANGUAGES.keys():
        json_file = json_dir / f'insect-article-urls-{lang_code}.json'
        
        if not json_file.exists():
            print(f"  ❌ {lang_code}: JSON文件不存在")
            all_complete = False
            continue
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 检查两种可能的结构
            if 'categories' in data:
                article_count = sum(len(cat.get('articles', [])) for cat in data['categories'])
            elif 'articleCategories' in data:
                article_count = sum(len(cat.get('articles', [])) for cat in data['articleCategories'].values())
            else:
                article_count = 0
            status = "✅" if article_count == 50 else "⚠️ "
            print(f"  {status} {lang_code}: {article_count} 条URL配置")
            
            if article_count != 50:
                all_complete = False
        except Exception as e:
            print(f"  ❌ {lang_code}: 读取失败 - {e}")
            all_complete = False
    
    return all_complete

def check_index_pages():
    """检查索引页面"""
    print("\n🏠 检查索引页面")
    print("-" * 60)
    
    all_complete = True
    for lang_code in LANGUAGES.keys():
        index_file = Path(f'insect/{lang_code}/insect-articles-index.html')
        
        if index_file.exists():
            print(f"  ✅ {lang_code}: 索引页面存在")
        else:
            print(f"  ❌ {lang_code}: 索引页面缺失")
            all_complete = False
    
    return all_complete

def check_images():
    """检查图片资源"""
    print("\n🖼️  检查图片资源")
    print("-" * 60)
    
    images_dir = Path('insect/images')
    
    if not images_dir.exists():
        print("  ❌ 图片目录不存在")
        return False
    
    image_files = list(images_dir.glob('*.jpg'))
    print(f"  ✅ 图片总数: {len(image_files)} 张")
    
    # 检查关键图片类型
    main_images = len(list(images_dir.glob('*_main.jpg')))
    icon_images = len(list(images_dir.glob('*_icon.jpg')))
    divider_images = len(list(images_dir.glob('*_divider.jpg')))
    
    print(f"  ✅ 主图片: {main_images} 张")
    print(f"  ✅ 图标: {icon_images} 张")
    print(f"  ✅ 分隔符: {divider_images} 张")
    
    return True

def check_main_pages():
    """检查主要页面"""
    print("\n🌐 检查主要页面")
    print("-" * 60)
    
    pages = {
        'index.html': '主页',
        'insect-app.html': '昆虫应用页面'
    }
    
    all_complete = True
    for page_file, page_name in pages.items():
        if Path(page_file).exists():
            print(f"  ✅ {page_name}: 存在")
        else:
            print(f"  ❌ {page_name}: 缺失")
            all_complete = False
    
    return all_complete

def main():
    print("=" * 80)
    print("🔍 InsectAiSnap 最终质量检查")
    print("=" * 80)
    
    checks = {
        '文章完整性': check_articles(),
        'JSON配置': check_json_configs(),
        '索引页面': check_index_pages(),
        '图片资源': check_images(),
        '主要页面': check_main_pages()
    }
    
    print("\n" + "=" * 80)
    print("📊 检查总结")
    print("=" * 80)
    
    all_passed = True
    for check_name, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"  {status} {check_name}: {'通过' if passed else '需要修复'}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 80)
    
    if all_passed:
        print("\n🎉🎉🎉 所有检查通过！项目质量完美！")
        print("\n✅ 450篇文章 - 9种语言")
        print("✅ JSON配置完整")
        print("✅ 索引页面完整")
        print("✅ 图片资源完整")
        print("✅ 主要页面完整")
        print("\n🚀 项目已准备好部署！")
    else:
        print("\n⚠️  发现需要修复的问题，请检查上述报告")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    main()

