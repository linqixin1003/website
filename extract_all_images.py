#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
完整版本：从所有 HTML 文件中提取头图 URL 并更新到所有语言版本的 JSON 配置文件中
"""

import json
import os
import re

def extract_background_image_url(html_content):
    """从 HTML 内容中提取背景图片 URL"""
    # 查找任何 url() 引用
    pattern = r'url\([\'"]?([^\'")]+)[\'"]?\)'
    matches = re.findall(pattern, html_content)
    
    for url in matches:
        # 只返回图片文件
        if any(ext in url.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
            return url.strip('\'"')
    
    return None

def convert_relative_to_absolute_url(relative_url, base_url="https://linqixin1003.github.io/website"):
    """将相对路径转换为绝对路径"""
    if relative_url.startswith('http'):
        return relative_url
    
    # 处理相对路径，如 ../../images/birds/species/bird-image-001.png
    if relative_url.startswith('../'):
        # 移除开头的 ../
        clean_path = relative_url.replace('../', '')
        return f"{base_url}/{clean_path}"
    elif relative_url.startswith('./'):
        clean_path = relative_url[2:]
        return f"{base_url}/{clean_path}"
    elif relative_url.startswith('/'):
        return f"{base_url}{relative_url}"
    else:
        return f"{base_url}/{relative_url}"

def find_html_file(url_path):
    """根据 URL 路径查找对应的 HTML 文件"""
    # 移除开头的斜杠
    if url_path.startswith('/'):
        url_path = url_path[1:]
    
    # 尝试英文版本的路径
    html_file = f"en/{url_path}"
    if os.path.exists(html_file):
        return html_file
    
    return None

def update_json_with_extracted_images(json_file):
    """更新 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes_count = 0
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        print(f"\n处理分类: {category_key}")
        
        for article in category_data.get('articles', []):
            article_url = article.get('url', '')
            article_id = article.get('id', '')
            
            if article_url:
                # 查找对应的 HTML 文件
                html_file = find_html_file(article_url)
                
                if html_file and os.path.exists(html_file):
                    try:
                        # 读取 HTML 文件内容
                        with open(html_file, 'r', encoding='utf-8') as f:
                            html_content = f.read()
                        
                        # 提取背景图片 URL
                        bg_image_url = extract_background_image_url(html_content)
                        
                        if bg_image_url:
                            # 转换为绝对路径
                            absolute_url = convert_relative_to_absolute_url(bg_image_url)
                            
                            # 更新 JSON 中的 imageUrl
                            if article.get('imageUrl') != absolute_url:
                                article['imageUrl'] = absolute_url
                                changes_count += 1
                                print(f"  ✓ {article_id}: {absolute_url}")
                            else:
                                print(f"  = {article_id}: 已是正确的 URL")
                        else:
                            print(f"  ✗ {article_id}: 无法提取图片 URL")
                    
                    except Exception as e:
                        print(f"  ✗ {article_id}: 读取文件错误 - {e}")
                else:
                    print(f"  ✗ {article_id}: 找不到 HTML 文件 {html_file}")
    
    # 保存修改后的 JSON 文件
    if changes_count > 0:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ 成功更新 {changes_count} 个图片 URL")
    else:
        print("\n= 没有需要修改的图片 URL")

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
            print(f"\n{'='*50}")
            print(f"处理文件: {json_file}")
            print(f"{'='*50}")
            update_json_with_extracted_images(json_file)
        else:
            print(f"文件不存在: {json_file}")