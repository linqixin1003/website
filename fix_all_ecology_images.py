#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 正确的图片映射（基于实际文章头图）
image_mapping = {
    '01-habitat-ecosystems': 'bird-image-075.webp',
    '02-food-webs-chains': 'bird-image-076.webp', 
    '03-migration-patterns': 'bird-image-077.webp',
    '04-breeding-ecology': 'head_breeding_cology.webp',
    '05-climate-change-impact': 'bird-image-079.webp',
    '06-urban-ecology': 'head_urban_ecology.webp',
    '07-conservation-biology': 'head_conservation_biology.webp',
    '08-island-biogeography': 'head_island_biogeography.webp',
    '09-pollination-seed-dispersal': 'head_pollination_seed_dispersal.webp',
    '10-community-dynamics': 'head_community_dynamics.webp'
}

# 需要修复的文件列表
ecology_files = [
    'zh/ecology.html',
    'es/ecology.html', 
    'it/ecology.html',
    'pt/ecology.html',
    'ru/ecology.html',
    'ja/ecology.html',
    'ko/ecology.html'
]

def fix_ecology_images(file_path):
    """修复ecology.html文件中的图片路径"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复每个文章的图片路径
        for article_key, correct_image in image_mapping.items():
            # 查找对应的文章链接和图片
            pattern = rf'(href="[^"]*/{article_key}\.html"[^>]*>[\s\S]*?<img src=")[^"]*(")'
            replacement = rf'\1../images/birds/species/{correct_image}\2'
            content = re.sub(pattern, replacement, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已修复: {file_path}")
        
    except Exception as e:
        print(f"❌ 修复失败 {file_path}: {e}")

def main():
    print("开始修复所有语言版本的ecology.html图片路径...")
    
    for file_path in ecology_files:
        fix_ecology_images(file_path)
    
    print("\n修复完成！")

if __name__ == "__main__":
    main()