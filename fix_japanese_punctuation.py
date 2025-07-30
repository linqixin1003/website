#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_japanese_punctuation(content):
    """修复日文标点符号"""
    # 替换英文标点为日文标点
    replacements = [
        (r'\.(?=\s|$)', '。'),  # 句号
        (r',(?=\s)', '、'),     # 逗号
        (r'!(?=\s|$)', '！'),   # 感叹号
        (r'\?(?=\s|$)', '？'),  # 问号
        (r':(?=\s)', '：'),     # 冒号
        (r';(?=\s)', '；'),     # 分号
        (r'"([^"]*)"', '「\\1」'),  # 引号
        (r"'([^']*)'", '『\\1』'),  # 单引号
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    return content

def process_japanese_files():
    """处理所有日文生态学文章"""
    japanese_files = [
        'ja/ecology/03-migration-patterns.html',
        'ja/ecology/05-climate-change-impact.html', 
        'ja/ecology/06-urban-ecology.html',
        'ja/ecology/07-conservation-biology.html',
        'ja/ecology/08-island-biogeography.html',
        'ja/ecology/09-pollination-seed-dispersal.html',
        'ja/ecology/10-community-dynamics.html'
    ]
    
    for file_path in japanese_files:
        if os.path.exists(file_path):
            print(f"修复日文标点: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 只修复HTML内容中的日文文本，不影响HTML标签和属性
            # 使用更精确的正则表达式来匹配日文内容区域
            def fix_text_content(match):
                text = match.group(1)
                if any('\u3040' <= char <= '\u309F' or '\u30A0' <= char <= '\u30FF' or '\u4E00' <= char <= '\u9FAF' for char in text):
                    return f'>{fix_japanese_punctuation(text)}<'
                return match.group(0)
            
            # 修复标签之间的文本内容
            content = re.sub(r'>([^<]+)<', fix_text_content, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ 已修复: {file_path}")
        else:
            print(f"❌ 文件不存在: {file_path}")

if __name__ == "__main__":
    print("开始修复日文标点符号...")
    process_japanese_files()
    print("日文标点修复完成！")