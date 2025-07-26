#!/usr/bin/env python3
import os
import re
from pathlib import Path

def optimize_es_ecology_for_mobile():
    """对es/ecology目录下的HTML文件进行手机适配"""
    
    ecology_dir = Path('es/ecology')
    if not ecology_dir.exists():
        print("es/ecology 目录不存在")
        return
    
    modified_files = []
    
    # 手机适配的CSS样式
    mobile_css = """
        @media (max-width: 768px) {
            .hero-image {
                height: 250px !important;
            }
            
            .content {
                margin: -20px 10px 20px 10px !important;
                padding: 20px 15px !important;
            }
            
            .title {
                font-size: 20px !important;
                line-height: 1.2 !important;
            }
            
            .main-text {
                font-size: 14px !important;
                line-height: 1.6 !important;
            }
            
            .section-title {
                font-size: 18px !important;
            }
            
            .quote-text {
                font-size: 16px !important;
            }
            
            .tip-title {
                font-size: 14px !important;
            }
            
            img {
                max-width: 100% !important;
                height: auto !important;
            }
            
            .bird-image, .content-image {
                max-width: 100% !important;
                height: auto !important;
                margin: 10px 0 !important;
            }
        }
        
        @media (max-width: 480px) {
            .hero-image {
                height: 200px !important;
            }
            
            .content {
                margin: -15px 8px 15px 8px !important;
                padding: 15px 12px !important;
            }
            
            .title {
                font-size: 18px !important;
            }
            
            .main-text {
                font-size: 13px !important;
            }
            
            .section-title {
                font-size: 16px !important;
            }
        }"""
    
    print("处理 es/ecology 目录下的HTML文件...")
    
    for html_file in ecology_dir.glob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 检查是否已经有手机适配样式
            if '@media (max-width: 768px)' in content:
                print(f"  ⚠️  {html_file} 已经有手机适配样式，跳过")
                continue
            
            # 在</style>标签前添加手机适配CSS
            if '</style>' in content:
                content = content.replace('</style>', mobile_css + '\n        </style>')
            else:
                # 如果没有style标签，在head中添加
                if '</head>' in content:
                    style_block = f'    <style>{mobile_css}\n    </style>\n</head>'
                    content = content.replace('</head>', style_block)
            
            # 确保viewport meta标签存在
            if 'viewport' not in content:
                viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
                if '<meta charset="UTF-8">' in content:
                    content = content.replace('<meta charset="UTF-8">', f'<meta charset="UTF-8">\n    {viewport_meta}')
                elif '<head>' in content:
                    content = content.replace('<head>', f'<head>\n    {viewport_meta}')
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                modified_files.append(str(html_file))
                print(f"  ✅ 已优化: {html_file}")
                
        except Exception as e:
            print(f"  ❌ 处理文件 {html_file} 时出错: {e}")
    
    print(f"\n=== es/ecology 手机适配完成 ===")
    print(f"共修改了 {len(modified_files)} 个文件")
    
    return modified_files

if __name__ == "__main__":
    optimize_es_ecology_for_mobile()