#!/usr/bin/env python3
import os
import re

# 英文版本的正确图片映射
correct_images = {
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

def fix_ecology_images():
    de_ecology_dir = 'de/ecology'
    
    if not os.path.exists(de_ecology_dir):
        print(f"目录 {de_ecology_dir} 不存在")
        return
    
    for filename, correct_image in correct_images.items():
        filepath = os.path.join(de_ecology_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"文件 {filepath} 不存在，跳过")
            continue
            
        print(f"处理文件: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找并替换头图路径
            pattern = r"url\('../../images/birds/species/[^']+'\)"
            replacement = f"url('../../images/birds/species/{correct_image}')"
            
            new_content = re.sub(pattern, replacement, content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 已修复 {filename} 的头图路径为 {correct_image}")
            else:
                print(f"ℹ️  {filename} 的头图路径已经正确")
                
        except Exception as e:
            print(f"❌ 处理 {filepath} 时出错: {e}")

if __name__ == "__main__":
    fix_ecology_images()
    print("德语 ecology 文章头图修复完成！")