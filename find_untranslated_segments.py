#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""找出所有包含未翻译内容的文章"""

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

def has_untranslated_content(html_content):
    """检查是否有未翻译的大段英文内容"""
    # 提取所有段落
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html_content, re.DOTALL)
    
    untranslated_paras = []
    
    for i, para in enumerate(paragraphs):
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', para).strip()
        
        # 跳过太短的
        if len(text) < 50:
            continue
        
        # 检查是否包含大量英文内容（特别是列表项）
        # 检测常见英文词
        english_patterns = [
            r'\b(the|and|are|that|with|this|from|have|they|which|their|for)\b',
            r'<li><strong>[A-Z][a-z]+:?</strong>',  # 列表项
            r'\bpollinator|beetle|insect|species|flower|plant\b'  # 专业术语
        ]
        
        english_matches = sum(len(re.findall(pattern, text, re.IGNORECASE)) 
                             for pattern in english_patterns)
        
        # 如果有超过10个英文特征，认为未翻译
        if english_matches >= 10:
            untranslated_paras.append({
                'index': i + 1,
                'content': text[:150] + '...',
                'english_count': english_matches
            })
    
    return untranslated_paras

def check_all_articles():
    """检查所有文章"""
    print("=" * 80)
    print("🔍 查找未翻译段落")
    print("=" * 80)
    print()
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    all_issues = {}
    
    for lang_code, lang_name in LANGUAGES.items():
        print(f"\n{'='*70}")
        print(f"📊 检查 {lang_name} ({lang_code})")
        print(f"{'='*70}\n")
        
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"  ❌ 目录不存在")
            continue
        
        issues_in_lang = []
        
        for category in categories:
            cat_dir = lang_dir / category
            if not cat_dir.exists():
                continue
            
            articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
            
            for article in articles:
                try:
                    with open(article, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    untranslated = has_untranslated_content(content)
                    
                    if untranslated:
                        rel_path = f"{category}/{article.name}"
                        issues_in_lang.append({
                            'file': rel_path,
                            'paragraphs': untranslated
                        })
                        
                        print(f"  ⚠️  {rel_path}")
                        for para in untranslated[:2]:  # 只显示前2个问题段落
                            print(f"      段落 {para['index']}: {para['content'][:80]}...")
                
                except Exception as e:
                    print(f"  ❌ {article.name}: {e}")
        
        if issues_in_lang:
            all_issues[lang_code] = issues_in_lang
            print(f"\n  📊 {lang_name}: 发现 {len(issues_in_lang)} 篇文章有未翻译内容")
        else:
            print(f"\n  ✅ {lang_name}: 所有文章翻译完整")
    
    # 总结
    print("\n" + "=" * 80)
    print("📊 总结")
    print("=" * 80)
    
    total_issues = sum(len(issues) for issues in all_issues.values())
    
    if total_issues == 0:
        print("\n🎉 所有语言翻译完整！")
    else:
        print(f"\n⚠️  发现 {total_issues} 篇文章需要修复:")
        print()
        for lang_code, issues in sorted(all_issues.items()):
            lang_name = LANGUAGES[lang_code]
            print(f"  {lang_name} ({lang_code}): {len(issues)} 篇")
            
            # 保存到文件
            output_file = f"fix_list_{lang_code}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                for issue in issues:
                    f.write(f"{issue['file']}\n")
            
            print(f"    → 列表已保存到 {output_file}")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    check_all_articles()

