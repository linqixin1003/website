#!/usr/bin/env python3
"""
修复所有语言版本的 pet-care/10-species-profiles.html 文件的头部图片为 bird-image-025.webp
"""

import os
import re

def fix_species_profiles_image():
    """修复所有语言版本的species-profiles文件的头部图片"""
    
    # 所有语言目录
    languages = ['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
    
    # 目标图片
    target_image = '../../images/birds/species/bird-image-025.webp'
    
    print("🔧 开始修复所有语言版本的 pet-care/10-species-profiles.html 头部图片...")
    
    fixed_count = 0
    total_count = 0
    
    for lang in languages:
        file_path = f"{lang}/pet-care/10-species-profiles.html"
        
        if os.path.exists(file_path):
            total_count += 1
            print(f"\n📄 处理文件: {file_path}")
            
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 修复CSS背景图片
                css_pattern = r"url\('../../images/birds/species/[^']+'\)"
                if re.search(css_pattern, content):
                    content = re.sub(css_pattern, f"url('{target_image}')", content)
                    print(f"   ✅ 更新CSS背景图片")
                
                # 修复HTML img标签
                img_pattern = r'<img([^>]+)src="../../images/birds/species/[^"]+"([^>]*>)'
                if re.search(img_pattern, content):
                    content = re.sub(img_pattern, f'<img\\1src="{target_image}"\\2', content)
                    print(f"   ✅ 更新HTML img标签")
                
                # 如果内容有变化，写回文件
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_count += 1
                    print(f"   ✅ 文件已更新")
                else:
                    print(f"   ℹ️  文件无需更新")
                    
            except Exception as e:
                print(f"   ❌ 处理文件时出错: {e}")
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n📊 修复完成统计:")
    print(f"   总文件数: {total_count}")
    print(f"   成功修复: {fixed_count}")
    print(f"   失败数量: {total_count - fixed_count}")
    
    if fixed_count == total_count:
        print("🎉 所有文件都已成功修复!")
    else:
        print("⚠️  部分文件修复失败，请检查错误信息")

if __name__ == "__main__":
    fix_species_profiles_image()