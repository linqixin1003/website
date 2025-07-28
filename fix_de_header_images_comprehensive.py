#!/usr/bin/env python3
"""
综合修复德语文章头图问题
- 统一使用CSS背景图片格式
- 根据映射文件使用正确的图片编号
- 确保与英语版本完全一致
"""

import os
import re
import json

def load_image_mapping():
    """加载图片映射文件"""
    with open('images/article-image-mapping.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_correct_image_number(category, article_num, mapping):
    """根据映射文件获取正确的图片编号"""
    if category in mapping and article_num in mapping[category]:
        filename = mapping[category][article_num]['image_filename']
        # 从 bird-image-XXX.png 提取编号
        match = re.search(r'bird-image-(\d+(?:-alt-\d+)?)', filename)
        if match:
            return match.group(1)
    return None

def fix_header_image_in_file(filepath, correct_image_num):
    """修复单个文件的头图"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 构建正确的图片路径
    correct_image_path = f'../../images/birds/species/bird-image-{correct_image_num}.webp'
    
    # 1. 修复CSS中的背景图片
    css_pattern = r'(\.hero-image\s*{[^}]*background:[^;]*url\([\'"]?)([^\'")]+)([\'"]?\)[^}]*})'
    content = re.sub(css_pattern, rf'\g<1>{correct_image_path}\g<3>', content)
    
    # 2. 修复HTML img标签中的图片
    img_pattern = r'(<img[^>]*src=[\'"])([^\'">]+)([\'"][^>]*>)'
    def replace_img_src(match):
        if 'bird-image-' in match.group(2):
            return f'{match.group(1)}{correct_image_path}{match.group(3)}'
        return match.group(0)
    
    content = re.sub(img_pattern, replace_img_src, content)
    
    # 3. 确保有hero-image div（如果没有则添加）
    if '<div class="hero-image">' not in content and '.hero-image' not in content:
        # 在body标签后添加hero-image
        body_pattern = r'(<body[^>]*>)'
        hero_div = f'''
    <!-- Hero-Bild -->
    <div class="hero-image"></div>
'''
        content = re.sub(body_pattern, rf'\g<1>{hero_div}', content)
        
        # 添加CSS样式
        style_pattern = r'(</style>)'
        hero_css = f'''
        .hero-image {{
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('{correct_image_path}') center/cover;
            position: relative;
            margin-top: 0;
        }}
        '''
        content = re.sub(style_pattern, rf'{hero_css}\g<1>', content)
    
    # 4. 统一使用CSS背景图片格式，移除img标签
    if 'class="hero-image"' in content:
        # 移除hero-image div中的img标签
        hero_img_pattern = r'(<div class="hero-image"[^>]*>)\s*<img[^>]*>\s*(</div>)'
        content = re.sub(hero_img_pattern, r'\g<1>\g<2>', content)
        
        # 确保CSS中有正确的背景图片
        if '.hero-image' in content and 'background:' not in content:
            style_pattern = r'(\.hero-image\s*{[^}]*)(})'
            bg_style = f'''
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('{correct_image_path}') center/cover;
            position: relative;
            margin-top: 0;
            '''
            content = re.sub(style_pattern, rf'\g<1>{bg_style}\g<2>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """主函数"""
    print("🔧 开始综合修复德语文章头图...")
    
    # 加载映射文件
    mapping = load_image_mapping()
    
    # 定义文章类别和对应的目录
    categories = {
        'birdwatching': 'de/birdwatching',
        'scientific-wonders': 'de/scientific-wonders', 
        'pet-care': 'de/pet-care',
        'ecology': 'de/ecology',
        'knowledge': 'de/knowledge'
    }
    
    fixed_count = 0
    total_count = 0
    
    for category, directory in categories.items():
        if not os.path.exists(directory):
            print(f"⚠️  目录不存在: {directory}")
            continue
            
        print(f"\n📁 处理类别: {category}")
        
        # 获取所有HTML文件
        html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
        
        for html_file in sorted(html_files):
            # 提取文章编号
            match = re.search(r'(\d+)-', html_file)
            if not match:
                continue
                
            article_num = match.group(1).zfill(2)  # 确保是两位数
            filepath = os.path.join(directory, html_file)
            
            # 获取正确的图片编号
            correct_image_num = get_correct_image_number(category, article_num, mapping)
            
            if correct_image_num:
                total_count += 1
                try:
                    if fix_header_image_in_file(filepath, correct_image_num):
                        fixed_count += 1
                        print(f"  ✅ {html_file} -> bird-image-{correct_image_num}.webp")
                    else:
                        print(f"  ❌ 修复失败: {html_file}")
                except Exception as e:
                    print(f"  ❌ 错误处理 {html_file}: {e}")
            else:
                print(f"  ⚠️  未找到映射: {html_file}")
    
    print(f"\n🎯 修复完成!")
    print(f"   总文件数: {total_count}")
    print(f"   成功修复: {fixed_count}")
    print(f"   修复率: {fixed_count/total_count*100:.1f}%" if total_count > 0 else "   修复率: 0%")

if __name__ == "__main__":
    main()