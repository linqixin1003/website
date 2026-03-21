#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查所有语言翻译的实际质量"""

import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = {
    'zh': '中文',
    'de': '德语', 
    'es': '西班牙语',
    'fr': '法语',
    'it': '意大利语',
    'ja': '日语',
    'ko': '韩语',
    'pt': '葡萄牙语',
    'ru': '俄语'
}

def check_article_translation(html_file, lang_code):
    """检查文章是否真正翻译了"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查lang属性
        if f'lang="{lang_code}"' not in content:
            return False, "lang属性未更新"
        
        # 检查title是否翻译（不应该还是英文）
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            title = title_match.group(1)
            # 如果title还包含很多英文单词，说明没翻译
            english_words = len(re.findall(r'\b[A-Z][a-z]+\b', title))
            if english_words > 3:
                return False, "title未翻译"
        
        # 检查正文段落
        paragraphs = re.findall(r'<p class="intro">(.*?)</p>', content, re.DOTALL)
        if paragraphs:
            text = paragraphs[0]
            # 统计英文单词
            english_words = len(re.findall(r'\b[a-zA-Z]{4,}\b', text))
            if english_words > 20:
                return False, "正文未翻译"
        
        return True, "已翻译"
    except Exception as e:
        return False, f"错误: {e}"

def main():
    print("=" * 80)
    print("多语言翻译质量检查")
    print("=" * 80)
    print()
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total_translated = 0
    total_files = 0
    
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"❌ {lang_name:8} - 目录不存在")
            continue
        
        translated = 0
        total = 0
        
        for category in categories:
            cat_dir = lang_dir / category
            if not cat_dir.exists():
                continue
            
            articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
            for article in articles:
                total += 1
                is_translated, reason = check_article_translation(article, lang_code)
                if is_translated:
                    translated += 1
        
        percent = (translated * 100 // total) if total > 0 else 0
        bar_length = 20
        filled = (translated * bar_length // total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        status = '✅' if translated == total else '⚠️ ' if translated > 0 else '❌'
        
        print(f"{status} {lang_name:10} [{bar}] {translated:2}/{total} ({percent:3}%)")
        
        total_translated += translated
        total_files += total
    
    print()
    print("=" * 80)
    overall_percent = (total_translated * 100 // total_files) if total_files > 0 else 0
    print(f"总进度: {total_translated}/{total_files} ({overall_percent}%)")
    print("=" * 80)
    
    if total_translated == total_files:
        print("\n🎉 所有语言翻译完成并通过质量检查！")
    elif total_translated > 0:
        print(f"\n✅ 已翻译 {total_translated} 篇文章")
        print(f"⏳ 还需检查/修复 {total_files - total_translated} 篇")

if __name__ == '__main__':
    main()

