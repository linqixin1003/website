#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
验证所有文章的 imageUrl 是否与 HTML 文件中的实际头图匹配
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

def verify_json_image_urls(json_file):
    """验证 JSON 文件中的图片 URL"""
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"验证文件: {json_file}")
    print(f"{'='*60}")
    
    total_articles = 0
    correct_urls = 0
    incorrect_urls = 0
    missing_html = 0
    no_image_found = 0
    
    # 遍历所有分类和文章
    for category_key, category_data in data['articleCategories'].items():
        print(f"\n📂 分类: {category_key}")
        print("-" * 40)
        
        for article in category_data.get('articles', []):
            total_articles += 1
            article_url = article.get('url', '')
            article_id = article.get('id', '')
            current_image_url = article.get('imageUrl', '')
            
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
                            expected_url = convert_relative_to_absolute_url(bg_image_url)
                            
                            # 比较当前 URL 和期望 URL
                            if current_image_url == expected_url:
                                print(f"  ✅ {article_id}: 正确")
                                correct_urls += 1
                            else:
                                print(f"  ❌ {article_id}: 不匹配")
                                print(f"     当前: {current_image_url}")
                                print(f"     应为: {expected_url}")
                                incorrect_urls += 1
                        else:
                            print(f"  ⚠️  {article_id}: HTML 中未找到图片")
                            no_image_found += 1
                    
                    except Exception as e:
                        print(f"  ❌ {article_id}: 读取文件错误 - {e}")
                        incorrect_urls += 1
                else:
                    print(f"  ❌ {article_id}: 找不到 HTML 文件")
                    missing_html += 1
    
    # 输出统计结果
    print(f"\n{'='*60}")
    print(f"验证结果统计:")
    print(f"{'='*60}")
    print(f"📊 总文章数: {total_articles}")
    print(f"✅ 正确的 URL: {correct_urls}")
    print(f"❌ 不匹配的 URL: {incorrect_urls}")
    print(f"⚠️  HTML 中未找到图片: {no_image_found}")
    print(f"❌ 找不到 HTML 文件: {missing_html}")
    
    accuracy = (correct_urls / total_articles * 100) if total_articles > 0 else 0
    print(f"🎯 准确率: {accuracy:.1f}%")
    
    return {
        'total': total_articles,
        'correct': correct_urls,
        'incorrect': incorrect_urls,
        'no_image': no_image_found,
        'missing_html': missing_html,
        'accuracy': accuracy
    }

if __name__ == "__main__":
    # 只验证德语版本
    json_file = "android-article-urls-de.json"
    
    if os.path.exists(json_file):
        verify_json_image_urls(json_file)
    else:
        print(f"文件不存在: {json_file}")