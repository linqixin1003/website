#!/usr/bin/env python3
"""
为每篇蘑菇文章生成对应的HTML页面
HTML文件将与原txt文件放在同一目录
"""

import os
from pathlib import Path
import re

def read_article_content(txt_path):
    """读取文章内容"""
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

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

def parse_article(content):
    """解析文章内容，提取标题、章节等"""
    lines = content.split('\n')
    
    # 提取主标题（第一行），跳过frontmatter
    title = "Mushroom Article"
    title_line_idx = 0
    
    # 检查是否有frontmatter
    if lines and lines[0].strip() == '---':
        in_frontmatter = True
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                in_frontmatter = False
                title_line_idx = i + 1
                break
    
    # 找到第一个有效标题
    for i in range(title_line_idx, len(lines)):
        line = lines[i].strip()
        if line.startswith('#'):
            full_title = line.lstrip('#').strip()
            if full_title and len(full_title) > 3:
                title = simplify_title(full_title)
                break
    
    # 将markdown格式转换为HTML
    html_content = []
    in_list = False
    
    for line in lines[1:]:  # 跳过第一行标题
        line = line.rstrip()
        
        # 标题处理
        if line.startswith('## '):
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith('### '):
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith('#### '):
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append(f'<h4>{line[5:].strip()}</h4>')
        # 列表项
        elif line.startswith('- '):
            if not in_list:
                html_content.append('<ul>')
                in_list = True
            html_content.append(f'<li>{line[2:].strip()}</li>')
        # 空行
        elif not line.strip():
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append('<br>')
        # 普通段落
        else:
            if in_list:
                html_content.append('</ul>')
                in_list = False
            # 处理加粗文本
            processed_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            html_content.append(f'<p>{processed_line}</p>')
    
    if in_list:
        html_content.append('</ul>')
    
    return title, '\n'.join(html_content)

def get_category_info(category):
    """获取类别信息"""
    category_info = {
        'culinary-mushrooms': {
            'name': 'Culinary Mushrooms',
            'icon': '🍳',
            'color': '#FF6B6B'
        },
        'mushroom-ecology': {
            'name': 'Mushroom Ecology',
            'icon': '🌲',
            'color': '#4ECDC4'
        },
        'mushroom-identification': {
            'name': 'Mushroom Identification',
            'icon': '🔍',
            'color': '#45B7D1'
        },
        'mushroom-safety': {
            'name': 'Mushroom Safety',
            'icon': '⚠️',
            'color': '#FFA07A'
        },
        'mushroom-science': {
            'name': 'Mushroom Science',
            'icon': '🔬',
            'color': '#98D8C8'
        }
    }
    return category_info.get(category, {'name': category, 'icon': '🍄', 'color': '#8B4513'})

