#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高质量多语言翻译优化脚本
优化法语、德语、日语的翻译质量
"""

import os
import re
import json
from pathlib import Path

class TranslationOptimizer:
    def __init__(self):
        self.base_dir = Path('.')
        
        # 高质量翻译词典
        self.translations = {
            'fr': {
                # 基础词汇
                'Bird Watching': 'Observation des Oiseaux',
                'Birdwatching': 'Observation des Oiseaux',
                'for Beginners': 'pour Débutants',
                'Getting Started': 'Commencer',
                'Essential Equipment': 'Équipement Essentiel',
                'Identification Techniques': 'Techniques d\'Identification',
                'Best Locations': 'Meilleurs Emplacements',
                'Seasonal Guide': 'Guide Saisonnier',
                'Photography Tips': 'Conseils de Photographie',
                'Behavior Observation': 'Observation du Comportement',
                'Song Identification': 'Identification des Chants',
                'Ethics Conservation': 'Éthique et Conservation',
                'Journal Keeping': 'Tenue de Journal',
                
                # 内容翻译
                'Discover the joy of birdwatching': 'Découvrez la joie de l\'observation des oiseaux',
                'your gateway to nature\'s most fascinating creatures': 'votre porte d\'entrée vers les créatures les plus fascinantes de la nature',
                'Bird watching is one of the most rewarding': 'L\'observation des oiseaux est l\'un des passe-temps les plus gratifiants',
                'and accessible hobbies in the world': 'et accessibles au monde',
                'Whether you\'re drawn to the beauty of birds': 'Que vous soyez attiré par la beauté des oiseaux',
                'fascinated by their behaviors': 'fasciné par leurs comportements',
                'or simply enjoy being outdoors': 'ou que vous aimiez simplement être à l\'extérieur',
                'birding offers endless opportunities': 'l\'ornithologie offre des opportunités infinies',
                'for discovery and wonder': 'de découverte et d\'émerveillement',
                
                # 步骤和说明
                'Start in Your Backyard': 'Commencez dans Votre Jardin',
                'Begin by observing birds': 'Commencez par observer les oiseaux',
                'in your own yard or neighborhood': 'dans votre propre jardin ou quartier',
                'Spend 15-20 minutes each morning': 'Passez 15-20 minutes chaque matin',
                'watching and listening': 'à regarder et écouter',
                'Get Basic Equipment': 'Obtenez l\'Équipement de Base',
                'Invest in simple binoculars': 'Investissez dans des jumelles simples',
                'and download a bird identification app': 'et téléchargez une application d\'identification des oiseaux',
                'Learn Common Species': 'Apprenez les Espèces Communes',
                'Focus on identifying 5-10 common birds': 'Concentrez-vous sur l\'identification de 5-10 oiseaux communs',
                'in your area first': 'dans votre région d\'abord',
                'Quality over quantity is key': 'La qualité prime sur la quantité',
                'for beginners': 'pour les débutants',
                
                # 鸟类名称
                'American Robin': 'Merle d\'Amérique',
                'Northern Cardinal': 'Cardinal Rouge',
                'Blue Jay': 'Geai Bleu',
                'House Sparrow': 'Moineau Domestique',
                'Mourning Dove': 'Tourterelle Triste',
                'Red-winged Blackbird': 'Carouge à Épaulettes',
                
                # 描述
                'Orange breast, dark head': 'Poitrine orange, tête sombre',
                'Often seen hopping on lawns': 'Souvent vu sautillant sur les pelouses',
                'Bright red male, brown female': 'Mâle rouge vif, femelle brune',
                'Clear whistled songs': 'Chants sifflés clairs',
                'Bright blue with white underparts': 'Bleu vif avec parties inférieures blanches',
                'Intelligent behavior': 'Comportement intelligent',
                'Small brown bird': 'Petit oiseau brun',
                'Very common around homes': 'Très commun autour des maisons',
                'Soft gray-brown': 'Gris-brun doux',
                'Distinctive cooing call': 'Appel roucoulant distinctif',
                'Black male with red shoulder patches': 'Mâle noir avec épaulettes rouges',
                
                # 提示和建议
                'Benefits of Birdwatching': 'Avantages de l\'Observation des Oiseaux',
                'Connect with nature': 'Se connecter avec la nature',
                'reduce stress': 'réduire le stress',
                'get gentle exercise': 'faire de l\'exercice doux',
                'join a welcoming community': 'rejoindre une communauté accueillante',
                'of fellow enthusiasts': 'd\'autres passionnés',
                'Learning Tips for Beginners': 'Conseils d\'Apprentissage pour Débutants',
                'Focus on size and shape first': 'Concentrez-vous d\'abord sur la taille et la forme',
                'notice behavior patterns': 'remarquez les modèles de comportement',
                'listen to sounds': 'écoutez les sons',
                'use size comparisons': 'utilisez les comparaisons de taille',
                'always take notes': 'prenez toujours des notes',
                'of what you observe': 'de ce que vous observez',
                
                # 时间和地点
                'Best Times for Birding': 'Meilleurs Moments pour l\'Observation',
                'Early morning': 'Tôt le matin',
                'first 2-3 hours after sunrise': 'les 2-3 premières heures après le lever du soleil',
                'late afternoon before sunset': 'fin d\'après-midi avant le coucher du soleil',
                'overcast days': 'jours nuageux',
                'after storms': 'après les orages',
                'when weather changes trigger': 'quand les changements météorologiques déclenchent',
                'increased bird activity': 'une activité aviaire accrue'
            },
            
            'de': {
                # 基础词汇
                'Bird Watching': 'Vogelbeobachtung',
                'Birdwatching': 'Vogelbeobachtung',
                'for Beginners': 'für Anfänger',
                'Getting Started': 'Erste Schritte',
                'Essential Equipment': 'Grundausstattung',
                'Identification Techniques': 'Bestimmungstechniken',
                'Best Locations': 'Beste Standorte',
                'Seasonal Guide': 'Saisonaler Leitfaden',
                'Photography Tips': 'Fotografietipps',
                'Behavior Observation': 'Verhaltensbeobachtung',
                'Song Identification': 'Gesangserkennung',
                'Ethics Conservation': 'Ethik und Naturschutz',
                'Journal Keeping': 'Tagebuchführung',
                
                # 内容翻译
                'Discover the joy of birdwatching': 'Entdecken Sie die Freude der Vogelbeobachtung',
                'your gateway to nature\'s most fascinating creatures': 'Ihr Tor zu den faszinierendsten Geschöpfen der Natur',
                'Bird watching is one of the most rewarding': 'Die Vogelbeobachtung ist eines der lohnendsten',
                'and accessible hobbies in the world': 'und zugänglichsten Hobbys der Welt',
                'Whether you\'re drawn to the beauty of birds': 'Ob Sie von der Schönheit der Vögel angezogen werden',
                'fascinated by their behaviors': 'von ihrem Verhalten fasziniert sind',
                'or simply enjoy being outdoors': 'oder einfach gerne draußen sind',
                'birding offers endless opportunities': 'bietet das Birding endlose Möglichkeiten',
                'for discovery and wonder': 'für Entdeckung und Staunen',
                
                # 步骤和说明
                'Start in Your Backyard': 'Beginnen Sie in Ihrem Garten',
                'Begin by observing birds': 'Beginnen Sie mit der Beobachtung von Vögeln',
                'in your own yard or neighborhood': 'in Ihrem eigenen Garten oder in der Nachbarschaft',
                'Spend 15-20 minutes each morning': 'Verbringen Sie jeden Morgen 15-20 Minuten',
                'watching and listening': 'mit Beobachten und Zuhören',
                'Get Basic Equipment': 'Grundausstattung besorgen',
                'Invest in simple binoculars': 'Investieren Sie in ein einfaches Fernglas',
                'and download a bird identification app': 'und laden Sie eine Vogelbestimmungs-App herunter',
                'Learn Common Species': 'Häufige Arten lernen',
                'Focus on identifying 5-10 common birds': 'Konzentrieren Sie sich darauf, 5-10 häufige Vögel',
                'in your area first': 'in Ihrer Gegend zuerst zu identifizieren',
                'Quality over quantity is key': 'Qualität vor Quantität ist der Schlüssel',
                'for beginners': 'für Anfänger',
                
                # 鸟类名称
                'American Robin': 'Amerikanische Wanderdrossel',
                'Northern Cardinal': 'Roter Kardinal',
                'Blue Jay': 'Blauhäher',
                'House Sparrow': 'Haussperling',
                'Mourning Dove': 'Carolinataube',
                'Red-winged Blackbird': 'Rotschulterstärling',
                
                # 描述
                'Orange breast, dark head': 'Orange Brust, dunkler Kopf',
                'Often seen hopping on lawns': 'Oft hüpfend auf Rasenflächen zu sehen',
                'Bright red male, brown female': 'Leuchtend roter Männchen, braunes Weibchen',
                'Clear whistled songs': 'Klare gepfiffene Gesänge',
                'Bright blue with white underparts': 'Leuchtend blau mit weißer Unterseite',
                'Intelligent behavior': 'Intelligentes Verhalten',
                'Small brown bird': 'Kleiner brauner Vogel',
                'Very common around homes': 'Sehr häufig um Häuser herum',
                'Soft gray-brown': 'Sanftes Graubraun',
                'Distinctive cooing call': 'Charakteristischer Gurrruf',
                'Black male with red shoulder patches': 'Schwarzes Männchen mit roten Schulterflecken',
                
                # 提示和建议
                'Benefits of Birdwatching': 'Vorteile der Vogelbeobachtung',
                'Connect with nature': 'Verbindung zur Natur',
                'reduce stress': 'Stress reduzieren',
                'get gentle exercise': 'sanfte Bewegung bekommen',
                'join a welcoming community': 'einer einladenden Gemeinschaft beitreten',
                'of fellow enthusiasts': 'von Gleichgesinnten',
                'Learning Tips for Beginners': 'Lerntipps für Anfänger',
                'Focus on size and shape first': 'Konzentrieren Sie sich zuerst auf Größe und Form',
                'notice behavior patterns': 'Verhaltensmuster bemerken',
                'listen to sounds': 'auf Geräusche hören',
                'use size comparisons': 'Größenvergleiche verwenden',
                'always take notes': 'immer Notizen machen',
                'of what you observe': 'von dem, was Sie beobachten',
                
                # 时间和地点
                'Best Times for Birding': 'Beste Zeiten für die Vogelbeobachtung',
                'Early morning': 'Früher Morgen',
                'first 2-3 hours after sunrise': 'erste 2-3 Stunden nach Sonnenaufgang',
                'late afternoon before sunset': 'später Nachmittag vor Sonnenuntergang',
                'overcast days': 'bewölkte Tage',
                'after storms': 'nach Stürmen',
                'when weather changes trigger': 'wenn Wetteränderungen auslösen',
                'increased bird activity': 'erhöhte Vogelaktivität'
            },
            
            'ja': {
                # 基础词汇
                'Bird Watching': 'バードウォッチング',
                'Birdwatching': 'バードウォッチング',
                'for Beginners': '初心者向け',
                'Getting Started': '始め方',
                'Essential Equipment': '必要な装備',
                'Identification Techniques': '識別技術',
                'Best Locations': '最適な場所',
                'Seasonal Guide': '季節ガイド',
                'Photography Tips': '撮影のコツ',
                'Behavior Observation': '行動観察',
                'Song Identification': '鳴き声識別',
                'Ethics Conservation': '倫理と保護',
                'Journal Keeping': '記録の取り方',
                
                # 内容翻译
                'Discover the joy of birdwatching': 'バードウォッチングの楽しさを発見しよう',
                'your gateway to nature\'s most fascinating creatures': '自然界で最も魅力的な生き物への入り口',
                'Bird watching is one of the most rewarding': 'バードウォッチングは最もやりがいのある',
                'and accessible hobbies in the world': 'そして親しみやすい趣味の一つです',
                'Whether you\'re drawn to the beauty of birds': '鳥の美しさに惹かれても',
                'fascinated by their behaviors': 'その行動に魅了されても',
                'or simply enjoy being outdoors': 'または単に屋外にいることを楽しんでも',
                'birding offers endless opportunities': 'バードウォッチングは無限の機会を提供します',
                'for discovery and wonder': '発見と驚きの',
                
                # 步骤和说明
                'Start in Your Backyard': '自分の庭から始める',
                'Begin by observing birds': '鳥の観察から始めましょう',
                'in your own yard or neighborhood': '自分の庭や近所で',
                'Spend 15-20 minutes each morning': '毎朝15-20分間',
                'watching and listening': '観察と聞き取りに費やしましょう',
                'Get Basic Equipment': '基本装備を揃える',
                'Invest in simple binoculars': 'シンプルな双眼鏡に投資し',
                'and download a bird identification app': '鳥類識別アプリをダウンロードしましょう',
                'Learn Common Species': '一般的な種を学ぶ',
                'Focus on identifying 5-10 common birds': 'まず地域の一般的な鳥5-10種の',
                'in your area first': '識別に集中しましょう',
                'Quality over quantity is key': '量より質が重要です',
                'for beginners': '初心者にとって',
                
                # 鸟类名称
                'American Robin': 'アメリカコマツグミ',
                'Northern Cardinal': 'ショウジョウコウカンチョウ',
                'Blue Jay': 'アオカケス',
                'House Sparrow': 'イエスズメ',
                'Mourning Dove': 'ナゲキバト',
                'Red-winged Blackbird': 'ハゴロモガラス',
                
                # 描述
                'Orange breast, dark head': 'オレンジ色の胸、暗い頭部',
                'Often seen hopping on lawns': '芝生でよく跳ねているのを見かけます',
                'Bright red male, brown female': '鮮やかな赤いオス、茶色のメス',
                'Clear whistled songs': '明瞭な口笛のような鳴き声',
                'Bright blue with white underparts': '鮮やかな青色で腹部は白',
                'Intelligent behavior': '知的な行動',
                'Small brown bird': '小さな茶色い鳥',
                'Very common around homes': '住宅周辺で非常に一般的',
                'Soft gray-brown': '柔らかい灰褐色',
                'Distinctive cooing call': '特徴的なクークー鳴き',
                'Black male with red shoulder patches': '赤い肩章のある黒いオス',
                
                # 提示和建议
                'Benefits of Birdwatching': 'バードウォッチングの利点',
                'Connect with nature': '自然とのつながり',
                'reduce stress': 'ストレス軽減',
                'get gentle exercise': '軽い運動',
                'join a welcoming community': '温かいコミュニティへの参加',
                'of fellow enthusiasts': '同好の士との',
                'Learning Tips for Beginners': '初心者向け学習のコツ',
                'Focus on size and shape first': 'まずサイズと形に注目',
                'notice behavior patterns': '行動パターンに注意',
                'listen to sounds': '音を聞く',
                'use size comparisons': 'サイズ比較を使用',
                'always take notes': '常にメモを取る',
                'of what you observe': '観察したことの',
                
                # 时间和地点
                'Best Times for Birding': 'バードウォッチングに最適な時間',
                'Early morning': '早朝',
                'first 2-3 hours after sunrise': '日の出後最初の2-3時間',
                'late afternoon before sunset': '日没前の夕方',
                'overcast days': '曇りの日',
                'after storms': '嵐の後',
                'when weather changes trigger': '天候の変化が引き起こす',
                'increased bird activity': '鳥の活動の活発化'
            }
        }
    
    def fix_language_tags(self, content, lang):
        """修复语言标签"""
        content = re.sub(r'<html lang="[^"]*">', f'<html lang="{lang}">', content)
        return content
    
    def fix_title(self, content, lang):
        """修复标题"""
        title_patterns = {
            'fr': {
                r'<title>[^<]*Bird Watching[^<]*</title>': '<title>Observation des Oiseaux pour Débutants - BirdAiSnap</title>',
                r'<title>[^<]*Birdwatching[^<]*</title>': '<title>Observation des Oiseaux pour Débutants - BirdAiSnap</title>'
            },
            'de': {
                r'<title>[^<]*Bird Watching[^<]*</title>': '<title>Vogelbeobachtung für Anfänger - BirdAiSnap</title>',
                r'<title>[^<]*Vogel Watching[^<]*</title>': '<title>Vogelbeobachtung für Anfänger - BirdAiSnap</title>'
            },
            'ja': {
                r'<title>[^<]*Bird W[^<]*</title>': '<title>初心者向けバードウォッチング - BirdAiSnap</title>',
                r'<title>[^<]*Bird Watching[^<]*</title>': '<title>初心者向けバードウォッチング - BirdAiSnap</title>'
            }
        }
        
        if lang in title_patterns:
            for pattern, replacement in title_patterns[lang].items():
                content = re.sub(pattern, replacement, content)
        
        return content
    
    def translate_content(self, content, lang):
        """翻译内容"""
        if lang not in self.translations:
            return content
        
        translations = self.translations[lang]
        
        # 按长度排序，先替换长的短语
        sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
        
        for english, translation in sorted_translations:
            # 使用正则表达式进行更精确的替换
            pattern = re.escape(english)
            content = re.sub(pattern, translation, content, flags=re.IGNORECASE)
        
        return content
    
    def fix_html_comments(self, content, lang):
        """修复HTML注释"""
        comment_translations = {
            'fr': {
                '<!-- 返回按钮 -->': '<!-- Bouton de retour -->',
                '<!-- 英雄图片 -->': '<!-- Image héroïque -->',
                '<!-- 主要内容 -->': '<!-- Contenu principal -->',
                '<!-- 进度条 -->': '<!-- Barre de progression -->'
            },
            'de': {
                '<!-- 返回按钮 -->': '<!-- Zurück-Button -->',
                '<!-- 英雄图片 -->': '<!-- Hero-Bild -->',
                '<!-- 主要内容 -->': '<!-- Hauptinhalt -->',
                '<!-- 进度条 -->': '<!-- Fortschrittsbalken -->'
            },
            'ja': {
                '<!-- 返回按钮 -->': '<!-- 戻るボタン -->',
                '<!-- 英雄图片 -->': '<!-- ヒーロー画像 -->',
                '<!-- 主要内容 -->': '<!-- メインコンテンツ -->',
                '<!-- 进度条 -->': '<!-- プログレスバー -->'
            }
        }
        
        if lang in comment_translations:
            for chinese, translation in comment_translations[lang].items():
                content = content.replace(chinese, translation)
        
        return content
    
    def fix_css_classes(self, content, lang):
        """修复CSS类名中的错误"""
        if lang == 'ja':
            # 修复日语中的CSS类名错误
            content = re.sub(r'クラス="([^"]*)"', r'class="\1"', content)
            content = re.sub(r'スタイル="([^"]*)"', r'style="\1"', content)
        elif lang == 'de':
            # 修复德语中的CSS类名错误
            content = re.sub(r'Farbe:', 'color:', content)
            content = re.sub(r'font-Größe:', 'font-size:', content)
            content = re.sub(r'margin-bottom:', 'margin-bottom:', content)
        
        return content
    
    def optimize_file(self, file_path, lang):
        """优化单个文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"优化 {file_path}")
            
            # 应用所有修复
            content = self.fix_language_tags(content, lang)
            content = self.fix_title(content, lang)
            content = self.translate_content(content, lang)
            content = self.fix_html_comments(content, lang)
            content = self.fix_css_classes(content, lang)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            print(f"优化 {file_path} 时出错: {e}")
            return False
    
    def optimize_language_directory(self, lang):
        """优化指定语言目录"""
        lang_dir = self.base_dir / lang
        if not lang_dir.exists():
            print(f"语言目录 {lang} 不存在")
            return
        
        print(f"\n🔧 开始优化 {lang.upper()} 翻译...")
        
        # 查找所有HTML文件
        html_files = list(lang_dir.rglob('*.html'))
        
        success_count = 0
        total_count = len(html_files)
        
        for html_file in html_files:
            if self.optimize_file(html_file, lang):
                success_count += 1
        
        print(f"✅ {lang.upper()} 优化完成: {success_count}/{total_count} 文件成功")
    
    def run(self):
        """运行优化"""
        print("🚀 开始高质量翻译优化...")
        
        languages = ['fr', 'de', 'ja']
        
        for lang in languages:
            self.optimize_language_directory(lang)
        
        print("\n🎉 所有语言翻译优化完成！")
        
        # 生成优化报告
        self.generate_report()
    
    def generate_report(self):
        """生成优化报告"""
        print("\n📊 优化报告:")
        print("=" * 50)
        
        languages = {
            'fr': '法语',
            'de': '德语', 
            'ja': '日语'
        }
        
        for lang_code, lang_name in languages.items():
            lang_dir = self.base_dir / lang_code
            if lang_dir.exists():
                html_files = list(lang_dir.rglob('*.html'))
                print(f"{lang_name} ({lang_code}): {len(html_files)} 个文件已优化")
        
        print("\n🔧 优化内容:")
        print("- ✅ 修复语言标签")
        print("- ✅ 优化页面标题")
        print("- ✅ 高质量内容翻译")
        print("- ✅ 修复HTML注释")
        print("- ✅ 修复CSS类名错误")
        print("- ✅ 统一术语翻译")

if __name__ == "__main__":
    optimizer = TranslationOptimizer()
    optimizer.run()