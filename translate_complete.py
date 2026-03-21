#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整翻译脚本 - 使用 Google Translate (free) 翻译所有 still-alive-tips 文章
支持断点续传：已完整的文件会被跳过
用法:
  python3 translate_complete.py                    # 翻译所有文章的所有语言
  python3 translate_complete.py 02 03              # 只翻译文章 02 和 03
  python3 translate_complete.py 02 --lang=zh,es    # 只翻译文章 02 的中文和西班牙语
  python3 translate_complete.py --force             # 强制重新翻译（忽略已完成的）
"""
import re
import sys
import time
import traceback
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from deep_translator import GoogleTranslator

ROOT = Path('/Users/conalin/website')
EN_DIR = ROOT / 'still-alive-tips'
MAX_CHARS = 4500  # Google Translate 的安全字符限制

# 语言配置
LANGUAGES = {
    'zh': {
        'name': 'Simplified Chinese', 'gt_code': 'zh-CN', 'html_lang': 'zh-CN',
        'back_text': '← 返回列表',
        'category_map': {'Bowel Health': '肠道健康', 'Hydration': '水分补充', 'Menstrual Health': '经期健康', 'Nutrition': '营养', 'Safety': '安全'},
        'min_read_fmt': '{n}分钟阅读',
    },
    'es': {
        'name': 'Spanish', 'gt_code': 'es', 'html_lang': 'es',
        'back_text': '← Volver',
        'category_map': {'Bowel Health': 'Salud Intestinal', 'Hydration': 'Hidratación', 'Menstrual Health': 'Salud Menstrual', 'Nutrition': 'Nutrición', 'Safety': 'Seguridad'},
        'min_read_fmt': '{n} min de lectura',
    },
    'fr': {
        'name': 'French', 'gt_code': 'fr', 'html_lang': 'fr',
        'back_text': '← Retour',
        'category_map': {'Bowel Health': 'Santé Intestinale', 'Hydration': 'Hydratation', 'Menstrual Health': 'Santé Menstruelle', 'Nutrition': 'Nutrition', 'Safety': 'Sécurité'},
        'min_read_fmt': '{n} min de lecture',
    },
    'de': {
        'name': 'German', 'gt_code': 'de', 'html_lang': 'de',
        'back_text': '← Zurück',
        'category_map': {'Bowel Health': 'Darmgesundheit', 'Hydration': 'Hydratation', 'Menstrual Health': 'Menstruationsgesundheit', 'Nutrition': 'Ernährung', 'Safety': 'Sicherheit'},
        'min_read_fmt': '{n} Min. Lesezeit',
    },
    'it': {
        'name': 'Italian', 'gt_code': 'it', 'html_lang': 'it',
        'back_text': '← Indietro',
        'category_map': {'Bowel Health': 'Salute Intestinale', 'Hydration': 'Idratazione', 'Menstrual Health': 'Salute Mestruale', 'Nutrition': 'Nutrizione', 'Safety': 'Sicurezza'},
        'min_read_fmt': '{n} min di lettura',
    },
    'pt': {
        'name': 'Portuguese', 'gt_code': 'pt', 'html_lang': 'pt',
        'back_text': '← Voltar',
        'category_map': {'Bowel Health': 'Saúde Intestinal', 'Hydration': 'Hidratação', 'Menstrual Health': 'Saúde Menstrual', 'Nutrition': 'Nutrição', 'Safety': 'Segurança'},
        'min_read_fmt': '{n} min de leitura',
    },
    'ja': {
        'name': 'Japanese', 'gt_code': 'ja', 'html_lang': 'ja',
        'back_text': '← 戻る',
        'category_map': {'Bowel Health': '腸の健康', 'Hydration': '水分補給', 'Menstrual Health': '月経の健康', 'Nutrition': '栄養', 'Safety': '安全'},
        'min_read_fmt': '{n}分で読める',
    },
    'ko': {
        'name': 'Korean', 'gt_code': 'ko', 'html_lang': 'ko',
        'back_text': '← 뒤로',
        'category_map': {'Bowel Health': '장 건강', 'Hydration': '수분 보충', 'Menstrual Health': '월경 건강', 'Nutrition': '영양', 'Safety': '안전'},
        'min_read_fmt': '{n}분 읽기',
    },
    'ru': {
        'name': 'Russian', 'gt_code': 'ru', 'html_lang': 'ru',
        'back_text': '← Назад',
        'category_map': {'Bowel Health': 'Здоровье кишечника', 'Hydration': 'Гидратация', 'Menstrual Health': 'Менструальное здоровье', 'Nutrition': 'Питание', 'Safety': 'Безопасность'},
        'min_read_fmt': '{n} мин чтения',
    },
}


def translate_text(text, target_lang_code, retries=3):
    """翻译纯文本，带重试"""
    if not text or not text.strip():
        return text
    for attempt in range(retries):
        try:
            result = GoogleTranslator(source='en', target=target_lang_code).translate(text)
            return result if result else text
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"      ⚠️ Translation failed for chunk: {str(e)[:80]}")
                return text  # 返回原文作为 fallback


def protect_html_attributes(html):
    """在翻译前保护 HTML 属性不被翻译"""
    placeholders = {}
    counter = [0]
    
    def replace_attr(match):
        key = f'ATTRPLACEHOLDER{counter[0]:04d}'
        counter[0] += 1
        placeholders[key] = match.group(0)
        return key
    
    # 保护 class="..." id="..." href="..." src="..." onclick="..." style="..." 等属性
    protected = re.sub(r'\b(class|id|href|src|onclick|style|data-theme|type|rel|charset|name|content|viewBox|viewbox|xmlns|fill|stroke|stroke-width|stroke-linecap|opacity|cx|cy|r|d|x1|x2|y1|y2|offset|transform|dur|values|repeatCount|repeatcount|attributeName|attributename)="[^"]*"', replace_attr, html)
    
    # 保护 <svg>...</svg> 整个 SVG 标签
    protected = re.sub(r'<svg[\s\S]*?</svg>', replace_attr, protected)
    
    return protected, placeholders


def restore_html_attributes(html, placeholders):
    """翻译后恢复 HTML 属性（大小写不敏感，修复 Google Translate 改变占位符大小写的问题）"""
    for key, value in placeholders.items():
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        html = pattern.sub(lambda m: value, html)
    return html


def translate_html_chunk(html_chunk, target_lang_code, retries=3):
    """翻译 HTML 片段（保留标签结构和属性）"""
    if not html_chunk or not html_chunk.strip():
        return html_chunk
    
    # 如果太长，需要分割
    if len(html_chunk) > MAX_CHARS:
        return translate_html_long(html_chunk, target_lang_code)
    
    # 保护 HTML 属性
    protected, placeholders = protect_html_attributes(html_chunk)
    
    # 如果保护后太长，用长文本方法
    if len(protected) > MAX_CHARS:
        result = translate_html_long(html_chunk, target_lang_code)
        return result
    
    for attempt in range(retries):
        try:
            result = GoogleTranslator(source='en', target=target_lang_code).translate(protected)
            if result:
                result = restore_html_attributes(result, placeholders)
                return result
            return html_chunk
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"      ⚠️ HTML chunk translation failed: {str(e)[:80]}")
                return html_chunk


def translate_html_long(html_content, target_lang_code):
    """翻译大块 HTML 内容 - 按段落/元素分割翻译"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 遍历所有直接子元素，逐个翻译
    for element in soup.find_all(True):  # 所有标签
        # 只处理包含直接文本的叶子节点
        for child in list(element.children):
            if isinstance(child, NavigableString) and child.strip():
                text = str(child)
                if len(text.strip()) > 1:  # 跳过单字符（如空格、标点）
                    translated = translate_text(text, target_lang_code)
                    if translated:
                        child.replace_with(translated)
                    time.sleep(0.3)
    
    return str(soup)


