#!/usr/bin/env python3
"""
验证所有语言版本的 pet-care/10-species-profiles.html 文件的头部图片
"""

import os
import re

def verify_species_profiles_images():
    """验证所有语言版本的species-profiles文件的头部图片"""
    
    # 所有语言目录
    languages = ['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
    
    # 期望的图片
    expected_image = 'bird-image-025.webp'
    
    print("🔍 验证所有语言版本的 pet-care/10-species-profiles.html 头部图片...")
    
    correct_count = 0
    total_count = 0
    
    for lang in languages:
        file_path = f"{lang}/pet-care/10-species-profiles.html"
        
        if os.path.exists(file_path):
            total_count += 1
            
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找CSS背景图片
                css_match = re.search(r"url\('../../images/birds/species/([^']+)'\)", content)
                
                # 查找HTML img标签
                img_match = re.search(r'<img[^>]+src="../../images/birds/species/([^"]+)"[^>]*>', content)
                
                found_image = None
                if css_match:
                    found_image = css_match.group(1)
                elif img_match:
                    found_image = img_match.group(1)
                
                if found_image:
                    if found_image == expected_image:
                        print(f"✅ {file_path}: {found_image}")
                        correct_count += 1
                    else:
                        print(f"❌ {file_path}: {found_image} (应该是 {expected_image})")
                else:
                    print(f"⚠️  {file_path}: 未找到头部图片")
                    
            except Exception as e:
                print(f"❌ {file_path}: 读取文件时出错 - {e}")
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n📊 验证结果统计:")
    print(f"   总文件数: {total_count}")
    print(f"   正确图片: {correct_count}")
    print(f"   错误图片: {total_count - correct_count}")
    
    if correct_count == total_count:
        print("🎉 所有文件的头部图片都正确!")
    else:
        print("⚠️  部分文件的头部图片不正确")

if __name__ == "__main__":
    verify_species_profiles_images()