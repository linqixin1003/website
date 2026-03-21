#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通过文件修改时间检查翻译进度"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

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

def main():
    print("=" * 80)
    print("基于修改时间的翻译进度检查")
    print("=" * 80)
    print()
    
    # 获取最近2小时内的时间戳
    now = datetime.now()
    recent_threshold = now - timedelta(hours=2)
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total_recent = 0
    total_files = 0
    
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"❌ {lang_name:10} - 目录不存在")
            continue
        
        recent_count = 0
        total = 0
        
        for category in categories:
            cat_dir = lang_dir / category
            if not cat_dir.exists():
                continue
            
            articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
            for article in articles:
                total += 1
                # 检查文件修改时间
                mtime = datetime.fromtimestamp(article.stat().st_mtime)
                if mtime >= recent_threshold:
                    recent_count += 1
        
        percent = (recent_count * 100 // total) if total > 0 else 0
        bar_length = 20
        filled = (recent_count * bar_length // total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        status = '✅' if recent_count == total else '⚠️ ' if recent_count > 0 else '❌'
        
        print(f"{status} {lang_name:10} [{bar}] {recent_count:2}/{total} ({percent:3}%) 最近修改")
        
        total_recent += recent_count
        total_files += total
    
    print()
    print("=" * 80)
    overall_percent = (total_recent * 100 // total_files) if total_files > 0 else 0
    print(f"总进度: {total_recent}/{total_files} ({overall_percent}%) 在最近2小时内修改")
    print("=" * 80)
    
    if total_recent == total_files:
        print("\n🎉🎉🎉 所有文件最近都已更新！翻译很可能已完成！")
    elif total_recent >= total_files * 0.9:
        print(f"\n🎉 接近完成！{total_recent}篇文件最近已更新")
    else:
        print(f"\n⏳ {total_recent}篇文件最近已更新")

if __name__ == '__main__':
    main()

