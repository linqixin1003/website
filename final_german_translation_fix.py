#!/usr/bin/env python3
import os
import re
from pathlib import Path

def create_additional_translation_dict():
    """创建补充的英语到德语翻译词典"""
    return {
        # 剩余的常见词汇
        'Information': 'Information',  # 在德语中也使用Information
        'information': 'Information',
        'Migration': 'Migration',      # 在德语中也使用Migration
        'migration': 'Migration',
        'Evolution': 'Evolution',      # 在德语中也使用Evolution
        'evolution': 'Evolution',
        'Winter': 'Winter',           # 在德语中也使用Winter
        'winter': 'Winter',
        'Parks': 'Parks',             # 在德语中也使用Parks
        'parks': 'Parks',
        'Population': 'Population',    # 在德语中也使用Population
        'population': 'Population',
        'Nest': 'Nest',               # 在德语中也使用Nest
        'nest': 'Nest',
        'Region': 'Region',           # 在德语中也使用Region
        'region': 'Region',
        'Zone': 'Zone',               # 在德语中也使用Zone
        'zone': 'Zone',
        'global': 'global',           # 在德语中也使用global
        'Global': 'Global',
        'national': 'national',       # 在德语中也使用national
        'National': 'National',
        'international': 'international', # 在德语中也使用international
        'International': 'International',
        'regional': 'regional',       # 在德语中也使用regional
        'Regional': 'Regional',
        
        # 其他可能的翻译
        'Locations': 'Standorte',
        'locations': 'Standorte',
        'Seasonal': 'Saisonal',
        'seasonal': 'saisonal',
        'Monitoring': 'Überwachung',
        'monitoring': 'Überwachung',
        'Survey': 'Untersuchung',
        'survey': 'Untersuchung',
        'Research': 'Forschung',
        'research': 'Forschung',
        'Studies': 'Studien',
        'studies': 'Studien',
        'Analysis': 'Analyse',
        'analysis': 'Analyse',
        'Data': 'Daten',
        'data': 'Daten',
        'Knowledge': 'Wissen',
        'knowledge': 'Wissen',
        'Science': 'Wissenschaft',
        'science': 'Wissenschaft',
        'Scientific': 'Wissenschaftlich',
        'scientific': 'wissenschaftlich',
        'Biology': 'Biologie',
        'biology': 'Biologie',
        'Biological': 'Biologisch',
        'biological': 'biologisch',
        'Ornithology': 'Ornithologie',
        'ornithology': 'Ornithologie',
        'Ornithological': 'Ornithologisch',
        'ornithological': 'ornithologisch'
    }

def final_fix_german_content(content, translation_dict):
    """最终修复德语内容中剩余的英语单词"""
    
    protected_content = content
    
    # 逐个替换剩余的英语单词
    for english, german in translation_dict.items():
        # 使用单词边界匹配
        pattern = r'\b' + re.escape(english) + r'\b'
        protected_content = re.sub(pattern, german, protected_content)
    
    return protected_content

def final_translate_german_articles():
    """最终翻译德语文章中剩余的英语内容"""
    
    de_dir = Path('de')
    if not de_dir.exists():
        print("德语目录不存在")
        return
    
    translation_dict = create_additional_translation_dict()
    modified_files = []
    
    print("开始最终修复德语文章中剩余的英语内容...")
    
    for html_file in de_dir.rglob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 最终修复英语内容
            fixed_content = final_fix_german_content(content, translation_dict)
            
            if fixed_content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                
                modified_files.append(str(html_file))
                print(f"✅ 已最终修复: {html_file}")
                
        except Exception as e:
            print(f"❌ 处理文件 {html_file} 时出错: {e}")
    
    print(f"\n=== 德语翻译最终修复完成 ===")
    print(f"共修复了 {len(modified_files)} 个文件")
    
    return modified_files

if __name__ == "__main__":
    final_translate_german_articles()