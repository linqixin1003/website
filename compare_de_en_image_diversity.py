#!/usr/bin/env python3
"""
比较德语和英语版本的头部图片多样性
"""

import os
import re
from collections import Counter, defaultdict

def extract_header_image(file_path):
    """提取文件的头部图片路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS背景图片
        css_match = re.search(r"url\('(../../images/[^']+)'\)", content)
        if css_match:
            return css_match.group(1)
        
        # 查找HTML img标签
        img_match = re.search(r'<img[^>]+src="(../../images/[^"]+)"[^>]*>', content)
        if img_match:
            return img_match.group(1)
        
        return None
        
    except Exception as e:
        return None

def find_all_html_files(directory):
    """查找目录下所有HTML文件"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and not file.endswith('knowledge.html') and not file.endswith('index.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def analyze_language_images(lang_code):
    """分析特定语言的图片使用情况"""
    files = find_all_html_files(lang_code)
    image_usage = Counter()
    file_to_image = {}
    
    for file_path in files:
        image = extract_header_image(file_path)
        if image:
            image_usage[image] += 1
            file_to_image[file_path] = image
    
    return files, image_usage, file_to_image

def main():
    """主函数"""
    print("🔍 比较德语和英语版本的头部图片多样性...")
    
    # 分析德语版本
    print("\n📋 分析德语版本...")
    de_files, de_image_usage, de_file_to_image = analyze_language_images('de')
    
    # 分析英语版本
    print("📋 分析英语版本...")
    en_files, en_image_usage, en_file_to_image = analyze_language_images('en')
    
    print("\n" + "=" * 80)
    print("📊 德语 vs 英语 图片使用对比")
    print("=" * 80)
    
    # 基本统计
    print(f"{'指标':<30} {'德语':<15} {'英语':<15}")
    print("-" * 60)
    print(f"{'总文件数':<30} {len(de_files):<15} {len(en_files):<15}")
    print(f"{'有头部图片的文件':<30} {len(de_file_to_image):<15} {len(en_file_to_image):<15}")
    print(f"{'使用的不同图片数':<30} {len(de_image_usage):<15} {len(en_image_usage):<15}")
    
    # 重复使用分析
    de_duplicates = sum(1 for count in de_image_usage.values() if count > 1)
    en_duplicates = sum(1 for count in en_image_usage.values() if count > 1)
    
    de_unique = len(de_image_usage) - de_duplicates
    en_unique = len(en_image_usage) - en_duplicates
    
    print(f"{'重复使用的图片数':<30} {de_duplicates:<15} {en_duplicates:<15}")
    print(f"{'唯一使用的图片数':<30} {de_unique:<15} {en_unique:<15}")
    
    if len(de_image_usage) > 0:
        de_unique_rate = (de_unique / len(de_image_usage)) * 100
    else:
        de_unique_rate = 0
        
    if len(en_image_usage) > 0:
        en_unique_rate = (en_unique / len(en_image_usage)) * 100
    else:
        en_unique_rate = 0
    
    print(f"{'图片唯一性比例':<30} {de_unique_rate:.1f}%{'':<10} {en_unique_rate:.1f}%")
    
    # 检查德语和英语是否使用相同的图片
    print(f"\n🔍 德语和英语图片使用对比:")
    
    # 找到对应的文件对
    matched_pairs = []
    for de_file in de_file_to_image.keys():
        en_file = de_file.replace('de/', 'en/')
        if en_file in en_file_to_image:
            de_image = de_file_to_image[de_file]
            en_image = en_file_to_image[en_file]
            matched_pairs.append((de_file, en_file, de_image, en_image))
    
    print(f"   找到 {len(matched_pairs)} 对对应的德语-英语文件")
    
    # 检查图片是否匹配
    matching_images = 0
    different_images = 0
    
    print(f"\n📋 图片匹配情况:")
    for de_file, en_file, de_image, en_image in matched_pairs:
        if de_image == en_image:
            matching_images += 1
        else:
            different_images += 1
            de_img_name = os.path.basename(de_image)
            en_img_name = os.path.basename(en_image)
            print(f"❌ {os.path.basename(de_file)}")
            print(f"   德语: {de_img_name}")
            print(f"   英语: {en_img_name}")
    
    print(f"\n📈 匹配统计:")
    print(f"   图片完全匹配: {matching_images} 对")
    print(f"   图片不匹配: {different_images} 对")
    
    if len(matched_pairs) > 0:
        match_rate = (matching_images / len(matched_pairs)) * 100
        print(f"   匹配率: {match_rate:.1f}%")
    
    # 最重复使用的图片
    print(f"\n🔄 最常被重复使用的图片:")
    print("德语版本:")
    de_sorted = sorted(de_image_usage.items(), key=lambda x: x[1], reverse=True)[:5]
    for image, count in de_sorted:
        if count > 1:
            print(f"   {os.path.basename(image)}: {count} 次")
    
    print("英语版本:")
    en_sorted = sorted(en_image_usage.items(), key=lambda x: x[1], reverse=True)[:5]
    for image, count in en_sorted:
        if count > 1:
            print(f"   {os.path.basename(image)}: {count} 次")
    
    # 总结和建议
    print(f"\n💡 分析结论:")
    if different_images > 0:
        print(f"   ❌ 发现 {different_images} 个文件的德语和英语版本使用了不同的头部图片")
        print(f"   📝 建议: 需要同步德语和英语版本的头部图片")
    else:
        print(f"   ✅ 所有德语和英语文件的头部图片都完全匹配")
    
    if de_duplicates > 10 or en_duplicates > 10:
        print(f"   ⚠️  图片重复使用较多，可能需要增加图片多样性")
    else:
        print(f"   ✅ 图片重复使用情况在合理范围内")

if __name__ == "__main__":
    main()