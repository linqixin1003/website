#!/usr/bin/env python3
import os
import re
import glob

def add_language_redirect_script(file_path):
    """为HTML文件添加语言重定向脚本"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经包含language-redirect.js
        if 'language-redirect.js' in content:
            print(f"跳过 {file_path} - 已包含语言重定向脚本")
            return
        
        # 计算相对路径深度
        path_parts = file_path.split('/')
        depth = len(path_parts) - 1  # 减去文件名本身
        relative_path = '../' * (depth - 1) + 'language-redirect.js'
        
        # 查找</body>标签前的位置，插入脚本
        script_tag = f'    <script src="{relative_path}"></script>\n'
        
        # 在最后一个</script>标签后插入
        if '</script>' in content:
            # 找到最后一个</script>的位置
            last_script_pos = content.rfind('</script>')
            if last_script_pos != -1:
                # 在最后一个</script>后插入新脚本
                insert_pos = last_script_pos + len('</script>')
                content = content[:insert_pos] + '\n' + script_tag + content[insert_pos:]
            else:
                # 如果没找到</script>，在</body>前插入
                content = content.replace('</body>', script_tag + '</body>')
        else:
            # 如果没有script标签，在</body>前插入
            content = content.replace('</body>', script_tag + '</body>')
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已更新 {file_path}")
        
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

def main():
    """主函数"""
    # 查找所有语言目录下的HTML文件
    languages = ['en', 'zh', 'ko', 'ja', 'de', 'fr', 'es', 'it', 'pt', 'ru']
    categories = ['knowledge', 'birdwatching', 'pet-care', 'scientific-wonders', 'ecology', 'cultural-symbolism']
    
    for lang in languages:
        for category in categories:
            pattern = f"{lang}/{category}/*.html"
            html_files = glob.glob(pattern)
            
            for file_path in html_files:
                if os.path.exists(file_path):
                    add_language_redirect_script(file_path)
    
    print("所有文章页面已更新完成！")

if __name__ == "__main__":
    main()