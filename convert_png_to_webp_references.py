#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

class PngToWebpConverter:
    """将所有PNG图片引用转换为WebP格式"""
    
    def __init__(self):
        self.processed_files = 0
        self.modified_files = 0
        self.total_replacements = 0
        
    def convert_png_references_in_file(self, file_path):
        """转换单个文件中的PNG引用为WebP"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            replacements_count = 0
            
            # 匹配所有PNG图片引用并替换为WebP
            # 匹配模式：images/birds/species/xxx.png
            png_pattern = r'(images/birds/species/[^"\'\s]+)\.png'
            
            def replace_png_with_webp(match):
                nonlocal replacements_count
                replacements_count += 1
                return match.group(1) + '.webp'
            
            content = re.sub(png_pattern, replace_png_with_webp, content)
            
            # 如果内容有变化，写回文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.total_replacements += replacements_count
                return True, replacements_count
            
            return False, 0
            
        except Exception as e:
            print(f"❌ 处理文件失败 {file_path}: {e}")
            return False, 0
    
    def process_directory(self, directory_path):
        """处理指定目录下的所有HTML文件"""
        directory = Path(directory_path)
        if not directory.exists():
            print(f"⚠️ 目录不存在: {directory_path}")
            return 0
        
        modified_count = 0
        
        # 递归查找所有HTML文件
        html_files = list(directory.rglob('*.html'))
        
        for html_file in html_files:
            self.processed_files += 1
            modified, replacements = self.convert_png_references_in_file(html_file)
            
            if modified:
                print(f"✅ 已转换 {replacements} 个PNG引用: {html_file}")
                modified_count += 1
                self.modified_files += 1
            else:
                print(f"ℹ️ 无需修改: {html_file}")
        
        return modified_count
    
    def convert_all_references(self):
        """转换所有PNG引用为WebP"""
        print("🚀 开始将所有PNG图片引用转换为WebP格式")
        print("="*60)
        
        # 需要处理的目录列表
        directories_to_process = [
            'en',
            'zh', 
            'ja',
            'ko',
            'fr',
            'de',
            'it',
            'pt',
            'ru',
            'es',
            '.'  # 根目录的HTML文件
        ]
        
        total_modified = 0
        
        for directory in directories_to_process:
            if directory == '.':
                # 处理根目录的HTML文件，但不递归
                root_files = [f for f in Path('.').glob('*.html')]
                if root_files:
                    print(f"\n🔧 处理根目录HTML文件...")
                    for html_file in root_files:
                        self.processed_files += 1
                        modified, replacements = self.convert_png_references_in_file(html_file)
                        
                        if modified:
                            print(f"✅ 已转换 {replacements} 个PNG引用: {html_file}")
                            total_modified += 1
                            self.modified_files += 1
                        else:
                            print(f"ℹ️ 无需修改: {html_file}")
            else:
                if Path(directory).exists():
                    print(f"\n🔧 处理 {directory.upper()} 目录...")
                    modified_count = self.process_directory(directory)
                    total_modified += modified_count
                    print(f"📊 {directory.upper()} 目录修改了 {modified_count} 个文件")
        
        print("\n" + "="*60)
        print("🎉 PNG到WebP转换完成！")
        print(f"📊 总计处理文件: {self.processed_files} 个")
        print(f"✅ 成功修改文件: {self.modified_files} 个")
        print(f"🔄 总计替换次数: {self.total_replacements} 次")
        print("\n主要修改:")
        print("- 将所有 .png 引用替换为 .webp")
        print("- 保持图片路径结构不变")
        print("- 提升网站加载性能")
        
        return total_modified

def main():
    """主函数"""
    converter = PngToWebpConverter()
    converter.convert_all_references()

if __name__ == "__main__":
    main()