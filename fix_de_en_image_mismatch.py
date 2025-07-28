#!/usr/bin/env python3
"""
修复德语和英语文章头图不匹配的问题
确保德语版本与英语版本使用相同的头图
"""

import os
import re
import glob

def extract_image_from_file(file_path):
    """从文件中提取头图编号"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找各种图片路径模式
        patterns = [
            r'bird-image-(\d+)\.webp',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            if matches:
                return f"bird-image-{matches[0]}.webp"
        
        return None
    except:
        return None

def compare_and_fix():
    """对比英语和德语文章的头图，修复不匹配的问题"""
    print("🔍 对比英语和德语文章头图...")
    
    mismatches = []
    
    # 获取所有德语文章
    for de_file in glob.glob('de/**/*.html', recursive=True):
        # 跳过目录页面
        if de_file.endswith('.html') and '/' in de_file:
            en_file = de_file.replace('de/', 'en/')
            
            if os.path.exists(en_file):
                de_image = extract_image_from_file(de_file)
                en_image = extract_image_from_file(en_file)
                
                if de_image and en_image and de_image != en_image:
                    mismatches.append({
                        'de_file': de_file,
                        'en_file': en_file,
                        'de_image': de_image,
                        'en_image': en_image
                    })
                    print(f"❌ 不匹配: {de_file}")
                    print(f"   德语: {de_image}")
                    print(f"   英语: {en_image}")
    
    print(f"\n📊 发现 {len(mismatches)} 个头图不匹配的文件")
    
    # 修复不匹配的文件
    fixed_count = 0
    for mismatch in mismatches:
        if fix_image_mismatch(mismatch['de_file'], mismatch['de_image'], mismatch['en_image']):
            fixed_count += 1
    
    print(f"\n🎉 修复完成: {fixed_count}/{len(mismatches)} 个文件")

def fix_image_mismatch(de_file, old_image, new_image):
    """修复单个文件的头图不匹配问题"""
    try:
        with open(de_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 替换所有出现的旧图片为新图片
        old_num = re.search(r'bird-image-(\d+)\.webp', old_image).group(1)
        new_num = re.search(r'bird-image-(\d+)\.webp', new_image).group(1)
        
        # 替换各种格式的图片引用
        replacements = [
            (f'bird-image-{old_num}.webp', f'bird-image-{new_num}.webp'),
        ]
        
        for old_pattern, new_pattern in replacements:
            content = content.replace(old_pattern, new_pattern)
        
        if content != original_content:
            with open(de_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复: {de_file} ({old_image} -> {new_image})")
            return True
        else:
            print(f"⚪ 跳过: {de_file} (无变化)")
            return False
            
    except Exception as e:
        print(f"❌ 修复失败: {de_file} - {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始修复德语和英语文章头图不匹配问题...")
    compare_and_fix()

if __name__ == "__main__":
    main()