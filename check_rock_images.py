#!/usr/bin/env python3
import os
import re

def check_file_has_image(file_path):
    """检查文件是否包含岩石图片"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含rock图片路径
        if 'images/rock/' in content:
            return True
        return False
    except:
        return False

def main():
    """检查所有岩石文章的图片情况"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    total_files = 0
    files_with_images = 0
    
    print("🔍 检查岩石文章头图添加情况:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"📁 {directory}:")
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in sorted(html_files):
                file_path = os.path.join(directory, html_file)
                total_files += 1
                
                if check_file_has_image(file_path):
                    print(f"  ✅ {html_file}")
                    files_with_images += 1
                else:
                    print(f"  ❌ {html_file}")
            print()
    
    print(f"📊 总结: {files_with_images}/{total_files} 个文件已添加头图")
    print(f"完成率: {files_with_images/total_files*100:.1f}%")

if __name__ == "__main__":
    main()