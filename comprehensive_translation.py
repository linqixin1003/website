#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面翻译ru目录下HTML文件中的所有英文内容
"""

import os
import re
from pathlib import Path

# 全面的英文到俄语翻译字典
COMPREHENSIVE_TRANSLATIONS = {
    # 基本标签和标题
    "Care Level": "Уровень ухода",
    "Noise Level": "Уровень шума", 
    "Beginner": "Начинающий",
    "Intermediate": "Средний",
    "Advanced": "Продвинутый",
    "Expert": "Эксперт",
    "Low-Moderate": "Низкий-Средний",
    "Moderate": "Средний",
    "Moderate-High": "Средний-Высокий",
    "Very High": "Очень высокий",
    
    # 种类相关
    "Intermediate Species": "Виды среднего уровня",
    "Advanced Species": "Продвинутые виды",
    "Beginner-Friendly Species": "Виды для начинающих",
    "Sun Conure": "Солнечный конур",
    "African Grey Parrot": "Африканский серый попугай",
    "Blue and Gold Macaw": "Сине-желтый ара",
    
    # 护理要求
    "Care Requirements:": "Требования по уходу:",
    "Care Requirements": "Требования по уходу",
    
    # 选择相关
    "Choosing the Right Species": "Выбор подходящего вида",
    "Experience Level Matching:": "Соответствие уровню опыта:",
    "Lifestyle Compatibility:": "Совместимость с образом жизни:",
    "Special Considerations:": "Особые соображения:",
    
    # 经验等级匹配
    "Beginners: Budgies, canaries, cockatiels": "Начинающие: волнистые попугайчики, канарейки, кореллы",
    "Intermediate: Lovebirds, small conures, parrotlets": "Средний уровень: неразлучники, маленькие конуры, попугайчики",
    "Advanced: Large conures, small macaws, amazons": "Продвинутый: крупные конуры, маленькие ара, амазоны",
    "Expert: African greys, large macaws, cockatoos": "Эксперт: африканские серые, крупные ара, какаду",
    
    # 生活方式兼容性
    "Noise tolerance and living situation": "Толерантность к шуму и жилищная ситуация",
    "Available time for interaction and training": "Доступное время для взаимодействия и обучения",
    "Experience with bird behavior and training": "Опыт работы с поведением и дрессировкой птиц",
    "Long-term commitment capability": "Способность к долгосрочным обязательствам",
    
    # 特殊考虑
    "Some species do better in pairs": "Некоторые виды лучше живут парами",
    "Consider starting smaller and working up": "Рассмотрите возможность начать с меньших и продвигаться вверх",
    "Research specific dietary and housing needs": "Изучите специфические потребности в питании и жилье",
    "Factor in veterinary costs and availability": "Учтите ветеринарные расходы и доступность",
    
    # 老年鸟护理
    "Understanding Bird Aging": "Понимание старения птиц",
    "When Birds Are Considered Senior:": "Когда птицы считаются пожилыми:",
    "Small birds (budgies, canaries): 5-7 years": "Маленькие птицы (волнистые попугайчики, канарейки): 5-7 лет",
    "Medium birds (cockatiels, conures): 10-15 years": "Средние птицы (кореллы, конуры): 10-15 лет",
    "Large birds (macaws, cockatoos): 20-30 years": "Крупные птицы (ара, какаду): 20-30 лет",
    
    # 身体衰老迹象
    "Physical Signs of Aging:": "Физические признаки старения:",
    "Decreased activity and energy levels": "Снижение активности и уровня энергии",
    "Changes in feather quality and molting patterns": "Изменения в качестве перьев и схемах линьки",
    "Slower movement and reaction times": "Замедление движений и времени реакции",
    "Weight fluctuations": "Колебания веса",
    
    # 行为变化
    "Behavioral Changes in Senior Birds:": "Поведенческие изменения у пожилых птиц:",
    "Increased sleeping and resting": "Увеличение сна и отдыха",
    "Reduced vocalization": "Снижение вокализации",
    "Changes in social interaction preferences": "Изменения в предпочтениях социального взаимодействия",
    "Possible increased irritability or sensitivity": "Возможное увеличение раздражительности или чувствительности",
    
    # 常见年龄相关健康问题
    "Common Age-Related Health Issues": "Распространенные возрастные проблемы со здоровьем",
    "Arthritis and Joint Issues": "Артрит и проблемы с суставами",
    "Heart Disease": "Болезни сердца",
    "Respiratory Issues": "Проблемы с дыханием",
    "Digestive Problems": "Проблемы с пищеварением",
    "Vision Problems": "Проблемы со зрением",
    "Cognitive Changes": "Когнитивные изменения",
    
    # 症状描述
    "Symptoms:": "Симптомы:",
    "Difficulty perching, reluctance to move": "Трудности с сидением на жердочке, нежелание двигаться",
    "Exercise intolerance, breathing difficulty": "Непереносимость физических нагрузок, затрудненное дыхание",
    "Labored breathing, tail bobbing": "Затрудненное дыхание, покачивание хвостом",
    "Poor appetite, weight loss": "Плохой аппетит, потеря веса",
    "Bumping into objects, hesitation": "Столкновение с предметами, колебания",
    "Confusion, repetitive behaviors": "Замешательство, повторяющееся поведение",
    
    # 环境修改
    "Environmental Modifications": "Модификации окружающей среды",
    "Cage Modifications:": "Модификации клетки:",
    "Lower perch placement for easier access": "Более низкое размещение жердочек для облегчения доступа",
    "Softer perch materials to reduce joint stress": "Более мягкие материалы жердочек для снижения нагрузки на суставы",
    "Multiple food and water stations": "Множественные станции для еды и воды",
    "Easy-access cage doors": "Легкодоступные дверцы клетки",
    
    # 舒适增强
    "Comfort Enhancements:": "Улучшения комфорта:",
    "Warmer environment (75-80°F)": "Более теплая среда (24-27°C)",
    "Draft-free location": "Место без сквозняков",
    "Consistent lighting schedule": "Постоянный график освещения",
    "Quiet, stress-free environment": "Тихая, свободная от стресса среда",
    
    # 安全考虑
    "Safety Considerations:": "Соображения безопасности:",
    "Remove high perches that could cause falls": "Удалите высокие жердочки, которые могут привести к падениям",
    "Ensure easy access to food and water": "Обеспечьте легкий доступ к еде и воде",
    "Monitor for signs of discomfort or pain": "Следите за признаками дискомфорта или боли",
    "Regular health check-ups": "Регулярные медицинские осмотры",
    
    # 营养需求
    "Nutritional Needs for Senior Birds": "Потребности в питании для пожилых птиц",
    "Senior Diet Considerations:": "Соображения по диете для пожилых:",
    "Easily digestible foods": "Легко усваиваемые продукты",
    "Higher quality protein sources": "Источники белка более высокого качества",
    "Reduced portion sizes, more frequent meals": "Уменьшенные порции, более частые приемы пищи",
    "Softer food textures when needed": "Более мягкие текстуры пищи при необходимости",
    
    # 有益食物
    "Beneficial Foods for Seniors:": "Полезные продукты для пожилых:",
    "Cooked quinoa and brown rice": "Вареная киноа и коричневый рис",
    "Steamed vegetables": "Приготовленные на пару овощи",
    "Soft fruits like banana and cooked sweet potato": "Мягкие фрукты, такие как банан и вареный сладкий картофель",
    "High-quality pellets designed for senior birds": "Высококачественные гранулы, предназначенные для пожилых птиц",
    
    # 补充剂
    "Supplements for Senior Birds:": "Добавки для пожилых птиц:",
    "Omega-3 fatty acids for joint health": "Омега-3 жирные кислоты для здоровья суставов",
    "Probiotics for digestive support": "Пробиотики для поддержки пищеварения",
    "Vitamin D3 for bone health": "Витамин D3 для здоровья костей",
    "Antioxidants for cognitive support": "Антиоксиданты для когнитивной поддержки",
    
    # 兽医护理
    "Veterinary Care for Senior Birds": "Ветеринарная помощь для пожилых птиц",
    "Recommended Veterinary Schedule:": "Рекомендуемый график ветеринарных осмотров:",
    "Semi-annual wellness exams (every 6 months)": "Полугодовые осмотры здоровья (каждые 6 месяцев)",
    "More frequent monitoring of chronic conditions": "Более частый мониторинг хронических состояний",
    "Immediate attention for any behavioral changes": "Немедленное внимание к любым поведенческим изменениям",
    
    # 健康筛查
    "Senior Bird Health Screening:": "Скрининг здоровья пожилых птиц:",
    "Complete blood chemistry panel": "Полная панель биохимии крови",
    "X-rays to check for arthritis or organ changes": "Рентген для проверки артрита или изменений органов",
    "Fecal examination for parasites": "Исследование кала на паразитов",
    "Weight and body condition assessment": "Оценка веса и состояния тела",
    
    # 慢性病管理
    "Managing Chronic Conditions:": "Управление хроническими состояниями:",
    "Daily medication administration": "Ежедневное введение лекарств",
    "Environmental modifications for comfort": "Модификации окружающей среды для комфорта",
    "Regular monitoring and adjustment of treatment": "Регулярный мониторинг и корректировка лечения",
    "Pain management strategies": "Стратегии управления болью",
    
    # 心理和社交需求
    "Mental and Social Needs": "Психические и социальные потребности",
    "Age-Appropriate Enrichment:": "Соответствующее возрасту обогащение:",
    "Gentle, low-impact activities": "Мягкие, низкоинтенсивные активности",
    "Familiar toys and routines": "Знакомые игрушки и рутины",
    "Shorter play sessions": "Более короткие игровые сессии",
    "Comfortable resting areas": "Удобные места для отдыха",
    
    # 社交互动调整
    "Social Interaction Adjustments:": "Корректировки социального взаимодействия:",
    "Shorter, more frequent interaction sessions": "Более короткие, более частые сессии взаимодействия",
    "Respect for increased need for rest": "Уважение к возросшей потребности в отдыхе",
    "Gentle handling and reduced stress": "Бережное обращение и снижение стресса",
    "Maintaining familiar social bonds": "Поддержание знакомых социальных связей",
    
    # 认知支持
    "Cognitive Support:": "Когнитивная поддержка:",
    "Simple training exercises": "Простые тренировочные упражнения",
    "Consistent daily routines": "Постоянные ежедневные рутины",
    "Mental stimulation through gentle activities": "Умственная стимуляция через мягкие активности",
    "Familiar environment and minimal changes": "Знакомая среда и минимальные изменения",
    
    # 生命终期考虑
    "End-of-Life Considerations": "Соображения конца жизни",
    "Quality of Life Indicators:": "Показатели качества жизни:",
    "Appetite and interest in food": "Аппетит и интерес к еде",
    "Social interaction and responsiveness": "Социальное взаимодействие и отзывчивость",
    "Mobility and comfort level": "Подвижность и уровень комфорта",
    "Overall alertness and engagement": "Общая бдительность и вовлеченность",
    
    # 姑息治疗选择
    "Palliative Care Options:": "Варианты паллиативной помощи:",
    "Pain management medications": "Лекарства для управления болью",
    "Comfort-focused environmental modifications": "Модификации окружающей среды, ориентированные на комфорт",
    "Supportive nutritional therapy": "Поддерживающая пищевая терапия",
    "Gentle, compassionate care": "Мягкий, сострадательный уход",
    
    # 困难决定
    "Making Difficult Decisions:": "Принятие трудных решений:",
    "Consult with experienced avian veterinarian": "Консультация с опытным орнитологическим ветеринаром",
    "Consider bird's quality of life objectively": "Объективно оцените качество жизни птицы",
    "Discuss options with family members": "Обсудите варианты с членами семьи",
    "Seek support from bird community": "Обратитесь за поддержкой к сообществу птицеводов",
    
    # 支持老年鸟主人
    "Supporting Senior Bird Owners": "Поддержка владельцев пожилых птиц",
    "Building Support Networks:": "Создание сетей поддержки:",
    "Join senior bird care groups": "Присоединяйтесь к группам по уходу за пожилыми птицами",
    "Connect with experienced bird owners": "Связывайтесь с опытными владельцами птиц",
    "Maintain relationships with avian veterinarians": "Поддерживайте отношения с орнитологическими ветеринарами",
    "Seek emotional support when needed": "Обращайтесь за эмоциональной поддержкой при необходимости",
    
    # 丰富活动相关
    "Understanding Bird Enrichment Needs": "Понимание потребностей птиц в обогащении",
    "Foraging Enrichment": "Обогащение поиском пищи",
    "Cognitive Enrichment": "Когнитивное обогащение",
    "Physical Enrichment": "Физическое обогащение",
    "Social Enrichment": "Социальное обогащение",
    "Sensory Enrichment": "Сенсорное обогащение",
    "Environmental Enrichment": "Экологическое обогащение",
    
    # 目的描述
    "Purpose:": "Цель:",
    "Mimics natural food-seeking behavior": "Имитирует естественное поведение поиска пищи",
    "Challenges problem-solving abilities": "Вызывает способности решения проблем",
    "Promotes exercise and movement": "Способствует упражнениям и движению",
    "Fulfills social interaction needs": "Удовлетворяет потребности в социальном взаимодействии",
    "Stimulates different senses": "Стимулирует различные чувства",
    "Creates interesting living spaces": "Создает интересные жилые пространства",
    
    # 觅食活动
    "Foraging Activities": "Активности поиска пищи",
    "Simple Foraging Ideas:": "Простые идеи поиска пищи:",
    "Hide treats in paper cups or small boxes": "Прячьте лакомства в бумажные стаканчики или маленькие коробки",
    "Wrap food in paper or leaves": "Заворачивайте еду в бумагу или листья",
    "Use puzzle feeders and treat balls": "Используйте кормушки-головоломки и шарики с лакомствами",
    "Create foraging trees with multiple hiding spots": "Создавайте деревья для поиска пищи с множественными укрытиями",
    
    # DIY项目
    "DIY Foraging Box": "Коробка для поиска пищи своими руками",
    "Materials:": "Материалы:",
    "Small cardboard box, paper shreds, bird-safe treats": "Маленькая картонная коробка, измельченная бумага, безопасные для птиц лакомства",
    "Instructions:": "Инструкции:",
    "Fill box with paper shreds and hide treats throughout": "Заполните коробку измельченной бумагой и спрячьте лакомства по всей коробке",
    
    # 高级觅食挑战
    "Advanced Foraging Challenges:": "Продвинутые вызовы поиска пищи:",
    "Multi-level puzzle feeders": "Многоуровневые кормушки-головоломки",
    "Rotating treat dispensers": "Вращающиеся дозаторы лакомств",
    "Hidden compartment toys": "Игрушки со скрытыми отделениями",
    "Foraging wheels and spinning devices": "Колеса для поиска пищи и вращающиеся устройства",
    
    # DIY玩具项目
    "DIY Toy Projects": "Проекты игрушек своими руками",
    "Paper Roll Shredder": "Измельчитель бумажных рулонов",
    "Toilet paper rolls, bird-safe paper, treats": "Рулоны туалетной бумаги, безопасная для птиц бумага, лакомства",
    "Stuff rolls with paper and treats, hang in cage": "Набейте рулоны бумагой и лакомствами, повесьте в клетке",
    
    # 按钮和导航
    "Back Button": "Кнопка назад",
    "Hero Image": "Главное изображение",
    "Main Content": "Основное содержание",
    
    # 提示框
    "Visit Before You Decide": "Посетите перед принятием решения",
    "Spend time with different species at bird rescues, pet stores, or bird shows before making your decision. Each species has a unique personality and energy level.": "Проведите время с разными видами в приютах для птиц, зоомагазинах или выставках птиц перед принятием решения. Каждый вид имеет уникальную личность и уровень энергии.",
    
    "Comfort First": "Комфорт прежде всего",
    "Senior birds prioritize comfort over activity. Focus on making their environment as comfortable and accessible as possible.": "Пожилые птицы отдают приоритет комфорту над активностью. Сосредоточьтесь на том, чтобы сделать их среду максимально комфортной и доступной.",
    
    "Weight Management": "Управление весом",
    "Monitor weight regularly": "Регулярно контролируйте вес",
    "Adjust portions based on activity level": "Корректируйте порции в зависимости от уровня активности",
    "Consult vet for significant weight changes": "Консультируйтесь с ветеринаром при значительных изменениях веса",
    
    # 物种描述
    "Sun Conures are stunning birds with brilliant yellow and orange plumage. They're extremely social, intelligent, and affectionate, but also very loud and demanding. These birds require experienced owners who can provide consistent training and socialization. They can learn to talk and perform tricks, but their vocal nature makes them unsuitable for apartments or noise-sensitive environments.": "Солнечные конуры - потрясающие птицы с ярким желто-оранжевым оперением. Они чрезвычайно социальны, умны и ласковы, но также очень громки и требовательны. Эти птицы требуют опытных владельцев, которые могут обеспечить последовательную дрессировку и социализацию. Они могут научиться говорить и выполнять трюки, но их вокальная природа делает их непригодными для квартир или шумочувствительных сред.",
    
    "African Grey Parrots are considered among the most intelligent birds in the world. They can learn extensive vocabularies, understand context, and even engage in simple conversations. However, they're also sensitive, prone to stress, and require experienced owners who understand their complex needs. They can be one-person birds and may become aggressive toward others if not properly socialized.": "Африканские серые попугаи считаются одними из самых умных птиц в мире. Они могут выучить обширный словарный запас, понимать контекст и даже участвовать в простых разговорах. Однако они также чувствительны, склонны к стрессу и требуют опытных владельцев, которые понимают их сложные потребности. Они могут быть птицами одного человека и могут стать агрессивными по отношению к другим, если не социализированы должным образом.",
    
    "Blue and Gold Macaws are magnificent large parrots that require expert care and significant commitment. They're intelligent, social, and can be wonderful companions for experienced bird owners. However, they're extremely loud, destructive, and require enormous amounts of space and attention. Their powerful beaks can cause serious injury, and they need consistent training from an early age.": "Сине-желтые ара - великолепные крупные попугаи, которые требуют экспертного ухода и значительных обязательств. Они умны, социальны и могут быть замечательными компаньонами для опытных владельцев птиц. Однако они чрезвычайно громки, разрушительны и требуют огромного количества пространства и внимания. Их мощные клювы могут причинить серьезные травмы, и им нужна последовательная дрессировка с раннего возраста.",
}

def translate_file_content(file_path):
    """翻译文件内容"""
    print(f"翻译文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用所有翻译
        for en_text, ru_text in COMPREHENSIVE_TRANSLATIONS.items():
            content = content.replace(en_text, ru_text)
        
        # 检查是否有变化
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已翻译: {file_path}")
            return True
        else:
            print(f"⏭️  无需翻译: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 翻译文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始全面翻译ru目录下的英文内容...")
    
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
    
    # 翻译每个文件
    translated_count = 0
    for file_path in html_files:
        if translate_file_content(file_path):
            translated_count += 1
    
    print(f"\n✅ 全面翻译完成! 共处理了 {len(html_files)} 个文件，翻译了 {translated_count} 个文件")

if __name__ == "__main__":
    main()