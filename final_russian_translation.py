#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终俄语翻译脚本 - 处理所有剩余的英文内容
"""

import os
import re
from pathlib import Path

# 最终翻译映射
FINAL_TRANSLATIONS = {
    # HTML标签内的英文内容
    '<div class="stat-label">Noise Level</div>': '<div class="stat-label">Уровень шума</div>',
    '<div class="stat-label">Care Level</div>': '<div class="stat-label">Уровень ухода</div>',
    '<div class="stat-value">Low-Moderate</div>': '<div class="stat-value">Низкий-Средний</div>',
    '<div class="stat-value">Moderate</div>': '<div class="stat-value">Средний</div>',
    '<div class="stat-value">Moderate-High</div>': '<div class="stat-value">Средний-Высокий</div>',
    '<div class="stat-value">Very High</div>': '<div class="stat-value">Очень высокий</div>',
    '<div class="stat-value">High</div>': '<div class="stat-value">Высокий</div>',
    '<div class="stat-value">Low</div>': '<div class="stat-value">Низкий</div>',
    '<div class="stat-value">Beginner</div>': '<div class="stat-value">Начинающий</div>',
    '<div class="stat-value">Intermediate</div>': '<div class="stat-value">Средний</div>',
    '<div class="stat-value">Advanced</div>': '<div class="stat-value">Продвинутый</div>',
    '<div class="stat-value">Expert</div>': '<div class="stat-value">Эксперт</div>',
    
    # 章节标题
    '<div class="section-title">Intermediate Species</div>': '<div class="section-title">Виды среднего уровня</div>',
    '<div class="section-title">Advanced Species</div>': '<div class="section-title">Продвинутые виды</div>',
    '<div class="section-title">Beginner-Friendly Species</div>': '<div class="section-title">Виды для начинающих</div>',
    '<div class="section-title">Advanced Techniques</div>': '<div class="section-title">Продвинутые техники</div>',
    
    # 提示标题
    '<div class="tip-title">💡 Learning Tips for Beginners</div>': '<div class="tip-title">💡 Советы по обучению для начинающих</div>',
    
    # 经验等级匹配
    '<strong>Experience Level Matching:</strong>': '<strong>Соответствие уровню опыта:</strong>',
    '• Beginners: Budgies, canaries, cockatiels': '• Начинающие: волнистые попугайчики, канарейки, кореллы',
    '• Intermediate: Lovebirds, small conures, parrotlets': '• Средний уровень: неразлучники, маленькие конуры, попугайчики',
    '• Advanced: Large conures, small macaws, amazons': '• Продвинутый: крупные конуры, маленькие ара, амазоны',
    '• Expert: African greys, large macaws, cockatoos': '• Эксперт: африканские серые, крупные ара, какаду',
    '• Consider starting smaller and working up': '• Рассмотрите возможность начать с меньших и продвигаться вверх',
    
    # 高级觅食挑战
    '<strong>Advanced Foraging Challenges:</strong>': '<strong>Продвинутые вызовы поиска пищи:</strong>',
    '• Multi-level puzzle feeders': '• Многоуровневые кормушки-головоломки',
    '<strong>Large Birds (Macaws, African Greys):</strong>': '<strong>Крупные птицы (ара, африканские серые):</strong>',
    '• Advanced problem-solving puzzles': '• Продвинутые головоломки для решения проблем',
    '• Large foraging opportunities': '• Большие возможности для поиска пищи',
    
    # 护理等级和噪音等级
    '<strong>Care Level:</strong> Beginner-friendly': '<strong>Уровень ухода:</strong> Для начинающих',
    '<strong>Care Level:</strong> Beginner to intermediate': '<strong>Уровень ухода:</strong> От начинающего до среднего',
    '<strong>Care Level:</strong> Intermediate': '<strong>Уровень ухода:</strong> Средний',
    '<strong>Care Level:</strong> Intermediate to advanced': '<strong>Уровень ухода:</strong> От среднего до продвинутого',
    '<strong>Care Level:</strong> Advanced': '<strong>Уровень ухода:</strong> Продвинутый',
    
    '<strong>Noise Level:</strong> Moderate': '<strong>Уровень шума:</strong> Средний',
    '<strong>Noise Level:</strong> Low to moderate': '<strong>Уровень шума:</strong> От низкого до среднего',
    '<strong>Noise Level:</strong> Moderate to high': '<strong>Уровень шума:</strong> От среднего до высокого',
    '<strong>Noise Level:</strong> High': '<strong>Уровень шума:</strong> Высокий',
    
    # 个性描述
    '<strong>Personality:</strong> Social, playful, can learn to talk': '<strong>Личность:</strong> Социальные, игривые, могут научиться говорить',
    '<strong>Personality:</strong> Gentle, affectionate, whistlers': '<strong>Личность:</strong> Нежные, ласковые, свистуны',
    '<strong>Personality:</strong> Energetic, playful, can be territorial': '<strong>Личность:</strong> Энергичные, игривые, могут быть территориальными',
    '<strong>Personality:</strong> Independent, excellent singers': '<strong>Личность:</strong> Независимые, отличные певцы',
    '<strong>Personality:</strong> Playful, loud, affectionate': '<strong>Личность:</strong> Игривые, громкие, ласковые',
    '<strong>Personality:</strong> Highly intelligent, can be sensitive': '<strong>Личность:</strong> Очень умные, могут быть чувствительными',
    
    # 描述文本
    "Perfect for first-time bird owners. They're social, relatively quiet, and can learn simple words and tricks.": "Идеально подходят для начинающих владельцев птиц. Они социальны, относительно тихи и могут выучить простые слова и трюки.",
    "Known for their distinctive crest and gentle nature. They're excellent whistlers and can learn melodies.": "Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии.",
    "Colorful and energetic birds that do well in pairs. They're active and require plenty of toys and stimulation.": "Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции.",
    "Beautiful singers that don't require as much social interaction. Perfect for those who enjoy bird songs.": "Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями.",
    "Colorful, playful birds with big personalities. They can be quite loud and require experienced owners.": "Красочные, игривые птицы с большими личностями. Они могут быть довольно громкими и требуют опытных владельцев.",
    "Extremely intelligent birds that require experienced owners and consistent mental stimulation.": "Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции.",
    
    # 提示内容
    "Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.": "Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.",
}

def process_file(file_path):
    """处理单个文件"""
    print(f"处理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # 应用所有翻译
        for en_text, ru_text in FINAL_TRANSLATIONS.items():
            if en_text in content:
                content = content.replace(en_text, ru_text)
                changes_made += 1
                print(f"  ✓ 翻译: {en_text[:50]}...")
        
        # 如果有变化，保存文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 完成翻译: {file_path} ({changes_made} 处修改)")
            return True
        else:
            print(f"⏭️  无需翻译: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始最终俄语翻译...")
    
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
        if process_file(file_path):
            processed_count += 1
    
    print(f"\n✅ 最终翻译完成! 共处理了 {len(html_files)} 个文件，修改了 {processed_count} 个文件")

if __name__ == "__main__":
    main()