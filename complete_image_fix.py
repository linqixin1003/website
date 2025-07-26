#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
完整的图片URL修复脚本
修复所有发现的问题
"""

import json
import os

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
    
    # 需要修复的图片映射
    fixes = {
        "kn001": "bird-image-015.png",  # 修复不匹配的图片
        "kn002": "bird-image-062.png",  # 保持原有图片
        "pc009": "bird-image-090.png",  # 修复重复图片
        "pc010": "bird-image-025.png"   # 修复重复图片
    }
    
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            article_id = article.get('id')
            current_image_url = article.get('imageUrl', '')
            
            if article_id in fixes:
                correct_image_filename = fixes[article_id]
                correct_image_url = f"https://linqixin1003.github.io/website/images/birds/species/{correct_image_filename}"
                
                if current_image_url != correct_image_url:
                    article['imageUrl'] = correct_image_url
                    changes_count += 1
                    print(f"✓ 更新 {article_id}: {article.get('title', article.get('titleEn', ''))}")
                    print(f"  新图片: {correct_image_filename}")
    
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