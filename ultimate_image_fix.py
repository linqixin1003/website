#!/usr/bin/env python3
import os
import re
import shutil

def create_all_missing_images():
    """创建所有缺失的图片文件"""
    base_path = "images/birds/species/"
    
    # 创建所有需要的图片文件
    images_to_create = [
        # 宠物护理文章图片
        ("bird-image-040.webp", "pet-care-04-health-veterinary.webp"),
        ("bird-image-060.webp", "pet-care-06-breeding-reproduction.webp"),
        ("bird-image-070.webp", "pet-care-07-emergency-first-aid.webp"),
        ("bird-image-080.webp", "pet-care-08-seasonal-care.webp"),
        
        # 演示页面图片
        ("bird-image-011.webp", "birdwatching-01-getting-started.webp"),
        ("bird-image-047.webp", "demo-image-1.webp"),
        ("bird-image-025.webp", "demo-image-2.webp"),
        
        # 法语文章图片
        ("bird-image-067.webp", "birdwatching-02-essential-equipment.webp"),
        
        # 知识指南中的鸟类图片
        ("bird-image-035.webp", "bird-mourning-dove.webp"),
        ("bird-image-040.webp", "bird-red-winged-blackbird.webp"),
        
        # 西班牙语生态学文章图片
        ("bird-image-038.webp", "ecology-main-header.webp"),
        ("bird-image-041.webp", "ecology-02-food-webs-chains.webp"),
        ("bird-image-042.webp", "ecology-05-climate-change-impact.webp"),
        ("bird-image-039.webp", "ecology-04-breeding-ecology.webp"),
        ("bird-image-033.webp", "ecology-06-urban-ecology.webp"),
        ("bird-image-034.webp", "ecology-08-island-biogeography.webp"),
        ("bird-image-036.webp", "ecology-02-food-webs-chains.webp"),
        ("bird-image-037.webp", "ecology-10-community-dynamics.webp"),
    ]
    
    for src_name, dest_name in images_to_create:
        src_path = os.path.join(base_path, src_name)
        dest_path = os.path.join(base_path, dest_name)
        if not os.path.exists(dest_path):
            if os.path.exists(src_path):
                shutil.copy2(src_path, dest_path)
                print(f"✅ 创建图片: {dest_path}")
            else:
                print(f"❌ 源文件不存在: {src_path}")

def update_all_remaining_files():
    """更新所有剩余的HTML文件"""
    
    # 全局替换映射
    global_replacements = {
        # 宠物护理
        'bird-image-040.webp': 'pet-care-04-health-veterinary.webp',
        'bird-image-060.webp': 'pet-care-06-breeding-reproduction.webp', 
        'bird-image-070.webp': 'pet-care-07-emergency-first-aid.webp',
        'bird-image-080.webp': 'pet-care-08-seasonal-care.webp',
        
        # 演示页面
        'bird-image-011.webp': 'birdwatching-01-getting-started.webp',
        'bird-image-047.webp': 'demo-image-1.webp',
        'bird-image-025.webp': 'demo-image-2.webp',
        
        # 法语文章
        'bird-image-067.webp': 'birdwatching-02-essential-equipment.webp',
        
        # 知识指南中的鸟类
        'bird-image-035.webp': 'bird-mourning-dove.webp',
        # 'bird-image-040.webp': 'bird-red-winged-blackbird.webp',  # 与宠物护理冲突，需要特殊处理
        
        # 生态学文章
        'bird-image-038.webp': 'ecology-main-header.webp',
        'bird-image-041.webp': 'ecology-02-food-webs-chains.webp',
        'bird-image-042.webp': 'ecology-05-climate-change-impact.webp',
        'bird-image-039.webp': 'ecology-04-breeding-ecology.webp',
        'bird-image-033.webp': 'ecology-06-urban-ecology.webp',
        'bird-image-034.webp': 'ecology-08-island-biogeography.webp',
        'bird-image-036.webp': 'ecology-02-food-webs-chains.webp',
        'bird-image-037.webp': 'ecology-10-community-dynamics.webp',
    }
    
    # 特殊文件映射
    special_mappings = {
        'knowledge/01-beginners-guide.html': {
            'bird-image-040.webp': 'bird-red-winged-blackbird.webp'
        },
        'pet-care.html': {
            'bird-image-040.webp': 'pet-care-04-health-veterinary.webp'
        }
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
            rel_path = os.path.relpath(file_path, '.')
            
            # 应用特殊映射
            for pattern, mappings in special_mappings.items():
                if pattern in rel_path:
                    for old_img, new_img in mappings.items():
                        content = content.replace(old_img, new_img)
            
            # 应用全局映射
            for old_img, new_img in global_replacements.items():
                # 跳过已经在特殊映射中处理的情况
                skip = False
                for pattern, mappings in special_mappings.items():
                    if pattern in rel_path and old_img in mappings:
                        skip = True
                        break
                
                if not skip:
                    content = content.replace(old_img, new_img)
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已更新: {rel_path}")
                updated_count += 1
                
        except Exception as e:
            print(f"❌ 处理文件失败 {file_path}: {e}")
    
    print(f"\n🎉 完成！共更新了 {updated_count} 个文件")

if __name__ == "__main__":
    print("开始创建缺失的图片文件...")
    create_all_missing_images()
    
    print("\n开始更新HTML文件...")
    update_all_remaining_files()