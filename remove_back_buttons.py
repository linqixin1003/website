#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

class BackButtonRemover:
    """移除所有多语言文章中的返回键"""
    
    def __init__(self):
        self.languages = ['zh', 'ja', 'ko', 'fr', 'de', 'it', 'pt', 'ru']
        self.categories = ['birdwatching', 'ecology', 'knowledge', 'pet-care', 'scientific-wonders']
        self.processed_files = 0
        self.modified_files = 0
    
    def remove_back_button_from_file(self, file_path):
        """从单个HTML文件中移除返回键"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 移除返回按钮的HTML代码
            # 匹配 <!-- 返回按钮 --> 到 </button> 的整个块
            back_button_pattern = r'<!-- 返回按钮 -->.*?</button>'
            content = re.sub(back_button_pattern, '', content, flags=re.DOTALL)
            
            # 移除返回按钮相关的CSS样式
            # 匹配 .back-button 样式块
            css_pattern = r'\.back-button\s*\{[^}]*\}'
            content = re.sub(css_pattern, '', content, flags=re.DOTALL)
            
            # 清理多余的空行
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ 处理文件失败 {file_path}: {e}")
            return False
    
    def process_language_directory(self, lang_code):
        """处理指定语言目录下的所有HTML文件"""
        print(f"\n🔧 处理 {lang_code.upper()} 语言版本...")
        
        lang_dir = Path(lang_code)
        if not lang_dir.exists():
            print(f"⚠️ 目录不存在: {lang_code}")
            return 0
        
        modified_count = 0
        
        # 遍历所有分类目录
        for category in self.categories:
            category_dir = lang_dir / category
            if category_dir.exists():
                # 处理该分类下的所有HTML文件
                html_files = list(category_dir.glob('*.html'))
                
                for html_file in html_files:
                    self.processed_files += 1
                    if self.remove_back_button_from_file(html_file):
                        print(f"✅ 已移除返回键: {html_file}")
                        modified_count += 1
                        self.modified_files += 1
                    else:
                        print(f"ℹ️ 无需修改: {html_file}")
        
        print(f"📊 {lang_code.upper()} 语言修改了 {modified_count} 个文件")
        return modified_count
    
    def remove_all_back_buttons(self):
        """移除所有语言版本中的返回键"""
        print("🚀 开始移除所有多语言文章中的返回键")
        print("="*60)
        
        total_modified = 0
        
        for lang_code in self.languages:
            modified_count = self.process_language_directory(lang_code)
            total_modified += modified_count
        
        print("\n" + "="*60)
        print("🎉 返回键移除完成！")
        print(f"📊 总计处理文件: {self.processed_files} 个")
        print(f"✅ 成功修改文件: {self.modified_files} 个")
        print(f"🌍 涉及语言: {', '.join([lang.upper() for lang in self.languages])}")
        print("\n主要修改:")
        print("- 移除了返回按钮的HTML代码")
        print("- 移除了返回按钮的CSS样式")
        print("- 清理了多余的空行")
        
        return total_modified

def main():
    """主函数"""
    remover = BackButtonRemover()
    remover.remove_all_back_buttons()

if __name__ == "__main__":
    main()