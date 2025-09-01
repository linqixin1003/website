#!/usr/bin/env python3
import os
import re

# 定义图片映射关系
image_mappings = {
    # Rock Formation Processes
    'en/rock-formation/01-the-complete-rock-cycle.html': 'Rock_Formation_Processes/01_The_Complete_Rock_Cycle.webp',
    'en/rock-formation/02-plate-tectonics-rock-formation.html': 'Rock_Formation_Processes/02_Plate_Tectonics_&_Rock_Formation.webp',
    'en/rock-formation/03-volcanic-processes.html': 'Rock_Formation_Processes/03_Volcanic_Processes.webp',
    'en/rock-formation/04-igneous-rocks.html': 'Rock_Formation_Processes/04_Igneous_Rocks.webp',
    'en/rock-formation/05-igneous-rock-formation.html': 'Rock_Formation_Processes/05_Igneous_Rock_Formation.webp',
    'en/rock-formation/06-sedimentary-layers.html': 'Rock_Formation_Processes/06_Sedimentary_Layers.webp',
    'en/rock-formation/07-pressure-temperature-effects.html': 'Rock_Formation_Processes/07_Pressure_&_Temperature_Effects.webp',
    'en/rock-formation/08-metamorphic-transformation.html': 'Rock_Formation_Processes/08_Metamorphic_Transformation.webp',
    'en/rock-formation/09-crystal-formation-growth.html': 'Rock_Formation_Processes/09_Crystal_Formation_&_Growth.webp',
    'en/rock-formation/10-geological-time-rock-dating.html': 'Rock_Formation_Processes/10_Geological_Time_&_Rock_Dating.webp',
    
    # Rock Formation Types
    'en/rock-formation-types/01-rock-cycle-geological-processes.html': 'Rock_Formation_Types&Classification/01_Rock_Cycle_&_Geological_Processes.webp',
    'en/rock-formation-types/02-igneous-rocks-types-formation.html': 'Rock_Formation_Types&Classification/02_Igneous_Rocks_Types_&_Formation.webp',
    'en/rock-formation-types/03-sedimentary-rocks-formation-classification.html': 'Rock_Formation_Types&Classification/03_Sedimentary_Rocks_Formation_&_Classification.webp',
    'en/rock-formation-types/04-metamorphic-rocks-formation-types.html': 'Rock_Formation_Types&Classification/04_Metamorphic_Rocks_Formation_&_Types.webp',
    'en/rock-formation-types/05-rock-identification-field-techniques.html': 'Rock_Formation_Types&Classification/05_Rock_Identification_Field_Techniques.webp',
    'en/rock-formation-types/06-rock-physical-properties-engineering.html': 'Rock_Formation_Types&Classification/06_Rock_Physical_Properties_&_Engineering.webp',
    'en/rock-formation-types/07-rocks-environmental-processes.html': 'Rock_Formation_Types&Classification/07_Rocks_&_Environmental_Processes.webp',
    'en/rock-formation-types/08-rocks-and-geologic-time.html': 'Rock_Formation_Types&Classification/08_Rocks_&_Geologic_Time.webp',
    'en/rock-formation-types/09-unusual-rock-types-formations.html': 'Rock_Formation_Types&Classification/09_Unusual_Rock_Types_&_Formations.webp',
    'en/rock-formation-types/10-rocks-human-civilization.html': 'Rock_Formation_Types&Classification/10_Rocks_&_Human_Civilization.webp',
    
    # Rock Identification
    'en/rock-identification/01-complete-field-identification-guide.html': 'Rock&Mineral_Identification/01_Complete_Field_Ientification_Guide.webp',
    'en/rock-identification/02-key-mineral-properties.html': 'Rock&Mineral_Identification/02_Key_Mineral_Properties.webp',
    'en/rock-identification/03-crystal-systems.html': 'Rock&Mineral_Identification/03_Crystal_Systems_&_Symmetry.webp',
    'en/rock-identification/04-color-streak.html': 'Rock&Mineral_Identification/04_Color_&_Streak_Analysis.webp',
    'en/rock-identification/05-luster-transparency.html': 'Rock&Mineral_Identification/05_Luster_&_Transparency.webp',
    'en/rock-identification/06-cleavage-fracture.html': 'Rock&Mineral_Identification/06_Cleavage_&_Fracture_Patterns.webp',
    'en/rock-identification/07-mohs-hardness-scale-testing.html': 'Rock&Mineral_Identification/07_Mohs_Hardness_Scale_Testing.webp',
    'en/rock-identification/08-specific-gravity-density.html': 'Rock&Mineral_Identification/08_Specific_Gravity_&_Density.webp',
    'en/rock-identification/09-acid-tests.html': 'Rock&Mineral_Identification/09_Chemical_Testing_&_Acid_Tests.webp',
    'en/rock-identification/10-expert-identification-techniques.html': 'Rock&Mineral_Identification/10_Expert_Identification_Techniques.webp',
    
    # Rock Mineral Science
    'en/rock-mineral-science/01-mineral-classification-systems.html': 'Rock&Mineral_Science/01_Mineral_Classification_Systems.webp',
    'en/rock-mineral-science/02-mineral-crystallography.html': 'Rock&Mineral_Science/02_Mineral_Crystallography.webp',
    'en/rock-mineral-science/03-mineral-formation-processes.html': 'Rock&Mineral_Science/03_Mineral_Formation_Processes.webp',
    'en/rock-mineral-science/04-physical-chemical-properties.html': 'Rock&Mineral_Science/04_Physical_&_Chemical_Properties.webp',
    'en/rock-mineral-science/05-economic-minerals-uses.html': 'Rock&Mineral_Science/05_Economic_Minerals_&_Uses.webp',
    'en/rock-mineral-science/06-mineral-collections-display.html': 'Rock&Mineral_Science/06_Mineral_Collections_&_Display.webp',
    'en/rock-mineral-science/07-fluorescent-minerals.html': 'Rock&Mineral_Science/07_Fluorescent_Minerals.webp',
    'en/rock-mineral-science/08-gemstones-precious-treasures.html': 'Rock&Mineral_Science/08_Gemstones_Precious_Treasures.webp',
    'en/rock-mineral-science/09-rocks-minerals-ancient-technology.html': 'Rock&Mineral_Science/09_Rocks_&_Minerals_in_Ancient_Technology.webp',
    'en/rock-mineral-science/10-rocks-minerals-modern-technology.html': 'Rock&Mineral_Science/10_Rocks_&_Minerals_in_Modern_Technology.webp'
}

