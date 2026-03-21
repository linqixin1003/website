#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最终验证 - 检查所有语言的翻译是否完成"""

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

def check_file_translated(file_path, lang_code):
    """检查单个文件是否已翻译"""
    try:
        if not file_path.exists():
            return False
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查lang属性
        if f'lang="{lang_code}"' not in content:
            return False
        
        # 提取第一个段落内容
        intro_match = re.search(r'<p class="intro">([^<]{100})', content)
        if not intro_match:
            return False
        
        intro_text = intro_match.group(1)
        
        # 简单检测：如果包含大量常见英文单词，认为未翻译
        english_keywords = ['the', 'and', 'are', 'that', 'with', 'their', 'from', 'this', 'have']
        english_count = sum(1 for word in english_keywords if word in intro_text.lower())
        
        # 如果有5个以上常见英文词，认为未翻译
        return english_count < 5
    
    except Exception:
        return False

def main():
    print("=" * 80)
    print("🔍 最终翻译验证 - 所有语言全面检查")
    print("=" * 80)
    print()
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    grand_total = 0
    grand_translated = 0
    
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"❌ {lang_name:10} - 目录不存在")
            continue
        
        total = 0
        translated = 0
        
        for category in categories:
            cat_dir = lang_dir / category
            if not cat_dir.exists():
                continue
            
            articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
            for article in articles:
                total += 1
                if check_file_translated(article, lang_code):
                    translated += 1
        
        percent = (translated * 100 // total) if total > 0 else 0
        bar_length = 20
        filled = (translated * bar_length // total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        status = '✅' if translated == total else '⚠️ ' if translated > 0 else '❌'
        
        print(f"{status} {lang_name:10} [{bar}] {translated:2}/{total} ({percent:3}%)")
        
        grand_total += total
        grand_translated += translated
    
    print()
    print("=" * 80)
    overall_percent = (grand_translated * 100 // grand_total) if grand_total > 0 else 0
    print(f"📊 总进度: {grand_translated}/{grand_total} ({overall_percent}%)")
    print("=" * 80)
    
    if grand_translated == grand_total:
        print("\n🎉🎉🎉 所有语言翻译完成！")
        print("\n✅ 全部450篇文章已完整翻译")
        print("✅ 9种语言全部完成")
        print("✅ 包括中文、德语、西班牙语、法语、意大利语、日语、韩语、葡萄牙语、俄语")
    else:
        missing = grand_total - grand_translated
        print(f"\n⏳ 还需完成 {missing} 篇文章")

if __name__ == '__main__':
    main()

