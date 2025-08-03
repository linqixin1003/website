#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

def update_senior_bird_care_content():
    """
    将正确的老年鸟护理内容更新到所有语言版本的 10-senior-bird-care.html 文件中
    """
    print("🔧 开始更新所有语言版本的 10-senior-bird-care.html 内容...")
    
    # 语言列表
    languages = ['en', 'fr', 'ko', 'de', 'es', 'ru', 'zh', 'it', 'ja', 'pt']
    
    # 检查源文件是否存在
    source_file = 'en/pet-care/09-senior-bird-care.html'
    if not os.path.exists(source_file):
        print(f"⚠️ 源文件 {source_file} 不存在，将创建新的老年鸟护理内容")
        create_senior_bird_care_content()
        return
    
    # 读取源文件内容
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            source_content = f.read()
        print(f"✅ 成功读取源文件 {source_file}")
    except Exception as e:
        print(f"❌ 读取源文件失败: {e}")
        create_senior_bird_care_content()
        return
    
    # 为每种语言更新内容
    for lang in languages:
        target_file = f'{lang}/pet-care/10-senior-bird-care.html'
        
        if os.path.exists(target_file):
            try:
                # 根据语言调整内容
                updated_content = adapt_content_for_language(source_content, lang)
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ {lang}: 成功更新 {target_file}")
            except Exception as e:
                print(f"❌ {lang}: 更新失败 - {e}")
        else:
            print(f"⚠️ {lang}: 文件 {target_file} 不存在")
    
    print("✅ 完成内容更新操作")

def adapt_content_for_language(content, lang):
    """
    根据语言调整内容
    """
    # 语言特定的标题和内容映射
    titles = {
        'en': 'Senior Bird Care',
        'fr': 'Soins des oiseaux âgés',
        'ko': '노령 조류 관리',
        'de': 'Pflege älterer Vögel',
        'es': 'Cuidado de aves mayores',
        'ru': 'Уход за пожилыми птицами',
        'zh': '老年鸟类护理',
        'it': 'Cura degli uccelli anziani',
        'ja': '高齢鳥の世話',
        'pt': 'Cuidados com pássaros idosos'
    }
    
    # 更新语言属性
    content = content.replace('lang="en"', f'lang="{lang}"')
    
    # 更新标题
    if lang in titles:
        # 更新页面标题
        content = content.replace(
            '<title>Senior Bird Care - Pet Care Guide</title>',
            f'<title>{titles[lang]} - Pet Care Guide</title>'
        )
        
        # 更新主标题
        content = content.replace(
            '<h1 class="title">Senior Bird Care</h1>',
            f'<h1 class="title">{titles[lang]}</h1>'
        )
    
    return content

