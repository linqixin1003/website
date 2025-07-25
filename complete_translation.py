#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整翻译ru目录下的HTML文件为俄语
处理所有剩余的英文内容
"""

import os
import re
import glob
from pathlib import Path

# 更完整的英文到俄语翻译映射
TRANSLATIONS = {
    # 基础词汇
    "Getting Started": "Начало работы",
    "Essential Equipment": "Необходимое оборудование",
    "Identification Techniques": "Техники идентификации",
    "Best Locations": "Лучшие места",
    "Behavior Observation": "Наблюдение за поведением",
    "Song Identification": "Идентификация песен",
    "Photography Tips": "Советы по фотографии",
    "Seasonal Guide": "Сезонный гид",
    "Journal Keeping": "Ведение журнала",
    "Ethics and Conservation": "Этика и охрана природы",
    
    # Pet Care
    "Choosing Right Bird": "Выбор подходящей птицы",
    "Nutrition and Feeding": "Питание и кормление",
    "Housing and Environment": "Жилье и окружающая среда",
    "Health and Veterinary": "Здоровье и ветеринария",
    "Training and Behavior": "Дрессировка и поведение",
    "Breeding and Reproduction": "Разведение и размножение",
    "Emergency First Aid": "Экстренная первая помощь",
    "Seasonal Care": "Сезонный уход",
    "Enrichment Activities": "Обогащающие активности",
    "Senior Bird Care": "Уход за пожилыми птицами",
    "Species Profiles": "Профили видов",
    
    # 级别和状态
    "Beginner": "Начинающий",
    "Beginner-friendly": "Для начинающих",
    "Intermediate": "Средний",
    "Advanced": "Продвинутый",
    "Expert": "Эксперт",
    "Low": "Низкий",
    "Low-Moderate": "Низкий-Умеренный",
    "Moderate": "Умеренный",
    "Moderate-High": "Умеренный-Высокий",
    "High": "Высокий",
    "Very High": "Очень высокий",
    
    # 护理标签
    "Care Level": "Уровень ухода",
    "Noise Level": "Уровень шума",
    "Care Requirements": "Требования по уходу",
    "Personality": "Личность",
    
    # 种类分类
    "Beginner-Friendly Species": "Виды для начинающих",
    "Intermediate Species": "Виды среднего уровня",
    "Advanced Species": "Продвинутые виды",
    "Choosing the Right Species": "Выбор подходящего вида",
    
    # 伦理相关
    "Bird Welfare First": "Благополучие птиц прежде всего",
    "Habitat Protection": "Защита среды обитания",
    "Respect Others": "Уважение к другим",
    "Responsible Field Behavior": "Ответственное полевое поведение",
    "Photography Ethics": "Этика фотографии",
    "Conservation Action": "Природоохранные действия",
    "Citizen Science": "Гражданская наука",
    "Support Organizations": "Поддержка организаций",
    "Advocacy": "Адвокация",
    "Sharing Information Responsibly": "Ответственное распространение информации",
    "Climate Change and Birds": "Изменение климата и птицы",
    
    # 健康相关
    "Finding an Avian Veterinarian": "Поиск орнитологического ветеринара",
    "Regular Health Monitoring": "Регулярный мониторинг здоровья",
    "Preventive Care Schedule": "График профилактического ухода",
    "Common Health Issues": "Распространенные проблемы со здоровьем",
    "Emergency Situations": "Экстренные ситуации",
    "Quarantine Procedures": "Процедуры карантина",
    "Understanding Bird Aging": "Понимание старения птиц",
    "Common Age-Related Health Issues": "Распространенные возрастные проблемы со здоровьем",
    "Physical Appearance": "Физический вид",
    "Behavior and Activity": "Поведение и активность",
    
    # 通用界面元素
    "Back Button": "Кнопка назад",
    "Hero Image": "Главное изображение",
    "Main Content": "Основное содержание",
    "Visit Before You Decide": "Посетите перед принятием решения",
    "Special Considerations": "Особые соображения",
    "Emergency Preparedness": "Готовность к чрезвычайным ситуациям",
    "Never Give Birds": "Никогда не давайте птицам",
    "Vet Selection Tip": "Совет по выбору ветеринара",
    "Personal Actions": "Личные действия",
    "Playback Guidelines": "Рекомендации по воспроизведению",
    "Digital vs. Physical Guides": "Цифровые против физических гидов",
    "Field Guides and Reference Materials": "Полевые гиды и справочные материалы",
    "Signs of Bird Distress": "Признаки беспокойства птиц",
    "Learning Tips for Beginners": "Советы по обучению для начинающих",
    "Advanced Techniques": "Продвинутые техники",
    "Advanced Foraging Challenges": "Продвинутые задачи поиска пищи",
    "Experience Level Matching": "Соответствие уровню опыта",
    
    # 鸟类相关描述
    "Social, playful, can learn to talk": "Социальные, игривые, могут научиться говорить",
    "Gentle, affectionate, whistlers": "Нежные, ласковые, свистуны",
    "Energetic, playful, can be territorial": "Энергичные, игривые, могут быть территориальными",
    "Independent, excellent singers": "Независимые, отличные певцы",
    "Playful, loud, affectionate": "Игривые, громкие, ласковые",
    "Highly intelligent, can be sensitive": "Очень умные, могут быть чувствительными",
    "Perfect for first-time bird owners. They're social, relatively quiet, and can learn simple words and tricks.": "Идеально подходят для начинающих владельцев птиц. Они социальные, относительно тихие и могут выучить простые слова и трюки.",
    "Known for their distinctive crest and gentle nature. They're excellent whistlers and can learn melodies.": "Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии.",
    "Colorful and energetic birds that do well in pairs. They're active and require plenty of toys and stimulation.": "Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции.",
    "Beautiful singers that don't require as much social interaction. Perfect for those who enjoy bird songs.": "Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями.",
    "Colorful, playful birds with big personalities. They can be quite loud and require experienced owners.": "Красочные, игривые птицы с яркими личностями. Они могут быть довольно громкими и требуют опытных владельцев.",
    "Extremely intelligent birds that require experienced owners and consistent mental stimulation.": "Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции.",
    
    # 经验级别匹配
    "Beginners: Budgies, canaries, cockatiels": "Начинающие: Волнистые попугайчики, канарейки, кореллы",
    "Intermediate: Lovebirds, small conures, parrotlets": "Средний уровень: Неразлучники, маленькие конуры, воробьиные попугайчики",
    "Advanced: Large conures, small macaws, amazons": "Продвинутый: Большие конуры, маленькие ара, амазоны",
    "Expert: African greys, large macaws, cockatoos": "Эксперт: Африканские серые, большие ара, какаду",
    
    # 其他常见短语
    "Multi-level puzzle feeders": "Многоуровневые кормушки-головоломки",
    "Large Birds (Macaws, African Greys)": "Крупные птицы (Ара, Африканские серые)",
    "Advanced problem-solving puzzles": "Продвинутые головоломки для решения проблем",
    "Large foraging opportunities": "Большие возможности для поиска пищи",
    "Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.": "Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.",
    
    # 长句翻译
    "Always prioritize the well-being of birds over getting a sighting, photo, or recording.": "Всегда ставьте благополучие птиц выше получения наблюдения, фото или записи.",
    "Respect and protect bird habitats. Stay on designated trails and avoid damaging vegetation.": "Уважайте и защищайте среды обитания птиц. Оставайтесь на обозначенных тропах и избегайте повреждения растительности.",
    "Be considerate of other birders, property owners, and local communities.": "Будьте внимательны к другим орнитологам, владельцам собственности и местным сообществам.",
}

def translate_text(text):
    """翻译文本，保持HTML标签不变"""
    if not text or not isinstance(text, str):
        return text
    
    # 按长度排序，先处理长句
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for en_text, ru_text in sorted_translations:
        if en_text in text:
            text = text.replace(en_text, ru_text)
    
    return text

def process_html_file(file_path):
    """处理单个HTML文件"""
    print(f"处理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 确保语言属性是俄语
        content = re.sub(r'<html lang="[^"]*"', '<html lang="ru"', content)
        
        # 翻译内容
        original_content = content
        content = translate_text(content)
        
        # 只有内容发生变化时才写入文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"⏭️  无需更新: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始完整翻译ru目录下的HTML文件...")
    
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
    updated_count = 0
    for file_path in html_files:
        if process_html_file(file_path):
            updated_count += 1
    
    print(f"\n✅ 完整翻译完成! 共处理了 {len(html_files)} 个文件，更新了 {updated_count} 个文件")
    
    # 检查翻译结果
    print("\n检查剩余英文内容...")
    remaining_english = []
    
    # 检查常见的英文模式
    english_patterns = [
        r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # 大写开头的英文短语
        r'\bBird [A-Z][a-z]+\b',         # Bird开头的短语
        r'\b[A-Z][a-z]+ Guide\b',        # Guide结尾的短语
        r'\bCare [A-Z][a-z]+\b',         # Care开头的短语
        r'\bNoise Level\b',              # Noise Level
        r'\bCare Level\b',               # Care Level
        r'\bBeginner\b',                 # Beginner
        r'\bIntermediate\b',             # Intermediate
        r'\bAdvanced\b',                 # Advanced
        r'\bExpert\b',                   # Expert
    ]
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for pattern in english_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    for match in matches:
                        if match not in TRANSLATIONS.values():  # 避免重复计算已翻译的内容
                            remaining_english.append((str(file_path), match))
        
        except Exception as e:
            print(f"检查文件 {file_path} 时出错: {e}")
    
    if remaining_english:
        print(f"\n⚠️  发现 {len(remaining_english)} 处可能需要进一步翻译的英文内容:")
        unique_remaining = list(set([item[1] for item in remaining_english]))
        for i, text in enumerate(unique_remaining[:20]):  # 只显示前20个唯一项
            print(f"  {i+1}. {text}")
        if len(unique_remaining) > 20:
            print(f"  ... 还有 {len(unique_remaining) - 20} 处")
    else:
        print("\n✅ 所有主要英文内容都已翻译完成!")

if __name__ == "__main__":
    main()