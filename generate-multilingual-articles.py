#!/usr/bin/env python3
"""
生成完整的法语文章内容
基于英语模板生成标准的法语文章
"""

import os
from pathlib import Path

# 文章分类和标题的法语翻译
FRENCH_ARTICLES = {
    'birdwatching': [
        {
            'id': '01',
            'title': 'Commencer l\'observation des oiseaux',
            'content': '''
            <div class="article-hero-image">
                <img src="../images/birds/species/bird-image-011.png" 
                     alt="Commencer l'observation des oiseaux - Belle illustration d'oiseau" 
                     class="hero-image responsive-image" 
                     loading="eager">
            </div>
            
            <div class="article-intro">
                Ce guide complet couvre les bases de l'observation des oiseaux pour les passionnés de tous niveaux.
            </div>
            
            <p class="article-paragraph">Comprendre les fondamentaux de l'observation des oiseaux est essentiel pour une observation réussie.</p>
            
            <div class="article-image">
                <img src="../images/birds/species/bird-image-047.png" 
                     alt="Belle illustration d'oiseau 1" 
                     class="content-image responsive-image" 
                     loading="lazy">
                <p class="image-caption">Figure 1: Bel oiseau dans son habitat naturel</p>
            </div>
            
            <p class="article-paragraph">Les observateurs expérimentés recommandent de se concentrer sur les techniques de base pour améliorer vos compétences d'observation.</p>
            <p class="article-paragraph">La clé pour maîtriser l'observation des oiseaux réside dans une pratique constante et la patience.</p>
            <p class="article-paragraph">La technologie moderne a révolutionné notre approche de l'observation des oiseaux.</p>
            '''
        },
        {
            'id': '02',
            'title': 'Équipement essentiel pour l\'observation des oiseaux',
            'content': '''
            <div class="article-hero-image">
                <img src="../images/birds/species/bird-image-067.png" 
                     alt="Équipement essentiel pour l'observation des oiseaux - Belle illustration d'oiseau" 
                     class="hero-image responsive-image" 
                     loading="eager">
            </div>
            
            <div class="article-intro">
                Découvrez l'équipement essentiel pour commencer votre aventure d'observation des oiseaux.
            </div>
            
            <p class="article-paragraph">Le bon équipement peut considérablement améliorer votre expérience d'observation des oiseaux.</p>
            
            <div class="article-image">
                <img src="../images/birds/species/bird-image-025.png" 
                     alt="Belle illustration d'oiseau 1" 
                     class="content-image responsive-image" 
                     loading="lazy">
                <p class="image-caption">Figure 1: Bel oiseau dans son habitat naturel</p>
            </div>
            
            <p class="article-paragraph">Les jumelles sont l'outil le plus important pour tout observateur d'oiseaux.</p>
            <p class="article-paragraph">Un guide d'identification des oiseaux vous aidera à reconnaître les espèces locales.</p>
            <p class="article-paragraph">Un carnet de notes est essentiel pour enregistrer vos observations.</p>
            '''
        }
    ],
    'scientific-wonders': [
        {
            'id': '01',
            'title': 'Les mécanismes du vol des oiseaux',
            'content': '''
            <div class="article-hero-image">
                <img src="../images/birds/species/bird-image-040.png" 
                     alt="Les mécanismes du vol des oiseaux - Belle illustration d'oiseau" 
                     class="hero-image responsive-image" 
                     loading="eager">
            </div>
            
            <div class="article-intro">
                Explorez les principes scientifiques fascinants derrière le vol des oiseaux.
            </div>
            
            <p class="article-paragraph">Le vol des oiseaux est l'un des phénomènes les plus remarquables de la nature.</p>
            
            <div class="article-image">
                <img src="../images/birds/species/bird-image-015.png" 
                     alt="Belle illustration d'oiseau 1" 
                     class="content-image responsive-image" 
                     loading="lazy">
                <p class="image-caption">Figure 1: Bel oiseau dans son habitat naturel</p>
            </div>
            
            <p class="article-paragraph">Les ailes des oiseaux sont des merveilles d'ingénierie biologique.</p>
            <p class="article-paragraph">La portance et la poussée sont les forces clés qui permettent le vol.</p>
            <p class="article-paragraph">Différentes espèces ont développé des stratégies de vol uniques.</p>
            '''
        }
    ]
}

