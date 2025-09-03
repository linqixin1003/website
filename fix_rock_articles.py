#!/usr/bin/env python3
import os
import shutil

# 支持的语言
languages = ['de', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']

# 英文文章列表
en_articles = {
    'rock-collecting': [
        '01-rock-collecting-basics.html',
        '02-rock-hunting-locations.html',
        '03-essential-rock-collecting-tools.html',
        '04-rock-mineral-identification-basics.html',
        '05-building-a-rock-collection-display.html',
        '06-rock-collecting-history-culture.html',
        '07-rare-and-valuable-rocks.html',
        '08-cleaning-preserving-rock-specimens.html',
        '09-rock-collecting-for-children.html',
        '10-rock-collecting-ethics.html'
    ],
    'rock-formation': [
        '01-the-complete-rock-cycle.html',
        '02-plate-tectonics-rock-formation.html',
        '03-volcanic-processes.html',
        '04-igneous-rocks.html',
        '05-igneous-rock-formation.html',
        '06-sedimentary-layers.html',
        '07-pressure-temperature-effects.html',
        '08-metamorphic-transformation.html',
        '09-crystal-formation-growth.html',
        '10-geological-time-rock-dating.html'
    ],
    'rock-formation-types': [
        '01-rock-cycle-geological-processes.html',
        '02-igneous-rocks-types-formation.html',
        '03-sedimentary-rocks-formation-classification.html',
        '04-metamorphic-rocks-formation-types.html',
        '05-rock-identification-field-techniques.html',
        '06-rock-physical-properties-engineering.html',
        '07-rocks-environmental-processes.html',
        '08-rocks-and-geologic-time.html',
        '09-unusual-rock-types-formations.html',
        '10-rocks-human-civilization.html'
    ],
    'rock-identification': [
        '01-complete-field-identification-guide.html',
        '02-key-mineral-properties.html',
        '03-crystal-systems.html',
        '04-color-streak.html',
        '05-luster-transparency.html',
        '06-cleavage-fracture.html',
        '07-mohs-hardness-scale-testing.html',
        '08-specific-gravity-density.html',
        '09-acid-tests.html',
        '10-expert-identification-techniques.html'
    ],
    'rock-mineral-science': [
        '01-mineral-classification-systems.html',
        '02-mineral-crystallography.html',
        '03-mineral-formation-processes.html',
        '04-physical-chemical-properties.html',
        '05-economic-minerals-uses.html',
        '06-mineral-collections-display.html',
        '07-fluorescent-minerals.html',
        '08-gemstones-precious-treasures.html',
        '09-rocks-minerals-ancient-technology.html',
        '10-rocks-minerals-modern-technology.html'
    ]
}

def check_and_fix_articles():
    for lang in languages:
        print(f"\n=== Checking {lang} ===")
        for category, articles in en_articles.items():
            lang_dir = f"{lang}/{category}"
            if not os.path.exists(lang_dir):
                print(f"  {category}: Directory not found")
                continue
                
            existing_files = [f for f in os.listdir(lang_dir) if f.endswith('.html')]
            existing_files.sort()
            
            print(f"  {category}: {len(existing_files)} articles")
            
            # 检查缺失的文章
            missing_articles = []
            for article in articles:
                if article not in existing_files:
                    missing_articles.append(article)
            
            if missing_articles:
                print(f"    Missing: {missing_articles}")
                
                # 从英文版本复制缺失的文章
                for article in missing_articles:
                    en_file = f"en/{category}/{article}"
                    lang_file = f"{lang_dir}/{article}"
                    
                    if os.path.exists(en_file):
                        shutil.copy2(en_file, lang_file)
                        print(f"    Copied: {article}")
                    else:
                        print(f"    English source not found: {en_file}")

if __name__ == "__main__":
    check_and_fix_articles()
