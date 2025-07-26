#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path

def convert_png_to_webp():
    """将PNG格式的图片引用转换为WebP格式"""
    
    # 语言目录
    languages = ['en', 'zh', 'de', 'ja', 'ko', 'fr', 'es', 'it', 'pt', 'ru']
    
    converted_files = []
    
    for lang in languages:
        lang_dir = Path(lang)
        if not lang_dir.exists():
            continue
            
        print(f"\n处理 {lang} 语言版本...")
        
        # 遍历所有HTML文件
        for html_file in lang_dir.rglob('*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 替换所有PNG引用为WebP
                # 匹配各种图片引用模式
                patterns = [
                    # src="...png" -> src="...webp"
                    (r'src=["\']([^"\']*\.png)["\']', lambda m: f'src="{m.group(1)[:-4]}.webp"'),
                    # url('...png') -> url('...webp')
                    (r'url\(["\']?([^"\']*\.png)["\']?\)', lambda m: f'url("{m.group(1)[:-4]}.webp")'),
                    # background: url(...png) -> background: url(...webp)
                    (r'(background[^:]*:[^;]*url\(["\']?)([^"\']*\.png)(["\']?\))', 
                     lambda m: f'{m.group(1)}{m.group(2)[:-4]}.webp{m.group(3)}'),
                ]
                
                for pattern, replacement in patterns:
                    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                
                # 如果内容有变化，保存文件
                if content != original_content:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    converted_files.append(str(html_file))
                    print(f"  ✅ 已转换: {html_file}")
                    
            except Exception as e:
                print(f"  ❌ 处理文件 {html_file} 时出错: {e}")
    
    # 处理JSON配置文件
    json_files = [
        'android-article-urls.json',
        'android-article-urls-en.json',
        'android-article-urls-zh.json',
        'android-article-urls-de.json',
        'android-article-urls-ja.json',
        'android-article-urls-ko.json',
        'android-article-urls-fr.json',
        'android-article-urls-es.json',
        'android-article-urls-it.json',
        'android-article-urls-pt.json',
        'android-article-urls-ru.json'
    ]
    
    print(f"\n处理JSON配置文件...")
    
    for json_file in json_files:
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                modified = False
                
                for article in data:
                    if 'imageUrl' in article and article['imageUrl'].endswith('.png'):
                        article['imageUrl'] = article['imageUrl'][:-4] + '.webp'
                        modified = True
                
                if modified:
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    converted_files.append(json_file)
                    print(f"  ✅ 已转换: {json_file}")
                    
            except Exception as e:
                print(f"  ❌ 处理JSON文件 {json_file} 时出错: {e}")
    
    print(f"\n=== 转换完成 ===")
    print(f"共转换了 {len(converted_files)} 个文件")
    
    if converted_files:
        print(f"\n转换的文件列表:")
        for file in converted_files:
            print(f"  - {file}")
    
    return converted_files

if __name__ == "__main__":
    converted_files = convert_png_to_webp()