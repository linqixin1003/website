#!/usr/bin/env python3
"""
验证修复后的德语文件头部图片
"""

import os
import re

def extract_header_image(file_path):
    """提取文件的头部图片路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS背景图片
        css_match = re.search(r"url\('(../../images/[^']+)'\)", content)
        if css_match:
            return css_match.group(1)
        
        # 查找HTML img标签
        img_match = re.search(r'<img[^>]+src="(../../images/[^"]+)"[^>]*>', content)
        if img_match:
            return img_match.group(1)
        
        return None
        
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None

def main():
    """主函数"""
    print("🔍 验证修复后的德语文件头部图片...")
    
    # 需要验证的文件和期望的图片路径
    files_to_verify = {
        'de/pet-care/09-enrichment-activities.html': '../../images/birds/species/head-enrichment-activities.webp',
        'de/ecology/04-breeding-ecology.html': '../../images/birds/species/head_breeding_cology.webp',
        'de/ecology/06-urban-ecology.html': '../../images/birds/species/head_urban_ecology.webp',
        'de/ecology/07-conservation-biology.html': '../../images/birds/species/head_conservation_biology.webp',
        'de/ecology/08-island-biogeography.html': '../../images/birds/species/head_island_biogeography.webp',
        'de/ecology/09-pollination-seed-dispersal.html': '../../images/birds/species/head_pollination_seed_dispersal.webp',
        'de/ecology/10-community-dynamics.html': '../../images/birds/species/head_community_dynamics.webp'
    }
    
    success_count = 0
    total_count = len(files_to_verify)
    
    for de_file, expected_image in files_to_verify.items():
        if os.path.exists(de_file):
            actual_image = extract_header_image(de_file)
            if actual_image == expected_image:
                print(f"✅ {de_file}: {actual_image}")
                success_count += 1
            else:
                print(f"❌ {de_file}: 期望 {expected_image}, 实际 {actual_image}")
        else:
            print(f"❌ 文件不存在: {de_file}")
    
    print(f"\n📊 验证结果统计:")
    print(f"   总文件数: {total_count}")
    print(f"   验证成功: {success_count}")
    print(f"   验证失败: {total_count - success_count}")
    
    if success_count == total_count:
        print("🎉 所有文件的头部图片都已正确修复!")
    else:
        print("⚠️  部分文件的头部图片仍需修复")

if __name__ == "__main__":
    main()