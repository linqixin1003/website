#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_german_ecology_header_images():
    """修复德语版本生态学文章的头图路径，确保与英语版本一致"""
    
    # 英语版本对应的头图映射
    header_image_mapping = {
        '01-habitat-ecosystems.html': 'bird-image-075.webp',
        '02-food-webs-chains.html': 'bird-image-076.webp', 
        '03-migration-patterns.html': 'bird-image-077.webp',
        '04-breeding-ecology.html': 'head_breeding_cology.webp',
        '05-climate-change-impact.html': 'bird-image-079.webp',
        '06-urban-ecology.html': 'head_urban_ecology.webp',
        '07-conservation-biology.html': 'head_conservation_biology.webp',
        '08-island-biogeography.html': 'head_island_biogeography.webp',
        '09-pollination-seed-dispersal.html': 'head_pollination_seed_dispersal.webp',
        '10-community-dynamics.html': 'head_community_dynamics.webp'
    }
    
    de_ecology_dir = 'de/ecology'
    
    if not os.path.exists(de_ecology_dir):
        print(f"目录不存在: {de_ecology_dir}")
        return
    
    for filename, correct_image in header_image_mapping.items():
        file_path = os.path.join(de_ecology_dir, filename)
        
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找并替换头图背景URL
            pattern = r"url\('../../images/birds/species/[^']+'\)"
            replacement = f"url('../../images/birds/species/{correct_image}')"
            
            # 检查是否需要更新
            if pattern in content or correct_image not in content:
                updated_content = re.sub(pattern, replacement, content)
                
                # 如果没有找到pattern，可能需要添加完整的样式
                if updated_content == content:
                    # 查找.hero-image样式块并更新
                    hero_pattern = r'(\.hero-image\s*\{[^}]*background:\s*linear-gradient[^}]*?)url\([^)]+\)([^}]*\})'
                    hero_replacement = f'\\1{replacement}\\2'
                    updated_content = re.sub(hero_pattern, hero_replacement, content, flags=re.DOTALL)
                
                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"✅ 已更新: {filename} -> {correct_image}")
                else:
                    print(f"ℹ️  无需更新: {filename} (已是正确图片)")
            else:
                print(f"ℹ️  无需更新: {filename} (已是正确图片)")
                
        except Exception as e:
            print(f"❌ 处理文件时出错 {filename}: {e}")

if __name__ == "__main__":
    print("开始修复德语版本生态学文章头图...")
    fix_german_ecology_header_images()
    print("修复完成！")