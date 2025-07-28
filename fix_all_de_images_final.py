#!/usr/bin/env python3
"""
系统性修复德语目录下所有文章的头图路径
确保与英语版本使用相同的头图编号
"""

import os
import re
import glob

def get_english_image_mapping():
    """获取英语文章的头图映射"""
    mapping = {}
    
    # 手动定义英语文章的头图映射（基于之前的分析）
    english_images = {
        # birdwatching
        'en/birdwatching/01-getting-started.html': 'bird-image-001.webp',
        'en/birdwatching/02-essential-equipment.html': 'bird-image-002.webp', 
        'en/birdwatching/03-identification-techniques.html': 'bird-image-003.webp',
        'en/birdwatching/04-best-locations.html': 'bird-image-004.webp',
        'en/birdwatching/05-seasonal-guide.html': 'bird-image-005.webp',
        'en/birdwatching/06-photography-tips.html': 'bird-image-006.webp',
        'en/birdwatching/07-behavior-observation.html': 'bird-image-007.webp',
        'en/birdwatching/08-song-identification.html': 'bird-image-008.webp',
        'en/birdwatching/09-ethics-conservation.html': 'bird-image-009.webp',
        'en/birdwatching/10-journal-keeping.html': 'bird-image-010.webp',
        
        # ecology
        'en/ecology/01-habitat-ecosystems.html': 'bird-image-015.webp',
        'en/ecology/02-food-webs-chains.html': 'bird-image-016.webp',
        'en/ecology/03-migration-patterns.html': 'bird-image-017.webp',
        'en/ecology/04-breeding-ecology.html': 'bird-image-018.webp',
        'en/ecology/05-climate-change-impact.html': 'bird-image-019.webp',
        
        # pet-care
        'en/pet-care/01-choosing-right-bird.html': 'bird-image-025.webp',
        'en/pet-care/02-nutrition-feeding.html': 'bird-image-026.webp',
        'en/pet-care/03-housing-environment.html': 'bird-image-027.webp',
        'en/pet-care/04-health-veterinary.html': 'bird-image-028.webp',
        'en/pet-care/05-training-behavior.html': 'bird-image-029.webp',
        'en/pet-care/06-breeding-reproduction.html': 'bird-image-030.webp',
        'en/pet-care/07-emergency-first-aid.html': 'bird-image-031.webp',
        'en/pet-care/08-seasonal-care.html': 'bird-image-032.webp',
        'en/pet-care/09-enrichment-activities.html': 'bird-image-033.webp',
        'en/pet-care/10-senior-bird-care.html': 'bird-image-034.webp',
        
        # scientific-wonders
        'en/scientific-wonders/01-bird-flight-mechanics.html': 'bird-image-035.webp',
        'en/scientific-wonders/02-magnetic-navigation.html': 'bird-image-036.webp',
        'en/scientific-wonders/03-hummingbird-mechanics.html': 'bird-image-037.webp',
        'en/scientific-wonders/04-bird-intelligence.html': 'bird-image-038.webp',
        'en/scientific-wonders/05-feather-structure.html': 'bird-image-039.webp',
        'en/scientific-wonders/06-bird-vision.html': 'bird-image-040.webp',
        'en/scientific-wonders/07-egg-development.html': 'bird-image-041.webp',
        'en/scientific-wonders/08-bird-communication.html': 'bird-image-042.webp',
        'en/scientific-wonders/09-migration-physiology.html': 'bird-image-043.webp',
        'en/scientific-wonders/10-biomechanics.html': 'bird-image-044.webp',
        
        # knowledge
        'en/knowledge/01-beginners-guide.html': 'bird-image-001.webp',
        'en/knowledge/02-essential-equipment.html': 'bird-image-002.webp',
        'en/knowledge/03-identification-techniques.html': 'bird-image-003.webp',
        'en/knowledge/04-best-locations.html': 'bird-image-004.webp',
        'en/knowledge/05-behavior-observation.html': 'bird-image-007.webp',
        'en/knowledge/06-song-identification.html': 'bird-image-008.webp',
        'en/knowledge/07-photography-tips.html': 'bird-image-006.webp',
        'en/knowledge/08-seasonal-guide.html': 'bird-image-005.webp',
        'en/knowledge/09-journal-keeping.html': 'bird-image-010.webp',
        'en/knowledge/10-ethics-conservation.html': 'bird-image-009.webp',
    }
    
    return english_images

def fix_german_article_image(file_path, correct_image):
    """修复单个德语文章的头图路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换各种错误的头图路径
        patterns_to_fix = [
            # 错误的Vögel/Art路径
            r'src="[^"]*Vögel/Art/[^"]*"',
            r'src="[^"]*V%C3%B6gel/Art/[^"]*"',
            # 错误的head_开头的图片
            r'src="[^"]*head_[^"]*\.webp"',
            # 错误的png格式
            r'src="[^"]*bird-image-\d+\.png"',
            # 其他可能的错误路径
            r'src="[^"]*images/[^"]*(?:Vogel-image|head_)[^"]*"'
        ]
        
        # 正确的图片路径
        correct_path = f'../../images/birds/species/{correct_image}'
        
        # 替换所有匹配的模式
        modified = False
        for pattern in patterns_to_fix:
            if re.search(pattern, content):
                content = re.sub(pattern, f'src="{correct_path}"', content)
                modified = True
        
        # 如果没有找到错误模式，检查是否需要添加头图
        if not modified:
            # 检查是否已经有正确的头图
            if correct_path not in content:
                # 查找hero-image div并添加正确的图片
                hero_pattern = r'(<div class="hero-image"[^>]*>)'
                if re.search(hero_pattern, content):
                    # 如果找到hero-image div但没有img标签，添加img
                    if '<img' not in re.search(r'<div class="hero-image"[^>]*>.*?</div>', content, re.DOTALL).group():
                        content = re.sub(
                            hero_pattern,
                            f'\\1\n<img alt="Header Image" src="{correct_path}"/>',
                            content
                        )
                        modified = True
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复: {file_path} -> {correct_image}")
            return True
        else:
            print(f"⚪ 跳过: {file_path} (已正确)")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {file_path} - {e}")
        return False

def main():
    """主函数"""
    print("🔧 开始修复德语文章头图路径...")
    
    # 获取英语文章的头图映射
    english_mapping = get_english_image_mapping()
    
    # 统计
    total_files = 0
    fixed_files = 0
    
    # 遍历德语目录下的所有HTML文件
    for de_file in glob.glob('de/**/*.html', recursive=True):
        # 构造对应的英语文件路径
        en_file = de_file.replace('de/', 'en/')
        
        if en_file in english_mapping:
            correct_image = english_mapping[en_file]
            total_files += 1
            
            if fix_german_article_image(de_file, correct_image):
                fixed_files += 1
        else:
            print(f"⚠️  未找到对应的英语文件映射: {en_file}")
    
    print(f"\n📊 修复完成:")
    print(f"   总文件数: {total_files}")
    print(f"   修复文件数: {fixed_files}")
    print(f"   跳过文件数: {total_files - fixed_files}")

if __name__ == "__main__":
    main()