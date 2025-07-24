#!/usr/bin/env python3
"""
为50篇文章分配头图的脚本
每篇文章选择一张合适的鸟类图片作为头图
"""

import json
import os
from pathlib import Path
import random

# 文章分类和标题
ARTICLE_CATEGORIES = {
    'birdwatching': [
        'Getting Started with Bird Watching',
        'Essential Bird Watching Equipment', 
        'Bird Identification Techniques',
        'Best Bird Watching Locations',
        'Seasonal Bird Watching Guide',
        'Photography Tips for Bird Watchers',
        'Bird Behavior Observation',
        'Bird Song Identification',
        'Bird Watching Ethics and Conservation',
        'Keeping a Bird Watching Journal'
    ],
    'scientific-wonders': [
        'The Mechanics of Bird Flight',
        'Magnetic Navigation in Birds',
        'Hummingbird Flight Mechanics',
        'Bird Intelligence and Cognition',
        'The Structure and Function of Feathers',
        'Extraordinary Bird Vision',
        'The Science of Egg Development',
        'Bird Communication and Vocalizations',
        'Migration Physiology',
        'Biomechanics of Bird Movement'
    ],
    'pet-care': [
        'Choosing the Right Pet Bird',
        'Bird Nutrition and Feeding',
        'Housing and Environment Setup',
        'Health and Veterinary Care',
        'Training and Behavior Management',
        'Breeding and Reproduction',
        'Emergency First Aid for Birds',
        'Seasonal Care Considerations',
        'Enrichment and Mental Stimulation',
        'Senior Bird Care'
    ],
    'ecology': [
        'Bird Habitats and Ecosystems',
        'Food Webs and Feeding Relationships',
        'Migration Patterns and Routes',
        'Breeding Ecology and Reproduction',
        'Climate Change Impact on Birds',
        'Urban Bird Ecology',
        'Conservation Biology Principles',
        'Island Biogeography and Birds',
        'Pollination and Seed Dispersal',
        'Community Dynamics and Competition'
    ],
    'knowledge': [
        'Introduction to Ornithology',
        'Bird Anatomy and Physiology',
        'Evolution and Phylogeny of Birds',
        'Bird Taxonomy and Classification',
        'Behavioral Ecology of Birds',
        'Avian Reproduction Strategies',
        'Bird Migration Mysteries',
        'Vocal Communication in Birds',
        'Predator-Prey Relationships',
        'Conservation Success Stories'
    ]
}

def load_image_index():
    """加载图片索引"""
    index_file = Path("images/image-index.json")
    
    if not index_file.exists():
        print("❌ 图片索引文件不存在，请先运行 rename-images.py")
        return None
    
    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def assign_images_to_articles():
    """为文章分配头图"""
    
    # 加载图片索引
    image_index = load_image_index()
    if not image_index:
        return
    
    available_images = image_index['images'].copy()
    random.shuffle(available_images)  # 随机打乱图片顺序
    
    article_images = {}
    image_counter = 0
    
    print("🖼️  开始为文章分配头图...")
    print("=" * 50)
    
    for category, titles in ARTICLE_CATEGORIES.items():
        print(f"\\n📁 分类: {category.upper()}")
        article_images[category] = {}
        
        for i, title in enumerate(titles, 1):
            article_id = f"{i:02d}"
            
            # 选择图片（循环使用可用图片）
            if image_counter < len(available_images):
                selected_image = available_images[image_counter]
            else:
                # 如果图片用完了，重新开始循环
                image_counter = 0
                selected_image = available_images[image_counter]
            
            article_images[category][article_id] = {
                'title': title,
                'hero_image': selected_image['path'],
                'hero_image_alt': f"{title} - Beautiful bird illustration",
                'image_filename': selected_image['filename']
            }
            
            print(f"  📄 {article_id}: {title}")
            print(f"      🖼️  图片: {selected_image['filename']}")
            
            image_counter += 1
    
    return article_images

def create_article_image_mapping(article_images):
    """创建文章图片映射文件"""
    
    mapping_file = Path("images/article-image-mapping.json")
    
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(article_images, f, indent=2, ensure_ascii=False)
    
    print(f"\\n📋 创建文章图片映射文件: {mapping_file}")
    
    # 统计信息
    total_articles = sum(len(articles) for articles in article_images.values())
    print(f"📊 总共为 {total_articles} 篇文章分配了头图")

def main():
    print("🚀 开始为50篇文章分配头图...")
    print("=" * 60)
    
    # 1. 为文章分配图片
    article_images = assign_images_to_articles()
    if not article_images:
        return
    
    # 2. 创建映射文件
    create_article_image_mapping(article_images)
    
    print("\\n" + "=" * 60)
    print("🎉 文章头图分配完成！")

if __name__ == "__main__":
    main()