#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""详细的翻译完整性和准确率检查"""

import re
import sys
from pathlib import Path
import random

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = {
    'zh': {'name': '中文', 'sample_chars': '的是在有', 'english_threshold': 15},
    'de': {'name': '德语', 'sample_chars': 'der die das und', 'english_threshold': 20},
    'es': {'name': '西班牙语', 'sample_chars': 'el la los las', 'english_threshold': 20},
    'fr': {'name': '法语', 'sample_chars': 'le la les de', 'english_threshold': 20},
    'it': {'name': '意大利语', 'sample_chars': 'il la gli le', 'english_threshold': 20},
    'ja': {'name': '日语', 'sample_chars': 'のはをに', 'english_threshold': 15},
    'ko': {'name': '韩语', 'sample_chars': '이가을는', 'english_threshold': 15},
    'pt': {'name': '葡萄牙语', 'sample_chars': 'o a os as', 'english_threshold': 20},
    'ru': {'name': '俄语', 'sample_chars': 'в и на с', 'english_threshold': 15}
}

def extract_text_content(html_content):
    """提取HTML中的文本内容"""
    # 提取所有可翻译的文本
    texts = {
        'title': '',
        'hero_title': '',
        'hero_subtitle': '',
        'article_title': '',
        'intro': '',
        'paragraphs': [],
        'section_titles': [],
        'captions': [],
        'tips': []
    }
    
    # Title
    title_match = re.search(r'<title>([^<]+)</title>', html_content)
    if title_match:
        texts['title'] = title_match.group(1).replace(' - InsectAiSnap', '').strip()
    
    # Hero title
    hero_title_match = re.search(r'<h1 class="hero-title">([^<]+)</h1>', html_content)
    if hero_title_match:
        texts['hero_title'] = hero_title_match.group(1).strip()
    
    # Hero subtitle
    hero_sub_match = re.search(r'<p class="hero-subtitle">([^<]+)</p>', html_content)
    if hero_sub_match:
        texts['hero_subtitle'] = hero_sub_match.group(1).strip()
    
    # Article title
    article_title_match = re.search(r'<h2 class="article-title">([^<]+)</h2>', html_content)
    if article_title_match:
        texts['article_title'] = article_title_match.group(1).strip()
    
    # Intro paragraph
    intro_match = re.search(r'<p class="intro">([^<]+)', html_content)
    if intro_match:
        texts['intro'] = intro_match.group(1).strip()
    
    # All paragraphs
    paragraphs = re.findall(r'<p(?:\s+class="[^"]*")?>(.*?)</p>', html_content, re.DOTALL)
    for para in paragraphs:
        para_text = re.sub(r'<[^>]+>', '', para).strip()
        if para_text and len(para_text) > 20 and '<' not in para_text:
            texts['paragraphs'].append(para_text)
    
    # Section titles
    section_titles = re.findall(r'<h3 class="section-title">.*?<span.*?</span>\s*([^<]+)</h3>', 
                                html_content, re.DOTALL)
    texts['section_titles'] = [s.strip() for s in section_titles if s.strip()]
    
    # Captions
    captions = re.findall(r'<p class="illustration-caption">([^<]+)</p>', html_content)
    texts['captions'] = [c.strip() for c in captions if c.strip()]
    
    # Tips
    tips = re.findall(r'<div class="tip-title">([^<]+)</div>', html_content)
    texts['tips'] = [t.strip() for t in tips if t.strip()]
    
    return texts

