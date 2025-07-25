#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终俄语翻译脚本 - 处理ru目录下所有剩余的英文内容
"""

import os
import re
from pathlib import Path

# 最终翻译字典 - 包含所有剩余的英文内容
FINAL_TRANSLATIONS = {
    # HTML标签内容
    'stat-label">Noise Level': 'stat-label">Уровень шума',
    'stat-label">Care Level': 'stat-label">Уровень ухода',
    'stat-value">Low-Moderate': 'stat-value">Низкий-Средний',
    'stat-value">Moderate': 'stat-value">Средний',
    'stat-value">Moderate-High': 'stat-value">Средний-Высокий',
    'stat-value">Very High': 'stat-value">Очень высокий',
    'stat-value">High': 'stat-value">Высокий',
    'stat-value">Low': 'stat-value">Низкий',
    'stat-value">Beginner': 'stat-value">Начинающий',
    'stat-value">Intermediate': 'stat-value">Средний',
    'stat-value">Advanced': 'stat-value">Продвинутый',
    'stat-value">Expert': 'stat-value">Эксперт',
    'stat-value">Beginner-friendly': 'stat-value">Для начинающих',
    'stat-value">Low to moderate': 'stat-value">От низкого до среднего',
    'stat-value">Moderate to high': 'stat-value">От среднего до высокого',
    'stat-value">Intermediate to advanced': 'stat-value">От среднего до продвинутого',
    
    # 基本词汇
    'Care Level:': 'Уровень ухода:',
    'Noise Level:': 'Уровень шума:',
    'Care Level': 'Уровень ухода',
    'Noise Level': 'Уровень шума',
    'Beginner': 'Начинающий',
    'Intermediate': 'Средний',
    'Advanced': 'Продвинутый',
    'Expert': 'Эксперт',
    'Beginner-friendly': 'Для начинающих',
    'Low-Moderate': 'Низкий-Средний',
    'Moderate': 'Средний',
    'Moderate-High': 'Средний-Высокий',
    'Very High': 'Очень высокий',
    'High': 'Высокий',
    'Low': 'Низкий',
    'Low to moderate': 'От низкого до среднего',
    'Moderate to high': 'От среднего до высокого',
    'Intermediate to advanced': 'От среднего до продвинутого',
    'Beginner to intermediate': 'От начинающего до среднего',
    
    # 章节标题
    'section-title">Advanced Techniques': 'section-title">Продвинутые техники',
    'section-title">Intermediate Species': 'section-title">Виды среднего уровня',
    'section-title">Advanced Species': 'section-title">Продвинутые виды',
    'section-title">Beginner-Friendly Species': 'section-title">Виды для начинающих',
    'section-title">Choosing the Right Species': 'section-title">Выбор подходящего вида',
    
    # 提示框标题
    'tip-title">💡 Learning Tips for Beginners': 'tip-title">💡 Советы по обучению для начинающих',
    
    # 护理要求
    'care-title">Care Requirements:': 'care-title">Требования по уходу:',
    'care-title">Care Requirements': 'care-title">Требования по уходу',
    
    # 个性描述
    'Personality:': 'Личность:',
    'Social, playful, can learn to talk': 'Социальные, игривые, могут научиться говорить',
    'Gentle, affectionate, whistlers': 'Нежные, ласковые, свистуны',
    'Energetic, playful, can be territorial': 'Энергичные, игривые, могут быть территориальными',
    'Independent, excellent singers': 'Независимые, отличные певцы',
    'Playful, loud, affectionate': 'Игривые, громкие, ласковые',
    'Highly intelligent, can be sensitive': 'Очень умные, могут быть чувствительными',
    
    # 描述文本
    "Perfect for first-time bird owners. They're social, relatively quiet, and can learn simple words and tricks.": "Идеально подходят для начинающих владельцев птиц. Они социальны, относительно тихи и могут выучить простые слова и трюки.",
    "Known for their distinctive crest and gentle nature. They're excellent whistlers and can learn melodies.": "Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии.",
    "Colorful and energetic birds that do well in pairs. They're active and require plenty of toys and stimulation.": "Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции.",
    "Beautiful singers that don't require as much social interaction. Perfect for those who enjoy bird songs.": "Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями.",
    "Colorful, playful birds with big personalities. They can be quite loud and require experienced owners.": "Красочные, игривые птицы с большими личностями. Они могут быть довольно громкими и требуют опытных владельцев.",
    "Extremely intelligent birds that require experienced owners and consistent mental stimulation.": "Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции.",
    
    # 高级觅食挑战
    'Advanced Foraging Challenges:': 'Продвинутые вызовы поиска пищи:',
    'Multi-level puzzle feeders': 'Многоуровневые кормушки-головоломки',
    'Large Birds (Macaws, African Greys):': 'Крупные птицы (ара, африканские серые):',
    'Advanced problem-solving puzzles': 'Продвинутые головоломки для решения проблем',
    'Large foraging opportunities': 'Большие возможности для поиска пищи',
    
    # 提示内容
    'Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.': 'Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.',
}

def translate_file(file_path):
    """翻译单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用所有翻译
        for english, russian in FINAL_TRANSLATIONS.items():
            content = content.replace(english, russian)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 翻译完成: {file_path}")
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
    
    print("🚀 开始最终俄语翻译...")
    
    # 查找所有HTML文件
    html_files = list(ru_dir.rglob('*.html'))
    
    translated_count = 0
    total_files = len(html_files)
    
    for file_path in html_files:
        if translate_file(file_path):
            translated_count += 1
    
    print(f"\n📊 翻译统计:")
    print(f"   总文件数: {total_files}")
    print(f"   已翻译: {translated_count}")
    print(f"   无需翻译: {total_files - translated_count}")
    print("🎉 最终俄语翻译完成!")

if __name__ == "__main__":
    main()