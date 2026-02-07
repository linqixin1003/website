#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译并生成多语言文章
使用AI进行翻译
"""
from pathlib import Path
import json
import re
from bs4 import BeautifulSoup
import time

root = Path('/Users/conalin/website')

# 语言配置
LANG_CONFIG = {
    'de': {'name': 'German', 'code': 'de', 'back_text': '← Zurück', 'tldr_title': '⚡ TL;DR'},
    'es': {'name': 'Spanish', 'code': 'es', 'back_text': '← Volver', 'tldr_title': '⚡ TL;DR'},
    'fr': {'name': 'French', 'code': 'fr', 'back_text': '← Retour', 'tldr_title': '⚡ TL;DR'},
    'it': {'name': 'Italian', 'code': 'it', 'back_text': '← Indietro', 'tldr_title': '⚡ TL;DR'},
    'ja': {'name': 'Japanese', 'code': 'ja', 'back_text': '← 戻る', 'tldr_title': '⚡ TL;DR'},
    'ko': {'name': 'Korean', 'code': 'ko', 'back_text': '← 뒤로', 'tldr_title': '⚡ TL;DR'},
    'pt': {'name': 'Portuguese', 'code': 'pt', 'back_text': '← Voltar', 'tldr_title': '⚡ TL;DR'},
    'ru': {'name': 'Russian', 'code': 'ru', 'back_text': '← Назад', 'tldr_title': '⚡ TL;DR'}
}

# 颜色和主题配置
color_map = {
    "bowel": ("#A78BFA", "#C4B5FD"),
    "urinary": ("#60A5FA", "#93C5FD"),
    "menstrual": ("#F472B6", "#FBCFE8"),
    "hydration": ("#2DD4BF", "#99F6E4"),
    "fitness": ("#FB7185", "#FECDD3"),
    "nutrition": ("#34D399", "#A7F3D0")
}

def translate_with_ai(text, target_lang, source_lang='zh'):
    """
    使用AI翻译文本
    这里需要集成实际的翻译API（OpenAI, DeepL等）
    目前返回占位符，实际使用时需要替换
    """
    # TODO: 集成翻译API
    # 示例：使用OpenAI
    # import openai
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{
    #         "role": "system",
    #         "content": f"Translate the following Chinese text to {LANG_CONFIG[target_lang]['name']}. Preserve HTML tags and formatting."
    #     }, {
    #         "role": "user",
    #         "content": text
    #     }]
    # )
    # return response.choices[0].message.content
    
    # 临时：返回原文（实际使用时需要替换为真实翻译）
    return text

def extract_text_from_html(html_content):
    """从HTML中提取纯文本用于翻译"""
    soup = BeautifulSoup(html_content, 'html.parser')
    # 移除script和style标签
    for tag in soup(['script', 'style']):
        tag.decompose()
    return soup.get_text(separator=' ', strip=True)

def translate_html_content(html_content, target_lang):
    """
    翻译HTML内容，保留HTML标签结构
    策略：提取文本节点，翻译后替换
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 遍历所有文本节点
    for element in soup.find_all(string=True):
        parent = element.parent
        if parent and parent.name in ['script', 'style']:
            continue
        
        text = element.strip()
        if text and len(text) > 0:
            # 翻译文本
            translated = translate_with_ai(text, target_lang)
            element.replace_with(translated)
    
    return str(soup)

