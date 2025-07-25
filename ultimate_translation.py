#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
终极翻译脚本 - 处理ru目录下所有剩余的英文内容
"""

import os
import re
from pathlib import Path

# 终极翻译字典 - 包含所有可能的英文内容
ULTIMATE_TRANSLATIONS = {
    # HTML标签内容
    "stat-label\">Noise Level": "stat-label\">Уровень шума",
    "stat-label\">Care Level": "stat-label\">Уровень ухода",
    "stat-value\">Low-Moderate": "stat-value\">Низкий-Средний",
    "stat-value\">Moderate": "stat-value\">Средний",
    "stat-value\">Moderate-High": "stat-value\">Средний-Высокий",
    "stat-value\">Very High": "stat-value\">Очень высокий",
    "stat-value\">High": "stat-value\">Высокий",
    "stat-value\">Low": "stat-value\">Низкий",
    "stat-value\">Beginner": "stat-value\">Начинающий",
    "stat-value\">Intermediate": "stat-value\">Средний",
    "stat-value\">Advanced": "stat-value\">Продвинутый",
    "stat-value\">Expert": "stat-value\">Эксперт",
    "stat-value\">Beginner-friendly": "stat-value\">Для начинающих",
    "stat-value\">Low to moderate": "stat-value\">От низкого до среднего",
    "stat-value\">Moderate to high": "stat-value\">От среднего до высокого",
    "stat-value\">Intermediate to advanced": "stat-value\">От среднего до продвинутого",
    
    # 标题和章节
    "section-title\">Intermediate Species": "section-title\">Виды среднего уровня",
    "section-title\">Advanced Species": "section-title\">Продвинутые виды",
    "section-title\">Beginner-Friendly Species": "section-title\">Виды для начинающих",
    "section-title\">Choosing the Right Species": "section-title\">Выбор подходящего вида",
    "section-title\">Understanding Bird Aging": "section-title\">Понимание старения птиц",
    "section-title\">Common Age-Related Health Issues": "section-title\">Распространенные возрастные проблемы со здоровьем",
    "section-title\">Environmental Modifications": "section-title\">Модификации окружающей среды",
    "section-title\">Nutritional Needs for Senior Birds": "section-title\">Потребности в питании для пожилых птиц",
    "section-title\">Veterinary Care for Senior Birds": "section-title\">Ветеринарная помощь для пожилых птиц",
    "section-title\">Mental and Social Needs": "section-title\">Психические и социальные потребности",
    "section-title\">End-of-Life Considerations": "section-title\">Соображения конца жизни",
    "section-title\">Supporting Senior Bird Owners": "section-title\">Поддержка владельцев пожилых птиц",
    "section-title\">Understanding Bird Enrichment Needs": "section-title\">Понимание потребностей птиц в обогащении",
    "section-title\">Foraging Activities": "section-title\">Активности поиска пищи",
    "section-title\">DIY Toy Projects": "section-title\">Проекты игрушек своими руками",
    "section-title\">Advanced Techniques": "section-title\">Продвинутые техники",
    
    # 护理要求标题
    "care-title\">Care Requirements:": "care-title\">Требования по уходу:",
    "care-title\">Care Requirements": "care-title\">Требования по уходу",
    
    # 物种名称
    "species-name\">Sun Conure": "species-name\">Солнечный конур",
    "species-name\">African Grey Parrot": "species-name\">Африканский серый попугай",
    "species-name\">Blue and Gold Macaw": "species-name\">Сине-желтый ара",
    
    # 提示框标题
    "tip-title\">🏠 Visit Before You Decide": "tip-title\">🏠 Посетите перед принятием решения",
    "tip-title\">🛏️ Comfort First": "tip-title\">🛏️ Комфорт прежде всего",
    "tip-title\">💡 Learning Tips for Beginners": "tip-title\">💡 Советы по обучению для начинающих",
    
    # 警告框标题
    "warning-title\">⚠️ Weight Management": "warning-title\">⚠️ Управление весом",
    
    # 健康卡片标题
    "🦴 Arthritis and Joint Issues": "🦴 Артрит и проблемы с суставами",
    "❤️ Heart Disease": "❤️ Болезни сердца",
    "🫁 Respiratory Issues": "🫁 Проблемы с дыханием",
    "🍽️ Digestive Problems": "🍽️ Проблемы с пищеварением",
    "👁️ Vision Problems": "👁️ Проблемы со зрением",
    "🧠 Cognitive Changes": "🧠 Когнитивные изменения",
    
    # 丰富活动卡片
    "🍽️ Foraging Enrichment": "🍽️ Обогащение поиском пищи",
    "🎯 Cognitive Enrichment": "🎯 Когнитивное обогащение",
    "🏃 Physical Enrichment": "🏃 Физическое обогащение",
    "👥 Social Enrichment": "👥 Социальное обогащение",
    "🎨 Sensory Enrichment": "🎨 Сенсорное обогащение",
    "🏠 Environmental Enrichment": "🏠 Экологическое обогащение",
    
    # DIY项目标题
    "🛠️ DIY Foraging Box": "🛠️ Коробка для поиска пищи своими руками",
    "🧻 Paper Roll Shredder": "🧻 Измельчитель бумажных рулонов",
    
    # 基本词汇和短语
    "Care Level:": "Уровень ухода:",
    "Noise Level:": "Уровень шума:",
    "Care Level": "Уровень ухода",
    "Noise Level": "Уровень шума",
    "Beginner": "Начинающий",
    "Intermediate": "Средний",
    "Advanced": "Продвинутый",
    "Expert": "Эксперт",
    "Beginner-friendly": "Для начинающих",
    "Low-Moderate": "Низкий-Средний",
    "Moderate": "Средний",
    "Moderate-High": "Средний-Высокий",
    "Very High": "Очень высокий",
    "High": "Высокий",
    "Low": "Низкий",
    "Low to moderate": "От низкого до среднего",
    "Moderate to high": "От среднего до высокого",
    "Intermediate to advanced": "От среднего до продвинутого",
    
    # 经验等级匹配
    "Experience Level Matching:": "Соответствие уровню опыта:",
    "Beginners: Budgies, canaries, cockatiels": "Начинающие: волнистые попугайчики, канарейки, кореллы",
    "Intermediate: Lovebirds, small conures, parrotlets": "Средний уровень: неразлучники, маленькие конуры, попугайчики",
    "Advanced: Large conures, small macaws, amazons": "Продвинутый: крупные конуры, маленькие ара, амазоны",
    "Expert: African greys, large macaws, cockatoos": "Эксперт: африканские серые, крупные ара, какаду",
    "Consider starting smaller and working up": "Рассмотрите возможность начать с меньших и продвигаться вверх",
    
    # 生活方式兼容性
    "Lifestyle Compatibility:": "Совместимость с образом жизни:",
    "Noise tolerance and living situation": "Толерантность к шуму и жилищная ситуация",
    "Available time for interaction and training": "Доступное время для взаимодействия и обучения",
    "Experience with bird behavior and training": "Опыт работы с поведением и дрессировкой птиц",
    "Long-term commitment capability": "Способность к долгосрочным обязательствам",
    
    # 特殊考虑
    "Special Considerations:": "Особые соображения:",
    "Some species do better in pairs": "Некоторые виды лучше живут парами",
    "Research specific dietary and housing needs": "Изучите специфические потребности в питании и жилье",
    "Factor in veterinary costs and availability": "Учтите ветеринарные расходы и доступность",
    
    # 个性描述
    "Personality:": "Личность:",
    "Social, playful, can learn to talk": "Социальные, игривые, могут научиться говорить",
    "Gentle, affectionate, whistlers": "Нежные, ласковые, свистуны",
    "Energetic, playful, can be territorial": "Энергичные, игривые, могут быть территориальными",
    "Independent, excellent singers": "Независимые, отличные певцы",
    "Playful, loud, affectionate": "Игривые, громкие, ласковые",
    "Highly intelligent, can be sensitive": "Очень умные, могут быть чувствительными",
    
    # 描述文本
    "Perfect for first-time bird owners. They're social, relatively quiet, and can learn simple words and tricks.": "Идеально подходят для начинающих владельцев птиц. Они социальны, относительно тихи и могут выучить простые слова и трюки.",
    "Known for their distinctive crest and gentle nature. They're excellent whistlers and can learn melodies.": "Известны своим характерным хохолком и нежным характером. Они отличные свистуны и могут выучить мелодии.",
    "Colorful and energetic birds that do well in pairs. They're active and require plenty of toys and stimulation.": "Красочные и энергичные птицы, которые хорошо живут парами. Они активны и требуют много игрушек и стимуляции.",
    "Beautiful singers that don't require as much social interaction. Perfect for those who enjoy bird songs.": "Красивые певцы, которые не требуют столько социального взаимодействия. Идеально подходят для тех, кто наслаждается птичьими песнями.",
    "Colorful, playful birds with big personalities. They can be quite loud and require experienced owners.": "Красочные, игривые птицы с большими личностями. Они могут быть довольно громкими и требуют опытных владельцев.",
    "Extremely intelligent birds that require experienced owners and consistent mental stimulation.": "Чрезвычайно умные птицы, которые требуют опытных владельцев и постоянной умственной стимуляции.",
    
    # 年龄相关
    "When Birds Are Considered Senior:": "Когда птицы считаются пожилыми:",
    "Small birds (budgies, canaries): 5-7 years": "Маленькие птицы (волнистые попугайчики, канарейки): 5-7 лет",
    "Medium birds (cockatiels, conures): 10-15 years": "Средние птицы (кореллы, конуры): 10-15 лет",
    "Large birds (macaws, cockatoos): 20-30 years": "Крупные птицы (ара, какаду): 20-30 лет",
    "Individual variation based on genetics and care": "Индивидуальные различия на основе генетики и ухода",
    "Species-specific lifespans vary considerably": "Продолжительность жизни, специфичная для видов, значительно варьируется",
    
    # 身体衰老迹象
    "Physical Signs of Aging:": "Физические признаки старения:",
    "Decreased activity and energy levels": "Снижение активности и уровня энергии",
    "Changes in feather quality and molting patterns": "Изменения в качестве перьев и схемах линьки",
    "Slower movement and reaction times": "Замедление движений и времени реакции",
    "Weight fluctuations": "Колебания веса",
    "Reduced muscle mass and strength": "Снижение мышечной массы и силы",
    "Changes in beak and claw condition": "Изменения в состоянии клюва и когтей",
    
    # 行为变化
    "Behavioral Changes in Senior Birds:": "Поведенческие изменения у пожилых птиц:",
    "Increased sleeping and resting": "Увеличение сна и отдыха",
    "Reduced vocalization": "Снижение вокализации",
    "Changes in social interaction preferences": "Изменения в предпочтениях социального взаимодействия",
    "Possible increased irritability or sensitivity": "Возможное увеличение раздражительности или чувствительности",
    "Altered eating and drinking patterns": "Измененные схемы питания и питья",
    "Decreased interest in toys and activities": "Снижение интереса к игрушкам и активностям",
    
    # 症状描述
    "Symptoms:": "Симптомы:",
    "Difficulty perching, reluctance to move": "Трудности с сидением на жердочке, нежелание двигаться",
    "Exercise intolerance, breathing difficulty": "Непереносимость физических нагрузок, затрудненное дыхание",
    "Labored breathing, tail bobbing": "Затрудненное дыхание, покачивание хвостом",
    "Poor appetite, weight loss": "Плохой аппетит, потеря веса",
    "Bumping into objects, hesitation": "Столкновение с предметами, колебания",
    "Confusion, repetitive behaviors": "Замешательство, повторяющееся поведение",
    
    # 环境修改
    "Cage Modifications:": "Модификации клетки:",
    "Lower perch placement for easier access": "Более низкое размещение жердочек для облегчения доступа",
    "Softer perch materials to reduce joint stress": "Более мягкие материалы жердочек для снижения нагрузки на суставы",
    "Multiple food and water stations": "Множественные станции для еды и воды",
    "Easy-access cage doors": "Легкодоступные дверцы клетки",
    "Non-slip surfaces on cage bottom": "Нескользящие поверхности на дне клетки",
    
    # 舒适增强
    "Comfort Enhancements:": "Улучшения комфорта:",
    "Warmer environment (75-80°F)": "Более теплая среда (24-27°C)",
    "Draft-free location": "Место без сквозняков",
    "Consistent lighting schedule": "Постоянный график освещения",
    "Quiet, stress-free environment": "Тихая, свободная от стресса среда",
    "Comfortable bedding materials": "Удобные материалы для подстилки",
    
    # 安全考虑
    "Safety Considerations:": "Соображения безопасности:",
    "Remove high perches that could cause falls": "Удалите высокие жердочки, которые могут привести к падениям",
    "Ensure easy access to food and water": "Обеспечьте легкий доступ к еде и воде",
    "Monitor for signs of discomfort or pain": "Следите за признаками дискомфорта или боли",
    "Regular health check-ups": "Регулярные медицинские осмотры",
    "Secure cage placement to prevent accidents": "Безопасное размещение клетки для предотвращения несчастных случаев",
    
    # 营养相关
    "Senior Diet Considerations:": "Соображения по диете для пожилых:",
    "Easily digestible foods": "Легко усваиваемые продукты",
    "Higher quality protein sources": "Источники белка более высокого качества",
    "Reduced portion sizes, more frequent meals": "Уменьшенные порции, более частые приемы пищи",
    "Softer food textures when needed": "Более мягкие текстуры пищи при необходимости",
    "Increased hydration support": "Увеличенная поддержка гидратации",
    
    # 有益食物
    "Beneficial Foods for Seniors:": "Полезные продукты для пожилых:",
    "Cooked quinoa and brown rice": "Вареная киноа и коричневый рис",
    "Steamed vegetables": "Приготовленные на пару овощи",
    "Soft fruits like banana and cooked sweet potato": "Мягкие фрукты, такие как банан и вареный сладкий картофель",
    "High-quality pellets designed for senior birds": "Высококачественные гранулы, предназначенные для пожилых птиц",
    "Omega-3 rich foods like flaxseed": "Богатые омега-3 продукты, такие как льняное семя",
    
    # 补充剂
    "Supplements for Senior Birds:": "Добавки для пожилых птиц:",
    "Omega-3 fatty acids for joint health": "Омега-3 жирные кислоты для здоровья суставов",
    "Probiotics for digestive support": "Пробиотики для поддержки пищеварения",
    "Vitamin D3 for bone health": "Витамин D3 для здоровья костей",
    "Antioxidants for cognitive support": "Антиоксиданты для когнитивной поддержки",
    "Glucosamine for joint support": "Глюкозамин для поддержки суставов",
    
    # 兽医护理
    "Recommended Veterinary Schedule:": "Рекомендуемый график ветеринарных осмотров:",
    "Semi-annual wellness exams (every 6 months)": "Полугодовые осмотры здоровья (каждые 6 месяцев)",
    "More frequent monitoring of chronic conditions": "Более частый мониторинг хронических состояний",
    "Immediate attention for any behavioral changes": "Немедленное внимание к любым поведенческим изменениям",
    "Preventive care to catch issues early": "Профилактическая помощь для раннего выявления проблем",
    
    # 健康筛查
    "Senior Bird Health Screening:": "Скрининг здоровья пожилых птиц:",
    "Complete blood chemistry panel": "Полная панель биохимии крови",
    "X-rays to check for arthritis or organ changes": "Рентген для проверки артрита или изменений органов",
    "Fecal examination for parasites": "Исследование кала на паразитов",
    "Weight and body condition assessment": "Оценка веса и состояния тела",
    "Vision and hearing evaluation": "Оценка зрения и слуха",
    
    # 慢性病管理
    "Managing Chronic Conditions:": "Управление хроническими состояниями:",
    "Daily medication administration": "Ежедневное введение лекарств",
    "Environmental modifications for comfort": "Модификации окружающей среды для комфорта",
    "Regular monitoring and adjustment of treatment": "Регулярный мониторинг и корректировка лечения",
    "Pain management strategies": "Стратегии управления болью",
    "Quality of life assessments": "Оценки качества жизни",
    
    # 心理和社交需求
    "Age-Appropriate Enrichment:": "Соответствующее возрасту обогащение:",
    "Gentle, low-impact activities": "Мягкие, низкоинтенсивные активности",
    "Familiar toys and routines": "Знакомые игрушки и рутины",
    "Shorter play sessions": "Более короткие игровые сессии",
    "Comfortable resting areas": "Удобные места для отдыха",
    "Sensory stimulation appropriate for abilities": "Сенсорная стимуляция, соответствующая способностям",
    
    # 社交互动调整
    "Social Interaction Adjustments:": "Корректировки социального взаимодействия:",
    "Shorter, more frequent interaction sessions": "Более короткие, более частые сессии взаимодействия",
    "Respect for increased need for rest": "Уважение к возросшей потребности в отдыхе",
    "Gentle handling and reduced stress": "Бережное обращение и снижение стресса",
    "Maintaining familiar social bonds": "Поддержание знакомых социальных связей",
    "Patience with slower responses": "Терпение к более медленным реакциям",
    
    # 认知支持
    "Cognitive Support:": "Когнитивная поддержка:",
    "Simple training exercises": "Простые тренировочные упражнения",
    "Consistent daily routines": "Постоянные ежедневные рутины",
    "Mental stimulation through gentle activities": "Умственная стимуляция через мягкие активности",
    "Familiar environment and minimal changes": "Знакомая среда и минимальные изменения",
    "Memory-supporting activities": "Активности, поддерживающие память",
    
    # 生命终期考虑
    "Quality of Life Indicators:": "Показатели качества жизни:",
    "Appetite and interest in food": "Аппетит и интерес к еде",
    "Social interaction and responsiveness": "Социальное взаимодействие и отзывчивость",
    "Mobility and comfort level": "Подвижность и уровень комфорта",
    "Overall alertness and engagement": "Общая бдительность и вовлеченность",
    "Pain levels and management": "Уровни боли и управление",
    
    # 姑息治疗选择
    "Palliative Care Options:": "Варианты паллиативной помощи:",
    "Pain management medications": "Лекарства для управления болью",
    "Comfort-focused environmental modifications": "Модификации окружающей среды, ориентированные на комфорт",
    "Supportive nutritional therapy": "Поддерживающая пищевая терапия",
    "Gentle, compassionate care": "Мягкий, сострадательный уход",
    "Stress reduction techniques": "Техники снижения стресса",
    
    # 困难决定
    "Making Difficult Decisions:": "Принятие трудных решений:",
    "Consult with experienced avian veterinarian": "Консультация с опытным орнитологическим ветеринаром",
    "Consider bird's quality of life objectively": "Объективно оцените качество жизни птицы",
    "Discuss options with family members": "Обсудите варианты с членами семьи",
    "Seek support from bird community": "Обратитесь за поддержкой к сообществу птицеводов",
    "Take time to process emotions": "Найдите время для обработки эмоций",
    
    # 支持老年鸟主人
    "Building Support Networks:": "Создание сетей поддержки:",
    "Join senior bird care groups": "Присоединяйтесь к группам по уходу за пожилыми птицами",
    "Connect with experienced bird owners": "Связывайтесь с опытными владельцами птиц",
    "Maintain relationships with avian veterinarians": "Поддерживайте отношения с орнитологическими ветеринарами",
    "Seek emotional support when needed": "Обращайтесь за эмоциональной поддержкой при необходимости",
    "Share experiences and learn from others": "Делитесь опытом и учитесь у других",
    
    # 丰富活动目的
    "Purpose:": "Цель:",
    "Mimics natural food-seeking behavior": "Имитирует естественное поведение поиска пищи",
    "Challenges problem-solving abilities": "Вызывает способности решения проблем",
    "Promotes exercise and movement": "Способствует упражнениям и движению",
    "Fulfills social interaction needs": "Удовлетворяет потребности в социальном взаимодействии",
    "Stimulates different senses": "Стимулирует различные чувства",
    "Creates interesting living spaces": "Создает интересные жилые пространства",
    
    # 觅食活动
    "Simple Foraging Ideas:": "Простые идеи поиска пищи:",
    "Hide treats in paper cups or small boxes": "Прячьте лакомства в бумажные стаканчики или маленькие коробки",
    "Wrap food in paper or leaves": "Заворачивайте еду в бумагу или листья",
    "Use puzzle feeders and treat balls": "Используйте кормушки-головоломки и шарики с лакомствами",
    "Create foraging trees with multiple hiding spots": "Создавайте деревья для поиска пищи с множественными укрытиями",
    "Scatter feeding on cage floor": "Разбрасывайте корм по дну клетки",
    
    # 高级觅食挑战
    "Advanced Foraging Challenges:": "Продвинутые вызовы поиска пищи:",
    "Multi-level puzzle feeders": "Многоуровневые кормушки-головоломки",
    "Rotating treat dispensers": "Вращающиеся дозаторы лакомств",
    "Hidden compartment toys": "Игрушки со скрытыми отделениями",
    "Foraging wheels and spinning devices": "Колеса для поиска пищи и вращающиеся устройства",
    "Complex puzzle boxes": "Сложные коробки-головоломки",
    
    # 大型鸟类特殊需求
    "Large Birds (Macaws, African Greys):": "Крупные птицы (ара, африканские серые):",
    "Advanced problem-solving puzzles": "Продвинутые головоломки для решения проблем",
    "Large foraging opportunities": "Большие возможности для поиска пищи",
    "Destructible toys for beak exercise": "Разрушаемые игрушки для упражнения клюва",
    "Social interaction challenges": "Вызовы социального взаимодействия",
    
    # DIY材料和说明
    "Materials:": "Материалы:",
    "Small cardboard box, paper shreds, bird-safe treats": "Маленькая картонная коробка, измельченная бумага, безопасные для птиц лакомства",
    "Toilet paper rolls, bird-safe paper, treats": "Рулоны туалетной бумаги, безопасная для птиц бумага, лакомства",
    "Instructions:": "Инструкции:",
    "Fill box with paper shreds and hide treats throughout": "Заполните коробку измельченной бумагой и спрячьте лакомства по всей коробке",
    "Stuff rolls with paper and treats, hang in cage": "Набейте рулоны бумагой и лакомствами, повесьте в клетке",
    
    # 提示框内容
    "Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.": "Сначала сосредоточьтесь на размере и форме, замечайте поведенческие паттерны, слушайте звуки, используйте сравнения размеров и всегда делайте заметки о том, что наблюдаете.",
    "Spend time with different species at bird rescues, pet stores, or bird shows before making your decision. Each species has a unique personality and energy level.": "Проведите время с разными видами в приютах для птиц, зоомагазинах или выставках птиц перед принятием решения. Каждый вид имеет уникальную личность и уровень энергии.",
    "Senior birds prioritize comfort over activity. Focus on making their environment as comfortable and accessible as possible.": "Пожилые птицы отдают приоритет комфорту над активностью. Сосредоточьтесь на том, чтобы сделать их среду максимально комфортной и доступной.",
    
    # 警告框内容
    "Monitor weight regularly": "Регулярно контролируйте вес",
    "Adjust portions based on activity level": "Корректируйте порции в зависимости от уровня активности",
    "Consult vet for significant weight changes": "Консультируйтесь с ветеринаром при значительных изменениях веса",
    
    # 按钮和导航
    "Back Button": "Кнопка назад",
    "Hero Image": "Главное изображение", 
    "Main Content": "Основное содержание",
    
    # 注释
    "<!-- Back Button -->": "<!-- Кнопка назад -->",
    "<!-- Hero Image -->": "<!-- Главное изображение -->",
    "<!-- Main Content -->": "<!-- Основное содержание -->",
}

def translate_file_comprehensive(file_path):
    """全面翻译文件内容"""
    print(f"翻译文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用所有翻译
        for en_text, ru_text in ULTIMATE_TRANSLATIONS.items():
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
    print("开始终极翻译ru目录下的所有英文内容...")
    
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
        if translate_file_comprehensive(file_path):
            translated_count += 1
    
    print(f"\n✅ 终极翻译完成! 共处理了 {len(html_files)} 个文件，翻译了 {translated_count} 个文件")
    
    # 最终检查
    print("\n进行最终检查...")
    remaining_issues = []
    
    # 检查特定的英文模式
    check_patterns = [
        "Care Level", "Noise Level", "Beginner", "Intermediate", "Advanced", "Expert",
        "Back Button", "Hero Image", "Main Content", "Understanding Bird",
        "Species Profiles", "Emergency First Aid", "Getting Started"
    ]
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for pattern in check_patterns:
                if pattern in content:
                    remaining_issues.append((str(file_path), pattern))
        
        except Exception as e:
            print(f"检查文件 {file_path} 时出错: {e}")
    
    if remaining_issues:
        print(f"\n⚠️  发现 {len(remaining_issues)} 处需要手动检查的内容:")
        for file_path, text in remaining_issues[:20]:  # 只显示前20个
            print(f"  {file_path}: {text}")
        if len(remaining_issues) > 20:
            print(f"  ... 还有 {len(remaining_issues) - 20} 处")
    else:
        print("\n🎉 所有英文内容都已成功翻译为俄语!")

if __name__ == "__main__":
    main()
