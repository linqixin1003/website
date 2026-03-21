#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证insect JSON格式是否与rock格式一致"""

import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def verify_json_structure(json_file, expected_structure):
    """验证JSON结构"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        issues = []
        
        # 检查顶层结构
        if "articleCategories" not in data:
            issues.append("缺少 'articleCategories'")
            return issues
        
        categories = data["articleCategories"]
        total_articles = 0
        
        # 检查每个分类
        for cat_key, cat_data in categories.items():
            # 检查分类字段
            required_cat_fields = ["categoryName", "categoryNameEn", "categoryIcon", "baseUrl", "articles"]
            for field in required_cat_fields:
                if field not in cat_data:
                    issues.append(f"{cat_key}: 缺少字段 '{field}'")
            
            # 检查文章列表
            if "articles" in cat_data:
                articles = cat_data["articles"]
                total_articles += len(articles)
                
                # 检查前3篇文章的字段
                for idx, article in enumerate(articles[:3]):
                    required_article_fields = ["id", "title", "titleEn", "url", "description", "difficulty", "readTime", "imageUrl"]
                    for field in required_article_fields:
                        if field not in article:
                            issues.append(f"{cat_key} 文章{idx+1}: 缺少字段 '{field}'")
        
        return {
            'issues': issues,
            'categories': len(categories),
            'total_articles': total_articles
        }
        
    except Exception as e:
        return {'issues': [f"读取错误: {str(e)}"], 'categories': 0, 'total_articles': 0}

def compare_formats():
    """对比rock和insect的JSON格式"""
    print("=" * 80)
    print("🔍 验证Insect JSON格式（对比Rock格式）")
    print("=" * 80)
    print()
    
    # 读取rock的JSON作为参考
    rock_json = Path("rock-articles-json/rock-article-urls.json")
    print(f"📘 参考格式: {rock_json}")
    
    if rock_json.exists():
        with open(rock_json, 'r', encoding='utf-8') as f:
            rock_data = json.load(f)
        
        rock_cat = list(rock_data["articleCategories"].values())[0]
        rock_article = rock_cat["articles"][0]
        
        print(f"  分类字段: {list(rock_cat.keys())}")
        print(f"  文章字段: {list(rock_article.keys())}")
    
    print()
    print("=" * 80)
    print("📊 检查Insect JSON文件")
    print("=" * 80)
    print()
    
    # 检查所有insect JSON文件
    insect_json_dir = Path("insect-articles-json")
    json_files = sorted(insect_json_dir.glob("*.json"))
    
    results = []
    
    for json_file in json_files:
        result = verify_json_structure(json_file, None)
        
        lang = "英文" if json_file.name == "insect-article-urls.json" else json_file.stem.split('-')[-1].upper()
        
        if result['issues']:
            status = "❌"
            print(f"{status} {lang:8s} ({json_file.name})")
            for issue in result['issues']:
                print(f"    ⚠️  {issue}")
        else:
            status = "✅"
            print(f"{status} {lang:8s} - {result['categories']}个分类, {result['total_articles']}篇文章")
        
        results.append({
            'file': json_file.name,
            'lang': lang,
            'status': status,
            'issues': result['issues'],
            'categories': result['categories'],
            'articles': result['total_articles']
        })
    
    print()
    print("=" * 80)
    print("📈 验证总结")
    print("=" * 80)
    
    total_files = len(results)
    valid_files = len([r for r in results if not r['issues']])
    total_articles = sum(r['articles'] for r in results)
    
    print(f"✅ 有效文件: {valid_files}/{total_files}")
    print(f"📚 文章总数: {total_articles}")
    print(f"🌍 语言数: {len(json_files)}")
    
    if valid_files == total_files:
        print()
        print("🎉 所有JSON文件格式完全符合Rock标准！")
    else:
        print()
        print("⚠️  部分文件存在问题，需要修复")
    
    print("=" * 80)

def sample_comparison():
    """抽样对比rock和insect的JSON内容"""
    print()
    print("=" * 80)
    print("🔬 抽样对比 Rock vs Insect 格式")
    print("=" * 80)
    print()
    
    # Rock示例
    with open("rock-articles-json/rock-article-urls.json", 'r', encoding='utf-8') as f:
        rock_data = json.load(f)
    
    rock_cat_key = list(rock_data["articleCategories"].keys())[0]
    rock_cat = rock_data["articleCategories"][rock_cat_key]
    rock_article = rock_cat["articles"][0]
    
    print("📘 Rock格式示例:")
    print(f"  分类: {rock_cat_key}")
    print(f"    categoryName: {rock_cat['categoryName']}")
    print(f"    categoryIcon: {rock_cat['categoryIcon']}")
    print(f"    文章数: {len(rock_cat['articles'])}")
    print(f"  文章示例:")
    print(f"    id: {rock_article['id']}")
    print(f"    title: {rock_article['title'][:50]}...")
    print(f"    difficulty: {rock_article['difficulty']}")
    print()
    
    # Insect示例
    with open("insect-articles-json/insect-article-urls.json", 'r', encoding='utf-8') as f:
        insect_data = json.load(f)
    
    insect_cat_key = list(insect_data["articleCategories"].keys())[0]
    insect_cat = insect_data["articleCategories"][insect_cat_key]
    insect_article = insect_cat["articles"][0]
    
    print("🐛 Insect格式示例:")
    print(f"  分类: {insect_cat_key}")
    print(f"    categoryName: {insect_cat['categoryName']}")
    print(f"    categoryIcon: {insect_cat['categoryIcon']}")
    print(f"    文章数: {len(insect_cat['articles'])}")
    print(f"  文章示例:")
    print(f"    id: {insect_article['id']}")
    print(f"    title: {insect_article['title'][:50]}...")
    print(f"    difficulty: {insect_article['difficulty']}")
    print()
    
    # 字段对比
    rock_cat_fields = set(rock_cat.keys())
    insect_cat_fields = set(insect_cat.keys())
    
    rock_article_fields = set(rock_article.keys())
    insect_article_fields = set(insect_article.keys())
    
    print("🔍 字段对比:")
    print(f"  分类字段 Rock:   {sorted(rock_cat_fields)}")
    print(f"  分类字段 Insect: {sorted(insect_cat_fields)}")
    print(f"  匹配: {'✅ 完全一致' if rock_cat_fields == insect_cat_fields else '❌ 不一致'}")
    print()
    print(f"  文章字段 Rock:   {sorted(rock_article_fields)}")
    print(f"  文章字段 Insect: {sorted(insect_article_fields)}")
    print(f"  匹配: {'✅ 完全一致' if rock_article_fields == insect_article_fields else '❌ 不一致'}")
    print()
    print("=" * 80)

if __name__ == '__main__':
    compare_formats()
    sample_comparison()

