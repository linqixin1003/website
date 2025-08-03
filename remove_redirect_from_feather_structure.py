#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def remove_redirect_script_from_file(file_path):
    """从文件中移除language-redirect.js脚本引用"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 移除language-redirect.js脚本引用
        # 匹配各种可能的脚本引用格式
        patterns = [
            r'\s*<script src="../../language-redirect\.js"></script>\s*',
            r'\s*<script src="\.\.\/\.\.\/language-redirect\.js"></script>\s*',
            r'\s*<script src="../../language-redirect\.js">\s*</script>\s*',
        ]
        
        original_content = content
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数：移除所有语言版本的05-feather-structure.html文件中的重定向脚本"""
    
    # 支持的语言列表
    languages = ['en', 'zh', 'fr', 'de', 'es', 'it', 'ja', 'ko', 'pt', 'ru']
    
    print("🔧 开始移除所有语言版本的05-feather-structure.html文件中的重定向脚本...")
    
    success_count = 0
    total_count = 0
    
    for lang in languages:
        file_path = f"{lang}/scientific-wonders/05-feather-structure.html"
        total_count += 1
        
        if os.path.exists(file_path):
            if remove_redirect_script_from_file(file_path):
                print(f"✅ {lang}: 成功移除重定向脚本 {file_path}")
                success_count += 1
            else:
                print(f"ℹ️ {lang}: 文件 {file_path} 中没有找到重定向脚本")
        else:
            print(f"⚠️ {lang}: 文件 {file_path} 不存在")
    
    print(f"\n✅ 完成处理，成功修改了 {success_count}/{total_count} 个文件")

if __name__ == "__main__":
    main()