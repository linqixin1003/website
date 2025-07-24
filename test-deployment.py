#!/usr/bin/env python3
"""
本地部署测试脚本
测试多语言文章系统的各项功能
"""

import requests
import time
import sys
from urllib.parse import urljoin

# 测试配置
BASE_URL = "http://localhost:3000"
LANGUAGES = ['en', 'zh', 'ja', 'ko', 'de', 'fr', 'es', 'it', 'pt', 'ru']
CATEGORIES = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
TEST_ARTICLES = [1, 5, 10]  # 测试第1、5、10篇文章

def test_url(url, expected_status=200):
    """测试URL访问"""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == expected_status, response.status_code, response
    except requests.exceptions.RequestException as e:
        return False, 0, str(e)

def test_content_localization(url, language):
    """测试内容本地化"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return False, f"HTTP {response.status_code}"
        
        content = response.text
        
        # 检查语言标识
        if f'Language: {get_language_name(language)}' not in content:
            return False, "Missing language identifier"
        
        # 检查基本结构
        required_elements = ['article-title', 'article-intro', 'article-paragraph']
        for element in required_elements:
            if element not in content:
                return False, f"Missing {element}"
        
        # 检查是否包含模板内容（应该已经被替换）
        if 'This is a sample article' in content:
            return False, "Contains template content"
        
        return True, "Content properly localized"
        
    except requests.exceptions.RequestException as e:
        return False, str(e)

def get_language_name(code):
    """获取语言名称"""
    names = {
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
    return names.get(code, code)

def main():
    print("🚀 开始本地部署测试...")
    print("=" * 60)
    
    # 首先测试服务器是否运行
    print("🔍 检查服务器状态...")
    success, status, _ = test_url(BASE_URL + "/index.html")
    if not success:
        print(f"❌ 服务器未运行或无法访问 (状态码: {status})")
        print("💡 请先运行: python3 start-server.py")
        sys.exit(1)
    
    print("✅ 服务器运行正常")
    
    # 测试统计
    total_tests = 0
    passed_tests = 0
    failed_tests = []
    
    print(f"\n📊 开始测试多语言文章...")
    print("-" * 40)
    
    for category in CATEGORIES:
        print(f"\n📁 测试分类: {category.upper()}")
        
        for article_num in TEST_ARTICLES:
            print(f"\n  📄 测试文章 {article_num:02d}:")
            
            for language in LANGUAGES:
                total_tests += 1
                
                # 构建URL
                if language == 'en':
                    url = f"{BASE_URL}/{category}/{article_num:02d}-article.html"
                else:
                    url = f"{BASE_URL}/{language}/{category}/{article_num:02d}-article.html"
                
                # 测试访问
                success, status, response = test_url(url)
                
                if success:
                    # 测试内容本地化
                    content_ok, content_msg = test_content_localization(url, language)
                    
                    if content_ok:
                        print(f"    ✅ {language}: 访问正常，内容已本地化")
                        passed_tests += 1
                    else:
                        print(f"    ⚠️  {language}: 访问正常，但内容问题 - {content_msg}")
                        failed_tests.append(f"{category}/{article_num:02d} ({language}): {content_msg}")
                else:
                    print(f"    ❌ {language}: 访问失败 (状态码: {status})")
                    failed_tests.append(f"{category}/{article_num:02d} ({language}): HTTP {status}")
    
    # 测试特殊功能
    print(f"\n🔧 测试特殊功能...")
    print("-" * 40)
    
    # 测试主页
    print("🏠 测试主页访问...")
    success, status, _ = test_url(BASE_URL + "/index.html")
    total_tests += 1
    if success:
        print("  ✅ 主页访问正常")
        passed_tests += 1
    else:
        print(f"  ❌ 主页访问失败 (状态码: {status})")
        failed_tests.append(f"主页访问: HTTP {status}")
    
    # 测试知识中心页面
    print("📚 测试知识中心页面...")
    success, status, _ = test_url(BASE_URL + "/knowledge.html")
    total_tests += 1
    if success:
        print("  ✅ 知识中心页面访问正常")
        passed_tests += 1
    else:
        print(f"  ❌ 知识中心页面访问失败 (状态码: {status})")
        failed_tests.append(f"知识中心页面: HTTP {status}")
    
    # 测试分类页面
    for category in ['scientific-wonders', 'birdwatching']:
        print(f"📂 测试 {category} 分类页面...")
        success, status, _ = test_url(BASE_URL + f"/{category}.html")
        total_tests += 1
        if success:
            print(f"  ✅ {category} 页面访问正常")
            passed_tests += 1
        else:
            print(f"  ❌ {category} 页面访问失败 (状态码: {status})")
            failed_tests.append(f"{category} 页面: HTTP {status}")
    
    # 测试不存在的页面（应该返回404）
    print("🚫 测试404处理...")
    success, status, _ = test_url(BASE_URL + "/nonexistent-page.html", expected_status=404)
    total_tests += 1
    if success:
        print("  ✅ 404处理正常")
        passed_tests += 1
    else:
        print(f"  ⚠️  404处理异常 (状态码: {status})")
        failed_tests.append(f"404处理: 期望404，实际{status}")
    
    # 测试结果总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    
    success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"\n🔢 总体统计:")
    print(f"  总测试数: {total_tests}")
    print(f"  通过测试: {passed_tests}")
    print(f"  失败测试: {len(failed_tests)}")
    print(f"  成功率: {success_rate:.1f}%")
    
    if failed_tests:
        print(f"\n❌ 失败的测试:")
        for i, failure in enumerate(failed_tests, 1):
            print(f"  {i}. {failure}")
    
    # 测试建议
    print(f"\n💡 测试建议:")
    if success_rate == 100:
        print("  🎉 所有测试通过！多语言系统运行完美")
        print("  ✅ 可以进行生产环境部署")
    elif success_rate >= 90:
        print("  ✅ 大部分功能正常，少量问题需要修复")
        print("  🔧 建议修复失败的测试项目")
    elif success_rate >= 70:
        print("  ⚠️  基本功能正常，但有较多问题需要解决")
        print("  🔧 需要重点检查失败的测试项目")
    else:
        print("  ❌ 系统存在严重问题，需要全面检查")
        print("  🔧 建议重新部署或检查服务器配置")
    
    print(f"\n🌐 访问地址:")
    print(f"  主页: {BASE_URL}/index.html")
    print(f"  知识中心: {BASE_URL}/knowledge.html")
    print(f"  科学奇迹: {BASE_URL}/scientific-wonders.html")
    print(f"  中文文章示例: {BASE_URL}/zh/scientific-wonders/01-article.html")
    print(f"  日语文章示例: {BASE_URL}/ja/birdwatching/01-article.html")
    
    return success_rate == 100

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)