#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
完整提取所有 HTML 文件的头图，确保每个 imageUrl 都指向对应 HTML 的实际头图
"""

import json
import os
import re

def extract_image_from_html(html_file_path):
    """从 HTML 文件中提取头图 URL"""
    if not os.path.exists(html_file_path):
        return None
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 多种正则表达式模式来匹配不同的图片引用方式
        patterns = [
            # 1. CSS background 样式
            r'background:[^;]*url\([\'"]?([^\'")]+)[\'"]?\)',
            # 2. background-image 样式
            r'background-image:[^;]*url\([\'"]?([^\'")]+)[\'"]?\)',
            # 3. style 属性中的 background
            r'style="[^"]*background[^"]*url\([\'"]?([^\'")]+)[\'"]?\)',
            # 4. img 标签的 src
            r'<img[^>]+src=[\'"]([^\'">]+)[\'"]',
            # 5. hero-image 类的背景
            r'\.hero-image[^}]*background[^}]*url\([\'"]?([^\'")]+)[\'"]?\)',
            # 6. header 相关的图片
            r'header[^}]*background[^}]*url\([\'"]?([^\'")]+)[\'"]?\)',
            # 7. 任何包含 bird-image 的 URL
            r'url\([\'"]?([^\'")]*bird-image[^\'")]*)[\'"]?\)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if 'bird-image' in match or 'birds/' in match:
                    # 处理相对路径
                    if match.startswith('../../'):
                        # 转换为绝对 URL
                        image_path = match.replace('../../', '')
                        return f"https://linqixin1003.github.io/website/{image_path}"
                    elif match.startswith('/'):
                        return f"https://linqixin1003.github.io/website{match}"
                    elif match.startswith('http'):
                        return match
                    else:
                        return f"https://linqixin1003.github.io/website/{match}"
        
        return None
        
    except Exception as e:
        print(f"❌ 读取文件 {html_file_path} 时出错: {e}")
        return None

def extract_all_images():
    """提取所有 HTML 文件的头图并更新 JSON 配置"""
    
    # 所有语言版本的 JSON 文件
    json_files = [
        "android-article-urls-en.json",
        "android-article-urls-zh.json", 
        "android-article-urls-ja.json",
        "android-article-urls-ko.json",
        "android-article-urls-fr.json",
        "android-article-urls-de.json",
        "android-article-urls-it.json",
        "android-article-urls-pt.json",
        "android-article-urls-ru.json",
    ]
    
    for json_file in json_files:
        if not os.path.exists(json_file):
            print(f"❌ 文件不存在: {json_file}")
            continue
            
        print(f"\n📝 处理文件: {json_file}")
        print("=" * 50)
        
        # 读取 JSON 文件
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changes_count = 0
        
        # 遍历所有分类和文章
        for category_key, category_data in data['articleCategories'].items():
            print(f"\n📂 处理分类: {category_key}")
            
            for article in category_data.get('articles', []):
                article_id = article.get('id')
                article_url = article.get('url', '')
                
                if article_url:
                    # 构建 HTML 文件路径
                    html_path = f"en{article_url}"
                    
                    # 提取图片 URL
                    extracted_image_url = extract_image_from_html(html_path)
                    
                    if extracted_image_url:
                        current_url = article.get('imageUrl', '')
                        if current_url != extracted_image_url:
                            article['imageUrl'] = extracted_image_url
                            changes_count += 1
                            print(f"  ✓ {article_id}: 更新头图")
                            print(f"    HTML: {html_path}")
                            print(f"    新图片: {extracted_image_url.split('/')[-1]}")
                        else:
                            print(f"  = {article_id}: 已是正确的 URL")
                    else:
                        print(f"  ⚠️  {article_id}: HTML 中未找到图片 ({html_path})")
        
        # 保存修改后的文件
        if changes_count > 0:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"\n✅ 成功更新 {changes_count} 个图片 URL")
        else:
            print(f"\n= 没有需要修改的图片 URL")

if __name__ == "__main__":
    extract_all_images()