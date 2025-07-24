#!/usr/bin/env python3
"""
检测50篇文章的T1国家本地化完成情况
"""

import os
from pathlib import Path

# T1国家语言配置
LANGUAGES = ['en', 'zh', 'ja', 'ko', 'de', 'fr', 'es', 'it', 'pt', 'ru']
CATEGORIES = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
ARTICLES_PER_CATEGORY = 10

def check_article_exists(category, article_num, language):
    """检查文章是否存在"""
    article_id = f"{article_num:02d}"
    
    if language == 'en':
        file_path = Path(category) / f"{article_id}-article.html"
    else:
        file_path = Path(language) / category / f"{article_id}-article.html"
    
    return file_path.exists(), file_path

def check_article_content(file_path):
    """检查文章内容是否已本地化"""
    if not file_path.exists():
        return False, "File not found"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含本地化内容标识
        if 'article-intro' in content and 'article-paragraph' in content:
            if 'This is a sample article' in content:
                return False, "Contains template content"
            else:
                return True, "Localized content found"
        else:
            return False, "Missing content structure"
            
    except Exception as e:
        return False, f"Error reading file: {e}"

def main():
    print("🔍 检测50篇文章的T1国家本地化完成情况...")
    print("=" * 60)
    
    total_articles = 0
    localized_articles = 0
    missing_articles = 0
    template_articles = 0
    
    # 统计信息
    stats = {
        'categories': {},
        'languages': {}
    }
    
    for category in CATEGORIES:
        print(f"\n📁 分类: {category.upper()}")
        print("-" * 40)
        
        category_stats = {
            'total': 0,
            'localized': 0,
            'missing': 0,
            'template': 0
        }
        
        for article_num in range(1, ARTICLES_PER_CATEGORY + 1):
            print(f"\n  📄 文章 {article_num:02d}:")
            
            for language in LANGUAGES:
                exists, file_path = check_article_exists(category, article_num, language)
                total_articles += 1
                category_stats['total'] += 1
                
                if language not in stats['languages']:
                    stats['languages'][language] = {'total': 0, 'localized': 0, 'missing': 0, 'template': 0}
                
                stats['languages'][language]['total'] += 1
                
                if exists:
                    is_localized, status = check_article_content(file_path)
                    
                    if is_localized:
                        print(f"    ✅ {language}: 已本地化")
                        localized_articles += 1
                        category_stats['localized'] += 1
                        stats['languages'][language]['localized'] += 1
                    else:
                        if "template content" in status:
                            print(f"    ⚠️  {language}: 模板内容")
                            template_articles += 1
                            category_stats['template'] += 1
                            stats['languages'][language]['template'] += 1
                        else:
                            print(f"    ❌ {language}: {status}")
                            template_articles += 1
                            category_stats['template'] += 1
                            stats['languages'][language]['template'] += 1
                else:
                    print(f"    ❌ {language}: 文件不存在")
                    missing_articles += 1
                    category_stats['missing'] += 1
                    stats['languages'][language]['missing'] += 1
        
        stats['categories'][category] = category_stats
    
    # 总结报告
    print("\n" + "=" * 60)
    print("📊 本地化完成情况总结")
    print("=" * 60)
    
    print(f"\n🔢 总体统计:")
    print(f"  总文章数: {total_articles}")
    print(f"  已本地化: {localized_articles} ({localized_articles/total_articles*100:.1f}%)")
    print(f"  模板内容: {template_articles} ({template_articles/total_articles*100:.1f}%)")
    print(f"  文件缺失: {missing_articles} ({missing_articles/total_articles*100:.1f}%)")
    
    print(f"\n📂 分类统计:")
    for category, stats_data in stats['categories'].items():
        total = stats_data['total']
        localized = stats_data['localized']
        print(f"  {category}: {localized}/{total} ({localized/total*100:.1f}% 完成)")
    
    print(f"\n🌍 语言统计:")
    for language, stats_data in stats['languages'].items():
        total = stats_data['total']
        localized = stats_data['localized']
        print(f"  {language}: {localized}/{total} ({localized/total*100:.1f}% 完成)")
    
    # 完成状态
    completion_rate = localized_articles / total_articles * 100
    
    print(f"\n🎯 本地化完成度: {completion_rate:.1f}%")
    
    if completion_rate == 100:
        print("🎉 所有文章已完成T1国家本地化！")
    elif completion_rate >= 80:
        print("✅ 本地化基本完成，还有少量工作需要完善")
    elif completion_rate >= 50:
        print("⚠️  本地化进度过半，需要继续完善")
    else:
        print("❌ 本地化工作需要大量完善")
    
    print("\n💡 建议:")
    if template_articles > 0:
        print("  - 需要将模板内容替换为真实的本地化内容")
    if missing_articles > 0:
        print("  - 需要创建缺失的文章文件")
    
    print("  - 考虑使用专业翻译服务提高内容质量")
    print("  - 定期检查和更新本地化内容")

if __name__ == "__main__":
    main()