def split_content_at_h2(body_html):
    """将 body HTML 在 <h2> 处分割为段落组"""
    # 使用正则在 <h2 前分割
    parts = re.split(r'(?=<h2[\s>])', body_html)
    return [p for p in parts if p.strip()]


def extract_en_article(en_file):
    """提取英文文章的完整结构"""
    html = en_file.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    title_elem = soup.find('h1', class_='hero-title')
    title = title_elem.get_text(strip=True) if title_elem else ''
    
    theme = soup.find('html').get('data-theme', 'bowel')
    
    meta = soup.find('div', class_='article-meta-top')
    if meta:
        spans = meta.find_all('span')
        category = spans[0].get_text(strip=True) if len(spans) > 0 else 'Bowel Health'
        read_time_raw = spans[2].get_text(strip=True) if len(spans) > 2 else '7 min read'
        read_minutes = re.search(r'(\d+)', read_time_raw)
        read_minutes = read_minutes.group(1) if read_minutes else '7'
    else:
        category = 'Bowel Health'
        read_minutes = '7'
    
    # TL;DR
    summary_list = soup.find('ul', class_='summary-list')
    tldr_items = []
    if summary_list:
        for li in summary_list.find_all('li'):
            tldr_items.append(str(li))  # 保留 <li> 内部 HTML
    
    # Intro
    intro_elem = soup.find('p', class_='intro-text')
    intro_html = str(intro_elem) if intro_elem else ''
    
    # SVG Hero
    hero_img = soup.find('div', class_='hero-image')
    svg_hero = str(hero_img) if hero_img else ''
    
    # Body content (除去 intro)
    content_block = soup.find('div', class_='content-block')
    body_sections = []
    if content_block:
        # 获取 intro 之后的所有内容
        full_html = ''.join(str(c) for c in content_block.children)
        # 移除 intro
        if intro_elem:
            intro_str = str(intro_elem)
            full_html = full_html.replace(intro_str, '', 1)
        body_sections = split_content_at_h2(full_html)
    
    h2_count = len(soup.find_all('h2'))
    
    # Share title for nav script
    share_title = title
    
    return {
        'title': title,
        'theme': theme,
        'category': category,
        'read_minutes': read_minutes,
        'tldr_items': tldr_items,
        'intro_html': intro_html,
        'svg_hero': svg_hero,
        'body_sections': body_sections,
        'h2_count': h2_count,
        'share_title': share_title,
    }


