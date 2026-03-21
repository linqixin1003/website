#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用AI能力翻译文章 - 逐篇处理
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path('/Users/conalin/website')

T1_LANGUAGES = {
    'de': {'name': 'German', 'back_text': '← Zurück', 'tldr_title': '⚡ TL;DR'},
    'es': {'name': 'Spanish', 'back_text': '← Volver', 'tldr_title': '⚡ TL;DR'},
    'fr': {'name': 'French', 'back_text': '← Retour', 'tldr_title': '⚡ TL;DR'},
    'it': {'name': 'Italian', 'back_text': '← Indietro', 'tldr_title': '⚡ TL;DR'},
    'ja': {'name': 'Japanese', 'back_text': '← 戻る', 'tldr_title': '⚡ TL;DR'},
    'ko': {'name': 'Korean', 'back_text': '← 뒤로', 'tldr_title': '⚡ TL;DR'},
    'pt': {'name': 'Portuguese', 'back_text': '← Voltar', 'tldr_title': '⚡ TL;DR'},
    'ru': {'name': 'Russian', 'back_text': '← Назад', 'tldr_title': '⚡ TL;DR'}
}

def extract_en_article(en_file_path):
    """提取英文文章的所有内容"""
    en_html = en_file_path.read_text(encoding='utf-8')
    en_soup = BeautifulSoup(en_html, 'html.parser')
    
    title = en_soup.find('h1', class_='hero-title').get_text(strip=True)
    intro = en_soup.find('p', class_='intro-text').get_text(strip=True)
    tldr_items = [li.decode_contents() for li in en_soup.find('ul', class_='summary-list').find_all('li')]
    
    content_block = en_soup.find('div', class_='content-block')
    content_children = []
    for child in content_block.children:
        if hasattr(child, 'get') and child.get('class') and 'intro-text' in child.get('class'):
            continue
        content_children.append(str(child))
    content_html = ''.join(content_children)
    
    svg_hero = str(en_soup.find('div', class_='hero-image'))
    category = en_soup.find('div', class_='article-meta-top').find_all('span')[0].get_text(strip=True)
    read_time = en_soup.find('div', class_='article-meta-top').find_all('span')[2].get_text(strip=True)
    theme = en_soup.find('html').get('data-theme', 'bowel')
    
    return {
        'title': title,
        'intro': intro,
        'tldr': tldr_items,
        'content': content_html,
        'svg_hero': svg_hero,
        'category': category,
        'read_time': read_time,
        'theme': theme
    }

def generate_html(en_article, translated, lang_code, lang_config):
    """生成翻译后的HTML"""
    safe_title = translated['title'].replace("'", "\\'")
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_code}" data-theme="{en_article['theme']}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{translated['title']} - Happy Poop</title>
    <link rel="stylesheet" href="../../article-theme-v2.css">
</head>
<body>
    <header class="hero-section">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="article-meta-top">
                <span>{en_article['category']}</span>
                <span>•</span>
                <span>{en_article['read_time']}</span>
            </div>
            <h1 class="hero-title">{translated['title']}</h1>
            <div class="hero-image">{en_article['svg_hero']}</div>
        </div>
    </header>
    <div class="summary-card">
        <div class="summary-title">{lang_config['tldr_title']}</div>
        <ul class="summary-list">
            <li>{translated['tldr'][0]}</li>
            <li>{translated['tldr'][1]}</li>
            <li>{translated['tldr'][2]}</li>
            <li>{translated['tldr'][3]}</li>
        </ul>
    </div>
    <article class="content-container">
        <div class="content-block">
            <p class="intro-text">{translated['intro']}</p>
            {translated['content']}
        </div>
    </article>
    <nav class="floating-nav">
        <a href="../../happy-poop-mobile.html" class="back-btn">{lang_config['back_text']}</a>
        <a href="#" class="share-btn" onclick="navigator.share({{title: '{safe_title}', url: window.location.href}}); return false;">📤</a>
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

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("用法: python3 ai_translate_article.py <article_number>")
        print("例如: python3 ai_translate_article.py 01")
        sys.exit(1)
    
    article_num = sys.argv[1]
    en_file = root / 'still-alive-tips' / f'{article_num}-*.html'
    en_files = list(root.glob(f'still-alive-tips/{article_num}-*.html'))
    
    if not en_files:
        print(f"找不到文章 {article_num}")
        sys.exit(1)
    
    en_file = en_files[0]
    print(f"处理文章: {en_file.name}")
    
    en_article = extract_en_article(en_file)
    print(f"\n标题: {en_article['title']}")
    print(f"介绍: {en_article['intro'][:80]}...")
    print(f"\n准备翻译到 {len(T1_LANGUAGES)} 种语言...")
    print("\n请使用AI能力翻译以下内容:")
    print(f"\n1. 标题: {en_article['title']}")
    print(f"\n2. 介绍: {en_article['intro']}")
    print(f"\n3. TL;DR:")
    for i, item in enumerate(en_article['tldr'], 1):
        print(f"   {i}. {item}")
    print(f"\n4. 正文内容 (HTML格式，需要保留标签)")
