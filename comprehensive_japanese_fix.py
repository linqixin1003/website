#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面的日语翻译修复脚本
修复ja目录下所有HTML文件中的机器翻译错误
"""

import os
import re
import glob

def comprehensive_fix_japanese_file(file_path):
    """全面修复单个HTML文件的日语翻译问题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 修复HTML属性名的错误翻译
        content = re.sub(r'クラス="([^"]*)"', r'class="\1"', content)
        content = re.sub(r'スタイル="([^"]*)"', r'style="\1"', content)
        
        # 2. 修复BirdAiSnp -> BirdAiSnap
        content = re.sub(r'BirdAiSnp', 'BirdAiSnap', content)
        
        # 3. 修复常见的机器翻译错误字符组合 - 更全面的模式
        error_patterns = [
            (r'でg\b', 'ing'),
            (r'でe\b', 'the'),
            (r'でt\b', 'at'),
            (r'でi\b', 'in'),
            (r'でch\b', 'atch'),
            (r'でr\b', 'er'),
            (r'でs\b', 'es'),
            (r'でn\b', 'en'),
            (r'でm\b', 'em'),
            (r'でl\b', 'el'),
            (r'でk\b', 'ek'),
            (r'でj\b', 'ej'),
            (r'でh\b', 'eh'),
            (r'でf\b', 'ef'),
            (r'でd\b', 'ed'),
            (r'でc\b', 'ec'),
            (r'でb\b', 'eb'),
            (r'でa\b', 'ea'),
            (r'でy\b', 'ey'),
            (r'でu\b', 'eu'),
            (r'でo\b', 'eo'),
            (r'でp\b', 'ep'),
            (r'でv\b', 'ev'),
            (r'でw\b', 'ew'),
            (r'でx\b', 'ex'),
            (r'でz\b', 'ez')
        ]
        
        # 4. 修复更多的英日混合问题
        mixed_patterns = [
            (r'Bird Wでchでg', 'バードウォッチング'),
            (r'のために Begでners', 'のための初心者'),
            (r'年齢', '画像'),  # 在图片路径中
            (r'im年齢', 'image'),
            (r'進歩-br', 'progress-bar'),
            (r'進歩-fill', 'progress-fill'),
            (r'quote-テキスト', 'quote-text'),
            (r'tip-title', 'tip-title'),
            (r'ステップ-item', 'step-item'),
            (r'ステップ-数', 'step-number'),
            (r'鳥-車d', 'bird-card'),
            (r'鳥-im年齢-小さい', 'bird-image-small'),
            (r'bckground-im年齢', 'background-image'),
            (r'Avi Biomechics Prでciples', '鳥類バイオメカニクスの原理'),
            (r'Birds\' Super Vですiで System', '鳥類の超視覚システム'),
            (r'The Mircle の Bird Egg Development', '鳥の卵発達の奇跡'),
            (r'Birds\' Complex Communicでiで Systems', '鳥類の複雑なコミュニケーションシステム'),
            (r'The Physiologicl Mircle の Mig比率n', '渡りの生理学的奇跡'),
            (r'The Microscopic Mircle の Fer Structure', '羽毛構造の微視的奇跡')
        ]
        
        # 5. 修复常见的日语语法错误
        grammar_fixes = [
            (r'です で', 'での'),
            (r'できます 飛ぶ', '飛ぶことができます'),
            (r'です について', 'について'),
            (r'です の', 'の'),
            (r'です と', 'と'),
            (r'です から', 'から'),
            (r'です に', 'に'),
            (r'です を', 'を'),
            (r'です が', 'が'),
            (r'です は', 'は'),
            (r'です も', 'も')
        ]
        
        # 6. 修复更多的错误翻译词汇
        vocabulary_fixes = [
            (r'所有する', '持つ'),
            (r'年齢', '歳'),
            (r'権利', '正しい'),
            (r'車d', 'カード'),
            (r'車bohyd率s', '炭水化物'),
            (r'車til年齢', '軟骨'),
            (r'芸術ificil', '人工的な'),
            (r'楽しみctiで', '機能'),
            (r'配偶者', 'パートナー'),
            (r'比率', 'tion'),
            (r'率', 'rate'),
            (r'座る', 'sit'),
            (r'食べる', 'eat'),
            (r'打つ', 'hit'),
            (r'休む', 'rest'),
            (r'得る', 'get'),
            (r'作る', 'make'),
            (r'来る', 'come'),
            (r'行く', 'go'),
            (r'見る', 'see'),
            (r'聞く', 'hear'),
            (r'話す', 'speak'),
            (r'歩く', 'walk'),
            (r'走る', 'run'),
            (r'飛ぶ', 'fly'),
            (r'泳ぐ', 'swim')
        ]
        
        # 应用所有修复模式
        for pattern, replacement in error_patterns:
            content = re.sub(pattern, replacement, content)
            
        for pattern, replacement in mixed_patterns:
            content = re.sub(pattern, replacement, content)
            
        for pattern, replacement in grammar_fixes:
            content = re.sub(pattern, replacement, content)
            
        for pattern, replacement in vocabulary_fixes:
            content = re.sub(pattern, replacement, content)
        
        # 7. 修复特定的标题翻译
        title_translations = {
            'Avi Biomechics Prでciples': '鳥類バイオメカニクスの原理',
            'Birds\' Super Vですiで System': '鳥類の超視覚システム',
            'The Mircle の Bird Egg Development': '鳥の卵発達の奇跡',
            'Birds\' Complex Communicでiで Systems': '鳥類の複雑なコミュニケーションシステム',
            'The Physiologicl Mircle の Mig比率n': '渡りの生理学的奇跡',
            'The Microscopic Mircle の Fer Structure': '羽毛構造の微視的奇跡'
        }
        
        for english_title, japanese_title in title_translations.items():
            content = re.sub(re.escape(english_title), japanese_title, content)
        
        # 8. 清理剩余的错误模式
        cleanup_patterns = [
            (r'[でが]{2,}', 'で'),  # 重复的で
            (r'です{2,}', 'です'),   # 重复的です
            (r'と{2,}', 'と'),      # 重复的と
            (r'の{2,}', 'の'),      # 重复的の
            (r'に{2,}', 'に'),      # 重复的に
            (r'を{2,}', 'を'),      # 重复的を
            (r'が{2,}', 'が'),      # 重复的が
            (r'は{2,}', 'は'),      # 重复的は
            (r'も{2,}', 'も')       # 重复的も
        ]
        
        for pattern, replacement in cleanup_patterns:
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
    print("🚀 开始全面修复ja目录下的日语翻译问题...")
    
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
        if comprehensive_fix_japanese_file(file_path):
            fixed_count += 1
    
    print(f"\n🎉 全面修复完成!")
    print(f"📊 总文件数: {total_count}")
    print(f"✅ 修复文件数: {fixed_count}")
    print(f"⏭️  无需修复: {total_count - fixed_count}")

if __name__ == "__main__":
    main()