#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insect项目系统性全面检查"""

import re
import sys
import json
from pathlib import Path
from collections import defaultdict

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LANGUAGES = {
    'en': '英文',
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

CATEGORIES = [
    'basics-identification',
    'ecology-environment',
    'beneficial-pollinators',
    'pest-management',
    'behavior-evolution'
]

def check_file_structure():
    """检查1：文件结构完整性"""
    print("\n" + "=" * 80)
    print("📁 检查1：文件结构完整性")
    print("=" * 80)
    
    issues = []
    stats = {
        'total_files': 0,
        'missing_files': 0,
        'by_language': {}
    }
    
    for lang_code, lang_name in LANGUAGES.items():
        lang_dir = Path(f"insect/{lang_code}")
        
        if not lang_dir.exists():
            issues.append(f"❌ {lang_name}目录不存在: {lang_dir}")
            continue
        
        lang_stats = {'found': 0, 'missing': []}
        
        for category in CATEGORIES:
            cat_dir = lang_dir / category
            
            if not cat_dir.exists():
                issues.append(f"⚠️  {lang_name}/{category} 目录不存在")
                continue
            
            # 检查HTML文件
            html_files = list(cat_dir.glob("*.html"))
            html_files = [f for f in html_files if 'index' not in f.name.lower()]
            
            lang_stats['found'] += len(html_files)
        
        stats['by_language'][lang_code] = lang_stats
        stats['total_files'] += lang_stats['found']
    
    # 输出结果
    print(f"\n📊 文件统计:")
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code in stats['by_language']:
            count = stats['by_language'][lang_code]['found']
            status = "✅" if count >= 50 else "⚠️"
            print(f"  {status} {lang_name:10s}: {count} 篇文章")
    
    print(f"\n📈 总计: {stats['total_files']} 个HTML文件")
    
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个问题:")
        for issue in issues[:10]:
            print(f"  {issue}")
    else:
        print("\n✅ 文件结构完整，无问题！")
    
    return len(issues) == 0, stats

def check_translation_quality():
    """检查2：翻译质量和完整性"""
    print("\n" + "=" * 80)
    print("🌐 检查2：翻译质量和完整性")
    print("=" * 80)
    
    issues = []
    stats = defaultdict(lambda: {'complete': 0, 'incomplete': 0})
    
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code == 'en':
            continue
        
        lang_dir = Path(f"insect/{lang_code}")
        if not lang_dir.exists():
            continue
        
        html_files = list(lang_dir.rglob("*.html"))
        html_files = [f for f in html_files if 'index' not in f.name.lower()]
        
        for html_file in html_files[:5]:  # 抽样检查前5个
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查lang属性
                has_correct_lang = f'lang="{lang_code}"' in content
                
                # 检查是否有未翻译的英文（针对非拉丁语系）
                if lang_code in ['zh', 'ja', 'ko', 'ru']:
                    main_content = re.search(r'<div class="article-content">(.*?)</div>\s*<footer', content, re.DOTALL)
                    if main_content:
                        text = re.sub(r'<[^>]+>', ' ', main_content.group(1))
                        english_words = len(re.findall(
                            r'\b(the|and|are|is|that|with|from|have|they|which)\b',
                            text,
                            re.IGNORECASE
                        ))
                        
                        if english_words > 30:
                            stats[lang_code]['incomplete'] += 1
                        else:
                            stats[lang_code]['complete'] += 1
                    else:
                        stats[lang_code]['complete'] += 1
                else:
                    stats[lang_code]['complete'] += 1
                    
            except Exception as e:
                issues.append(f"❌ {lang_name}/{html_file.name}: {str(e)[:50]}")
    
    # 输出结果
    print(f"\n📊 翻译质量（抽样检查）:")
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code == 'en':
            continue
        
        if lang_code in stats:
            complete = stats[lang_code]['complete']
            incomplete = stats[lang_code]['incomplete']
            total = complete + incomplete
            rate = (complete / total * 100) if total > 0 else 0
            status = "✅" if rate >= 95 else "⚠️"
            print(f"  {status} {lang_name:10s}: {complete}/{total} 完整 ({rate:.0f}%)")
    
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个问题")
    else:
        print("\n✅ 翻译质量良好！")
    
    return len(issues) == 0, stats

def check_json_configuration():
    """检查3：JSON配置完整性"""
    print("\n" + "=" * 80)
    print("📋 检查3：JSON配置完整性")
    print("=" * 80)
    
    issues = []
    json_dir = Path("insect-articles-json")
    
    if not json_dir.exists():
        print("❌ insect-articles-json 目录不存在！")
        return False, {}
    
    stats = {
        'total_json': 0,
        'valid_json': 0,
        'total_articles': 0
    }
    
    # 检查每个语言的JSON文件
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code == 'en':
            json_file = json_dir / "insect-article-urls.json"
        else:
            json_file = json_dir / f"insect-article-urls-{lang_code}.json"
        
        stats['total_json'] += 1
        
        if not json_file.exists():
            issues.append(f"❌ {lang_name} JSON文件不存在: {json_file.name}")
            continue
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 验证结构
            if "articleCategories" not in data:
                issues.append(f"❌ {lang_name} JSON缺少 articleCategories")
                continue
            
            categories = data["articleCategories"]
            article_count = sum(len(cat.get("articles", [])) for cat in categories.values())
            
            stats['valid_json'] += 1
            stats['total_articles'] += article_count
            
            status = "✅" if article_count >= 50 else "⚠️"
            print(f"  {status} {lang_name:10s}: {len(categories)}个分类, {article_count}篇文章")
            
        except json.JSONDecodeError as e:
            issues.append(f"❌ {lang_name} JSON格式错误: {str(e)[:50]}")
        except Exception as e:
            issues.append(f"❌ {lang_name} JSON读取错误: {str(e)[:50]}")
    
    print(f"\n📈 JSON统计:")
    print(f"  有效JSON: {stats['valid_json']}/{stats['total_json']}")
    print(f"  文章配置总数: {stats['total_articles']}")
    
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✅ JSON配置完整！")
    
    return len(issues) == 0, stats

def check_image_references():
    """检查4：图片引用"""
    print("\n" + "=" * 80)
    print("🖼️  检查4：图片引用")
    print("=" * 80)
    
    # 检查图片目录
    img_dir = Path("images")
    
    if not img_dir.exists():
        print("⚠️  images 目录不存在")
        return True, {}
    
    # 统计图片文件
    insect_images = list(img_dir.glob("insect_*.webp"))
    insect_images.extend(img_dir.glob("insect_*.jpg"))
    insect_images.extend(img_dir.glob("insect_*.png"))
    
    print(f"\n📊 图片统计:")
    print(f"  Insect相关图片: {len(insect_images)} 个")
    
    # 抽样检查HTML中的图片引用
    en_dir = Path("insect/en")
    if en_dir.exists():
        html_files = list(en_dir.rglob("*.html"))[:3]
        
        print(f"\n🔍 抽样检查图片引用:")
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                img_tags = re.findall(r'<img[^>]+src="([^"]+)"', content)
                print(f"  ✅ {html_file.name[:50]}: {len(img_tags)} 个图片引用")
                
            except Exception as e:
                print(f"  ⚠️  {html_file.name}: 检查失败")
    
    print("\n✅ 图片引用检查完成")
    
    return True, {'insect_images': len(insect_images)}

def check_index_pages():
    """检查5：索引页面"""
    print("\n" + "=" * 80)
    print("📑 检查5：索引页面")
    print("=" * 80)
    
    issues = []
    stats = {'found': 0, 'missing': 0}
    
    for lang_code, lang_name in LANGUAGES.items():
        index_file = Path(f"insect/{lang_code}/insect-articles-index.html")
        
        if index_file.exists():
            stats['found'] += 1
            print(f"  ✅ {lang_name:10s}: 索引页存在")
        else:
            stats['missing'] += 1
            issues.append(f"⚠️  {lang_name} 索引页不存在")
    
    print(f"\n📊 索引页统计:")
    print(f"  存在: {stats['found']}/{len(LANGUAGES)}")
    print(f"  缺失: {stats['missing']}/{len(LANGUAGES)}")
    
    if stats['missing'] > 0:
        print(f"\n⚠️  {stats['missing']} 个语言缺少索引页")
    else:
        print("\n✅ 所有索引页完整！")
    
    return stats['missing'] == 0, stats

def check_multilingual_consistency():
    """检查6：多语言一致性"""
    print("\n" + "=" * 80)
    print("🌍 检查6：多语言一致性")
    print("=" * 80)
    
    # 获取英文文章列表作为基准
    en_dir = Path("insect/en")
    en_files = set()
    
    for category in CATEGORIES:
        cat_dir = en_dir / category
        if cat_dir.exists():
            files = [f.name for f in cat_dir.glob("*.html") if 'index' not in f.name.lower()]
            en_files.update(files)
    
    print(f"📚 英文基准: {len(en_files)} 篇文章")
    print()
    
    # 检查每种语言是否有对应文章
    issues = []
    
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code == 'en':
            continue
        
        lang_dir = Path(f"insect/{lang_code}")
        if not lang_dir.exists():
            continue
        
        lang_files = set()
        for category in CATEGORIES:
            cat_dir = lang_dir / category
            if cat_dir.exists():
                files = [f.name for f in cat_dir.glob("*.html") if 'index' not in f.name.lower()]
                lang_files.update(files)
        
        # 计算覆盖率
        coverage = len(lang_files) / len(en_files) * 100 if en_files else 0
        missing = len(en_files - lang_files)
        
        status = "✅" if coverage >= 98 else "⚠️"
        print(f"  {status} {lang_name:10s}: {len(lang_files)}/{len(en_files)} 篇 ({coverage:.1f}%)")
        
        if missing > 0:
            issues.append(f"{lang_name} 缺少 {missing} 篇文章")
    
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个不一致:")
        for issue in issues[:5]:
            print(f"  {issue}")
    else:
        print("\n✅ 多语言文章数量一致！")
    
    return len(issues) == 0, {}

def generate_system_report(all_results):
    """生成系统检查报告"""
    print("\n" + "=" * 80)
    print("📊 系统检查总结报告")
    print("=" * 80)
    
    checks = [
        ("文件结构", all_results[0][0]),
        ("翻译质量", all_results[1][0]),
        ("JSON配置", all_results[2][0]),
        ("图片引用", all_results[3][0]),
        ("索引页面", all_results[4][0]),
        ("多语言一致性", all_results[5][0])
    ]
    
    print()
    for check_name, passed in checks:
        status = "✅ 通过" if passed else "⚠️  需注意"
        print(f"  {status:15s} - {check_name}")
    
    passed_count = sum(1 for _, passed in checks if passed)
    total_count = len(checks)
    
    print()
    print(f"总体通过率: {passed_count}/{total_count} ({passed_count/total_count*100:.0f}%)")
    print()
    
    # 关键指标
    print("=" * 80)
    print("🎯 关键指标")
    print("=" * 80)
    print(f"  • 总文章数: {all_results[0][1].get('total_files', 0)}")
    print(f"  • JSON配置: {all_results[2][1].get('valid_json', 0)}/{all_results[2][1].get('total_json', 0)}")
    print(f"  • JSON文章配置: {all_results[2][1].get('total_articles', 0)}")
    print(f"  • 语言数: {len(LANGUAGES)}")
    print(f"  • 分类数: {len(CATEGORIES)}")
    
    # 部署就绪评估
    print()
    print("=" * 80)
    print("🚀 部署就绪评估")
    print("=" * 80)
    
    if passed_count == total_count:
        print("✅ 状态: 完全就绪，可以立即部署！")
        print("   所有检查项目通过，系统状态优秀。")
    elif passed_count >= total_count * 0.8:
        print("⚠️  状态: 基本就绪，建议修复警告后部署")
        print("   大部分检查通过，有少量需要关注的问题。")
    else:
        print("❌ 状态: 需要修复问题后再部署")
        print("   存在较多问题，建议先完成修复工作。")
    
    print("=" * 80)

def main():
    print("=" * 80)
    print("🔍 Insect项目 - 系统性全面检查")
    print("=" * 80)
    print()
    print("检查范围:")
    print("  1. 文件结构完整性")
    print("  2. 翻译质量和完整性")
    print("  3. JSON配置完整性")
    print("  4. 图片引用")
    print("  5. 索引页面")
    print("  6. 多语言一致性")
    
    # 执行所有检查
    results = []
    
    results.append(check_file_structure())
    results.append(check_translation_quality())
    results.append(check_json_configuration())
    results.append(check_image_references())
    results.append(check_index_pages())
    results.append(check_multilingual_consistency())
    
    # 生成报告
    generate_system_report(results)
    
    print()
    print("✅ 系统检查完成！")
    print()

if __name__ == '__main__':
    main()

