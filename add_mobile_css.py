#!/usr/bin/env python3
import os
import re

def add_mobile_css_to_file(file_path):
    """为HTML文件添加移动端CSS链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经包含mobile-rock-styles.css
        if 'mobile-rock-styles.css' in content:
            return False
        
        # 查找现有的CSS链接并添加移动端CSS
        css_pattern = r'(<link rel="stylesheet" href="[^"]*rock-styles\.css">)'
        
        def add_mobile_css(match):
            existing_css = match.group(1)
            mobile_css = '\n    <link rel="stylesheet" href="../../mobile-rock-styles.css">'
            return existing_css + mobile_css
        
        new_content = re.sub(css_pattern, add_mobile_css, content)
        
        # 如果没有找到rock-styles.css，尝试在head结束前添加
        if new_content == content:
            head_pattern = r'(</head>)'
            mobile_css = '    <link rel="stylesheet" href="../../mobile-rock-styles.css">\n'
            new_content = re.sub(head_pattern, mobile_css + r'\1', content)
        
        # 如果内容有变化，写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
            
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    """为所有岩石文章添加移动端CSS"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    success_count = 0
    total_count = 0
    
    print("📱 为岩石文章添加移动端CSS优化...")
    
    for directory in directories:
        if os.path.exists(directory):
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in html_files:
                file_path = os.path.join(directory, html_file)
                total_count += 1
                
                if add_mobile_css_to_file(file_path):
                    print(f"✅ {file_path}")
                    success_count += 1
                else:
                    print(f"⚠️  {file_path} (已存在或无法添加)")
    
    print(f"\n完成! 成功为 {success_count}/{total_count} 个文件添加了移动端CSS")

if __name__ == "__main__":
    main()