def check_existing(lang, filename, en_h2_count, force=False):
    """检查现有翻译是否完整"""
    if force:
        return False
    
    target = ROOT / lang / 'still-alive-tips' / filename
    if not target.exists():
        return False
    
    content = target.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    h2_count = len(soup.find_all('h2'))
    
    # h2 数量达到英文的 70% 认为完整
    return h2_count >= max(en_h2_count * 0.7, en_h2_count - 1)


def generate_translated_html(en_article, lang, lang_config, translated_parts):
    """生成翻译后的完整 HTML"""
    safe_title = translated_parts['title'].replace("'", "\\'").replace('"', '&quot;')
    
    tldr_html = '\n            '.join(translated_parts['tldr_items'])
    body_html = '\n            '.join(translated_parts['body_sections'])
    
    category = lang_config['category_map'].get(en_article['category'], en_article['category'])
    read_time = lang_config['min_read_fmt'].format(n=en_article['read_minutes'])
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_config['html_lang']}" data-theme="{en_article['theme']}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{translated_parts['title']} - Happy Poop</title>
    <link rel="stylesheet" href="../../article-theme-v2.css">
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
            <h1 class="hero-title">{translated_parts['title']}</h1>
            {en_article['svg_hero']}
        </div>
    </header>
    <div class="summary-card">
        <div class="summary-title">⚡ TL;DR</div>
        <ul class="summary-list">
            {tldr_html}
        </ul>
    </div>
    <article class="content-container">
        <div class="content-block">
            {translated_parts['intro_html']}
            {body_html}
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


def translate_article_to_lang(en_article, lang, lang_config):
    """翻译一篇文章到指定语言"""
    gt_code = lang_config['gt_code']
    
    # 1. 翻译标题
    title = translate_text(en_article['title'], gt_code)
    time.sleep(0.5)
    
    # 2. 翻译 TL;DR 条目
    translated_tldr = []
    for item in en_article['tldr_items']:
        translated_item = translate_html_chunk(item, gt_code)
        translated_tldr.append(translated_item)
        time.sleep(0.5)
    
    # 3. 翻译 intro
    intro_text = en_article['intro_html']
    if intro_text:
        # 提取 <p> 内的文本翻译
        intro_soup = BeautifulSoup(intro_text, 'html.parser')
        intro_p = intro_soup.find('p')
        if intro_p:
            inner_html = intro_p.decode_contents()
            translated_inner = translate_html_chunk(inner_html, gt_code)
            intro_html = f'<p class="intro-text">{translated_inner}</p>'
        else:
            intro_html = translate_html_chunk(intro_text, gt_code)
    else:
        intro_html = ''
    time.sleep(0.5)
    
    # 4. 翻译 body sections
    translated_sections = []
    for i, section in enumerate(en_article['body_sections']):
        print(f"        section {i+1}/{len(en_article['body_sections'])}...", end=' ', flush=True)
        
        if len(section) <= MAX_CHARS:
            translated = translate_html_chunk(section, gt_code)
        else:
            # 大段落需要进一步分割
            sub_parts = re.split(r'(?=<(?:p|div|ul)\s*[^>]*>)', section)
            translated_sub = []
            for sub in sub_parts:
                if sub.strip():
                    if len(sub) <= MAX_CHARS:
                        t = translate_html_chunk(sub, gt_code)
                    else:
                        t = translate_html_long(sub, gt_code)
                    translated_sub.append(t)
                    time.sleep(0.3)
            translated = ''.join(translated_sub)
        
        translated_sections.append(translated)
        print("✓", flush=True)
        time.sleep(0.5)
    
    return {
        'title': title,
        'tldr_items': translated_tldr,
        'intro_html': intro_html,
        'body_sections': translated_sections,
    }


