#!/usr/bin/env python3
"""
对比德语和英语文章的头图是否一致
"""

import os
import re
import json

def extract_image_from_file(filepath):
    """从文件中提取头图编号"""
    if not os.path.exists(filepath):
        return None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找CSS背景图片
    css_match = re.search(r'bird-image-(\d+(?:-alt-\d+)?)\.webp', content)
    if css_match:
        return css_match.group(1)
    
    # 查找HTML img标签
    img_match = re.search(r'src=[\'"][^\'">]*bird-image-(\d+(?:-alt-\d+)?)\.webp[\'"]', content)
    if img_match:
        return img_match.group(1)
    
    return None

def compare_directories():
    """对比德语和英语目录的头图"""
    categories = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
    
    mismatches = []
    matches = []
    missing_files = []
    
    for category in categories:
        print(f"\n📁 检查类别: {category}")
        
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
            
            if de_image is None and en_image is None:
                missing_files.append(f"{category}/{filename}")
                print(f"  ❓ {filename}: 两个版本都没有头图")
            elif de_image is None:
                missing_files.append(f"de/{category}/{filename}")
                print(f"  ❌ {filename}: 德语版缺少头图 (英语版: {en_image})")
            elif en_image is None:
                missing_files.append(f"en/{category}/{filename}")
                print(f"  ❌ {filename}: 英语版缺少头图 (德语版: {de_image})")
            elif de_image != en_image:
                mismatches.append({
                    'file': f"{category}/{filename}",
                    'de_image': de_image,
                    'en_image': en_image
                })
                print(f"  ❌ {filename}: 头图不匹配 (德语: {de_image}, 英语: {en_image})")
            else:
                matches.append(f"{category}/{filename}")
                print(f"  ✅ {filename}: 头图一致 ({de_image})")
    
    return matches, mismatches, missing_files

def main():
    print("🔍 对比德语和英语文章头图...")
    
    matches, mismatches, missing_files = compare_directories()
    
    print(f"\n📊 对比结果:")
    print(f"  ✅ 头图一致: {len(matches)} 个文件")
    print(f"  ❌ 头图不匹配: {len(mismatches)} 个文件")
    print(f"  ❓ 缺少头图: {len(missing_files)} 个文件")
    
    if mismatches:
        print(f"\n❌ 头图不匹配的文件:")
        for mismatch in mismatches:
            print(f"  - {mismatch['file']}: 德语({mismatch['de_image']}) vs 英语({mismatch['en_image']})")
    
    if missing_files:
        print(f"\n❓ 缺少头图的文件:")
        for missing in missing_files:
            print(f"  - {missing}")
    
    # 计算匹配率
    total = len(matches) + len(mismatches)
    if total > 0:
        match_rate = len(matches) / total * 100
        print(f"\n🎯 头图匹配率: {match_rate:.1f}%")
    
    return len(mismatches) == 0 and len(missing_files) == 0

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 所有德语和英语文章的头图完全一致！")
    else:
        print("\n⚠️  发现头图不一致的问题，需要修复。")