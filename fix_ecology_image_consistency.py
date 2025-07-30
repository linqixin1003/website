#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_ecology_images():
    """修复所有语言版本的生态学页面图片路径，确保与英文版本一致"""
    
    # 正确的图片路径映射（基于英文版本）
    correct_images = {
        1: "bird-image-075.webp",
        2: "bird-image-076.webp", 
        3: "bird-image-077.webp",
        4: "head_breeding_cology.webp",
        5: "bird-image-079.webp",
        6: "head_urban_ecology.webp",
        7: "head_conservation_biology.webp",
        8: "head_island_biogeography.webp",
        9: "head_pollination_seed_dispersal.webp",
        10: "head_community_dynamics.webp"
    }
    
    # 语言代码列表
    languages = ['de', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
    
    for lang in languages:
        ecology_file = f"{lang}/ecology.html"
        
        if not os.path.exists(ecology_file):
            print(f"❌ 文件不存在: {ecology_file}")
            continue
            
        try:
            with open(ecology_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            changes_made = 0
            
            # 修复每个文章的图片路径
            for article_num, correct_image in correct_images.items():
                # 查找对应文章的图片标签
                pattern = rf'(<a href="ecology/{article_num:02d}-[^"]+\.html"[^>]*>[\s\S]*?<img src=")([^"]+)(" class="article-image")'
                
                def replace_image(match):
                    nonlocal changes_made
                    prefix = match.group(1)
                    old_image = match.group(2)
                    suffix = match.group(3)
                    
                    new_image = f"../images/birds/species/{correct_image}"
                    
                    if old_image != new_image:
                        changes_made += 1
                        print(f"  📝 文章{article_num}: {old_image} → {new_image}")
                        return prefix + new_image + suffix
                    return match.group(0)
                
                content = re.sub(pattern, replace_image, content)
            
            # 如果有更改，保存文件
            if changes_made > 0:
                with open(ecology_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ {lang}/ecology.html - 修复了 {changes_made} 个图片路径")
            else:
                print(f"✅ {lang}/ecology.html - 图片路径已正确")
                
        except Exception as e:
            print(f"❌ 处理 {ecology_file} 时出错: {e}")

if __name__ == "__main__":
    print("开始修复生态学页面图片路径一致性...")
    fix_ecology_images()
    print("修复完成！")