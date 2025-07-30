#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime

def backup_file(file_path):
    """备份文件"""
    backup_path = file_path + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def detect_main_language(content):
    """检测内容的主要语言"""
    # 定义语言特征词汇
    language_patterns = {
        'zh': [r'鸟类', r'设备', r'研究', r'的', r'和', r'或', r'在', r'为', r'是'],
        'en': [r'\bbird\b', r'\bequipment\b', r'\bresearch\b', r'\bthe\b', r'\band\b', r'\bor\b', r'\bin\b', r'\bfor\b', r'\bis\b'],
        'ja': [r'鳥', r'機材', r'研究', r'の', r'と', r'また', r'が', r'を', r'に'],
        'ko': [r'새', r'장비', r'연구', r'의', r'와', r'또는', r'가', r'을', r'에'],
        'de': [r'Vogel', r'Ausrüstung', r'Forschung', r'der', r'und', r'oder', r'in', r'für', r'ist'],
        'fr': [r'oiseau', r'équipement', r'recherche', r'le', r'et', r'ou', r'dans', r'pour', r'est'],
        'es': [r'ave', r'equipo', r'investigación', r'el', r'y', r'o', r'en', r'para', r'es'],
        'it': [r'uccello', r'attrezzatura', r'ricerca', r'il', r'e', r'o', r'in', r'per', r'è'],
        'pt': [r'ave', r'equipamento', r'pesquisa', r'o', r'e', r'ou', r'em', r'para', r'é'],
        'ru': [r'птица', r'оборудование', r'исследование', r'и', r'или', r'в', r'для', r'это']
    }
    
    content_lower = content.lower()
    scores = {}
    
    for lang, patterns in language_patterns.items():
        score = 0
        for pattern in patterns:
            matches = len(re.findall(pattern, content_lower, re.IGNORECASE))
            score += matches
        scores[lang] = score
    
    # 返回得分最高的语言
    if scores:
        main_lang = max(scores, key=scores.get)
        if scores[main_lang] > 3:  # 至少要有3个匹配
            return main_lang
    
    return None

def get_problematic_files():
    """获取有问题的文件列表"""
    problematic_files = [
        'en/knowledge/02-essential-equipment.html',
        'en/knowledge/01-beginners-guide.html', 
        'en/knowledge/03-identification-techniques.html',
        'en/birdwatching/02-essential-equipment.html',
        'en/birdwatching/03-identification-techniques.html',
        'zh/birdwatching/03-identification-techniques.html',
        'ko/knowledge/02-essential-equipment.html',
        'ja/knowledge/03-identification-techniques.html',
        'de/knowledge/02-essential-equipment.html',
        'de/knowledge/01-beginners-guide.html',
        'de/knowledge/03-identification-techniques.html',
        'de/birdwatching/02-essential-equipment.html',
        'de/birdwatching/03-identification-techniques.html',
        'fr/knowledge/02-essential-equipment.html',
        'fr/knowledge/01-beginners-guide.html',
        'fr/knowledge/03-identification-techniques.html',
        'fr/birdwatching/02-essential-equipment.html',
        'fr/birdwatching/03-identification-techniques.html',
        'es/knowledge/02-essential-equipment.html',
        'es/knowledge/01-beginners-guide.html',
        'es/knowledge/03-identification-techniques.html',
        'es/birdwatching/02-essential-equipment.html',
        'es/birdwatching/03-identification-techniques.html',
        'it/knowledge/02-essential-equipment.html',
        'it/knowledge/01-beginners-guide.html',
        'it/birdwatching/02-essential-equipment.html',
        'it/birdwatching/03-identification-techniques.html',
        'pt/knowledge/01-beginners-guide.html',
        'pt/birdwatching/03-identification-techniques.html',
        'ru/knowledge/02-essential-equipment.html'
    ]
    
    return [f for f in problematic_files if os.path.exists(f)]

def check_and_fix_file(file_path):
    """检查并修复单个文件"""
    print(f"📄 检查文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取文件应该的语言（从路径）
        expected_lang = file_path.split('/')[0]
        
        # 提取主要内容（去掉HTML标签和样式）
        # 找到body标签之后的内容
        body_match = re.search(r'<body.*?>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
        if body_match:
            body_content = body_match.group(1)
            # 移除HTML标签
            text_content = re.sub(r'<[^>]+>', ' ', body_content)
            # 移除多余空白
            text_content = re.sub(r'\s+', ' ', text_content).strip()
            
            # 检测主要语言
            detected_lang = detect_main_language(text_content)
            
            if detected_lang and detected_lang != expected_lang:
                print(f"  ❌ 语言混乱: 期望 {expected_lang}, 检测到 {detected_lang}")
                print(f"  📝 内容预览: {text_content[:100]}...")
                
                # 备份原文件
                backup_path = backup_file(file_path)
                print(f"  💾 已备份到: {backup_path}")
                
                return True
            else:
                print(f"  ✅ 语言正确: {expected_lang}")
                return False
        else:
            print(f"  ⚠️  无法找到body内容")
            return False
            
    except Exception as e:
        print(f"  ❌ 处理错误: {e}")
        return False

def main():
    """主函数"""
    print("🔧 开始修复语言内容混乱问题...")
    print("=" * 60)
    
    problematic_files = get_problematic_files()
    
    if not problematic_files:
        print("✅ 没有找到有问题的文件！")
        return
    
    print(f"📋 找到 {len(problematic_files)} 个有问题的文件")
    print()
    
    fixed_count = 0
    
    for file_path in problematic_files:
        if check_and_fix_file(file_path):
            fixed_count += 1
        print()
    
    print("=" * 60)
    print(f"🏁 处理完成！")
    print(f"📊 检查了 {len(problematic_files)} 个文件")
    print(f"🔧 发现需要修复的文件: {fixed_count} 个")
    print()
    print("⚠️  注意：文件已备份，但需要手动修复内容或重新生成正确的语言版本")

if __name__ == "__main__":
    main() 