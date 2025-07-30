#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

def extract_title_and_content(file_path):
    """提取文件的标题和主要内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # 提取标题
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else "No title"
        
        # 提取主要内容文本
        # 查找主要内容区域
        main_content = ""
        
        # 尝试找到h1标题
        h1_tag = soup.find('h1')
        h1_text = h1_tag.text if h1_tag else ""
        
        # 提取前200个字符的主要文本内容
        text_content = soup.get_text()
        # 清理多余的空白
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        main_content = text_content[:200] + "..." if len(text_content) > 200 else text_content
        
        return {
            'title': title,
            'h1': h1_text,
            'content_preview': main_content
        }
    except Exception as e:
        return {
            'title': f"Error: {e}",
            'h1': "",
            'content_preview': ""
        }

def check_language_content():
    """检查多语言内容是否正确"""
    languages = ['en', 'zh', 'ko', 'ja', 'de', 'fr', 'es', 'it', 'pt', 'ru']
    categories = ['knowledge', 'birdwatching', 'pet-care', 'scientific-wonders', 'ecology']
    
    # 检查具体文件
    test_files = [
        '02-essential-equipment.html',
        '01-beginners-guide.html',
        '03-identification-techniques.html'
    ]
    
    language_indicators = {
        'en': ['Bird', 'Equipment', 'Guide', 'the', 'and', 'or'],
        'zh': ['鸟', '设备', '指南', '的', '和', '或'],
        'ko': ['새', '장비', '가이드', '의', '와', '또는'],
        'ja': ['鳥', '機材', 'ガイド', 'の', 'と', 'または'],
        'de': ['Vogel', 'Ausrüstung', 'Führer', 'der', 'und', 'oder'],
        'fr': ['Oiseau', 'Équipement', 'Guide', 'le', 'et', 'ou'],
        'es': ['Ave', 'Equipo', 'Guía', 'el', 'y', 'o'],
        'it': ['Uccello', 'Attrezzatura', 'Guida', 'il', 'e', 'o'],
        'pt': ['Ave', 'Equipamento', 'Guia', 'o', 'e', 'ou'],
        'ru': ['Птица', 'Оборудование', 'Руководство', 'и', 'или', 'для']
    }
    
    print("🔍 检查多语言内容正确性...")
    print("=" * 80)
    
    issues_found = []
    
    for lang in languages:
        print(f"\n📋 检查语言: {lang}")
        print("-" * 40)
        
        for category in categories:
            for test_file in test_files:
                file_path = f"{lang}/{category}/{test_file}"
                
                if os.path.exists(file_path):
                    content_info = extract_title_and_content(file_path)
                    
                    # 检查内容是否包含正确语言的指示词
                    content_text = content_info['title'] + " " + content_info['h1'] + " " + content_info['content_preview']
                    
                    # 计算当前语言指示词的出现次数
                    current_lang_count = sum(1 for word in language_indicators[lang] if word in content_text)
                    
                    # 检查是否包含其他语言的指示词
                    other_lang_words = []
                    for other_lang, words in language_indicators.items():
                        if other_lang != lang:
                            for word in words:
                                if word in content_text and word not in language_indicators[lang]:
                                    other_lang_words.append(f"{word}({other_lang})")
                    
                    status = "✅ 正确" if current_lang_count > 0 and len(other_lang_words) < 3 else "❌ 异常"
                    
                    print(f"  {category}/{test_file}: {status}")
                    
                    if status == "❌ 异常":
                        issue = {
                            'file': file_path,
                            'title': content_info['title'],
                            'current_lang_indicators': current_lang_count,
                            'other_lang_words': other_lang_words[:5]  # 只显示前5个
                        }
                        issues_found.append(issue)
                        print(f"    标题: {content_info['title'][:100]}...")
                        if other_lang_words:
                            print(f"    发现其他语言词汇: {', '.join(other_lang_words[:3])}")
    
    print("\n" + "=" * 80)
    print(f"🏁 检查完成！发现 {len(issues_found)} 个问题文件")
    
    if issues_found:
        print("\n❌ 问题文件详情:")
        for i, issue in enumerate(issues_found[:10], 1):  # 只显示前10个
            print(f"{i}. {issue['file']}")
            print(f"   标题: {issue['title'][:80]}...")
            if issue['other_lang_words']:
                print(f"   包含其他语言: {', '.join(issue['other_lang_words'])}")
            print()
    else:
        print("✅ 所有文件语言内容正确！")

if __name__ == "__main__":
    check_language_content() 