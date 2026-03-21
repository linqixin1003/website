#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""快速翻译 - 移除延迟，加速处理"""

import re
import sys
import time
from pathlib import Path
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

LANGUAGES = {
    'de': 'German',
    'es': 'Spanish',
    'fr': 'French',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian'
}

def translate_text(text, target_lang):
    """快速翻译 - 无延迟"""
    if not text or len(text.strip()) < 3:
        return text
    
    lang_name = LANGUAGES.get(target_lang, target_lang)
    prompt = f"Translate to {lang_name}, only output translation:\n\n{text}"
    
    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 4000
            },
            timeout=20
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip().strip('"\'')
    except:
        pass
    
    return text

def translate_article_fast(source_file, target_file, target_lang):
    """快速翻译文章 - 批量处理"""
    with open(source_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<html lang="en">', f'<html lang="{target_lang}">')
    
    # 收集所有需要翻译的文本
    texts_to_translate = []
    
    # title
    if m := re.search(r'<title>([^<]+)</title>', html):
        texts_to_translate.append(('title', m.group(1).replace(' - InsectAiSnap', '')))
    
    # hero-title
    if m := re.search(r'<h1 class="hero-title">([^<]+)</h1>', html):
        texts_to_translate.append(('hero-title', m.group(1)))
    
    # hero-subtitle
    if m := re.search(r'<p class="hero-subtitle">([^<]+)</p>', html):
        texts_to_translate.append(('hero-subtitle', m.group(1)))
    
    # article-title
    if m := re.search(r'<h2 class="article-title">([^<]+)</h2>', html):
        texts_to_translate.append(('article-title', m.group(1)))
    
    # 段落（只取前10个主要段落，加快速度）
    for i, m in enumerate(re.finditer(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', html, re.DOTALL)):
        text = m.group(1).strip()
        if text and '<img' not in text and len(text) > 10:
            texts_to_translate.append(('paragraph', text, m.group(0)))
            if i >= 15:  # 限制数量
                break
    
    # 并行翻译所有文本
    print(f"    翻译 {len(texts_to_translate)} 个文本...", end=' ', flush=True)
    
    translations = {}
    for item in texts_to_translate:
        if len(item) == 2:
            key, text = item
            translated = translate_text(text, target_lang)
            translations[key] = translated
        else:
            key, text, original = item
            translated = translate_text(text, target_lang)
            if original:
                html = html.replace(original, original.replace(text, translated), 1)
    
    # 应用翻译
    if 'title' in translations:
        html = re.sub(r'<title>([^<]+)</title>', 
                     f'<title>{translations["title"]} - InsectAiSnap</title>', html)
    
    if 'hero-title' in translations:
        html = re.sub(r'<h1 class="hero-title">([^<]+)</h1>',
                     f'<h1 class="hero-title">{translations["hero-title"]}</h1>', html)
    
    if 'hero-subtitle' in translations:
        html = re.sub(r'<p class="hero-subtitle">([^<]+)</p>',
                     f'<p class="hero-subtitle">{translations["hero-subtitle"]}</p>', html)
    
    if 'article-title' in translations:
        html = re.sub(r'<h2 class="article-title">([^<]+)</h2>',
                     f'<h2 class="article-title">{translations["article-title"]}</h2>', html)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅")

def process_language(lang_code, lang_name):
    """处理一种语言"""
    print(f"\n{'='*60}")
    print(f"{lang_name} ({lang_code})")
    print(f"{'='*60}\n")
    
    source_dir = Path('insect/en')
    target_dir = Path(f'insect/{lang_code}')
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    success = 0
    
    for category in categories:
        source_cat = source_dir / category
        if not source_cat.exists():
            continue
        
        articles = sorted([f for f in source_cat.glob('[0-9]*.html')])
        
        for article in articles:
            total += 1
            target_file = target_dir / category / article.name
            
            print(f"  [{total}/50] {article.name[:40]}...", end=' ', flush=True)
            
            try:
                translate_article_fast(article, target_file, lang_code)
                success += 1
            except Exception as e:
                print(f"❌ {e}")
    
    print(f"\n{lang_name} 完成: {success}/{total}")
    return success, total

def main():
    print("=" * 80)
    print("快速翻译模式 - DeepSeek API（无延迟）")
    print("=" * 80)
    print()
    
    total_success = 0
    total_articles = 0
    
    for lang_code, lang_name in LANGUAGES.items():
        success, total = process_language(lang_code, lang_name)
        total_success += success
        total_articles += total
    
    print("\n" + "=" * 80)
    print(f"✅ 翻译完成: {total_success}/{total_articles}")
    print("=" * 80)

if __name__ == '__main__':
    main()

