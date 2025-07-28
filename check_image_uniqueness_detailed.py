#!/usr/bin/env python3
"""
详细检查德语文章头部图片的唯一性和多样性
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

def main():
    """主函数"""
    print("🔍 详细检查德语文章头部图片的唯一性...")
    
    # 获取所有德语HTML文件
    de_files = find_all_html_files('de')
    
    # 统计图片使用情况
    image_usage = Counter()
    file_to_image = {}
    image_to_files = defaultdict(list)
    
    print("\n📋 德语文章头部图片详情:")
    print("=" * 100)
    
    for de_file in sorted(de_files):
        image = extract_header_image(de_file)
        if image:
            image_usage[image] += 1
            file_to_image[de_file] = image
            image_to_files[image].append(de_file)
            
            # 提取图片文件名
            image_name = os.path.basename(image)
            print(f"📄 {de_file:<60} → {image_name}")
        else:
            print(f"❌ {de_file:<60} → 无头部图片")
    
    print("=" * 100)
    
    # 分析图片使用统计
    print(f"\n📊 图片使用统计:")
    print(f"   总德语文件数: {len(de_files)}")
    print(f"   有头部图片的文件: {len(file_to_image)}")
    print(f"   使用的不同图片数: {len(image_usage)}")
    print(f"   图片重复使用情况:")
    
    # 按使用次数排序
    sorted_usage = sorted(image_usage.items(), key=lambda x: x[1], reverse=True)
    
    duplicate_count = 0
    unique_count = 0
    
    for image, count in sorted_usage:
        image_name = os.path.basename(image)
        if count > 1:
            print(f"   🔄 {image_name} (使用 {count} 次)")
            duplicate_count += 1
        else:
            unique_count += 1
    
    print(f"\n📈 唯一性分析:")
    print(f"   重复使用的图片: {duplicate_count} 个")
    print(f"   唯一使用的图片: {unique_count} 个")
    print(f"   图片唯一性比例: {(unique_count / len(image_usage) * 100):.1f}%")
    
    # 显示重复使用的图片详情
    if duplicate_count > 0:
        print(f"\n🔍 重复使用图片的详细情况:")
        print("-" * 80)
        for image, count in sorted_usage:
            if count > 1:
                image_name = os.path.basename(image)
                print(f"\n📸 {image_name} (使用 {count} 次):")
                for file_path in image_to_files[image]:
                    print(f"   • {file_path}")
    
    # 检查是否有明显的模式
    print(f"\n🎯 图片命名模式分析:")
    standard_pattern = 0
    special_pattern = 0
    
    for image in image_usage.keys():
        image_name = os.path.basename(image)
        if image_name.startswith('bird-image-'):
            standard_pattern += 1
        elif image_name.startswith('head'):
            special_pattern += 1
    
    print(f"   标准格式 (bird-image-*): {standard_pattern} 个")
    print(f"   特殊格式 (head*): {special_pattern} 个")
    
    # 总结
    if duplicate_count > 10:
        print(f"\n⚠️  警告: 发现 {duplicate_count} 个图片被重复使用，可能存在图片多样性不足的问题！")
    elif duplicate_count > 5:
        print(f"\n🟡 注意: 有 {duplicate_count} 个图片被重复使用，建议检查是否需要更多样化的图片")
    else:
        print(f"\n✅ 图片使用情况良好，重复使用较少")

if __name__ == "__main__":
    main()