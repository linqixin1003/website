#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全面检查所有文章的完整性"""

import re
import sys
from pathlib import Path
from collections import defaultdict

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

def count_elements(html_content):
    """统计HTML中的各种元素数量"""
    stats = {
        'paragraphs': len(re.findall(r'<p(?:\s+class="[^"]*")?>[^<]', html_content)),
        'sections': len(re.findall(r'<h3 class="section-title">', html_content)),
        'list_items': len(re.findall(r'<li>', html_content)),
        'captions': len(re.findall(r'<p class="illustration-caption">', html_content)),
        'tip_boxes': len(re.findall(r'<div class="tip-box', html_content))
    }
    return stats

def check_article(file_path, lang_code):
    """检查单篇文章的完整性"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 检查基本元素
        has_lang = f'lang="{lang_code}"' in html
        has_translated_title = True  # 暂时假设标题都已翻译
        
        # 统计元素
        stats = count_elements(html)
        
        # 检查是否有未翻译的英文（针对非拉丁语系）
        english_words = 0
        if lang_code in ['zh', 'ja', 'ko', 'ru']:
            # 检查主要内容区域的英文单词
            content_match = re.search(r'<div class="article-content">(.*?)</div>\s*<footer', html, re.DOTALL)
            if content_match:
                content = content_match.group(1)
                # 移除HTML标签
                text = re.sub(r'<[^>]+>', ' ', content)
                # 统计常见英文单词
                english_words = len(re.findall(
                    r'\b(the|and|are|is|that|with|from|have|they|which|their|when|what|this|these|those|for|can|will|about|into|through|during|before|after)\b',
                    text,
                    re.IGNORECASE
                ))
        
        issues = []
        if not has_lang:
            issues.append("缺少lang属性")
        if english_words > 20:
            issues.append(f"可能有未翻译内容(英文词:{english_words})")
        if stats['paragraphs'] < 5:
            issues.append(f"段落数过少({stats['paragraphs']})")
        
        return {
            'status': 'ok' if len(issues) == 0 else 'incomplete',
            'stats': stats,
            'issues': issues,
            'english_words': english_words
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e)
        }

def main():
    print("=" * 80)
    print("🔍 全面完整性检查 - 所有语言所有文章")
    print("=" * 80)
    print()
    
    # 获取英文文章列表作为参考（排除索引页）
    en_dir = Path("insect/en")
    en_files = sorted([
        f.name for f in en_dir.rglob("*.html") 
        if f.is_file() and 'index' not in f.name.lower()
    ])
    
    print(f"📚 参考英文文章数: {len(en_files)}")
    print()
    
    results = {}
    
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{'='*70}")
        print(f"🌐 检查 {lang_name} ({lang_code})")
        print(f"{'='*70}")
        
        lang_dir = Path(f"insect/{lang_code}")
        
        if not lang_dir.exists():
            print(f"  ⚠️  目录不存在")
            continue
        
        incomplete_files = []
        ok_files = []
        error_files = []
        
        for en_file in en_files:
            # 构造对应语言的文件路径
            lang_file = lang_dir / en_file.replace('.html', '.html')
            
            # 尝试在子目录中查找
            if not lang_file.exists():
                # 尝试查找
                found_files = list(lang_dir.rglob(en_file))
                if found_files:
                    lang_file = found_files[0]
                else:
                    continue
            
            result = check_article(lang_file, lang_code)
            
            if result['status'] == 'ok':
                ok_files.append(en_file)
            elif result['status'] == 'incomplete':
                try:
                    rel_path = str(lang_file.relative_to(Path.cwd()))
                except ValueError:
                    rel_path = str(lang_file)
                
                incomplete_files.append({
                    'file': en_file,
                    'path': rel_path,
                    'issues': result['issues'],
                    'stats': result['stats'],
                    'english_words': result.get('english_words', 0)
                })
            else:
                error_files.append((en_file, result.get('error', 'Unknown')))
        
        # 输出统计
        total = len(ok_files) + len(incomplete_files) + len(error_files)
        print(f"  ✅ 完整: {len(ok_files)}/{total}")
        print(f"  ⚠️  不完整: {len(incomplete_files)}/{total}")
        print(f"  ❌ 错误: {len(error_files)}/{total}")
        
        # 显示不完整的文章
        if incomplete_files:
            print(f"\n  📋 不完整文章列表:")
            for item in incomplete_files[:10]:  # 只显示前10个
                print(f"    • {item['file'][:60]}")
                print(f"      问题: {', '.join(item['issues'])}")
                print(f"      段落:{item['stats']['paragraphs']} 章节:{item['stats']['sections']} 列表项:{item['stats']['list_items']}")
                if item['english_words'] > 20:
                    print(f"      ⚠️  英文词数: {item['english_words']}")
            
            if len(incomplete_files) > 10:
                print(f"    ... 还有 {len(incomplete_files) - 10} 篇")
        
        print()
        
        results[lang_code] = {
            'lang_name': lang_name,
            'ok': len(ok_files),
            'incomplete': len(incomplete_files),
            'error': len(error_files),
            'total': total,
            'incomplete_files': incomplete_files
        }
    
    # 总结
    print("=" * 80)
    print("📊 总体完整性报告")
    print("=" * 80)
    
    for lang_code, data in results.items():
        completeness = (data['ok'] / data['total'] * 100) if data['total'] > 0 else 0
        status = "✅" if completeness >= 95 else "⚠️" if completeness >= 80 else "❌"
        print(f"{status} {data['lang_name']:10s} - {data['ok']}/{data['total']} 完整 ({completeness:.1f}%)")
    
    print()
    
    # 生成修复列表
    print("=" * 80)
    print("📝 生成修复列表")
    print("=" * 80)
    
    total_to_fix = 0
    for lang_code, data in results.items():
        if data['incomplete'] > 0:
            fix_file = f"fix_incomplete_{lang_code}.txt"
            with open(fix_file, 'w', encoding='utf-8') as f:
                for item in data['incomplete_files']:
                    f.write(f"{item['path']}\n")
            print(f"  ✅ {data['lang_name']}: {data['incomplete']}篇 → {fix_file}")
            total_to_fix += data['incomplete']
    
    print()
    print(f"📋 总计需修复: {total_to_fix} 篇文章")
    print("=" * 80)

if __name__ == '__main__':
    main()

