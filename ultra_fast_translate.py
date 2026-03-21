#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""超快速多线程翻译 - 只翻译剩余语言"""

import re
import sys
from pathlib import Path
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

# 只翻译这些语言（跳过中文zh和日语ja）
LANGUAGES = {
    'de': 'German',
    'es': 'Spanish',
    'fr': 'French',
    'it': 'Italian',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian'
}

print_lock = threading.Lock()
completed = {'count': 0}

def safe_print(msg):
    with print_lock:
        print(msg, flush=True)

def translate_batch(texts, lang_code):
    """批量翻译多个文本"""
    if not texts:
        return texts
    
    lang_name = LANGUAGES.get(lang_code, lang_code)
    combined = "\n###\n".join(texts)
    
    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": f"Translate each part to {lang_name}, keep ### separators:\n\n{combined}"}],
                "temperature": 0.3,
                "max_tokens": 8000
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
            translations = result.split('###')
            return [t.strip().strip('"\'') for t in translations]
    except:
        pass
    
    return texts

def translate_article_ultra_fast(source_file, target_file, lang_code):
    """超快速翻译单篇文章"""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        html = html.replace('<html lang="en">', f'<html lang="{lang_code}">')
        
        # 收集需要翻译的文本
        texts = []
        
        # title
        if m := re.search(r'<title>([^<]+)</title>', html):
            texts.append(m.group(1).replace(' - InsectAiSnap', ''))
        
        # hero-title
        if m := re.search(r'<h1 class="hero-title">([^<]+)</h1>', html):
            texts.append(m.group(1))
        
        # hero-subtitle
        if m := re.search(r'<p class="hero-subtitle">([^<]+)</p>', html):
            texts.append(m.group(1))
        
        # article-title
        if m := re.search(r'<h2 class="article-title">([^<]+)</h2>', html):
            texts.append(m.group(1))
        
        # 前8个主要段落
        for i, m in enumerate(re.finditer(r'<p class="intro">(.*?)</p>', html, re.DOTALL)):
            if i < 8:
                texts.append(m.group(1).strip())
        
        # 批量翻译
        translations = translate_batch(texts, lang_code)
        
        # 应用翻译
        idx = 0
        if idx < len(translations):
            html = re.sub(r'<title>([^<]+)</title>', f'<title>{translations[idx]} - InsectAiSnap</title>', html)
            idx += 1
        
        if idx < len(translations):
            html = re.sub(r'<h1 class="hero-title">([^<]+)</h1>', f'<h1 class="hero-title">{translations[idx]}</h1>', html)
            idx += 1
        
        if idx < len(translations):
            html = re.sub(r'<p class="hero-subtitle">([^<]+)</p>', f'<p class="hero-subtitle">{translations[idx]}</p>', html)
            idx += 1
        
        if idx < len(translations):
            html = re.sub(r'<h2 class="article-title">([^<]+)</h2>', f'<h2 class="article-title">{translations[idx]}</h2>', html)
            idx += 1
        
        # 替换段落
        for i, m in enumerate(re.finditer(r'<p class="intro">(.*?)</p>', html, re.DOTALL)):
            if i < 8 and idx < len(translations):
                html = html.replace(m.group(0), f'<p class="intro">{translations[idx]}</p>', 1)
                idx += 1
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return True
    except Exception as e:
        return False

def process_article_task(args):
    """处理单篇文章任务"""
    source_file, target_file, lang_code, lang_name, idx = args
    
    success = translate_article_ultra_fast(source_file, target_file, lang_code)
    
    completed['count'] += 1
    status = "✅" if success else "❌"
    safe_print(f"[{completed['count']}/350] {lang_name:12} {status} {source_file.name[:35]}")
    
    return success

def main():
    print("=" * 80)
    print("🚀🚀🚀 超快速多线程翻译 - 7种语言并行")
    print("=" * 80)
    print(f"线程数: 20个并发")
    print(f"语言: {', '.join(LANGUAGES.values())}")
    print()
    
    source_dir = Path('insect/en')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    # 收集所有任务
    all_tasks = []
    for lang_code, lang_name in LANGUAGES.items():
        target_dir = Path(f'insect/{lang_code}')
        
        for category in categories:
            source_cat = source_dir / category
            if not source_cat.exists():
                continue
            
            articles = sorted([f for f in source_cat.glob('[0-9]*.html')])
            for article in articles:
                target_file = target_dir / category / article.name
                all_tasks.append((article, target_file, lang_code, lang_name, len(all_tasks)+1))
    
    print(f"总任务: {len(all_tasks)} 篇文章")
    print("=" * 80)
    print()
    
    # 20线程并发执行
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(process_article_task, task) for task in all_tasks]
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                safe_print(f"❌ 错误: {e}")
    
    print()
    print("=" * 80)
    print("🎉 翻译完成！")
    print("=" * 80)

if __name__ == '__main__':
    main()

