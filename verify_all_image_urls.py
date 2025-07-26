#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
验证所有JSON文件中的imageUrl是否对应正确的文章头图
"""

import json
import os
import re
from pathlib import Path

def extract_image_from_html(html_file_path):
    """从HTML文件中提取头图URL"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS中的background属性
        pattern = r'background:\s*linear-gradient[^,]+,\s*url\(["\']?([^"\']+)["\']?\)'
        match = re.search(pattern, content)
        
        if match:
            image_path = match.group(1)
            # 提取文件名
            image_filename = os.path.basename(image_path)
            return image_filename
        
        return None
    except Exception as e:
        print(f"❌ 读取HTML文件失败 {html_file_path}: {e}")
        return None

def verify_json_file(json_file):
    """验证单个JSON文件的图片URL"""
    print(f"\n🔍 验证文件: {json_file}")
    print("=" * 60)
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取JSON文件失败: {e}")
        return False
    
    all_correct = True
    
    for category_key, category_data in data['articleCategories'].items():
        print(f"\n📂 分类: {category_key}")
        print("-" * 40)
        
        for article in category_data.get('articles', []):
            article_id = article.get('id')
            article_url = article.get('url', '')
            current_image_url = article.get('imageUrl', '')
            
            # 从imageUrl中提取图片文件名
            current_image_filename = os.path.basename(current_image_url) if current_image_url else ''
            
            # 构建HTML文件路径
            html_file_path = f"en{article_url}"
            
            if os.path.exists(html_file_path):
                # 从HTML文件中提取实际的头图
                actual_image_filename = extract_image_from_html(html_file_path)
                
                if actual_image_filename:
                    if current_image_filename == actual_image_filename:
                        print(f"  ✅ {article_id}: {current_image_filename}")
                    else:
                        print(f"  ❌ {article_id}: 不匹配!")
                        print(f"      当前: {current_image_filename}")
                        print(f"      应为: {actual_image_filename}")
                        all_correct = False
                else:
                    print(f"  ⚠️  {article_id}: 无法从HTML中提取头图")
                    all_correct = False
            else:
                print(f"  ❌ {article_id}: HTML文件不存在 {html_file_path}")
                all_correct = False
    
    return all_correct

def main():
    """主函数"""
    json_files = [
        "android-article-urls-en.json",
        "android-article-urls-zh.json", 
        "android-article-urls-ja.json",
        "android-article-urls-ko.json",
        "android-article-urls-fr.json",
        "android-article-urls-es.json",
        "android-article-urls-de.json",
        "android-article-urls-it.json",
        "android-article-urls-pt.json",
        "android-article-urls-ru.json"
    ]
    
    print("🔍 开始验证所有JSON文件的图片URL...")
    print("=" * 80)
    
    all_files_correct = True
    
    for json_file in json_files:
        if os.path.exists(json_file):
            file_correct = verify_json_file(json_file)
            if not file_correct:
                all_files_correct = False
        else:
            print(f"\n❌ 文件不存在: {json_file}")
            all_files_correct = False
    
    print("\n" + "=" * 80)
    if all_files_correct:
        print("🎉 所有JSON文件的图片URL都正确对应了文章头图!")
    else:
        print("⚠️  发现一些图片URL不匹配，需要修复")

if __name__ == "__main__":
    main()