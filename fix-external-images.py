#!/usr/bin/env python3
"""
修复外部图片链接，替换为本地鸟类图片
"""

import re
import json
from pathlib import Path

def load_image_index():
    """加载图片索引"""
    index_file = Path("images/image-index.json")
    
    if not index_file.exists():
        print("❌ 图片索引文件不存在")
        return None
    
    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def fix_beginners_guide():
    """修复初学者指南中的外部图片"""
    
    file_path = Path("knowledge/01-beginners-guide.html")
    
    if not file_path.exists():
        print(f"❌ 文件不存在: {file_path}")
        return
    
    # 加载图片索引
    image_index = load_image_index()
    if not image_index:
        return
    
    # 选择一些图片用于替换
    available_images = image_index['images']
    selected_images = [
        available_images[10]['path'],  # 第二张图片
        available_images[25]['path'],  # 第三张图片
        available_images[40]['path'],  # 第四张图片
        available_images[55]['path'],  # 第五张图片
        available_images[15]['path'],  # 第六张图片
        available_images[30]['path'],  # 第七张图片
    ]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换所有外部图片链接
        unsplash_patterns = [
            (r'https://images\.unsplash\.com/photo-1552728089-57bdde30beb3\?w=800&h=400&fit=crop', f"../{selected_images[0]}"),
            (r'https://images\.unsplash\.com/photo-1518709268805-4e9042af2176\?w=800&h=400&fit=crop', f"../{selected_images[1]}"),
            (r'https://images\.unsplash\.com/photo-1444927714506-8492d94b5ba0\?w=800&h=400&fit=crop', f"../{selected_images[2]}"),
            (r'https://images\.unsplash\.com/photo-1559827260-dc66d52bef19\?w=800&h=400&fit=crop', f"../{selected_images[3]}"),
            (r'https://images\.unsplash\.com/photo-1441974231531-c6227db76b6e\?w=800&h=400&fit=crop', f"../{selected_images[4]}"),
            (r'https://images\.unsplash\.com/photo-1574263867128-a3d5c1b1deae\?w=800&h=400&fit=crop', f"../{selected_images[5]}"),
        ]
        
        # 执行替换
        for pattern, replacement in unsplash_patterns:
            content = re.sub(pattern, replacement, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 成功修复: {file_path}")
        print(f"   替换了 {len(unsplash_patterns)} 个外部图片链接")
        
    except Exception as e:
        print(f"❌ 错误: {file_path} - {e}")

def find_and_fix_all_external_images():
    """查找并修复所有外部图片链接"""
    
    print("🔍 查找所有包含外部图片的文件...")
    
    # 查找所有HTML文件
    html_files = list(Path(".").rglob("*.html"))
    
    external_image_files = []
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否包含外部图片链接
            if 'unsplash.com' in content or 'https://images.' in content:
                external_image_files.append(file_path)
                
        except Exception as e:
            continue
    
    print(f"📊 找到 {len(external_image_files)} 个包含外部图片的文件:")
    for file_path in external_image_files:
        print(f"  - {file_path}")
    
    return external_image_files

def main():
    print("🚀 开始修复外部图片链接...")
    print("=" * 60)
    
    # 1. 查找所有外部图片文件
    external_files = find_and_fix_all_external_images()
    
    # 2. 修复初学者指南
    print("\\n🔧 修复初学者指南...")
    fix_beginners_guide()
    
    print("\\n" + "=" * 60)
    print("🎉 外部图片修复完成！")
    print("\\n💡 建议:")
    print("  - 检查修复后的图片显示效果")
    print("  - 确认所有图片路径正确")
    print("  - 考虑为其他外部图片文件创建类似的修复")

if __name__ == "__main__":
    main()