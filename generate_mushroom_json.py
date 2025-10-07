#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成蘑菇文章的JSON文件（用于客户端加载）
为所有10种语言生成独立的JSON文件
"""

import json
from pathlib import Path
from datetime import datetime

# 基础配置
BASE_DIR = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom")
OUTPUT_DIR = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom-articles-json")

# 所有支持的语言
LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇺🇸'},
    'ja': {'name': 'Japanese', 'flag': '🇯🇵'},
    'zh': {'name': 'Chinese', 'flag': '🇨🇳'},
    'de': {'name': 'German', 'flag': '🇩🇪'},
    'es': {'name': 'Spanish', 'flag': '🇪🇸'},
    'fr': {'name': 'French', 'flag': '🇫🇷'},
    'it': {'name': 'Italian', 'flag': '🇮🇹'},
    'ko': {'name': 'Korean', 'flag': '🇰🇷'},
    'pt': {'name': 'Portuguese', 'flag': '🇧🇷'},
    'ru': {'name': 'Russian', 'flag': '🇷🇺'}
}

# 分类配置
CATEGORIES = {
    'culinary-mushrooms': {
        'name': {'en': 'Culinary Mushrooms', 'ja': '料理用キノコ', 'zh': '烹饪蘑菇', 'de': 'Speisepilze', 
                 'es': 'Hongos Culinarios', 'fr': 'Champignons Culinaires', 'it': 'Funghi Culinari', 
                 'ko': '요리용 버섯', 'pt': 'Cogumelos Culinários', 'ru': 'Кулинарные грибы'},
        'icon': '🍳',
        'count': 11
    },
    'mushroom-ecology': {
        'name': {'en': 'Mushroom Ecology', 'ja': 'キノコ生態学', 'zh': '菌类生态学', 'de': 'Pilzökologie', 
                 'es': 'Ecología de Hongos', 'fr': 'Écologie des Champignons', 'it': 'Ecologia dei Funghi', 
                 'ko': '버섯 생태학', 'pt': 'Ecologia de Cogumelos', 'ru': 'Экология грибов'},
        'icon': '🌲',
        'count': 11
    },
    'mushroom-identification': {
        'name': {'en': 'Mushroom Identification', 'ja': 'キノコ識別', 'zh': '菌类鉴定', 'de': 'Pilzbestimmung', 
                 'es': 'Identificación de Hongos', 'fr': 'Identification des Champignons', 'it': 'Identificazione dei Funghi', 
                 'ko': '버섯 식별', 'pt': 'Identificação de Cogumelos', 'ru': 'Определение грибов'},
        'icon': '🔍',
        'count': 11
    },
    'mushroom-safety': {
        'name': {'en': 'Mushroom Safety', 'ja': 'キノコ安全性', 'zh': '蘑菇安全', 'de': 'Pilzsicherheit', 
                 'es': 'Seguridad de Hongos', 'fr': 'Sécurité des Champignons', 'it': 'Sicurezza dei Funghi', 
                 'ko': '버섯 안전', 'pt': 'Segurança de Cogumelos', 'ru': 'Безопасность грибов'},
        'icon': '⚠️',
        'count': 11
    },
    'mushroom-science': {
        'name': {'en': 'Mushroom Science', 'ja': 'キノコ科学', 'zh': '菌类科学', 'de': 'Pilzwissenschaft', 
                 'es': 'Ciencia de Hongos', 'fr': 'Science des Champignons', 'it': 'Scienza dei Funghi', 
                 'ko': '버섯 과학', 'pt': 'Ciência de Cogumelos', 'ru': 'Наука о грибах'},
        'icon': '🔬',
        'count': 11
    }
}

def read_article_title(file_path):
    """读取文章标题，跳过frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # 检查是否有frontmatter (以---开始)
            in_frontmatter = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # 检测frontmatter开始
                if i == 0 and stripped == '---':
                    in_frontmatter = True
                    continue
                
                # 检测frontmatter结束
                if in_frontmatter and stripped == '---':
                    in_frontmatter = False
                    continue
                
                # 跳过frontmatter内容
                if in_frontmatter:
                    continue
                
                # 找到第一个有效的标题行（#开头）
                if stripped.startswith('#'):
                    title = stripped.lstrip('#').strip()
                    if title and len(title) > 3:  # 确保不是空标题或太短的标题
                        return title
            
            # 如果没找到，返回文件名
            return file_path.stem.replace('-', ' ').title()
            
    except Exception as e:
        print(f"❌ 读取标题失败 {file_path}: {e}")
        return None

