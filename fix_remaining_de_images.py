#!/usr/bin/env python3
"""
修复剩余7个德语文章的头部图片
"""

import os
import re

def update_german_header_image(file_path, new_image_path):
    """更新德语文件的头部图片"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换头部图片
        # 匹配CSS background-image格式
        css_pattern = r"url\('../../images/[^']+'\)"
        if re.search(css_pattern, content):
            content = re.sub(css_pattern, f"url('{new_image_path}')", content)
            print(f"✅ 更新CSS背景图片: {file_path}")
        
        # 匹配HTML img标签格式
        img_pattern = r'<img[^>]+src="../../images/[^"]+"[^>]*>'
        if re.search(img_pattern, content):
            def replace_img_src(match):
                img_tag = match.group(0)
                return re.sub(r'src="../../images/[^"]+"', f'src="{new_image_path}"', img_tag)
            content = re.sub(img_pattern, replace_img_src, content)
            print(f"✅ 更新HTML img标签: {file_path}")
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("🔧 开始修复剩余7个德语文章的头部图片...")
    
    # 需要修复的文件映射 (德语文件路径 -> 英语头部图片路径)
    files_to_fix = {
        'de/pet-care/09-enrichment-activities.html': '../../images/birds/species/head-enrichment-activities.webp',
        'de/ecology/04-breeding-ecology.html': '../../images/birds/species/head_breeding_cology.webp',
        'de/ecology/06-urban-ecology.html': '../../images/birds/species/head_urban_ecology.webp',
        'de/ecology/07-conservation-biology.html': '../../images/birds/species/head_conservation_biology.webp',
        'de/ecology/08-island-biogeography.html': '../../images/birds/species/head_island_biogeography.webp',
        'de/ecology/09-pollination-seed-dispersal.html': '../../images/birds/species/head_pollination_seed_dispersal.webp',
        'de/ecology/10-community-dynamics.html': '../../images/birds/species/head_community_dynamics.webp'
    }
    
    success_count = 0
    total_count = len(files_to_fix)
    
    for de_file, image_path in files_to_fix.items():
        if os.path.exists(de_file):
            if update_german_header_image(de_file, image_path):
                success_count += 1
            else:
                print(f"⚠️  文件存在但更新失败: {de_file}")
        else:
            print(f"❌ 文件不存在: {de_file}")
    
    print(f"\n📊 修复完成统计:")
    print(f"   总文件数: {total_count}")
    print(f"   成功修复: {success_count}")
    print(f"   失败数量: {total_count - success_count}")
    
    if success_count == total_count:
        print("🎉 所有文件都已成功修复!")
    else:
        print("⚠️  部分文件修复失败，请检查错误信息")

if __name__ == "__main__":
    main()