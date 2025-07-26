#!/usr/bin/env python3
import os
import re
from pathlib import Path

def remove_back_buttons():
    """移除所有文章中的返回键"""
    
    languages = ['en', 'zh', 'de', 'ja', 'ko', 'fr', 'es', 'it', 'pt', 'ru']
    modified_files = []
    
    for lang in languages:
        lang_dir = Path(lang)
        if not lang_dir.exists():
            continue
            
        print(f"处理 {lang} 语言版本...")
        
        # 遍历所有HTML文件
        for html_file in lang_dir.rglob('*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 移除返回按钮相关的CSS样式
                content = re.sub(r'\.back-button\s*\{[^}]*\}', '', content, flags=re.DOTALL)
                
                # 移除返回按钮的HTML元素
                content = re.sub(r'<button[^>]*class="back-button"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
                content = re.sub(r'<!--[^>]*返回[^>]*-->\s*<button[^>]*onclick="history\.back\(\)"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
                content = re.sub(r'<!--[^>]*戻る[^>]*-->\s*<button[^>]*onclick="history\.back\(\)"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
                content = re.sub(r'<!--[^>]*Zurück[^>]*-->\s*<button[^>]*onclick="history\.back\(\)"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
                content = re.sub(r'<!--[^>]*Back[^>]*-->\s*<button[^>]*onclick="history\.back\(\)"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
                
                # 清理多余的空行
                content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
                
                if content != original_content:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    modified_files.append(str(html_file))
                    print(f"  ✅ 已移除返回键: {html_file}")
                    
            except Exception as e:
                print(f"  ❌ 处理文件 {html_file} 时出错: {e}")
    
    print(f"\n=== 移除返回键完成 ===")
    print(f"共修改了 {len(modified_files)} 个文件")
    
    return modified_files

if __name__ == "__main__":
    remove_back_buttons()