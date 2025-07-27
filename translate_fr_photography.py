import os
import re
import sys

# 英文到法语的基本翻译映射 - 专注于摄影相关术语
translations = {
    # 标题和常见短语
    "Bird Photography Tips": "Conseils de Photographie d'Oiseaux",
    "Capture the beauty and behavior of birds with these essential photography techniques": "Capturez la beauté et le comportement des oiseaux avec ces techniques de photographie essentielles",
    "Essential Camera Equipment": "Équipement Photo Essentiel",
    "Camera Settings for Birds": "Réglages de l'Appareil Photo pour les Oiseaux",
    "Understanding avian behavior": "Comprendre le comportement des oiseaux",
    "Understanding Bird Behavior": "Comprendre le comportement des oiseaux",
    "Composition Techniques": "Techniques de Composition",
    "Ethical Considerations": "Considérations Éthiques",
    "Post-Processing Tips": "Conseils de Post-Traitement",
    "Creative Tips": "Conseils Créatifs",
    "Key Settings": "Réglages Clés",
    
    # 常见词汇
    "bird": "oiseau",
    "birds": "oiseaux",
    "photography": "photographie",
    "camera": "appareil photo",
    "lens": "objectif",
    "telephoto": "téléobjectif",
    "shutter": "obturateur",
    "aperture": "ouverture",
    "ISO": "ISO",
    "RAW": "RAW",
    "DSLR": "DSLR",
    "Mirrorless": "Sans Miroir",
    "Superzoom": "Superzoom",
    "Smartphone": "Smartphone",
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
        text = text.replace(phrase, translation)
    
    # 然后翻译单词
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if word.lower() in translations:
            text = re.sub(r'\b' + word + r'\b', translations[word.lower()], text)
    
    return text

def translate_html_file(file_path):
    """翻译HTML文件中的英文内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取HTML标签之间的文本内容
    pattern = r'>([^<>]+)<'
    matches = re.findall(pattern, content)
    
    # 翻译每个匹配的文本
    for match in matches:
        # 跳过纯数字、空白或特殊字符的文本
        if re.match(r'^[\d\s\W]+$', match):
            continue
        
        # 翻译文本
        translated = translate_text(match)
        
        # 替换原文本
        content = content.replace('>' + match + '<', '>' + translated + '<')
    
    # 翻译标题
    title_pattern = r'<title>([^<>]+)</title>'
    title_match = re.search(title_pattern, content)
    if title_match:
        title = title_match.group(1)
        translated_title = translate_text(title)
        content = content.replace('<title>' + title + '</title>', '<title>' + translated_title + '</title>')
    
    # 保存翻译后的文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已翻译文件: {file_path}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python translate_fr_photography.py <文件路径>")
        return
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在")
        return
    
    translate_html_file(file_path)

if __name__ == "__main__":
    main()