#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译所有英文文章到T1国家语言
30篇文章 × 8种语言 = 240个文件
使用AI逐篇完整翻译，确保准确完整
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path('/Users/conalin/website')

# T1国家语言配置
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

def generate_html(lang_code, lang_config, translated, en_article_data):
    """生成单篇文章的HTML"""
    html = f'''<!DOCTYPE html>
<html lang="{lang_code}" data-theme="{en_article_data['theme']}">
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
                <span>{en_article_data['category']}</span>
                <span>•</span>
                <span>{en_article_data['read_time']}</span>
            </div>
            <h1 class="hero-title">{translated['title']}</h1>
            <div class="hero-image">{en_article_data['svg_hero']}</div>
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
        <a href="#" class="share-btn" onclick="navigator.share({{title: '{translated['title']}', url: window.location.href}}); return false;">📤</a>
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
    en_dir = root / 'still-alive-tips'
    en_files = sorted(en_dir.glob('*.html'))
    
    print(f"📚 开始翻译 {len(en_files)} 篇英文文章")
    print(f"🌍 目标语言: {', '.join([T1_LANGUAGES[lang]['name'] for lang in T1_LANGUAGES.keys()])}")
    print(f"📊 总计: {len(en_files)} × {len(T1_LANGUAGES)} = {len(en_files) * len(T1_LANGUAGES)} 个文件\n")
    
    print("💡 由于翻译量很大，将使用AI逐篇完整翻译")
    print("   建议分批处理，确保每篇都准确完整\n")
    
    # TODO: 集成AI翻译API
    # 当前脚本框架已就绪，等待集成实际翻译功能
    
    print("📝 脚本框架已就绪，等待集成AI翻译API")
    print("   需要翻译的内容：")
    print("   - 标题 (title)")
    print("   - 介绍 (intro)")
    print("   - TL;DR 列表 (tldr)")
    print("   - 正文内容 (content)")

if __name__ == '__main__':
    main()
