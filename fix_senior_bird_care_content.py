#!/usr/bin/env python3
"""
修复10-senior-bird-care.html的内容，将其从物种档案改为老年鸟护理内容
"""
import os
import shutil

def fix_senior_bird_care_content():
    """修复所有语言版本的10-senior-bird-care.html内容"""
    
    # 所有支持的语言
    languages = ['en', 'fr', 'ko', 'de', 'es', 'ru', 'zh', 'it', 'ja', 'pt']
    
    print("🔧 开始修复所有语言版本的 10-senior-bird-care.html 内容...")
    
    for lang in languages:
        # 源文件路径（09-senior-bird-care.html 包含正确的老年鸟护理内容）
        source_file = f"{lang}/pet-care/09-senior-bird-care.html"
        # 目标文件路径（10-senior-bird-care.html 需要被替换）
        target_file = f"{lang}/pet-care/10-senior-bird-care.html"
        
        if os.path.exists(source_file) and os.path.exists(target_file):
            try:
                # 读取源文件内容
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 写入目标文件
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ {lang}: 成功将老年鸟护理内容复制到 {target_file}")
            except Exception as e:
                print(f"❌ {lang}: 复制失败: {str(e)}")
        else:
            if not os.path.exists(source_file):
                print(f"⚠️ {lang}: 源文件 {source_file} 不存在")
            if not os.path.exists(target_file):
                print(f"⚠️ {lang}: 目标文件 {target_file} 不存在")

if __name__ == "__main__":
    fix_senior_bird_care_content()
    print("✅ 完成内容修复操作")