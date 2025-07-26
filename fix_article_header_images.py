#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复 android-article-urls-en.json 文件中的图片 URL
确保每个文章的 imageUrl 是对应 HTML 文件的头图
"""

import json
import os
import re

def extract_html_path(url):
    """从 URL 中提取 HTML 路径"""
    # 去掉开头的斜杠
    if url.startswith('/'):
        url = url[1:]
    return url

def fix_image_urls(json_file):
    """修复 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 记录修改数量
    changes_count = 0
    
    base_url = "https://linqixin1003.github.io/website"
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            article_url = article.get('url', '')
            
            if article_url:
                # 提取 HTML 路径，例如 "/birdwatching/01-getting-started.html"
                html_path = extract_html_path(article_url)
                
                # 构建新的图片 URL（头图，PNG 格式）
                new_image_url = f"{base_url}/images/headers/{html_path}"
                # 将 .html 替换为 .png
                new_image_url = new_image_url.replace('.html', '.png')
                
                # 如果 imageUrl 与新构建的不同，则更新
                if article.get('imageUrl') != new_image_url:
                    article['imageUrl'] = new_image_url
                    changes_count += 1
    
    # 保存修改后的 JSON 文件
    if changes_count > 0:
        backup_file = json_file + '.bak'
        # 创建备份
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        # 保存修改后的文件
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"已修改 {changes_count} 个图片 URL，原文件已备份为 {backup_file}")
    else:
        print("没有需要修改的图片 URL")

if __name__ == "__main__":
    json_files = [
        "android-article-urls-en.json",
        "android-article-urls-zh.json",
        "android-article-urls-ja.json",
        "android-article-urls-ko.json",
        "android-article-urls-fr.json",
        "android-article-urls-es.json",
        "android-article-urls-de.json",
        "android-article-urls-it.json",
        "android-article-urls-pt.json",
        "android-article-urls-ru.json",
        "android-article-urls-en-us.json"
    ]
    
    for json_file in json_files:
        if os.path.exists(json_file):
            print(f"\n处理文件: {json_file}")
            fix_image_urls(json_file)
        else:
            print(f"文件不存在: {json_file}")