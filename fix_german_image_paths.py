import os
import re

def fix_german_image_paths():
    """修复德语版本文章页面中的图片路径"""
    
    # 德语文章目录
    de_dir = "de/birdwatching"
    
    if not os.path.exists(de_dir):
        print(f"目录不存在: {de_dir}")
        return
    
    # 图片路径映射
    path_mapping = {
        "images/Vögel/Art/Vogel-image-001.webp": "images/birds/species/bird-image-001.webp",
        "images/Vögel/Art/Vogel-image-001-alt-1.webp": "images/birds/species/bird-image-001-alt-1.webp",
        "images/Vögel/Art/Vogel-image-002.webp": "images/birds/species/bird-image-002.webp",
        "images/Vögel/Art/Vogel-image-003.webp": "images/birds/species/bird-image-003.webp",
        "images/Vögel/Art/Vogel-image-004.webp": "images/birds/species/bird-image-004.webp",
        "images/Vögel/Art/Vogel-image-005.webp": "images/birds/species/bird-image-005.webp",
        "images/Vögel/Art/Vogel-image-006.webp": "images/birds/species/bird-image-006.webp",
        "images/Vögel/Art/Vogel-image-007.webp": "images/birds/species/bird-image-007.webp",
        "images/Vögel/Art/Vogel-image-008.webp": "images/birds/species/bird-image-008.webp",
        "images/Vögel/Art/Vogel-image-009.webp": "images/birds/species/bird-image-009.webp",
    }
    
    # 遍历所有HTML文件
    for filename in os.listdir(de_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(de_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 替换所有错误的图片路径
                for old_path, new_path in path_mapping.items():
                    # 处理相对路径
                    old_relative = f"../../{old_path}"
                    new_relative = f"../../{new_path}"
                    content = content.replace(old_relative, new_relative)
                
                # 如果内容有变化，写回文件
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ 已修复: {filepath}")
                else:
                    print(f"⚪ 无需修复: {filepath}")
                    
            except Exception as e:
                print(f"❌ 处理文件时出错 {filepath}: {e}")

if __name__ == "__main__":
    print("开始修复德语版本的图片路径...")
    fix_german_image_paths()
    print("修复完成！")