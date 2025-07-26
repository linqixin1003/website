#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复所有语言版本的生态学HTML文件中的图片引用
将不存在的bird-image-081到085.png替换为对应的专用头图
"""

import os
import re
import glob

# 图片映射关系
IMAGE_MAPPING = {
    'bird-image-078.png': 'head_breeding_cology.png',         # 04-breeding-ecology.html
    'bird-image-081.png': 'head_urban_ecology.png',           # 06-urban-ecology.html
    'bird-image-082.png': 'head_conservation_biology.png',    # 07-conservation-biology.html  
    'bird-image-083.png': 'head_island_biogeography.png',     # 08-island-biogeography.html
    'bird-image-084.png': 'head_pollination_seed_dispersal.png', # 09-pollination-seed-dispersal.html
    'bird-image-085.png': 'head_community_dynamics.png'       # 10-community-dynamics.html
}

def fix_html_file(file_path):
    """修复单个HTML文件中的图片引用"""
    print(f"\n📝 处理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return False
    
    original_content = content
    changes_made = []
    
    # 替换图片引用
    for old_image, new_image in IMAGE_MAPPING.items():
        if old_image in content:
            content = content.replace(old_image, new_image)
            changes_made.append(f"{old_image} → {new_image}")
    
    if changes_made:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新图片引用:")
            for change in changes_made:
                print(f"   {change}")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")
            return False
    else:
        print("ℹ️ 该文件无需修改")
    
    return len(changes_made) > 0

def main():
    """主函数"""
    # 查找所有语言版本的生态学HTML文件
    languages = ['en', 'zh', 'ja', 'ko', 'fr', 'de', 'it', 'pt', 'ru']
    ecology_files = [
        '04-breeding-ecology.html',
        '06-urban-ecology.html',
        '07-conservation-biology.html', 
        '08-island-biogeography.html',
        '09-pollination-seed-dispersal.html',
        '10-community-dynamics.html'
    ]
    
    print("🔧 开始修复所有语言版本的生态学HTML文件中的图片引用...")
    print("=" * 70)
    
    total_fixed = 0
    total_files = 0
    
    for lang in languages:
        print(f"\n🌍 处理 {lang.upper()} 语言版本:")
        lang_fixed = 0
        
        for ecology_file in ecology_files:
            file_path = f"{lang}/ecology/{ecology_file}"
            total_files += 1
            
            if os.path.exists(file_path):
                if fix_html_file(file_path):
                    total_fixed += 1
                    lang_fixed += 1
            else:
                print(f"\n⚠️ 文件不存在: {file_path}")
        
        print(f"   📊 {lang.upper()} 语言修复了 {lang_fixed} 个文件")
    
    print("\n" + "=" * 70)
    print(f"🎉 修复完成!")
    print(f"📊 总计检查了 {total_files} 个文件")
    print(f"✅ 成功修复了 {total_fixed} 个HTML文件")
    
    print("\n📋 图片映射关系:")
    for old_image, new_image in IMAGE_MAPPING.items():
        print(f"   {old_image} → {new_image}")
    
    print(f"\n🌍 涉及语言: {', '.join([lang.upper() for lang in languages])}")
    print("✨ 现在所有语言版本的生态学HTML文件都使用专用头图了！")

if __name__ == "__main__":
    main()