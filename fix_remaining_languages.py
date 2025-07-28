#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 正确的图片映射
image_mapping = {
    'bird-image-025.webp': 'bird-image-016.webp',  # 文章1
    'bird-image-026.webp': 'bird-image-011.webp',  # 文章2
    'bird-image-027.webp': 'bird-image-014.webp',  # 文章3
    'bird-image-028.webp': 'bird-image-019.webp',  # 文章4
    'bird-image-029.webp': 'bird-image-013.webp',  # 文章5
    'bird-image-030.webp': 'bird-image-010.webp',  # 文章6
    'bird-image-031.webp': 'bird-image-012.webp',  # 文章7
    'bird-image-032.webp': 'bird-image-017.webp',  # 文章8
    'bird-image-033.webp': 'bird-image-015.webp',  # 文章9
    'bird-image-034.webp': 'bird-image-018.webp',  # 文章10
}

# 需要处理的语言目录
language_dirs = ['ja', 'ko', 'pt', 'ru']

def fix_images_in_file(file_path):
    """修复单个文件中的图片路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换所有错误的图片路径
        for old_image, new_image in image_mapping.items():
            content = content.replace(old_image, new_image)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ 成功修复: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {str(e)}")
        return False

def main():
    """主函数"""
    print("开始修复剩余语言版本的scientific-wonders.html图片...")
    
    success_count = 0
    total_count = 0
    
    for lang_dir in language_dirs:
        file_path = os.path.join(lang_dir, 'scientific-wonders.html')
        
        if not os.path.exists(file_path):
            print(f"⚠️  文件不存在: {file_path}")
            continue
            
        total_count += 1
        if fix_images_in_file(file_path):
            success_count += 1
    
    print(f"\n修复完成！成功: {success_count}/{total_count}")

if __name__ == "__main__":
    main()