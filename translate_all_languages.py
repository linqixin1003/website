#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用DeepSeek API翻译所有语言"""

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

LANGUAGES = {
    'de': 'German (Deutsch)',
    'es': 'Spanish (Español)',
    'fr': 'French (Français)',
    'it': 'Italian (Italiano)',
    'ja': 'Japanese (日本語)',
    'ko': 'Korean (한국어)',
    'pt': 'Portuguese (Português)',
    'ru': 'Russian (Русский)'
}

def translate_text(text, target_lang, max_retries=2):
    """翻译单个文本到目标语言"""
    if not text or len(text.strip()) < 3:
        return text
    
    # 如果已经是目标语言，直接返回
    if target_lang == 'zh' and re.search(r'[\u4e00-\u9fff]{5,}', text):
        return text
    
    lang_name = LANGUAGES.get(target_lang, target_lang)
    
    prompt = f"""Translate the following English text to {lang_name}.
Only provide the translation, no explanations.
Keep the professional and scientific tone.

English text:
{text}

Translation:"""
    
    for attempt in range(max_retries):
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
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()['choices'][0]['message']['content'].strip()
                return result.strip('"\'')
            else:
                print(f" [API错误{response.status_code}]", end='')
                time.sleep(1)
        except Exception as e:
            print(f" [错误]", end='')
            time.sleep(1)
    
    return text

def translate_article(source_file, target_file, target_lang):
    """翻译整篇文章到目标语言"""
    with open(source_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. lang属性
    html = html.replace('<html lang="en">', f'<html lang="{target_lang}">')
    
    # 2. title
    title_match = re.search(r'<title>([^<]+)</title>', html)
    if title_match:
        english_title = title_match.group(1).replace(' - InsectAiSnap', '')
        translated_title = translate_text(english_title, target_lang)
        html = html.replace(
            f'<title>{title_match.group(1)}</title>',
            f'<title>{translated_title} - InsectAiSnap</title>'
        )
    
    # 3. hero-title
    hero_match = re.search(r'<h1 class="hero-title">([^<]+)</h1>', html)
    if hero_match:
        translated = translate_text(hero_match.group(1), target_lang)
        html = html.replace(
            f'<h1 class="hero-title">{hero_match.group(1)}</h1>',
            f'<h1 class="hero-title">{translated}</h1>'
        )
    
    # 4. hero-subtitle
    subtitle_match = re.search(r'<p class="hero-subtitle">([^<]+)</p>', html)
    if subtitle_match:
        translated = translate_text(subtitle_match.group(1), target_lang)
        html = html.replace(
            f'<p class="hero-subtitle">{subtitle_match.group(1)}</p>',
            f'<p class="hero-subtitle">{translated}</p>'
        )
    
    # 5. article-title
    article_match = re.search(r'<h2 class="article-title">([^<]+)</h2>', html)
    if article_match:
        translated = translate_text(article_match.group(1), target_lang)
        html = html.replace(
            f'<h2 class="article-title">{article_match.group(1)}</h2>',
            f'<h2 class="article-title">{translated}</h2>'
        )
    
    # 6. 所有段落
    paragraphs = list(re.finditer(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', html, re.DOTALL))
    for i, match in enumerate(paragraphs):
        text = match.group(1).strip()
        if text and '<img' not in text and '<a' not in text and len(text) > 10:
            translated = translate_text(text, target_lang)
            html = html.replace(match.group(0), match.group(0).replace(text, translated), 1)
            if i % 3 == 0:
                print('.', end='', flush=True)
                time.sleep(0.3)
    
    # 7. section-title
    for match in re.finditer(r'(<h3[^>]*>.*?</span>\s*)([^<]+)(</h3>)', html, re.DOTALL):
        text = match.group(2).strip()
        if text:
            translated = translate_text(text, target_lang)
            html = html.replace(match.group(0), f"{match.group(1)}{translated}{match.group(3)}", 1)
    
    # 8. illustration-caption
    for match in re.finditer(r'(<p class="illustration-caption">)([^<]+)(</p>)', html):
        text = match.group(2).strip()
        if text:
            translated = translate_text(text, target_lang)
            html = html.replace(match.group(0), f"{match.group(1)}{translated}{match.group(3)}", 1)
    
    # 9. tip-title
    tip_match = re.search(r'(<div class="tip-title">)([^<]+)(</div>)', html)
    if tip_match:
        translated = translate_text(tip_match.group(2), target_lang)
        html = html.replace(tip_match.group(0), f"{tip_match.group(1)}{translated}{tip_match.group(3)}")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print("=" * 80)
    print("DeepSeek API - 多语言翻译系统")
    print("=" * 80)
    print()
    
    # 显示待翻译的语言
    print("将翻译到以下语言:")
    for code, name in LANGUAGES.items():
        print(f"  • {code}: {name}")
    print()
    
    source_dir = Path('insect/en')
    categories = [
        'basics-identification',
        'ecology-environment',
        'beneficial-pollinators',
        'pest-management',
        'behavior-evolution'
    ]
    
    # 获取所有文章列表
    all_articles = []
    for category in categories:
        source_cat = source_dir / category
        if source_cat.exists():
            articles = sorted([f for f in source_cat.glob('*.html') if f.name[0].isdigit()])
            all_articles.extend([(category, article) for article in articles])
    
    print(f"总计: {len(all_articles)} 篇文章")
    print(f"语言数: {len(LANGUAGES)} 种")
    print(f"总任务: {len(all_articles) * len(LANGUAGES)} 篇文章翻译")
    print()
    
    # 逐语言翻译
    for lang_code, lang_name in LANGUAGES.items():
        print(f"\n{'='*80}")
        print(f"开始翻译: {lang_name} ({lang_code})")
        print(f"{'='*80}\n")
        
        target_dir = Path(f'insect/{lang_code}')
        
        success = 0
        total = 0
        
        for category, article in all_articles:
            total += 1
            target_cat = target_dir / category
            target_file = target_cat / article.name
            
            print(f"[{total}/{len(all_articles)}] {article.name[:45]}... ", end='', flush=True)
            
            try:
                translate_article(article, target_file, lang_code)
                success += 1
                print(" ✅")
            except Exception as e:
                print(f" ❌ {e}")
            
            time.sleep(1)
        
        print(f"\n{lang_name} 完成: {success}/{total} 篇")
        print(f"成功率: {success*100//total}%")
    
    print("\n" + "=" * 80)
    print("🎉 所有语言翻译完成！")
    print("=" * 80)
    print()
    print("翻译统计:")
    print(f"  • 语言数: {len(LANGUAGES)} 种")
    print(f"  • 文章数: {len(all_articles)} 篇/语言")
    print(f"  • 总翻译: {len(all_articles) * len(LANGUAGES)} 篇")
    print()

if __name__ == '__main__':
    main()

