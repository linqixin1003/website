#!/usr/bin/env python3
import os

def create_spanish_ecology_articles():
    """创建完整的西班牙语生态学文章"""
    
    # 确保目录存在
    os.makedirs("es/ecology", exist_ok=True)
    
    # 文章1: 栖息地与生态系统
    article_01 = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hábitats y Ecosistemas de Aves - BirdAiSnap</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
            padding-bottom: 80px;
        }
        
        .hero-image {
            width: 100%;
            height: 250px;
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.5)), 
                        url('../../images/birds/species/ecology-01-habitat-ecosystems.webp') center/cover;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }
        
        .hero-content h1 {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }
        
        .hero-content p {
            font-size: 16px;
            opacity: 0.9;
        }
        
        .content {
            background: white;
            margin: -20px 15px 20px 15px;
            border-radius: 15px;
            padding: 25px 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .article-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
            font-size: 14px;
        }
        
        .category {
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 500;
        }
        
        .read-time {
            background: #f5f5f5;
            padding: 4px 12px;
            border-radius: 20px;
            color: #666;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            font-style: italic;
        }
        
        .article-body h3 {
            color: #2c3e50;
            font-size: 20px;
            margin: 25px 0 15px 0;
            font-weight: 600;
        }
        
        .article-body h4 {
            color: #34495e;
            font-size: 18px;
            margin: 20px 0 10px 0;
            font-weight: 600;
        }
        
        .article-body p {
            margin-bottom: 15px;
            text-align: justify;
        }
        
        .article-body ul {
            margin: 15px 0;
            padding-left: 20px;
        }
        
        .article-body li {
            margin-bottom: 8px;
        }
        
        .highlight-box {
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }
        
        .tip-box {
            background: #e8f5e8;
            border: 1px solid #4caf50;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        
        .warning-box {
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        
        .related-articles {
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #f0f0f0;
        }
        
        .article-grid {
            display: grid;
            gap: 15px;
        }
        
        .article-card {
            display: block;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-decoration: none;
            color: inherit;
        }
        
        .article-card img {
            width: 100%;
            height: 120px;
            object-fit: cover;
        }
        
        .article-card-content {
            padding: 15px;
        }
        
        .article-card h4 {
            font-size: 16px;
            margin-bottom: 8px;
            color: #2c3e50;
        }
        
        .article-card p {
            font-size: 14px;
            color: #666;
            line-height: 1.4;
        }
        
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-top: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-around;
            padding: 8px 0;
            z-index: 1000;
        }
        
        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #666;
            font-size: 12px;
            padding: 4px;
        }
        
        .nav-item.active {
            color: #007bff;
        }
        
        .nav-icon {
            font-size: 20px;
            margin-bottom: 2px;
        }
        
        @media (max-width: 480px) {
            .hero-image {
                height: 200px;
            }
            
            .content {
                margin: -15px 10px 15px 10px;
                padding: 20px 15px;
            }
            
            .hero-content h1 {
                font-size: 20px;
            }
        }
    </style>
