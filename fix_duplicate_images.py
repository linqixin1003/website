#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复所有分类中重复使用的图片，确保每个分类内的图片都是唯一的
"""

import json
import os

def fix_duplicate_images():
    """修复重复使用的图片"""
    
    # petCare 分类的图片修复映射
    petcare_image_mapping = {
        "pc001": "bird-image-015.png",  # 选择合适的宠物鸟
        "pc002": "bird-image-020.png",  # 鸟类营养与喂养
        "pc003": "bird-image-030.png",  # 鸟类住房与环境
        "pc004": "bird-image-040.png",  # 鸟类健康与兽医护理
        "pc005": "bird-image-050.png",  # 鸟类训练与行为
        "pc006": "bird-image-060.png",  # 鸟类繁殖与生殖
        "pc007": "bird-image-070.png",  # 紧急护理与急救
        "pc008": "bird-image-080.png",  # 季节性护理指南
        "pc009": "bird-image-035.png",  # 丰富活动 - 改为不同图片
        "pc010": "bird-image-021.png",  # 老年鸟护理 - 改为不同图片
    }
    
    # 所有语言版本的 JSON 文件
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
        if not os.path.exists(json_file):
            print(f"❌ 文件不存在: {json_file}")
            continue
            
        print(f"\n📝 处理文件: {json_file}")
        
        # 读取 JSON 文件
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changes_count = 0
        
        # 处理 petCare 分类
        if 'petCare' in data['articleCategories']:
            petcare_articles = data['articleCategories']['petCare']['articles']
            
            for article in petcare_articles:
                article_id = article.get('id')
                if article_id in petcare_image_mapping:
                    new_image_name = petcare_image_mapping[article_id]
                    new_image_url = f"https://linqixin1003.github.io/website/images/birds/species/{new_image_name}"
                    
                    old_url = article.get('imageUrl', '')
                    if old_url != new_image_url:
                        article['imageUrl'] = new_image_url
                        changes_count += 1
                        print(f"✓ 更新 {article_id}: {article.get('title', article.get('titleEn', ''))}")
                        print(f"  新图片: {new_image_name}")
        
        # 保存修改后的文件
        if changes_count > 0:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 总共修改了 {changes_count} 个图片 URL")
        else:
            print("= 没有需要修改的图片 URL")

if __name__ == "__main__":
    fix_duplicate_images()