def process_article(en_file, langs_to_process=None, force=False):
    """处理单篇文章"""
    filename = en_file.name
    article_num = filename.split('-')[0]
    
    print(f"\n{'='*60}")
    print(f"📄 [{article_num}] {filename}")
    print(f"{'='*60}")
    
    en_article = extract_en_article(en_file)
    print(f"  EN: {en_article['title'][:60]}... ({en_article['h2_count']} sections, {len(en_article['body_sections'])} body blocks)")
    
    langs = langs_to_process or list(LANGUAGES.keys())
    completed = 0
    skipped = 0
    failed = 0
    
    for lang in langs:
        lang_config = LANGUAGES[lang]
        target_dir = ROOT / lang / 'still-alive-tips'
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / filename
        
        # 检查是否已完整
        if check_existing(lang, filename, en_article['h2_count'], force):
            print(f"  ✅ {lang.upper():3} - already complete ({target_file.stat().st_size} bytes)")
            skipped += 1
            continue
        
        print(f"  🔄 {lang.upper():3} - translating to {lang_config['name']}...")
        
        try:
            translated = translate_article_to_lang(en_article, lang, lang_config)
            html = generate_translated_html(en_article, lang, lang_config, translated)
            
            # 验证
            soup = BeautifulSoup(html, 'html.parser')
            new_h2 = len(soup.find_all('h2'))
            file_size = len(html.encode('utf-8'))
            
            target_file.write_text(html, encoding='utf-8')
            
            status = '✅' if new_h2 >= en_article['h2_count'] * 0.7 else '⚠️'
            print(f"  {status} {lang.upper():3} - done ({new_h2}/{en_article['h2_count']} sections, {file_size} bytes)")
            completed += 1
            
        except Exception as e:
            print(f"  ❌ {lang.upper():3} - error: {str(e)[:100]}")
            traceback.print_exc()
            failed += 1
        
        # 语言之间稍作暂停
        time.sleep(1)
    
    return completed, skipped, failed


def main():
    articles_filter = []
    langs_filter = None
    force = False
    
    for arg in sys.argv[1:]:
        if arg.startswith('--lang='):
            langs_filter = arg.replace('--lang=', '').split(',')
        elif arg == '--force':
            force = True
        elif re.match(r'^\d{2}$', arg):
            articles_filter.append(arg)
    
    en_files = sorted(EN_DIR.glob('*.html'))
    
    if articles_filter:
        en_files = [f for f in en_files if f.name.split('-')[0] in articles_filter]
    
    total_articles = len(en_files)
    total_langs = len(langs_filter) if langs_filter else len(LANGUAGES)
    
    print(f"🚀 Happy Poop 文章完整翻译")
    print(f"📚 文章数: {total_articles}")
    print(f"🌍 语言数: {total_langs}")
    print(f"📊 最大文件数: {total_articles * total_langs}")
    if force:
        print(f"⚠️  强制模式: 已有翻译将被覆盖")
    
    total_completed = 0
    total_skipped = 0
    total_failed = 0
    
    for i, en_file in enumerate(en_files, 1):
        print(f"\n{'─'*60}")
        print(f"  进度: [{i}/{total_articles}]")
        c, s, f = process_article(en_file, langs_filter, force)
        total_completed += c
        total_skipped += s
        total_failed += f
    
    print(f"\n\n{'='*60}")
    print(f"✨ 翻译任务完成!")
    print(f"  ✅ 新翻译: {total_completed}")
    print(f"  ⏭️  跳过: {total_skipped}")
    print(f"  ❌ 失败: {total_failed}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
