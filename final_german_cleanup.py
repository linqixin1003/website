#!/usr/bin/env python3
"""
德语翻译最终清理脚本
修复剩余的中文注释和英德混合问题
"""
import os
import re
import shutil
from datetime import datetime

def backup_file(file_path):
    """备份文件"""
    backup_path = file_path + f".backup_final_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def clean_remaining_issues(content):
    """清理剩余的翻译问题"""
    
    # 1. 修复中文HTML注释
    comment_replacements = {
        r'<!-- 主要内容 -->': '<!-- Hauptinhalt -->',
        r'<!-- 英雄图片 -->': '<!-- Hero-Bild -->',
        r'<!-- 文章信息 -->': '<!-- Artikel-Info -->',
        r'<!-- 引用框 -->': '<!-- Zitat-Box -->',
        r'<!-- 文章正文 -->': '<!-- Artikel-Text -->',
        r'<!-- 主图 -->': '<!-- Hauptbild -->',
        r'<!-- 进度条 -->': '<!-- Fortschrittsbalken -->',
        r'<!-- 更新时间 -->': '<!-- Aktualisierung Zeit -->',
        r'<!-- 模拟阅读进度 -->': '<!-- Simuliere Lesefortschritt -->',
        r'<!-- 初始化 -->': '<!-- Initialisierung -->',
        r'<!-- 移动端优化 -->': '<!-- Mobile Optimierung -->',
        r'<!-- 解决文本离边框太近的问题 -->': '<!-- Löse Text-zu-Rand Problem -->',
        r'<!-- 练习部分优化 -->': '<!-- Übungsbereich Optimierung -->',
    }
    
    for chinese_comment, german_comment in comment_replacements.items():
        content = re.sub(chinese_comment, german_comment, content)
    
    # 2. 修复英德混合表达
    mixed_fixes = {
        r'when human activity ist minimal': 'wenn menschliche Aktivität minimal ist',
        r'when Sie': 'wenn Sie',
        r'if Sie': 'wenn Sie',
        r'ist usually': 'ist normalerweise',
        r'as these sind': 'da diese sind',
        r'as they sind': 'da sie sind',
        r'more wichtig than': 'wichtiger als',
        r'for discovery und wonder': 'für Entdeckung und Staunen',
        r'peak activity times': 'Hauptaktivitätszeiten',
        r'in most Gebiete': 'in den meisten Gebieten',
        r'to improve': 'zur Verbesserung',
        r'to help Sie': 'um Ihnen zu helfen',
    }
    
    for english_phrase, german_phrase in mixed_fixes.items():
        content = re.sub(english_phrase, german_phrase, content, flags=re.IGNORECASE)
    
    # 3. 清理其他可能的中文残留
    other_fixes = {
        r'学': '',  # 单独的中文字符
        r'[\u4e00-\u9fff]': '',  # 清理其他孤立的中文字符（谨慎使用）
    }
    
    # 只清理孤立的中文字符，不清理在引号或特定上下文中的
    content = re.sub(r'(?<!["\'\w])[\u4e00-\u9fff](?!["\'\w])', '', content)
    
    return content

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 备份文件
        backup_path = backup_file(file_path)
        
        # 清理内容
        cleaned_content = clean_remaining_issues(content)
        
        # 检查是否有变化
        if cleaned_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            print(f"✅ 修复完成: {file_path}")
            return True
        else:
            # 删除不必要的备份
            os.remove(backup_path)
            print(f"📝 无需修复: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 修复失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("🔧 开始最终德语清理...")
    print("=" * 50)
    
    # 需要清理的文件列表（基于检查结果）
    problematic_files = [
        'de/birdwatching/04-best-locations.html',
        'de/birdwatching/02-essential-equipment.html',
        'de/birdwatching/01-getting-started.html',
        'de/birdwatching/03-identification-techniques.html',
        'de/knowledge/03-identification-techniques.html',
        'de/ecology/02-food-webs-chains.html',
        'de/ecology/01-habitat-ecosystems.html',
        'de/ecology/03-migration-patterns.html',
        'de/scientific-wonders/04-bird-intelligence.html',
    ]
    
    fixed_count = 0
    total_count = len(problematic_files)
    
    for file_path in problematic_files:
        if os.path.exists(file_path):
            if process_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️ 文件不存在: {file_path}")
    
    print("\n" + "=" * 50)
    print("📊 最终清理结果")
    print("=" * 50)
    print(f"📄 处理文件数: {total_count}")
    print(f"✅ 修复文件数: {fixed_count}")
    print(f"📝 无需修复: {total_count - fixed_count}")
    
    if fixed_count > 0:
        print(f"\n🎉 成功修复 {fixed_count} 个文件！")
        print("✨ 建议重新运行检查脚本验证修复效果")
    else:
        print("\n📝 所有文件都已符合要求")

if __name__ == "__main__":
    main() 