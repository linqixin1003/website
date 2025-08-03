#!/usr/bin/env python3
"""
将所有语言版本的 pet-care/10-species-profiles.html 文件重命名为 pet-care/10-senior-bird-care.html
"""
import os
import shutil

def rename_species_profiles_files():
    """将所有语言版本的species-profiles文件重命名为senior-bird-care"""
    
    # 所有支持的语言
    languages = ['en', 'fr', 'ko', 'de', 'es', 'ru', 'zh', 'it', 'ja', 'pt']
    
    print("🔧 开始将所有语言版本的 pet-care/10-species-profiles.html 重命名为 pet-care/10-senior-bird-care.html...")
    
    for lang in languages:
        old_path = f"{lang}/pet-care/10-species-profiles.html"
        new_path = f"{lang}/pet-care/10-senior-bird-care.html"
        
        if os.path.exists(old_path):
            try:
                # 如果目标文件已存在，先检查内容是否相同
                if os.path.exists(new_path):
                    with open(old_path, 'r', encoding='utf-8') as old_file:
                        old_content = old_file.read()
                    with open(new_path, 'r', encoding='utf-8') as new_file:
                        new_content = new_file.read()
                    
                    if old_content == new_content:
                        print(f"✅ {lang}: 文件内容相同，删除旧文件 {old_path}")
                        os.remove(old_path)
                    else:
                        print(f"⚠️ {lang}: 文件内容不同，保留两个文件")
                else:
                    # 如果目标文件不存在，直接重命名
                    shutil.move(old_path, new_path)
                    print(f"✅ {lang}: 成功将 {old_path} 重命名为 {new_path}")
            except Exception as e:
                print(f"❌ {lang}: 重命名失败: {str(e)}")
        else:
            print(f"ℹ️ {lang}: 文件 {old_path} 不存在")

if __name__ == "__main__":
    rename_species_profiles_files()
    print("✅ 完成重命名操作")