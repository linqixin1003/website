#!/usr/bin/env python3
import os
import re

def check_article_format(file_path):
    """检查文章是否符合bird格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'has_hero_image': '.hero-image' in content,
            'has_bird_styles': 'font-family: -apple-system' in content,
            'has_rock_image': 'images/rock/' in content,
            'no_back_to_explorer': 'back to rock explorer' not in content.lower(),
            'has_content_div': 'class="content"' in content
        }
        
        return checks
        
    except Exception as e:
        return {'error': str(e)}

def main():
    """检查所有岩石文章的格式"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    total_files = 0
    perfect_files = 0
    
    print("🔍 检查岩石文章格式转换情况:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"📁 {directory}:")
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in sorted(html_files):
                file_path = os.path.join(directory, html_file)
                total_files += 1
                
                checks = check_article_format(file_path)
                
                if 'error' in checks:
                    print(f"  ❌ {html_file} - 错误: {checks['error']}")
                    continue
                
                # 检查所有条件
                all_good = all(checks.values())
                
                if all_good:
                    print(f"  ✅ {html_file}")
                    perfect_files += 1
                else:
                    issues = [k for k, v in checks.items() if not v]
                    print(f"  ⚠️  {html_file} - 问题: {', '.join(issues)}")
            print()
    
    print(f"📊 总结: {perfect_files}/{total_files} 个文件格式完美")
    print(f"完成率: {perfect_files/total_files*100:.1f}%")

if __name__ == "__main__":
    main()