def update_hero_background_image(file_path, image_path):
    """更新HTML文件中的hero背景图片"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换hero-image的背景图片URL
        # 匹配模式：url('../../images/...') 或 url("../../images/...")
        pattern = r"(\.hero-image\s*{[^}]*background:[^;]*url\s*\(\s*['\"]?)([^'\"]*?)(['\"]?\s*\)[^;}]*)"
        
        def replace_bg_image(match):
            prefix = match.group(1)
            old_url = match.group(2)
            suffix = match.group(3)
            new_url = f"../../images/rock/{image_path}"
            return f"{prefix}{new_url}{suffix}"
        
        new_content = re.sub(pattern, replace_bg_image, content, flags=re.DOTALL | re.IGNORECASE)
        
        # 如果没有找到hero-image样式，尝试查找其他背景图片模式
        if new_content == content:
            # 查找任何包含images/的背景图片
            pattern2 = r"(url\s*\(\s*['\"]?)([^'\"]*?images/[^'\"]*?)(['\"]?\s*\))"
            
            def replace_any_bg_image(match):
                prefix = match.group(1)
                old_url = match.group(2)
                suffix = match.group(3)
                # 如果是相对路径，保持相对路径结构
                if old_url.startswith('../../'):
                    new_url = f"../../images/rock/{image_path}"
                else:
                    new_url = f"images/rock/{image_path}"
                return f"{prefix}{new_url}{suffix}"
            
            new_content = re.sub(pattern2, replace_any_bg_image, content, flags=re.IGNORECASE)
        
        # 如果内容有变化，写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已更新 {file_path} 的背景图片")
            return True
        else:
            print(f"⚠️  {file_path} 未找到可更新的背景图片")
            return False
            
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    success_count = 0
    total_count = len(image_mappings)
    
    print(f"开始更新 {total_count} 个岩石文章的背景图片...")
    
    for file_path, image_path in image_mappings.items():
        if os.path.exists(file_path):
            if update_hero_background_image(file_path, image_path):
                success_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n完成! 成功处理了 {success_count}/{total_count} 个文件")

if __name__ == "__main__":
    main()