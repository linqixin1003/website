#!/usr/bin/env python3
"""
批量重命名图片文件脚本
将中文文件名改为规范的英文文件名
"""

import os
import re
from pathlib import Path

def rename_bird_images():
    """重命名鸟类图片文件"""
    
    # 图片目录路径
    image_dir = Path("images/ui/placeholders")
    
    if not image_dir.exists():
        print(f"❌ 目录不存在: {image_dir}")
        return
    
    print(f"🔍 开始处理目录: {image_dir}")
    
    # 获取所有需要重命名的文件
    files_to_rename = []
    
    for file_path in image_dir.iterdir():
        if file_path.is_file() and file_path.name.startswith("请求大量鸟类美图"):
            files_to_rename.append(file_path)
    
    # 按文件名排序
    files_to_rename.sort(key=lambda x: x.name)
    
    print(f"📊 找到 {len(files_to_rename)} 个需要重命名的文件")
    
    # 重命名文件
    renamed_count = 0
    
    for i, old_path in enumerate(files_to_rename, 1):
        # 提取文件扩展名
        extension = old_path.suffix
        
        # 生成新的文件名
        if "(" in old_path.name and ")" in old_path.name:
            # 提取括号中的数字
            match = re.search(r'\((\d+)\)', old_path.name)
            if match:
                number = int(match.group(1))
                new_name = f"bird-image-{number:03d}{extension}"
            else:
                new_name = f"bird-image-{i:03d}{extension}"
        else:
            # 没有括号的原始文件
            new_name = f"bird-image-001{extension}"
        
        new_path = old_path.parent / new_name
        
        # 检查新文件名是否已存在
        counter = 1
        original_new_name = new_name
        while new_path.exists():
            name_without_ext = original_new_name.rsplit('.', 1)[0]
            new_name = f"{name_without_ext}-alt-{counter}{extension}"
            new_path = old_path.parent / new_name
            counter += 1
        
        try:
            old_path.rename(new_path)
            print(f"  ✅ {old_path.name} → {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"  ❌ 重命名失败 {old_path.name}: {e}")
    
    print(f"\n🎉 重命名完成！成功重命名 {renamed_count} 个文件")
    
    # 显示重命名后的文件列表
    print(f"\n📋 重命名后的文件列表:")
    renamed_files = sorted([f for f in image_dir.iterdir() if f.is_file() and f.name.startswith("bird-image")])
    for file_path in renamed_files:
        print(f"  📷 {file_path.name}")

def organize_images():
    """整理图片到合适的目录"""
    
    placeholders_dir = Path("images/ui/placeholders")
    birds_dir = Path("images/birds/species")
    
    # 确保目标目录存在
    birds_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 开始整理图片到合适的目录...")
    
    moved_count = 0
    
    # 移动鸟类图片到专门的目录
    for file_path in placeholders_dir.iterdir():
        if file_path.is_file() and file_path.name.startswith("bird-image") and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            new_path = birds_dir / file_path.name
            
            # 避免覆盖现有文件
            counter = 1
            original_name = file_path.name
            while new_path.exists():
                name_parts = original_name.rsplit('.', 1)
                new_name = f"{name_parts[0]}-{counter}.{name_parts[1]}"
                new_path = birds_dir / new_name
                counter += 1
            
            try:
                file_path.rename(new_path)
                print(f"  📦 移动: {file_path.name} → birds/species/{new_path.name}")
                moved_count += 1
            except Exception as e:
                print(f"  ❌ 移动失败 {file_path.name}: {e}")
    
    print(f"\n✅ 图片整理完成！移动了 {moved_count} 个文件到 birds/species/ 目录")

def create_image_index():
    """创建图片索引文件"""
    
    birds_dir = Path("images/birds/species")
    
    if not birds_dir.exists():
        print("❌ birds/species 目录不存在")
        return
    
    # 获取所有图片文件
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.webp']:
        image_files.extend(birds_dir.glob(ext))
    
    image_files.sort()
    
    # 创建索引内容
    index_content = {
        "total_images": len(image_files),
        "images": []
    }
    
    for i, img_path in enumerate(image_files, 1):
        image_info = {
            "id": i,
            "filename": img_path.name,
            "path": f"images/birds/species/{img_path.name}",
            "alt": f"Beautiful bird species image {i}",
            "category": "species",
            "tags": ["bird", "species", "nature", "wildlife"]
        }
        index_content["images"].append(image_info)
    
    # 写入索引文件
    import json
    index_file = Path("images/image-index.json")
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_content, f, indent=2, ensure_ascii=False)
    
    print(f"📋 创建图片索引文件: {index_file}")
    print(f"📊 索引了 {len(image_files)} 张图片")

if __name__ == "__main__":
    print("🚀 开始批量重命名和整理图片...")
    print("=" * 50)
    
    # 1. 重命名文件
    rename_bird_images()
    
    # 2. 整理图片到合适目录
    organize_images()
    
    # 3. 创建图片索引
    create_image_index()
    
    print("\n" + "=" * 50)
    print("🎉 所有操作完成！")
    print("\n💡 建议:")
    print("  - 检查重命名后的文件是否正确")
    print("  - 为图片添加更具描述性的文件名")
    print("  - 考虑压缩图片以优化网站性能")
    print("  - 为每张图片添加合适的 alt 文本")