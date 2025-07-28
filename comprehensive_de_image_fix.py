#!/usr/bin/env python3
"""
全面检查和修复德语目录下所有文章的头图路径问题
"""

import os
import re
import glob

def analyze_english_images():
    """分析英语文章的头图使用情况"""
    print("🔍 分析英语文章头图使用情况...")
    
    en_images = {}
    
    for en_file in glob.glob('en/**/*.html', recursive=True):
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找所有图片路径
            img_patterns = [
                r'src="([^"]*bird-image-\d+\.webp)"',
                r"url\('([^']*bird-image-\d+\.webp)'\)",
                r'url\("([^"]*bird-image-\d+\.webp)"\)'
            ]
            
            for pattern in img_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    # 提取图片编号
                    for match in matches:
                        img_num = re.search(r'bird-image-(\d+)\.webp', match)
                        if img_num:
                            en_images[en_file] = f"bird-image-{img_num.group(1)}.webp"
                            break
                    
        except Exception as e:
            print(f"❌ 读取英语文件失败: {en_file} - {e}")
    
    return en_images

def check_german_images():
    """检查德语文章的头图问题"""
    print("🔍 检查德语文章头图问题...")
    
    problems = []
    
    for de_file in glob.glob('de/**/*.html', recursive=True):
        try:
            with open(de_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查各种可能的错误路径
            error_patterns = [
                (r'Vögel/Art/', '错误的德语路径'),
                (r'V%C3%B6gel/Art/', '编码错误的德语路径'),
                (r'head_[^"\']*\.webp', '错误的head_开头图片'),
                (r'bird-image-\d+\.png', '错误的PNG格式'),
                (r'images/[^/]*/', '不完整的路径'),
            ]
            
            file_problems = []
            for pattern, desc in error_patterns:
                if re.search(pattern, content):
                    file_problems.append(desc)
            
            if file_problems:
                problems.append({
                    'file': de_file,
                    'problems': file_problems
                })
                
        except Exception as e:
            print(f"❌ 读取德语文件失败: {de_file} - {e}")
    
    return problems

def fix_german_image(file_path, correct_image):
    """修复单个德语文章的头图"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 修复各种错误的图片路径
        fixes = [
            # 错误的德语路径
            (r'src="[^"]*Vögel/Art/[^"]*"', f'src="../../images/birds/species/{correct_image}"'),
            (r'src="[^"]*V%C3%B6gel/Art/[^"]*"', f'src="../../images/birds/species/{correct_image}"'),
            
            # 错误的head_开头图片
            (r'src="[^"]*head_[^"]*\.webp"', f'src="../../images/birds/species/{correct_image}"'),
            
            # 错误的PNG格式
            (r'src="[^"]*bird-image-\d+\.png"', f'src="../../images/birds/species/{correct_image}"'),
            
            # CSS中的错误路径
            (r"url\('[^']*Vögel/Art/[^']*'\)", f"url('../../images/birds/species/{correct_image}')"),
            (r'url\("[^"]*Vögel/Art/[^"]*"\)', f'url("../../images/birds/species/{correct_image}")'),
            
            # CSS中的head_开头图片
            (r"url\('[^']*head_[^']*\.webp'\)", f"url('../../images/birds/species/{correct_image}')"),
            (r'url\("[^"]*head_[^"]*\.webp"\)', f'url("../../images/birds/species/{correct_image}")'),
        ]
        
        for pattern, replacement in fixes:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复: {file_path} -> {correct_image}")
            return True
        else:
            print(f"⚪ 跳过: {file_path} (无需修复)")
            return False
            
    except Exception as e:
        print(f"❌ 修复失败: {file_path} - {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始全面修复德语文章头图...")
    
    # 1. 分析英语文章的头图
    en_images = analyze_english_images()
    print(f"📊 找到 {len(en_images)} 个英语文章头图")
    
    # 2. 检查德语文章问题
    problems = check_german_images()
    print(f"⚠️  发现 {len(problems)} 个德语文章有头图问题")
    
    for problem in problems:
        print(f"   {problem['file']}: {', '.join(problem['problems'])}")
    
    # 3. 创建德语到英语的映射
    de_to_en_mapping = {}
    for de_file in glob.glob('de/**/*.html', recursive=True):
        en_file = de_file.replace('de/', 'en/')
        if en_file in en_images:
            de_to_en_mapping[de_file] = en_images[en_file]
    
    # 4. 为没有对应英语文件的德语文章分配头图
    used_images = set(de_to_en_mapping.values())
    available_images = [f"bird-image-{i:03d}.webp" for i in range(1, 101)]
    
    for de_file in glob.glob('de/**/*.html', recursive=True):
        if de_file not in de_to_en_mapping:
            # 为额外的德语文章分配未使用的头图
            for img in available_images:
                if img not in used_images:
                    de_to_en_mapping[de_file] = img
                    used_images.add(img)
                    break
    
    print(f"📋 创建了 {len(de_to_en_mapping)} 个德语文章头图映射")
    
    # 5. 修复所有德语文章
    fixed_count = 0
    for de_file, correct_image in de_to_en_mapping.items():
        if fix_german_image(de_file, correct_image):
            fixed_count += 1
    
    print(f"\n🎉 修复完成:")
    print(f"   总文件数: {len(de_to_en_mapping)}")
    print(f"   修复文件数: {fixed_count}")
    print(f"   跳过文件数: {len(de_to_en_mapping) - fixed_count}")

if __name__ == "__main__":
    main()