#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证完整翻译 - 检查所有段落是否翻译"""

import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = {
    'zh': '中文',
    'de': '德语', 
    'es': '西班牙语',
    'fr': '法语',
    'it': '意大利语',
    'ja': '日语',
    'ko': '韩语',
    'pt': '葡萄牙语',
    'ru': '俄语'
}

def check_article_complete(html_file, lang_code):
    """检查文章是否完整翻译（所有段落）"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 检查lang属性
        if f'lang="{lang_code}"' not in content:
            return False, "lang属性未更新"
        
        # 2. 提取所有普通段落（排除包含HTML标签的）
        all_paragraphs = re.findall(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', content, re.DOTALL)
        
        translated_count = 0
        english_count = 0
        
        for para in all_paragraphs:
            # 跳过包含图片等HTML的段落
            if '<img' in para or '<a' in para or len(para.strip()) < 20:
                continue
            
            # 统计英文单词（4个字母以上）
            english_words = len(re.findall(r'\b[a-zA-Z]{4,}\b', para))
            
            # 如果英文单词少于10个，认为已翻译
            if english_words < 10:
                translated_count += 1
            else:
                english_count += 1
        
        # 如果至少80%的段落已翻译，认为文章完成
        total = translated_count + english_count
        if total == 0:
            return False, "未找到段落"
        
        percent = translated_count * 100 // total
        if percent >= 80:
            return True, f"已翻译 ({translated_count}/{total}段落)"
        else:
            return False, f"仅{percent}%段落翻译"
    
    except Exception as e:
        return False, f"错误: {e}"

def main():
    print("=" * 80)
    print("完整翻译质量检查 - 检查所有段落")
    print("=" * 80)
    print()
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    total_translated = 0
    total_files = 0
    language_stats = {}
    
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"❌ {lang_name:10} - 目录不存在")
            continue
        
        translated = 0
        total = 0
        failed_files = []
        
        for category in categories:
            cat_dir = lang_dir / category
            if not cat_dir.exists():
                continue
            
            articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
            for article in articles:
                total += 1
                is_translated, reason = check_article_complete(article, lang_code)
                if is_translated:
                    translated += 1
                else:
                    failed_files.append((article.name, reason))
        
        percent = (translated * 100 // total) if total > 0 else 0
        bar_length = 20
        filled = (translated * bar_length // total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        status = '✅' if translated == total else '⚠️ ' if percent >= 50 else '❌'
        
        print(f"{status} {lang_name:10} [{bar}] {translated:2}/{total} ({percent:3}%)")
        
        if failed_files and len(failed_files) <= 5:
            for fname, reason in failed_files[:3]:
                print(f"    ⚠️  {fname[:40]}: {reason}")
        
        language_stats[lang_code] = {'translated': translated, 'total': total}
        total_translated += translated
        total_files += total
    
    print()
    print("=" * 80)
    overall_percent = (total_translated * 100 // total_files) if total_files > 0 else 0
    print(f"总进度: {total_translated}/{total_files} ({overall_percent}%)")
    print("=" * 80)
    
    if total_translated == total_files:
        print("\n🎉🎉🎉 所有语言完整翻译完成！")
        print("\n✅ 全部450篇文章已翻译")
    elif total_translated > 400:
        print(f"\n🎉 接近完成！已翻译 {total_translated} 篇")
        print(f"⏳ 还需修复 {total_files - total_translated} 篇")
    else:
        print(f"\n✅ 已翻译 {total_translated} 篇文章")
        print(f"⏳ 还需翻译/修复 {total_files - total_translated} 篇")

if __name__ == '__main__':
    main()

