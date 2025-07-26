#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def update_json_header_images():
    """更新所有JSON文件中的6个特定头图URL"""
    
    # 头图映射关系
    header_image_mapping = {
        "04-breeding-ecology.html": "head_breeding_cology.png",
        "10-community-dynamics.html": "head_community_dynamics.png", 
        "07-conservation-biology.html": "head_conservation_biology.png",
        "08-island-biogeography.html": "head_island_biogeography.png",
        "09-pollination-seed-dispersal.html": "head_pollination_seed_dispersal.png",
        "06-urban-ecology.html": "head_urban_ecology.png"
    }
    
    # 需要更新的JSON文件列表
    json_files = [
        "android-article-urls-de.json",
        "android-article-urls-en.json", 
        "android-article-urls-es.json",
        "android-article-urls-fr.json",
        "android-article-urls-it.json",
        "android-article-urls-ja.json",
        "android-article-urls-ko.json",
        "android-article-urls-pt.json",
        "android-article-urls-ru.json",
        "android-article-urls-zh.json"
    ]
    
    updated_files = 0
    updated_articles = 0
    
    for json_file in json_files:
        if not os.path.exists(json_file):
            print(f"⚠️ 文件不存在: {json_file}")
            continue
            
        try:
            # 读取JSON文件
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            file_updated = False
            
            # 遍历所有分类
            for category_key, category_data in data.get("articleCategories", {}).items():
                articles = category_data.get("articles", [])
                
                for article in articles:
                    article_url = article.get("url", "")
                    
                    # 检查是否是需要更新头图的文章
                    for html_file, header_image in header_image_mapping.items():
                        if html_file in article_url:
                            # 更新头图URL
                            old_image_url = article.get("imageUrl", "")
                            new_image_url = f"https://linqixin1003.github.io/website/images/headers/{header_image}"
                            
                            if old_image_url != new_image_url:
                                article["imageUrl"] = new_image_url
                                print(f"✅ 更新 {json_file} - {article.get('title', 'Unknown')}")
                                print(f"   旧头图: {old_image_url}")
                                print(f"   新头图: {new_image_url}")
                                file_updated = True
                                updated_articles += 1
                            break
            
            # 如果文件有更新，写回文件
            if file_updated:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                updated_files += 1
                print(f"📝 已保存: {json_file}\n")
            else:
                print(f"ℹ️ 无需更新: {json_file}")
                
        except Exception as e:
            print(f"❌ 处理文件失败 {json_file}: {e}")
    
    print("="*60)
    print("🎉 头图更新完成！")
    print(f"✅ 更新文件数: {updated_files}")
    print(f"✅ 更新文章数: {updated_articles}")
    print("\n更新的头图:")
    for html_file, header_image in header_image_mapping.items():
        print(f"- {html_file} → {header_image}")

if __name__ == "__main__":
    print("🚀 开始更新JSON文件中的头图URL")
    print("="*60)
    update_json_header_images()