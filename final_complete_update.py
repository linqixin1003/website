#!/usr/bin/env python3
import os
import re
import shutil

def copy_image_if_not_exists(src, dest):
    """复制图片文件，如果目标不存在"""
    if not os.path.exists(dest):
        if os.path.exists(src):
            shutil.copy2(src, dest)
            print(f"✅ 创建图片: {dest}")
        else:
            print(f"❌ 源文件不存在: {src}")

def create_missing_images():
    """创建所有缺失的图片文件"""
    base_path = "images/birds/species/"
    
    # 创建所有需要的图片文件
    images_to_create = [
        # 主页面头图
        ("bird-image-001.webp", "scientific-wonders-header.webp"),
        ("bird-image-007.webp", "birdwatching-header.webp"),
        ("bird-image-020.webp", "knowledge-header.webp"),
        ("bird-image-050.webp", "cultural-symbolism-header.webp"),
        ("bird-image-015.webp", "ecology-header.webp"),
        ("bird-image-090.webp", "pet-care-header.webp"),
        
        # 观鸟文章图片
        ("bird-image-002.webp", "birdwatching-01-getting-started.webp"),
        ("bird-image-001.webp", "birdwatching-02-essential-equipment.webp"),
        ("bird-image-007.webp", "birdwatching-03-identification-techniques.webp"),
        ("bird-image-023.webp", "birdwatching-04-best-locations.webp"),
        ("bird-image-006.webp", "birdwatching-05-seasonal-guide.webp"),
        ("bird-image-005.webp", "birdwatching-06-photography-tips.webp"),
        ("bird-image-008.webp", "birdwatching-07-behavior-observation.webp"),
        ("bird-image-003.webp", "birdwatching-08-song-identification.webp"),
        ("bird-image-009.webp", "birdwatching-09-ethics-conservation.webp"),
        ("bird-image-004.webp", "birdwatching-10-journal-keeping.webp"),
        
        # 知识文章图片
        ("bird-image-020.webp", "knowledge-01-beginners-guide.webp"),
        ("bird-image-021.webp", "knowledge-02-essential-equipment.webp"),
        ("bird-image-022.webp", "knowledge-03-identification-techniques.webp"),
        ("bird-image-023.webp", "knowledge-04-best-locations.webp"),
        ("bird-image-024.webp", "knowledge-05-behavior-observation.webp"),
        ("bird-image-025.webp", "knowledge-06-song-identification.webp"),
        ("bird-image-026.webp", "knowledge-07-photography-tips.webp"),
        ("bird-image-027.webp", "knowledge-08-seasonal-guide.webp"),
        ("bird-image-028.webp", "knowledge-09-journal-keeping.webp"),
        ("bird-image-029.webp", "knowledge-10-ethics-conservation.webp"),
        
        # 宠物护理文章图片
        ("bird-image-090.webp", "pet-care-09-enrichment-activities.webp"),
        ("bird-image-020.webp", "pet-care-11-senior-bird-care.webp"),
        
        # 文化象征文章图片
        ("bird-image-015.webp", "cultural-symbolism-01-american-eagle.webp"),
        ("bird-image-062.webp", "cultural-symbolism-02-turkey-thanksgiving.webp"),
        ("bird-image-003.webp", "cultural-symbolism-03-swan-mythology.webp"),
        ("bird-image-004.webp", "cultural-symbolism-04-owl-folklore.webp"),
        ("bird-image-005.webp", "cultural-symbolism-05-duck-conservation.webp"),
        ("bird-image-006.webp", "cultural-symbolism-06-carolina-parakeet.webp"),
        ("bird-image-007.webp", "cultural-symbolism-07-red-tailed-hawk.webp"),
        ("bird-image-008.webp", "cultural-symbolism-08-canada-goose.webp"),
        ("bird-image-009.webp", "cultural-symbolism-09-golden-eagle.webp"),
        ("bird-image-010.webp", "cultural-symbolism-10-literature-art.webp"),
    ]
    
    for src_name, dest_name in images_to_create:
        src_path = os.path.join(base_path, src_name)
        dest_path = os.path.join(base_path, dest_name)
        copy_image_if_not_exists(src_path, dest_path)

