#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复所有JSON文件中的imageUrl，确保对应正确的文章头图
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

def fix_json_file(json_file):
    """修复单个JSON文件的图片URL"""
    print(f"\n📝 处理文件: {json_file}")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取JSON文件失败: {e}")
        return 0
    
    changes_count = 0
    
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            article_id = article.get('id')
            article_url = article.get('url', '')
            current_image_url = article.get('imageUrl', '')
            
            # 构建HTML文件路径
            html_file_path = f"en{article_url}"
            
            if os.path.exists(html_file_path):
                # 从HTML文件中提取实际的头图
                actual_image_filename = extract_image_from_html(html_file_path)
                
                if actual_image_filename:
                    # 构建正确的图片URL
                    correct_image_url = f"https://linqixin1003.github.io/website/images/birds/species/{actual_image_filename}"
                    
                    if current_image_url != correct_image_url:
                        article['imageUrl'] = correct_image_url
                        changes_count += 1
                        print(f"✓ 更新 {article_id}: {article.get('title', article.get('titleEn', ''))}")
                        print(f"  新图片: {actual_image_filename}")
    
    # 保存修改后的文件
    if changes_count > 0:
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 总共修改了 {changes_count} 个图片 URL")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")
            return 0
    else:
        print("✅ 该文件无需修改")
    
    return changes_count

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
    
    print("🔧 开始修复所有JSON文件的图片URL...")
    print("=" * 60)
    
    total_changes = 0
    
    for json_file in json_files:
        if os.path.exists(json_file):
            changes = fix_json_file(json_file)
            total_changes += changes
        else:
            print(f"\n❌ 文件不存在: {json_file}")
    
    print("\n" + "=" * 60)
    print(f"🎉 修复完成! 总共修改了 {total_changes} 个图片URL")

if __name__ == "__main__":
    main()