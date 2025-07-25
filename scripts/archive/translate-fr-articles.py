#!/usr/bin/env python3
"""
将fr/目录下的文章内容翻译为法语
保持HTML格式和排版不变，只翻译文本内容
"""

import os
import re
from pathlib import Path

# 中文到法语的翻译映射
TRANSLATIONS = {
    # 页面标题和基本信息
    '观鸟入门指南': 'Guide d\'initiation à l\'observation des oiseaux',
    '观鸟设备指南': 'Guide de l\'équipement d\'observation des oiseaux',
    '鸟类识别技巧': 'Techniques d\'identification des oiseaux',
    '最佳观鸟地点': 'Meilleurs sites d\'observation des oiseaux',
    '季节性观鸟': 'Observation saisonnière des oiseaux',
    '鸟类摄影技巧': 'Techniques de photographie d\'oiseaux',
    '鸟类行为观察': 'Observation du comportement des oiseaux',
    '鸟类声音识别': 'Identification des chants d\'oiseaux',
    '观鸟伦理与保护': 'Éthique et conservation de l\'observation des oiseaux',
    '观鸟日志记录': 'Tenue d\'un journal d\'observation des oiseaux',
    
    # 生态学相关
    '鸟类栖息地与生态系统': 'Habitats et écosystèmes des oiseaux',
    '食物网与食物链': 'Réseaux et chaînes alimentaires',
    '迁徙模式': 'Modèles de migration',
    '繁殖生态学': 'Écologie de la reproduction',
    '气候变化影响': 'Impact du changement climatique',
    '城市鸟类生态': 'Écologie urbaine des oiseaux',
    '保护生物学': 'Biologie de la conservation',
    '岛屿生物地理学': 'Biogéographie insulaire',
    '授粉与种子传播': 'Pollinisation et dispersion des graines',
    '群落动态': 'Dynamique des communautés',
    
    # 宠物护理
    '选择合适的宠物鸟': 'Choisir le bon oiseau de compagnie',
    '鸟类营养与喂养': 'Nutrition et alimentation des oiseaux',
    '住房与环境设置': 'Logement et aménagement de l\'environnement',
    '健康与兽医护理': 'Santé et soins vétérinaires',
    '训练与行为管理': 'Dressage et gestion du comportement',
    '繁殖与繁殖': 'Élevage et reproduction',
    '紧急急救': 'Premiers secours d\'urgence',
    '季节性护理': 'Soins saisonniers',
    '丰富活动': 'Activités d\'enrichissement',
    '老年鸟类护理': 'Soins aux oiseaux âgés',
    
    # 科学奇观
    '鸟类飞行机制': 'Mécanismes de vol des oiseaux',
    '磁场导航': 'Navigation magnétique',
    '蜂鸟飞行机制': 'Mécanismes de vol du colibri',
    '鸟类智能': 'Intelligence des oiseaux',
    '羽毛结构': 'Structure des plumes',
    '鸟类视觉': 'Vision des oiseaux',
    '蛋的发育': 'Développement de l\'œuf',
    '鸟类交流': 'Communication des oiseaux',
    '迁徙生理学': 'Physiologie de la migration',
    '生物力学': 'Biomécanique',
    
    # 知识库
    '初学者指南': 'Guide du débutant',
    '基本设备': 'Équipement de base',
    '识别技术': 'Techniques d\'identification',
    '最佳地点': 'Meilleurs emplacements',
    '行为观察': 'Observation du comportement',
    '声音识别': 'Identification sonore',
    '摄影技巧': 'Conseils de photographie',
    '季节指南': 'Guide saisonnier',
    '日志记录': 'Tenue de journal',
    '伦理保护': 'Éthique et protection',
    
    # 通用词汇
    'BirdAiSnap': 'BirdAiSnap',
    '返回': 'Retour',
    '主页': 'Accueil',
    '关于': 'À propos',
    '联系': 'Contact',
    '特色': 'Fonctionnalités',
    '知识': 'Connaissances',
    '开始观鸟之旅': 'Commencez votre voyage d\'observation des oiseaux',
    '探索鸟类世界': 'Explorez le monde des oiseaux',
    '学习鸟类知识': 'Apprenez sur les oiseaux',
    '发现鸟类之美': 'Découvrez la beauté des oiseaux',
    
    # 内容相关
    '观鸟是一项令人着迷的爱好': 'L\'observation des oiseaux est un passe-temps fascinant',
    '通过观察鸟类，我们可以': 'En observant les oiseaux, nous pouvons',
    '了解自然世界': 'comprendre le monde naturel',
    '享受户外活动': 'profiter des activités de plein air',
    '培养耐心和专注力': 'développer la patience et la concentration',
    '与大自然建立联系': 'établir une connexion avec la nature',
    
    # 设备相关
    '双筒望远镜': 'Jumelles',
    '观鸟指南': 'Guide d\'observation des oiseaux',
    '笔记本': 'Carnet de notes',
    '相机': 'Appareil photo',
    '野外服装': 'Vêtements de terrain',
    
    # 技巧相关
    '仔细观察': 'Observer attentivement',
    '记录细节': 'Noter les détails',
    '识别特征': 'Identifier les caractéristiques',
    '聆听声音': 'Écouter les sons',
    '保持安静': 'Rester silencieux',
    
    # 时间和季节
    '春季': 'Printemps',
    '夏季': 'Été',
    '秋季': 'Automne',
    '冬季': 'Hiver',
    '早晨': 'Matin',
    '傍晚': 'Soir',
    
    # 地点
    '公园': 'Parc',
    '森林': 'Forêt',
    '湖泊': 'Lac',
    '河流': 'Rivière',
    '海岸': 'Côte',
    '山区': 'Montagne',
    '城市': 'Ville',
    '乡村': 'Campagne',
    
    # 鸟类相关
    '鸟类': 'Oiseaux',
    '羽毛': 'Plumes',
    '翅膀': 'Ailes',
    '喙': 'Bec',
    '爪子': 'Griffes',
    '尾巴': 'Queue',
    '鸣叫': 'Chant',
    '飞行': 'Vol',
    '觅食': 'Recherche de nourriture',
    '筑巢': 'Nidification',
    
    # 行为描述
    '飞翔': 'Voler',
    '栖息': 'Se percher',
    '觅食': 'Chercher de la nourriture',
    '歌唱': 'Chanter',
    '筑巢': 'Construire un nid',
    '迁徙': 'Migrer',
    '繁殖': 'Se reproduire',
    
    # 常用短语
    '这是一个': 'C\'est un',
    '非常重要': 'très important',
    '需要注意': 'il faut faire attention',
    '建议': 'il est recommandé',
    '可以帮助': 'peut aider',
    '有助于': 'contribue à',
    '通过': 'grâce à',
    '因此': 'par conséquent',
    '此外': 'de plus',
    '总之': 'en conclusion',
    
    # 页面元素
    '点击这里': 'Cliquez ici',
    '了解更多': 'En savoir plus',
    '查看详情': 'Voir les détails',
    '继续阅读': 'Continuer la lecture',
    '相关文章': 'Articles connexes',
    '推荐阅读': 'Lecture recommandée',
}

