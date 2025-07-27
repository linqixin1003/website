import os
import re
import sys
from bs4 import BeautifulSoup

# 英文到法语的基本翻译映射 - 专注于摄影和鸟类观察相关术语
translations = {
    # 标题和常见短语
    "Bird Photography Tips": "Conseils de Photographie d'Oiseaux",
    "Capture the beauty and behavior of birds with these essential photography techniques": "Capturez la beauté et le comportement des oiseaux avec ces techniques de photographie essentielles",
    "Essential Camera Equipment": "Équipement Photo Essentiel",
    "Camera Settings for Birds": "Réglages de l'Appareil Photo pour les Oiseaux",
    "Understanding Bird Behavior": "Comprendre le Comportement des Oiseaux",
    "Understanding avian behavior": "Comprendre le Comportement des Oiseaux",
    "Composition Techniques": "Techniques de Composition",
    "Ethical Considerations": "Considérations Éthiques",
    "Post-Processing Tips": "Conseils de Post-Traitement",
    "Creative Tips": "Conseils Créatifs",
    "Key Settings": "Réglages Clés",
    "DSLR/Mirrorless": "Reflex/Sans Miroir",
    "Superzoom Camera": "Appareil Photo Superzoom",
    "Smartphone + Adapter": "Smartphone + Adaptateur",
    "Best image quality and lens options": "Meilleure qualité d'image et options d'objectifs",
    "Ideal for serious bird photographers who want maximum control and flexibility": "Idéal pour les photographes d'oiseaux sérieux qui veulent un contrôle et une flexibilité maximale",
    "Convenient all-in-one solution with impressive zoom ranges": "Solution tout-en-un pratique avec des plages de zoom impressionnantes",
    "Perfect for beginners and travel photography": "Parfait pour les débutants et la photographie de voyage",
    "Budget-friendly option using digiscoping techniques with binoculars or spotting scopes": "Option économique utilisant des techniques de digiscopie avec des jumelles ou des longues-vues",
    "Shutter Priority or Manual mode, continuous autofocus (AI Servo/AF-C), high ISO capability (1600-6400), and burst mode for action sequences": "Mode Priorité Vitesse ou Manuel, autofocus continu (AI Servo/AF-C), capacité ISO élevée (1600-6400) et mode rafale pour les séquences d'action",
    "Capture behavior and interaction, use shallow depth of field to isolate subjects, include environmental context, and shoot at the bird's eye level for more engaging images": "Capturez le comportement et l'interaction, utilisez une faible profondeur de champ pour isoler les sujets, incluez le contexte environnemental et photographiez au niveau des yeux de l'oiseau pour des images plus attrayantes",
    "Practice makes perfect in bird photography": "La pratique rend parfait en photographie d'oiseaux",
    "Start with common, approachable species in your backyard or local parks": "Commencez avec des espèces communes et accessibles dans votre jardin ou les parcs locaux",
    "As your skills develop, you can tackle more challenging subjects and situations": "À mesure que vos compétences se développent, vous pouvez aborder des sujets et des situations plus difficiles",
    "Remember that the best camera is the one you have with you": "N'oubliez pas que le meilleur appareil photo est celui que vous avez avec vous",
    
    # 常见词汇
    "bird": "oiseau",
    "birds": "oiseaux",
    "photography": "photographie",
    "camera": "appareil photo",
    "lens": "objectif",
    "telephoto": "téléobjectif",
    "shutter": "vitesse d'obturation",
    "aperture": "ouverture",
    "ISO": "ISO",
    "RAW": "RAW",
    "DSLR": "reflex",
    "Mirrorless": "sans miroir",
    "Superzoom": "superzoom",
    "Smartphone": "smartphone",
    "adapter": "adaptateur",
    "behavior": "comportement",
    "avian": "aviaire",
    "perched": "perché",
    "flight": "vol",
    "nest": "nid",
    "nesting": "nidification",
    "welfare": "bien-être",
    "image": "image",
    "photo": "photo",
    "composition": "composition",
    "technique": "technique",
    "settings": "réglages",
    "mode": "mode",
    "manual": "manuel",
    "priority": "priorité",
    "autofocus": "autofocus",
    "continuous": "continu",
    "burst": "rafale",
    "depth of field": "profondeur de champ",
    "rule of thirds": "règle des tiers",
    "eye level": "niveau des yeux",
    "editing": "édition",
    "processing": "traitement",
    "crop": "recadrer",
    "noise reduction": "réduction du bruit",
    "quality": "qualité",
    "flexibility": "flexibilité",
    "wildlife": "faune",
    "nature": "nature",
    "dynamic": "dynamique",
    "success": "succès",
    "requires": "nécessite",
    "understanding": "compréhension",
    "patience": "patience",
    "approach": "approche",
    "avoid": "éviter",
    "sudden": "soudain",
    "movements": "mouvements",
    "natural": "naturel",
    "cover": "couverture",
    "trees": "arbres",
    "blinds": "caches",
    "possible": "possible",
    "many": "nombreux",
    "predictable": "prévisible",
    "routines": "routines",
    "observe": "observer",
    "shooting": "prise de vue",
    "anticipate": "anticiper",
    "best": "meilleur",
    "moments": "moments",
    "apply": "appliquer",
    "placing": "placer",
    "along": "le long",
    "intersection": "intersection",
    "points": "points",
    "ensure": "assurer",
    "sharp": "net",
    "well-lit": "bien éclairé",
    "critical": "critique",
    "element": "élément",
    "portrait": "portrait",
    "leave": "laisser",
    "space": "espace",
    "direction": "direction",
    "looking": "regardant",
    "moving": "se déplaçant",
    "capture": "capturer",
    "interaction": "interaction",
    "use": "utiliser",
    "shallow": "peu profond",
    "isolate": "isoler",
    "subjects": "sujets",
    "include": "inclure",
    "environmental": "environnemental",
    "context": "contexte",
    "shoot": "photographier",
    "engaging": "attrayant",
    "images": "images",
    "always": "toujours",
    "prioritize": "prioriser",
    "over": "plutôt que",
    "getting": "obtenir",
    "shot": "prise de vue",
    "maintain": "maintenir",
    "appropriate": "approprié",
    "distances": "distances",
    "disturbing": "perturber",
    "nests": "nids",
    "roosting": "repos",
    "sites": "sites",
    "never": "jamais",
    "playback": "lecture",
    "near": "près",
    "respect": "respecter",
    "private": "privé",
    "property": "propriété",
    "protected": "protégé",
    "areas": "zones",
    "format": "format",
    "maximum": "maximum",
    "enhancing": "améliorer",
    "natural": "naturel",
    "colors": "couleurs",
    "details": "détails",
    "rather": "plutôt",
    "than": "que",
    "judiciously": "judicieusement",
    "improve": "améliorer",
    "software": "logiciel",
    "help": "aider",
    "high": "élevé",
    "practice": "pratique",
    "makes": "rend",
    "perfect": "parfait",
    "start": "commencer",
    "common": "commun",
    "approachable": "accessible",
    "species": "espèces",
    "backyard": "jardin",
    "local": "local",
    "parks": "parcs",
    "skills": "compétences",
    "develop": "développer",
    "tackle": "aborder",
    "challenging": "difficile",
    "subjects": "sujets",
    "situations": "situations",
    "remember": "rappelez-vous",
    "that": "que",
    "the": "le",
    "is": "est",
    "you": "vous",
    "have": "avez",
    "with": "avec",
    "your": "votre",
    "and": "et",
    "for": "pour",
    "in": "dans",
    "of": "de",
    "to": "à",
    "a": "un",
    "an": "un",
    "as": "comme",
    "at": "à",
    "by": "par",
    "can": "peut",
    "from": "de",
    "it": "il",
    "more": "plus",
    "most": "la plupart",
    "on": "sur",
    "or": "ou",
    "this": "ce",
    "while": "tandis que",
    "who": "qui",
    "will": "va",
    "when": "quand",
    "which": "qui",
    "what": "quoi",
    "where": "où",
    "why": "pourquoi",
    "how": "comment",
    "all": "tous",
    "any": "tout",
    "some": "certains",
    "such": "tel",
    "no": "non",
    "not": "pas",
    "only": "seulement",
    "very": "très",
    "also": "aussi",
    "but": "mais",
    "if": "si",
    "so": "donc",
    "about": "à propos",
    "after": "après",
    "before": "avant",
    "between": "entre",
    "during": "pendant",
    "under": "sous",
    "through": "à travers",
    "throughout": "tout au long",
    "within": "dans",
    "without": "sans"
}

