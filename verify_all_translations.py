#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面验证所有昆虫文章翻译质量
"""

import os
import re
from pathlib import Path
from collections import defaultdict

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

def check_article_quality(file_path, lang_code):
    """检查单篇文章的质量"""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 1. 检查lang属性
        if f'<html lang="{lang_code}">' not in html:
            issues.append(f"❌ lang属性错误")
        
        # 2. 检查title是否包含InsectAiSnap
        if 'InsectAiSnap</title>' not in html:
            issues.append(f"❌ title缺少InsectAiSnap")
        
        # 3. 检查是否有未翻译的英文段落
        # 统计常见英文单词
        english_words = re.findall(
            r'\b(the|and|are|that|with|from|have|they|which|their|when|what|this|will|can|but)\b',
            html,
            re.IGNORECASE
        )
        
        # 排除script、style等标签内的内容
        text_content = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
        text_content = re.sub(r'<style.*?</style>', '', text_content, flags=re.DOTALL)
        
        english_in_content = re.findall(
            r'\b(the|and|are|that|with|from|have|they|which|their|when|what|this|will|can|but)\b',
            text_content,
            re.IGNORECASE
        )
        
        if len(english_in_content) > 20:
            issues.append(f"⚠️  可能有未翻译内容 (英文词: {len(english_in_content)}个)")
        
        # 4. 检查关键元素是否存在
        if '<h1 class="hero-title">' not in html:
            issues.append(f"❌ 缺少hero-title")
        
        if '<h2 class="article-title">' not in html:
            issues.append(f"❌ 缺少article-title")
        
        # 5. 检查段落数量
        paragraphs = re.findall(r'<p[^>]*>.*?</p>', html, re.DOTALL)
        if len(paragraphs) < 5:
            issues.append(f"⚠️  段落数量较少 ({len(paragraphs)}个)")
        
        return issues
        
    except Exception as e:
        return [f"❌ 读取错误: {str(e)}"]

def main():
    print("=" * 80)
    print("🔍 昆虫文章翻译质量全面检查")
    print("=" * 80)
    print()
    
    # 统计数据
    total_stats = {
        'total_files': 0,
        'perfect_files': 0,
        'warning_files': 0,
        'error_files': 0
    }
    
    language_stats = defaultdict(lambda: {
        'total': 0,
        'perfect': 0,
        'warnings': 0,
        'errors': 0
    })
    
    all_issues = defaultdict(list)
    
    # 检查每种语言
    for lang_code, lang_name in LANGUAGES.items():
        print(f"\n{'='*60}")
        print(f"📋 检查 {lang_name} ({lang_code})")
        print('='*60)
        
        lang_dir = Path(f'insect/{lang_code}')
        
        if not lang_dir.exists():
            print(f"❌ 目录不存在: {lang_dir}")
            continue
        
        # 获取所有HTML文件
        html_files = sorted(lang_dir.rglob('*.html'))
        
        if not html_files:
            print(f"⚠️  未找到HTML文件")
            continue
        
        print(f"📄 共找到 {len(html_files)} 个文件\n")
        
        # 检查每个文件
        for html_file in html_files:
            total_stats['total_files'] += 1
            language_stats[lang_code]['total'] += 1
            
            issues = check_article_quality(html_file, lang_code)
            
            if issues:
                # 判断严重程度
                has_error = any('❌' in issue for issue in issues)
                
                if has_error:
                    total_stats['error_files'] += 1
                    language_stats[lang_code]['errors'] += 1
                else:
                    total_stats['warning_files'] += 1
                    language_stats[lang_code]['warnings'] += 1
                
                all_issues[lang_code].append({
                    'file': str(html_file),
                    'issues': issues
                })
            else:
                total_stats['perfect_files'] += 1
                language_stats[lang_code]['perfect'] += 1
        
        # 显示该语言的统计
        stats = language_stats[lang_code]
        print(f"\n{lang_name} 统计:")
        print(f"  ✅ 完美: {stats['perfect']}/{stats['total']}")
        print(f"  ⚠️  警告: {stats['warnings']}")
        print(f"  ❌ 错误: {stats['errors']}")
        
        if stats['perfect'] == stats['total']:
            print(f"  🎉 所有文件都完美！")
    
    # 全局统计
    print("\n" + "=" * 80)
    print("📊 全局统计")
    print("=" * 80)
    print(f"总文件数: {total_stats['total_files']}")
    print(f"✅ 完美文件: {total_stats['perfect_files']} ({total_stats['perfect_files']/total_stats['total_files']*100:.1f}%)")
    print(f"⚠️  有警告: {total_stats['warning_files']} ({total_stats['warning_files']/total_stats['total_files']*100:.1f}%)")
    print(f"❌ 有错误: {total_stats['error_files']} ({total_stats['error_files']/total_stats['total_files']*100:.1f}%)")
    
    # 详细问题列表
    if all_issues:
        print("\n" + "=" * 80)
        print("📋 详细问题列表")
        print("=" * 80)
        
        for lang_code, issues_list in all_issues.items():
            if issues_list:
                print(f"\n{'='*60}")
                print(f"{LANGUAGES[lang_code]} ({lang_code}) - {len(issues_list)} 个文件有问题")
                print('='*60)
                
                for item in issues_list[:10]:  # 只显示前10个
                    print(f"\n📄 {item['file']}")
                    for issue in item['issues']:
                        print(f"   {issue}")
                
                if len(issues_list) > 10:
                    print(f"\n   ... 还有 {len(issues_list) - 10} 个文件有问题")
    else:
        print("\n🎉 所有文件都完美通过检查！")
    
    # 生成报告
    print("\n" + "=" * 80)
    print("💾 生成详细报告...")
    print("=" * 80)
    
    with open('TRANSLATION_VERIFICATION_REPORT.md', 'w', encoding='utf-8') as f:
        f.write("# 昆虫文章翻译质量验证报告\n\n")
        f.write(f"**检查时间**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## 全局统计\n\n")
        f.write(f"- 总文件数: {total_stats['total_files']}\n")
        f.write(f"- ✅ 完美文件: {total_stats['perfect_files']} ({total_stats['perfect_files']/total_stats['total_files']*100:.1f}%)\n")
        f.write(f"- ⚠️  有警告: {total_stats['warning_files']} ({total_stats['warning_files']/total_stats['total_files']*100:.1f}%)\n")
        f.write(f"- ❌ 有错误: {total_stats['error_files']} ({total_stats['error_files']/total_stats['total_files']*100:.1f}%)\n\n")
        
        f.write("## 各语言统计\n\n")
        f.write("| 语言 | 总数 | 完美 | 警告 | 错误 | 完成率 |\n")
        f.write("|------|------|------|------|------|--------|\n")
        
        for lang_code, lang_name in LANGUAGES.items():
            stats = language_stats[lang_code]
            if stats['total'] > 0:
                completion = stats['perfect'] / stats['total'] * 100
                f.write(f"| {lang_name} ({lang_code}) | {stats['total']} | {stats['perfect']} | {stats['warnings']} | {stats['errors']} | {completion:.1f}% |\n")
        
        if all_issues:
            f.write("\n## 详细问题列表\n\n")
            for lang_code, issues_list in all_issues.items():
                if issues_list:
                    f.write(f"\n### {LANGUAGES[lang_code]} ({lang_code})\n\n")
                    for item in issues_list:
                        f.write(f"**{item['file']}**\n\n")
                        for issue in item['issues']:
                            f.write(f"- {issue}\n")
                        f.write("\n")
    
    print("✅ 报告已保存: TRANSLATION_VERIFICATION_REPORT.md")
    
    print("\n" + "=" * 80)
    if total_stats['error_files'] == 0 and total_stats['warning_files'] == 0:
        print("✅ 所有翻译都完美！")
    elif total_stats['error_files'] == 0:
        print("⚠️  有少量警告，但无严重错误")
    else:
        print("❌ 发现一些错误，需要修复")
    print("=" * 80)

if __name__ == '__main__':
    main()

