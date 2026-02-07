#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用AI能力批量翻译英文文章到T1国家语言
逐篇处理，确保翻译质量
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re
import json

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

def generate_article_html(en_article_data, translated, lang_code, lang_config):
    """生成单篇文章的HTML"""
    # 转义标题中的单引号
    safe_title = translated['title'].replace("'", "\\'")
    
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

def save_translation_data(article_id, lang_code, translated_data):
    """保存翻译数据到JSON文件，供AI使用"""
    data_file = root / 'translation_cache.json'
    if data_file.exists():
        with open(data_file, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    else:
        cache = {}
    
    if article_id not in cache:
        cache[article_id] = {}
    
    cache[article_id][lang_code] = translated_data
    
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def main():
    en_dir = root / 'still-alive-tips'
    en_files = sorted(en_dir.glob('*.html'))
    
    print(f"📚 开始处理 {len(en_files)} 篇英文文章")
    print(f"🌍 目标语言: {', '.join([T1_LANGUAGES[lang]['name'] for lang in T1_LANGUAGES.keys()])}")
    print(f"📊 总计: {len(en_files)} × {len(T1_LANGUAGES)} = {len(en_files) * len(T1_LANGUAGES)} 个文件\n")
    
    for en_file in en_files:
        article_id = re.match(r'(\d+)-', en_file.name)
        if not article_id:
            continue
        
        article_id = article_id.group(1)
        print(f"\n{'='*70}")
        print(f"📄 文章 [{article_id}]: {en_file.name}")
        print(f"{'='*70}")
        
        # 提取英文文章内容
        en_article = extract_en_article(en_file)
        
        print(f"\n📝 英文内容摘要:")
        print(f"   标题: {en_article['title'][:60]}...")
        print(f"   介绍: {en_article['intro'][:60]}...")
        print(f"   TL;DR: {len(en_article['tldr'])} 项")
        print(f"   正文: {len(en_article['content'])} 字符")
        
        # 为每种语言准备翻译数据
        for lang_code, lang_config in T1_LANGUAGES.items():
            lang_dir = root / lang_code / 'still-alive-tips'
            lang_dir.mkdir(parents=True, exist_ok=True)
            target_file = lang_dir / en_file.name
            
            print(f"\n  🌍 [{lang_config['name']}] 准备翻译数据...")
            
            # 保存需要翻译的内容到JSON
            translation_data = {
                'title': en_article['title'],
                'intro': en_article['intro'],
                'tldr': en_article['tldr'],
                'content': en_article['content'],
                'category': en_article['category'],
                'read_time': en_article['read_time'],
                'theme': en_article['theme'],
                'svg_hero': en_article['svg_hero']
            }
            
            save_translation_data(article_id, lang_code, translation_data)
            print(f"     ✅ 翻译数据已保存，等待AI翻译...")

if __name__ == '__main__':
    main()
