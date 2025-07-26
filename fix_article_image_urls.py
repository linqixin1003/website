#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复 android-article-urls-en.json 文件中的图片 URL
确保每个文章的 imageUrl 与其 url 路径相匹配
"""

import json
import os
import re

def extract_article_id(url):
    """从 URL 中提取文章 ID"""
    match = re.search(r'/(\d+-[a-z-]+)\.html$', url)
    if match:
        return match.group(1)
    return None

def fix_image_urls(json_file):
    """修复 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 记录修改数量
    changes_count = 0
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        base_url = category_data.get('baseUrl', 'https://linqixin1003.github.io/website')
        
        for article in category_data.get('articles', []):
            article_url = article.get('url', '')
            article_id = extract_article_id(article_url)
            
            if article_id:
                # 构建新的图片 URL
                category_path = article_url.split('/')[1]  # 例如 'birdwatching'
                new_image_url = f"{base_url}/images/{category_path}/{article_id}.jpg"
                
                # 如果 imageUrl 与新构建的不同，则更新
                if article.get('imageUrl') != new_image_url:
                    old_url = article.get('imageUrl', '')
                    article['imageUrl'] = new_image_url
                    changes_count += 1
                    print(f"已更新: {article.get('id')} - {article.get('title')}")
                    print(f"  旧 URL: {old_url}")
                    print(f"  新 URL: {new_image_url}")
    
    # 保存修改后的 JSON 文件
    if changes_count > 0:
        backup_file = json_file + '.bak'
        # 创建备份
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        # 保存修改后的文件
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n总共修改了 {changes_count} 个图片 URL")
        print(f"原文件已备份为: {backup_file}")
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
    ]
    
    for json_file in json_files:
        if os.path.exists(json_file):
            print(f"\n处理文件: {json_file}")
            fix_image_urls(json_file)
        else:
            print(f"文件不存在: {json_file}")