def translate_text(text):
    """将英文文本翻译成法语"""
    # 先翻译完整的短语
    for phrase, translation in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        if phrase.lower() in text.lower():
            # 保持原始大小写
            if text.lower() == phrase.lower():
                return translation
            else:
                pattern = re.compile(re.escape(phrase), re.IGNORECASE)
                text = pattern.sub(translation, text)
    
    # 然后翻译单词
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if word.lower() in translations:
            pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
            text = pattern.sub(translations[word.lower()], text)
    
    return text

def translate_html_file(file_path):
    """翻译HTML文件中的英文内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 保存原始HTML内容
        original_content = content
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # 设置语言属性
        if soup.html.has_attr('lang'):
            soup.html['lang'] = 'fr'
        
        # 翻译标题
        if soup.title:
            soup.title.string = translate_text(soup.title.string)
        
        # 翻译所有文本节点，但排除script和style标签内的内容
        for element in soup.find_all(string=True):
            if element.parent.name not in ['script', 'style']:
                # 跳过纯数字、空白或特殊字符的文本
                if not re.match(r'^[\d\s\W]+$', element.strip()):
                    new_text = translate_text(element.string)
                    element.replace_with(new_text)
        
        # 将修改后的HTML转换回字符串
        translated_content = str(soup)
        
        # 保存翻译后的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"已翻译文件: {file_path}")
        return True
    except Exception as e:
        print(f"翻译文件 {file_path} 时出错: {e}")
        return False

def translate_all_files(directory, file_pattern="*.html"):
    """翻译指定目录下所有匹配的文件"""
    import glob
    
    # 获取所有匹配的文件
    files = glob.glob(os.path.join(directory, "**", file_pattern), recursive=True)
    
    # 翻译每个文件
    success_count = 0
    for file_path in files:
        print(f"正在翻译: {file_path}")
        if translate_html_file(file_path):
            success_count += 1
    
    print(f"成功翻译了 {success_count}/{len(files)} 个文件")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python final_french_translator.py <文件路径或目录>")
        return
    
    path = sys.argv[1]
    
    if os.path.isdir(path):
        # 如果是目录，翻译目录下所有HTML文件
        translate_all_files(path)
    elif os.path.isfile(path):
        # 如果是文件，只翻译该文件
        translate_html_file(path)
    else:
        print(f"路径 {path} 不存在")

if __name__ == "__main__":
    main()