</head>
<body>
    <!-- 英雄图片 -->
    <div class="hero-image">
        <div class="hero-content">
            <h1>Hábitats y Ecosistemas de Aves</h1>
            <p>Hogar de vida, piedra angular ecológica</p>
        </div>
    </div>

    <!-- 主要内容 -->
    <div class="content">
        <!-- 文章信息 -->
        <div class="article-meta">
            <span class="category">Ecología de Aves</span>
            <span class="read-time">📖 8 minutos de lectura</span>
        </div>

        <!-- 引用框 -->
        <div class="quote-box">
            <p>"El hábitat es la base para la supervivencia de las aves, y el ecosistema es el escenario para su reproducción. Proteger el hábitat es proteger el futuro de las aves."</p>
            <cite>— Ecólogo de Aves</cite>
        </div>

        <!-- 文章正文 -->
        <div class="article-body">
            <h3>🏠 ¿Qué es un Hábitat de Aves?</h3>
            <p>Un hábitat es el entorno natural donde las aves viven y se reproducen, incluyendo fuentes de alimento, sitios de anidación, fuentes de agua y refugio. Diferentes especies de aves tienen requisitos de hábitat muy diversos, y esta diversidad crea ricos ecosistemas aviares.</p>

            <div class="highlight-box">
                <h4>🌲 Tipos Principales de Hábitats</h4>
                <ul>
                    <li><strong>Bosques:</strong> Proporcionan recursos alimenticios ricos y sitios de anidación</li>
                    <li><strong>Praderas:</strong> Ambientes abiertos para aves terrestres y rapaces</li>
                    <li><strong>Humedales:</strong> Hábitats críticos para aves acuáticas</li>
                    <li><strong>Montañas:</strong> Distribución vertical con diferentes comunidades</li>
                    <li><strong>Costas:</strong> Zonas de transición entre tierra y mar</li>
                    <li><strong>Desiertos:</strong> Ambientes extremos con adaptaciones especiales</li>
                </ul>
            </div>

            <h3>🌍 Roles de las Aves en los Ecosistemas</h3>
            <p>Las aves desempeñan múltiples roles cruciales en los ecosistemas:</p>

            <h4>🍽️ Como Consumidores</h4>
            <ul>
                <li><strong>Consumidores Primarios:</strong> Aves herbívoras como gansos y palomas</li>
                <li><strong>Consumidores Secundarios:</strong> Aves insectívoras como golondrinas</li>
                <li><strong>Consumidores Terciarios:</strong> Rapaces como águilas y halcones</li>
                <li><strong>Descomponedores:</strong> Aves carroñeras como buitres</li>
            </ul>

            <h4>🌱 Como Proveedores de Servicios</h4>
            <ul>
                <li><strong>Polinización:</strong> Colibríes y nectarínidos polinizan plantas</li>
                <li><strong>Dispersión de Semillas:</strong> Aves frugívoras ayudan a la regeneración forestal</li>
                <li><strong>Control de Plagas:</strong> Aves insectívoras controlan poblaciones de insectos</li>
                <li><strong>Ciclo de Nutrientes:</strong> Los excrementos enriquecen los suelos</li>
            </ul>

            <h3>⚠️ Amenazas a los Hábitats</h3>
            <div class="warning-box">
                <h4>🏗️ Principales Amenazas</h4>
                <ul>
                    <li><strong>Pérdida de Hábitat:</strong> Urbanización y expansión agrícola</li>
                    <li><strong>Fragmentación:</strong> División de hábitats continuos</li>
                    <li><strong>Contaminación:</strong> Química, acústica y lumínica</li>
                    <li><strong>Cambio Climático:</strong> Alteración de patrones ambientales</li>
                    <li><strong>Especies Invasoras:</strong> Competencia y depredación</li>
                </ul>
            </div>

            <h3>🛡️ Estrategias de Conservación</h3>
            <div class="tip-box">
                <h4>🤝 Lo Que Puedes Hacer</h4>
                <ul>
                    <li>Plantar especies nativas en tu jardín</li>
                    <li>Instalar bebederos y comederos para aves</li>
                    <li>Reducir el uso de pesticidas</li>
                    <li>Participar en monitoreo de aves</li>
                    <li>Apoyar proyectos de conservación</li>
                    <li>Educar a otros sobre la importancia de los hábitats</li>
                </ul>
            </div>
        </div>

        <!-- 相关文章推荐 -->
        <div class="related-articles">
            <h3>Artículos Relacionados</h3>
            <div class="article-grid">
                <a href="02-food-webs-chains.html" class="article-card">
                    <img src="../../images/birds/species/ecology-02-food-webs-chains.webp" alt="Redes alimentarias">
                    <div class="article-card-content">
                        <h4>Redes y Cadenas Alimentarias</h4>
                        <p>Comprende las relaciones nutricionales de las aves en los ecosistemas</p>
                    </div>
                </a>
                <a href="07-conservation-biology.html" class="article-card">
                    <img src="../../images/birds/species/ecology-07-conservation-biology.webp" alt="Biología de conservación">
                    <div class="article-card-content">
                        <h4>Biología de la Conservación</h4>
                        <p>Profundiza en los principios científicos de la conservación de aves</p>
                    </div>
                </a>
            </div>
        </div>
    </div>

    <!-- 底部导航 -->
    <nav class="bottom-nav">
        <a href="../ecology.html" class="nav-item">
            <span class="nav-icon">🏠</span>
            <span class="nav-label">Inicio</span>
        </a>
        <a href="../birdwatching.html" class="nav-item">
            <span class="nav-icon">🔍</span>
            <span class="nav-label">Observación</span>
        </a>
        <a href="../knowledge.html" class="nav-item">
            <span class="nav-icon">📚</span>
            <span class="nav-label">Conocimiento</span>
        </a>
        <a href="../ecology.html" class="nav-item active">
            <span class="nav-icon">🌿</span>
            <span class="nav-label">Ecología</span>
        </a>
    </nav>

    <script src="../language-redirect.js"></script>
</body>
</html>'''

    with open("es/ecology/01-habitat-ecosystems.html", "w", encoding="utf-8") as f:
        f.write(article_01)
    
    print("✅ 已创建: 01-habitat-ecosystems.html")

if __name__ == "__main__":
    print("开始创建西班牙语生态学文章...")
    create_spanish_ecology_articles()
    print("完成！")