#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def improved_german_fix():
    """改进的德语翻译修复"""
    
    # 完整句子翻译（优先级最高）
    sentence_translations = {
        "Birdwatching is a fascinating outdoor activity that not only brings you closer to nature but also cultivates patience, focus, and a deep understanding of ecological environments": "Vogelbeobachtung ist eine faszinierende Outdoor-Aktivität, die Sie nicht nur der Natur näher bringt, sondern auch Geduld, Konzentration und ein tiefes Verständnis für ökologische Umgebungen kultiviert",
        
        "Whether you're a complete beginner or a nature enthusiast with some experience, birdwatching can open a magical door to the natural world": "Ob Sie ein kompletter Anfänger oder ein Naturliebhaber mit etwas Erfahrung sind, kann die Vogelbeobachtung eine magische Tür zur natürlichen Welt öffnen",
        
        "Birdwatching has unique charm and multiple benefits": "Vogelbeobachtung hat einzigartigen Charme und vielfältige Vorteile",
        
        "First, it's a low-cost, high-reward leisure activity that requires only basic equipment to get started": "Erstens ist es eine kostengünstige, lohnende Freizeitaktivität, die nur eine Grundausstattung erfordert, um zu beginnen",
        
        "Second, birdwatching effectively relieves the stress of modern life, allowing you to relax in the peaceful natural environment": "Zweitens lindert die Vogelbeobachtung effektiv den Stress des modernen Lebens und ermöglicht es Ihnen, sich in der friedlichen natürlichen Umgebung zu entspannen",
        
        "More importantly, birdwatching cultivates your observational skills and ecological awareness": "Noch wichtiger ist, dass die Vogelbeobachtung Ihre Beobachtungsfähigkeiten und Ihr ökologisches Bewusstsein schult",
        
        "By observing the behaviors, habitats, and seasonal changes of different bird species, you'll gradually understand the complexity and fragility of ecosystems": "Durch die Beobachtung der Verhaltensweisen, Lebensräume und saisonalen Veränderungen verschiedener Vogelarten werden Sie allmählich die Komplexität und Fragilität von Ökosystemen verstehen",
        
        "This deep natural experience often inspires enthusiasm and responsibility for environmental protection": "Diese tiefe Naturerfahrung weckt oft Begeisterung und Verantwortung für den Umweltschutz",
        
        "Before starting birdwatching, understanding some basic knowledge will greatly enhance your experience": "Bevor Sie mit der Vogelbeobachtung beginnen, wird das Verständnis einiger Grundkenntnisse Ihre Erfahrung erheblich verbessern",
        
        "First, learn to identify the basic characteristics of birds: body size, color patterns, beak shape, leg length and color, etc": "Lernen Sie zunächst, die grundlegenden Merkmale von Vögeln zu identifizieren: Körpergröße, Farbmuster, Schnabelform, Beinlänge und -farbe usw",
        
        "These features are important criteria for distinguishing different bird species": "Diese Merkmale sind wichtige Kriterien zur Unterscheidung verschiedener Vogelarten",
        
        "It's recommended to start by observing common birds, such as sparrows, pigeons, and crows. These birds are easy to observe and help build confidence and experience": "Es wird empfohlen, mit der Beobachtung häufiger Vögel wie Spatzen, Tauben und Krähen zu beginnen. Diese Vögel sind leicht zu beobachten und helfen beim Aufbau von Vertrauen und Erfahrung",
        
        "Understanding birds' living habits is equally important": "Das Verständnis der Lebensgewohnheiten von Vögeln ist ebenso wichtig",
        
        "Different birds have different activity times, feeding habits, and habitat preferences": "Verschiedene Vögel haben unterschiedliche Aktivitätszeiten, Fressgewohnheiten und Lebensraumpräferenzen",
        
        "For example, most birds are most active during early morning and dusk, which are also the best times for birdwatching": "Zum Beispiel sind die meisten Vögel am frühen Morgen und in der Dämmerung am aktivsten, was auch die besten Zeiten für die Vogelbeobachtung sind",
        
        "Learning to identify bird calls is also an essential component of birdwatching skills": "Das Erlernen der Identifizierung von Vogelrufen ist ebenfalls ein wesentlicher Bestandteil der Vogelbeobachtungsfähigkeiten",
        
        "Although the barrier to entry for birdwatching is low, suitable equipment can significantly enhance your experience": "Obwohl die Einstiegshürde für die Vogelbeobachtung niedrig ist, kann geeignete Ausrüstung Ihre Erfahrung erheblich verbessern",
        
        "Binoculars are the most important tool, and it's recommended to choose 8x42 or 10x42 specifications": "Ein Fernglas ist das wichtigste Werkzeug, und es wird empfohlen, 8x42- oder 10x42-Spezifikationen zu wählen",
        
        "These specifications strike a good balance between magnification and field of view": "Diese Spezifikationen bieten ein gutes Gleichgewicht zwischen Vergrößerung und Sichtfeld",
        
        "Field guide books or mobile applications are also essential tools": "Feldführer oder mobile Anwendungen sind ebenfalls unverzichtbare Werkzeuge",
        
        "They can help you quickly identify observed birds and learn about their basic information and distribution": "Sie können Ihnen helfen, beobachtete Vögel schnell zu identifizieren und etwas über ihre grundlegenden Informationen und Verbreitung zu erfahren",
        
        "Additionally, prepare a birdwatching journal to record your observations, which not only aids learning but can also become precious personal memories": "Bereiten Sie außerdem ein Vogelbeobachtungstagebuch vor, um Ihre Beobachtungen aufzuzeichnen, was nicht nur beim Lernen hilft, sondern auch zu wertvollen persönlichen Erinnerungen werden kann",
        
        "Responsible birdwatching behavior is crucial for protecting birds and their habitats": "Verantwortungsvolles Vogelbeobachtungsverhalten ist entscheidend für den Schutz von Vögeln und ihren Lebensräumen",
        
        "Always maintain an appropriate observation distance and avoid disturbing birds' normal activities": "Halten Sie immer einen angemessenen Beobachtungsabstand ein und vermeiden Sie es, die normalen Aktivitäten der Vögel zu stören",
        
        "Be especially careful during breeding seasons; don't approach nests or interfere with parent birds' nurturing behaviors": "Seien Sie besonders vorsichtig während der Brutzeit; nähern Sie sich nicht den Nestern und stören Sie nicht das Brutverhalten der Elternvögel",
        
        "Personal safety is equally important when birdwatching in the wild": "Die persönliche Sicherheit ist beim Vogelbeobachten in der Wildnis ebenso wichtig",
        
        "Inform others of your itinerary, carry necessary safety equipment, and pay attention to weather changes": "Informieren Sie andere über Ihre Reiseroute, führen Sie notwendige Sicherheitsausrüstung mit sich und achten Sie auf Wetterveränderungen",
        
        "Follow local laws, regulations, and protected area rules to be a responsible nature observer": "Befolgen Sie örtliche Gesetze, Vorschriften und Schutzgebietsregeln, um ein verantwortungsvoller Naturbeobachter zu sein",
        
        "Joining local birdwatching organizations or participating in birdwatching activities to learn from experienced birdwatchers is the best way to quickly improve your birdwatching skills": "Der Beitritt zu örtlichen Vogelbeobachtungsorganisationen oder die Teilnahme an Vogelbeobachtungsaktivitäten, um von erfahrenen Vogelbeobachtern zu lernen, ist der beste Weg, um Ihre Vogelbeobachtungsfähigkeiten schnell zu verbessern",
        
        "Birdwatching is a lifelong learning and exploration activity": "Vogelbeobachtung ist eine lebenslange Lern- und Erkundungsaktivität",
        
        "As you gain experience, you'll find that each birdwatching outing brings new discoveries and surprises": "Mit zunehmender Erfahrung werden Sie feststellen, dass jeder Vogelbeobachtungsausflug neue Entdeckungen und Überraschungen bringt",
        
        "From simple species identification to in-depth behavioral observation, from local birds to migratory species, the world of birdwatching is full of endless possibilities and enjoyment": "Von der einfachen Artbestimmung bis zur tiefgreifenden Verhaltensbeobachtung, von einheimischen Vögeln bis zu Zugvögeln - die Welt der Vogelbeobachtung ist voller endloser Möglichkeiten und Freude"
    }
    
    # 常用词汇翻译
    word_translations = {
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
        "at": "bei",
        "by": "durch",
        "from": "von",
        "about": "über",
        "during": "während",
        "before": "vor",
        "after": "nach",
        "when": "wann",
        "where": "wo",
        "how": "wie",
        "what": "was",
        "why": "warum",
        "this": "dies",
        "that": "das",
        "these": "diese",
        "those": "jene",
        "all": "alle",
        "some": "einige",
        "many": "viele",
        "most": "meiste",
        "each": "jeder",
        "every": "jeder",
        "first": "erste",
        "second": "zweite",
        "last": "letzte",
        "next": "nächste",
        "new": "neu",
        "old": "alt",
        "small": "klein",
        "large": "groß",
        "long": "lang",
        "short": "kurz",
        "high": "hoch",
        "low": "niedrig",
        "safe": "sicher",
        "local": "örtlich",
        "popular": "beliebt",
        "experienced": "erfahren",
        "perfect": "perfekt",
        "complete": "vollständig",
        "unique": "einzigartig",
        "amazing": "erstaunlich",
        "wonderful": "wunderbar"
    }
    
    def translate_text(text):
        """翻译文本"""
        if not text.strip():
            return text
        
        # 首先尝试完整句子翻译
        for english_sentence, german_sentence in sentence_translations.items():
            if english_sentence.lower() in text.lower():
                text = text.replace(english_sentence, german_sentence)
        
        # 然后进行词汇翻译
        for english_word, german_word in word_translations.items():
            # 使用单词边界匹配
            pattern = r'\b' + re.escape(english_word) + r'\b'
            text = re.sub(pattern, german_word, text, flags=re.IGNORECASE)
        
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
    print("开始改进德语翻译...")
    
    for html_file in html_files:
        fix_file(html_file)
    
    print(f"\n🎉 德语翻译改进完成！共处理了 {len(html_files)} 个文件")

if __name__ == "__main__":
    improved_german_fix()