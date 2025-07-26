import os
import json
import re
from bs4 import BeautifulSoup

def load_json_config(file_path):
    """加载JSON配置文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_hero_image_to_html(html_path, image_url):
    """向HTML文件添加头图元素"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否已有hero-image元素
        hero_image = soup.select_one('.hero-image')
        if hero_image:
            return False, "已存在头图元素"
            
        # 从JSON URL中提取相对路径
        relative_url = image_url.replace('https://linqixin1003.github.io/website/', '../../')
        
        # 查找main-content元素，在其前面添加hero-image
        main_content = soup.select_one('.main-content')
        if main_content:
            # 创建hero-image元素
            hero_div = soup.new_tag('div')
            hero_div['class'] = 'hero-image'
            hero_div['style'] = f"width: 100%; height: 400px; background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), url('{relative_url}') center/cover; position: relative; margin-top: 0;"
            
            # 在main-content前插入hero-image
            main_content.insert_before(hero_div)
            
            # 写回文件
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
            return True, "成功添加头图元素"
        else:
            # 查找body元素，在其第一个子元素前添加hero-image
            body = soup.body
            if body and body.contents:
                # 创建hero-image元素
                hero_div = soup.new_tag('div')
                hero_div['class'] = 'hero-image'
                hero_div['style'] = f"width: 100%; height: 400px; background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), url('{relative_url}') center/cover; position: relative; margin-top: 0;"
                
                # 在body的第一个子元素前插入hero-image
                body.insert(0, hero_div)
                
                # 写回文件
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                    
                return True, "成功添加头图元素"
            else:
                return False, "找不到合适的位置添加头图元素"
    except Exception as e:
        return False, f"处理文件 {html_path} 时出错: {e}"

def fix_missing_images(json_config, base_dir, language_code):
    """修复所有缺失的头图"""
    fixed_count = 0
    failed_count = 0
    
    for category_key, category_data in json_config['articleCategories'].items():
        base_url = category_data['baseUrl']
        for article in category_data['articles']:
            article_url = article['url'].lstrip('/')
            html_path = os.path.join(base_dir, language_code, article_url)
            
            if os.path.exists(html_path):
                # 检查HTML文件中是否有头图元素
                with open(html_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                soup = BeautifulSoup(content, 'html.parser')
                hero_image = soup.select_one('.hero-image')
                
                if not hero_image:
                    print(f"修复文章: {article['title']} ({article['id']})")
                    print(f"  URL: {article_url}")
                    print(f"  JSON中的图片URL: {article['imageUrl']}")
                    print(f"  HTML中的图片URL: None")
                    
                    success, message = add_hero_image_to_html(html_path, article['imageUrl'])
                    if success:
                        fixed_count += 1
                        print(f"  ✅ {message}")
                    else:
                        failed_count += 1
                        print(f"  ❌ {message}")
    
    return fixed_count, failed_count

def main():
    base_dir = '.'  # 当前目录
    
    # 支持的语言代码
    language_codes = ['en', 'zh', 'ja', 'ko', 'fr', 'de', 'es', 'it', 'pt', 'ru']
    
    for lang_code in language_codes:
        json_config_path = f'android-article-urls-{lang_code}.json'
        
        if not os.path.exists(json_config_path):
            print(f"跳过 {lang_code}，找不到配置文件: {json_config_path}")
            continue
            
        try:
            print(f"\n处理 {lang_code} 语言版本...")
            json_config = load_json_config(json_config_path)
            fixed_count, failed_count = fix_missing_images(json_config, base_dir, lang_code)
            
            print(f"{lang_code} 语言版本修复完成! 成功修复: {fixed_count}, 修复失败: {failed_count}")
        except Exception as e:
            print(f"处理 {lang_code} 语言版本时出错: {e}")

if __name__ == "__main__":
    main()