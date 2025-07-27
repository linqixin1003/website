#!/usr/bin/env python3
import os
import re

def fix_scientific_wonders_paths():
    """修复德语版本科学奇观页面的图片路径"""
    
    # 德语科学奇观目录
    de_scientific_dir = 'de/scientific-wonders'
    
    if not os.path.exists(de_scientific_dir):
        print(f"❌ 目录不存在: {de_scientific_dir}")
        return
    
    # 遍历所有HTML文件
    for filename in os.listdir(de_scientific_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(de_scientific_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查是否包含错误的德语路径
                if 'images/Vögel/Art/' in content:
                    # 替换错误的德语路径为正确的英语路径
                    new_content = content.replace('images/Vögel/Art/', 'images/birds/species/')
                    
                    # 写回文件
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"✅ 已修复: {filepath}")
                else:
                    print(f"⚪ 无需修复: {filepath}")
                    
            except Exception as e:
                print(f"❌ 处理文件时出错 {filepath}: {e}")

if __name__ == "__main__":
    print("开始修复德语版本科学奇观页面的图片路径...")
    fix_scientific_wonders_paths()
    print("修复完成！")