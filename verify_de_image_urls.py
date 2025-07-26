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
            return None
            
        # 检查是否有img标签
        img_tag = hero_image.find('img')
        if img_tag and img_tag.get('src'):
            return img_tag['src']
            
        # 检查背景图片样式
        style = hero_image.get('style')
        if style:
            match = re.search(r'url\([\'"]?(.*?)[\'"]?\)', style)
            if match:
                return match.group(1)
                
        # 检查内联样式
        background_image = None
        for tag in soup.select('[style*="background"]'):
            style = tag.get('style', '')
            if 'url(' in style and '.hero-image' in str(tag):
                match = re.search(r'url\([\'"]?(.*?)[\'"]?\)', style)
                if match:
                    background_image = match.group(1)
                    break
        
        if background_image:
            return background_image
            
        # 查找CSS样式中的背景图片
        style_tags = soup.find_all('style')
        for style_tag in style_tags:
            style_content = style_tag.string
            if style_content and '.hero-image' in style_content:
                match = re.search(r'\.hero-image\s*{[^}]*background[^}]*url\([\'"]?(.*?)[\'"]?\)', style_content)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"处理文件 {html_path} 时出错: {e}")
    
    return None

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

def verify_image_urls(json_config, base_dir):
    """验证所有文章的头图URL"""
    mismatches = []
    
    for category_key, category_data in json_config['articleCategories'].items():
        base_url = category_data['baseUrl']
        for article in category_data['articles']:
            article_url = article['url'].lstrip('/')
            html_path = os.path.join(base_dir, 'de', article_url)
            
            if os.path.exists(html_path):
                html_image_url = extract_image_url_from_html(html_path)
                json_image_url = article['imageUrl']
                
                norm_html_url = normalize_url(html_image_url)
                norm_json_url = normalize_url(json_image_url)
                
                if norm_html_url != norm_json_url:
                    mismatches.append({
                        'article_id': article['id'],
                        'title': article['title'],
                        'url': article_url,
                        'json_image_url': json_image_url,
                        'html_image_url': html_image_url,
                        'normalized_json_url': norm_json_url,
                        'normalized_html_url': norm_html_url
                    })
    
    return mismatches

def main():
    base_dir = '.'  # 当前目录
    json_config_path = 'android-article-urls-de.json'
    
    json_config = load_json_config(json_config_path)
    mismatches = verify_image_urls(json_config, base_dir)
    
    if mismatches:
        print(f"发现 {len(mismatches)} 个头图URL不匹配:")
        for i, mismatch in enumerate(mismatches, 1):
            print(f"\n{i}. 文章: {mismatch['title']} ({mismatch['article_id']})")
            print(f"   URL: {mismatch['url']}")
            print(f"   JSON中的图片URL: {mismatch['json_image_url']}")
            print(f"   HTML中的图片URL: {mismatch['html_image_url']}")
    else:
        print("所有头图URL都匹配!")

if __name__ == "__main__":
    main()