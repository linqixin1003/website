#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def simple_translate_to_portuguese():
    """简单有效的葡萄牙语翻译"""
    
    # 核心翻译映射 - 只包含最重要的翻译
    translations = {
        # 完整句子优先
        "Birdwatching Beginner's Guide": "Guia do Iniciante em Observação de Aves",
        "Begin your birdwatching journey and discover the wonders of nature": "Inicie sua jornada de observação de aves e descubra as maravilhas da natureza",
        "Find the perfect feathered companion that matches your lifestyle": "Encontre o companheiro emplumado perfeito que combine com seu estilo de vida",
        
        # 页面标题
        "Essential Equipment": "Equipamentos Essenciais",
        "Identification Techniques": "Técnicas de Identificação",
        "Best Locations": "Melhores Locais", 
        "Seasonal Guide": "Guia Sazonal",
        "Photography Tips": "Dicas de Fotografia",
        "Behavior Observation": "Observação de Comportamento",
        "Song Identification": "Identificação de Cantos",
        "Ethics and Conservation": "Ética e Conservação",
        "Journal Keeping": "Manutenção de Diário",
        "Choosing the Right Bird": "Escolhendo a Ave Certa",
        "Nutrition and Feeding": "Nutrição e Alimentação",
        "Housing and Environment": "Habitação e Ambiente",
        "Health and Veterinary": "Saúde e Veterinária",
        "Training and Behavior": "Treinamento e Comportamento",
        "Breeding and Reproduction": "Reprodução e Criação",
        "Emergency First Aid": "Primeiros Socorros de Emergência",
        "Seasonal Care": "Cuidados Sazonais",
        "Enrichment Activities": "Atividades de Enriquecimento",
        "Senior Bird Care": "Cuidados com Aves Idosas",
        "Species Profiles": "Perfis de Espécies",
        "Bird Flight Mechanics": "Mecânica do Voo das Aves",
        "Magnetic Navigation": "Navegação Magnética",
        "Hummingbird Mechanics": "Mecânica dos Beija-flores",
        "Bird Intelligence": "Inteligência das Aves",
        "Feather Structure": "Estrutura das Penas",
        "Bird Vision": "Visão das Aves",
        "Egg Development": "Desenvolvimento do Ovo",
        "Bird Communication": "Comunicação das Aves",
        "Migration Physiology": "Fisiologia da Migração",
        "Biomechanics": "Biomecânica",
        "Habitat Ecosystems": "Ecossistemas de Habitat",
        "Food Webs Chains": "Cadeias Alimentares",
        "Migration Patterns": "Padrões de Migração",
        "Breeding Ecology": "Ecologia Reprodutiva",
        "Climate Change Impact": "Impacto das Mudanças Climáticas",
        "Urban Ecology": "Ecologia Urbana",
        "Conservation Biology": "Biologia da Conservação",
        "Island Biogeography": "Biogeografia de Ilhas",
        "Pollination Seed Dispersal": "Polinização e Dispersão de Sementes",
        "Community Dynamics": "Dinâmica Comunitária",
        
        # 常用短语
        "Why Choose Birdwatching?": "Por que Escolher a Observação de Aves?",
        "Essential Knowledge for Beginners": "Conhecimento Essencial para Iniciantes",
        "Recommended Basic Equipment": "Equipamentos Básicos Recomendados",
        "Birdwatching Etiquette and Safety": "Etiqueta e Segurança na Observação de Aves",
        "Beginner's Tip": "Dica para Iniciantes",
        "Expert Advice": "Conselho de Especialista",
        "Back Button": "Botão Voltar",
        "Hero Image": "Imagem Principal",
        "Main Content": "Conteúdo Principal",
        "Progress Bar": "Barra de Progresso",
        
        # 基本词汇
        "birdwatching": "observação de aves",
        "bird": "ave",
        "birds": "aves",
        "nature": "natureza",
        "wildlife": "vida selvagem",
        "habitat": "habitat",
        "species": "espécie",
        "observation": "observação",
        "identification": "identificação",
        "behavior": "comportamento",
        "migration": "migração",
        "breeding": "reprodução",
        "feeding": "alimentação",
        "conservation": "conservação",
        "ecology": "ecologia",
        "ecosystem": "ecossistema",
        "environment": "ambiente",
        "equipment": "equipamento",
        "binoculars": "binóculos",
        "guide": "guia",
        "photography": "fotografia",
        "camera": "câmera",
        "notebook": "caderno",
        "journal": "diário",
        "location": "localização",
        "season": "estação",
        "weather": "clima",
        "temperature": "temperatura",
        "morning": "manhã",
        "evening": "noite",
        "forest": "floresta",
        "park": "parque",
        "garden": "jardim",
        "urban": "urbano",
        "rural": "rural",
        "wild": "selvagem",
        "domestic": "doméstico",
        "pet": "animal de estimação",
        "care": "cuidado",
        "health": "saúde",
        "nutrition": "nutrição",
        "food": "comida",
        "water": "água",
        "training": "treinamento",
        "intelligence": "inteligência",
        "communication": "comunicação",
        "flight": "voo",
        "feather": "pena",
        "wing": "asa",
        "beak": "bico",
        "eye": "olho",
        "size": "tamanho",
        "color": "cor",
        "male": "macho",
        "female": "fêmea",
        "adult": "adulto",
        "egg": "ovo",
        "nest": "ninho",
        
        # 常用词
        "and": "e",
        "or": "ou",
        "the": "o",
        "with": "com",
        "for": "para",
        "to": "para",
        "of": "de",
        "in": "em",
        "on": "em",
        "at": "em",
        "by": "por",
        "from": "de",
        "about": "sobre",
        "during": "durante",
        "before": "antes",
        "after": "depois",
        "when": "quando",
        "where": "onde",
        "how": "como",
        "what": "o que",
        "why": "por que",
        "this": "este",
        "that": "que",
        "these": "estes",
        "those": "aqueles",
        "all": "todos",
        "some": "alguns",
        "many": "muitos",
        "most": "maioria",
        "each": "cada",
        "every": "todo",
        "first": "primeiro",
        "last": "último",
        "next": "próximo",
        "new": "novo",
        "old": "velho",
        "small": "pequeno",
        "large": "grande",
        "long": "longo",
        "short": "curto",
        "high": "alto",
        "low": "baixo",
        "good": "bom",
        "best": "melhor",
        "important": "importante",
        "essential": "essencial",
        "basic": "básico",
        "common": "comum",
        "different": "diferente",
        "special": "especial",
        "natural": "natural",
        "beautiful": "bonito",
        "interesting": "interessante",
        "easy": "fácil",
        "difficult": "difícil",
        "safe": "seguro",
        "local": "local",
        "popular": "popular",
        "experienced": "experiente",
        "perfect": "perfeito",
        "complete": "completo",
        "unique": "único",
        "amazing": "incrível",
        "wonderful": "maravilhoso",
        
        # 动词
        "learn": "aprender",
        "understand": "entender",
        "observe": "observar",
        "find": "encontrar",
        "discover": "descobrir",
        "start": "começar",
        "begin": "começar",
        "help": "ajudar",
        "choose": "escolher",
        "need": "precisar",
        "want": "querer",
        "like": "gostar",
        "see": "ver",
        "watch": "assistir",
        "listen": "escutar",
        "build": "construir",
        "create": "criar",
        "provide": "fornecer",
        "protect": "proteger",
        "improve": "melhorar",
        "develop": "desenvolver",
        
        # 时间词汇
        "time": "tempo",
        "day": "dia",
        "night": "noite",
        "week": "semana",
        "month": "mês",
        "year": "ano",
        "hour": "hora",
        "minute": "minuto",
        "moment": "momento",
        "life": "vida",
        "world": "mundo",
        "place": "lugar",
        "home": "casa",
        "house": "casa",
        "family": "família",
        "people": "pessoas",
        "person": "pessoa",
        "man": "homem",
        "woman": "mulher",
        "child": "criança",
        "friend": "amigo"
    }
    
    def translate_text(text):
        """翻译文本"""
        if not text.strip():
            return text
        
        # 按长度排序，优先匹配长短语
        sorted_keys = sorted(translations.keys(), key=len, reverse=True)
        
        for english in sorted_keys:
            # 使用单词边界匹配
            pattern = r'\b' + re.escape(english) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                text = re.sub(pattern, translations[english], text, flags=re.IGNORECASE)
        
        return text
    
    def translate_file(src_file, dest_file):
        """翻译单个文件"""
        print(f"正在处理: {src_file} -> {dest_file}")
        
        try:
            with open(src_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 更新lang属性
            content = re.sub(r'lang="en"', 'lang="pt"', content)
            
            # 处理title标签
            def translate_title(match):
                title_content = match.group(1)
                translated = translate_text(title_content)
                return f'<title>{translated}</title>'
            
            content = re.sub(r'<title>(.*?)</title>', translate_title, content, flags=re.DOTALL)
            
            # 处理HTML标签内的文本
            def translate_html_text(match):
                tag_start = match.group(1)
                text_content = match.group(2)
                tag_end = match.group(3)
                
                if text_content.strip():
                    translated_text = translate_text(text_content)
                    return tag_start + translated_text + tag_end
                
                return match.group(0)
            
            # 匹配各种HTML标签
            html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'a', 'li', 'td', 'th', 'cite', 'button']
            
            for tag in html_tags:
                pattern = f'(<{tag}[^>]*>)(.*?)(</{tag}>)'
                content = re.sub(pattern, translate_html_text, content, flags=re.DOTALL)
            
            # 处理注释
            def translate_comment(match):
                comment_text = match.group(1)
                translated = translate_text(comment_text)
                return f'<!-- {translated} -->'
            
            content = re.sub(r'<!--\s*(.*?)\s*-->', translate_comment, content, flags=re.DOTALL)
            
            # 确保目标目录存在
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入文件
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ 完成: {dest_file}")
            
        except Exception as e:
            print(f"❌ 错误: {src_file}: {str(e)}")
    
    # 主函数
    en_dir = Path("en")
    pt_dir = Path("pt")
    
    if not en_dir.exists():
        print("❌ en目录不存在")
        return
    
    html_files = list(en_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 未找到HTML文件")
        return
    
    print(f"找到 {len(html_files)} 个英文HTML文件")
    print("开始最终翻译...")
    
    for html_file in html_files:
        relative_path = html_file.relative_to(en_dir)
        dest_file = pt_dir / relative_path
        translate_file(html_file, dest_file)
    
    print(f"\n🎉 翻译完成！共处理了 {len(html_files)} 个文件")

if __name__ == "__main__":
    simple_translate_to_portuguese()