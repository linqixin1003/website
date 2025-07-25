#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
强制俄语翻译脚本 - 使用正则表达式处理所有英文内容
"""

import os
import re
from pathlib import Path

def force_translate_file(file_path):
    """强制翻译文件中的所有英文内容"""
    print(f"强制翻译文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 使用正则表达式替换所有英文内容
        replacements = [
            # HTML标签内的英文
            (r'<div class="stat-label">Noise Level</div>', r'<div class="stat-label">Уровень шума</div>'),
            (r'<div class="stat-label">Care Level</div>', r'<div class="stat-label">Уровень ухода</div>'),
            (r'<div class="stat-value">([^<]*)</div>', lambda m: f'<div class="stat-value">{translate_value(m.group(1))}</div>'),
            (r'<div class="section-title">([^<]*)</div>', lambda m: f'<div class="section-title">{translate_section_title(m.group(1))}</div>'),
            (r'<div class="tip-title">([^<]*)</div>', lambda m: f'<div class="tip-title">{translate_tip_title(m.group(1))}</div>'),
            
            # 强标签内的英文
            (r'<strong>Care Level:</strong>', r'<strong>Уровень ухода:</strong>'),
            (r'<strong>Noise Level:</strong>', r'<strong>Уровень шума:</strong>'),
            (r'<strong>Personality:</strong>', r'<strong>Личность:</strong>'),
            (r'<strong>Experience Level Matching:</strong>', r'<strong>Соответствие уровню опыта:</strong>'),
            (r'<strong>Advanced Foraging Challenges:</strong>', r'<strong>Продвинутые вызовы поиска пищи:</strong>'),
            (r'<strong>Large Birds \(Macaws, African Greys\):</strong>', r'<strong>Крупные птицы (ара, африканские серые):</strong>'),
            
            # 列表项
            (r'• Beginners: Budgies, canaries, cockatiels', r'• Начинающие: волнистые попугайчики, канарейки, кореллы'),
            (r'• Intermediate: Lovebirds, small conures, parrotlets', r'• Средний уровень: неразлучники, маленькие конуры, попугайчики'),
            (r'• Advanced: Large conures, small macaws, amazons', r'• Продвинутый: крупные конуры, маленькие ара, амазоны'),
            (r'• Expert: African greys, large macaws, cockatoos', r'• Эксперт: африканские серые, крупные ара, какаду'),
            (r'• Consider starting smaller and working up', r'• Рассмотрите возможность начать с меньших и продвигаться вверх'),
            (r'• Multi-level puzzle feeders', r'• Многоуровневые кормушки-головоломки'),
            (r'• Advanced problem-solving puzzles', r'• Продвинутые головоломки для решения проблем'),
            (r'• Large foraging opportunities', r'• Большие возможности для поиска пищи'),
            
            # 描述文本
            (r"Perfect for first-time bird owners\. They're social, relatively quiet, and can learn simple words and tricks\.", 
             r"Идеально подходят для начинающих владельцев птиц. Они социальны, относительно тихи и могут выучить простые слова и трюки."),
            (r"Known for their distinctive crest and gentle nature\. They're excellent whistlers and can learn melodies\.", 
             r"Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии."),
            (r"Colorful and energetic birds that do well in pairs\. They're active and require plenty of toys and stimulation\.", 
             r"Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции."),
            (r"Beautiful singers that don't require as much social interaction\. Perfect for those who enjoy bird songs\.", 
             r"Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями."),
            (r"Colorful, playful birds with big personalities\. They can be quite loud and require experienced owners\.", 
             r"Красочные, игривые птицы с большими личностями. Они могут быть довольно громкими и требуют опытных владельцев."),
            (r"Extremely intelligent birds that require experienced owners and consistent mental stimulation\.", 
             r"Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции."),
            
            # 提示内容
            (r"Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe\.", 
             r"Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете."),
        ]
        
        # 应用所有替换
        for pattern, replacement in replacements:
            if callable(replacement):
                content = re.sub(pattern, replacement, content)
            else:
                content = re.sub(pattern, replacement, content)
        
        # 如果有变化，保存文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 强制翻译完成: {file_path}")
            return True
        else:
            print(f"⏭️  无需翻译: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 强制翻译文件 {file_path} 时出错: {e}")
        return False

def translate_value(value):
    """翻译stat-value中的值"""
    translations = {
        'Low-Moderate': 'Низкий-Средний',
        'Moderate': 'Средний',
        'Moderate-High': 'Средний-Высокий',
        'Very High': 'Очень высокий',
        'High': 'Высокий',
        'Low': 'Низкий',
        'Beginner': 'Начинающий',
        'Intermediate': 'Средний',
        'Advanced': 'Продвинутый',
        'Expert': 'Эксперт',
        'Beginner-friendly': 'Для начинающих',
        'Low to moderate': 'От низкого до среднего',
        'Moderate to high': 'От среднего до высокого',
        'Intermediate to advanced': 'От среднего до продвинутого',
    }
    return translations.get(value.strip(), value)

def translate_section_title(title):
    """翻译章节标题"""
    translations = {
        'Intermediate Species': 'Виды среднего уровня',
        'Advanced Species': 'Продвинутые виды',
        'Beginner-Friendly Species': 'Виды для начинающих',
        'Advanced Techniques': 'Продвинутые техники',
        'Understanding Bird Aging': 'Понимание старения птиц',
        'Common Age-Related Health Issues': 'Распространенные возрастные проблемы со здоровьем',
        'Environmental Modifications': 'Модификации окружающей среды',
        'Nutritional Needs for Senior Birds': 'Потребности в питании для пожилых птиц',
        'Veterinary Care for Senior Birds': 'Ветеринарная помощь для пожилых птиц',
        'Mental and Social Needs': 'Психические и социальные потребности',
        'End-of-Life Considerations': 'Соображения конца жизни',
        'Supporting Senior Bird Owners': 'Поддержка владельцев пожилых птиц',
        'Understanding Bird Enrichment Needs': 'Понимание потребностей птиц в обогащении',
        'Foraging Activities': 'Активности поиска пищи',
        'DIY Toy Projects': 'Проекты игрушек своими руками',
    }
    return translations.get(title.strip(), title)

def translate_tip_title(title):
    """翻译提示标题"""
    translations = {
        '💡 Learning Tips for Beginners': '💡 Советы по обучению для начинающих',
        '🏠 Visit Before You Decide': '🏠 Посетите перед принятием решения',
        '🛏️ Comfort First': '🛏️ Комфорт прежде всего',
    }
    return translations.get(title.strip(), title)

def main():
    """主函数"""
    print("开始强制俄语翻译...")
    
    # 获取ru目录下的所有HTML文件
    ru_dir = Path("ru")
    if not ru_dir.exists():
        print("❌ ru目录不存在!")
        return
    
    html_files = list(ru_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 在ru目录下没有找到HTML文件!")
        return
    
    print(f"找到 {len(html_files)} 个HTML文件")
    
    # 处理每个文件
    processed_count = 0
    for file_path in html_files:
        if force_translate_file(file_path):
            processed_count += 1
    
    print(f"\n✅ 强制翻译完成! 共处理了 {len(html_files)} 个文件，修改了 {processed_count} 个文件")

if __name__ == "__main__":
    main()