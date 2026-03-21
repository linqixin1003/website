#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""完整翻译昆虫文章内容 - 包括正文段落"""

import re
import sys
import time
from pathlib import Path
from googletrans import Translator

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = ['de', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']

def translate_text(text, target_lang, translator, max_retries=3):
    """翻译文本"""
    lang_map = {
        'de': 'de', 'es': 'es', 'fr': 'fr', 'it': 'it',
        'ja': 'ja', 'ko': 'ko', 'pt': 'pt', 'ru': 'ru', 'zh': 'zh-cn'
    }
    
    for attempt in range(max_retries):
        try:
            if not text or len(text.strip()) < 3:
                return text
            
            result = translator.translate(text, dest=lang_map[target_lang], src='en')
            time.sleep(0.5)
            return result.text
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"    ⚠️  翻译失败: {text[:30]}...")
                return text
            time.sleep(2)
    return text

def translate_article_content(html_file, target_lang, translator):
    """翻译文章的所有内容"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 翻译所有<p>标签内的内容（不包括class属性）
        def translate_paragraph(match):
            tag_start = match.group(1)  # <p> 或 <p class="...">
            text = match.group(2)
            tag_end = match.group(3)
            
            # 跳过空段落
            if not text.strip():
                return match.group(0)
            
            # 翻译文本
            translated = translate_text(text, target_lang, translator)
            return f"{tag_start}{translated}{tag_end}"
        
        # 翻译普通段落
        content = re.sub(
            r'(<p(?:\s+class="[^"]*")?>)(.*?)(</p>)',
            translate_paragraph,
            content,
            flags=re.DOTALL
        )
        
        # 翻译h3标题（section-title中的文本）
        def translate_h3(match):
            before = match.group(1)
            text = match.group(2)
            after = match.group(3)
            
            if text.strip():
                translated = translate_text(text, target_lang, translator)
                return f"{before}{translated}{after}"
            return match.group(0)
        
        content = re.sub(
            r'(<h3[^>]*>.*?</span>\s*)(.*?)(</h3>)',
            translate_h3,
            content,
            flags=re.DOTALL
        )
        
        # 翻译illustration-caption
        def translate_caption(match):
            before = match.group(1)
            text = match.group(2)
            after = match.group(3)
            
            if text.strip():
                translated = translate_text(text, target_lang, translator)
                return f"{before}{translated}{after}"
            return match.group(0)
        
        content = re.sub(
            r'(<p class="illustration-caption">)(.*?)(</p>)',
            translate_caption,
            content
        )
        
        return content
        
    except Exception as e:
        print(f"    ❌ 错误: {e}")
        return None

def main():
    print("=" * 80)
    print("完整翻译昆虫文章内容（包括正文）")
    print("=" * 80)
    print("\n⚠️  警告：这将需要很长时间，建议使用专业翻译API")
    print("当前使用Google Translate免费版，可能有限制\n")
    
    translator = Translator()
    
    # 只处理中文作为示例
    lang_code = 'zh'
    print(f"\n开始翻译中文版本...")
    print(f"{'='*60}\n")
    
    source_dir = Path('insect/en')
    target_dir = Path(f'insect/{lang_code}')
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total = 0
    success = 0
    
    for category in categories:
        print(f"分类: {category}")
        source_cat = source_dir / category
        target_cat = target_dir / category
        
        if not source_cat.exists():
            continue
        
        # 只翻译前3篇作为示例
        articles = sorted([f for f in source_cat.glob('*.html') if f.name[0].isdigit()])[:3]
        
        for article in articles:
            total += 1
            print(f"  翻译: {article.name}...", end=' ')
            
            translated_content = translate_article_content(article, lang_code, translator)
            
            if translated_content:
                target_file = target_cat / article.name
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(translated_content)
                success += 1
                print("✅")
            else:
                print("❌")
            
            time.sleep(1)
    
    print(f"\n{'='*80}")
    print(f"示例翻译完成: {success}/{total} 篇")
    print(f"{'='*80}")
    print("\n💡 建议:")
    print("  1. 使用专业翻译服务(DeepL/Google Cloud Translation)")
    print("  2. 或保持正文英文，只翻译标题和关键词")
    print("  3. 英文正文是国际学术惯例")

if __name__ == '__main__':
    main()

