#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""监控翻译进度"""

import re
import sys
import time
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_translation(html_file):
    """检查文章翻译状态"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有中文
    has_chinese = bool(re.search(r'[\u4e00-\u9fff]{10,}', content))
    
    # 检查lang属性
    correct_lang = '<html lang="zh">' in content
    
    # 计算中文字符比例
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    english_words = len(re.findall(r'\b[a-zA-Z]+\b', content))
    
    if chinese_chars > english_words * 2:
        return '✅ 完全'
    elif has_chinese:
        return '⚠️  部分'
    else:
        return '❌ 未翻译'

def main():
    while True:
        print("\033[2J\033[H")  # 清屏
        print("=" * 80)
        print("DeepSeek 翻译进度监控")
        print("=" * 80)
        print(f"更新时间: {time.strftime('%H:%M:%S')}")
        print()
        
        zh_dir = Path('insect/zh')
        categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                      'pest-management', 'behavior-evolution']
        
        total = 0
        complete = 0
        partial = 0
        
        for category in categories:
            cat_dir = zh_dir / category
            if not cat_dir.exists():
                continue
            
            print(f"\n{category}")
            articles = sorted([f for f in cat_dir.glob('*.html') if f.name[0].isdigit()])
            
            for article in articles:
                total += 1
                status = check_translation(article)
                print(f"  {status} {article.name}")
                
                if '完全' in status:
                    complete += 1
                elif '部分' in status:
                    partial += 1
        
        percent = complete * 100 // total if total > 0 else 0
        print(f"\n进度: {complete}/{total} ({percent}%)")
        print("=" * 80)
        
        if complete == total:
            print("\n🎉 翻译完成！")
            break
        
        print("\n按Ctrl+C停止监控...")
        time.sleep(10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n监控已停止")