def simplify_title(full_title):
    """精简标题，参考rock的长度（平均27字符左右）"""
    
    # 如果标题包含冒号，智能选择冒号前或后的部分
    if ':' in full_title:
        parts = [p.strip() for p in full_title.split(':')]
        
        # 移除常见的冗余前缀/后缀
        def clean_part(text):
            # 移除修饰性前缀
            prefixes = [
                'The Complete Professional Guide to ',
                'The Complete Guide to ',
                'Complete Guide to ',
                'A Comprehensive Guide to ',
                'The Complete ', 'Complete ', 'A Complete ',
                'The ', 'A ', 'An ', 'Essential ',
                'Professional ', 'Comprehensive '
            ]
            for prefix in prefixes:
                if text.startswith(prefix):
                    text = text[len(prefix):]
            
            # 移除修饰性后缀
            suffixes = [
                ': From Basics to Mastery',
                ': From Basic to Advanced',
                ': From Fundamental Principles to Master-Level Techniques',
                ': From Forest to Table',
                ': A Cross-Cultural Culinary Guide from Foraging to Table',
                ' from Forest to Table',
                ' from Foraging to Table',
                ' from Field Collection to Table Safety',
                ' from Basics to Mastery',
                ' and Practical Analysis'
            ]
            for suffix in suffixes:
                if text.endswith(suffix):
                    text = text[:-len(suffix)]
            
            return text.strip()
        
        # 清理所有部分
        cleaned_parts = [clean_part(p) for p in parts]
        
        # 过滤掉无效部分（太短、只有符号、空白等）
        valid_parts = []
        for p in cleaned_parts:
            # 去除只有符号或空白的部分
            if len(p) >= 10 and any(c.isalnum() for c in p):
                valid_parts.append(p)
        
        if valid_parts:
            # 选择最短的有效部分
            result = min(valid_parts, key=len)
        elif cleaned_parts:
            # 如果都太短，返回第一个非空部分
            non_empty = [p for p in cleaned_parts if p and any(c.isalnum() for c in p)]
            result = non_empty[0] if non_empty else full_title
        else:
            result = full_title
    else:
        # 如果没有冒号，直接清理
        result = full_title
        
        # 移除前缀
        prefixes = [
            'The Complete Professional Guide to ',
            'The Complete Guide to ',
            'Complete Guide to ',
            'A Comprehensive Guide to ',
            'The Complete ', 'Complete ', 'A Complete ',
            'The ', 'A ', 'An ', 'Essential ',
            'Professional ', 'Comprehensive '
        ]
        for prefix in prefixes:
            if result.startswith(prefix):
                result = result[len(prefix):]
                break
        
        # 移除后缀
        suffixes = [
            ': From Basics to Mastery',
            ': From Basic to Advanced',
            ' from Forest to Table',
            ' and Practical Analysis'
        ]
        for suffix in suffixes:
            if result.endswith(suffix):
                result = result[:-len(suffix)]
                break
    
    # 确保首字母大写
    result = result.strip()
    if result and result[0].islower():
        result = result[0].upper() + result[1:]
    
    return result

def read_article_excerpt(file_path):
    """读取文章摘要（第一段非标题内容）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:  # 跳过标题
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('**'):
                    # 截取前150个字符
                    excerpt = line[:150]
                    if len(line) > 150:
                        excerpt += "..."
                    return excerpt
        return "Learn more about this topic..."
    except Exception as e:
        print(f"❌ 读取摘要失败 {file_path}: {e}")
        return "Read this comprehensive article..."

def estimate_read_time(file_path):
    """估算阅读时间（基于字数）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            word_count = len(content.split())
            # 假设每分钟阅读200个单词
            minutes = max(5, round(word_count / 200))
            return f"{minutes} minutes"
    except:
        return "15 minutes"

def determine_difficulty(article_num):
    """根据文章编号确定难度"""
    num = int(article_num)
    if num <= 3:
        return "beginner"
    elif num <= 8:
        return "intermediate"
    else:
        return "advanced"

