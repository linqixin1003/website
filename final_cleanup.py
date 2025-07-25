#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终清理ru目录下HTML文件中剩余的英文内容
"""

import os
import re
from pathlib import Path

# 剩余的英文翻译
FINAL_TRANSLATIONS = {
    "Emergency First Aid:": "Экстренная первая помощь:",
    "Keep the bird warm and quiet": "Держите птицу в тепле и покое",
    "Getting Started": "Начало работы",
    "Essential Equipment": "Необходимое оборудование",
    "Species Profiles": "Профили видов",
    "Bird Welfare": "Благополучие птиц",
    "Habitat Protection": "Защита среды обитания",
    
    # 其他可能遗漏的内容
    "• Keep the bird warm and quiet": "• Держите птицу в тепле и покое",
    "• Contact your avian veterinarian immediately": "• Немедленно свяжитесь с орнитологическим ветеринаром",
    "• Do not attempt to give food or water": "• Не пытайтесь давать еду или воду",
    "• Handle minimally to reduce stress": "• Обращайтесь минимально, чтобы уменьшить стресс",
    "• Transport in a secure, ventilated carrier": "• Транспортируйте в безопасной, вентилируемой переноске",
    
    # 健康相关
    "Immediate Emergency Signs": "Немедленные признаки экстренной ситуации",
    "Difficulty breathing": "Затрудненное дыхание",
    "Bleeding": "Кровотечение",
    "Unconsciousness": "Потеря сознания",
    "Severe injury": "Серьезная травма",
    "Seizures": "Судороги",
    "Inability to perch": "Неспособность сидеть на жердочке",
    
    # 其他常见短语
    "Contact your avian veterinarian immediately": "Немедленно свяжитесь с орнитологическим ветеринаром",
    "Do not attempt to give food or water": "Не пытайтесь давать еду или воду",
    "Handle minimally to reduce stress": "Обращайтесь минимально, чтобы уменьшить стресс",
    "Transport in a secure, ventilated carrier": "Транспортируйте в безопасной, вентилируемой переноске",
}

def clean_remaining_english(file_path):
    """清理文件中剩余的英文内容"""
    print(f"清理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用最终翻译
        for en_text, ru_text in FINAL_TRANSLATIONS.items():
            content = content.replace(en_text, ru_text)
        
        # 检查是否有变化
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已清理: {file_path}")
            return True
        else:
            print(f"⏭️  无需清理: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 清理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("开始最终清理ru目录下的英文内容...")
    
    # 获取ru目录下的所有HTML文件
    ru_dir = Path("ru")
    if not ru_dir.exists():
        print("❌ ru目录不存在!")
        return
    
    html_files = list(ru_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 在ru目录下没有找到HTML文件!")
        return
    
    print(f"找到 {len(html_files)} 个HTML文件")
    
    # 清理每个文件
    cleaned_count = 0
    for file_path in html_files:
        if clean_remaining_english(file_path):
            cleaned_count += 1
    
    print(f"\n✅ 最终清理完成! 共处理了 {len(html_files)} 个文件，清理了 {cleaned_count} 个文件")
    
    # 最终检查
    print("\n进行最终检查...")
    remaining_issues = []
    
    # 检查特定的英文模式
    check_patterns = [
        "Emergency First Aid",
        "Getting Started", 
        "Essential Equipment",
        "Species Profiles",
        "Bird Welfare",
        "Habitat Protection",
        "Keep the bird warm",
        "Contact your avian"
    ]
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for pattern in check_patterns:
                if pattern in content:
                    remaining_issues.append((str(file_path), pattern))
        
        except Exception as e:
            print(f"检查文件 {file_path} 时出错: {e}")
    
    if remaining_issues:
        print(f"\n⚠️  发现 {len(remaining_issues)} 处需要手动检查的内容:")
        for file_path, text in remaining_issues[:10]:  # 只显示前10个
            print(f"  {file_path}: {text}")
        if len(remaining_issues) > 10:
            print(f"  ... 还有 {len(remaining_issues) - 10} 处")
    else:
        print("\n🎉 所有英文内容都已成功翻译为俄语!")

if __name__ == "__main__":
    main()