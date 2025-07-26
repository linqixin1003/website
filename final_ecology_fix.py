#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def clean_html_structure(content):
    """清理HTML结构问题"""
    # 移除多余的</div>标签在body开始处
    content = re.sub(r'<body>\s*</div>', '<body>', content)
    
    # 移除文章末尾多余的</div>标签
    content = re.sub(r'</main>\s*</div>\s*</body>', '</main>\n</body>', content)
    
    # 移除空的div标签
    content = re.sub(r'<div>\s*</div>', '', content)
    
    # 清理多余的空行
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content

def process_ecology_file(file_path):
    """处理单个ecology文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 清理HTML结构
        content = clean_html_structure(content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ 处理文件失败 {file_path}: {e}")
        return False

def main():
    print("🔧 最终修复ecology文章HTML结构问题")
    print("=" * 60)
    
    # 语言列表
    languages = ['en', 'zh', 'ko', 'ja', 'fr', 'de', 'pt', 'ru']
    
    # ecology文章列表
    articles = [
        '01-habitat-ecosystems.html',
        '02-food-webs-chains.html', 
        '03-migration-patterns.html',
        '04-breeding-ecology.html',
        '05-climate-change-impact.html',
        '06-urban-ecology.html',
        '07-conservation-biology.html',
        '08-island-biogeography.html',
        '09-pollination-seed-dispersal.html',
        '10-community-dynamics.html'
    ]
    
    total_files = 0
    fixed_files = 0
    
    for lang in languages:
        print(f"\n🌍 处理 {lang.upper()} 语言版本:")
        print("-" * 40)
        
        lang_fixed = 0
        for article in articles:
            file_path = Path(f"{lang}/ecology/{article}")
            
            if file_path.exists():
                if process_ecology_file(file_path):
                    print(f"✅ 修复: {file_path}")
                    fixed_files += 1
                    lang_fixed += 1
                else:
                    print(f"❌ 失败: {file_path}")
                total_files += 1
            else:
                print(f"⚠️  文件不存在: {file_path}")
        
        print(f"📊 {lang.upper()} 统计: {lang_fixed}/{len(articles)} 个文件已修复")
    
    print("\n" + "=" * 60)
    print("🎉 最终修复完成！")
    print(f"📊 总体统计:")
    print(f"  📁 总文件数: {total_files}")
    print(f"  🔧 修复文件数: {fixed_files}")
    print(f"  ✅ 修复率: {(fixed_files/total_files*100):.1f}%")
    
    print(f"\n🔧 修复内容:")
    print(f"  1. ✅ 清理多余的</div>标签")
    print(f"  2. ✅ 修复HTML结构问题")
    print(f"  3. ✅ 移除空的div元素")
    print(f"  4. ✅ 清理多余的空行")

if __name__ == "__main__":
    main()