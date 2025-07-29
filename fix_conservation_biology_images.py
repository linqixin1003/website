#!/usr/bin/env python3
import os
import re

def fix_conservation_biology_image(file_path):
    """修复保护生物学文章的头图URL"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换各种可能的图片URL模式
        patterns = [
            r"url\('../../images/birds/species/bird-image-077\.webp'\)",
            r"url\('../../images/birds/ecology/ecology-image-007\.webp'\)",
            r"url\('../../images/birds/species/head_conservation_biology\.webp'\)",
            r"src=\"../../images/birds/species/bird-image-077\.webp\"",
            r"src=\"../../images/birds/ecology/ecology-image-007\.webp\"",
            r"src=\"../../images/birds/species/head_conservation_biology\.webp\""
        ]
        
        replacements = [
            "url('../../images/head_conservation_biology.webp')",
            "url('../../images/head_conservation_biology.webp')",
            "url('../../images/head_conservation_biology.webp')",
            'src="../../images/head_conservation_biology.webp"',
            'src="../../images/head_conservation_biology.webp"',
            'src="../../images/head_conservation_biology.webp"'
        ]
        
        modified = False
        for pattern, replacement in zip(patterns, replacements):
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
                print(f"✅ 修复了 {file_path} 中的图片URL")
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            print(f"ℹ️  {file_path} 不需要修复")
            return False
            
    except Exception as e:
        print(f"❌ 修复 {file_path} 时出错: {e}")
        return False

def main():
    """主函数：修复所有语言版本的保护生物学文章"""
    languages = ['zh', 'ru', 'de', 'fr', 'es', 'it', 'ja', 'ko', 'pt']
    
    fixed_count = 0
    
    for lang in languages:
        file_path = f"{lang}/ecology/07-conservation-biology.html"
        if os.path.exists(file_path):
            if fix_conservation_biology_image(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n🎉 总共修复了 {fixed_count} 个文件")
    print("✅ 所有保护生物学文章的头图已更新为 head_conservation_biology.webp")

if __name__ == "__main__":
    main()