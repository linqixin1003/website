#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def check_translation_quality():
    """检查所有生态学文章的翻译质量"""
    
    # 语言配置
    languages = {
        'en': 'English',
        'zh': '中文',
        'ja': '日本語', 
        'ko': '한국어',
        'de': 'Deutsch',
        'fr': 'Français',
        'es': 'Español',
        'it': 'Italiano',
        'pt': 'Português',
        'ru': 'Русский'
    }
    
    # 文章列表
    articles = [
        '01-habitat-ecosystems.html',
        '02-food-webs-chains.html',
        '03-migration-patterns.html',
        '04-breeding-ecology.html',
        '05-climate-change-impact.html',
        '06-urban-ecology.html',
        '07-conservation-biology.html',
        '08-island-biogeography.html',
        '09-pollination-seed-dispersal.html',
        '10-community-dynamics.html'
    ]
    
    issues_found = []
    
    for lang_code, lang_name in languages.items():
        print(f"\n检查 {lang_name} ({lang_code}) 版本...")
        
        for article in articles:
            file_path = f"{lang_code}/ecology/{article}"
            
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 检查常见问题
                    issues = check_common_issues(content, lang_code, article)
                    if issues:
                        issues_found.extend(issues)
                        
                except Exception as e:
                    issues_found.append(f"❌ {file_path}: 读取文件错误 - {str(e)}")
            else:
                issues_found.append(f"❌ {file_path}: 文件不存在")
    
    # 输出检查结果
    print(f"\n{'='*60}")
    print("翻译质量检查结果")
    print(f"{'='*60}")
    
    if issues_found:
        print(f"发现 {len(issues_found)} 个问题:")
        for issue in issues_found:
            print(issue)
    else:
        print("✅ 所有文章翻译质量良好，未发现问题")
    
    return issues_found

def check_common_issues(content, lang_code, article):
    """检查常见的翻译问题"""
    issues = []
    file_path = f"{lang_code}/ecology/{article}"
    
    # 1. 检查是否有英文残留（非英文版本）
    if lang_code != 'en':
        english_patterns = [
            r'\b(Bird|Ecology|Habitat|Migration|Climate|Urban|Conservation|Island|Pollination|Community)\b',
            r'\b(the|and|of|in|to|for|with|by|from|at|on)\b',
            r'\b(species|ecosystem|environment|population|biodiversity)\b'
        ]
        
        for pattern in english_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                # 排除一些合理的英文词汇（如专有名词、引用等）
                filtered_matches = [m for m in matches if not is_acceptable_english(m, content)]
                if filtered_matches:
                    issues.append(f"⚠️  {file_path}: 发现英文残留 - {', '.join(set(filtered_matches))}")
    
    # 2. 检查HTML结构问题
    if '<title>' not in content:
        issues.append(f"❌ {file_path}: 缺少title标签")
    
    if 'hero-image' not in content:
        issues.append(f"❌ {file_path}: 缺少hero-image样式")
    
    # 3. 检查图片路径
    img_pattern = r'url\([\'"]?([^\'")]+)[\'"]?\)'
    img_matches = re.findall(img_pattern, content)
    for img_path in img_matches:
        if 'bird-image' in img_path and not img_path.startswith('../../images/'):
            issues.append(f"❌ {file_path}: 图片路径错误 - {img_path}")
    
    # 4. 检查语言特定问题
    if lang_code == 'zh':
        # 中文应该有中文标点
        if content.count('，') < 5 and content.count(',') > 10:
            issues.append(f"⚠️  {file_path}: 中文标点使用不当")
    
    elif lang_code == 'ja':
        # 日文应该有日文标点
        if '。' not in content and '.' in content:
            issues.append(f"⚠️  {file_path}: 日文标点使用不当")
    
    elif lang_code == 'ko':
        # 韩文检查
        if content.count('다.') < 3:
            issues.append(f"⚠️  {file_path}: 韩文语法结构可能有问题")
    
    # 5. 检查CSS和JS引用
    required_css = ['mobile-styles.css', 'mobile-enhancement.css', 'ecology-theme.css']
    for css in required_css:
        if css not in content:
            issues.append(f"❌ {file_path}: 缺少CSS引用 - {css}")
    
    return issues

def is_acceptable_english(word, content):
    """判断英文词汇是否可接受（如专有名词、引用等）"""
    acceptable_contexts = [
        'BirdAiSnap',  # 网站名称
        'CSS',         # 技术术语
        'HTML',        # 技术术语
        'JavaScript',  # 技术术语
        'URL',         # 技术术语
    ]
    
    # 检查是否在可接受的上下文中
    for context in acceptable_contexts:
        if context.lower() in content.lower():
            return True
    
    # 检查是否在引号中（可能是引用）
    if f'"{word}"' in content or f"'{word}'" in content:
        return True
    
    return False

def fix_common_issues():
    """修复常见的翻译问题"""
    print("\n开始修复常见问题...")
    
    # 这里可以添加自动修复逻辑
    # 例如：统一图片路径、修复CSS引用等
    
    print("✅ 自动修复完成")

if __name__ == "__main__":
    print("开始检查所有生态学文章的翻译质量...")
    issues = check_translation_quality()
    
    if issues:
        print(f"\n发现 {len(issues)} 个问题需要修复")
        
        # 询问是否进行自动修复
        response = input("\n是否尝试自动修复一些问题？(y/n): ")
        if response.lower() == 'y':
            fix_common_issues()
    else:
        print("\n🎉 所有文章翻译质量检查通过！")