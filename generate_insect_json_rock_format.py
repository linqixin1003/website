#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成与rock格式相同的insect JSON配置文件"""

import re
import sys
import json
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 语言配置
LANGUAGES = {
    'en': {'name': 'English', 'baseUrl': 'https://birdid.net/en'},
    'zh': {'name': '中文', 'baseUrl': 'https://birdid.net/zh'},
    'de': {'name': 'Deutsch', 'baseUrl': 'https://birdid.net/de'},
    'es': {'name': 'Español', 'baseUrl': 'https://birdid.net/es'},
    'fr': {'name': 'Français', 'baseUrl': 'https://birdid.net/fr'},
    'it': {'name': 'Italiano', 'baseUrl': 'https://birdid.net/it'},
    'ja': {'name': '日本語', 'baseUrl': 'https://birdid.net/ja'},
    'ko': {'name': '한국어', 'baseUrl': 'https://birdid.net/ko'},
    'pt': {'name': 'Português', 'baseUrl': 'https://birdid.net/pt'},
    'ru': {'name': 'Русский', 'baseUrl': 'https://birdid.net/ru'}
}

# 分类配置
CATEGORIES = {
    'basics-identification': {
        'en': 'Basics & Identification',
        'zh': '基础与识别',
        'de': 'Grundlagen & Identifikation',
        'es': 'Conceptos Básicos e Identificación',
        'fr': 'Bases et Identification',
        'it': 'Basi e Identificazione',
        'ja': '基礎と識別',
        'ko': '기초 및 식별',
        'pt': 'Fundamentos e Identificação',
        'ru': 'Основы и идентификация',
        'icon': '🔍'
    },
    'ecology-environment': {
        'en': 'Ecology & Environment',
        'zh': '生态与环境',
        'de': 'Ökologie & Umwelt',
        'es': 'Ecología y Medio Ambiente',
        'fr': 'Écologie et Environnement',
        'it': 'Ecologia e Ambiente',
        'ja': '生態学と環境',
        'ko': '생태학 및 환경',
        'pt': 'Ecologia e Meio Ambiente',
        'ru': 'Экология и окружающая среда',
        'icon': '🌿'
    },
    'beneficial-pollinators': {
        'en': 'Beneficial Insects & Pollinators',
        'zh': '有益昆虫与授粉者',
        'de': 'Nützliche Insekten & Bestäuber',
        'es': 'Insectos Beneficiosos y Polinizadores',
        'fr': 'Insectes Utiles et Pollinisateurs',
        'it': 'Insetti Benefici e Impollinatori',
        'ja': '有益な昆虫と花粉媒介者',
        'ko': '유익한 곤충 및 수분 매개자',
        'pt': 'Insetos Benéficos e Polinizadores',
        'ru': 'Полезные насекомые и опылители',
        'icon': '🐝'
    },
    'pest-management': {
        'en': 'Pest Management',
        'zh': '害虫管理',
        'de': 'Schädlingsbekämpfung',
        'es': 'Manejo de Plagas',
        'fr': 'Gestion des Ravageurs',
        'it': 'Gestione dei Parassiti',
        'ja': '害虫管理',
        'ko': '해충 관리',
        'pt': 'Gestão de Pragas',
        'ru': 'Управление вредителями',
        'icon': '🛡️'
    },
    'behavior-evolution': {
        'en': 'Behavior & Evolution',
        'zh': '行为与进化',
        'de': 'Verhalten & Evolution',
        'es': 'Comportamiento y Evolución',
        'fr': 'Comportement et Évolution',
        'it': 'Comportamento ed Evoluzione',
        'ja': '行動と進化',
        'ko': '행동 및 진화',
        'pt': 'Comportamento e Evolução',
        'ru': 'Поведение и эволюция',
        'icon': '🦋'
    }
}

