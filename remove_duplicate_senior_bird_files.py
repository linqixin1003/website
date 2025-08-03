#!/usr/bin/env python3
"""
删除所有语言版本的 pet-care/11-senior-bird-care.html 文件，避免与 10-senior-bird-care.html 混淆
"""
import os

def remove_duplicate_files():
    """删除所有语言版本的11-senior-bird-care.html文件"""
    
    # 所有支持的语言
    languages = ['en', 'fr', 'ko', 'de', 'es', 'ru', 'zh', 'it', 'ja', 'pt']
    
    print("🔧 开始删除所有语言版本的 pet-care/11-senior-bird-care.html 文件...")
    
    for lang in languages:
        file_path = f"{lang}/pet-care/11-senior-bird-care.html"
        
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"✅ {lang}: 成功删除 {file_path}")
            except Exception as e:
                print(f"❌ {lang}: 删除失败: {str(e)}")
        else:
            print(f"ℹ️ {lang}: 文件 {file_path} 不存在")

if __name__ == "__main__":
    remove_duplicate_files()
    print("✅ 完成删除操作")