def create_french_article(category, article_data):
    """创建法语文章文件"""
    
    article_id = article_data['id']
    title = article_data['title']
    content = article_data['content']
    
    html_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - BirdAiSnap</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../knowledge.css">
    <link rel="stylesheet" href="../article-images.css">
    <script src="../language-router.js"></script>
    <script src="../script.js"></script>
    <script src="../image-loader.js"></script>
    <style>
        .article-content {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-top: 2rem;
        }}
        
        .article-header {{
            text-align: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #f0f0f0;
        }}
        
        .category-badge {{
            background: #667eea;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            display: inline-block;
            margin-bottom: 1rem;
        }}
        
        .article-title {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #333;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }}
        
        .article-meta {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            font-size: 0.9rem;
            color: #888;
        }}
        
        .article-body {{
            line-height: 1.8;
            font-size: 1.1rem;
            color: #444;
        }}
        
        .article-intro {{
            font-size: 1.3rem;
            font-weight: 500;
            color: #555;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: #f8f9ff;
            border-left: 4px solid #667eea;
            border-radius: 8px;
        }}
        
        .article-paragraph {{
            margin-bottom: 1.5rem;
            text-align: justify;
        }}
        
        .language-notice {{
            margin-top: 3rem;
            padding: 1rem;
            background: #e8f4f8;
            border-radius: 8px;
            text-align: center;
            font-style: italic;
            color: #666;
        }}
        
        @media (max-width: 768px) {{
            .article-content {{
                margin: 1rem;
                padding: 1.5rem;
            }}
            
            .article-title {{
                font-size: 1.8rem;
            }}
            
            .article-meta {{
                flex-direction: column;
                gap: 0.5rem;
            }}
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <h2><a href="../index.html">BirdAiSnap</a></h2>
            </div>
            <ul class="nav-menu">
                <li><a href="../index.html#home">Accueil</a></li>
                <li><a href="../index.html#features">Fonctionnalités</a></li>
                <li><a href="../index.html#about">À propos</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
                <li><a href="../knowledge.html">Connaissances</a></li>
            </ul>
            <div class="language-switcher">
                <select id="languageSelector" onchange="languageRouter.switchLanguage(this.value)">
                    <option value="en">English</option>
                    <option value="zh">中文</option>
                    <option value="ja">日本語</option>
                    <option value="ko">한국어</option>
                    <option value="de">Deutsch</option>
                    <option value="fr" selected>Français</option>
                    <option value="es">Español</option>
                    <option value="it">Italiano</option>
                    <option value="pt">Português</option>
                    <option value="ru">Русский</option>
                </select>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <section class="article-content">
            <div class="article-header">
                <span class="category-badge">{category.title()}</span>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    <span>Langue: Français</span>
                    <span>Catégorie: {category.title()}</span>
                    <span>Article: {article_id}</span>
                </div>
            </div>
            
            <div class="article-body">
                {content}
                
                <div class="language-notice">
                    <p>Cet article est disponible en plusieurs langues. Utilisez le sélecteur de langue ci-dessus pour changer.</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>BirdAiSnap</h3>
                    <p>Reconnaissance intelligente des oiseaux alimentée par la technologie IA</p>
                </div>
                <div class="footer-section">
                    <h4>Liens rapides</h4>
                    <ul>
                        <li><a href="../index.html">Accueil</a></li>
                        <li><a href="../knowledge.html">Centre de connaissances</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Contact</h4>
                    <p>Email: lingjuetech@gmail.com</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Hangzhou Lingjue Technology Co., Ltd. Tous droits réservés.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    # 创建目录
    fr_dir = Path(f"fr/{category}")
    fr_dir.mkdir(parents=True, exist_ok=True)
    
    # 写入文件
    file_path = fr_dir / f"{article_id}-article.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return file_path

def generate_all_french_articles():
    """生成所有法语文章"""
    
    print("🇫🇷 生成标准法语文章...")
    print("=" * 60)
    
    generated_count = 0
    
    for category, articles in FRENCH_ARTICLES.items():
        print(f"\\n📁 生成分类: {category.upper()}")
        
        for article_data in articles:
            file_path = create_french_article(category, article_data)
            print(f"  ✅ 生成: {file_path}")
            generated_count += 1
    
    print(f"\\n📊 生成完成: {generated_count} 个标准法语文章")

def main():
    print("🚀 开始生成法语文章...")
    print("=" * 60)
    
    generate_all_french_articles()
    
    print("\\n" + "=" * 60)
    print("🎉 法语文章生成完成！")
    print("\\n📋 完成的任务:")
    print("  ✅ 生成了标准格式的法语文章")
    print("  ✅ 包含了本地鸟类图片")
    print("  ✅ 使用了正确的法语内容")
    print("  ✅ 保持了响应式设计")

if __name__ == "__main__":
    main()