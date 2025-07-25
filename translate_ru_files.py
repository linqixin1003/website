#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译ru目录下的HTML文件为俄语
保持格式和排版不变，只翻译文本内容
"""

import os
import re
import glob
from pathlib import Path

# 英文到俄语的翻译映射
TRANSLATIONS = {
    # 通用词汇
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
    
    # Pet Care 相关
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
    
    # 常见短语
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
    
    # 状态和级别
    "Beginner": "Начинающий",
    "Intermediate": "Средний",
    "Advanced": "Продвинутый",
    "Expert": "Эксперт",
    "Low": "Низкий",
    "Moderate": "Умеренный",
    "High": "Высокий",
    "Very High": "Очень высокий",
    
    # 护理相关
    "Care Level": "Уровень ухода",
    "Noise Level": "Уровень шума",
    "Care Requirements": "Требования по уходу",
    "Beginner-Friendly Species": "Виды для начинающих",
    "Intermediate Species": "Виды среднего уровня",
    "Advanced Species": "Продвинутые виды",
    "Choosing the Right Species": "Выбор подходящего вида",
    
    # 健康相关
    "Finding an Avian Veterinarian": "Поиск орнитологического ветеринара",
    "Regular Health Monitoring": "Регулярный мониторинг здоровья",
    "Preventive Care Schedule": "График профилактического ухода",
    "Common Health Issues": "Распространенные проблемы со здоровьем",
    "Emergency Situations": "Экстренные ситуации",
    "Quarantine Procedures": "Процедуры карантина",
    "Senior Bird Care": "Уход за пожилыми птицами",
    
    # 行为和训练
    "Understanding Bird Aging": "Понимание старения птиц",
    "Common Age-Related Health Issues": "Распространенные возрастные проблемы со здоровьем",
    "Physical Appearance": "Физический вид",
    "Behavior and Activity": "Поведение и активность",
    
    # 通用短语
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
    
    # 长句翻译
    "Always prioritize the well-being of birds over getting a sighting, photo, or recording.": "Всегда ставьте благополучие птиц выше получения наблюдения, фото или записи.",
    "Respect and protect bird habitats. Stay on designated trails and avoid damaging vegetation.": "Уважайте и защищайте среды обитания птиц. Оставайтесь на обозначенных тропах и избегайте повреждения растительности.",
    "Be considerate of other birders, property owners, and local communities.": "Будьте внимательны к другим орнитологам, владельцам собственности и местным сообществам.",
    "Maintain appropriate distances from birds, especially during sensitive periods like nesting, feeding, or roosting": "Поддерживайте соответствующие расстояния от птиц, особенно в чувствительные периоды, такие как гнездование, кормление или ночевка",
    "Use binoculars and telephoto lenses to observe birds without getting too close. If a bird shows signs of stress or alarm, back away immediately.": "Используйте бинокли и телеобъективы для наблюдения за птицами, не приближаясь слишком близко. Если птица проявляет признаки стресса или тревоги, немедленно отступите.",
    "Use recorded bird calls sparingly and responsibly": "Используйте записанные птичьи крики экономно и ответственно",
    "Excessive playback can stress birds, disrupt their natural behavior, and interfere with breeding activities. Never use playback near active nests or during sensitive breeding periods.": "Чрезмерное воспроизведение может вызвать стресс у птиц, нарушить их естественное поведение и помешать размножению. Никогда не используйте воспроизведение рядом с активными гнездами или в чувствительные периоды размножения.",
    "Bird photography requires extra ethical consideration due to the desire for close, detailed images": "Фотография птиц требует дополнительного этического рассмотрения из-за желания получить близкие, детальные изображения",
    "Never manipulate the environment by moving nests, removing vegetation, or using bait near nesting sites. The bird's welfare is more important than any photograph.": "Никогда не манипулируйте окружающей средой, перемещая гнезда, удаляя растительность или используя приманку рядом с местами гнездования. Благополучие птицы важнее любой фотографии.",
    "Avoid flash photography, especially with nocturnal species or during sensitive periods": "Избегайте фотографии со вспышкой, особенно с ночными видами или в чувствительные периоды",
    "Be patient and work with natural behavior rather than trying to force interactions or poses. Share location information responsibly, especially for rare or sensitive species.": "Будьте терпеливы и работайте с естественным поведением, а не пытайтесь принуждать к взаимодействию или позам. Делитесь информацией о местоположении ответственно, особенно для редких или чувствительных видов.",
    "Ethical birding extends beyond field behavior to active conservation support": "Этичное наблюдение за птицами выходит за рамки полевого поведения и включает активную поддержку охраны природы",
    "Participate in citizen science projects, support conservation organizations, and advocate for bird-friendly policies and habitat protection.": "Участвуйте в проектах гражданской науки, поддерживайте природоохранные организации и выступайте за политику, дружественную к птицам, и защиту среды обитания.",
    "Contribute to eBird, Christmas Bird Count, and other research projects that inform conservation decisions.": "Вносите вклад в eBird, Рождественский подсчет птиц и другие исследовательские проекты, которые информируют решения по охране природы.",
    "Join and support Audubon, local bird clubs, and conservation groups working to protect birds.": "Присоединяйтесь и поддерживайте Audubon, местные птичьи клубы и природоохранные группы, работающие над защитой птиц.",
    "Support bird-friendly legislation, habitat protection, and policies that address climate change.": "Поддерживайте законодательство, дружественное к птицам, защиту среды обитания и политику, направленную на борьбу с изменением климата.",
    "Be thoughtful about sharing locations of rare or sensitive species": "Будьте внимательны при распространении информации о местонахождении редких или чувствительных видов",
    "While sharing birding discoveries builds community, it can also lead to overcrowding and disturbance. Consider the potential impact before posting specific locations on social media.": "Хотя обмен орнитологическими открытиями укрепляет сообщество, это также может привести к переполненности и беспокойству. Рассмотрите потенциальное воздействие перед публикацией конкретных местоположений в социальных сетях.",
    "Climate change is one of the greatest threats facing birds today": "Изменение климата является одной из величайших угроз, с которыми сталкиваются птицы сегодня",
    "As birders, we can contribute to solutions by reducing our carbon footprint, supporting renewable energy, and documenting climate-related changes in bird populations and distributions.": "Как орнитологи, мы можем внести вклад в решения, уменьшив наш углеродный след, поддерживая возобновляемую энергию и документируя связанные с климатом изменения в популяциях и распределении птиц.",
    "Reduce energy consumption, choose sustainable transportation, support bird-friendly agriculture, create bird-friendly spaces at home, and educate others about conservation.": "Сократите потребление энергии, выбирайте устойчивый транспорт, поддерживайте дружественное к птицам сельское хозяйство, создавайте дружественные к птицам пространства дома и обучайте других охране природы.",
    "Ethical birding is about more than following rules - it's about developing a conservation mindset that puts birds first": "Этичное наблюдение за птицами - это больше, чем следование правилам - это развитие природоохранного мышления, которое ставит птиц на первое место",
    "By practicing responsible birding and supporting conservation efforts, we ensure that future generations will have the same opportunities to experience the wonder of birds that we enjoy today.": "Практикуя ответственное наблюдение за птицами и поддерживая усилия по охране природы, мы обеспечиваем будущим поколениям те же возможности испытать чудо птиц, которыми мы наслаждаемся сегодня.",
    "Limit sessions to 30 seconds, wait several minutes between attempts, stop if birds show distress, and avoid playback during breeding season in sensitive areas.": "Ограничьте сеансы до 30 секунд, подождите несколько минут между попытками, остановитесь, если птицы проявляют беспокойство, и избегайте воспроизведения во время сезона размножения в чувствительных областях.",
    "While traditional printed field guides remain popular, smartphone apps like eBird, Merlin Bird ID, and BirdAiSnap offer interactive features, bird songs, and real-time sighting data.": "Хотя традиционные печатные полевые гиды остаются популярными, приложения для смартфонов, такие как eBird, Merlin Bird ID и BirdAiSnap, предлагают интерактивные функции, птичьи песни и данные наблюдений в реальном времени.",
    "Field Guides and Reference Materials": "Полевые гиды и справочные материалы",
    "Alarm calls, aggressive posturing, abandoning nest or young, repeated flushing, or changes in normal behavior patterns indicate you may be too close.": "Тревожные крики, агрессивные позы, покидание гнезда или птенцов, повторное вспугивание или изменения в нормальных поведенческих паттернах указывают на то, что вы можете быть слишком близко.",
    "Signs of Bird Distress": "Признаки беспокойства птиц"
}

def translate_text(text):
    """翻译文本，保持HTML标签不变"""
    if not text or not isinstance(text, str):
        return text
    
    # 先处理完整的长句
    for en_text, ru_text in TRANSLATIONS.items():
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
        else:
            print(f"⏭️  无需更新: {file_path}")
            
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")

def main():
    """主函数"""
    print("开始批量翻译ru目录下的HTML文件...")
    
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
    for file_path in html_files:
        process_html_file(file_path)
    
    print(f"\n✅ 批量翻译完成! 共处理了 {len(html_files)} 个文件")
    
    # 检查翻译结果
    print("\n检查翻译结果...")
    remaining_english = []
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否还有英文内容
            english_patterns = [
                r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # 大写开头的英文短语
                r'\bBird [A-Z][a-z]+\b',         # Bird开头的短语
                r'\b[A-Z][a-z]+ Guide\b',        # Guide结尾的短语
                r'\bCare [A-Z][a-z]+\b',         # Care开头的短语
            ]
            
            for pattern in english_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    remaining_english.extend([(str(file_path), match) for match in matches])
        
        except Exception as e:
            print(f"检查文件 {file_path} 时出错: {e}")
    
    if remaining_english:
        print(f"\n⚠️  发现 {len(remaining_english)} 处可能需要进一步翻译的英文内容:")
        for file_path, text in remaining_english[:20]:  # 只显示前20个
            print(f"  {file_path}: {text}")
        if len(remaining_english) > 20:
            print(f"  ... 还有 {len(remaining_english) - 20} 处")
    else:
        print("\n✅ 所有文件的主要英文内容都已翻译完成!")

if __name__ == "__main__":
    main()