def detect_language_quality(text, lang_code):
    """检测文本是否是目标语言"""
    if not text or len(text) < 10:
        return True, "文本太短"
    
    # 统计英文单词（常见词）
    common_english = ['the', 'and', 'are', 'that', 'with', 'this', 'from', 'have', 
                      'they', 'which', 'their', 'will', 'when', 'what', 'there',
                      'about', 'more', 'other', 'such', 'into', 'through']
    
    english_count = sum(1 for word in common_english 
                       if re.search(r'\b' + word + r'\b', text.lower()))
    
    lang_info = LANGUAGES[lang_code]
    threshold = lang_info['english_threshold']
    
    # 对于欧洲语言，降低阈值（因为它们使用拉丁字母）
    if lang_code in ['de', 'es', 'fr', 'it', 'pt']:
        # 检查特定语言的特征词
        has_lang_features = any(char in text.lower() for char in lang_info['sample_chars'].split())
        if has_lang_features and english_count < 10:
            return True, f"检测到{lang_info['name']}特征"
    
    # 对于非拉丁字符语言（中日韩俄），检查字符集
    if lang_code == 'zh':
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
        if chinese_chars > len(text) * 0.3:
            return True, f"中文字符占比{chinese_chars}/{len(text)}"
    elif lang_code == 'ja':
        japanese_chars = len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', text))
        if japanese_chars > len(text) * 0.3:
            return True, f"日文字符占比{japanese_chars}/{len(text)}"
    elif lang_code == 'ko':
        korean_chars = len(re.findall(r'[\uac00-\ud7af]', text))
        if korean_chars > len(text) * 0.3:
            return True, f"韩文字符占比{korean_chars}/{len(text)}"
    elif lang_code == 'ru':
        cyrillic_chars = len(re.findall(r'[\u0400-\u04ff]', text))
        if cyrillic_chars > len(text) * 0.3:
            return True, f"俄文字符占比{cyrillic_chars}/{len(text)}"
    
    if english_count >= 5:
        return False, f"发现{english_count}个常见英文词"
    
    return True, "通过检测"

def check_article_detailed(en_file, lang_file, lang_code):
    """详细检查单篇文章的翻译质量"""
    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            en_content = f.read()
        with open(lang_file, 'r', encoding='utf-8') as f:
            lang_content = f.read()
        
        # 提取内容
        en_texts = extract_text_content(en_content)
        lang_texts = extract_text_content(lang_content)
        
        results = {
            'complete': True,
            'accurate': True,
            'issues': [],
            'stats': {}
        }
        
        # 1. 检查lang属性
        if f'lang="{lang_code}"' not in lang_content:
            results['complete'] = False
            results['issues'].append('lang属性未更新')
        
        # 2. 检查标题翻译
        if not lang_texts['title']:
            results['complete'] = False
            results['issues'].append('标题缺失')
        else:
            is_translated, reason = detect_language_quality(lang_texts['title'], lang_code)
            if not is_translated:
                results['accurate'] = False
                results['issues'].append(f'标题未翻译: {reason}')
        
        # 3. 检查段落翻译覆盖率
        en_para_count = len(en_texts['paragraphs'])
        lang_para_count = len(lang_texts['paragraphs'])
        
        if lang_para_count < en_para_count * 0.8:
            results['complete'] = False
            results['issues'].append(f'段落数不足: {lang_para_count}/{en_para_count}')
        
        # 4. 抽样检查段落翻译质量（检查前3个段落）
        bad_paragraphs = 0
        for i, para in enumerate(lang_texts['paragraphs'][:5]):
            is_translated, reason = detect_language_quality(para, lang_code)
            if not is_translated:
                bad_paragraphs += 1
                if bad_paragraphs <= 2:  # 只报告前2个问题
                    results['issues'].append(f'段落{i+1}未翻译: {reason}')
        
        if bad_paragraphs > 2:
            results['accurate'] = False
        
        # 5. 统计信息
        results['stats'] = {
            'en_paragraphs': en_para_count,
            'lang_paragraphs': lang_para_count,
            'coverage': f"{lang_para_count}/{en_para_count}" if en_para_count > 0 else "N/A",
            'section_titles': len(lang_texts['section_titles']),
            'captions': len(lang_texts['captions'])
        }
        
        return results
    
    except Exception as e:
        return {
            'complete': False,
            'accurate': False,
            'issues': [f'错误: {str(e)}'],
            'stats': {}
        }

