#!/usr/bin/env python3
"""
生成多语言文章系统
为所有50篇文章创建T1国家语言版本
"""

import os
import json
import shutil
from pathlib import Path

# T1国家语言配置
LANGUAGES = {
    'en': 'English',
    'zh': '中文',
    'ja': '日本語', 
    'ko': '한국어',
    'de': 'Deutsch',
    'fr': 'Français',
    'es': 'Español',
    'it': 'Italiano',
    'pt': 'Português',
    'ru': 'Русский'
}

# 文章分类和数量
CATEGORIES = {
    'birdwatching': 10,
    'scientific-wonders': 10,
    'pet-care': 10,
    'ecology': 10,
    'knowledge': 10
}

# 多语言内容模板
ARTICLE_TRANSLATIONS = {
    'birdwatching': {
        'en': {
            'category_name': 'Bird Watching',
            'hero_title': '🔍 Bird Watching',
            'hero_subtitle': 'Master the art of bird observation and identification techniques'
        },
        'zh': {
            'category_name': '观鸟指南',
            'hero_title': '🔍 观鸟指南',
            'hero_subtitle': '掌握鸟类观察和识别的艺术技巧'
        },
        'ja': {
            'category_name': 'バードウォッチング',
            'hero_title': '🔍 バードウォッチング',
            'hero_subtitle': '鳥の観察と識別技術の芸術をマスターする'
        },
        'ko': {
            'category_name': '조류 관찰',
            'hero_title': '🔍 조류 관찰',
            'hero_subtitle': '조류 관찰과 식별 기술의 예술을 마스터하세요'
        },
        'de': {
            'category_name': 'Vogelbeobachtung',
            'hero_title': '🔍 Vogelbeobachtung',
            'hero_subtitle': 'Meistern Sie die Kunst der Vogelbeobachtung und Identifikationstechniken'
        },
        'fr': {
            'category_name': 'Observation des Oiseaux',
            'hero_title': '🔍 Observation des Oiseaux',
            'hero_subtitle': 'Maîtrisez l\'art de l\'observation et des techniques d\'identification des oiseaux'
        },
        'es': {
            'category_name': 'Observación de Aves',
            'hero_title': '🔍 Observación de Aves',
            'hero_subtitle': 'Domina el arte de la observación e identificación de aves'
        },
        'it': {
            'category_name': 'Birdwatching',
            'hero_title': '🔍 Birdwatching',
            'hero_subtitle': 'Padroneggia l\'arte dell\'osservazione e delle tecniche di identificazione degli uccelli'
        },
        'pt': {
            'category_name': 'Observação de Aves',
            'hero_title': '🔍 Observação de Aves',
            'hero_subtitle': 'Domine a arte da observação e técnicas de identificação de aves'
        },
        'ru': {
            'category_name': 'Наблюдение за Птицами',
            'hero_title': '🔍 Наблюдение за Птицами',
            'hero_subtitle': 'Овладейте искусством наблюдения за птицами и техниками идентификации'
        }
    },
    'scientific-wonders': {
        'en': {
            'category_name': 'Scientific Wonders',
            'hero_title': '🔬 Scientific Wonders',
            'hero_subtitle': 'Amazing discoveries and scientific insights about birds'
        },
        'zh': {
            'category_name': '科学奇迹',
            'hero_title': '🔬 科学奇迹',
            'hero_subtitle': '关于鸟类的惊人发现和科学见解'
        },
        'ja': {
            'category_name': '科学の驚異',
            'hero_title': '🔬 科学の驚異',
            'hero_subtitle': '鳥類に関する驚くべき発見と科学的洞察'
        },
        'ko': {
            'category_name': '과학의 경이',
            'hero_title': '🔬 과학의 경이',
            'hero_subtitle': '조류에 대한 놀라운 발견과 과학적 통찰'
        },
        'de': {
            'category_name': 'Wissenschaftliche Wunder',
            'hero_title': '🔬 Wissenschaftliche Wunder',
            'hero_subtitle': 'Erstaunliche Entdeckungen und wissenschaftliche Erkenntnisse über Vögel'
        },
        'fr': {
            'category_name': 'Merveilles Scientifiques',
            'hero_title': '🔬 Merveilles Scientifiques',
            'hero_subtitle': 'Découvertes étonnantes et perspectives scientifiques sur les oiseaux'
        },
        'es': {
            'category_name': 'Maravillas Científicas',
            'hero_title': '🔬 Maravillas Científicas',
            'hero_subtitle': 'Descubrimientos asombrosos y conocimientos científicos sobre las aves'
        },
        'it': {
            'category_name': 'Meraviglie Scientifiche',
            'hero_title': '🔬 Meraviglie Scientifiche',
            'hero_subtitle': 'Scoperte straordinarie e intuizioni scientifiche sugli uccelli'
        },
        'pt': {
            'category_name': 'Maravilhas Científicas',
            'hero_title': '🔬 Maravilhas Científicas',
            'hero_subtitle': 'Descobertas incríveis e insights científicos sobre aves'
        },
        'ru': {
            'category_name': 'Научные Чудеса',
            'hero_title': '🔬 Научные Чудеса',
            'hero_subtitle': 'Удивительные открытия и научные знания о птицах'
        }
    },
    'pet-care': {
        'en': {
            'category_name': 'Pet Care',
            'hero_title': '🐦 Pet Care',
            'hero_subtitle': 'Complete guide to caring for your feathered companions'
        },
        'zh': {
            'category_name': '宠物护理',
            'hero_title': '🐦 宠物护理',
            'hero_subtitle': '照顾您羽毛伙伴的完整指南'
        },
        'ja': {
            'category_name': 'ペットケア',
            'hero_title': '🐦 ペットケア',
            'hero_subtitle': '羽毛の仲間たちのケアの完全ガイド'
        },
        'ko': {
            'category_name': '반려동물 관리',
            'hero_title': '🐦 반려동물 관리',
            'hero_subtitle': '깃털 달린 반려동물을 돌보는 완전한 가이드'
        },
        'de': {
            'category_name': 'Haustierpflege',
            'hero_title': '🐦 Haustierpflege',
            'hero_subtitle': 'Vollständiger Leitfaden zur Pflege Ihrer gefiederten Begleiter'
        },
        'fr': {
            'category_name': 'Soins des Animaux',
            'hero_title': '🐦 Soins des Animaux',
            'hero_subtitle': 'Guide complet pour prendre soin de vos compagnons à plumes'
        },
        'es': {
            'category_name': 'Cuidado de Mascotas',
            'hero_title': '🐦 Cuidado de Mascotas',
            'hero_subtitle': 'Guía completa para cuidar a tus compañeros emplumados'
        },
        'it': {
            'category_name': 'Cura degli Animali',
            'hero_title': '🐦 Cura degli Animali',
            'hero_subtitle': 'Guida completa per prendersi cura dei tuoi compagni piumati'
        },
        'pt': {
            'category_name': 'Cuidados com Animais',
            'hero_title': '🐦 Cuidados com Animais',
            'hero_subtitle': 'Guia completo para cuidar de seus companheiros emplumados'
        },
        'ru': {
            'category_name': 'Уход за Питомцами',
            'hero_title': '🐦 Уход за Питомцами',
            'hero_subtitle': 'Полное руководство по уходу за пернатыми спутниками'
        }
    },
    'ecology': {
        'en': {
            'category_name': 'Ecology',
            'hero_title': '🌿 Ecology',
            'hero_subtitle': 'Understanding bird ecology and environmental relationships'
        },
        'zh': {
            'category_name': '生态学',
            'hero_title': '🌿 生态学',
            'hero_subtitle': '理解鸟类生态学和环境关系'
        },
        'ja': {
            'category_name': '生態学',
            'hero_title': '🌿 生態学',
            'hero_subtitle': '鳥類の生態学と環境関係の理解'
        },
        'ko': {
            'category_name': '생태학',
            'hero_title': '🌿 생태학',
            'hero_subtitle': '조류 생태학과 환경 관계 이해'
        },
        'de': {
            'category_name': 'Ökologie',
            'hero_title': '🌿 Ökologie',
            'hero_subtitle': 'Verständnis der Vogelökologie und Umweltbeziehungen'
        },
        'fr': {
            'category_name': 'Écologie',
            'hero_title': '🌿 Écologie',
            'hero_subtitle': 'Comprendre l\'écologie des oiseaux et les relations environnementales'
        },
        'es': {
            'category_name': 'Ecología',
            'hero_title': '🌿 Ecología',
            'hero_subtitle': 'Entendiendo la ecología de las aves y las relaciones ambientales'
        },
        'it': {
            'category_name': 'Ecologia',
            'hero_title': '🌿 Ecologia',
            'hero_subtitle': 'Comprendere l\'ecologia degli uccelli e le relazioni ambientali'
        },
        'pt': {
            'category_name': 'Ecologia',
            'hero_title': '🌿 Ecologia',
            'hero_subtitle': 'Compreendendo a ecologia das aves e relações ambientais'
        },
        'ru': {
            'category_name': 'Экология',
            'hero_title': '🌿 Экология',
            'hero_subtitle': 'Понимание экологии птиц и экологических взаимосвязей'
        }
    }
}

