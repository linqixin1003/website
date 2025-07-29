#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def get_image_mapping():
    """获取图片映射关系"""
    return {
        # birdwatching
        'bird-image-002.webp': 'birdwatching-01-getting-started.webp',
        'bird-image-001.webp': 'birdwatching-02-essential-equipment.webp',
        'bird-image-007.webp': 'birdwatching-03-identification-techniques.webp',
        'bird-image-004.webp': 'birdwatching-04-best-locations.webp',
        'bird-image-006.webp': 'birdwatching-05-seasonal-guide.webp',
        'bird-image-005.webp': 'birdwatching-06-photography-tips.webp',
        'bird-image-008.webp': 'birdwatching-07-behavior-observation.webp',
        'bird-image-003.webp': 'birdwatching-08-song-identification.webp',
        'bird-image-009.webp': 'birdwatching-09-ethics-conservation.webp',
        # 'bird-image-004.webp': 'birdwatching-10-journal-keeping.webp',  # 重复，需要特殊处理
        
        # ecology
        'bird-image-075.webp': 'ecology-01-habitat-ecosystems.webp',
        'bird-image-076.webp': 'ecology-02-food-webs-chains.webp',
        'bird-image-077.webp': 'ecology-03-migration-patterns.webp',
        # 'bird-image-078.webp': 'ecology-04-breeding-ecology.webp',  # 文件不存在
        'bird-image-079.webp': 'ecology-05-climate-change-impact.webp',
        'bird-image-080.webp': 'ecology-06-urban-ecology.webp',
        # 'bird-image-081.webp': 'ecology-07-conservation-biology.webp',  # 文件不存在
        # 'bird-image-082.webp': 'ecology-08-island-biogeography.webp',  # 文件不存在
        # 'bird-image-083.webp': 'ecology-09-pollination-seed-dispersal.webp',  # 文件不存在
        # 'bird-image-084.webp': 'ecology-10-community-dynamics.webp',  # 文件不存在
        
        # knowledge
        'bird-image-015.webp': 'knowledge-01-beginners-guide.webp',
        'bird-image-062.webp': 'knowledge-02-essential-equipment.webp',
        # 'bird-image-003.webp': 'knowledge-03-identification-techniques.webp',  # 重复
        # 'bird-image-004.webp': 'knowledge-04-best-locations.webp',  # 重复
        # 'bird-image-005.webp': 'knowledge-05-behavior-observation.webp',  # 重复
        # 'bird-image-006.webp': 'knowledge-06-song-identification.webp',  # 重复
        # 'bird-image-007.webp': 'knowledge-07-photography-tips.webp',  # 重复
        # 'bird-image-008.webp': 'knowledge-08-seasonal-guide.webp',  # 重复
        # 'bird-image-009.webp': 'knowledge-09-journal-keeping.webp',  # 重复
        'bird-image-010.webp': 'knowledge-10-ethics-conservation.webp',
        
        # pet-care
        # 'bird-image-015.webp': 'pet-care-01-choosing-right-bird.webp',  # 重复
        'bird-image-020.webp': 'pet-care-02-nutrition-feeding.webp',
        'bird-image-030.webp': 'pet-care-03-housing-environment.webp',
        'bird-image-040.webp': 'pet-care-04-health-veterinary.webp',
        'bird-image-050.webp': 'pet-care-05-training-behavior.webp',
        'bird-image-060.webp': 'pet-care-06-breeding-reproduction.webp',
        'bird-image-070.webp': 'pet-care-07-emergency-first-aid.webp',
        # 'bird-image-080.webp': 'pet-care-08-seasonal-care.webp',  # 重复
        'bird-image-025.webp': 'pet-care-09-enrichment-activities.webp',
        # 'bird-image-025.webp': 'pet-care-10-species-profiles.webp',  # 重复
        # 'bird-image-025.webp': 'pet-care-11-senior-bird-care.webp',  # 重复
        
        # scientific-wonders
        'bird-image-016.webp': 'scientific-wonders-01-bird-flight-mechanics.webp',
        'bird-image-011.webp': 'scientific-wonders-02-magnetic-navigation.webp',
        'bird-image-014.webp': 'scientific-wonders-03-hummingbird-mechanics.webp',
        'bird-image-019.webp': 'scientific-wonders-04-bird-intelligence.webp',
        'bird-image-013.webp': 'scientific-wonders-05-feather-structure.webp',
        # 'bird-image-010.webp': 'scientific-wonders-06-bird-vision.webp',  # 重复
        'bird-image-012.webp': 'scientific-wonders-07-egg-development.webp',
        'bird-image-017.webp': 'scientific-wonders-08-bird-communication.webp',
        # 'bird-image-015.webp': 'scientific-wonders-09-migration-physiology.webp',  # 重复
        'bird-image-018.webp': 'scientific-wonders-10-biomechanics.webp',
    }

