#!/usr/bin/env python3
"""
压缩蘑菇图片为 WebP 格式并居中裁剪为 4:3 比例
"""

import os
from pathlib import Path
from PIL import Image

def center_crop_4_3(image):
    """居中裁剪图片为 4:3 比例"""
    width, height = image.size
    target_ratio = 4 / 3
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        # 图片太宽，需要裁剪宽度
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        right = left + new_width
        cropped = image.crop((left, 0, right, height))
    else:
        # 图片太高，需要裁剪高度
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        bottom = top + new_height
        cropped = image.crop((0, top, width, bottom))
    
    return cropped

def compress_to_webp(jpg_path, webp_path, quality=85, max_width=1200):
    """压缩JPG图片为WebP格式"""
    try:
        # 打开图片
        with Image.open(jpg_path) as img:
            # 转换为RGB模式（如果需要）
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # 居中裁剪为 4:3 比例
            img = center_crop_4_3(img)
            
            # 调整大小（保持比例）
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # 保存为WebP格式
            img.save(webp_path, 'WEBP', quality=quality, method=6)
            
            return True
    except Exception as e:
        print(f"  ❌ 处理失败: {e}")
        return False

def get_file_size_mb(file_path):
    """获取文件大小（MB）"""
    return os.path.getsize(file_path) / (1024 * 1024)

def main():
    images_dir = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom/images")
    
    if not images_dir.exists():
        print(f"❌ 目录不存在: {images_dir}")
        return
    
    # 获取所有 jpg 文件
    jpg_files = list(images_dir.glob("*.jpg"))
    
    if not jpg_files:
        print("⚠️ 没有找到 JPG 文件")
        return
    
    print("🍄 开始压缩蘑菇图片...")
    print(f"📁 图片目录: {images_dir}")
    print(f"📊 总文件数: {len(jpg_files)}")
    print("=" * 80)
    
    total_original_size = 0
    total_compressed_size = 0
    success_count = 0
    
    for i, jpg_file in enumerate(jpg_files, 1):
        # 生成 webp 文件路径
        webp_file = jpg_file.with_suffix('.webp')
        
        original_size = get_file_size_mb(jpg_file)
        total_original_size += original_size
        
        print(f"\n[{i}/{len(jpg_files)}] {jpg_file.name}")
        print(f"  📦 原始大小: {original_size:.2f} MB")
        
        # 压缩并转换
        if compress_to_webp(jpg_file, webp_file, quality=85, max_width=1200):
            compressed_size = get_file_size_mb(webp_file)
            total_compressed_size += compressed_size
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            print(f"  ✅ 压缩后: {compressed_size:.2f} MB")
            print(f"  📉 压缩率: {compression_ratio:.1f}%")
            
            # 删除原始 JPG 文件
            jpg_file.unlink()
            print(f"  🗑️  已删除原文件")
            
            success_count += 1
        else:
            print(f"  ❌ 失败")
    
    # 总结
    print("\n" + "=" * 80)
    print("🎉 处理完成！")
    print(f"✅ 成功: {success_count}/{len(jpg_files)}")
    print(f"📦 原始总大小: {total_original_size:.2f} MB")
    print(f"📦 压缩后总大小: {total_compressed_size:.2f} MB")
    if total_original_size > 0:
        total_compression = (1 - total_compressed_size / total_original_size) * 100
        print(f"📉 总压缩率: {total_compression:.1f}%")
        print(f"💾 节省空间: {total_original_size - total_compressed_size:.2f} MB")

if __name__ == "__main__":
    main()