def generate_article_html(article_data, lang_code, file_name):
    """生成单篇文章的HTML"""
    theme = article_data['theme']
    lang_config = LANG_CONFIG[lang_code]
    
    # 翻译内容
    print(f"    翻译标题...")
    title = translate_with_ai(article_data['title'], lang_code)
    
    category = article_data['category']  # 保持英文
    read_time = article_data['read_time']  # 保持英文格式
    
    print(f"    翻译介绍...")
    intro = translate_with_ai(article_data['intro'], lang_code)
    
    print(f"    翻译正文...")
    content = translate_html_content(article_data['content'], lang_code)
    
    # 翻译TL;DR
    print(f"    翻译TL;DR...")
    tldr_items = []
    for i, item in enumerate(article_data['tldr']):
        translated_item = translate_html_content(item, lang_code)
        tldr_items.append(translated_item)
    
    tldr_html = ''.join([f'<li>{item}</li>' for item in tldr_items])
    
    # SVG Hero（保持原样，只翻译其中的文本）
    svg_hero = article_data['svg_hero']
    if svg_hero:
        svg_soup = BeautifulSoup(svg_hero, 'html.parser')
        for text_node in svg_soup.find_all(string=True):
            if text_node.strip():
                translated = translate_with_ai(text_node, lang_code)
                text_node.replace_with(translated)
        svg_hero = str(svg_soup)
    
    # 路径配置
    back_text = lang_config['back_text']
    tldr_title = lang_config['tldr_title']
    css_path = '../../article-theme-v2.css'
    back_path = '../../happy-poop-mobile.html'
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_code}" data-theme="{theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title} - Happy Poop</title>
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
    <header class="hero-section">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="article-meta-top">
                <span>{category}</span>
                <span>•</span>
                <span>{read_time}</span>
            </div>
            <h1 class="hero-title">{title}</h1>
            <div class="hero-image">{svg_hero}</div>
        </div>
    </header>
    <div class="summary-card">
        <div class="summary-title">{tldr_title}</div>
        <ul class="summary-list">{tldr_html}</ul>
    </div>
    <article class="content-container">
        <div class="content-block">
            <p class="intro-text">{intro}</p>
            {content}
        </div>
    </article>
    <nav class="floating-nav">
        <a href="{back_path}" class="back-btn">{back_text}</a>
        <a href="#" class="share-btn" onclick="navigator.share({{title: '{title}', url: window.location.href}}); return false;">📤</a>
    </nav>
    <script>
        document.querySelectorAll('.checklist-item').forEach(item => {{
            item.addEventListener('click', () => {{
                item.style.backgroundColor = '#F3F4F6';
                setTimeout(() => item.style.backgroundColor = 'transparent', 200);
            }});
        }});
    </script>
</body>
</html>'''
    
    return html

def main():
    # 读取中文文章数据
    json_file = root / 'zh_articles_content.json'
    with open(json_file, 'r', encoding='utf-8') as f:
        articles_data = json.load(f)
    
    print(f"📚 开始处理 {len(articles_data)} 篇文章...")
    print(f"🌍 目标语言: {', '.join([LANG_CONFIG[lang]['name'] for lang in LANG_CONFIG.keys()])}")
    print(f"\n⚠️  注意：此脚本需要集成翻译API才能实际翻译。")
    print(f"   当前版本会保留中文原文作为占位符。\n")
    
    total_files = len(articles_data) * len(LANG_CONFIG)
    processed = 0
    
    # 处理每种语言
    for lang_code, lang_info in LANG_CONFIG.items():
        print(f"\n{'='*60}")
        print(f"🌍 处理语言: {lang_info['name']} ({lang_code})")
        print(f"{'='*60}")
        
        lang_dir = root / lang_code / 'still-alive-tips'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        for article_id in sorted(articles_data.keys()):
            article_data = articles_data[article_id]
            
            # 确定文件名
            zh_files = list((root / 'zh' / 'still-alive-tips').glob(f'{article_id}-*.html'))
            if not zh_files:
                continue
            
            zh_file_name = zh_files[0].name
            target_file = lang_dir / zh_file_name
            
            print(f"\n  📄 [{article_id}] {article_data['title'][:40]}...")
            
            try:
                # 生成HTML
                html_content = generate_article_html(article_data, lang_code, zh_file_name)
                
                # 保存文件
                target_file.write_text(html_content, encoding='utf-8')
                processed += 1
                print(f"     ✅ 已生成: {target_file.name}")
                
                # 避免API限流
                time.sleep(0.1)
                
            except Exception as e:
                print(f"     ❌ 错误: {str(e)}")
                continue
    
    print(f"\n{'='*60}")
    print(f"✨ 完成！已生成 {processed}/{total_files} 个文件。")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
