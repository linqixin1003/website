#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path

def check_image_formats():
    """检查所有文章中的图片格式"""
    
    # 语言目录
    languages = ['en', 'zh', 'de', 'ja', 'ko', 'fr', 'es', 'it', 'pt', 'ru']
    
    png_images = []
    webp_images = []
    
    for lang in languages:
        lang_dir = Path(lang)
        if not lang_dir.exists():
            continue
            
        print(f"\n检查 {lang} 语言版本...")
        
        # 遍历所有HTML文件
        for html_file in lang_dir.rglob('*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找所有图片引用
                # 匹配 src="..." 和 url('...') 中的图片
                img_patterns = [
                    r'src=["\']([^"\']*\.(png|webp))["\']',
                    r'url\(["\']?([^"\']*\.(png|webp))["\']?\)',
                    r'background[^:]*:[^;]*url\(["\']?([^"\']*\.(png|webp))["\']?\)'
                ]
                
                for pattern in img_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for match in matches:
                        if isinstance(match, tuple):
                            img_path = match[0]
                            ext = match[1].lower()
                        else:
                            img_path = match
                            ext = img_path.split('.')[-1].lower()
                        
                        if ext == 'png':
                            png_images.append({
                                'file': str(html_file),
                                'image': img_path
                            })
                        elif ext == 'webp':
                            webp_images.append({
                                'file': str(html_file),
                                'image': img_path
                            })
                            
            except Exception as e:
                print(f"处理文件 {html_file} 时出错: {e}")
    
    # 检查JSON配置文件
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
    
    for json_file in json_files:
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                for article in data:
                    if 'imageUrl' in article:
                        img_url = article['imageUrl']
                        if img_url.endswith('.png'):
                            png_images.append({
                                'file': json_file,
                                'image': img_url,
                                'article_id': article.get('id', 'unknown')
                            })
                        elif img_url.endswith('.webp'):
                            webp_images.append({
                                'file': json_file,
                                'image': img_url,
                                'article_id': article.get('id', 'unknown')
                            })
                            
            except Exception as e:
                print(f"处理JSON文件 {json_file} 时出错: {e}")
    
    # 输出结果
    print(f"\n=== 图片格式检查结果 ===")
    print(f"发现 {len(png_images)} 个PNG格式图片")
    print(f"发现 {len(webp_images)} 个WebP格式图片")
    
    if png_images:
        print(f"\n需要转换为WebP格式的PNG图片:")
        for item in png_images[:20]:  # 只显示前20个
            print(f"  文件: {item['file']}")
            print(f"  图片: {item['image']}")
            if 'article_id' in item:
                print(f"  文章ID: {item['article_id']}")
            print()
        
        if len(png_images) > 20:
            print(f"  ... 还有 {len(png_images) - 20} 个PNG图片")
    
    return png_images, webp_images

if __name__ == "__main__":
    png_images, webp_images = check_image_formats()