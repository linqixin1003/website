#!/usr/bin/env python3
import os
import re
import urllib.parse

def fix_image_path_in_file(file_path):
    """修复文件中的图片路径，对特殊字符进行URL编码"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并修复CSS背景图片路径
        def encode_path(match):
            path = match.group(1)
            # 对路径中的特殊字符进行编码
            encoded_path = path.replace('&', '%26')
            return f"url('{encoded_path}')"
        
        # 替换所有的url()路径
        new_content = re.sub(r"url\('([^']+)'\)", encode_path, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"处理 {file_path} 时出错: {e}")
        return False

def main():
    """修复所有岩石文章的图片路径"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    fixed_count = 0
    total_count = 0
    
    print("🔧 修复岩石文章图片路径中的特殊字符:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"📁 {directory}:")
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in sorted(html_files):
                file_path = os.path.join(directory, html_file)
                total_count += 1
                
                if fix_image_path_in_file(file_path):
                    print(f"  ✅ 已修复 {html_file}")
                    fixed_count += 1
                else:
                    print(f"  ➖ {html_file} (无需修复)")
            print()
    
    print(f"📊 总结: 修复了 {fixed_count}/{total_count} 个文件")

if __name__ == "__main__":
    main()