import os
import json
import re
from bs4 import BeautifulSoup

def load_json_config(file_path):
    """加载JSON配置文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_image_url_from_html(html_path):
    """从HTML文件中提取头图URL"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # 查找hero-image元素
        hero_image = soup.select_one('.hero-image')
        if not hero_image:
            return None, None, None
            
        # 检查是否有img标签
        img_tag = hero_image.find('img')
        if img_tag and img_tag.get('src'):
            return img_tag['src'], 'img_src', soup
            
        # 检查背景图片样式
        style = hero_image.get('style')
        if style:
            match = re.search(r'url\([\'"]?(.*?)[\'"]?\)', style)
            if match:
                return match.group(1), 'inline_style', soup
                
        # 检查CSS样式中的背景图片
        style_tags = soup.find_all('style')
        for style_tag in style_tags:
            style_content = style_tag.string
            if style_content and '.hero-image' in style_content:
                match = re.search(r'\.hero-image\s*{[^}]*background[^}]*url\([\'"]?(.*?)[\'"]?\)', style_content)
                if match:
                    return match.group(1), 'css_style', soup
    except Exception as e:
        print(f"处理文件 {html_path} 时出错: {e}")
    
    return None, None, None

def normalize_url(url):
    """标准化URL以便比较"""
    if url is None:
        return None
        
    # 移除URL前缀
    url = url.replace('https://linqixin1003.github.io/website/', '')
    url = url.replace('../../', '')
    
    # 修正路径分隔符
    url = url.replace('\\', '/')
    
    # 修正德语特殊字符
    url = url.replace('Vögel', 'birds')
    url = url.replace('Art', 'species')
    url = url.replace('Vogel', 'bird')
    
    return url

def update_html_image_url(html_path, json_image_url, url_type, soup):
    """更新HTML文件中的头图URL"""
    try:
        # 从JSON URL中提取相对路径
        relative_url = json_image_url.replace('https://linqixin1003.github.io/website/', '../../')
        
        if url_type == 'img_src':
            # 更新img标签的src属性
            hero_image = soup.select_one('.hero-image')
            img_tag = hero_image.find('img')
            img_tag['src'] = relative_url
        elif url_type == 'inline_style':
            # 更新内联样式
            hero_image = soup.select_one('.hero-image')
            style = hero_image.get('style', '')
            new_style = re.sub(r'url\([\'"]?.*?[\'"]?\)', f'url(\'{relative_url}\')', style)
            hero_image['style'] = new_style
        elif url_type == 'css_style':
            # 更新CSS样式
            style_tags = soup.find_all('style')
            for style_tag in style_tags:
                if style_tag.string and '.hero-image' in style_tag.string:
                    style_content = style_tag.string
                    new_style = re.sub(
                        r'(\.hero-image\s*{[^}]*background[^}]*url\()[\'"]?.*?[\'"]?(\))', 
                        f'\\1\'{relative_url}\'\\2', 
                        style_content
                    )
                    style_tag.string = new_style
        
        # 写回文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        return True
    except Exception as e:
        print(f"更新文件 {html_path} 时出错: {e}")
        return False

def fix_image_urls(json_config, base_dir):
    """修复所有不匹配的头图URL"""
    fixed_count = 0
    failed_count = 0
    
    for category_key, category_data in json_config['articleCategories'].items():
        base_url = category_data['baseUrl']
        for article in category_data['articles']:
            article_url = article['url'].lstrip('/')
            html_path = os.path.join(base_dir, 'de', article_url)
            
            if os.path.exists(html_path):
                html_image_url, url_type, soup = extract_image_url_from_html(html_path)
                json_image_url = article['imageUrl']
                
                norm_html_url = normalize_url(html_image_url)
                norm_json_url = normalize_url(json_image_url)
                
                if norm_html_url != norm_json_url:
                    print(f"修复文章: {article['title']} ({article['id']})")
                    print(f"  URL: {article_url}")
                    print(f"  JSON中的图片URL: {json_image_url}")
                    print(f"  HTML中的图片URL: {html_image_url}")
                    
                    if url_type and soup:
                        success = update_html_image_url(html_path, json_image_url, url_type, soup)
                        if success:
                            fixed_count += 1
                            print(f"  ✅ 已修复")
                        else:
                            failed_count += 1
                            print(f"  ❌ 修复失败")
                    else:
                        failed_count += 1
                        print(f"  ❌ 无法确定如何修复")
    
    return fixed_count, failed_count

def main():
    base_dir = '.'  # 当前目录
    json_config_path = 'android-article-urls-de.json'
    
    json_config = load_json_config(json_config_path)
    fixed_count, failed_count = fix_image_urls(json_config, base_dir)
    
    print(f"\n修复完成! 成功修复: {fixed_count}, 修复失败: {failed_count}")

if __name__ == "__main__":
    main()