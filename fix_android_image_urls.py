#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复 android-article-urls-en.json 文件中的图片 URL
确保每个文章的 imageUrl 与其 url 路径相匹配
"""

import json
import os

def fix_image_urls(json_file):
    """修复 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 记录修改数量
    changes_count = 0
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            article_url = article.get('url', '')
            article_id = article.get('id', '')
            
            if article_url:
                # 从 URL 中提取路径部分，例如 "/birdwatching/01-getting-started.html"
                url_parts = article_url.strip('/').split('.')
                if len(url_parts) > 0:
                    path_without_extension = url_parts[0]  # 去掉 .html 后缀
                    
                    # 构建新的图片 URL
                    new_image_url = f"https://linqixin1003.github.io/website/images/{path_without_extension}.jpg"
                    
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
    json_file = "android-article-urls-en.json"
    if os.path.exists(json_file):
        fix_image_urls(json_file)
    else:
        print(f"文件不存在: {json_file}")