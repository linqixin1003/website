#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_de_ecology_file(filepath):
    """修复德语ecology文件的头部和样式"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取文件名以确定正确的头图
        filename = os.path.basename(filepath)
        
        # 根据文件名确定头图
        image_mapping = {
            '01-habitat-ecosystems.html': 'bird-image-062.webp',
            '02-food-webs-chains.html': 'bird-image-076.webp',
            '03-migration-patterns.html': 'bird-image-089.webp',
            '04-breeding-ecology.html': 'bird-image-095.webp',
            '05-climate-change-impact.html': 'bird-image-101.webp',
            '06-urban-ecology.html': 'bird-image-107.webp',
            '07-conservation-biology.html': 'bird-image-113.webp',
            '08-island-biogeography.html': 'bird-image-119.webp',
            '09-pollination-seed-dispersal.html': 'bird-image-125.webp',
            '10-community-dynamics.html': 'bird-image-131.webp'
        }
        
        image_file = image_mapping.get(filename, 'bird-image-062.webp')
        
        # 修复HTML结构
        # 1. 修复DOCTYPE和html标签
        content = re.sub(r'<html lang="de">', '<html lang="de">', content)
        content = re.sub(r'<kopf>', '<head>', content)
        content = re.sub(r'</kopf>', '</head>', content)
        content = re.sub(r'<körper>', '<body>', content)
        content = re.sub(r'</körper>', '</body>', content)
        
        # 2. 修复viewport meta标签
        content = re.sub(
            r'<meta content="width=device-width, initial-scale=1\.0, maximum-scale=5\.0, user-scalable=yes, viewport-fit=cover, shrink-to-fit=no" name="viewport"/>',
            '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>',
            content
        )
        
        # 3. 修复CSS链接
        content = re.sub(r'href="../../Ökologie-theme\.css"', 'href="../../ecology-theme.css"', content)
        
        # 4. 替换复杂的移动端CSS为简单的头图样式
        css_pattern = r'<style>.*?</style>'
        new_css = f'''<style>
        .hero-image img {{
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }}
        .article-card img {{
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }}
        .hero-image {{
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/{image_file}') center/cover;
        }}
        .article-meta {{
            margin-top: 15px !important;
        }}
    </style>'''
        
        content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)
        
        # 5. 移除科学注释
        content = re.sub(r'<div class="wissenschaftlich-note">.*?</div>', '', content, flags=re.DOTALL)
        
        # 6. 确保正确的头图div
        content = re.sub(r'<!-- Hauptbild -->\s*<div class="hero-image"></div>', '<div class="hero-image"></div>', content)
        content = re.sub(r'<div class="hero-image"></div>', '<div class="hero-image"></div>', content)
        
        # 7. 修复JavaScript中的document.Körper为document.body
        content = re.sub(r'document\.Körper', 'document.body', content)
        
        # 8. 移除底部的额外内容
        content = re.sub(r'<section class="Ökosystem-context">.*?</footer>', '', content, flags=re.DOTALL)
        
        # 9. 确保正确的结束标签
        if not content.strip().endswith('</html>'):
            content = content.rstrip() + '\n</body>\n</html>'
        
        # 写回文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已修复: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ 修复失败 {filepath}: {e}")
        return False

def main():
    """主函数"""
    de_ecology_dir = 'de/ecology'
    
    if not os.path.exists(de_ecology_dir):
        print(f"❌ 目录不存在: {de_ecology_dir}")
        return
    
    # 获取所有HTML文件
    html_files = [f for f in os.listdir(de_ecology_dir) if f.endswith('.html')]
    html_files.sort()
    
    print(f"🔧 开始修复德语ecology文章头图和样式...")
    print(f"📁 目录: {de_ecology_dir}")
    print(f"📄 文件数量: {len(html_files)}")
    print("-" * 50)
    
    success_count = 0
    for filename in html_files:
        filepath = os.path.join(de_ecology_dir, filename)
        if fix_de_ecology_file(filepath):
            success_count += 1
    
    print("-" * 50)
    print(f"✅ 修复完成: {success_count}/{len(html_files)} 个文件")

if __name__ == "__main__":
    main()