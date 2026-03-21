#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复包含列表的未翻译段落 - 使用DeepSeek API"""

import re
import sys
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_KEY = "sk-74142abf4d524e739abea8868b319adb"
API_URL = "https://api.deepseek.com/v1/chat/completions"

LANGUAGES = {
    'de': 'German',
    'es': 'Spanish',
    'fr': 'French',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian'
}

# 线程锁
print_lock = threading.Lock()
stats = {'total': 0, 'success': 0, 'failed': 0}
stats_lock = threading.Lock()

def safe_print(*args, **kwargs):
    """线程安全的打印"""
    with print_lock:
        print(*args, **kwargs)

def translate_html_content(html_text, target_lang):
    """翻译包含HTML的内容，保留标签"""
    if not html_text or len(html_text.strip()) < 10:
        return html_text
    
    lang_name = LANGUAGES.get(target_lang, target_lang)
    
    # 提示词：要求保留HTML标签，只翻译文本
    prompt = f"""Translate the following HTML content to {lang_name}. 
IMPORTANT: Keep ALL HTML tags (<ul>, <li>, <strong>, etc.) EXACTLY as they are. 
Only translate the text content inside the tags.

Content to translate:
{html_text}

Translated content (keep HTML tags unchanged):"""
    
    for attempt in range(3):  # 最多重试3次
        try:
            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.3,
                    "max_tokens": 4000
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()['choices'][0]['message']['content'].strip()
                # 移除可能的markdown代码块标记
                result = re.sub(r'^```html\s*', '', result)
                result = re.sub(r'\s*```$', '', result)
                return result.strip()
            
        except Exception as e:
            if attempt == 2:
                safe_print(f"    ❌ 翻译失败: {str(e)[:100]}")
            time.sleep(1)
    
    return html_text  # 失败返回原文

def fix_article(file_path, lang_code):
    """修复单篇文章"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 查找所有包含列表的段落
        paragraphs_with_lists = re.findall(
            r'<p[^>]*>(.*?<ul>.*?</ul>.*?)</p>',
            html,
            re.DOTALL
        )
        
        if not paragraphs_with_lists:
            return True, "无需修复"
        
        # 翻译每个包含列表的段落
        for para_content in paragraphs_with_lists:
            # 检查是否已经翻译（检测英文特征）
            english_count = len(re.findall(
                r'\b(the|and|are|that|with|from|have|they|which|their|when|what)\b',
                para_content,
                re.IGNORECASE
            ))
            
            if english_count < 5:
                continue  # 已翻译，跳过
            
            # 翻译这个段落
            translated_para = translate_html_content(para_content, lang_code)
            
            # 替换原段落
            html = html.replace(para_content, translated_para)
            time.sleep(0.5)  # 避免API限流
        
        # 保存修改后的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return True, f"修复了 {len(paragraphs_with_lists)} 个段落"
    
    except Exception as e:
        return False, str(e)

def process_file(args):
    """处理单个文件"""
    file_path, lang_code, idx, total = args
    
    with stats_lock:
        stats['total'] += 1
    
    safe_print(f"  [{idx}/{total}] 处理: {file_path.name[:50]}...")
    
    success, message = fix_article(file_path, lang_code)
    
    with stats_lock:
        if success:
            stats['success'] += 1
            status = "✅"
        else:
            stats['failed'] += 1
            status = "❌"
    
    safe_print(f"    {status} {message}")
    
    return success

def main():
    print("=" * 80)
    print("🔧 修复未翻译的列表段落 - DeepSeek API")
    print("=" * 80)
    print()
    
    # 读取修复列表
    for lang_code, lang_name in LANGUAGES.items():
        fix_list_file = f"fix_list_{lang_code}.txt"
        
        if not Path(fix_list_file).exists():
            safe_print(f"⚠️  {lang_name}: 未找到修复列表文件")
            continue
        
        with open(fix_list_file, 'r', encoding='utf-8') as f:
            file_list = [line.strip() for line in f if line.strip()]
        
        if not file_list:
            continue
        
        safe_print(f"\n{'='*70}")
        safe_print(f"🚀 {lang_name} ({lang_code}) - 修复 {len(file_list)} 篇文章")
        safe_print(f"{'='*70}\n")
        
        # 准备任务
        tasks = []
        for i, rel_path in enumerate(file_list, 1):
            file_path = Path(f"insect/{lang_code}/{rel_path}")
            if file_path.exists():
                tasks.append((file_path, lang_code, i, len(file_list)))
        
        # 多线程处理
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(process_file, task) for task in tasks]
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    safe_print(f"    ❌ 线程错误: {e}")
        
        elapsed = time.time() - start_time
        safe_print(f"\n  ⏱️  {lang_name} 完成，用时: {elapsed/60:.1f}分钟")
    
    # 总结
    print("\n" + "=" * 80)
    print("📊 修复统计")
    print("=" * 80)
    print(f"✅ 成功: {stats['success']}")
    print(f"❌ 失败: {stats['failed']}")
    print(f"📝 总计: {stats['total']}")
    print("=" * 80)

if __name__ == '__main__':
    main()