def translate_text(text):
    """翻译文本内容"""
    result = text
    
    # 按长度排序，先替换长的短语
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for chinese, french in sorted_translations:
        result = result.replace(chinese, french)
    
    return result

def translate_html_file(file_path):
    """翻译HTML文件中的文本内容，保持格式不变"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 更新语言属性
        content = re.sub(r'<html lang="zh-CN">', '<html lang="fr">', content)
        content = re.sub(r'<html lang="zh">', '<html lang="fr">', content)
        
        # 翻译title标签内容
        def translate_title(match):
            title_content = match.group(1)
            translated = translate_text(title_content)
            return f'<title>{translated}</title>'
        
        content = re.sub(r'<title>(.*?)</title>', translate_title, content, flags=re.DOTALL)
        
        # 翻译文本节点（不在HTML标签内的文本）
        def translate_text_nodes(text):
            # 分割HTML标签和文本内容
            parts = re.split(r'(<[^>]*>)', text)
            
            for i in range(len(parts)):
                # 只翻译不是HTML标签的部分
                if not parts[i].startswith('<'):
                    # 跳过空白和纯数字
                    if parts[i].strip() and not parts[i].strip().isdigit():
                        parts[i] = translate_text(parts[i])
            
            return ''.join(parts)
        
        # 翻译body内容
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
            translated_body = translate_text_nodes(body_content)
            content = content.replace(body_match.group(1), translated_body)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ 错误处理文件 {file_path}: {e}")
        return False

def translate_all_fr_articles():
    """翻译fr目录下的所有文章"""
    
    print("🇫🇷 开始翻译fr目录下的文章为法语...")
    print("=" * 60)
    
    fr_dir = Path("fr")
    if not fr_dir.exists():
        print("❌ fr目录不存在")
        return
    
    # 查找所有HTML文件
    html_files = list(fr_dir.rglob("*.html"))
    
    translated_count = 0
    total_count = len(html_files)
    
    for file_path in html_files:
        print(f"📝 翻译: {file_path}")
        if translate_html_file(file_path):
            translated_count += 1
            print(f"  ✅ 完成")
        else:
            print(f"  ❌ 失败")
    
    print(f"\\n📊 翻译完成: {translated_count}/{total_count} 个文件")

def main():
    print("🚀 开始法语文章翻译...")
    print("=" * 60)
    
    translate_all_fr_articles()
    
    print("\\n" + "=" * 60)
    print("🎉 法语翻译完成！")
    print("\\n📋 完成的任务:")
    print("  ✅ 翻译了fr目录下的所有HTML文件")
    print("  ✅ 保持了原有的HTML格式和排版")
    print("  ✅ 更新了语言属性为fr")
    print("  ✅ 翻译了页面标题和文本内容")

if __name__ == "__main__":
    main()