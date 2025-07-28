#!/usr/bin/env python3
"""
改进的德语英语文章头图同步脚本
支持检测各种格式的头图
"""

import os
import re

def extract_image_from_file(filepath):
    """从文件中提取头图路径和编号"""
    if not os.path.exists(filepath):
        return None, None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找各种格式的图片
    patterns = [
        # 标准格式: bird-image-XXX.webp
        r'bird-image-(\d+(?:-alt-\d+)?)\.webp',
        # 其他格式: head_XXX.webp
        r'head_([^\.]+)\.webp',
        # 任何webp图片
        r'([^/]+\.webp)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            full_match = match.group(0)
            if 'bird-image-' in full_match:
                return match.group(1), full_match
            else:
                return match.group(1), full_match
    
    return None, None

def update_de_image(de_filepath, en_image_path):
    """更新德语文件的头图"""
    if not os.path.exists(de_filepath) or not en_image_path:
        return False
        
    with open(de_filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    correct_path = f'../../images/birds/species/{en_image_path}'
    
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

def detailed_comparison():
    """详细对比德语和英语文章的头图"""
    categories = ['ecology']  # 先只检查ecology类别
    
    for category in categories:
        print(f"\n📁 详细检查类别: {category}")
        
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
            
            de_image_num, de_image_path = extract_image_from_file(de_path)
            en_image_num, en_image_path = extract_image_from_file(en_path)
            
            print(f"\n  📄 {filename}:")
            print(f"    德语: {de_image_path if de_image_path else '无头图'}")
            print(f"    英语: {en_image_path if en_image_path else '无头图'}")
            
            if en_image_path and de_image_path != en_image_path:
                print(f"    🔄 需要同步: {de_image_path} -> {en_image_path}")
                if update_de_image(de_path, en_image_path):
                    print(f"    ✅ 同步成功")
                else:
                    print(f"    ❌ 同步失败")
            elif en_image_path and de_image_path == en_image_path:
                print(f"    ✅ 已经一致")
            elif not en_image_path:
                print(f"    ⚠️  英语版无头图")

def main():
    print("🔍 详细检查和同步德语英语文章头图...")
    detailed_comparison()

if __name__ == "__main__":
    main()