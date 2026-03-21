#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""终极翻译 - 一次性完成所有剩余翻译"""

import re
import sys
import time
from pathlib import Path
import requests
import json

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def translate_text(text, max_retries=2):
    """翻译单个文本"""
    if not text or len(text.strip()) < 3:
        return text
    
    # 如果已经是中文，直接返回
    if re.search(r'[\u4e00-\u9fff]{5,}', text):
        return text
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": f"请将以下英文翻译成中文，只返回翻译结果：\n\n{text}"}],
                    "temperature": 0.3,
                    "max_tokens": 4000
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()['choices'][0]['message']['content'].strip()
                return result.strip('"\'')
            else:
                print(f" [API错误{response.status_code}]", end='')
                time.sleep(1)
        except Exception as e:
            print(f" [错误:{e}]", end='')
            time.sleep(1)
    
    return text

def translate_full_article(source_file, target_file):
    """完整翻译一篇文章"""
    with open(source_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. lang属性
    html = html.replace('<html lang="en">', '<html lang="zh">')
    
    # 2. title
    html = re.sub(
        r'<title>([^<]+)</title>',
        lambda m: f'<title>{translate_text(m.group(1).replace(" - InsectAiSnap", ""))} - InsectAiSnap</title>',
        html
    )
    
    # 3. hero-title
    html = re.sub(
        r'<h1 class="hero-title">([^<]+)</h1>',
        lambda m: f'<h1 class="hero-title">{translate_text(m.group(1))}</h1>',
        html
    )
    
    # 4. hero-subtitle
    html = re.sub(
        r'<p class="hero-subtitle">([^<]+)</p>',
        lambda m: f'<p class="hero-subtitle">{translate_text(m.group(1))}</p>',
        html
    )
    
    # 5. article-title
    html = re.sub(
        r'<h2 class="article-title">([^<]+)</h2>',
        lambda m: f'<h2 class="article-title">{translate_text(m.group(1))}</h2>',
        html
    )
    
    # 6. 所有段落（分批翻译）
    paragraphs = list(re.finditer(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', html, re.DOTALL))
    for i, match in enumerate(paragraphs):
        text = match.group(1).strip()
        if text and '<img' not in text and '<a' not in text:
            translated = translate_text(text)
            html = html.replace(match.group(0), match.group(0).replace(text, translated), 1)
            if i % 3 == 0:
                print('.', end='', flush=True)
                time.sleep(0.3)
    
    # 7. section-title
    html = re.sub(
        r'(<h3[^>]*>.*?</span>\s*)([^<]+)(</h3>)',
        lambda m: f"{m.group(1)}{translate_text(m.group(2).strip())}{m.group(3)}",
        html,
        flags=re.DOTALL
    )
    
    # 8. illustration-caption
    html = re.sub(
        r'(<p class="illustration-caption">)([^<]+)(</p>)',
        lambda m: f"{m.group(1)}{translate_text(m.group(2))}{m.group(3)}",
        html
    )
    
    # 9. tip-title
    html = re.sub(
        r'(<div class="tip-title">)([^<]+)(</div>)',
        lambda m: f"{m.group(1)}{translate_text(m.group(2))}{m.group(3)}",
        html
    )
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print("=" * 80)
    print("终极翻译 - DeepSeek API")
    print("=" * 80)
    print()
    
    source_dir = Path('insect/en')
    target_dir = Path('insect/zh')
    
    categories = [
        'basics-identification',
        'ecology-environment',
        'beneficial-pollinators',
        'pest-management',
        'behavior-evolution'
    ]
    
    total = 0
    success = 0
    
    for category in categories:
        source_cat = source_dir / category
        target_cat = target_dir / category
        
        if not source_cat.exists():
            continue
        
        print(f"\n📁 {category}")
        print("-" * 60)
        
        articles = sorted([f for f in source_cat.glob('*.html') if f.name[0].isdigit()])
        
        for article in articles:
            total += 1
            print(f"\n[{total}/50] {article.name[:40]}... ", end='', flush=True)
            
            try:
                translate_full_article(article, target_cat / article.name)
                success += 1
                print(" ✅")
            except Exception as e:
                print(f" ❌ {e}")
            
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print(f"✅ 翻译完成: {success}/{total} 篇")
    print("=" * 80)

if __name__ == '__main__':
    main()