def create_language_directories():
    """创建语言目录结构"""
    base_dir = Path('.')
    
    for lang_code in LANGUAGES.keys():
        if lang_code == 'en':  # 英语使用根目录
            continue
            
        lang_dir = base_dir / lang_code
        lang_dir.mkdir(exist_ok=True)
        
        # 为每个分类创建目录
        for category in CATEGORIES.keys():
            category_dir = lang_dir / category
            category_dir.mkdir(exist_ok=True)

def generate_article_template(category, article_num, language):
    """生成文章模板"""
    translations = ARTICLE_TRANSLATIONS.get(category, {}).get(language, {})
    
    # 如果没有翻译，使用英语作为后备
    if not translations:
        translations = ARTICLE_TRANSLATIONS.get(category, {}).get('en', {})
    
    article_id = f"{article_num:02d}"
    
    template = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{translations.get('category_name', 'Article')} - BirdAiSnap</title>
    <link rel="stylesheet" href="{'../' if language != 'en' else ''}styles.css">
    <link rel="stylesheet" href="{'../' if language != 'en' else ''}knowledge.css">
    <script src="{'../' if language != 'en' else ''}language-router.js"></script>
    <script src="{'../' if language != 'en' else ''}script.js"></script>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2><a href="{'../' if language != 'en' else ''}index.html">BirdAiSnap</a></h2>
            </div>
            <ul class="nav-menu">
                <li><a href="{'../' if language != 'en' else ''}index.html#home" data-i18n="nav.home">Home</a></li>
                <li><a href="{'../' if language != 'en' else ''}index.html#features" data-i18n="nav.features">Features</a></li>
                <li><a href="{'../' if language != 'en' else ''}index.html#about" data-i18n="nav.about">About</a></li>
                <li><a href="{'../' if language != 'en' else ''}index.html#contact" data-i18n="nav.contact">Contact</a></li>
                <li><a href="{'../' if language != 'en' else ''}knowledge.html" data-i18n="nav.knowledge">Knowledge</a></li>
            </ul>
            <div class="language-switcher">
                <select id="languageSelector" onchange="languageRouter.switchLanguage(this.value)">
                    <option value="en">English</option>
                    <option value="zh">中文</option>
                    <option value="ja">日本語</option>
                    <option value="ko">한국어</option>
                    <option value="de">Deutsch</option>
                    <option value="fr">Français</option>
                    <option value="es">Español</option>
                    <option value="it">Italiano</option>
                    <option value="pt">Português</option>
                    <option value="ru">Русский</option>
                </select>
            </div>
        </div>
    </nav>

    <!-- 主要内容 -->
    <main>
        <!-- 页面头部 -->
        <section class="knowledge-hero">
            <div class="container">
                <h1>{translations.get('hero_title', 'Article')}</h1>
                <p>{translations.get('hero_subtitle', 'Article content')}</p>
            </div>
        </section>

        <!-- 文章内容 -->
        <section class="article-content">
            <div class="container">
                <div class="article-header">
                    <span class="category-badge">{translations.get('category_name', 'Category')}</span>
                    <h2>Article {article_id} - {language.upper()}</h2>
                    <div class="article-meta">
                        <span>Language: {LANGUAGES[language]}</span>
                        <span>Category: {category}</span>
                    </div>
                </div>
                
                <div class="article-body">
                    <p>This is a sample article in {LANGUAGES[language]} for {category} category, article number {article_id}.</p>
                    <p>Content would be translated and localized for the {language} market.</p>
                    
                    <!-- 语言切换提示 -->
                    <div class="language-notice">
                        <p>This article is available in multiple languages. Use the language selector above to switch.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- 页脚 -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>BirdAiSnap</h3>
                    <p data-i18n="footer.description">Smart bird recognition powered by AI technology</p>
                </div>
                <div class="footer-section">
                    <h4 data-i18n="footer.quicklinks">Quick Links</h4>
                    <ul>
                        <li><a href="{'../' if language != 'en' else ''}index.html" data-i18n="nav.home">Home</a></li>
                        <li><a href="{'../' if language != 'en' else ''}knowledge.html" data-i18n="nav.knowledge">Knowledge Center</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 data-i18n="footer.contact">Contact</h4>
                    <p data-i18n="footer.email">Email: lingjuetech@gmail.com</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Hangzhou Lingjue Technology Co., Ltd. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>"""
    
    return template

def generate_all_articles():
    """生成所有文章的多语言版本"""
    print("🚀 开始生成多语言文章...")
    
    # 创建目录结构
    create_language_directories()
    
    total_articles = 0
    
    for category, count in CATEGORIES.items():
        print(f"\n📁 处理分类: {category}")
        
        for article_num in range(1, count + 1):
            for lang_code in LANGUAGES.keys():
                # 生成文章内容
                content = generate_article_template(category, article_num, lang_code)
                
                # 确定文件路径
                if lang_code == 'en':
                    file_path = Path(category) / f"{article_num:02d}-article.html"
                else:
                    file_path = Path(lang_code) / category / f"{article_num:02d}-article.html"
                
                # 确保目录存在
                file_path.parent.mkdir(parents=True, exist_ok=True)
                
                # 写入文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                total_articles += 1
                print(f"  ✅ 创建: {file_path}")
    
    print(f"\n🎉 完成！总共生成了 {total_articles} 篇文章")
    print(f"📊 统计: {len(CATEGORIES)} 个分类 × {sum(CATEGORIES.values())} 篇文章 × {len(LANGUAGES)} 种语言")

if __name__ == "__main__":
    generate_all_articles()