#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译所有文章 - 使用AI翻译
处理30篇文章 × 8种语言 = 240个文件
"""
import json
from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path('/Users/conalin/website')

# 语言配置
LANG_CONFIG = {
    'de': {'name': 'German', 'back_text': '← Zurück', 'tldr_title': '⚡ TL;DR'},
    'es': {'name': 'Spanish', 'back_text': '← Volver', 'tldr_title': '⚡ TL;DR'},
    'fr': {'name': 'French', 'back_text': '← Retour', 'tldr_title': '⚡ TL;DR'},
    'it': {'name': 'Italian', 'back_text': '← Indietro', 'tldr_title': '⚡ TL;DR'},
    'ja': {'name': 'Japanese', 'back_text': '← 戻る', 'tldr_title': '⚡ TL;DR'},
    'ko': {'name': 'Korean', 'back_text': '← 뒤로', 'tldr_title': '⚡ TL;DR'},
    'pt': {'name': 'Portuguese', 'back_text': '← Voltar', 'tldr_title': '⚡ TL;DR'},
    'ru': {'name': 'Russian', 'back_text': '← Назад', 'tldr_title': '⚡ TL;DR'}
}

def translate_text_ai(text, target_lang, source_lang='zh'):
    """
    使用AI翻译文本
    这里需要调用实际的AI翻译API
    返回翻译后的文本
    """
    # 实际使用时需要集成翻译API
    # 例如：OpenAI, DeepL, Google Translate等
    return text  # 占位符

def translate_html_preserving_structure(html_content, target_lang):
    """
    翻译HTML内容，保留HTML标签和结构
    """
    # 提取文本节点并翻译
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 遍历所有文本节点
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if parent and parent.name in ['script', 'style']:
            continue
        
        text = text_node.strip()
        if text:
            translated = translate_text_ai(text, target_lang)
            text_node.replace_with(translated)
    
    return str(soup)

def generate_article_html(article_data, lang_code, file_name):
    """生成单篇文章的HTML"""
    theme = article_data['theme']
    lang_config = LANG_CONFIG[lang_code]
    
    # 翻译各个部分
    title = translate_text_ai(article_data['title'], lang_code)
    category = article_data['category']  # 保持英文
    read_time = article_data['read_time']  # 保持英文格式
    intro = translate_text_ai(article_data['intro'], lang_code)
    content = translate_html_preserving_structure(article_data['content'], lang_code)
    
    # 翻译TL;DR
    tldr_items = []
    for item in article_data['tldr']:
        translated_item = translate_html_preserving_structure(item, lang_code)
        tldr_items.append(translated_item)
    
    tldr_html = ''.join([f'<li>{item}</li>' for item in tldr_items])
    
    # SVG Hero（保持原样，只翻译文本）
    svg_hero = article_data['svg_hero']
    if svg_hero:
        svg_soup = BeautifulSoup(svg_hero, 'html.parser')
        for text_node in svg_soup.find_all(string=True):
            if text_node.strip():
                translated = translate_text_ai(text_node, lang_code)
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
    
    print(f"📚 开始处理 {len(articles_data)} 篇文章")
    print(f"🌍 目标语言: {', '.join([LANG_CONFIG[lang]['name'] for lang in LANG_CONFIG.keys()])}")
    print(f"📊 总计: {len(articles_data)} × {len(LANG_CONFIG)} = {len(articles_data) * len(LANG_CONFIG)} 个文件\n")
    
    total = 0
    success = 0
    
    # 处理每篇文章
    for article_id in sorted(articles_data.keys()):
        article_data = articles_data[article_id]
        
        # 获取文件名
        zh_files = list((root / 'zh' / 'still-alive-tips').glob(f'{article_id}-*.html'))
        if not zh_files:
            continue
        zh_file_name = zh_files[0].name
        
        print(f"\n{'='*60}")
        print(f"📄 [{article_id}] {article_data['title'][:50]}...")
        print(f"{'='*60}")
        
        # 处理每种语言
        for lang_code, lang_info in LANG_CONFIG.items():
            lang_dir = root / lang_code / 'still-alive-tips'
            lang_dir.mkdir(parents=True, exist_ok=True)
            target_file = lang_dir / zh_file_name
            
            try:
                html_content = generate_article_html(article_data, lang_code, zh_file_name)
                target_file.write_text(html_content, encoding='utf-8')
                success += 1
                print(f"  ✅ {lang_info['name']:12} → {target_file.name}")
            except Exception as e:
                print(f"  ❌ {lang_info['name']:12} → 错误: {str(e)}")
            
            total += 1
    
    print(f"\n{'='*60}")
    print(f"✨ 完成！成功: {success}/{total} 个文件")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
