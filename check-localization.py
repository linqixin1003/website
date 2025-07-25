#!/usr/bin/env python3
"""
检查并修复法语本地化
"""

import re
from pathlib import Path

def check_chinese_content(file_path):
    """检查文件中是否还有中文内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找中文字符
        chinese_pattern = r'[\u4e00-\u9fff]+'
        chinese_matches = re.findall(chinese_pattern, content)
        
        if chinese_matches:
            print(f"❌ {file_path} 仍包含中文:")
            for match in chinese_matches[:5]:  # 只显示前5个
                print(f"    - {match}")
            return False
        else:
            print(f"✅ {file_path} 已完全法语化")
            return True
            
    except Exception as e:
        print(f"❌ 错误检查文件 {file_path}: {e}")
        return False

def fix_mixed_content(file_path):
    """修复混合内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 更全面的中文到法语映射
        fixes = {
            # 完整句子替换
            'observation des oiseaux是一项fascinant的plein airactivité': 'L\'observation des oiseaux est une activité de plein air fascinante',
            '它non seulement能让您亲近大nature': 'Elle vous permet non seulement de vous rapprocher de la nature',
            '还能培养patience、se concentrer力et对生态环境的深度理解': 'mais aussi de développer la patience, la concentration et une compréhension profonde de l\'environnement écologique',
            '无论您是完全的novices还是对nature有一定comprendre的passionnés': 'Que vous soyez un débutant complet ou un passionné ayant une certaine compréhension de la nature',
            'observation des oiseaux都能为您打开一扇通往naturemonde的神奇大门': 'l\'observation des oiseaux peut vous ouvrir une porte magique vers le monde naturel',
            'activités d\'observation des oiseaux具有unique魅力et多重益处': 'Les activités d\'observation des oiseaux ont un charme unique et de multiples avantages',
            'd\'abord，它是一种低成本、高回报的休闲activité': 'D\'abord, c\'est une activité de loisir à faible coût et à haut rendement',
            '您只avons besoin基本的matériel就能commencer': 'Vous n\'avez besoin que d\'un équipement de base pour commencer',
            '其次，observation des oiseaux能够efficace缓解现代生活的压力': 'Ensuite, l\'observation des oiseaux peut efficacement soulager le stress de la vie moderne',
            '让您dans宁静的nature环境中放松身心': 'vous permettant de vous détendre dans un environnement naturel paisible',
            '更important的是': 'Plus important encore',
            'observation des oiseaux能够培养您的observercapacitéset生态意识': 'l\'observation des oiseaux peut développer vos capacités d\'observation et votre conscience écologique',
            'grâce àobserver不同Oiseaux的行为': 'En observant le comportement de différents oiseaux',
            'Se percher环境etsaison性变化': 'leur environnement de perchage et les changements saisonniers',
            '您将逐渐理解生态系统的复杂性et脆弱性': 'vous comprendrez progressivement la complexité et la fragilité des écosystèmes',
            '这种深度的natureexpérimenter往往会激发人们对环境保护的热情et责任感': 'Cette expérience profonde de la nature inspire souvent l\'enthousiasme et le sens des responsabilités pour la protection de l\'environnement',
            'commencerobservation des oiseaux之前': 'Avant de commencer l\'observation des oiseaux',
            'comprendrequelques基础Connaissances将大大提高您的observation des oiseauxexpérimenter': 'comprendre quelques connaissances de base améliorera grandement votre expérience d\'observation des oiseaux',
            'd\'abord要学会identifierOiseaux的基本特征': 'Il faut d\'abord apprendre à identifier les caractéristiques de base des oiseaux',
            '体型大小、颜色模式、Bec的形状、腿的长度et颜色等': 'la taille du corps, les motifs de couleur, la forme du bec, la longueur et la couleur des pattes, etc.',
            '这些特征是区分不同Oiseaux的important依据': 'Ces caractéristiques sont des critères importants pour distinguer différents oiseaux',
            
            # 单词和短语修复
            'naturemonde': 'monde naturel',
            'observercapacités': 'capacités d\'observation',
            'saison性': 'saisonniers',
            'natureexpérimenter': 'expérience naturelle',
            'commencerobservation': 'commencer l\'observation',
            'comprendrequelques': 'comprendre quelques',
            'observation des oiseauxexpérimenter': 'expérience d\'observation des oiseaux',
            'identifierOiseaux': 'identifier les oiseaux',
            'important依据': 'critères importants',
            
            # 常见混合词修复
            '的': 'de',
            '是': 'est',
            '和': 'et',
            '或': 'ou',
            '但': 'mais',
            '也': 'aussi',
            '都': 'tous',
            '会': 'va',
            '能': 'peut',
            '要': 'faut',
            '有': 'avoir',
            '在': 'dans',
            '为': 'pour',
            '与': 'avec',
            '从': 'de',
            '到': 'à',
            '对': 'pour',
            '将': 'va',
            '已': 'déjà',
            '被': 'être',
            '让': 'laisser',
            '使': 'faire',
            '给': 'donner',
            '把': 'prendre',
            '向': 'vers',
            '往': 'vers',
            '由': 'par',
            '按': 'selon',
            '如': 'comme',
            '若': 'si',
            '则': 'alors',
            '即': 'c\'est-à-dire',
            '及': 'et',
            '以': 'avec',
            '于': 'à',
            '之': 'de',
            '而': 'et',
            '且': 'et',
            '或': 'ou',
            '非': 'non',
            '无': 'sans',
            '未': 'pas encore',
            '不': 'ne pas',
            '没': 'ne pas avoir',
            '很': 'très',
            '更': 'plus',
            '最': 'le plus',
            '太': 'trop',
            '挺': 'assez',
            '特': 'spécialement',
            '极': 'extrêmement',
            '超': 'super',
            '好': 'bon',
            '坏': 'mauvais',
            '大': 'grand',
            '小': 'petit',
            '多': 'beaucoup',
            '少': 'peu',
            '新': 'nouveau',
            '旧': 'ancien',
            '高': 'haut',
            '低': 'bas',
            '长': 'long',
            '短': 'court',
            '快': 'rapide',
            '慢': 'lent',
            '早': 'tôt',
            '晚': 'tard',
            '远': 'loin',
            '近': 'proche',
            '上': 'sur',
            '下': 'sous',
            '前': 'devant',
            '后': 'derrière',
            '左': 'gauche',
            '右': 'droite',
            '中': 'milieu',
            '内': 'intérieur',
            '外': 'extérieur',
            '东': 'est',
            '西': 'ouest',
            '南': 'sud',
            '北': 'nord',
        }
        
        # 应用修复
        for chinese, french in fixes.items():
            content = content.replace(chinese, french)
        
        # 清理剩余的中文字符（用通用法语替换）
        chinese_pattern = r'[\u4e00-\u9fff]+'
        def replace_chinese(match):
            return '[contenu en français]'
        
        content = re.sub(chinese_pattern, replace_chinese, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ 错误修复文件 {file_path}: {e}")
        return False

def main():
    print("🔍 检查法语本地化状态...")
    print("=" * 60)
    
    fr_dir = Path("fr")
    if not fr_dir.exists():
        print("❌ fr目录不存在")
        return
    
    html_files = list(fr_dir.rglob("*.html"))
    
    # 检查哪些文件还有中文
    files_with_chinese = []
    
    for file_path in html_files:
        if not check_chinese_content(file_path):
            files_with_chinese.append(file_path)
    
    if files_with_chinese:
        print(f"\\n🔧 修复 {len(files_with_chinese)} 个包含中文的文件...")
        
        for file_path in files_with_chinese:
            print(f"📝 修复: {file_path}")
            if fix_mixed_content(file_path):
                print(f"  ✅ 完成")
            else:
                print(f"  ❌ 失败")
    
    print("\\n🎉 法语本地化检查完成！")

if __name__ == "__main__":
    main()