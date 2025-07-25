#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
强力俄语翻译脚本 - 处理ru目录下所有顽固的英文内容
"""

import os
import re
from pathlib import Path

def aggressive_translate_file(file_path):
    """强力翻译单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 强力替换所有英文内容
        replacements = [
            # HTML标签内的英文
            (r'<div class="stat-label">Noise Level</div>', r'<div class="stat-label">Уровень шума</div>'),
            (r'<div class="stat-label">Care Level</div>', r'<div class="stat-label">Уровень ухода</div>'),
            (r'<div class="stat-value">Low-Moderate</div>', r'<div class="stat-value">Низкий-Средний</div>'),
            (r'<div class="stat-value">Moderate</div>', r'<div class="stat-value">Средний</div>'),
            (r'<div class="stat-value">Moderate-High</div>', r'<div class="stat-value">Средний-Высокий</div>'),
            (r'<div class="stat-value">Very High</div>', r'<div class="stat-value">Очень высокий</div>'),
            (r'<div class="stat-value">High</div>', r'<div class="stat-value">Высокий</div>'),
            (r'<div class="stat-value">Low</div>', r'<div class="stat-value">Низкий</div>'),
            (r'<div class="stat-value">Beginner</div>', r'<div class="stat-value">Начинающий</div>'),
            (r'<div class="stat-value">Intermediate</div>', r'<div class="stat-value">Средний</div>'),
            (r'<div class="stat-value">Advanced</div>', r'<div class="stat-value">Продвинутый</div>'),
            (r'<div class="stat-value">Expert</div>', r'<div class="stat-value">Эксперт</div>'),
            (r'<div class="stat-value">Beginner-friendly</div>', r'<div class="stat-value">Для начинающих</div>'),
            (r'<div class="stat-value">Low to moderate</div>', r'<div class="stat-value">От низкого до среднего</div>'),
            (r'<div class="stat-value">Moderate to high</div>', r'<div class="stat-value">От среднего до высокого</div>'),
            (r'<div class="stat-value">Intermediate to advanced</div>', r'<div class="stat-value">От среднего до продвинутого</div>'),
            (r'<div class="stat-value">Beginner to intermediate</div>', r'<div class="stat-value">От начинающего до среднего</div>'),
            
            # 章节标题
            (r'<div class="section-title">Advanced Techniques</div>', r'<div class="section-title">Продвинутые техники</div>'),
            (r'<div class="section-title">Intermediate Species</div>', r'<div class="section-title">Виды среднего уровня</div>'),
            (r'<div class="section-title">Advanced Species</div>', r'<div class="section-title">Продвинутые виды</div>'),
            (r'<div class="section-title">Beginner-Friendly Species</div>', r'<div class="section-title">Виды для начинающих</div>'),
            (r'<div class="section-title">Choosing the Right Species</div>', r'<div class="section-title">Выбор подходящего вида</div>'),
            
            # 提示框标题
            (r'<div class="tip-title">💡 Learning Tips for Beginners</div>', r'<div class="tip-title">💡 Советы по обучению для начинающих</div>'),
            
            # 护理要求
            (r'<div class="care-title">Care Requirements:</div>', r'<div class="care-title">Требования по уходу:</div>'),
            (r'<div class="care-title">Care Requirements</div>', r'<div class="care-title">Требования по уходу</div>'),
            
            # 基本词汇
            (r'Care Level:', r'Уровень ухода:'),
            (r'Noise Level:', r'Уровень шума:'),
            (r'Personality:', r'Личность:'),
            
            # 个性描述
            (r'Social, playful, can learn to talk', r'Социальные, игривые, могут научиться говорить'),
            (r'Gentle, affectionate, whistlers', r'Нежные, ласковые, свистуны'),
            (r'Energetic, playful, can be territorial', r'Энергичные, игривые, могут быть территориальными'),
            (r'Independent, excellent singers', r'Независимые, отличные певцы'),
            (r'Playful, loud, affectionate', r'Игривые, громкие, ласковые'),
            (r'Highly intelligent, can be sensitive', r'Очень умные, могут быть чувствительными'),
            
            # 描述文本
            (r"Perfect for first-time bird owners\. They're social, relatively quiet, and can learn simple words and tricks\.", r"Идеально подходят для начинающих владельцев птиц. Они социальны, относительно тихи и могут выучить простые слова и трюки."),
            (r"Known for their distinctive crest and gentle nature\. They're excellent whistlers and can learn melodies\.", r"Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии."),
            (r"Colorful and energetic birds that do well in pairs\. They're active and require plenty of toys and stimulation\.", r"Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции."),
            (r"Beautiful singers that don't require as much social interaction\. Perfect for those who enjoy bird songs\.", r"Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями."),
            (r"Colorful, playful birds with big personalities\. They can be quite loud and require experienced owners\.", r"Красочные, игривые птицы с большими личностями. Они могут быть довольно громкими и требуют опытных владельцев."),
            (r"Extremely intelligent birds that require experienced owners and consistent mental stimulation\.", r"Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции."),
            
            # 高级觅食挑战
            (r'Advanced Foraging Challenges:', r'Продвинутые вызовы поиска пищи:'),
            (r'Multi-level puzzle feeders', r'Многоуровневые кормушки-головоломки'),
            (r'Large Birds \(Macaws, African Greys\):', r'Крупные птицы (ара, африканские серые):'),
            (r'Advanced problem-solving puzzles', r'Продвинутые головоломки для решения проблем'),
            (r'Large foraging opportunities', r'Большие возможности для поиска пищи'),
            
            # 提示内容
            (r'Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe\.', r'Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.'),
            
            # 单独的词汇
            (r'\bBeginner\b', r'Начинающий'),
            (r'\bIntermediate\b', r'Средний'),
            (r'\bAdvanced\b', r'Продвинутый'),
            (r'\bExpert\b', r'Эксперт'),
            (r'\bModerate\b', r'Средний'),
            (r'\bHigh\b', r'Высокий'),
            (r'\bLow\b', r'Низкий'),
        ]
        
        # 应用所有替换
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 强力翻译完成: {file_path}")
            return True
        else:
            print(f"⏭️  无需翻译: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 翻译失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    ru_dir = Path('ru')
    
    if not ru_dir.exists():
        print("❌ ru目录不存在")
        return
    
    print("🚀 开始强力俄语翻译...")
    
    # 查找所有HTML文件
    html_files = list(ru_dir.rglob('*.html'))
    
    translated_count = 0
    total_files = len(html_files)
    
    for file_path in html_files:
        if aggressive_translate_file(file_path):
            translated_count += 1
    
    print(f"\n📊 强力翻译统计:")
    print(f"   总文件数: {total_files}")
    print(f"   已翻译: {translated_count}")
    print(f"   无需翻译: {total_files - translated_count}")
    print("🎉 强力俄语翻译完成!")

if __name__ == "__main__":
    main()