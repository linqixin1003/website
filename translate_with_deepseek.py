#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用DeepSeek API完整翻译昆虫文章"""

import re
import sys
import time
import json
from pathlib import Path
import requests

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# DeepSeek API配置
DEEPSEEK_API_KEY = "sk-74142abf4d524e739abea8868b319adb"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

LANGUAGES = {
    'de': 'German',
    'es': 'Spanish', 
    'fr': 'French',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh': 'Chinese'
}

def translate_with_deepseek(text, target_language, max_retries=3):
    """使用DeepSeek API翻译文本"""
    
    if not text or len(text.strip()) < 3:
        return text
    
    prompt = f"""Translate the following English text to {target_language}. 
Only provide the translation, no explanations or additional text.
Keep the same tone and style.

Text to translate:
{text}

Translation:"""

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                translated_text = result['choices'][0]['message']['content'].strip()
                # 清理可能的引号
                translated_text = translated_text.strip('"\'')
                return translated_text
            else:
                print(f"      API错误 {response.status_code}: {response.text[:100]}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                    
        except Exception as e:
            print(f"      翻译错误: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
    
    return text  # 失败则返回原文

def extract_translatable_parts(content):
    """提取需要翻译的部分"""
    parts = []
    
    # 提取所有段落文本
    for match in re.finditer(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', content, re.DOTALL):
        text = match.group(1).strip()
        if text and not text.startswith('<'):  # 不包含HTML标签的纯文本
            parts.append({
                'type': 'paragraph',
                'text': text,
                'full_match': match.group(0)
            })
    
    # 提取section-title中的文本
    for match in re.finditer(r'(<h3[^>]*>.*?</span>\s*)(.*?)(</h3>)', content, re.DOTALL):
        text = match.group(2).strip()
        if text:
            parts.append({
                'type': 'section-title',
                'text': text,
                'before': match.group(1),
                'after': match.group(3),
                'full_match': match.group(0)
            })
    
    # 提取图片说明
    for match in re.finditer(r'(<p class="illustration-caption">)(.*?)(</p>)', content):
        text = match.group(2).strip()
        if text:
            parts.append({
                'type': 'caption',
                'text': text,
                'before': match.group(1),
                'after': match.group(3),
                'full_match': match.group(0)
            })
    
    return parts

def translate_article(html_file, target_lang):
    """翻译整篇文章"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"      提取文本...", end=' ')
        parts = extract_translatable_parts(content)
        print(f"找到 {len(parts)} 个部分")
        
        translated_content = content
        translations = {}
        
        # 批量翻译
        for i, part in enumerate(parts, 1):
            print(f"      翻译 {i}/{len(parts)}: {part['text'][:40]}...", end=' ')
            
            translated_text = translate_with_deepseek(part['text'], LANGUAGES[target_lang])
            translations[part['full_match']] = translated_text
            
            print("✅")
            time.sleep(0.5)  # 避免API限流
        
        # 替换翻译内容
        for original, translation in translations.items():
            # 根据类型构建替换文本
            if '<p' in original:
                # 段落
                new_text = re.sub(r'(<p(?:\s+class="[^"]*")?>)(.*?)(</p>)', 
                                 rf'\1{translation}\3', original, flags=re.DOTALL)
            elif '<h3' in original:
                # 标题
                new_text = re.sub(r'(</span>\s*)(.*?)(</h3>)', 
                                 rf'\1{translation}\3', original, flags=re.DOTALL)
            else:
                new_text = original.replace(original, translation)
            
            translated_content = translated_content.replace(original, new_text, 1)
        
        return translated_content
        
    except Exception as e:
        print(f"      ❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    print("=" * 80)
    print("使用DeepSeek API翻译昆虫文章")
    print("=" * 80)
    print(f"API密钥: {DEEPSEEK_API_KEY[:20]}...")
    print()
    
    # 测试API连接
    print("测试API连接...")
    test_result = translate_with_deepseek("Hello, world!", "Chinese")
    if test_result and test_result != "Hello, world!":
        print(f"✅ API连接成功: {test_result}")
    else:
        print("❌ API连接失败，请检查密钥")
        return
    
    print()
    
    source_dir = Path('insect/en')
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    # 询问要翻译的语言
    print("选择要翻译的语言:")
    print("1. 仅中文 (zh)")
    print("2. 所有语言 (de, es, fr, it, ja, ko, pt, ru, zh)")
    print("3. 自定义")
    
    choice = input("\n请选择 (1/2/3): ").strip()
    
    if choice == '1':
        target_langs = ['zh']
    elif choice == '2':
        target_langs = list(LANGUAGES.keys())
    else:
        lang_input = input("输入语言代码 (用逗号分隔，如: zh,ja,ko): ").strip()
        target_langs = [l.strip() for l in lang_input.split(',') if l.strip() in LANGUAGES]
    
    if not target_langs:
        print("❌ 未选择有效语言")
        return
    
    print(f"\n将翻译到: {', '.join(target_langs)}")
    confirm = input("继续? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("已取消")
        return
    
    print("\n" + "=" * 80)
    
    for lang_code in target_langs:
        print(f"\n{'='*60}")
        print(f"翻译到 {LANGUAGES[lang_code]} ({lang_code})")
        print(f"{'='*60}\n")
        
        target_dir = Path(f'insect/{lang_code}')
        total = 0
        success = 0
        
        for category in categories:
            source_cat = source_dir / category
            target_cat = target_dir / category
            
            if not source_cat.exists():
                continue
            
            print(f"  分类: {category}")
            
            articles = sorted([f for f in source_cat.glob('*.html') if f.name[0].isdigit()])
            
            for article in articles:
                total += 1
                print(f"    [{total}] {article.name}")
                
                translated_content = translate_article(article, lang_code)
                
                if translated_content:
                    target_file = target_cat / article.name
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(translated_content)
                    success += 1
                    print(f"    ✅ 已保存")
                else:
                    print(f"    ❌ 翻译失败")
                
                time.sleep(1)
        
        print(f"\n  {LANGUAGES[lang_code]} 完成: {success}/{total} 篇")
    
    print("\n" + "=" * 80)
    print("翻译完成！")
    print("=" * 80)

if __name__ == '__main__':
    main()


