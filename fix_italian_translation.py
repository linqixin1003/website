#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复意大利语翻译文件
将it/目录下的英文和中文内容翻译成意大利语
"""

import os
import re
from pathlib import Path

# 英文到意大利语的翻译映射
TRANSLATIONS = {
    # 标题翻译
    "Bird Watching for Beginners": "Birdwatching per Principianti",
    "Choosing the Right Bird": "Scegliere l'Uccello Giusto",
    "观鸟入门指南": "Guida Introduttiva al Birdwatching",
    "Pet Care Guide": "Guida alla Cura degli Animali",
    "BirdAiSnap": "BirdAiSnap",
    
    # 常用短语翻译
    "Discover the joy of birdwatching": "Scopri la gioia del birdwatching",
    "your gateway to nature's most fascinating creatures": "la tua porta d'accesso alle creature più affascinanti della natura",
    "Find the perfect feathered companion": "Trova il compagno piumato perfetto",
    "that matches your lifestyle": "che si adatta al tuo stile di vita",
    "开启您的观鸟之旅，发现自然的奇妙世界": "Inizia il tuo viaggio nel birdwatching e scopri il mondo meraviglioso della natura",
    
    # 章节标题翻译
    "Why Start Bird Watching?": "Perché Iniziare il Birdwatching?",
    "Getting Started: Your First Steps": "Iniziare: I Tuoi Primi Passi",
    "Common Birds to Learn First": "Uccelli Comuni da Imparare Prima",
    "Basic Identification Techniques": "Tecniche di Identificazione di Base",
    "Where to Go Birding": "Dove Andare a Fare Birdwatching",
    "Building Your Skills": "Sviluppare le Tue Competenze",
    "Understanding Your Lifestyle": "Comprendere il Tuo Stile di Vita",
    "Popular Pet Bird Types": "Tipi Popolari di Uccelli Domestici",
    "Space and Housing Requirements": "Requisiti di Spazio e Alloggio",
    "Financial Considerations": "Considerazioni Finanziarie",
    "Pre-Adoption Checklist": "Lista di Controllo Pre-Adozione",
    "Where to Find Your Bird": "Dove Trovare il Tuo Uccello",
    "Making Your Final Decision": "Prendere la Tua Decisione Finale",
    
    # 中文章节标题翻译
    "为什么选择观鸟？": "Perché Scegliere il Birdwatching?",
    "入门必备知识": "Conoscenze Essenziali per Iniziare",
    "基础装备推荐": "Attrezzatura di Base Consigliata",
    "观鸟礼仪与安全": "Etichetta e Sicurezza nel Birdwatching",
    
    # 常用词汇翻译
    "Bird watching": "Birdwatching",
    "bird watching": "birdwatching",
    "Birdwatching": "Birdwatching",
    "birdwatching": "birdwatching",
    "birds": "uccelli",
    "bird": "uccello",
    "species": "specie",
    "habitat": "habitat",
    "behavior": "comportamento",
    "observation": "osservazione",
    "identification": "identificazione",
    "binoculars": "binocoli",
    "field guide": "guida da campo",
    "nature": "natura",
    "wildlife": "fauna selvatica",
    "beginner": "principiante",
    "beginners": "principianti",
    "tips": "consigli",
    "guide": "guida",
    "equipment": "attrezzatura",
    "essential": "essenziale",
    "techniques": "tecniche",
    "locations": "luoghi",
    "seasonal": "stagionale",
    "photography": "fotografia",
    "journal": "diario",
    "ethics": "etica",
    "conservation": "conservazione",
}

# 长文本翻译
LONG_TEXT_TRANSLATIONS = {
    "Bird watching is one of the most rewarding and accessible hobbies in the world.": 
    "Il birdwatching è uno degli hobby più gratificanti e accessibili al mondo.",
    
    "Whether you're drawn to the beauty of birds, fascinated by their behaviors, or simply enjoy being outdoors, birding offers endless opportunities for discovery and wonder.":
    "Che tu sia attratto dalla bellezza degli uccelli, affascinato dai loro comportamenti, o semplicemente ami stare all'aperto, il birdwatching offre infinite opportunità di scoperta e meraviglia.",
    
    "Before choosing a bird, it's crucial to honestly assess your lifestyle, living situation, and commitment level.":
    "Prima di scegliere un uccello, è fondamentale valutare onestamente il tuo stile di vita, la situazione abitativa e il livello di impegno.",
    
    "Birds are intelligent, social creatures that require daily interaction, proper care, and long-term dedication.":
    "Gli uccelli sono creature intelligenti e sociali che richiedono interazione quotidiana, cure adeguate e dedizione a lungo termine.",
    
    # 中文长文本翻译
    "观鸟是一项令人着迷的户外活动，它不仅能让您亲近大自然，还能培养耐心、专注力和对生态环境的深度理解。":
    "Il birdwatching è un'attività all'aperto affascinante che non solo ti permette di avvicinarti alla natura, ma sviluppa anche pazienza, concentrazione e una profonda comprensione dell'ambiente ecologico.",
    
    "无论您是完全的新手还是对自然有一定了解的爱好者，观鸟都能为您打开一扇通往自然世界的神奇大门。":
    "Che tu sia un completo principiante o un appassionato con una certa conoscenza della natura, il birdwatching può aprirti una porta magica verso il mondo naturale.",
}

def translate_text(text):
    """翻译文本内容"""
    # 首先处理长文本翻译
    for english, italian in LONG_TEXT_TRANSLATIONS.items():
        text = text.replace(english, italian)
    
    # 然后处理单词和短语翻译
    for english, italian in TRANSLATIONS.items():
        # 使用正则表达式进行更精确的替换
        text = re.sub(r'\b' + re.escape(english) + r'\b', italian, text, flags=re.IGNORECASE)
    
    return text

def fix_html_lang(content):
    """修复HTML语言标签"""
    # 将中文语言标签改为意大利语
    content = re.sub(r'<html lang="zh-CN">', '<html lang="it">', content)
    content = re.sub(r'<html lang="en">', '<html lang="it">', content)
    return content

def process_file(file_path):
    """处理单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复语言标签
        content = fix_html_lang(content)
        
        # 翻译内容
        content = translate_text(content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已处理: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 处理失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("🇮🇹 开始修复意大利语翻译...")
    
    it_dir = Path("it")
    if not it_dir.exists():
        print("❌ it/ 目录不存在")
        return
    
    # 查找所有HTML文件
    html_files = list(it_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 未找到HTML文件")
        return
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    
    success_count = 0
    for file_path in html_files:
        if process_file(file_path):
            success_count += 1
    
    print(f"\n🎉 完成! 成功处理 {success_count}/{len(html_files)} 个文件")

if __name__ == "__main__":
    main()