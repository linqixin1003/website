#!/usr/bin/env python3
"""
更新文章图片脚本
为所有文章添加头图和内容图片，使用本地图片
"""

import json
import os
from pathlib import Path
import random

def load_image_mapping():
    """加载图片映射文件"""
    mapping_file = Path("images/article-image-mapping.json")
    
    if not mapping_file.exists():
        print("❌ 图片映射文件不存在，请先运行 assign-article-images.py")
        return None
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_image_index():
    """加载图片索引"""
    index_file = Path("images/image-index.json")
    
    if not index_file.exists():
        print("❌ 图片索引文件不存在")
        return None
    
    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_random_images(image_index, count=3):
    """获取随机图片用于文章内容"""
    available_images = image_index['images'].copy()
    random.shuffle(available_images)
    return available_images[:count]

def update_article_with_images(file_path, article_info, content_images, language='en'):
    """更新单个文章文件，添加头图和内容图片"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 确定图片路径前缀
        if language == 'en':
            path_prefix = ''
        else:
            path_prefix = '../'
        
        # 头图HTML
        hero_image_path = f"{path_prefix}{article_info['hero_image']}"
        hero_image_html = f'''
        <!-- 文章头图 -->
        <div class="article-hero-image">
            <img src="{hero_image_path}" 
                 alt="{article_info['hero_image_alt']}" 
                 class="hero-image responsive-image" 
                 loading="eager">
        </div>
        '''
        
        # 内容图片HTML
        content_images_html = ""
        for i, img in enumerate(content_images, 1):
            img_path = f"{path_prefix}{img['path']}"
            content_images_html += f'''
        <div class="article-image">
            <img src="{img_path}" 
                 alt="Beautiful bird illustration {i}" 
                 class="content-image responsive-image" 
                 loading="lazy">
            <p class="image-caption">Figure {i}: Beautiful bird in natural habitat</p>
        </div>
        '''
        
        # 查找插入位置
        # 1. 在文章体开始处插入头图
        article_body_start = content.find('<div class="article-body">')
        if article_body_start != -1:
            insert_pos = content.find('>', article_body_start) + 1
            content = content[:insert_pos] + hero_image_html + content[insert_pos:]
        
        # 2. 在文章段落中插入内容图片
        paragraphs = content.split('<p class="article-paragraph">')
        if len(paragraphs) > 3:  # 确保有足够的段落
            # 在第2段后插入第一张图片
            if len(content_images) > 0:
                paragraphs[2] += f'</p>{content_images_html.split("</div>")[0]}</div><p class="article-paragraph">'
            
            # 在第4段后插入第二张图片（如果有）
            if len(content_images) > 1 and len(paragraphs) > 4:
                img_html = content_images_html.split("</div>")[1] + "</div>" if "</div>" in content_images_html.split("</div>")[1] else ""
                if img_html:
                    paragraphs[4] += f'</p>{img_html}<p class="article-paragraph">'
        
        # 重新组合内容
        content = '<p class="article-paragraph">'.join(paragraphs)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"    ❌ 错误: {file_path} - {e}")
        return False

def update_all_articles():
    """更新所有文章"""
    
    # 加载数据
    image_mapping = load_image_mapping()
    image_index = load_image_index()
    
    if not image_mapping or not image_index:
        return
    
    print("🖼️  开始更新所有文章的图片...")
    print("=" * 60)
    
    updated_count = 0
    total_count = 0
    
    # 语言列表
    languages = {
        'en': '',
        'zh': 'zh/',
        'ja': 'ja/',
        'ko': 'ko/',
        'de': 'de/',
        'fr': 'fr/',
        'es': 'es/',
        'it': 'it/',
        'pt': 'pt/',
        'ru': 'ru/'
    }
    
    for category, articles in image_mapping.items():
        print(f"\\n📁 处理分类: {category.upper()}")
        
        for article_id, article_info in articles.items():
            # 为每篇文章获取随机内容图片
            content_images = get_random_images(image_index, 2)
            
            # 更新所有语言版本
            for lang_code, lang_prefix in languages.items():
                if lang_code == 'en':
                    file_path = Path(f"{category}/{article_id}-article.html")
                else:
                    file_path = Path(f"{lang_prefix}{category}/{article_id}-article.html")
                
                if file_path.exists():
                    total_count += 1
                    if update_article_with_images(file_path, article_info, content_images, lang_code):
                        updated_count += 1
                        print(f"  ✅ {file_path}")
                    else:
                        print(f"  ❌ {file_path}")
    
    print(f"\\n📊 更新完成: {updated_count}/{total_count} 个文件")

def create_image_styles():
    """创建图片相关的CSS样式"""
    
    css_content = '''
/* 文章图片样式 */
.article-hero-image {
    width: 100%;
    margin: 0 0 2rem 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
    position: relative;
}

.hero-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
}

.article-hero-image:hover .hero-image {
    transform: scale(1.02);
}

.article-image {
    width: 100%;
    margin: 2rem 0;
    text-align: center;
}

.content-image {
    width: 100%;
    max-width: 600px;
    height: 250px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.content-image:hover {
    transform: scale(1.02);
}

.image-caption {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
}

.responsive-image {
    max-width: 100%;
    height: auto;
}

/* 响应式调整 */
@media (max-width: 768px) {
    .hero-image {
        height: 200px;
    }
    
    .content-image {
        height: 180px;
    }
    
    .article-hero-image {
        margin: 0 0 1.5rem 0;
        border-radius: 8px;
    }
}

@media (max-width: 480px) {
    .hero-image {
        height: 150px;
    }
    
    .content-image {
        height: 120px;
    }
}

/* 打印样式 */
@media print {
    .article-hero-image,
    .article-image {
        page-break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ddd;
    }
    
    .hero-image,
    .content-image {
        height: auto;
        max-height: 200px;
    }
}

/* 图片加载动画 */
.responsive-image {
    opacity: 0;
    transition: opacity 0.3s ease;
}

.responsive-image.loaded {
    opacity: 1;
}

/* 图片懒加载占位符 */
.image-placeholder {
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
'''
    
    css_file = Path("article-images.css")
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"🎨 创建图片样式文件: {css_file}")

def create_image_loading_script():
    """创建图片加载脚本"""
    
    js_content = '''
// 图片加载和懒加载脚本
document.addEventListener('DOMContentLoaded', function() {
    // 图片加载完成处理
    function handleImageLoad(img) {
        img.classList.add('loaded');
        img.style.opacity = '1';
    }
    
    // 图片加载错误处理
    function handleImageError(img) {
        img.src = 'images/ui/placeholders/image-not-found.svg';
        img.alt = 'Image not found';
        img.classList.add('loaded');
    }
    
    // 处理所有图片
    const images = document.querySelectorAll('.responsive-image');
    images.forEach(img => {
        if (img.complete) {
            handleImageLoad(img);
        } else {
            img.addEventListener('load', () => handleImageLoad(img));
            img.addEventListener('error', () => handleImageError(img));
        }
    });
    
    // 懒加载观察器
    if ('IntersectionObserver' in window) {
        const lazyImageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    img.classList.remove('image-placeholder');
                    lazyImageObserver.unobserve(img);
                }
            });
        });
        
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => {
            img.classList.add('image-placeholder');
            lazyImageObserver.observe(img);
        });
    }
});
'''
    
    js_file = Path("image-loader.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"📜 创建图片加载脚本: {js_file}")

def main():
    print("🚀 开始更新文章图片...")
    print("=" * 60)
    
    # 1. 更新所有文章
    update_all_articles()
    
    # 2. 创建样式文件
    create_image_styles()
    
    # 3. 创建加载脚本
    create_image_loading_script()
    
    print("\\n" + "=" * 60)
    print("🎉 文章图片更新完成！")
    print("\\n📋 完成的任务:")
    print("  ✅ 为所有文章添加了头图")
    print("  ✅ 为文章内容添加了配图")
    print("  ✅ 创建了图片样式文件")
    print("  ✅ 生成了图片加载脚本")
    print("\\n💡 下一步建议:")
    print("  - 在文章页面中引入 article-images.css")
    print("  - 在文章页面中引入 image-loader.js")
    print("  - 检查图片显示效果")
    print("  - 优化图片大小以提高加载速度")

if __name__ == "__main__":
    main()