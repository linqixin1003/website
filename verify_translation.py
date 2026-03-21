#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证翻译完成度和质量"""

import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_article_translation(html_file):
    """检查文章是否已翻译成中文"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有段落文本
    paragraphs = re.findall(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', content, re.DOTALL)
    
    if not paragraphs:
        return {'translated': False, 'reason': '无段落'}
    
    # 检查是否包含中文
    has_chinese = False
    has_english = False
    
    for p in paragraphs:
        text = re.sub(r'<[^>]+>', '', p).strip()
        if not text:
            continue
        
        if re.search(r'[\u4e00-\u9fff]', text):
            has_chinese = True
        if re.search(r'[a-zA-Z]{10,}', text):
            has_english = True
    
    if has_chinese and not has_english:
        return {'translated': True, 'status': '✅ 完全翻译'}
    elif has_chinese and has_english:
        return {'translated': True, 'status': '⚠️  部分翻译'}
    else:
        return {'translated': False, 'status': '❌ 未翻译'}

def main():
    print("=" * 80)
    print("验证中文翻译完成度")
    print("=" * 80)
    print()
    
    zh_dir = Path('insect/zh')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    fully_translated = 0
    partially_translated = 0
    not_translated = 0
    
    for category in categories:
        cat_dir = zh_dir / category
        if not cat_dir.exists():
            continue
        
        print(f"\n{category}")
        print("-" * 60)
        
        articles = sorted([f for f in cat_dir.glob('*.html') if f.name[0].isdigit()])
        
        for article in articles:
            total += 1
            result = check_article_translation(article)
            
            if result.get('translated'):
                if '完全' in result['status']:
                    fully_translated += 1
                else:
                    partially_translated += 1
            else:
                not_translated += 1
            
            print(f"  {result['status']} {article.name}")
    
    print("\n" + "=" * 80)
    print("统计")
    print("=" * 80)
    print(f"总文章数: {total}")
    print(f"完全翻译: {fully_translated} ({fully_translated*100//total if total > 0 else 0}%)")
    print(f"部分翻译: {partially_translated}")
    print(f"未翻译: {not_translated}")
    
    if fully_translated == total:
        print("\n🎉 所有文章已完全翻译！")
    elif fully_translated > 0:
        print(f"\n🔄 翻译进行中... ({fully_translated}/{total})")
    else:
        print("\n⏳ 翻译尚未开始或正在准备中...")

if __name__ == '__main__':
    main()


