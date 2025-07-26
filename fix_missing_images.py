#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复缺失图片 URL 的文章
为没有头图的 HTML 文件设置合适的默认图片
"""

import json
import os
import re

def fix_missing_images(json_file):
    """修复缺失图片的文章"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 记录修改数量
    changes_count = 0
    
    # 为不同分类设置默认图片映射
    default_images = {
        'knowledge': {
            'kn002': 'bird-image-062.png'  # Essential Equipment
        },
        'ecology': {
            'ec001': 'bird-image-075.png',  # Habitat Ecosystems
            'ec002': 'bird-image-080.png',  # Food Webs
            'ec003': 'bird-image-022.png',  # Migration Patterns
            'ec004': 'bird-image-070.png',  # Breeding Ecology
            'ec005': 'bird-image-006.png',  # Climate Change
            'ec006': 'bird-image-071.png',  # Urban Ecology
            'ec007': 'bird-image-042.png',  # Conservation Biology
            'ec008': 'bird-image-014.png',  # Island Biogeography
            'ec009': 'bird-image-034.png',  # Pollination
            'ec010': 'bird-image-007.png'   # Community Dynamics
        }
    }
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        if category_key in default_images:
            for article in category_data.get('articles', []):
                article_id = article.get('id')
                
                if article_id in default_images[category_key]:
                    # 构建新的图片 URL
                    image_filename = default_images[category_key][article_id]
                    new_image_url = f"https://linqixin1003.github.io/website/images/birds/species/{image_filename}"
                    
                    # 检查当前 URL 是否需要更新
                    current_url = article.get('imageUrl', '')
                    if 'headers' in current_url or current_url != new_image_url:
                        old_url = current_url
                        article['imageUrl'] = new_image_url
                        changes_count += 1
                        print(f"✓ 更新 {article_id}: {article.get('title', 'Unknown')}")
                        print(f"  旧 URL: {old_url}")
                        print(f"  新 URL: {new_image_url}")
    
    # 保存修改后的 JSON 文件
    if changes_count > 0:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 总共修改了 {changes_count} 个图片 URL")
    else:
        print("没有需要修改的图片 URL")

if __name__ == "__main__":
    json_files = [
        "android-article-urls-en.json",
        "android-article-urls-zh.json", 
        "android-article-urls-ja.json",
        "android-article-urls-ko.json",
        "android-article-urls-fr.json",
        "android-article-urls-de.json",
        "android-article-urls-it.json",
        "android-article-urls-pt.json",
        "android-article-urls-ru.json",
    ]
    
    for json_file in json_files:
        if os.path.exists(json_file):
            print(f"\n📝 处理文件: {json_file}")
            fix_missing_images(json_file)
        else:
            print(f"❌ 文件不存在: {json_file}")