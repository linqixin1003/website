#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完整翻译中文版 - 包括所有元素"""

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

def translate(text):
    """翻译为中文"""
    if not text or len(text.strip()) < 2:
        return text
    
    prompt = f"请将以下英文翻译成中文，只返回翻译结果：\n\n{text}"
    
    try:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3},
            timeout=30
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip().strip('"\'')
    except:
        pass
    return text

def translate_article_complete(source_file, target_file):
    """完整翻译文章"""
    print(f"    读取: {source_file.name}")
    
    with open(source_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. 修复lang属性
    html = html.replace('<html lang="en">', '<html lang="zh">')
    
    # 2. 翻译title
    html = re.sub(r'<title>([^<]+)</title>', 
                  lambda m: f'<title>{translate(m.group(1).replace(" - InsectAiSnap", ""))} - InsectAiSnap</title>', html)
    print(f"      ✅ 标题")
    
    # 3. 翻译hero-title
    html = re.sub(r'<h1 class="hero-title">([^<]+)</h1>',
                  lambda m: f'<h1 class="hero-title">{translate(m.group(1))}</h1>', html)
    
    # 4. 翻译hero-subtitle  
    html = re.sub(r'<p class="hero-subtitle">([^<]+)</p>',
                  lambda m: f'<p class="hero-subtitle">{translate(m.group(1))}</p>', html)
    print(f"      ✅ Hero区域")
    
    # 5. 翻译article-title
    html = re.sub(r'<h2 class="article-title">([^<]+)</h2>',
                  lambda m: f'<h2 class="article-title">{translate(m.group(1))}</h2>', html)
    
    # 6. 翻译所有段落
    para_count = 0
    def trans_para(m):
        nonlocal para_count
        para_count += 1
        text = m.group(2).strip()
        if text and '<' not in text:
            translated = translate(text)
            time.sleep(0.5)
            return f"{m.group(1)}{translated}{m.group(3)}"
        return m.group(0)
    
    html = re.sub(r'(<p(?:\s+class="[^"]*")?>)(.*?)(</p>)', trans_para, html, flags=re.DOTALL)
    print(f"      ✅ {para_count}个段落")
    
    # 7. 翻译section-title
    html = re.sub(r'(<h3[^>]*>.*?</span>\s*)([^<]+)(</h3>)',
                  lambda m: f"{m.group(1)}{translate(m.group(2).strip())}{m.group(3)}", html, flags=re.DOTALL)
    print(f"      ✅ 小节标题")
    
    # 8. 翻译illustration-caption
    html = re.sub(r'(<p class="illustration-caption">)([^<]+)(</p>)',
                  lambda m: f"{m.group(1)}{translate(m.group(2))}{m.group(3)}", html)
    
    # 9. 翻译tip-title
    html = re.sub(r'(<div class="tip-title">)([^<]+)(</div>)',
                  lambda m: f"{m.group(1)}{translate(m.group(2))}{m.group(3)}", html)
    print(f"      ✅ 提示框")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"      💾 保存完成\n")

def main():
    print("=" * 80)
    print("DeepSeek API - 完整翻译中文版")
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
                translate_article_complete(article, target_cat / article.name)
            except Exception as e:
                print(f"      ❌ 错误: {e}")
            
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print("✅ 翻译完成！")
    print("=" * 80)

if __name__ == '__main__':
    main()