def get_specific_mappings():
    """获取特定文件的映射关系"""
    return {
        # 处理重复的图片，根据文件路径确定使用哪个新图片
        'birdwatching/01-getting-started.html': {'bird-image-002.webp': 'birdwatching-01-getting-started.webp'},
        'birdwatching/02-essential-equipment.html': {'bird-image-001.webp': 'birdwatching-02-essential-equipment.webp'},
        'birdwatching/03-identification-techniques.html': {'bird-image-007.webp': 'birdwatching-03-identification-techniques.webp'},
        'birdwatching/04-best-locations.html': {'bird-image-004.webp': 'birdwatching-04-best-locations.webp'},
        'birdwatching/05-seasonal-guide.html': {'bird-image-006.webp': 'birdwatching-05-seasonal-guide.webp'},
        'birdwatching/06-photography-tips.html': {'bird-image-005.webp': 'birdwatching-06-photography-tips.webp'},
        'birdwatching/07-behavior-observation.html': {'bird-image-008.webp': 'birdwatching-07-behavior-observation.webp'},
        'birdwatching/08-song-identification.html': {'bird-image-003.webp': 'birdwatching-08-song-identification.webp'},
        'birdwatching/09-ethics-conservation.html': {'bird-image-009.webp': 'birdwatching-09-ethics-conservation.webp'},
        'birdwatching/10-journal-keeping.html': {'bird-image-004.webp': 'birdwatching-10-journal-keeping.webp'},
        
        'ecology/01-habitat-ecosystems.html': {'bird-image-075.webp': 'ecology-01-habitat-ecosystems.webp'},
        'ecology/02-food-webs-chains.html': {'bird-image-076.webp': 'ecology-02-food-webs-chains.webp'},
        'ecology/03-migration-patterns.html': {'bird-image-077.webp': 'ecology-03-migration-patterns.webp'},
        'ecology/05-climate-change-impact.html': {'bird-image-079.webp': 'ecology-05-climate-change-impact.webp'},
        'ecology/06-urban-ecology.html': {'bird-image-080.webp': 'ecology-06-urban-ecology.webp'},
        
        'knowledge/01-beginners-guide.html': {'bird-image-015.webp': 'knowledge-01-beginners-guide.webp'},
        'knowledge/02-essential-equipment.html': {'bird-image-062.webp': 'knowledge-02-essential-equipment.webp'},
        'knowledge/03-identification-techniques.html': {'bird-image-003.webp': 'knowledge-03-identification-techniques.webp'},
        'knowledge/04-best-locations.html': {'bird-image-004.webp': 'knowledge-04-best-locations.webp'},
        'knowledge/05-behavior-observation.html': {'bird-image-005.webp': 'knowledge-05-behavior-observation.webp'},
        'knowledge/06-song-identification.html': {'bird-image-006.webp': 'knowledge-06-song-identification.webp'},
        'knowledge/07-photography-tips.html': {'bird-image-007.webp': 'knowledge-07-photography-tips.webp'},
        'knowledge/08-seasonal-guide.html': {'bird-image-008.webp': 'knowledge-08-seasonal-guide.webp'},
        'knowledge/09-journal-keeping.html': {'bird-image-009.webp': 'knowledge-09-journal-keeping.webp'},
        'knowledge/10-ethics-conservation.html': {'bird-image-010.webp': 'knowledge-10-ethics-conservation.webp'},
        
        'pet-care/01-choosing-right-bird.html': {'bird-image-015.webp': 'pet-care-01-choosing-right-bird.webp'},
        'pet-care/02-nutrition-feeding.html': {'bird-image-020.webp': 'pet-care-02-nutrition-feeding.webp'},
        'pet-care/03-housing-environment.html': {'bird-image-030.webp': 'pet-care-03-housing-environment.webp'},
        'pet-care/04-health-veterinary.html': {'bird-image-040.webp': 'pet-care-04-health-veterinary.webp'},
        'pet-care/05-training-behavior.html': {'bird-image-050.webp': 'pet-care-05-training-behavior.webp'},
        'pet-care/06-breeding-reproduction.html': {'bird-image-060.webp': 'pet-care-06-breeding-reproduction.webp'},
        'pet-care/07-emergency-first-aid.html': {'bird-image-070.webp': 'pet-care-07-emergency-first-aid.webp'},
        'pet-care/08-seasonal-care.html': {'bird-image-080.webp': 'pet-care-08-seasonal-care.webp'},
        'pet-care/09-enrichment-activities.html': {'bird-image-025.webp': 'pet-care-09-enrichment-activities.webp'},
        'pet-care/10-species-profiles.html': {'bird-image-025.webp': 'pet-care-10-species-profiles.webp'},
        'pet-care/11-senior-bird-care.html': {'bird-image-025.webp': 'pet-care-11-senior-bird-care.webp'},
        
        'scientific-wonders/01-bird-flight-mechanics.html': {'bird-image-016.webp': 'scientific-wonders-01-bird-flight-mechanics.webp'},
        'scientific-wonders/02-magnetic-navigation.html': {'bird-image-011.webp': 'scientific-wonders-02-magnetic-navigation.webp'},
        'scientific-wonders/03-hummingbird-mechanics.html': {'bird-image-014.webp': 'scientific-wonders-03-hummingbird-mechanics.webp'},
        'scientific-wonders/04-bird-intelligence.html': {'bird-image-019.webp': 'scientific-wonders-04-bird-intelligence.webp'},
        'scientific-wonders/05-feather-structure.html': {'bird-image-013.webp': 'scientific-wonders-05-feather-structure.webp'},
        'scientific-wonders/06-bird-vision.html': {'bird-image-010.webp': 'scientific-wonders-06-bird-vision.webp'},
        'scientific-wonders/07-egg-development.html': {'bird-image-012.webp': 'scientific-wonders-07-egg-development.webp'},
        'scientific-wonders/08-bird-communication.html': {'bird-image-017.webp': 'scientific-wonders-08-bird-communication.webp'},
        'scientific-wonders/09-migration-physiology.html': {'bird-image-015.webp': 'scientific-wonders-09-migration-physiology.webp'},
        'scientific-wonders/10-biomechanics.html': {'bird-image-018.webp': 'scientific-wonders-10-biomechanics.webp'},
    }

