#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def fix_header_image_paths():
    """修正6个头图的URL路径 - 从 images/headers/ 改为 images/birds/"""
    
    # 需要修正的头图映射
    header_image_fixes = {
        "head_breeding_cology.png": "head_breeding_cology.png",
        "head_community_dynamics.png": "head_community_dynamics.png", 
        "head_conservation_biology.png": "head_conservation_biology.png",
        "head_island_biogeography.png": "head_island_biogeography.png",
        "head_pollination_seed_dispersal.png": "head_pollination_seed_dispersal.png",
        "head_urban_ecology.png": "head_urban_ecology.png"
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
                    image_url = article.get("imageUrl", "")
                    
                    # 检查是否包含错误的 headers 路径
                    if "/images/headers/" in image_url:
                        for header_image in header_image_fixes.keys():
                            if header_image in image_url:
                                # 修正路径：从 images/headers/ 改为 images/birds/
                                new_image_url = image_url.replace("/images/headers/", "/images/birds/")
                                article["imageUrl"] = new_image_url
                                
                                print(f"✅ 修正 {json_file} - {article.get('title', 'Unknown')}")
                                print(f"   旧路径: {image_url}")
                                print(f"   新路径: {new_image_url}")
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
    print("🎉 头图路径修正完成！")
    print(f"✅ 更新文件数: {updated_files}")
    print(f"✅ 更新文章数: {updated_articles}")
    print("\n修正的路径:")
    print("从: https://linqixin1003.github.io/website/images/headers/")
    print("到: https://linqixin1003.github.io/website/images/birds/")

if __name__ == "__main__":
    print("🚀 开始修正头图URL路径")
    print("="*60)
    fix_header_image_paths()