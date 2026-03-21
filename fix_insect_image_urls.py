#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复昆虫文章JSON文件中的图片URL
从HTML文件中提取实际使用的图片路径
"""

import json
import re
from pathlib import Path

# 基础路径
BASE_DIR = Path(__file__).parent
INSECT_DIR = BASE_DIR / "insect"
JSON_DIR = BASE_DIR / "insect-articles-json"

def extract_main_image_from_html(html_file):
    """从HTML文件中提取主图片路径"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找第一个insect-image类的图片（在insect-illustration div中）
        # 先查找insect-illustration div
        illustration_pattern = r'<div[^>]*class="[^"]*insect-illustration[^"]*"[^>]*>.*?<img[^>]*src="([^"]+)"[^>]*class="[^"]*insect-image'
        match = re.search(illustration_pattern, content, re.DOTALL)
        
        if not match:
            # 如果没找到，尝试直接查找insect-image类
            pattern = r'<img[^>]*class="[^"]*insect-image[^"]*"[^>]*src="([^"]+)"'
            match = re.search(pattern, content)
        
        if match:
            img_path = match.group(1)
            # 如果是相对路径，转换为绝对URL
            if img_path.startswith('../../images/'):
                img_filename = img_path.replace('../../images/', '')
                # 转换为绝对URL - 注意：图片在insect/images目录下
                return f"https://birdid.net/images/insect/{img_filename}"
            elif img_path.startswith('../images/'):
                img_filename = img_path.replace('../images/', '')
                return f"https://birdid.net/images/insect/{img_filename}"
            elif '/images/' in img_path:
                # 提取文件名
                img_filename = img_path.split('/images/')[-1]
                return f"https://birdid.net/images/insect/{img_filename}"
        
        return None
    except Exception as e:
        print(f"  ⚠️ 读取 {html_file.name} 失败: {e}")
        return None

def get_article_html_path(url, lang_code='en'):
    """根据URL获取HTML文件路径"""
    # URL格式: /insect/basics-identification/01-introduction-to-insects.html
    if url.startswith('/insect/'):
        path_part = url.replace('/insect/', '')
        # path_part 格式: basics-identification/01-introduction-to-insects.html
        html_file = INSECT_DIR / lang_code / path_part
        if html_file.exists():
            return html_file
        else:
            # 调试：打印路径
            print(f"    🔍 查找路径: {html_file}")
    return None

def fix_json_file(json_file):
    """修复单个JSON文件中的图片URL"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fixed_count = 0
        not_found_count = 0
        
        # 确定语言代码
        lang_code = 'en'
        if '-zh.json' in json_file.name:
            lang_code = 'zh'
        elif '-de.json' in json_file.name:
            lang_code = 'de'
        elif '-es.json' in json_file.name:
            lang_code = 'es'
        elif '-fr.json' in json_file.name:
            lang_code = 'fr'
        elif '-it.json' in json_file.name:
            lang_code = 'it'
        elif '-ja.json' in json_file.name:
            lang_code = 'ja'
        elif '-ko.json' in json_file.name:
            lang_code = 'ko'
        elif '-pt.json' in json_file.name:
            lang_code = 'pt'
        elif '-ru.json' in json_file.name:
            lang_code = 'ru'
        
        # 遍历所有分类和文章
        for category_key, category_data in data.get('articleCategories', {}).items():
            articles = category_data.get('articles', [])
            
            for article in articles:
                url = article.get('url', '')
                current_image_url = article.get('imageUrl', '')
                
                # 获取HTML文件路径
                html_file = get_article_html_path(url, lang_code)
                
                if html_file and html_file.exists():
                    # 提取实际图片路径
                    actual_image_url = extract_main_image_from_html(html_file)
                    
                    if actual_image_url:
                        # 更新图片URL
                        if current_image_url != actual_image_url:
                            article['imageUrl'] = actual_image_url
                            fixed_count += 1
                            print(f"  ✅ {article.get('id', 'unknown')}: {current_image_url} -> {actual_image_url}")
                    else:
                        not_found_count += 1
                        print(f"  ⚠️ {article.get('id', 'unknown')}: 未找到图片")
                else:
                    not_found_count += 1
                    print(f"  ⚠️ {article.get('id', 'unknown')}: HTML文件不存在 {url}")
        
        # 保存修复后的JSON
        if fixed_count > 0:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  💾 已保存 {json_file.name}: 修复了 {fixed_count} 个图片URL")
        
        return fixed_count, not_found_count
        
    except Exception as e:
        print(f"  ❌ 处理 {json_file.name} 失败: {e}")
        return 0, 0

def main():
    print("🔧 开始修复昆虫文章JSON文件中的图片URL...\n")
    
    json_files = list(JSON_DIR.glob("insect-article-urls*.json"))
    
    if not json_files:
        print("❌ 未找到JSON文件")
        return
    
    total_fixed = 0
    total_not_found = 0
    
    for json_file in sorted(json_files):
        print(f"\n📄 处理 {json_file.name}...")
        fixed, not_found = fix_json_file(json_file)
        total_fixed += fixed
        total_not_found += not_found
    
    print(f"\n✅ 修复完成！")
    print(f"  - 修复了 {total_fixed} 个图片URL")
    print(f"  - 未找到 {total_not_found} 个图片")

if __name__ == "__main__":
    main()