def create_senior_bird_care_content():
    """
    创建新的老年鸟护理内容
    """
    print("🔧 创建新的老年鸟护理内容...")
    
    # 语言列表
    languages = ['en', 'fr', 'ko', 'de', 'es', 'ru', 'zh', 'it', 'ja', 'pt']
    
    # 基础的老年鸟护理内容模板
    base_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Senior Bird Care - Pet Care Guide</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
        }

        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-025.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .title {
            font-size: 24px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 30px;
            margin-top: 15px;
            line-height: 1.3;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #2E8B57;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #2E8B57;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 18px;
            font-weight: 600;
            color: #1b5e20;
            margin-left: 25px;
            line-height: 1.4;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #2E8B57;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .emoji {
            font-size: 18px;
            margin: 0 2px;
        }
        
        @media (max-width: 375px) {
            .content {
                margin: -30px 15px 20px 15px;
                padding: 25px 15px;
            }
            
            .title {
                font-size: 22px;
            }
            
            .main-text {
                font-size: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    
    <div class="content">
        <h1 class="title">Senior Bird Care</h1>
        
        <div class="quote-box">
            <div class="quote-text">
                Aging birds deserve special care and attention to maintain their quality of life in their golden years
            </div>
        </div>
        
        <div class="main-text">
            As birds age, their care needs change significantly. Senior birds require modified environments, adjusted diets, and increased veterinary attention to maintain their health and comfort <span class="emoji">👴</span>. Understanding the aging process in birds and adapting your care approach ensures your feathered companion enjoys their golden years with dignity and comfort.
        </div>

        <div class="section-title">Understanding Bird Aging</div>
        <div class="main-text">
            Birds age differently than mammals, and the aging process varies significantly between species. Recognizing the signs of aging helps you provide appropriate care adjustments <span class="emoji">⏳</span>.
        </div>

        <div class="main-text">
            <strong>When Birds Are Considered Senior:</strong><br>
            • Small birds (budgies, canaries): 5-7 years<br>
            • Medium birds (cockatiels, conures): 10-15 years<br>
            • Large birds (macaws, cockatoos): 20-30 years<br>
            • Very large birds (some parrots): 40+ years
        </div>

        <div class="section-title">Common Age-Related Health Issues</div>
        <div class="main-text">
            Senior birds are prone to specific health conditions that require ongoing management and veterinary care. Early detection and treatment can significantly improve quality of life <span class="emoji">🏥</span>.
        </div>

        <div class="main-text">
            <strong>Common Health Issues:</strong><br>
            • Arthritis and joint problems<br>
            • Heart disease<br>
            • Respiratory issues<br>
            • Digestive problems<br>
            • Vision problems<br>
            • Cognitive changes
        </div>

        <div class="section-title">Environmental Modifications</div>
        <div class="main-text">
            Senior birds benefit from environmental adjustments that accommodate their changing physical abilities and comfort needs <span class="emoji">🏠</span>.
        </div>

        <div class="main-text">
            <strong>Cage Modifications:</strong><br>
            • Lower perch placement for easier access<br>
            • Softer perching materials<br>
            • Multiple food and water stations<br>
            • Warmer environment (75-80°F)<br>
            • Draft-free location<br>
            • Consistent lighting schedule
        </div>

        <div class="section-title">Nutritional Needs for Senior Birds</div>
        <div class="main-text">
            Aging birds often have changing nutritional requirements and may need dietary modifications to maintain health <span class="emoji">🥗</span>.
        </div>

        <div class="main-text">
            <strong>Senior Diet Considerations:</strong><br>
            • Easily digestible foods<br>
            • Higher quality protein sources<br>
            • Softer food textures if needed<br>
            • Smaller, more frequent meals<br>
            • Appropriate supplements as recommended by veterinarian
        </div>

        <div class="section-title">Veterinary Care for Senior Birds</div>
        <div class="main-text">
            Senior birds require more frequent veterinary attention and specialized care approaches <span class="emoji">👨‍⚕️</span>.
        </div>

        <div class="main-text">
            <strong>Recommended Schedule:</strong><br>
            • Semi-annual wellness exams (every 6 months)<br>
            • Annual comprehensive blood work<br>
            • Regular weight monitoring<br>
            • Immediate attention for any changes<br>
            • Pain management consultations when needed
        </div>

        <div class="main-text">
            Caring for a senior bird is both challenging and rewarding. These wise, gentle companions deserve the best care possible in their golden years. With patience, understanding, and appropriate modifications to their care, senior birds can continue to live comfortable, meaningful lives <span class="emoji">✨</span>.
        </div>
    </div>

    <script>
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
        }
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    # 为每种语言创建内容
    for lang in languages:
        target_file = f'{lang}/pet-care/10-senior-bird-care.html'
        
        if os.path.exists(target_file):
            try:
                # 根据语言调整内容
                updated_content = adapt_content_for_language(base_content, lang)
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ {lang}: 成功创建 {target_file}")
            except Exception as e:
                print(f"❌ {lang}: 创建失败 - {e}")
        else:
            print(f"⚠️ {lang}: 文件 {target_file} 不存在")
    
    print("✅ 完成内容创建操作")

if __name__ == "__main__":
    update_senior_bird_care_content()