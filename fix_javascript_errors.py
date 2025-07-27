#!/usr/bin/env python3
import os
import re

def fix_javascript_errors():
    """修复所有HTML文件中的JavaScript错误"""
    
    # 需要修复的文件列表
    files_to_fix = [
        'en/ecology/01-habitat-ecosystems.html',
        'en/ecology/02-food-webs-chains.html',
        'en/ecology/03-migration-patterns.html',
        'en/ecology/04-breeding-ecology.html',
        'en/ecology/05-climate-change-impact.html',
        'en/ecology/06-urban-ecology.html',
        'en/ecology/07-conservation-biology.html',
        'en/ecology/09-pollination-seed-dispersal.html',
        'en/ecology/10-community-dynamics.html',
        'en/knowledge/01-beginners-guide.html',
        'en/knowledge/03-identification-techniques.html',
        'en/knowledge/04-best-locations.html',
        'en/knowledge/05-behavior-observation.html',
        'en/knowledge/06-song-identification.html',
        'en/knowledge/07-photography-tips.html',
        'en/knowledge/08-seasonal-guide.html',
        'en/knowledge/09-journal-keeping.html',
        'en/knowledge/10-ethics-conservation.html',
        'en/birdwatching/01-getting-started.html',
        'en/birdwatching/02-essential-equipment.html',
        'en/birdwatching/03-identification-techniques.html',
        'en/birdwatching/04-best-locations.html',
        'en/birdwatching/05-seasonal-guide.html',
        'en/birdwatching/06-photography-tips.html',
        'en/birdwatching/07-behavior-observation.html',
        'en/birdwatching/08-song-identification.html',
        'en/birdwatching/09-ethics-conservation.html',
        'en/birdwatching/10-journal-keeping.html',
        'en/scientific-wonders/01-bird-flight-mechanics.html',
        'en/scientific-wonders/02-magnetic-navigation.html',
        'en/scientific-wonders/03-hummingbird-mechanics.html',
        'en/scientific-wonders/04-bird-intelligence.html',
        'en/scientific-wonders/05-feather-structure.html',
        'en/scientific-wonders/06-bird-vision.html',
        'en/scientific-wonders/07-egg-development.html',
        'en/scientific-wonders/08-bird-communication.html',
        'en/scientific-wonders/09-migration-physiology.html',
        'en/scientific-wonders/10-biomechanics.html'
    ]
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 修复 current-time 元素访问错误
                old_pattern = r"document\.getElementById\('current-time'\)\.textContent = timeString;"
                new_pattern = """const timeElement = document.getElementById('current-time');
            if (timeElement) {
                timeElement.textContent = timeString;
            }"""
                
                if old_pattern.replace('\\', '') in content:
                    content = re.sub(old_pattern, new_pattern, content)
                    
                    # 修复进度条访问错误
                    progress_old = r"document\.querySelector\('\.progress-fill'\)\.style\.width = progress \+ '%';"
                    progress_new = """const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }"""
                    
                    content = re.sub(progress_old, progress_new, content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixed_count += 1
                    print(f"✅ 已修复: {file_path}")
                else:
                    print(f"⚠️  未找到需要修复的内容: {file_path}")
                    
            except Exception as e:
                print(f"❌ 修复失败 {file_path}: {e}")
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    print(f"\n🎉 修复完成！共修复了 {fixed_count} 个文件")

if __name__ == "__main__":
    fix_javascript_errors()