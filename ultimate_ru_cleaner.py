#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
终极俄语清理脚本 - 彻底处理ru目录下所有英文内容
"""

import os
import re
from pathlib import Path

def ultimate_clean_file(file_path):
    """终极清理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 直接字符串替换 - 最可靠的方法
        replacements = {
            # HTML标签内容 - 精确匹配
            'stat-label">Noise Level</div>': 'stat-label">Уровень шума</div>',
            'stat-label">Care Level</div>': 'stat-label">Уровень ухода</div>',
            'stat-value">Low-Moderate</div>': 'stat-value">Низкий-Средний</div>',
            'stat-value">Moderate</div>': 'stat-value">Средний</div>',
            'stat-value">Moderate-High</div>': 'stat-value">Средний-Высокий</div>',
            'stat-value">Very High</div>': 'stat-value">Очень высокий</div>',
            'stat-value">High</div>': 'stat-value">Высокий</div>',
            'stat-value">Low</div>': 'stat-value">Низкий</div>',
            'stat-value">Beginner</div>': 'stat-value">Начинающий</div>',
            'stat-value">Intermediate</div>': 'stat-value">Средний</div>',
            'stat-value">Advanced</div>': 'stat-value">Продвинутый</div>',
            'stat-value">Expert</div>': 'stat-value">Эксперт</div>',
            'stat-value">Beginner-friendly</div>': 'stat-value">Для начинающих</div>',
            'stat-value">Low to moderate</div>': 'stat-value">От низкого до среднего</div>',
            'stat-value">Moderate to high</div>': 'stat-value">От среднего до высокого</div>',
            'stat-value">Intermediate to advanced</div>': 'stat-value">От среднего до продвинутого</div>',
            'stat-value">Beginner to intermediate</div>': 'stat-value">От начинающего до среднего</div>',
            
            # 章节标题
            'section-title">Advanced Techniques</div>': 'section-title">Продвинутые техники</div>',
            'section-title">Intermediate Species</div>': 'section-title">Виды среднего уровня</div>',
            'section-title">Advanced Species</div>': 'section-title">Продвинутые виды</div>',
            'section-title">Beginner-Friendly Species</div>': 'section-title">Виды для начинающих</div>',
            'section-title">Choosing the Right Species</div>': 'section-title">Выбор подходящего вида</div>',
            
            # 提示框标题
            'tip-title">💡 Learning Tips for Beginners</div>': 'tip-title">💡 Советы по обучению для начинающих</div>',
            
            # 护理要求
            'care-title">Care Requirements:</div>': 'care-title">Требования по уходу:</div>',
            'care-title">Care Requirements</div>': 'care-title">Требования по уходу</div>',
            
            # 基本词汇
            '<strong>Care Level:</strong>': '<strong>Уровень ухода:</strong>',
            '<strong>Noise Level:</strong>': '<strong>Уровень шума:</strong>',
            '<strong>Personality:</strong>': '<strong>Личность:</strong>',
            'Care Level:': 'Уровень ухода:',
            'Noise Level:': 'Уровень шума:',
            'Personality:': 'Личность:',
            
            # 个性描述
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
            '<strong>Advanced Foraging Challenges:</strong>': '<strong>Продвинутые вызовы поиска пищи:</strong>',
            'Advanced Foraging Challenges:': 'Продвинутые вызовы поиска пищи:',
            'Multi-level puzzle feeders': 'Многоуровневые кормушки-головоломки',
            '<strong>Large Birds (Macaws, African Greys):</strong>': '<strong>Крупные птицы (ара, африканские серые):</strong>',
            'Large Birds (Macaws, African Greys):': 'Крупные птицы (ара, африканские серые):',
            'Advanced problem-solving puzzles': 'Продвинутые головоломки для решения проблем',
            'Large foraging opportunities': 'Большие возможности для поиска пищи',
            
            # 提示内容
            'Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.': 'Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.',
            
            # 单独的词汇 - 在特定上下文中
            'Beginner-friendly': 'Для начинающих',
            'Low-Moderate': 'Низкий-Средний',
            'Moderate-High': 'Средний-Высокий',
            'Very High': 'Очень высокий',
            'Low to moderate': 'От низкого до среднего',
            'Moderate to high': 'От среднего до высокого',
            'Intermediate to advanced': 'От среднего до продвинутого',
            'Beginner to intermediate': 'От начинающего до среднего',
        }
        
        # 应用所有替换
        for english, russian in replacements.items():
            content = content.replace(english, russian)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 终极清理完成: {file_path}")
            return True
        else:
            print(f"⏭️  无需清理: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 清理失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    ru_dir = Path('ru')
    
    if not ru_dir.exists():
        print("❌ ru目录不存在")
        return
    
    print("🚀 开始终极俄语清理...")
    
    # 查找所有HTML文件
    html_files = list(ru_dir.rglob('*.html'))
    
    cleaned_count = 0
    total_files = len(html_files)
    
    for file_path in html_files:
        if ultimate_clean_file(file_path):
            cleaned_count += 1
    
    print(f"\n📊 终极清理统计:")
    print(f"   总文件数: {total_files}")
    print(f"   已清理: {cleaned_count}")
    print(f"   无需清理: {total_files - cleaned_count}")
    print("🎉 终极俄语清理完成!")

if __name__ == "__main__":
    main()