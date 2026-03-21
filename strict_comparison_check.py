#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""严格对比检查 - 将翻译版本与英文原文对比"""

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

def extract_detailed_stats(html_content):
    """提取详细统计信息"""
    # 计算各种段落类型
    intro_paras = len(re.findall(r'<p class="intro">', html_content))
    regular_paras = len(re.findall(r'<p>(?!<img)', html_content))
    conclusion_paras = len(re.findall(r'<p class="conclusion">', html_content))
    
    # 计算其他元素
    sections = len(re.findall(r'<h3 class="section-title">', html_content))
    list_items = len(re.findall(r'<li>', html_content))
    captions = len(re.findall(r'<p class="illustration-caption">', html_content))
    tip_boxes = len(re.findall(r'<div class="tip-box', html_content))
    
    # 总段落数（包括intro、regular、conclusion，但排除空段落）
    all_paras = len(re.findall(r'<p[^>]*>(?!<img)(?!\s*</p>)', html_content))
    
    return {
        'intro_paras': intro_paras,
        'regular_paras': regular_paras,
        'conclusion_paras': conclusion_paras,
        'total_paras': all_paras,
        'sections': sections,
        'list_items': list_items,
        'captions': captions,
        'tip_boxes': tip_boxes
    }

def compare_articles(en_file, trans_file, lang_code):
    """对比英文和翻译文章"""
    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            en_html = f.read()
        with open(trans_file, 'r', encoding='utf-8') as f:
            trans_html = f.read()
        
        en_stats = extract_detailed_stats(en_html)
        trans_stats = extract_detailed_stats(trans_html)
        
        # 计算差异
        differences = {}
        perfect_match = True
        
        for key in en_stats:
            if en_stats[key] != trans_stats[key]:
                differences[key] = {
                    'en': en_stats[key],
                    'trans': trans_stats[key],
                    'diff': trans_stats[key] - en_stats[key]
                }
                perfect_match = False
        
        return {
            'status': 'perfect' if perfect_match else 'different',
            'en_stats': en_stats,
            'trans_stats': trans_stats,
            'differences': differences
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e)
        }

def main():
    print("=" * 80)
    print("🔬 严格对比检查 - 翻译版本 vs 英文原文")
    print("=" * 80)
    print()
    
    # 获取英文文章列表
    en_dir = Path("insect/en")
    en_files = sorted([
        f for f in en_dir.rglob("*.html") 
        if f.is_file() and 'index' not in f.name.lower()
    ])
    
    print(f"📚 检查文章数: {len(en_files)}")
    print()
    
    summary = {}
    
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{'='*70}")
        print(f"🌐 对比 {lang_name} ({lang_code})")
        print(f"{'='*70}")
        
        perfect_count = 0
        different_count = 0
        error_count = 0
        
        different_files = []
        
        for en_file in en_files:
            # 构造翻译文件路径
            rel_path = en_file.relative_to(en_dir)
            trans_file = Path(f"insect/{lang_code}") / rel_path
            
            if not trans_file.exists():
                continue
            
            result = compare_articles(en_file, trans_file, lang_code)
            
            if result['status'] == 'perfect':
                perfect_count += 1
            elif result['status'] == 'different':
                different_count += 1
                different_files.append({
                    'file': en_file.name,
                    'en_stats': result['en_stats'],
                    'trans_stats': result['trans_stats'],
                    'differences': result['differences']
                })
            else:
                error_count += 1
        
        total = perfect_count + different_count + error_count
        match_rate = (perfect_count / total * 100) if total > 0 else 0
        
        print(f"  ✅ 完美匹配: {perfect_count}/{total} ({match_rate:.1f}%)")
        print(f"  ⚠️  有差异: {different_count}/{total}")
        print(f"  ❌ 错误: {error_count}/{total}")
        
        # 显示有差异的文章（只显示前5个）
        if different_files:
            print(f"\n  📋 差异详情（显示前5个）:")
            for item in different_files[:5]:
                print(f"    • {item['file'][:60]}")
                print(f"      EN段落:{item['en_stats']['total_paras']} → TRANS段落:{item['trans_stats']['total_paras']}")
                
                if item['differences']:
                    for key, diff in item['differences'].items():
                        if key == 'total_paras':
                            symbol = "⚠️" if abs(diff['diff']) > 2 else "ℹ️"
                            print(f"      {symbol} {key}: {diff['en']} → {diff['trans']} (差{diff['diff']:+d})")
            
            if len(different_files) > 5:
                print(f"    ... 还有 {len(different_files) - 5} 篇有差异")
        
        print()
        
        summary[lang_code] = {
            'lang_name': lang_name,
            'perfect': perfect_count,
            'different': different_count,
            'error': error_count,
            'total': total,
            'match_rate': match_rate
        }
    
    # 总结
    print("=" * 80)
    print("📊 对比结果总结")
    print("=" * 80)
    
    total_match_rate = sum(s['match_rate'] for s in summary.values()) / len(summary) if summary else 0
    
    for lang_code, data in summary.items():
        status = "✅" if data['match_rate'] >= 95 else "⚠️" if data['match_rate'] >= 85 else "❌"
        print(f"{status} {data['lang_name']:10s} - {data['perfect']}/{data['total']} 完美匹配 ({data['match_rate']:.1f}%)")
    
    print()
    print(f"🎯 平均匹配率: {total_match_rate:.1f}%")
    print("=" * 80)
    
    # 结论
    if total_match_rate >= 95:
        print("\n✅ 翻译质量优秀！所有文章结构都与原文高度一致。")
    elif total_match_rate >= 85:
        print("\n⚠️  翻译质量良好，但有部分文章的段落数与原文有差异。")
        print("   这可能是由于翻译时合并或拆分了段落，不一定影响内容完整性。")
    else:
        print("\n❌ 翻译需要改进，建议检查差异较大的文章。")

if __name__ == '__main__':
    main()

