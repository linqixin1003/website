#!/usr/bin/env python3
"""
快速修复德语文章头图 - 简化版本
"""

import os
import re
import json

# 正确的图片映射（根据映射文件）
CORRECT_MAPPINGS = {
    # birdwatching
    'de/birdwatching/01-getting-started.html': '011',
    'de/birdwatching/02-essential-equipment.html': '067', 
    'de/birdwatching/03-identification-techniques.html': '079',
    'de/birdwatching/04-best-locations.html': '056',
    'de/birdwatching/05-seasonal-guide.html': '060',
    'de/birdwatching/06-photography-tips.html': '009',
    'de/birdwatching/07-behavior-observation.html': '028',
    'de/birdwatching/08-song-identification.html': '016',
    'de/birdwatching/09-ethics-conservation.html': '021',
    'de/birdwatching/10-journal-keeping.html': '068',
    
    # scientific-wonders
    'de/scientific-wonders/01-bird-flight-mechanics.html': '040',
    'de/scientific-wonders/02-magnetic-navigation.html': '049',
    'de/scientific-wonders/03-hummingbird-mechanics.html': '029',
    'de/scientific-wonders/04-bird-intelligence.html': '077',
    'de/scientific-wonders/05-feather-structure.html': '018',
    'de/scientific-wonders/06-bird-vision.html': '037',
    'de/scientific-wonders/07-egg-development.html': '024',
    'de/scientific-wonders/08-bird-communication.html': '019',
    'de/scientific-wonders/09-migration-physiology.html': '012',
    'de/scientific-wonders/10-biomechanics.html': '058',
    
    # pet-care
    'de/pet-care/01-choosing-right-bird.html': '005',
    'de/pet-care/02-nutrition-feeding.html': '076',
    'de/pet-care/03-housing-environment.html': '064',
    'de/pet-care/04-health-veterinary.html': '044',
    'de/pet-care/05-training-behavior.html': '059',
    'de/pet-care/06-breeding-reproduction.html': '015',
    'de/pet-care/07-emergency-first-aid.html': '032',
    'de/pet-care/08-seasonal-care.html': '035',
    'de/pet-care/09-enrichment-activities.html': '027',
    'de/pet-care/10-senior-bird-care.html': '004',
    
    # ecology
    'de/ecology/01-habitat-ecosystems.html': '075',
    'de/ecology/02-food-webs-chains.html': '080',
    'de/ecology/03-migration-patterns.html': '022',
    'de/ecology/04-breeding-ecology.html': '070',
    'de/ecology/05-climate-change-impact.html': '006',
    'de/ecology/06-urban-ecology.html': '071',
    'de/ecology/07-conservation-biology.html': '042',
    'de/ecology/08-island-biogeography.html': '014',
    'de/ecology/09-pollination-seed-dispersal.html': '034',
    'de/ecology/10-community-dynamics.html': '007',
    
    # knowledge
    'de/knowledge/01-beginners-guide.html': '017',
    'de/knowledge/02-essential-equipment.html': '062',
    'de/knowledge/03-identification-techniques.html': '023',
    'de/knowledge/04-best-locations.html': '001-alt-1',
    'de/knowledge/05-behavior-observation.html': '003',
    'de/knowledge/06-song-identification.html': '055',
    'de/knowledge/07-photography-tips.html': '065',
    'de/knowledge/08-seasonal-guide.html': '010',
    'de/knowledge/09-journal-keeping.html': '051',
    'de/knowledge/10-ethics-conservation.html': '025',
}

def fix_file_image(filepath, correct_num):
    """修复单个文件的图片"""
    if not os.path.exists(filepath):
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    correct_path = f'../../images/birds/species/bird-image-{correct_num}.webp'
    
    # 修复CSS背景图片
    content = re.sub(
        r'(background:[^;]*url\([\'"]?)../../images/birds/species/bird-image-\d+(?:-alt-\d+)?\.webp([\'"]?\))',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    # 修复HTML img标签
    content = re.sub(
        r'(src=[\'"])../../images/birds/species/bird-image-\d+(?:-alt-\d+)?\.webp([\'"])',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("🚀 快速修复德语文章头图...")
    
    fixed = 0
    total = len(CORRECT_MAPPINGS)
    
    for filepath, correct_num in CORRECT_MAPPINGS.items():
        if fix_file_image(filepath, correct_num):
            fixed += 1
            print(f"✅ {filepath} -> bird-image-{correct_num}.webp")
        else:
            print(f"❌ 文件不存在: {filepath}")
    
    print(f"\n🎯 修复完成: {fixed}/{total}")

if __name__ == "__main__":
    main()