#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复中文文章的元数据（lang、title等）"""

import re
import sys
from pathlib import Path
import requests

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def translate_simple(text):
    """简单翻译"""
    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": f"翻译成中文：{text}"}], "temperature": 0.3},
            timeout=15
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip().strip('"\'')
    except:
        pass
    return text

def fix_metadata(html_file):
    """修复元数据"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    changed = False
    
    # 1. lang属性
    if '<html lang="en">' in html:
        html = html.replace('<html lang="en">', '<html lang="zh">')
        changed = True
        print(f"      ✅ lang属性")
    
    # 2. title
    title_match = re.search(r'<title>([^<]+)</title>', html)
    if title_match and ' - InsectAiSnap' in title_match.group(1):
        english_title = title_match.group(1).replace(' - InsectAiSnap', '')
        if not re.search(r'[\u4e00-\u9fff]', english_title):
            chinese_title = translate_simple(english_title)
            html = html.replace(
                f'<title>{title_match.group(1)}</title>',
                f'<title>{chinese_title} - InsectAiSnap</title>'
            )
            changed = True
            print(f"      ✅ title: {chinese_title}")
    
    # 3. hero-title
    hero_match = re.search(r'<h1 class="hero-title">([^<]+)</h1>', html)
    if hero_match and not re.search(r'[\u4e00-\u9fff]', hero_match.group(1)):
        chinese = translate_simple(hero_match.group(1))
        html = html.replace(
            f'<h1 class="hero-title">{hero_match.group(1)}</h1>',
            f'<h1 class="hero-title">{chinese}</h1>'
        )
        changed = True
        print(f"      ✅ hero-title")
    
    # 4. article-title
    article_match = re.search(r'<h2 class="article-title">([^<]+)</h2>', html)
    if article_match and not re.search(r'[\u4e00-\u9fff]', article_match.group(1)):
        chinese = translate_simple(article_match.group(1))
        html = html.replace(
            f'<h2 class="article-title">{article_match.group(1)}</h2>',
            f'<h2 class="article-title">{chinese}</h2>'
        )
        changed = True
        print(f"      ✅ article-title")
    
    if changed:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    
    return False

def main():
    print("=" * 80)
    print("修复中文文章元数据")
    print("=" * 80)
    print()
    
    zh_dir = Path('insect/zh')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    fixed = 0
    
    for category in categories:
        cat_dir = zh_dir / category
        if not cat_dir.exists():
            continue
        
        print(f"\n📁 {category}")
        
        for article in sorted(cat_dir.glob('*.html')):
            if not article.name[0].isdigit():
                continue
            
            total += 1
            print(f"  [{total}/50] {article.name}")
            
            try:
                if fix_metadata(article):
                    fixed += 1
            except Exception as e:
                print(f"      ❌ 错误: {e}")
    
    print("\n" + "=" * 80)
    print(f"✅ 修复完成: {fixed}/{total} 篇")
    print("=" * 80)

if __name__ == '__main__':
    main()


