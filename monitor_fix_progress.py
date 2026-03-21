#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""监控修复进度"""

import re
import sys
import time
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_progress():
    """检查修复进度"""
    log_file = Path("fix_progress.txt")
    
    if not log_file.exists():
        print("⏳ 日志文件还未生成，脚本正在启动...")
        return
    
    print("=" * 80)
    print("📊 修复进度监控")
    print("=" * 80)
    print()
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取当前处理的语言
        current_lang = re.findall(r'🚀 (\w+) \((\w+)\) - 修复 (\d+) 篇文章', content)
        if current_lang:
            last_lang = current_lang[-1]
            print(f"🌐 当前语言: {last_lang[0]} ({last_lang[1]}) - 总共 {last_lang[2]} 篇")
            print()
        
        # 提取处理进度
        progress_matches = re.findall(r'\[(\d+)/(\d+)\]', content)
        if progress_matches:
            current, total = progress_matches[-1]
            percentage = int(current) / int(total) * 100
            print(f"📈 当前语言进度: {current}/{total} ({percentage:.1f}%)")
            
            # 进度条
            bar_length = 50
            filled = int(bar_length * int(current) / int(total))
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"    [{bar}]")
            print()
        
        # 提取成功/失败数
        success_count = len(re.findall(r'✅', content))
        failed_count = len(re.findall(r'❌ 翻译失败', content))
        
        print(f"✅ 已成功: {success_count} 个段落")
        print(f"❌ 失败: {failed_count} 个段落")
        print()
        
        # 提取完成的语言
        completed_langs = re.findall(r'⏱️  (\w+) 完成，用时: ([\d.]+)分钟', content)
        if completed_langs:
            print("🎉 已完成语言:")
            for lang, duration in completed_langs:
                print(f"  • {lang}: {duration}分钟")
            print()
        
        # 最后几行
        lines = content.strip().split('\n')
        if len(lines) > 0:
            print("📝 最近活动:")
            for line in lines[-5:]:
                if line.strip():
                    print(f"  {line}")
    
    except Exception as e:
        print(f"❌ 读取日志出错: {e}")
    
    print()
    print("=" * 80)

if __name__ == '__main__':
    while True:
        check_progress()
        time.sleep(30)  # 每30秒更新一次

