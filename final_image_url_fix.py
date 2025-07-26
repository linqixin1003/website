#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
最终图片URL修复脚本
基于之前成功提取的图片信息来修复所有JSON文件
"""

import json
import os

# 基于之前成功提取的图片映射
IMAGE_MAPPING = {
    # birdwatching 分类
    "bw001": "bird-image-002.png",
    "bw002": "bird-image-001.png", 
    "bw003": "bird-image-007.png",
    "bw004": "bird-image-001-alt-1.png",
    "bw005": "bird-image-006.png",
    "bw006": "bird-image-005.png",
    "bw007": "bird-image-008.png",
    "bw008": "bird-image-003.png",
    "bw009": "bird-image-009.png",
    "bw010": "bird-image-004.png",
    
    # knowledge 分类
    "kn001": "bird-image-001.png",
    "kn002": "bird-image-062.png",
    "kn003": "bird-image-003.png",
    "kn004": "bird-image-004.png",
    "kn005": "bird-image-005.png",
    "kn006": "bird-image-006.png",
    "kn007": "bird-image-007.png",
    "kn008": "bird-image-008.png",
    "kn009": "bird-image-009.png",
    "kn010": "bird-image-010.png",
    
    # ecology 分类 (使用专用头图)
    "ec001": "bird-image-075.png",
    "ec002": "bird-image-076.png",
    "ec003": "bird-image-077.png",
    "ec004": "head_breeding_cology.png",        # 繁殖生态学
    "ec005": "bird-image-079.png",
    "ec006": "head_urban_ecology.png",          # 城市鸟类生态学
    "ec007": "head_conservation_biology.png",   # 鸟类保护生物学
    "ec008": "head_island_biogeography.png",    # 岛屿生物地理学
    "ec009": "head_pollination_seed_dispersal.png", # 授粉与种子传播
    "ec010": "head_community_dynamics.png",     # 鸟类群落动态
    
    # petCare 分类
    "pc001": "bird-image-015.png",
    "pc002": "bird-image-020.png",
    "pc003": "bird-image-030.png",
    "pc004": "bird-image-040.png",
    "pc005": "bird-image-050.png",
    "pc006": "bird-image-060.png",
    "pc007": "bird-image-070.png",
    "pc008": "bird-image-080.png",
    "pc009": "bird-image-030.png",  # 这个有重复，需要修复
    "pc010": "bird-image-020.png",  # 这个有重复，需要修复
    
    # scientificWonders 分类
    "sw001": "bird-image-016.png",
    "sw002": "bird-image-011.png",
    "sw003": "bird-image-014.png",
    "sw004": "bird-image-019.png",
    "sw005": "bird-image-013.png",
    "sw006": "bird-image-010.png",
    "sw007": "bird-image-012.png",
    "sw008": "bird-image-017.png",
    "sw009": "bird-image-015.png",
    "sw010": "bird-image-018.png"
}

# 修复petCare分类的重复图片
PETCARE_FIX = {
    "pc009": "bird-image-090.png",  # 替换重复的030
    "pc010": "bird-image-025.png"   # 替换重复的020
}

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
            current_image_url = article.get('imageUrl', '')
            
            # 确定正确的图片文件名
            correct_image_filename = None
            
            if article_id in PETCARE_FIX:
                correct_image_filename = PETCARE_FIX[article_id]
            elif article_id in IMAGE_MAPPING:
                correct_image_filename = IMAGE_MAPPING[article_id]
            
            if correct_image_filename:
                # 构建正确的图片URL
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
    
    # 最后验证一下petCare分类的唯一性
    print("\n🔍 验证petCare分类图片唯一性...")
    petcare_images = set()
    duplicates = []
    
    for article_id in ["pc001", "pc002", "pc003", "pc004", "pc005", "pc006", "pc007", "pc008", "pc009", "pc010"]:
        if article_id in PETCARE_FIX:
            image = PETCARE_FIX[article_id]
        else:
            image = IMAGE_MAPPING.get(article_id)
        
        if image:
            if image in petcare_images:
                duplicates.append(image)
            else:
                petcare_images.add(image)
    
    if duplicates:
        print(f"⚠️  仍有重复图片: {duplicates}")
    else:
        print("✅ petCare分类所有图片都是唯一的")

if __name__ == "__main__":
    main()