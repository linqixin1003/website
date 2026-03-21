#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用DeepSeek API翻译中文版昆虫文章"""

import re
import sys
import time
from pathlib import Path
import requests

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DEEPSEEK_API_KEY = "sk-74142abf4d524e739abea8868b319adb"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def translate_with_deepseek(text):
    """使用DeepSeek翻译为中文"""
    if not text or len(text.strip()) < 3:
        return text
    
    prompt = f"""Please translate the following English text to Chinese (Simplified).
Only provide the translation without any explanations.
Keep the professional and scientific tone.

English text:
{text}

Chinese translation:"""

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 3000
    }
    
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            translated = result['choices'][0]['message']['content'].strip()
            return translated.strip('"\'')
        else:
            print(f"        API错误: {response.status_code}")
            return text
    except Exception as e:
        print(f"        翻译错误: {e}")
        return text

def translate_article(source_file, target_file):
    """翻译整篇文章"""
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻译所有<p>段落
    def translate_p(match):
        tag_open = match.group(1)
        text = match.group(2)
        tag_close = match.group(3)
        
        if not text.strip() or '<' in text:
            return match.group(0)
        
        print(f"        段落: {text[:50]}...")
        translated = translate_with_deepseek(text)
        time.sleep(0.5)
        return f"{tag_open}{translated}{tag_close}"
    
    content = re.sub(r'(<p(?:\s+class="[^"]*")?>)(.*?)(</p>)', translate_p, content, flags=re.DOTALL)
    
    # 翻译h3标题
    def translate_h3(match):
        before = match.group(1)
        text = match.group(2)
        after = match.group(3)
        
        if not text.strip():
            return match.group(0)
        
        print(f"        标题: {text}")
        translated = translate_with_deepseek(text)
        time.sleep(0.5)
        return f"{before}{translated}{after}"
    
    content = re.sub(r'(<h3[^>]*>.*?</span>\s*)(.*?)(</h3>)', translate_h3, content, flags=re.DOTALL)
    
    # 翻译图片说明
    def translate_caption(match):
        before = match.group(1)
        text = match.group(2)
        after = match.group(3)
        
        if not text.strip():
            return match.group(0)
        
        print(f"        图片说明: {text}")
        translated = translate_with_deepseek(text)
        time.sleep(0.5)
        return f"{before}{translated}{after}"
    
    content = re.sub(r'(<p class="illustration-caption">)(.*?)(</p>)', translate_caption, content)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=" * 80)
    print("使用DeepSeek API翻译中文昆虫文章")
    print("=" * 80)
    print()
    
    source_dir = Path('insect/en')
    target_dir = Path('insect/zh')
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    success = 0
    
    for category in categories:
        source_cat = source_dir / category
        target_cat = target_dir / category
        
        if not source_cat.exists():
            continue
        
        print(f"\n分类: {category}")
        print("-" * 60)
        
        articles = sorted([f for f in source_cat.glob('*.html') if f.name[0].isdigit()])
        
        for article in articles:
            total += 1
            print(f"\n  [{total}/50] {article.name}")
            
            source_file = article
            target_file = target_cat / article.name
            
            try:
                translate_article(source_file, target_file)
                success += 1
                print(f"      ✅ 完成")
            except Exception as e:
                print(f"      ❌ 错误: {e}")
            
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print(f"翻译完成: {success}/{total} 篇")
    print("=" * 80)

if __name__ == '__main__':
    main()


