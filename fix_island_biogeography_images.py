#!/usr/bin/env python3
import os
import re

def fix_island_biogeography_images():
    """修复所有语言版本的岛屿生物地理学文章头图"""
    
    # 所有语言代码
    languages = ['en', 'zh', 'ru', 'de', 'fr', 'es', 'it', 'ja', 'ko', 'pt']
    
    # 目标图片URL
    target_image = "url('../../images/head_island_biogeography.webp') center/cover;"
    
    fixed_count = 0
    
    for lang in languages:
        file_path = f"{lang}/ecology/08-island-biogeography.html"
        
        if not os.path.exists(file_path):
            print(f"⚠️  文件不存在: {file_path}")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找并替换图片URL
            # 匹配各种可能的图片URL格式
            patterns = [
                r"url\('../../images/[^']+'\) center/cover;",
                r"url\(\"../../images/[^\"]+\"\) center/cover;",
                r"url\('../../images/birds/species/[^']+'\) center/cover;",
                r"url\('../../images/ecology-image-[^']+'\) center/cover;"
            ]
            
            original_content = content
            
            for pattern in patterns:
                if re.search(pattern, content):
                    content = re.sub(pattern, target_image, content)
                    break
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 修复了 {file_path} 中的图片URL")
                fixed_count += 1
            else:
                print(f"ℹ️  {file_path} 不需要修复")
                
        except Exception as e:
            print(f"❌ 处理 {file_path} 时出错: {e}")
    
    print(f"\n🎉 总共修复了 {fixed_count} 个文件")
    print("✅ 所有岛屿生物地理学文章的头图已更新为 head_island_biogeography.webp")

if __name__ == "__main__":
    fix_island_biogeography_images()