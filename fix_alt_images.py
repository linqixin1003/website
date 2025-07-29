#!/usr/bin/env python3
import os
import re
import shutil

def create_alt_images():
    """创建alt格式的图片文件"""
    base_path = "images/birds/species/"
    
    # 创建alt格式图片
    alt_images = [
        ("bird-image-001.webp", "bird-image-001-alt-1.webp"),
    ]
    
    for src_name, dest_name in alt_images:
        src_path = os.path.join(base_path, src_name)
        dest_path = os.path.join(base_path, dest_name)
        if not os.path.exists(dest_path):
            if os.path.exists(src_path):
                shutil.copy2(src_path, dest_path)
                print(f"✅ 创建图片: {dest_path}")

def fix_alt_image_references():
    """修复所有alt格式的图片引用"""
    
    # 替换映射
    replacements = {
        'bird-image-001-alt-1.webp': 'birdwatching-04-best-locations.webp',
    }
    
    # 查找所有HTML文件
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    
    updated_count = 0
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 应用替换
            for old_img, new_img in replacements.items():
                content = content.replace(old_img, new_img)
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                rel_path = os.path.relpath(file_path, '.')
                print(f"✅ 已更新: {rel_path}")
                updated_count += 1
                
        except Exception as e:
            print(f"❌ 处理文件失败 {file_path}: {e}")
    
    print(f"\n🎉 完成！共更新了 {updated_count} 个文件")

if __name__ == "__main__":
    print("开始创建alt格式图片...")
    create_alt_images()
    
    print("\n开始修复alt格式图片引用...")
    fix_alt_image_references()