def update_html_files():
    """更新所有HTML文件中的图片引用"""
    
    # 图片映射规则
    image_mappings = {
        # 主页面头图映射
        'scientific-wonders.html': {
            'bird-image-001.webp': 'scientific-wonders-header.webp',
            'bird-image-030.webp': 'scientific-wonders-header.webp',
            'bird-image-010.webp': 'scientific-wonders-header.webp',
        },
        'birdwatching.html': {
            'bird-image-007.webp': 'birdwatching-header.webp',
        },
        'knowledge.html': {
            'bird-image-020.webp': 'knowledge-header.webp',
        },
        'cultural-symbolism.html': {
            'bird-image-050.webp': 'cultural-symbolism-header.webp',
            'bird-image-001.webp': 'cultural-symbolism-header.webp',
        },
        'ecology.html': {
            'bird-image-015.webp': 'ecology-header.webp',
        },
        'pet-care.html': {
            'bird-image-090.webp': 'pet-care-header.webp',
        },
        
        # 观鸟文章映射
        'birdwatching/01-getting-started.html': {
            'bird-image-002.webp': 'birdwatching-01-getting-started.webp',
        },
        'birdwatching/02-essential-equipment.html': {
            'bird-image-001.webp': 'birdwatching-02-essential-equipment.webp',
        },
        'birdwatching/03-identification-techniques.html': {
            'bird-image-007.webp': 'birdwatching-03-identification-techniques.webp',
        },
        'birdwatching/04-best-locations.html': {
            'bird-image-023.webp': 'birdwatching-04-best-locations.webp',
        },
        'birdwatching/05-seasonal-guide.html': {
            'bird-image-006.webp': 'birdwatching-05-seasonal-guide.webp',
        },
        'birdwatching/06-photography-tips.html': {
            'bird-image-005.webp': 'birdwatching-06-photography-tips.webp',
        },
        'birdwatching/07-behavior-observation.html': {
            'bird-image-008.webp': 'birdwatching-07-behavior-observation.webp',
        },
        'birdwatching/08-song-identification.html': {
            'bird-image-003.webp': 'birdwatching-08-song-identification.webp',
        },
        'birdwatching/09-ethics-conservation.html': {
            'bird-image-009.webp': 'birdwatching-09-ethics-conservation.webp',
        },
        'birdwatching/10-journal-keeping.html': {
            'bird-image-004.webp': 'birdwatching-10-journal-keeping.webp',
        },
        
        # 知识文章映射
        'knowledge/01-beginners-guide.html': {
            'bird-image-001.webp': 'knowledge-01-beginners-guide.webp',
        },
        'knowledge/02-essential-equipment.html': {
            'bird-image-021.webp': 'knowledge-02-essential-equipment.webp',
        },
        'knowledge/03-identification-techniques.html': {
            'bird-image-022.webp': 'knowledge-03-identification-techniques.webp',
        },
        'knowledge/04-best-locations.html': {
            'bird-image-023.webp': 'knowledge-04-best-locations.webp',
        },
        'knowledge/05-behavior-observation.html': {
            'bird-image-024.webp': 'knowledge-05-behavior-observation.webp',
        },
        'knowledge/06-song-identification.html': {
            'bird-image-025.webp': 'knowledge-06-song-identification.webp',
        },
        'knowledge/07-photography-tips.html': {
            'bird-image-026.webp': 'knowledge-07-photography-tips.webp',
        },
        'knowledge/08-seasonal-guide.html': {
            'bird-image-027.webp': 'knowledge-08-seasonal-guide.webp',
        },
        'knowledge/09-journal-keeping.html': {
            'bird-image-028.webp': 'knowledge-09-journal-keeping.webp',
        },
        'knowledge/10-ethics-conservation.html': {
            'bird-image-029.webp': 'knowledge-10-ethics-conservation.webp',
        },
        
        # 宠物护理文章映射
        'pet-care/09-enrichment-activities.html': {
            'bird-image-090.webp': 'pet-care-09-enrichment-activities.webp',
        },
        'pet-care/11-senior-bird-care.html': {
            'bird-image-020.webp': 'pet-care-11-senior-bird-care.webp',
        },
        
        # 文化象征文章映射
        'cultural-symbolism': {
            'bird-image-015.webp': 'cultural-symbolism-01-american-eagle.webp',
            'bird-image-062.webp': 'cultural-symbolism-02-turkey-thanksgiving.webp',
            'bird-image-003.webp': 'cultural-symbolism-03-swan-mythology.webp',
            'bird-image-004.webp': 'cultural-symbolism-04-owl-folklore.webp',
            'bird-image-005.webp': 'cultural-symbolism-05-duck-conservation.webp',
            'bird-image-006.webp': 'cultural-symbolism-06-carolina-parakeet.webp',
            'bird-image-007.webp': 'cultural-symbolism-07-red-tailed-hawk.webp',
            'bird-image-008.webp': 'cultural-symbolism-08-canada-goose.webp',
            'bird-image-009.webp': 'cultural-symbolism-09-golden-eagle.webp',
            'bird-image-010.webp': 'cultural-symbolism-10-literature-art.webp',
        },
    }
    
    # 通用映射规则（适用于所有文件）
    general_mappings = {
        # 观鸟文章
        'bird-image-002.webp': 'birdwatching-01-getting-started.webp',
        'bird-image-001.webp': 'birdwatching-02-essential-equipment.webp',
        'bird-image-007.webp': 'birdwatching-03-identification-techniques.webp',
        'bird-image-023.webp': 'birdwatching-04-best-locations.webp',
        'bird-image-006.webp': 'birdwatching-05-seasonal-guide.webp',
        'bird-image-005.webp': 'birdwatching-06-photography-tips.webp',
        'bird-image-008.webp': 'birdwatching-07-behavior-observation.webp',
        'bird-image-003.webp': 'birdwatching-08-song-identification.webp',
        'bird-image-009.webp': 'birdwatching-09-ethics-conservation.webp',
        'bird-image-004.webp': 'birdwatching-10-journal-keeping.webp',
        
        # 知识文章
        'bird-image-020.webp': 'knowledge-01-beginners-guide.webp',
        'bird-image-021.webp': 'knowledge-02-essential-equipment.webp',
        'bird-image-022.webp': 'knowledge-03-identification-techniques.webp',
        # 'bird-image-023.webp': 'knowledge-04-best-locations.webp',  # 与观鸟冲突，在特定文件中处理
        'bird-image-024.webp': 'knowledge-05-behavior-observation.webp',
        'bird-image-025.webp': 'knowledge-06-song-identification.webp',
        'bird-image-026.webp': 'knowledge-07-photography-tips.webp',
        'bird-image-027.webp': 'knowledge-08-seasonal-guide.webp',
        'bird-image-028.webp': 'knowledge-09-journal-keeping.webp',
        'bird-image-029.webp': 'knowledge-10-ethics-conservation.webp',
        
        # 宠物护理
        'bird-image-090.webp': 'pet-care-09-enrichment-activities.webp',
        
        # 文化象征
        'bird-image-015.webp': 'cultural-symbolism-01-american-eagle.webp',
        'bird-image-062.webp': 'cultural-symbolism-02-turkey-thanksgiving.webp',
        # 'bird-image-003.webp': 'cultural-symbolism-03-swan-mythology.webp',  # 与观鸟冲突
        # 'bird-image-004.webp': 'cultural-symbolism-04-owl-folklore.webp',    # 与观鸟冲突
        # 'bird-image-005.webp': 'cultural-symbolism-05-duck-conservation.webp', # 与观鸟冲突
        # 'bird-image-006.webp': 'cultural-symbolism-06-carolina-parakeet.webp', # 与观鸟冲突
        # 'bird-image-007.webp': 'cultural-symbolism-07-red-tailed-hawk.webp',   # 与观鸟冲突
        # 'bird-image-008.webp': 'cultural-symbolism-08-canada-goose.webp',      # 与观鸟冲突
        # 'bird-image-009.webp': 'cultural-symbolism-09-golden-eagle.webp',      # 与观鸟冲突
        'bird-image-010.webp': 'cultural-symbolism-10-literature-art.webp',
        
        # 头图映射
        'bird-image-050.webp': 'cultural-symbolism-header.webp',
        'bird-image-030.webp': 'scientific-wonders-header.webp',
    }
    
    # 查找所有HTML文件
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    
    updated_count = 0
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 获取文件相对路径用于特定映射
            rel_path = os.path.relpath(file_path, '.')
            
            # 应用特定文件映射
            for pattern, mappings in image_mappings.items():
                if pattern in rel_path:
                    for old_img, new_img in mappings.items():
                        content = re.sub(
                            r'bird-image-\d+\.webp',
                            lambda m: new_img if m.group() == old_img else m.group(),
                            content
                        )
            
            # 应用通用映射
            for old_img, new_img in general_mappings.items():
                content = content.replace(old_img, new_img)
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已更新: {rel_path}")
                updated_count += 1
                
        except Exception as e:
            print(f"❌ 处理文件失败 {file_path}: {e}")
    
    print(f"\n🎉 完成！共更新了 {updated_count} 个文件")

if __name__ == "__main__":
    print("开始创建缺失的图片文件...")
    create_missing_images()
    
    print("\n开始更新HTML文件...")
    update_html_files()