def extract_article_info(file_path, lang_code):
    """从HTML文件中提取文章信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 提取标题
        title_match = re.search(r'<title>(.*?)</title>', html)
        title = title_match.group(1) if title_match else ''
        
        # 提取hero标题（可能更准确）
        hero_match = re.search(r'<h1 class="hero-title">(.*?)</h1>', html)
        if hero_match:
            title = hero_match.group(1)
        
        # 提取副标题作为描述
        subtitle_match = re.search(r'<p class="hero-subtitle">(.*?)</p>', html)
        description = subtitle_match.group(1) if subtitle_match else ''
        
        # 如果没有副标题，提取第一个intro段落
        if not description:
            intro_match = re.search(r'<p class="intro">(.*?)</p>', html, re.DOTALL)
            if intro_match:
                description = re.sub(r'<[^>]+>', '', intro_match.group(1))
                description = description.strip()[:150]  # 限制长度
        
        return {
            'title': title.strip(),
            'description': description.strip()
        }
        
    except Exception as e:
        print(f"  ⚠️  提取失败 {file_path.name}: {e}")
        return None

def generate_json_for_language(lang_code):
    """为指定语言生成JSON配置"""
    print(f"\n🌐 生成 {LANGUAGES[lang_code]['name']} ({lang_code}) JSON...")
    
    lang_dir = Path(f"insect/{lang_code}")
    if not lang_dir.exists():
        print(f"  ⚠️  目录不存在: {lang_dir}")
        return None
    
    json_data = {
        "articleCategories": {}
    }
    
    # 遍历每个分类
    for category_dir, category_info in CATEGORIES.items():
        category_path = lang_dir / category_dir
        
        if not category_path.exists():
            print(f"  ⚠️  分类不存在: {category_dir}")
            continue
        
        # 获取该分类的所有文章
        article_files = sorted(category_path.glob("*.html"))
        articles = []
        
        for idx, article_file in enumerate(article_files, 1):
            # 提取文章信息
            info = extract_article_info(article_file, lang_code)
            
            if not info:
                continue
            
            # 生成ID
            article_id = f"in{category_dir[:2]}{idx:03d}"
            
            # 构造URL
            url = f"/insect/{category_dir}/{article_file.name}"
            
            # 确定难度
            difficulty = "beginner"
            if idx > 20:
                difficulty = "intermediate"
            if idx > 40:
                difficulty = "advanced"
            
            # 估算阅读时间（基于文件大小）
            file_size_kb = article_file.stat().st_size / 1024
            read_time_min = max(5, min(25, int(file_size_kb / 2)))
            read_time = f"{read_time_min} minutes" if lang_code == 'en' else f"{read_time_min}分钟"
            
            # 生成图片URL（使用统一的昆虫图标）
            image_url = f"https://birdid.net/images/insect_{article_file.stem}.webp"
            
            # 获取英文标题（从英文文件中提取）
            title_en = info['title']
            if lang_code != 'en':
                en_file = Path(f"insect/en/{category_dir}/{article_file.name}")
                if en_file.exists():
                    en_info = extract_article_info(en_file, 'en')
                    if en_info:
                        title_en = en_info['title']
            
            article_data = {
                "id": article_id,
                "title": info['title'],
                "titleEn": title_en,
                "url": url,
                "description": info['description'],
                "difficulty": difficulty,
                "readTime": read_time,
                "imageUrl": image_url
            }
            
            articles.append(article_data)
        
        # 添加分类数据
        json_data["articleCategories"][category_dir] = {
            "categoryName": category_info[lang_code],
            "categoryNameEn": category_info['en'],
            "categoryIcon": category_info['icon'],
            "baseUrl": LANGUAGES[lang_code]['baseUrl'],
            "articles": articles
        }
        
        print(f"  ✅ {category_info[lang_code]}: {len(articles)} 篇文章")
    
    return json_data

def main():
    print("=" * 80)
    print("🐛 生成Insect JSON配置文件 - Rock格式")
    print("=" * 80)
    
    # 创建输出目录
    output_dir = Path("insect-articles-json")
    output_dir.mkdir(exist_ok=True)
    
    # 为每种语言生成JSON
    for lang_code in LANGUAGES.keys():
        json_data = generate_json_for_language(lang_code)
        
        if json_data:
            # 保存到文件
            if lang_code == 'en':
                output_file = output_dir / "insect-article-urls.json"
            else:
                output_file = output_dir / f"insect-article-urls-{lang_code}.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            
            print(f"  💾 已保存: {output_file}")
    
    print()
    print("=" * 80)
    print("✅ 所有JSON文件生成完成！")
    print("=" * 80)
    
    # 统计
    json_files = list(output_dir.glob("*.json"))
    print(f"\n📊 生成统计:")
    print(f"  • JSON文件数: {len(json_files)}")
    print(f"  • 语言数: {len(LANGUAGES)}")
    print(f"  • 分类数: {len(CATEGORIES)}")
    print(f"  • 预计文章总数: ~{50 * len(LANGUAGES)} 篇")

if __name__ == '__main__':
    main()