def generate_html(title, content, category, article_num, image_path):
    """生成HTML页面"""
    cat_info = get_category_info(category)
    
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {cat_info['name']}</title>
    <meta name="description" content="{title}">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.8;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}

        .article-title {{
            color: {cat_info['color']};
            font-size: 2.5em;
            margin-bottom: 30px;
            margin-top: 0;
            line-height: 1.3;
            padding-top: 0;
        }}

        .featured-image {{
            width: 100%;
            height: auto;
            aspect-ratio: 4 / 3;
            object-fit: cover;
            display: block;
        }}

        .content {{
            padding: 50px;
        }}

        .content h2 {{
            color: {cat_info['color']};
            font-size: 2em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid {cat_info['color']};
        }}

        .content h3 {{
            color: #555;
            font-size: 1.6em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}

        .content h4 {{
            color: #666;
            font-size: 1.3em;
            margin-top: 25px;
            margin-bottom: 12px;
        }}

        .content p {{
            margin-bottom: 20px;
            font-size: 1.1em;
            color: #444;
        }}

        .content ul {{
            margin: 20px 0;
            padding-left: 30px;
        }}

        .content li {{
            margin-bottom: 12px;
            font-size: 1.05em;
            color: #555;
        }}

        .content strong {{
            color: #222;
            font-weight: 600;
        }}

        .back-link {{
            display: inline-block;
            padding: 12px 25px;
            background: linear-gradient(135deg, {cat_info['color']}, #8B4513);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
            font-weight: 600;
        }}

        .back-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}

        .navigation {{
            padding: 30px 50px;
            background: #f8f9fa;
            border-top: 1px solid #e9ecef;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .nav-btn {{
            padding: 10px 20px;
            background: {cat_info['color']};
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }}

        .nav-btn:hover {{
            transform: translateX(5px);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
        }}

        .nav-btn.prev:hover {{
            transform: translateX(-5px);
        }}

        @media (max-width: 768px) {{
            .content {{
                padding: 30px 25px;
            }}

            .article-title {{
                font-size: 1.8em;
            }}

            .featured-image {{
                height: 250px;
            }}

            .navigation {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="{image_path}" alt="{title}" class="featured-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22900%22 height=%22400%22%3E%3Crect fill=%22%23D2691E%22 width=%22900%22 height=%22400%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 fill=%22white%22 font-size=%2260%22%3E🍄%3C/text%3E%3C/svg%3E'">

        <div class="content">
            <h1 class="article-title">{title}</h1>
            {content}
        </div>
    </div>
</body>
</html>"""
    
    return html_template

def main():
    base_dir = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom")
    
    # 所有支持的语言
    languages = ['en', 'ja', 'zh', 'de', 'es', 'fr', 'it', 'ko', 'pt', 'ru']
    
    categories = [
        'culinary-mushrooms',
        'mushroom-ecology',
        'mushroom-identification',
        'mushroom-safety',
        'mushroom-science'
    ]
    
    total_files = 0
    success_count = 0
    total_expected = len(languages) * 55
    
    print("🍄 开始生成蘑菇文章HTML页面（所有语言）...")
    print(f"📁 基础目录: {base_dir}")
    print(f"🌍 语言: {', '.join(languages)}")
    print(f"📊 预计文章数: {len(languages)} × 55 = {total_expected}")
    print("=" * 80)
    
    for lang in languages:
        lang_dir = base_dir / lang
        
        if not lang_dir.exists():
            print(f"\n⚠️ 语言目录不存在，跳过: {lang_dir}")
            continue
        
        print(f"\n🌍 处理语言: {lang.upper()}")
        print("=" * 80)
        
        for category in categories:
            category_dir = lang_dir / category
            
            if not category_dir.exists():
                print(f"  ⚠️ 目录不存在: {category}")
                continue
            
            print(f"  📂 {category}")
            
            # 获取该类别下所有 .txt 文件
            txt_files = sorted(category_dir.glob("*.txt"))
            
            for txt_file in txt_files:
                total_files += 1
                
                try:
                    # 读取文章内容
                    content = read_article_content(txt_file)
                    
                    # 解析文章
                    title, html_content = parse_article(content)
                    
                    # 获取文章编号
                    article_num = txt_file.stem.split('-')[0]
                    
                    # 确定图片路径（相对于HTML文件的路径）
                    image_filename = f"{category}_{txt_file.stem}.webp"
                    image_path = f"../../images/{image_filename}"
                    
                    # 生成HTML
                    html = generate_html(title, html_content, category, article_num, image_path)
                    
                    # 保存HTML文件
                    html_file = txt_file.with_suffix('.html')
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(html)
                    
                    print(f"    ✅ [{total_files}/{total_expected}] {txt_file.name}")
                    success_count += 1
                    
                except Exception as e:
                    print(f"    ❌ [{total_files}/{total_expected}] 失败: {txt_file.name} - {e}")
    
    print("\n" + "=" * 80)
    print("🎉 全部处理完成！")
    print(f"✅ 成功: {success_count}/{total_files}")
    print(f"❌ 失败: {total_files - success_count}/{total_files}")
    print(f"📊 完成率: {success_count/total_files*100:.1f}%")

if __name__ == "__main__":
    main()
