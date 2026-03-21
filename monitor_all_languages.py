#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""监控所有语言的翻译进度"""

import re
import sys
import time
from pathlib import Path
from datetime import datetime

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

def check_article(html_file):
    """检查文章翻译状态"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否有足够的非英文内容
        # 统计非ASCII字符（包括中文、德文、法文等）
        non_ascii = len([c for c in content if ord(c) > 127])
        ascii_letters = len(re.findall(r'[a-zA-Z]', content))
        
        if non_ascii > ascii_letters * 0.5:
            return True
        return False
    except:
        return False

def check_language(lang_code):
    """检查某个语言的翻译进度"""
    lang_dir = Path(f'insect/{lang_code}')
    if not lang_dir.exists():
        return 0, 50
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    completed = 0
    total = 0
    
    for category in categories:
        cat_dir = lang_dir / category
        if not cat_dir.exists():
            continue
        
        articles = [f for f in cat_dir.glob('*.html') if f.name[0].isdigit()]
        for article in articles:
            total += 1
            if check_article(article):
                completed += 1
    
    return completed, total

def main():
    print("\n" + "=" * 80)
    print("多语言翻译进度监控")
    print("=" * 80)
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    overall_completed = 0
    overall_total = 0
    
    for lang_code, lang_name in LANGUAGES.items():
        completed, total = check_language(lang_code)
        overall_completed += completed
        overall_total += total
        
        percent = (completed * 100 // total) if total > 0 else 0
        bar_length = 20
        filled = (completed * bar_length // total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        status = '✅' if completed == total else '🔄' if completed > 0 else '⏳'
        
        print(f"{status} {lang_name:8} [{bar}] {completed:2}/{total} ({percent:3}%)")
    
    print()
    print("=" * 80)
    overall_percent = (overall_completed * 100 // overall_total) if overall_total > 0 else 0
    print(f"总进度: {overall_completed}/{overall_total} ({overall_percent}%)")
    print("=" * 80)
    print()
    
    if overall_completed == overall_total:
        print("🎉 所有语言翻译完成！")
    else:
        remaining = overall_total - overall_completed
        print(f"剩余: {remaining} 篇")
        print(f"预计完成时间: 约 {remaining // 50} 小时")

if __name__ == '__main__':
    main()