def main():
    print("=" * 80)
    print("🔍 详细翻译完整性和准确率检查")
    print("=" * 80)
    print()
    
    categories = ['basics-identification', 'ecology-environment', 'beneficial-pollinators', 
                  'pest-management', 'behavior-evolution']
    
    overall_stats = {}
    
    for lang_code, lang_info in LANGUAGES.items():
        lang_name = lang_info['name']
        print(f"\n{'='*70}")
        print(f"📊 检查 {lang_name} ({lang_code})")
        print(f"{'='*70}\n")
        
        lang_dir = Path(f'insect/{lang_code}')
        en_dir = Path('insect/en')
        
        if not lang_dir.exists():
            print(f"  ❌ 目录不存在")
            continue
        
        # 收集所有文章
        all_articles = []
        for category in categories:
            cat_dir = lang_dir / category
            if cat_dir.exists():
                articles = sorted([f for f in cat_dir.glob('[0-9]*.html')])
                all_articles.extend([(category, f) for f in articles])
        
        # 随机抽样5篇文章进行详细检查
        sample_size = min(5, len(all_articles))
        sample_articles = random.sample(all_articles, sample_size)
        
        complete_count = 0
        accurate_count = 0
        total_issues = []
        
        for category, article_file in sample_articles:
            en_file = en_dir / category / article_file.name
            
            print(f"  📄 检查: {article_file.name[:50]}...")
            
            results = check_article_detailed(en_file, article_file, lang_code)
            
            if results['complete']:
                complete_count += 1
                status_complete = "✅"
            else:
                status_complete = "❌"
            
            if results['accurate']:
                accurate_count += 1
                status_accurate = "✅"
            else:
                status_accurate = "❌"
            
            print(f"    完整性: {status_complete}  准确性: {status_accurate}")
            
            if results['stats']:
                stats = results['stats']
                print(f"    段落覆盖: {stats.get('coverage', 'N/A')}, "
                      f"章节: {stats.get('section_titles', 0)}, "
                      f"图注: {stats.get('captions', 0)}")
            
            if results['issues']:
                for issue in results['issues'][:3]:  # 只显示前3个问题
                    print(f"    ⚠️  {issue}")
                total_issues.extend(results['issues'])
        
        # 统计
        completeness_rate = (complete_count / sample_size * 100) if sample_size > 0 else 0
        accuracy_rate = (accurate_count / sample_size * 100) if sample_size > 0 else 0
        
        print(f"\n  {'─'*66}")
        print(f"  📊 {lang_name} 抽样统计 (样本: {sample_size}/50)")
        print(f"  {'─'*66}")
        print(f"  完整性: {completeness_rate:.0f}% ({complete_count}/{sample_size})")
        print(f"  准确性: {accuracy_rate:.0f}% ({accurate_count}/{sample_size})")
        print(f"  问题数: {len(set(total_issues))}")
        
        overall_stats[lang_code] = {
            'name': lang_name,
            'completeness': completeness_rate,
            'accuracy': accuracy_rate,
            'sample_size': sample_size
        }
    
    # 总体统计
    print("\n" + "=" * 80)
    print("📈 总体翻译质量报告")
    print("=" * 80)
    
    avg_completeness = sum(s['completeness'] for s in overall_stats.values()) / len(overall_stats)
    avg_accuracy = sum(s['accuracy'] for s in overall_stats.values()) / len(overall_stats)
    
    print(f"\n平均完整性: {avg_completeness:.1f}%")
    print(f"平均准确性: {avg_accuracy:.1f}%")
    print()
    
    # 按质量排序
    sorted_langs = sorted(overall_stats.items(), 
                         key=lambda x: (x[1]['completeness'] + x[1]['accuracy']), 
                         reverse=True)
    
    print("各语言质量排名:")
    for i, (lang_code, stats) in enumerate(sorted_langs, 1):
        total_score = (stats['completeness'] + stats['accuracy']) / 2
        if total_score >= 90:
            grade = "优秀 ⭐⭐⭐"
        elif total_score >= 75:
            grade = "良好 ⭐⭐"
        elif total_score >= 60:
            grade = "及格 ⭐"
        else:
            grade = "需改进"
        
        print(f"  {i}. {stats['name']:10} - "
              f"完整性:{stats['completeness']:5.1f}% "
              f"准确性:{stats['accuracy']:5.1f}% - {grade}")
    
    print("\n" + "=" * 80)
    
    if avg_completeness >= 95 and avg_accuracy >= 95:
        print("\n🎉🎉🎉 翻译质量优秀！所有语言均达到高标准！")
    elif avg_completeness >= 85 and avg_accuracy >= 85:
        print("\n✅ 翻译质量良好！大部分内容准确完整。")
    else:
        print("\n⚠️  翻译质量需要改进，建议重新检查标记的问题。")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    main()

