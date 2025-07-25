#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def fix_german_translation():
    """修复德语翻译"""
    
    # 核心翻译映射
    translations = {
        # 页面标题
        "Birdwatching Beginner's Guide": "Vogelbeobachtung Anfängerhandbuch",
        "Essential Equipment": "Wesentliche Ausrüstung", 
        "Identification Techniques": "Identifikationstechniken",
        "Best Locations": "Beste Standorte",
        "Seasonal Guide": "Saisonaler Leitfaden",
        "Photography Tips": "Fotografie-Tipps",
        "Behavior Observation": "Verhaltensbeobachtung",
        "Song Identification": "Gesangsidentifikation",
        "Ethics and Conservation": "Ethik und Naturschutz",
        "Journal Keeping": "Tagebuchführung",
        
        # 宠物护理
        "Choosing the Right Bird": "Den richtigen Vogel wählen",
        "Nutrition and Feeding": "Ernährung und Fütterung",
        "Housing and Environment": "Unterbringung und Umgebung",
        "Health and Veterinary": "Gesundheit und Tierarzt",
        "Training and Behavior": "Training und Verhalten",
        "Breeding and Reproduction": "Zucht und Fortpflanzung",
        "Emergency First Aid": "Notfall-Erste Hilfe",
        "Seasonal Care": "Saisonale Pflege",
        "Enrichment Activities": "Bereicherungsaktivitäten",
        "Senior Bird Care": "Altenvogelpflege",
        "Species Profiles": "Artenprofile",
        
        # 科学奇迹
        "Bird Flight Mechanics": "Vogelflug-Mechanik",
        "Magnetic Navigation": "Magnetische Navigation", 
        "Hummingbird Mechanics": "Kolibri-Mechanik",
        "Bird Intelligence": "Vogelintelligenz",
        "Feather Structure": "Federstruktur",
        "Bird Vision": "Vogelsicht",
        "Egg Development": "Eientwicklung",
        "Bird Communication": "Vogelkommunikation",
        "Migration Physiology": "Migrationsphysiologie",
        "Biomechanics": "Biomechanik",
        
        # 生态学
        "Habitat Ecosystems": "Lebensraum-Ökosysteme",
        "Food Webs Chains": "Nahrungsnetze und -ketten",
        "Migration Patterns": "Migrationsmuster", 
        "Breeding Ecology": "Brutökologie",
        "Climate Change Impact": "Klimawandel-Auswirkungen",
        "Urban Ecology": "Stadtökologie",
        "Conservation Biology": "Naturschutzbiologie",
        "Island Biogeography": "Insel-Biogeographie",
        "Pollination Seed Dispersal": "Bestäubung und Samenverbreitung",
        "Community Dynamics": "Gemeinschaftsdynamik",
        
        # 引言和描述
        "Begin your birdwatching journey and discover the wonders of nature": "Beginnen Sie Ihre Vogelbeobachtungsreise und entdecken Sie die Wunder der Natur",
        "Find the perfect feathered companion that matches your lifestyle": "Finden Sie den perfekten gefiederten Begleiter, der zu Ihrem Lebensstil passt",
        
        # 章节标题
        "Why Choose Birdwatching?": "Warum Vogelbeobachtung wählen?",
        "Essential Knowledge for Beginners": "Wesentliches Wissen für Anfänger",
        "Recommended Basic Equipment": "Empfohlene Grundausstattung",
        "Birdwatching Etiquette and Safety": "Vogelbeobachtung Etikette und Sicherheit",
        
        # 提示框
        "Beginner's Tip": "Anfänger-Tipp",
        "Expert Advice": "Expertenrat",
        
        # 常用词汇
        "birdwatching": "Vogelbeobachtung",
        "bird": "Vogel",
        "birds": "Vögel", 
        "nature": "Natur",
        "wildlife": "Tierwelt",
        "habitat": "Lebensraum",
        "species": "Art",
        "observation": "Beobachtung",
        "identification": "Identifikation",
        "behavior": "Verhalten",
        "behaviour": "Verhalten",
        "migration": "Migration",
        "breeding": "Zucht",
        "feeding": "Fütterung",
        "conservation": "Naturschutz",
        "ecology": "Ökologie",
        "ecosystem": "Ökosystem",
        "environment": "Umgebung",
        "equipment": "Ausrüstung",
        "binoculars": "Fernglas",
        "guide": "Leitfaden",
        "photography": "Fotografie",
        "camera": "Kamera",
        "notebook": "Notizbuch",
        "journal": "Tagebuch",
        "location": "Standort",
        "season": "Jahreszeit",
        "weather": "Wetter",
        "temperature": "Temperatur",
        "morning": "Morgen",
        "evening": "Abend",
        "forest": "Wald",
        "park": "Park",
        "garden": "Garten",
        "urban": "städtisch",
        "rural": "ländlich",
        "wild": "wild",
        "domestic": "häuslich",
        "pet": "Haustier",
        "care": "Pflege",
        "health": "Gesundheit",
        "nutrition": "Ernährung",
        "food": "Nahrung",
        "water": "Wasser",
        "training": "Training",
        "intelligence": "Intelligenz",
        "communication": "Kommunikation",
        "flight": "Flug",
        "feather": "Feder",
        "wing": "Flügel",
        "beak": "Schnabel",
        "eye": "Auge",
        "important": "wichtig",
        "essential": "wesentlich",
        "basic": "grundlegend",
        "common": "häufig",
        "different": "unterschiedlich",
        "special": "besonders",
        "natural": "natürlich",
        "beautiful": "schön",
        "interesting": "interessant",
        "easy": "einfach",
        "difficult": "schwierig",
        "good": "gut",
        "best": "beste",
        "learn": "lernen",
        "understand": "verstehen",
        "observe": "beobachten",
        "find": "finden",
        "discover": "entdecken",
        "start": "beginnen",
        "begin": "anfangen",
        "help": "helfen",
        "choose": "wählen",
        "need": "brauchen",
        "want": "wollen",
        "see": "sehen",
        "watch": "beobachten",
        "listen": "hören",
        "and": "und",
        "or": "oder",
        "the": "der",
        "with": "mit",
        "for": "für",
        "to": "zu",
        "of": "von",
        "in": "in",
        "on": "auf",
        "at": "bei"
    }
    
    def translate_text(text):
        """翻译文本"""
        if not text.strip():
            return text
        
        # 按长度排序，优先匹配长短语
        sorted_keys = sorted(translations.keys(), key=len, reverse=True)
        
        for english in sorted_keys:
            # 使用单词边界匹配，避免部分替换
            pattern = r'\b' + re.escape(english) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                text = re.sub(pattern, translations[english], text, flags=re.IGNORECASE)
        
        return text
    
    def fix_file(file_path):
        """修复单个文件"""
        print(f"正在修复: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修复lang属性
            content = re.sub(r'lang="en"', 'lang="de"', content)
            
            # 翻译title标签
            def translate_title(match):
                title_content = match.group(1)
                translated = translate_text(title_content)
                return f'<title>{translated}</title>'
            
            content = re.sub(r'<title>(.*?)</title>', translate_title, content, flags=re.DOTALL)
            
            # 翻译HTML标签内的文本
            def translate_html_text(match):
                tag_start = match.group(1)
                text_content = match.group(2)
                tag_end = match.group(3)
                
                if text_content.strip():
                    translated_text = translate_text(text_content)
                    return tag_start + translated_text + tag_end
                
                return match.group(0)
            
            # 处理各种HTML标签
            html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'a', 'li', 'td', 'th', 'cite', 'button']
            
            for tag in html_tags:
                pattern = f'(<{tag}[^>]*>)(.*?)(</{tag}>)'
                content = re.sub(pattern, translate_html_text, content, flags=re.DOTALL)
            
            # 翻译注释
            def translate_comment(match):
                comment_text = match.group(1)
                translated = translate_text(comment_text)
                return f'<!-- {translated} -->'
            
            content = re.sub(r'<!--\s*(.*?)\s*-->', translate_comment, content, flags=re.DOTALL)
            
            # 写入文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ 修复完成: {file_path}")
            
        except Exception as e:
            print(f"❌ 错误: {file_path}: {str(e)}")
    
    # 主函数
    de_dir = Path("de")
    
    if not de_dir.exists():
        print("❌ de目录不存在")
        return
    
    html_files = list(de_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 未找到HTML文件")
        return
    
    print(f"找到 {len(html_files)} 个德语HTML文件需要修复")
    print("开始修复德语翻译...")
    
    for html_file in html_files:
        fix_file(html_file)
    
    print(f"\n🎉 德语翻译修复完成！共处理了 {len(html_files)} 个文件")

if __name__ == "__main__":
    fix_german_translation()