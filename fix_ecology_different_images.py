#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
为 Ecology 分类的每篇文章分配不同的头图，确保同一分类下不使用相同图片
"""

import json
import os

def fix_ecology_different_images():
    """为 ecology 分类分配不同的头图"""
    
    # 为 ecology 分类的 10 篇文章分配不同的头图
    ecology_image_mapping = {
        "ec001": "bird-image-075.png",  # 鸟类栖息地与生态系统
        "ec002": "bird-image-076.png",  # 食物网与食物链
        "ec003": "bird-image-077.png",  # 鸟类迁徙模式
        "ec004": "bird-image-078.png",  # 繁殖生态学
        "ec005": "bird-image-079.png",  # 气候变化影响
        "ec006": "bird-image-081.png",  # 城市鸟类生态学
        "ec007": "bird-image-082.png",  # 鸟类保护生物学
        "ec008": "bird-image-083.png",  # 岛屿生物地理学
        "ec009": "bird-image-084.png",  # 授粉与种子传播
        "ec010": "bird-image-085.png",  # 鸟类群落动态
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
        
        # 处理 ecology 分类
        if 'ecology' in data['articleCategories']:
            ecology_articles = data['articleCategories']['ecology']['articles']
            
            for article in ecology_articles:
                article_id = article.get('id')
                if article_id in ecology_image_mapping:
                    new_image_name = ecology_image_mapping[article_id]
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
    fix_ecology_different_images()