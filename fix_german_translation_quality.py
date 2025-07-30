#!/usr/bin/env python3
"""
德语翻译质量修复脚本
基于英语版本进行高质量德语翻译
"""
import os
import re
import shutil
from datetime import datetime

def backup_file(file_path):
    """备份文件"""
    backup_path = file_path + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def fix_common_german_errors(content):
    """修复常见的德语翻译错误"""
    
    # 修复常见的错误翻译模式
    fixes = {
        # 修复错误的定冠词使用
        r'\bsterben\b': 'die',
        r'\bder/sterben/das\b': 'der',
        r'\bjener/jene/jenes\b': 'diese',
        
        # 修复HTML标签错误
        r'<stark>': '<strong>',
        r'</stark>': '</strong>',
        
        # 修复CSS类名
        r'equipment-Beschreibung': 'equipment-description',
        r'haupt-text': 'main-text',
        
        # 修复常见的英德混合表达
        r'\bist\s+der/sterben/das\s+best\b': 'ist die beste',
        r'\bist\s+usually\b': 'ist normalerweise',
        r'\bist\s+minimal\b': 'ist minimal',
        r'\bwhen\s+Sie\b': 'wenn Sie',
        r'\bas\s+these\s+sind\b': 'da diese',
        r'\bas\s+they\s+sind\b': 'da sie',
        r'\bmore\s+wichtig\s+than\b': 'wichtiger als',
        r'\bif\s+Sie\b': 'wenn Sie',
        r'\bto\s+improve\b': 'zur Verbesserung',
        r'\bto\s+help\s+Sie\b': 'um Ihnen zu helfen',
        r'\bwhen\s+Sie\s+zurückkehren\s+home\b': 'wenn Sie nach Hause zurückkehren',
        
        # 修复中文标签
        r'观鸟指南': 'Vogelbeobachtung',
        r'知识库': 'Wissensdatenbank',
        r'科学奇观': 'Wissenschaftliche Wunder',
        r'生态学': 'Ökologie',
        r'宠物护理': 'Haustierpflege',
        
        # 修复常见的错误表达
        r'\bbietet\s+das\s+Birding\b': 'bietet die Vogelbeobachtung',
        r'\bvon\s+sterben\s+meisten\b': 'von den meisten',
        r'\bfor\s+discovery\s+und\s+wonder\b': 'für Entdeckung und Staunen',
        r'\bpeak\s+activity\s+times\b': 'Hauptaktivitätszeiten',
        r'\bin\s+most\s+Gebiete\b': 'in den meisten Gebieten',
        r'\bhelfen\s+Sie\s+erinnern\b': 'helfen Ihnen sich zu erinnern',
        r'\bin\s+der/sterben/das\s+field\b': 'im Feld',
        r'\bshoot\s+bei\s+der/sterben/das\s+Vogel\'s\s+eye\s+Ebene\b': 'fotografieren Sie auf Augenhöhe des Vogels',
    }
    
    # 应用修复
    for pattern, replacement in fixes.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    return content

def translate_high_quality_german_text(english_text):
    """基于英语文本生成高质量德语翻译"""
    
    # 专业术语翻译词典
    terminology = {
        'Bird Study Equipment': 'Vogelforschungsausrüstung',
        'Research Tools': 'Forschungswerkzeuge',
        'Birdwatching': 'Vogelbeobachtung',
        'Beginner\'s Guide': 'Leitfaden für Anfänger',
        'Essential Equipment': 'Grundausstattung',
        'Professional bird study': 'Professionelle Vogelforschung',
        'ornithological research': 'ornithologische Forschung',
        'specialized equipment': 'spezialisierte Ausrüstung',
        'scientific tools': 'wissenschaftliche Werkzeuge',
        'Bird banding': 'Vogelberingung',
        'tracking individual birds': 'Verfolgung einzelner Vögel',
        'GPS transmitters': 'GPS-Sender',
        'radio telemetry': 'Radiotelemetrie',
        'migration patterns': 'Zugmuster',
        'Metal Bands': 'Metallringe',
        'Color Bands': 'Farbringe',
        'Banding Pliers': 'Beringungszangen',
        'Band Size Guide': 'Ringgrößenführer',
        'Tracking Technology': 'Verfolgungstechnologie',
        'Radio Transmitters': 'Radiosender',
        'Geolocators': 'Geolokatoren',
        'Receiver Equipment': 'Empfangsgeräte',
        'Capture and Handling': 'Fang und Handhabung',
        'Mist nets': 'Nebelnetze',
        'Safety Protocol': 'Sicherheitsprotokoll',
        'proper training': 'ordnungsgemäße Ausbildung',
        'ethical guidelines': 'ethische Richtlinien',
        'licensed researchers': 'lizenzierte Forscher',
        'Measurement Tools': 'Messwerkzeuge',
        'Data Recording': 'Datenaufzeichnung',
        'Wing Rulers': 'Flügellineale',
        'Calipers': 'Messschieber',
        'Precision Scales': 'Präzisionswaagen',
        'Fat Score Charts': 'Fettscore-Tabellen',
        'Field Computers': 'Feldcomputer',
        'Data Loggers': 'Datenlogger',
        'Voice Recorders': 'Sprachaufzeichnungsgeräte',
        'Barcode Scanners': 'Barcode-Scanner',
        'Laboratory Equipment': 'Laborausrüstung',
        'genetic studies': 'genetische Studien',
        'physiological studies': 'physiologische Studien',
        'pathological studies': 'pathologische Studien',
        'conservation genetics': 'Naturschutzgenetik'
    }
    
    # 这里可以扩展为更复杂的翻译逻辑
    # 目前返回基础翻译框架
    return english_text

def process_german_file(file_path):
    """处理单个德语文件"""
    print(f"处理文件: {file_path}")
    
    try:
        # 备份原文件
        backup_path = backup_file(file_path)
        print(f"已备份至: {backup_path}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 应用修复
        fixed_content = fix_common_german_errors(content)
        
        # 保存修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ 修复完成: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 修复失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("开始德语翻译质量修复...")
    
    # 需要修复的德语文件目录
    german_dirs = [
        'de/birdwatching',
        'de/knowledge', 
        'de/ecology',
        'de/pet-care',
        'de/scientific-wonders'
    ]
    
    total_files = 0
    fixed_files = 0
    
    for dir_path in german_dirs:
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith('.html') and not filename.endswith('.backup'):
                    file_path = os.path.join(dir_path, filename)
                    total_files += 1
                    
                    if process_german_file(file_path):
                        fixed_files += 1
    
    print(f"\n修复完成!")
    print(f"总文件数: {total_files}")
    print(f"成功修复: {fixed_files}")
    print(f"失败数量: {total_files - fixed_files}")

if __name__ == "__main__":
    main() 