def generate_json_for_language(lang_code):
    """为指定语言生成JSON"""
    lang_dir = BASE_DIR / lang_code
    
    if not lang_dir.exists():
        print(f"⚠️ 语言目录不存在: {lang_code}")
        return None
    
    # 构建JSON结构
    json_data = {
        "articleCategories": {},
        "languageSupport": {
            "currentLanguage": {
                "code": lang_code,
                "name": LANGUAGES[lang_code]['name'],
                "nameEn": LANGUAGES[lang_code]['name'],
                "flag": LANGUAGES[lang_code]['flag']
            }
        },
        "apiEndpoints": {
            "baseUrl": f"https://birdid.net/{lang_code}",
            "articleEndpoint": f"/{lang_code}/{{category}}/{{articleId}}.html",
            "imageEndpoint": "/mushroom/images/{category}_{articleId}.webp"
        },
        "metadata": {
            "totalArticles": 55,
            "totalCategories": 5,
            "language": lang_code,
            "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0.0"
        }
    }
    
    # 处理每个分类
    for category, cat_info in CATEGORIES.items():
        category_dir = lang_dir / category
        
        if not category_dir.exists():
            print(f"  ⚠️ 分类目录不存在: {category}")
            continue
        
        # 初始化分类
        json_data["articleCategories"][category] = {
            "categoryName": cat_info['name'].get(lang_code, cat_info['name']['en']),
            "categoryNameEn": cat_info['name']['en'],
            "categoryIcon": cat_info['icon'],
            "baseUrl": f"https://birdid.net/{lang_code}",
            "articles": []
        }
        
        # 获取该分类下所有文本文件
        txt_files = sorted(category_dir.glob("*.txt"))
        
        for txt_file in txt_files:
            try:
                # 提取文章编号和文件名
                article_num = txt_file.stem.split('-')[0]
                filename_without_num = '-'.join(txt_file.stem.split('-')[1:])
                
                # 读取文章信息
                full_title = read_article_title(txt_file)
                if not full_title:
                    continue
                
                # 精简标题
                title = simplify_title(full_title)
                
                excerpt = read_article_excerpt(txt_file)
                read_time = estimate_read_time(txt_file)
                difficulty = determine_difficulty(article_num)
                
                # 构建文章对象
                article = {
                    "id": f"{category[:3]}{article_num}",
                    "title": title,
                    "titleEn": title,
                    "url": f"/{category}/{txt_file.stem}.html",
                    "description": excerpt,
                    "difficulty": difficulty,
                    "readTime": read_time,
                    "imageUrl": f"https://birdid.net/mushroom/images/{category}_{txt_file.stem}.webp"
                }
                
                json_data["articleCategories"][category]["articles"].append(article)
                
            except Exception as e:
                print(f"  ❌ 处理文章失败 {txt_file.name}: {e}")
    
    return json_data

def main():
    # 创建输出目录
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("🍄 开始生成蘑菇文章JSON文件...")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print(f"🌍 语言数量: {len(LANGUAGES)}")
    print("=" * 80)
    
    total_success = 0
    
    # 为每种语言生成JSON
    for lang_code in LANGUAGES.keys():
        print(f"\n🌍 处理语言: {lang_code.upper()} ({LANGUAGES[lang_code]['name']})")
        
        json_data = generate_json_for_language(lang_code)
        
        if json_data:
            # 保存JSON文件
            output_file = OUTPUT_DIR / f"mushroom-article-urls-{lang_code}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            
            total_articles = sum(
                len(cat['articles']) 
                for cat in json_data['articleCategories'].values()
            )
            
            print(f"  ✅ 已生成: {output_file.name}")
            print(f"  📊 文章数: {total_articles}")
            total_success += 1
        else:
            print(f"  ❌ 生成失败")
    
    # 生成通用的JSON文件（英文版作为默认）
    print(f"\n🌍 生成默认JSON文件...")
    en_json = generate_json_for_language('en')
    if en_json:
        output_file = OUTPUT_DIR / "mushroom-article-urls.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(en_json, f, ensure_ascii=False, indent=2)
        print(f"  ✅ 已生成: {output_file.name}")
        total_success += 1
    
    print("\n" + "=" * 80)
    print("🎉 处理完成！")
    print(f"✅ 成功生成: {total_success} 个JSON文件")
    print(f"📁 保存位置: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
