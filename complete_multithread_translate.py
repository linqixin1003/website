#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完整多线程翻译 - 翻译所有内容"""

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

# 线程锁
print_lock = threading.Lock()
stats = {'total': 0, 'success': 0, 'failed': 0}
stats_lock = threading.Lock()

def safe_print(*args, **kwargs):
    """线程安全的打印"""
    with print_lock:
        print(*args, **kwargs)

def translate_text(text, target_lang):
    """翻译文本 - 带重试机制"""
    if not text or len(text.strip()) < 3:
        return text
    
    lang_name = LANGUAGES.get(target_lang, target_lang)
    
    for attempt in range(3):  # 最多重试3次
        try:
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": f"Translate to {lang_name}, return ONLY the translation:\n{text}"}],
                    "temperature": 0.3,
                    "max_tokens": 4000
                },
                timeout=20
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip().strip('"\'')
        except Exception as e:
            if attempt == 2:  # 最后一次尝试失败
                safe_print(f"    ⚠️  翻译失败: {str(e)[:50]}")
            time.sleep(0.5)
    
    return text  # 如果失败返回原文

def translate_article_complete(source_file, target_file, lang_code):
    """完整翻译一篇文章 - 翻译所有文本内容"""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 1. lang属性
        html = html.replace('<html lang="en">', f'<html lang="{lang_code}">')
        
        # 2. title
        title_match = re.search(r'<title>([^<]+)</title>', html)
        if title_match:
            original = title_match.group(1).replace(" - InsectAiSnap", "")
            translated = translate_text(original, lang_code)
            html = html.replace(title_match.group(0), f'<title>{translated} - InsectAiSnap</title>')
        
        # 3. hero-title
        hero_title_match = re.search(r'<h1 class="hero-title">([^<]+)</h1>', html)
        if hero_title_match:
            translated = translate_text(hero_title_match.group(1), lang_code)
            html = html.replace(hero_title_match.group(0), f'<h1 class="hero-title">{translated}</h1>')
        
        # 4. hero-subtitle
        hero_sub_match = re.search(r'<p class="hero-subtitle">([^<]+)</p>', html)
        if hero_sub_match:
            translated = translate_text(hero_sub_match.group(1), lang_code)
            html = html.replace(hero_sub_match.group(0), f'<p class="hero-subtitle">{translated}</p>')
        
        # 5. article-title
        article_title_match = re.search(r'<h2 class="article-title">([^<]+)</h2>', html)
        if article_title_match:
            translated = translate_text(article_title_match.group(1), lang_code)
            html = html.replace(article_title_match.group(0), f'<h2 class="article-title">{translated}</h2>')
        
        # 6. 所有section-title（h3）
        def translate_h3(match):
            text = match.group(1)
            if text and len(text.strip()) > 3:
                translated = translate_text(text, lang_code)
                return match.group(0).replace(text, translated)
            return match.group(0)
        
        html = re.sub(r'<h3 class="section-title">.*?<span.*?</span>\s*([^<]+)</h3>', 
                     translate_h3, html, flags=re.DOTALL)
        
        # 7. 翻译所有段落 - intro, 普通p, conclusion
        def translate_paragraph(match):
            class_attr = match.group(1) if match.group(1) else ''
            text = match.group(2).strip()
            
            # 跳过包含HTML标签的段落
            if '<' in text or len(text) < 10:
                return match.group(0)
            
            translated = translate_text(text, lang_code)
            return f'<p{class_attr}>{translated}</p>'
        
        # 翻译所有<p>标签
        html = re.sub(r'<p(\s+class="[^"]*")?>(.*?)</p>', translate_paragraph, html, flags=re.DOTALL)
        
        # 8. 翻译tip-title
        html = re.sub(
            r'<div class="tip-title">([^<]+)</div>',
            lambda m: f'<div class="tip-title">{translate_text(m.group(1), lang_code)}</div>',
            html
        )
        
        # 9. 翻译illustration-caption
        html = re.sub(
            r'<p class="illustration-caption">([^<]+)</p>',
            lambda m: f'<p class="illustration-caption">{translate_text(m.group(1), lang_code)}</p>',
            html
        )
        
        # 保存
        target_file.parent.mkdir(parents=True, exist_ok=True)
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return True, source_file.name
    
    except Exception as e:
        return False, f"{source_file.name}: {e}"

def process_article(args):
    """处理单篇文章"""
    source_file, target_file, lang_code, lang_name, idx, total = args
    
    success, msg = translate_article_complete(source_file, target_file, lang_code)
    
    with stats_lock:
        stats['total'] += 1
        if success:
            stats['success'] += 1
            status = "✅"
        else:
            stats['failed'] += 1
            status = "❌"
    
    safe_print(f"  [{lang_name}] [{idx}/{total}] {status} {source_file.name[:40]}")
    
    return success

def process_language_multithread(lang_code, lang_name, max_workers=8):
    """多线程处理一种语言"""
    safe_print(f"\n{'='*70}")
    safe_print(f"🚀 {lang_name} ({lang_code}) - {max_workers}线程完整翻译")
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
    print("🚀 完整多线程翻译 - DeepSeek API")
    print("=" * 80)
    print()
    print("⚙️  配置:")
    print("  - 线程数: 8个并发线程")
    print("  - API: DeepSeek")
    print("  - 模式: 完整翻译（所有段落内容）")
    print()
    
    start_time = time.time()
    
    for lang_code, lang_name in LANGUAGES.items():
        process_language_multithread(lang_code, lang_name, max_workers=8)
    
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

