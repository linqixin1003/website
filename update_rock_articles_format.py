#!/usr/bin/env python3
import os
import re

# 定义图片映射关系
image_mappings = {
    # Rock Collecting & Hobby
    'en/rock-collecting/01-rock-collecting-basics.html': 'Rock_Collecting&Hobby/01_Rock_Collecting_Basics.webp',
    'en/rock-collecting/02-rock-hunting-locations.html': 'Rock_Collecting&Hobby/02_Rock_Hunting_Locations.webp',
    'en/rock-collecting/03-essential-rock-collecting-tools.html': 'Rock_Collecting&Hobby/03_Essential_Rock_Collecting_Tools.webp',
    'en/rock-collecting/04-rock-mineral-identification-basics.html': 'Rock_Collecting&Hobby/04_Rock_&_Mineral_Identification_Basics.webp',
    'en/rock-collecting/05-building-a-rock-collection-display.html': 'Rock_Collecting&Hobby/05_Building_a_Rock_Collection_Display.webp',
    'en/rock-collecting/06-rock-collecting-history-culture.html': 'Rock_Collecting&Hobby/06_Rock_Collecting_History_&_Culture.webp',
    'en/rock-collecting/07-rare-and-valuable-rocks.html': 'Rock_Collecting&Hobby/07_Rare_&_Valuable_Rocks.webp',
    'en/rock-collecting/08-cleaning-preserving-rock-specimens.html': 'Rock_Collecting&Hobby/08_Cleaning_&_Preserving_Rock_Specimens.webp',
    'en/rock-collecting/09-rock-collecting-for-children.html': 'Rock_Collecting&Hobby/09_Rock_Collecting_for_Children.webp',
    'en/rock-collecting/10-rock-collecting-ethics.html': 'Rock_Collecting&Hobby/10_Rock_Collecting_Ethics.webp',
    
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
    'en/rock-identification/professional-summary.html': 'Rock&Mineral_Identification/01_Complete_Field_Ientification_Guide.webp',
    
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

def get_bird_style_template():
    """返回bird文章风格的HTML模板"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
        }}

        .hero-image {{
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('{image_url}') center/cover;
            position: relative;
            margin-top: 0;
        }}
        
        .content {{
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }}
        
        .title {{
            font-size: 24px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 30px;
            margin-top: 15px;
            line-height: 1.3;
        }}
        
        .quote-box {{
            background: linear-gradient(135deg, #f3e5f5, #e1bee7);
            border-left: 4px solid #9c27b0;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            font-style: italic;
            color: #4a148c;
        }}
        
        .section {{
            margin-bottom: 30px;
        }}
        
        .section h2 {{
            color: #8B4513;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #D2691E;
        }}
        
        .section p {{
            line-height: 1.7;
            margin-bottom: 15px;
            color: #444;
        }}
        
        .section ul, .section ol {{
            margin-left: 20px;
            margin-bottom: 15px;
        }}
        
        .section li {{
            margin-bottom: 8px;
            line-height: 1.6;
        }}
        
        .highlight {{
            background: linear-gradient(120deg, #a8e6cf 0%, #dcedc1 100%);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #4caf50;
        }}
        
        .tip {{
            background: linear-gradient(120deg, #ffd3a5 0%, #fd9853 100%);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #ff9800;
        }}
        
        @media (max-width: 768px) {{
            .hero-image {{
                height: 250px;
            }}
            
            .content {{
                margin: -20px 10px 10px 10px;
                padding: 20px 15px;
            }}
            
            .title {{
                font-size: 20px;
            }}
            
            .section h2 {{
                font-size: 18px;
            }}
        }}
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">{title}</h1>
        {content}
    </div>
</body>
</html>'''

def extract_title_from_content(content):
    """从HTML内容中提取标题"""
    # 尝试从title标签提取
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
    if title_match:
        return title_match.group(1).strip()
    
    # 尝试从h1标签提取
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content, re.IGNORECASE)
    if h1_match:
        return h1_match.group(1).strip()
    
    return "Rock Article"

def extract_main_content(content):
    """提取文章的主要内容，移除导航和footer"""
    # 移除head部分
    content = re.sub(r'<head>.*?</head>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 提取body内容
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_content = body_match.group(1)
    else:
        body_content = content
    
    # 移除header/nav部分
    body_content = re.sub(r'<header>.*?</header>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
    body_content = re.sub(r'<nav>.*?</nav>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
    
    # 移除footer和"Back to rock explorer"相关内容
    body_content = re.sub(r'<footer>.*?</footer>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
    body_content = re.sub(r'<[^>]*back[^>]*rock[^>]*explorer[^>]*>.*?</[^>]*>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
    body_content = re.sub(r'back\s+to\s+rock\s+explorer', '', body_content, flags=re.IGNORECASE)
    
    # 提取main内容或直接使用body内容
    main_match = re.search(r'<main[^>]*>(.*?)</main>', body_content, re.DOTALL | re.IGNORECASE)
    if main_match:
        return main_match.group(1).strip()
    
    # 移除script标签
    body_content = re.sub(r'<script[^>]*>.*?</script>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
    
    return body_content.strip()

def convert_rock_article_to_bird_format(file_path, image_path):
    """将rock文章转换为bird格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题和内容
        title = extract_title_from_content(content)
        main_content = extract_main_content(content)
        
        # 构建图片URL
        image_url = f"../../images/rock/{image_path}"
        
        # 使用bird风格模板
        new_content = get_bird_style_template().format(
            title=title,
            image_url=image_url,
            content=main_content
        )
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 已转换 {file_path} 为bird格式")
        return True
        
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    success_count = 0
    total_count = len(image_mappings)
    
    print(f"开始转换 {total_count} 个岩石文章为bird格式...")
    
    for file_path, image_path in image_mappings.items():
        if os.path.exists(file_path):
            if convert_rock_article_to_bird_format(file_path, image_path):
                success_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n完成! 成功转换了 {success_count}/{total_count} 个文件")

if __name__ == "__main__":
    main()