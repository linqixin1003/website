#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
更新所有语言版本JSON文件中pc009条目的图片URL
将bird-image-090.png替换为head-enrichment-activities.png
"""

import json
import os

def update_enrichment_image(json_file):
    """更新单个JSON文件中pc009的图片URL"""
    print(f"\n📝 处理文件: {json_file}")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取JSON文件失败: {e}")
        return False
    
    # 查找并更新pc009条目
    updated = False
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            if article.get('id') == 'pc009':
                old_url = article.get('imageUrl', '')
                if 'bird-image-090.png' in old_url:
                    new_url = old_url.replace('bird-image-090.png', 'head-enrichment-activities.png')
                    article['imageUrl'] = new_url
                    updated = True
                    print(f"✅ 更新 pc009: {article.get('title', article.get('titleEn', ''))}")
                    print(f"   旧图片: bird-image-090.png")
                    print(f"   新图片: head-enrichment-activities.png")
                    break
    
    if updated:
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 文件已保存")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")
            return False
    else:
        print("ℹ️ 该文件无需更新")
    
    return updated

def main():
    """主函数"""
    json_files = [
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
    
    print("🔧 开始更新所有语言版本的pc009图片URL...")
    print("=" * 60)
    
    total_updated = 0
    
    for json_file in json_files:
        if os.path.exists(json_file):
            if update_enrichment_image(json_file):
                total_updated += 1
        else:
            print(f"\n❌ 文件不存在: {json_file}")
    
    print("\n" + "=" * 60)
    print(f"🎉 更新完成! 总共更新了 {total_updated} 个文件")
    print("📋 更新内容:")
    print("   文章ID: pc009 (Enrichment Activities)")
    print("   旧图片: bird-image-090.png")
    print("   新图片: head-enrichment-activities.png")

if __name__ == "__main__":
    main()