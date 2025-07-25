#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日语翻译修复脚本
修复ja目录下所有HTML文件中的机器翻译错误
"""

import os
import re
import glob

def fix_japanese_html_file(file_path):
    """修复单个HTML文件的日语翻译问题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 修复HTML属性名的错误翻译
        content = re.sub(r'クラス="([^"]*)"', r'class="\1"', content)
        content = re.sub(r'スタイル="([^"]*)"', r'style="\1"', content)
        
        # 2. 修复常见的机器翻译错误字符组合
        error_patterns = {
            r'でg': 'ing',
            r'でe': 'the',
            r'でt': 'at',
            r'でi': 'in',
            r'でch': 'atch',
            r'でr': 'er',
            r'でs': 'es',
            r'でn': 'en',
            r'でm': 'em',
            r'でl': 'el',
            r'でk': 'ek',
            r'でj': 'ej',
            r'でh': 'eh',
            r'でf': 'ef',
            r'でd': 'ed',
            r'でc': 'ec',
            r'でb': 'eb',
            r'でa': 'ea'
        }
        
        # 3. 修复BirdAiSnp -> BirdAiSnap
        content = re.sub(r'BirdAiSnp', 'BirdAiSnap', content)
        
        # 4. 修复常见的英日混合问题
        mixed_patterns = {
            r'Bird Wでchでg': 'バードウォッチング',
            r'のために Begでners': 'のための初心者',
            r'年齢': '画像',  # 在图片路径中
            r'im年齢': 'image',
            r'進歩-br': 'progress-bar',
            r'進歩-fill': 'progress-fill',
            r'quote-テキスト': 'quote-text',
            r'tip-title': 'tip-title',
            r'ステップ-item': 'step-item',
            r'ステップ-数': 'step-number',
            r'鳥-車d': 'bird-card',
            r'鳥-im年齢-小さい': 'bird-image-small'
        }
        
        # 应用修复模式
        for pattern, replacement in error_patterns.items():
            content = re.sub(pattern, replacement, content)
            
        for pattern, replacement in mixed_patterns.items():
            content = re.sub(pattern, replacement, content)
        
        # 5. 修复常见的日语语法错误
        grammar_fixes = {
            r'です で': 'での',
            r'できます 飛ぶ': '飛ぶことができます',
            r'です について': 'について',
            r'です の': 'の',
            r'です と': 'と'
        }
        
        for pattern, replacement in grammar_fixes.items():
            content = re.sub(pattern, replacement, content)
        
        # 6. 修复标题中的常见错误
        title_fixes = {
            r'Bird Wでchでg のために Begでners': '初心者のためのバードウォッチング',
            r'Avi Biomechics Prでciples': '鳥類バイオメカニクスの原理',
            r'Birds\' Super Vですiで System': '鳥類の超視覚システム',
            r'The Mircle の Bird Egg Development': '鳥の卵発達の奇跡',
            r'Birds\' Complex Communicでiで Systems': '鳥類の複雑なコミュニケーションシステム',
            r'The Physiologicl Mircle の Mig比率n': '渡りの生理学的奇跡'
        }
        
        for pattern, replacement in title_fixes.items():
            content = re.sub(pattern, replacement, content)
        
        # 只有在内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 修复完成: {file_path}")
            return True
        else:
            print(f"⏭️  无需修复: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 修复失败 {file_path}: {str(e)}")
        return False

def main():
    """主函数"""
    print("🚀 开始修复ja目录下的日语翻译问题...")
    
    # 查找所有HTML文件
    html_files = glob.glob('ja/**/*.html', recursive=True)
    
    if not html_files:
        print("❌ 未找到ja目录下的HTML文件")
        return
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    
    fixed_count = 0
    total_count = len(html_files)
    
    # 处理每个文件
    for file_path in html_files:
        if fix_japanese_html_file(file_path):
            fixed_count += 1
    
    print(f"\n🎉 修复完成!")
    print(f"📊 总文件数: {total_count}")
    print(f"✅ 修复文件数: {fixed_count}")
    print(f"⏭️  无需修复: {total_count - fixed_count}")

if __name__ == "__main__":
    main()