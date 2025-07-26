#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def fix_spanish_header_images():
    """修正西班牙语JSON文件中的头图URL路径"""
    
    json_file = "android-article-urls-es.json"
    
    if not os.path.exists(json_file):
        print(f"⚠️ 文件不存在: {json_file}")
        return 0
        
    try:
        # 读取JSON文件
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        file_updated = False
        updated_articles = 0
        
        # 遍历所有分类
        for category_key, category_data in data.get("articleCategories", {}).items():
            articles = category_data.get("articles", [])
            
            for article in articles:
                image_url = article.get("imageUrl", "")
                article_id = article.get("id", "")
                
                # 检查是否是需要更新的文章
                if article_id == "08-urban-ecology" and "/images/headers/" in image_url:
                    # 修正路径：从 images/headers/ 改为 images/birds/species/
                    new_image_url = image_url.replace("/images/headers/08-urban-ecology.png", "/images/birds/species/head_urban_ecology.png")
                    article["imageUrl"] = new_image_url
                    
                    print(f"✅ 修正 {json_file} - {article.get('title', 'Unknown')}")
                    print(f"   旧路径: {image_url}")
                    print(f"   新路径: {new_image_url}")
                    file_updated = True
                    updated_articles += 1
        
        # 如果文件有更新，写回文件
        if file_updated:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"📝 已保存: {json_file}\n")
        else:
            print(f"ℹ️ 无需更新: {json_file}")
            
        return updated_articles
            
    except Exception as e:
        print(f"❌ 处理文件失败 {json_file}: {e}")
        return 0

if __name__ == "__main__":
    print("🚀 开始修正西班牙语JSON文件中的头图URL路径")
    print("="*60)
    
    updated_count = fix_spanish_header_images()
    
    print("="*60)
    print("🎉 西班牙语头图路径修正完成！")
    print(f"✅ 更新文章数: {updated_count}")
    print("\n修正的路径:")
    print("从: https://linqixin1003.github.io/website/images/headers/08-urban-ecology.png")
    print("到: https://linqixin1003.github.io/website/images/birds/species/head_urban_ecology.png")