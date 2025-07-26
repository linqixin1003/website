#!/usr/bin/env python3
import re

def fix_es_flight_mechanics():
    """修复es/scientific-wonders/01-bird-flight-mechanics.html的格式问题"""
    
    file_path = 'es/scientific-wonders/01-bird-flight-mechanics.html'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("修复es/scientific-wonders/01-bird-flight-mechanics.html...")
        
        # 修复HTML结构问题
        # 1. 移除重复的div标签
        content = re.sub(r'<div[^>]*>\s*</div>\s*(?=<!--[^>]*按钮)', '', content)
        
        # 2. 修复不完整的div标签
        content = re.sub(r'</div>\s*<!--[^>]*按钮[^>]*-->', '<!-- 返回按钮 -->', content)
        
        # 3. 确保quote-box结构完整
        content = re.sub(r'(<div class="quote-text">[^<]*)</div>([^<]*<div class="main-text">)', r'\1\2', content)
        
        # 4. 修复缺失的结束标签
        if content.count('<div class="quote-box">') > content.count('</div>'):
            # 在quote-text后添加缺失的结束标签
            content = re.sub(r'(<div class="quote-text">[^<]*)\s*(<div class="main-text">)', r'\1\n        </div>\n        \n        \2', content)
        
        # 5. 清理多余的空行和格式
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 6. 确保正确的HTML结构
        content = re.sub(r'(<div class="quote-text">[^<]*)\s*(<div class="main-text">)', r'\1\n        </div>\n        \n        \2', content)
        
        # 7. 添加手机适配样式
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
        }"""
        
        # 如果还没有手机适配样式，添加它
        if '@media (max-width: 768px)' not in content:
            content = content.replace('</style>', mobile_css + '\n    </style>')
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 已修复格式问题")
        
    except Exception as e:
        print(f"❌ 修复文件时出错: {e}")

if __name__ == "__main__":
    fix_es_flight_mechanics()