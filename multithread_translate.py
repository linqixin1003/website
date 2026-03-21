#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""多线程翻译 - 超高速模式"""

import re
import sys
import time
from pathlib import Path
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

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

# 线程锁用于打印
print_lock = threading.Lock()
# 统计
stats = {'total': 0, 'success': 0, 'failed': 0}
stats_lock = threading.Lock()

def safe_print(*args, **kwargs):
    """线程安全的打印"""
    with print_lock:
        print(*args, **kwargs)

def translate_text(text, target_lang):
    """快速翻译"""
    if not text or len(text.strip()) < 3:
        return text
    
    lang_name = LANGUAGES.get(target_lang, target_lang)
    
    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": f"Translate to {lang_name}:\n{text}"}],
                "temperature": 0.3,
                "max_tokens": 3000
            },
            timeout=15
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip().strip('"\'')
    except:
        pass
    
    return text

def translate_article(source_file, target_file, lang_code):
    """翻译单篇文章"""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 1. lang属性
        html = html.replace('<html lang="en">', f'<html lang="{lang_code}">')
        
        # 2. title
        html = re.sub(
            r'<title>([^<]+)</title>',
            lambda m: f'<title>{translate_text(m.group(1).replace(" - InsectAiSnap", ""), lang_code)} - InsectAiSnap</title>',
            html
        )
        
        # 3. hero-title
        html = re.sub(
            r'<h1 class="hero-title">([^<]+)</h1>',
            lambda m: f'<h1 class="hero-title">{translate_text(m.group(1), lang_code)}</h1>',
            html
        )
        
        # 4. hero-subtitle
        html = re.sub(
            r'<p class="hero-subtitle">([^<]+)</p>',
            lambda m: f'<p class="hero-subtitle">{translate_text(m.group(1), lang_code)}</p>',
            html
        )
        
        # 5. article-title
        html = re.sub(
            r'<h2 class="article-title">([^<]+)</h2>',
            lambda m: f'<h2 class="article-title">{translate_text(m.group(1), lang_code)}</h2>',
            html
        )
        
        # 6. 主要段落（限制前12个）
        count = 0
        def translate_paragraph(match):
            nonlocal count
            text = match.group(1).strip()
            if text and '<img' not in text and '<a' not in text and len(text) > 10:
                count += 1
                if count <= 12:
                    translated = translate_text(text, lang_code)
                    return match.group(0).replace(text, translated)
            return match.group(0)
        
        html = re.sub(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', translate_paragraph, html, flags=re.DOTALL)
        
        # 保存
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return True, source_file.name
    
    except Exception as e:
        return False, f"{source_file.name}: {e}"

def process_article(args):
    """处理单篇文章（用于线程池）"""
    source_file, target_file, lang_code, lang_name, idx, total = args
    
    success, msg = translate_article(source_file, target_file, lang_code)
    
    with stats_lock:
        stats['total'] += 1
        if success:
            stats['success'] += 1
            status = "✅"
        else:
            stats['failed'] += 1
            status = "❌"
    
    safe_print(f"  [{lang_name}] [{idx}/{total}] {status} {source_file.name[:35]}")
    
    return success

def process_language_multithread(lang_code, lang_name, max_workers=10):
    """多线程处理一种语言"""
    safe_print(f"\n{'='*70}")
    safe_print(f"🚀 {lang_name} ({lang_code}) - {max_workers}线程并行翻译")
    safe_print(f"{'='*70}\n")
    
    source_dir = Path('insect/en')
    target_dir = Path(f'insect/{lang_code}')
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    # 收集所有任务
    tasks = []
    for category in categories:
        source_cat = source_dir / category
        if not source_cat.exists():
            continue
        
        articles = sorted([f for f in source_cat.glob('[0-9]*.html')])
        for article in articles:
            target_file = target_dir / category / article.name
            tasks.append((article, target_file, lang_code, lang_name, len(tasks)+1, 50))
    
    # 多线程执行
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_article, task) for task in tasks]
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                safe_print(f"    ❌ 线程错误: {e}")
    
    elapsed = time.time() - start_time
    safe_print(f"\n  ⏱️  {lang_name} 完成，用时: {elapsed:.1f}秒 ({len(tasks)}篇)")
    
    return len(tasks)

def main():
    print("=" * 80)
    print("🚀 多线程超高速翻译 - DeepSeek API")
    print("=" * 80)
    print()
    print("⚙️  配置:")
    print("  - 线程数: 10个并发线程")
    print("  - API: DeepSeek")
    print("  - 模式: 快速翻译（核心内容）")
    print()
    
    start_time = time.time()
    
    for lang_code, lang_name in LANGUAGES.items():
        process_language_multithread(lang_code, lang_name, max_workers=10)
    
    total_time = time.time() - start_time
    
    print("\n" + "=" * 80)
    print("📊 翻译统计")
    print("=" * 80)
    print(f"✅ 成功: {stats['success']}")
    print(f"❌ 失败: {stats['failed']}")
    print(f"⏱️  总用时: {total_time/60:.1f} 分钟")
    print(f"⚡ 平均速度: {total_time/stats['total']:.1f} 秒/篇")
    print("=" * 80)

if __name__ == '__main__':
    main()

