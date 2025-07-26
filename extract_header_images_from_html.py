#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从 HTML 文件中解析头图 URL 并更新到 JSON 配置文件中
"""

import json
import os
import re
from pathlib import Path

def extract_background_image_url(html_content):
    """从 HTML 内容中提取背景图片 URL"""
    # 查找 background: linear-gradient(...), url(...) 模式
    pattern = r'background:\s*linear-gradient\([^)]+\),\s*\n?\s*url\([\'"]?([^\'")]+)[\'"]?\)'
    match = re.search(pattern, html_content, re.MULTILINE | re.DOTALL)
    
    if match:
        url = match.group(1).strip('\'"')
        return url
    
    # 备用模式：直接查找 background-image: url(...)
    pattern2 = r'background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)'
    match2 = re.search(pattern2, html_content)
    
    if match2:
        url = match2.group(1).strip('\'"')
        return url
    
    # 第三种模式：查找多行的 background 属性
    pattern3 = r'background:[^;]*url\([\'"]?([^\'")]+)[\'"]?\)[^;]*;'
    match3 = re.search(pattern3, html_content, re.MULTILINE | re.DOTALL)
    
    if match3:
        url = match3.group(1).strip('\'"')
        return url
    
    return None

def convert_relative_to_absolute_url(relative_url, base_url="https://linqixin1003.github.io/website"):
    """将相对路径转换为绝对路径"""
    if relative_url.startswith('http'):
        return relative_url
    
    # 处理相对路径，如 ../../images/birds/species/bird-image-002.png
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
        url_path,  # 原始路径
        f"en/{url_path}",  # 英文版本
        f"zh/{url_path}",  # 中文版本
        f"ja/{url_path}",  # 日文版本
        f"ko/{url_path}",  # 韩文版本
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
                                old_url = article.get('imageUrl', '')
                                article['imageUrl'] = absolute_url
                                changes_count += 1
                                print(f"更新 {article.get('id')}: {article.get('title')}")
                                print(f"  HTML 文件: {html_file}")
                                print(f"  旧 URL: {old_url}")
                                print(f"  新 URL: {absolute_url}")
                        else:
                            print(f"警告: 无法从 {html_file} 中提取背景图片 URL")
                    
                    except Exception as e:
                        print(f"错误: 读取文件 {html_file} 时出错: {e}")
                else:
                    print(f"警告: 找不到文件 {article_url}")
    
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
            update_json_with_extracted_images(json_file)
        else:
            print(f"文件不存在: {json_file}")