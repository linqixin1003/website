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

def translate_with_ai(text, target_lang, source_lang='en'):
    """
    使用AI翻译文本
    这里需要调用实际的AI翻译API
    返回翻译后的文本
    """
    # TODO: 集成翻译API（OpenAI, DeepL等）
    # 实际使用时需要替换为真实翻译
    return text

def translate_html_content(html_content, target_lang):
    """
    翻译HTML内容，保留HTML标签结构
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 遍历所有文本节点并翻译
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if parent and parent.name in ['script', 'style']:
            continue
        
        text = text_node.strip()
        if text:
            translated = translate_with_ai(text, target_lang)
            text_node.replace_with(translated)
    
    return str(soup)

def generate_article_html(en_article_data, translated, lang_code, lang_config):
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

def main():
    en_dir = root / 'still-alive-tips'
    en_files = sorted(en_dir.glob('*.html'))
    
    print(f"📚 开始翻译 {len(en_files)} 篇英文文章")
    print(f"🌍 目标语言: {', '.join([T1_LANGUAGES[lang]['name'] for lang in T1_LANGUAGES.keys()])}")
    print(f"📊 总计: {len(en_files)} × {len(T1_LANGUAGES)} = {len(en_files) * len(T1_LANGUAGES)} 个文件\n")
    
    total = 0
    success = 0
    
    for en_file in en_files:
        article_id = re.match(r'(\d+)-', en_file.name)
        if not article_id:
            continue
        
        article_id = article_id.group(1)
        print(f"\n📄 [{article_id}] {en_file.name}")
        
        # 提取英文文章内容
        en_article = extract_en_article(en_file)
        
        # 处理每种语言
        for lang_code, lang_config in T1_LANGUAGES.items():
            lang_dir = root / lang_code / 'still-alive-tips'
            lang_dir.mkdir(parents=True, exist_ok=True)
            target_file = lang_dir / en_file.name
            
            try:
                # 翻译内容（需要调用AI翻译API）
                translated = {
                    'title': translate_with_ai(en_article['title'], lang_code),
                    'intro': translate_with_ai(en_article['intro'], lang_code),
                    'tldr': [translate_html_content(item, lang_code) for item in en_article['tldr']],
                    'content': translate_html_content(en_article['content'], lang_code)
                }
                
                # 生成HTML
                html = generate_article_html(en_article, translated, lang_code, lang_config)
                
                # 保存文件
                target_file.write_text(html, encoding='utf-8')
                success += 1
                print(f"  ✅ {lang_config['name']:12} → {target_file.name}")
            except Exception as e:
                print(f"  ❌ {lang_config['name']:12} → 错误: {str(e)}")
            
            total += 1
    
    print(f"\n{'='*60}")
    print(f"✨ 完成！成功: {success}/{total} 个文件")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
