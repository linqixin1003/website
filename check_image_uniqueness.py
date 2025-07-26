#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查每个分类中图片的唯一性，确保同一分类下的文章使用不同的头图
"""

import json
import os
from collections import defaultdict

def check_image_uniqueness():
    """检查图片使用的唯一性"""
    
    json_file = "android-article-urls-en.json"
    
    if not os.path.exists(json_file):
        print(f"❌ 文件不存在: {json_file}")
        return
    
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("🔍 检查各分类的图片使用情况:")
    print("=" * 60)
    
    for category_key, category_data in data['articleCategories'].items():
        print(f"\n📂 分类: {category_key}")
        print("-" * 40)
        
        image_usage = defaultdict(list)
        
        for article in category_data.get('articles', []):
            article_id = article.get('id')
            image_url = article.get('imageUrl', '')
            
            # 提取图片文件名
            if 'bird-image-' in image_url:
                image_name = image_url.split('/')[-1]
                image_usage[image_name].append(article_id)
                print(f"  {article_id}: {image_name}")
            else:
                print(f"  {article_id}: ❌ 无效图片 URL")
        
        # 检查重复使用的图片
        print(f"\n🔍 重复使用的图片:")
        duplicates_found = False
        for image_name, article_ids in image_usage.items():
            if len(article_ids) > 1:
                print(f"  ⚠️  {image_name} 被使用了 {len(article_ids)} 次: {', '.join(article_ids)}")
                duplicates_found = True
        
        if not duplicates_found:
            print(f"  ✅ 该分类中所有图片都是唯一的")

if __name__ == "__main__":
    check_image_uniqueness()