#!/usr/bin/env python3
import os
import re

def fix_german_filenames():
    """修复德语版本页面中的图片文件名"""
    
    # 需要修复的德语目录
    german_dirs = [
        'de/birdwatching',
        'de/scientific-wonders',
        'de/knowledge',
        'de/ecology', 
        'de/pet-care'
    ]
    
    total_fixed = 0
    
    for dir_path in german_dirs:
        if not os.path.exists(dir_path):
            print(f"❌ 目录不存在: {dir_path}")
            continue
            
        print(f"\n🔧 处理目录: {dir_path}")
        
        # 遍历目录中的所有HTML文件
        for filename in os.listdir(dir_path):
            if filename.endswith('.html'):
                filepath = os.path.join(dir_path, filename)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 检查是否包含德语文件名
                    if 'Vogel-image-' in content:
                        # 替换德语文件名为英语文件名
                        new_content = content.replace('Vogel-image-', 'bird-image-')
                        
                        # 写回文件
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"  ✅ 已修复: {filename}")
                        total_fixed += 1
                    else:
                        print(f"  ⚪ 无需修复: {filename}")
                        
                except Exception as e:
                    print(f"  ❌ 处理文件时出错 {filename}: {e}")
    
    print(f"\n🎉 修复完成！总共修复了 {total_fixed} 个文件")

if __name__ == "__main__":
    print("开始修复德语版本页面中的图片文件名...")
    fix_german_filenames()