def update_file_images(file_path, specific_mappings):
    """更新单个文件中的图片引用"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 获取文件的相对路径，用于确定特定映射
        rel_path = os.path.relpath(file_path, '.')
        
        # 查找匹配的特定映射
        file_mappings = {}
        for pattern, mappings in specific_mappings.items():
            if pattern in rel_path:
                file_mappings.update(mappings)
        
        if not file_mappings:
            return False
        
        # 替换图片引用
        for old_image, new_image in file_mappings.items():
            # 替换各种格式的图片引用
            patterns = [
                rf"url\(['\"]?[^'\"]*{re.escape(old_image)}['\"]?\)",
                rf"src=['\"][^'\"]*{re.escape(old_image)}['\"]",
                rf"background-image:\s*url\(['\"]?[^'\"]*{re.escape(old_image)}['\"]?\)"
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    new_match = match.replace(old_image, new_image)
                    content = content.replace(match, new_match)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("🔄 开始批量更新所有HTML文件中的头图引用...")
    
    specific_mappings = get_specific_mappings()
    
    # 查找所有HTML文件
    html_files = []
    
    # 查找所有语言目录下的HTML文件
    languages = ['en', 'es', 'fr', 'de', 'zh', 'it', 'ja', 'ko', 'pt', 'ru']
    
    for lang in languages:
        if os.path.exists(lang):
            # 查找该语言目录下的所有HTML文件
            pattern = os.path.join(lang, '**', '*.html')
            lang_files = glob.glob(pattern, recursive=True)
            html_files.extend(lang_files)
    
    # 也查找根目录下的HTML文件
    root_files = glob.glob('*.html')
    html_files.extend(root_files)
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    
    updated_count = 0
    
    # 处理每个文件
    for file_path in html_files:
        if update_file_images(file_path, specific_mappings):
            updated_count += 1
    
    print(f"\n🎉 完成！共更新了 {updated_count} 个文件")

if __name__ == "__main__":
    main()