#!/usr/bin/env python3
"""
更新所有语言的insect文章HTML，添加头图和统一样式
"""

import os
import json
import re
from pathlib import Path

# 基础路径
BASE_DIR = Path("/Users/infno/Documents/work-code/bird-web/website")
INSECT_DIR = BASE_DIR / "insect"
ARTICLE_JSON_PATH = Path("/Users/infno/Documents/work-code/bird-web/article")

# 语言列表
LANGUAGES = ["de", "en", "es", "fr", "it", "ja", "ko", "pt", "ru", "zh"]

# 分类映射到图片前缀
CATEGORY_IMAGE_PREFIX = {
    "basics-identification": "inba",
    "ecology-environment": "inec",
    "beneficial-pollinators": "inbe",
    "pest-management": "inpe",
    "behavior-evolution": "inbe"  # 注意：behavior-evolution 也使用 inbe 前缀（41-50号文章）
}

# Rock文章样式模板
ROCK_STYLE_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} - InsectAiSnap</title>
<link href="../../../mobile-styles.css" rel="stylesheet"/>
<link href="../../../mobile-enhancement.css" rel="stylesheet"/>
<link href="../../../ecology-theme.css" rel="stylesheet"/>
<style>
        .hero-image img {{
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }}
        .article-card img {{
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }}
        .hero-image {{
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('{image_url}') center/cover;
            position: relative;
            margin-top: 0;
        }}
        .article-meta {{
            margin-top: 15px !important;
        }}
    
        /* Insect Theme - {theme_color} */
        :root {{
            --primary-color: {primary_color};
            --primary-dark: {primary_dark};
            --primary-light: {primary_light};
            --accent-color: {accent_color};
        }}
        
        /* Theme Color Overrides */
        .content {{
            background: linear-gradient(135deg, #ffffff, var(--primary-light));
            border: 2px solid var(--primary-color);
        }}
        
        .quote-box {{
            background: linear-gradient(135deg, var(--primary-light), {secondary_light});
            border-left: 4px solid var(--primary-color);
        }}
        
        .quote-text {{
            color: var(--primary-dark);
        }}
        
        .section-title {{
            color: var(--primary-color);
            border-bottom: 2px solid var(--accent-color);
        }}
        
        .tip-box {{
            border-left: 4px solid var(--primary-color);
            background: var(--primary-light);
        }}
        
        .tip-title {{
            color: var(--primary-color);
        }}
        
        .highlight {{
            border-left: 4px solid var(--accent-color);
            background: linear-gradient(135deg, #f1f8e9, var(--primary-light));
        }}
        
        .warning {{
            border-left: 4px solid #f44336;
        }}
        
        .equipment-item {{
            border: 1px solid var(--accent-color);
            background: linear-gradient(135deg, #ffffff, var(--primary-light));
        }}
        
        .equipment-item h4 {{
            color: var(--primary-color);
        }}
        
        .category {{
            background: var(--primary-color);
            color: white;
        }}
    </style>
</head>
<body>
<div class="hero-image"></div>
<div class="content">
{content}
</div>
</body>
</html>
"""

# 分类主题颜色
CATEGORY_THEMES = {
    "basics-identification": {
        "theme_color": "Blue",
        "primary_color": "#2196F3",
        "primary_dark": "#0D47A1",
        "primary_light": "#E3F2FD",
        "accent_color": "#64B5F6",
        "secondary_light": "#BBDEFB"
    },
    "ecology-environment": {
        "theme_color": "Green",
        "primary_color": "#4CAF50",
        "primary_dark": "#1B5E20",
        "primary_light": "#E8F5E9",
        "accent_color": "#81C784",
        "secondary_light": "#C8E6C9"
    },
    "beneficial-pollinators": {
        "theme_color": "Amber",
        "primary_color": "#FFC107",
        "primary_dark": "#FF6F00",
        "primary_light": "#FFF8E1",
        "accent_color": "#FFD54F",
        "secondary_light": "#FFECB3"
    },
    "pest-management": {
        "theme_color": "Red",
        "primary_color": "#F44336",
        "primary_dark": "#B71C1C",
        "primary_light": "#FFEBEE",
        "accent_color": "#E57373",
        "secondary_light": "#FFCDD2"
    },
    "behavior-evolution": {
        "theme_color": "Purple",
        "primary_color": "#9C27B0",
        "primary_dark": "#4A148C",
        "primary_light": "#F3E5F5",
        "accent_color": "#BA68C8",
        "secondary_light": "#E1BEE7"
    }
}


def get_image_mapping(category, article_number):
    """根据分类和文章编号获取对应的图片文件名"""
    prefix = CATEGORY_IMAGE_PREFIX.get(category, "inba")
    
    # 特殊处理 behavior-evolution，它使用 41-50 号文章，但对应的图片是 inbe001-010
    if category == "behavior-evolution":
        # 41-50 -> 001-010
        image_num = article_number - 40
        return f"{prefix}{image_num:03d}.webp"
    
    # 其他分类：1-10, 11-20, 21-30, 31-40 对应 001-010
    image_num = ((article_number - 1) % 10) + 1
    return f"{prefix}{image_num:03d}.webp"


def extract_content_from_html(html_content):
    """从现有HTML中提取内容部分"""
    # 提取 <body> 中的内容
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
    if not body_match:
        return None
    
    body_content = body_match.group(1)
    
    # 移除旧的 hero 部分
    body_content = re.sub(r'<div class="hero">.*?</div>', '', body_content, flags=re.DOTALL)
    
    # 提取 content div 内的内容
    content_match = re.search(r'<div class="content">(.*?)</div>\s*$', body_content, re.DOTALL)
    if content_match:
        return content_match.group(1).strip()
    
    # 如果没有 content div，返回整个 body 内容
    return body_content.strip()


def update_article(file_path, category, article_number, title, lang):
    """更新单个文章文件"""
    if not file_path.exists():
        print(f"  ⚠️  文件不存在: {file_path}")
        return False
    
    try:
        # 读取现有内容
        with open(file_path, 'r', encoding='utf-8') as f:
            old_content = f.read()
        
        # 提取文章内容
        article_content = extract_content_from_html(old_content)
        if not article_content:
            print(f"  ⚠️  无法提取内容: {file_path}")
            return False
        
        # 获取图片文件名
        image_filename = get_image_mapping(category, article_number)
        image_url = f"../../../insect/images/headers/{image_filename}"
        
        # 获取主题颜色
        theme = CATEGORY_THEMES.get(category, CATEGORY_THEMES["basics-identification"])
        
        # 生成新的HTML内容
        new_content = ROCK_STYLE_TEMPLATE.format(
            lang=lang,
            title=title,
            image_url=image_url,
            content=article_content,
            **theme
        )
        
        # 写入新内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ 错误: {e}")
        return False


def process_language(lang):
    """处理单个语言的所有文章"""
    print(f"\n{'='*60}")
    print(f"处理语言: {lang.upper()}")
    print(f"{'='*60}")
    
    # 读取该语言的JSON配置
    json_file = ARTICLE_JSON_PATH / f"insect-article-urls-{lang}.json"
    if not json_file.exists():
        print(f"❌ JSON文件不存在: {json_file}")
        return
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    stats = {"success": 0, "failed": 0, "total": 0}
    
    # 遍历所有分类
    for category_key, category_data in data["articleCategories"].items():
        print(f"\n📁 分类: {category_data['categoryName']}")
        
        # 遍历该分类下的所有文章
        for article in category_data["articles"]:
            article_id = article["id"]
            title = article["title"]
            url = article["url"]
            
            # 提取文章编号
            article_num_match = re.search(r'/(\d+)-', url)
            if not article_num_match:
                print(f"  ⚠️  无法提取文章编号: {url}")
                continue
            
            article_number = int(article_num_match.group(1))
            
            # 构建文件路径
            # URL格式: /basics-identification/01-introduction-to-insects.html
            # 文件路径: insect/en/basics-identification/01-introduction-to-insects.html
            rel_path = url.lstrip('/')
            file_path = INSECT_DIR / lang / rel_path
            
            stats["total"] += 1
            print(f"  📄 {article_number:02d}. {title[:50]}...", end=" ")
            
            if update_article(file_path, category_key, article_number, title, lang):
                stats["success"] += 1
                print("✅")
            else:
                stats["failed"] += 1
                print("❌")
    
    print(f"\n{'='*60}")
    print(f"完成 {lang.upper()}: 成功 {stats['success']}/{stats['total']}, 失败 {stats['failed']}")
    print(f"{'='*60}")


def main():
    """主函数"""
    print("="*60)
    print("开始更新所有语言的 Insect 文章")
    print("="*60)
    
    total_stats = {"success": 0, "failed": 0, "total": 0}
    
    for lang in LANGUAGES:
        process_language(lang)
        # 这里可以添加总计统计
    
    print("\n" + "="*60)
    print("所有语言更新完成！")
    print("="*60)


if __name__ == "__main__":
    main()

