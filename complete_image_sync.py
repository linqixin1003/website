#!/usr/bin/env python3
"""
完整同步所有德语英语文章头图
处理各种格式的头图文件
"""

import os
import re

def extract_image_from_file(filepath):
    """从文件中提取头图路径"""
    if not os.path.exists(filepath):
        return None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找图片路径
    patterns = [
        # CSS背景图片
        r'background:[^;]*url\([\'"]?[^\'")]*?([^/]+\.webp)[\'"]?\)',
        # HTML img标签
        r'src=[\'"][^\'">]*?([^/]+\.webp)[\'"]'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    
    return None

def update_de_image(de_filepath, en_image_filename):
    """更新德语文件的头图"""
    if not os.path.exists(de_filepath) or not en_image_filename:
        return False
        
    with open(de_filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    correct_path = f'../../images/birds/species/{en_image_filename}'
    
    # 修复CSS背景图片
    content = re.sub(
        r'(background:[^;]*url\([\'"]?)../../images/birds/species/[^\'")]+([\'"]?\))',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    # 修复HTML img标签
    content = re.sub(
        r'(src=[\'"])../../images/birds/species/[^\'">]+([\'"])',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    with open(de_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def sync_all_categories():
    """同步所有类别的德语英语文章头图"""
    categories = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
    
    total_synced = 0
    total_processed = 0
    
    for category in categories:
        print(f"\n📁 同步类别: {category}")
        
        de_dir = f'de/{category}'
        en_dir = f'en/{category}'
        
        if not os.path.exists(de_dir) or not os.path.exists(en_dir):
            print(f"⚠️  目录不存在: {de_dir} 或 {en_dir}")
            continue
        
        # 获取所有HTML文件
        de_files = [f for f in os.listdir(de_dir) if f.endswith('.html')]
        en_files = [f for f in os.listdir(en_dir) if f.endswith('.html')]
        
        # 找到共同的文件
        common_files = set(de_files) & set(en_files)
        
        for filename in sorted(common_files):
            de_path = os.path.join(de_dir, filename)
            en_path = os.path.join(en_dir, filename)
            
            de_image = extract_image_from_file(de_path)
            en_image = extract_image_from_file(en_path)
            
            total_processed += 1
            
            if en_image and de_image != en_image:
                if update_de_image(de_path, en_image):
                    total_synced += 1
                    print(f"  ✅ {filename}: {de_image} -> {en_image}")
                else:
                    print(f"  ❌ {filename}: 同步失败")
            elif en_image and de_image == en_image:
                print(f"  ✅ {filename}: 已一致 ({en_image})")
            elif not en_image:
                print(f"  ⚠️  {filename}: 英语版无头图")
            else:
                print(f"  ❓ {filename}: 德语版无头图")
    
    return total_synced, total_processed

def main():
    print("🔄 完整同步所有德语英语文章头图...")
    
    synced, processed = sync_all_categories()
    
    print(f"\n📊 同步结果:")
    print(f"  🔄 已同步: {synced} 个文件")
    print(f"  📝 总处理: {processed} 个文件")
    
    if processed > 0:
        sync_rate = synced / processed * 100
        print(f"  🎯 同步率: {sync_rate:.1f}%")

if __name__ == "__main__":
    main()