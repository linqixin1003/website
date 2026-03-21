#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量翻译 - 更高效的版本"""

import re
import sys
import time
from pathlib import Path
import requests

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def translate_batch(texts):
    """批量翻译多个文本"""
    if not texts:
        return []
    
    # 合并文本，用特殊分隔符
    combined = "\n###SPLIT###\n".join(texts)
    
    prompt = f"""请将以下英文文本翻译成中文（简体）。
每段文本用 ###SPLIT### 分隔。
请保持相同的分隔格式输出翻译结果。
只返回翻译，不要解释。

{combined}"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 8000
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content'].strip()
            translations = result.split('###SPLIT###')
            return [t.strip().strip('"\'') for t in translations]
    except Exception as e:
        print(f"      批量翻译错误: {e}")
    
    return texts

def translate_article_fast(source_file, target_file):
    """快速翻译整篇文章"""
    with open(source_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 修复lang属性
    html = html.replace('<html lang="en">', '<html lang="zh">')
    
    # 收集所有需要翻译的文本
    texts_to_translate = []
    positions = []
    
    # 1. title
    m = re.search(r'<title>([^<]+)</title>', html)
    if m:
        texts_to_translate.append(m.group(1).replace(' - InsectAiSnap', ''))
        positions.append(('title', m.group(0), m.group(1)))
    
    # 2. hero-title
    m = re.search(r'<h1 class="hero-title">([^<]+)</h1>', html)
    if m:
        texts_to_translate.append(m.group(1))
        positions.append(('hero-title', m.group(0), m.group(1)))
    
    # 3. hero-subtitle
    m = re.search(r'<p class="hero-subtitle">([^<]+)</p>', html)
    if m:
        texts_to_translate.append(m.group(1))
        positions.append(('hero-subtitle', m.group(0), m.group(1)))
    
    # 4. article-title
    m = re.search(r'<h2 class="article-title">([^<]+)</h2>', html)
    if m:
        texts_to_translate.append(m.group(1))
        positions.append(('article-title', m.group(0), m.group(1)))
    
    # 5. 所有段落
    for m in re.finditer(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', html, re.DOTALL):
        text = m.group(1).strip()
        if text and '<' not in text and len(text) > 10:
            texts_to_translate.append(text)
            positions.append(('paragraph', m.group(0), text))
    
    # 6. section-title
    for m in re.finditer(r'<h3[^>]*>.*?</span>\s*([^<]+)</h3>', html, re.DOTALL):
        text = m.group(1).strip()
        if text:
            texts_to_translate.append(text)
            positions.append(('section-title', m.group(0), text))
    
    # 7. illustration-caption
    for m in re.finditer(r'<p class="illustration-caption">([^<]+)</p>', html):
        text = m.group(1).strip()
        if text:
            texts_to_translate.append(text)
            positions.append(('caption', m.group(0), text))
    
    # 8. tip-title
    m = re.search(r'<div class="tip-title">([^<]+)</div>', html)
    if m:
        texts_to_translate.append(m.group(1))
        positions.append(('tip-title', m.group(0), m.group(1)))
    
    print(f"      收集了 {len(texts_to_translate)} 个文本")
    
    # 批量翻译（每次10个）
    all_translations = []
    batch_size = 10
    
    for i in range(0, len(texts_to_translate), batch_size):
        batch = texts_to_translate[i:i+batch_size]
        print(f"      翻译批次 {i//batch_size + 1}... ", end='')
        translations = translate_batch(batch)
        all_translations.extend(translations)
        print(f"✅ ({len(translations)}个)")
        time.sleep(2)
    
    # 替换翻译
    for i, (pos_type, full_match, original_text) in enumerate(positions):
        if i < len(all_translations):
            translated = all_translations[i]
            html = html.replace(full_match, full_match.replace(original_text, translated), 1)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"      ✅ 保存完成\n")

def main():
    print("=" * 80)
    print("DeepSeek API - 批量快速翻译")
    print("=" * 80)
    print()
    
    source_dir = Path('insect/en')
    target_dir = Path('insect/zh')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    
    for category in categories:
        source_cat = source_dir / category
        target_cat = target_dir / category
        
        if not source_cat.exists():
            continue
        
        print(f"\n📁 {category}")
        print("-" * 60)
        
        for article in sorted(source_cat.glob('*.html')):
            if not article.name[0].isdigit():
                continue
            
            total += 1
            print(f"\n  [{total}/50] {article.name}")
            
            try:
                translate_article_fast(article, target_cat / article.name)
            except Exception as e:
                print(f"      ❌ 错误: {e}")
                import traceback
                traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("✅ 翻译完成！")
    print("=" * 80)

if __name__ == '__main__':
    main()


