#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""持续监控翻译进度"""

import re
import sys
import time
from pathlib import Path
from datetime import datetime

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_article(html_file):
    """检查文章翻译状态"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
        english_words = len(re.findall(r'\b[a-zA-Z]{3,}\b', content))
        
        if chinese_chars > english_words * 2:
            return '✅'
        elif chinese_chars > english_words * 0.5:
            return '⚠️ '
        else:
            return '❌'
    except:
        return '❌'

def show_progress():
    """显示进度"""
    zh_dir = Path('insect/zh')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    complete = 0
    partial = 0
    pending = 0
    
    print(f"\n{'='*80}")
    print(f"翻译进度 - {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*80}\n")
    
    for category in categories:
        cat_dir = zh_dir / category
        if not cat_dir.exists():
            continue
        
        cat_name = category.replace('-', ' ').title()
        articles = sorted([f for f in cat_dir.glob('*.html') if f.name[0].isdigit()])
        
        cat_complete = 0
        for article in articles:
            status = check_article(article)
            if '✅' in status:
                cat_complete += 1
                complete += 1
            elif '⚠️' in status:
                partial += 1
            else:
                pending += 1
        
        progress_bar = '█' * cat_complete + '░' * (10 - cat_complete)
        print(f"{cat_name:25} [{progress_bar}] {cat_complete}/10")
    
    total = complete + partial + pending
    percent = (complete * 100) // total if total > 0 else 0
    
    print(f"\n{'='*80}")
    print(f"总计: ✅ {complete}  ⚠️  {partial}  ❌ {pending}  |  {percent}% 完成")
    print(f"{'='*80}\n")
    
    return complete, total

def main():
    print("🔄 开始监控翻译进度...")
    print("按 Ctrl+C 停止\n")
    
    last_count = 0
    check_count = 0
    
    try:
        while True:
            complete, total = show_progress()
            
            if complete > last_count:
                print(f"📈 新完成 {complete - last_count} 篇！\n")
                last_count = complete
            
            if complete == total:
                print("🎉 所有文章翻译完成！\n")
                break
            
            check_count += 1
            if check_count % 3 == 0:
                print("💡 提示: 翻译需要时间，请耐心等待...\n")
            
            print(f"下次检查: 30秒后...")
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\n⏸️  监控已停止")
        print(f"当前进度: {last_count}/{total}\n")

if __name__ == '__main__':
    main()

