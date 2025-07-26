#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简化版本：从 HTML 文件中提取头图 URL 并更新到 JSON 配置文件中
"""

import json
import os
import re

def extract_background_image_url(html_content):
    """从 HTML 内容中提取背景图片 URL"""
    # 查找 .hero-image 类中的背景图片 URL
    pattern = r'\.hero-image[^}]*background:[^;]*url\([\'"]?([^\'")]+)[\'"]?\)'
    match = re.search(pattern, html_content, re.MULTILINE | re.DOTALL)
    
    if match:
        url = match.group(1).strip('\'"')
        return url
    
    # 备用模式：查找任何 url() 引用
    pattern2 = r'url\([\'"]?([^\'")]+)[\'"]?\)'
    match2 = re.search(pattern2, html_content)
    
    if match2:
        url = match2.group(1).strip('\'"')
        # 只返回图片文件
        if any(ext in url.lower() for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
            return url
    
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
    
    # 尝试不同语言版本的路径
    possible_paths = [
        f"en/{url_path}",  # 英文版本
        url_path,  # 原始路径
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

def update_json_with_extracted_images(json_file):
    """更新 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes_count = 0
    success_count = 0
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        for article in category_data.get('articles', []):
            article_url = article.get('url', '')
            
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
                                success_count += 1
                                print(f"✓ {article.get('id')}: {absolute_url}")
                        else:
                            print(f"✗ {article.get('id')}: 无法提取图片 URL")
                    
                    except Exception as e:
                        print(f"✗ {article.get('id')}: 读取文件错误")
                else:
                    print(f"✗ {article.get('id')}: 找不到 HTML 文件")
    
    # 保存修改后的 JSON 文件
    if changes_count > 0:
        backup_file = json_file + '.bak'
        # 保存修改后的文件
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n成功更新 {success_count} 个图片 URL")
    else:
        print("没有需要修改的图片 URL")

if __name__ == "__main__":
    json_file = "android-article-urls-en.json"
    if os.path.exists(json_file):
        print(f"处理文件: {json_file}")
        update_json_with_extracted_images(json_file)
    else:
        print(f"文件不存在: {json_file}")