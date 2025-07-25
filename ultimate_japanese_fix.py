#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def fix_japanese_translation():
    """修复ja目录下所有HTML文件的日语翻译问题"""
    
    # 获取所有ja目录下的HTML文件
    html_files = glob.glob('ja/**/*.html', recursive=True)
    
    print(f"找到 {len(html_files)} 个HTML文件需要修复")
    
    # 定义修复规则
    fixes = [
        # 修复HTML属性
        (r'クラス="([^"]*)"', r'class="\1"'),
        (r'スタイル="([^"]*)"', r'style="\1"'),
        
        # 修复网站名称
        (r'BirdAiSnp', 'BirdAiSnap'),
        
        # 修复常见的机器翻译错误
        (r'でg\b', 'ing'),
        (r'でe\b', 'ne'),
        (r'でt\b', 'nt'),
        (r'でi\b', 'ni'),
        (r'でch\b', 'nch'),
        (r'でr\b', 'ner'),
        (r'でs\b', 'nes'),
        (r'でn\b', 'nen'),
        (r'でm\b', 'nem'),
        (r'でl\b', 'nel'),
        (r'でk\b', 'nek'),
        (r'でj\b', 'nej'),
        (r'でh\b', 'neh'),
        (r'でf\b', 'nef'),
        (r'でd\b', 'ned'),
        (r'でc\b', 'nec'),
        (r'でb\b', 'neb'),
        (r'でa\b', 'nea'),
        
        # 修复其他常见错误
        (r'進歩-br', 'progress-bar'),
        (r'進歩-fill', 'progress-fill'),
        (r'quote-テキスト', 'quote-text'),
        
        # 修复一些明显的英日混合问题
        (r'Bird Wでchでg のために Begでners', 'バードウォッチング初心者ガイド'),
        (r'Avi Biomechics Prでciples', '鳥類バイオメカニクスの原理'),
        (r'The Physiologicl Mircle の Mig比率n', '渡りの生理学的奇跡'),
        (r'Birds\' Complex Communicでiで Systems', '鳥類の複雑なコミュニケーションシステム'),
        (r'The Mircle の Bird Egg Development', '鳥の卵発達の奇跡'),
        (r'Birds\' Super Vですiで System', '鳥類の超視覚システム'),
        (r'The Microscopic Mircle の Fer Structure', '羽毛構造の微視的奇跡'),
    ]
    
    total_fixes = 0
    
    for file_path in html_files:
        try:
            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = 0
            
            # 应用所有修复规则
            for pattern, replacement in fixes:
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    matches = len(re.findall(pattern, content))
                    file_fixes += matches
                    content = new_content
            
            # 如果有修改，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"修复了 {file_path}: {file_fixes} 处修改")
                total_fixes += file_fixes
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    print(f"\n修复完成！总共修复了 {total_fixes} 处问题")

if __name__ == "__main__":
    fix_japanese_translation()