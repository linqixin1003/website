#!/usr/bin/env python3
"""
最终验证所有德语文章的头部图片是否与英语版本匹配
"""

import os
import re
from pathlib import Path

def extract_header_image(file_path):
    """提取文件的头部图片路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS背景图片
        css_match = re.search(r"url\('(../../images/[^']+)'\)", content)
        if css_match:
            return css_match.group(1)
        
        # 查找HTML img标签
        img_match = re.search(r'<img[^>]+src="(../../images/[^"]+)"[^>]*>', content)
        if img_match:
            return img_match.group(1)
        
        return None
        
    except Exception as e:
        return None

def find_all_html_files(directory):
    """查找目录下所有HTML文件"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    """主函数"""
    print("🔍 最终验证所有德语文章的头部图片...")
    
    # 获取所有德语HTML文件
    de_files = find_all_html_files('de')
    de_files = [f for f in de_files if not f.endswith('knowledge.html') and not f.endswith('index.html')]
    
    total_files = 0
    matched_files = 0
    mismatched_files = 0
    missing_files = 0
    
    print("\n📋 检查结果:")
    print("=" * 80)
    
    for de_file in sorted(de_files):
        # 构造对应的英语文件路径
        en_file = de_file.replace('de/', 'en/')
        
        if os.path.exists(en_file):
            total_files += 1
            de_image = extract_header_image(de_file)
            en_image = extract_header_image(en_file)
            
            if de_image and en_image:
                if de_image == en_image:
                    print(f"✅ {de_file}")
                    print(f"   图片: {de_image}")
                    matched_files += 1
                else:
                    print(f"❌ {de_file}")
                    print(f"   德语: {de_image}")
                    print(f"   英语: {en_image}")
                    mismatched_files += 1
            elif not de_image and not en_image:
                print(f"⚪ {de_file} (两个版本都没有头部图片)")
                matched_files += 1
            else:
                print(f"⚠️  {de_file}")
                print(f"   德语: {de_image or '无'}")
                print(f"   英语: {en_image or '无'}")
                mismatched_files += 1
        else:
            print(f"❓ {de_file} (对应英语文件不存在)")
            missing_files += 1
    
    print("=" * 80)
    print(f"\n📊 最终统计:")
    print(f"   总德语文件数: {len(de_files)}")
    print(f"   有对应英语文件: {total_files}")
    print(f"   头部图片匹配: {matched_files}")
    print(f"   头部图片不匹配: {mismatched_files}")
    print(f"   英语文件缺失: {missing_files}")
    
    if mismatched_files == 0:
        print("🎉 所有德语文章的头部图片都与英语版本完美匹配!")
    else:
        print(f"⚠️  还有 {mismatched_files} 个文件的头部图片需要修复")
        
    # 计算匹配率
    if total_files > 0:
        match_rate = (matched_files / total_files) * 100
        print(f"📈 头部图片匹配率: {match_rate:.1f}%")

if __name__ == "__main__":
    main()