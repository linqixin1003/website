#!/usr/bin/env python3
import os

def create_remaining_articles():
    """创建剩余的西班牙语生态学文章"""
    
    # 文章模板
    template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - BirdAiSnap</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
            padding-bottom: 80px;
        }}
        
        .hero-image {{
            width: 100%;
            height: 250px;
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.5)), 
                        url('../../images/birds/species/{image}') center/cover;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }}
        
        .hero-content h1 {{
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }}
        
        .hero-content p {{
            font-size: 16px;
            opacity: 0.9;
        }}
        
        .content {{
            background: white;
            margin: -20px 15px 20px 15px;
            border-radius: 15px;
            padding: 25px 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .article-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
            font-size: 14px;
        }}
        
        .category {{
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 500;
        }}
        
        .read-time {{
            background: #f5f5f5;
            padding: 4px 12px;
            border-radius: 20px;
            color: #666;
        }}
        
        .quote-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            font-style: italic;
        }}
        
        .article-body h3 {{
            color: #2c3e50;
            font-size: 20px;
            margin: 25px 0 15px 0;
            font-weight: 600;
        }}
        
        .article-body h4 {{
            color: #34495e;
            font-size: 18px;
            margin: 20px 0 10px 0;
            font-weight: 600;
        }}
        
        .article-body p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        .article-body ul {{
            margin: 15px 0;
            padding-left: 20px;
        }}
        
        .article-body li {{
            margin-bottom: 8px;
        }}
        
        .highlight-box {{
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }}
        
        .tip-box {{
            background: #e8f5e8;
            border: 1px solid #4caf50;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .warning-box {{
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .bottom-nav {{
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
        }}
        
        .nav-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: #666;
            font-size: 12px;
            padding: 4px;
        }}
        
        .nav-item.active {{
            color: #007bff;
        }}
        
        .nav-icon {{
            font-size: 20px;
            margin-bottom: 2px;
        }}
        
        @media (max-width: 480px) {{
            .hero-image {{
                height: 200px;
            }}
            
            .content {{
                margin: -15px 10px 15px 10px;
                padding: 20px 15px;
            }}
            
            .hero-content h1 {{
                font-size: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="hero-image">
        <div class="hero-content">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    </div>

    <div class="content">
        <div class="article-meta">
            <span class="category">Ecología de Aves</span>
            <span class="read-time">📖 {read_time}</span>
        </div>

        <div class="quote-box">
            <p>"{quote}"</p>
            <cite>— {author}</cite>
        </div>

        <div class="article-body">
            {content}
        </div>
    </div>

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

    # 文章数据
    articles = [
        {
            'filename': '03-migration-patterns.html',
            'title': 'Patrones de Migración',
            'subtitle': 'Viajes épicos a través del mundo',
            'image': 'ecology-03-migration-patterns.webp',
            'read_time': '9 minutos de lectura',
            'quote': 'La migración es una de las maravillas más extraordinarias de la naturaleza.',
            'author': 'Ornitólogo Migratorio',
            'content': '''
            <h3>🗺️ ¿Qué es la Migración de Aves?</h3>
            <p>La migración es el movimiento estacional regular de las aves entre sus áreas de reproducción y de invernada. Este fenómeno involucra miles de millones de aves cada año y representa una de las adaptaciones más impresionantes del reino animal.</p>
            
            <div class="highlight-box">
                <h4>🌍 Tipos de Migración</h4>
                <ul>
                    <li><strong>Migración Latitudinal:</strong> Norte-Sur siguiendo las estaciones</li>
                    <li><strong>Migración Altitudinal:</strong> Entre diferentes elevaciones</li>
                    <li><strong>Migración Longitudinal:</strong> Este-Oeste siguiendo recursos</li>
                    <li><strong>Migración Parcial:</strong> Solo parte de la población migra</li>
                </ul>
            </div>
            
            <h3>🧭 Navegación y Orientación</h3>
            <p>Las aves utilizan múltiples sistemas de navegación:</p>
            <ul>
                <li><strong>Brújula Solar:</strong> Posición del sol durante el día</li>
                <li><strong>Brújula Estelar:</strong> Constelaciones durante la noche</li>
                <li><strong>Brújula Magnética:</strong> Campo magnético terrestre</li>
                <li><strong>Puntos de Referencia:</strong> Características geográficas</li>
            </ul>
            
            <div class="tip-box">
                <h4>🦅 Rutas Migratorias Principales</h4>
                <ul>
                    <li><strong>Ruta del Atlántico:</strong> Costa este de América</li>
                    <li><strong>Ruta del Pacífico:</strong> Costa oeste de América</li>
                    <li><strong>Ruta Central:</strong> Interior de América del Norte</li>
                    <li><strong>Ruta del Mediterráneo:</strong> Europa-África</li>
                </ul>
            </div>
            '''
        },
        {
            'filename': '04-breeding-ecology.html',
            'title': 'Ecología Reproductiva',
            'subtitle': 'Estrategias para la continuidad de la vida',
            'image': 'ecology-04-breeding-ecology.webp',
            'read_time': '8 minutos de lectura',
            'quote': 'El éxito reproductivo determina el futuro de las especies.',
            'author': 'Biólogo Reproductivo',
            'content': '''
            <h3>🥚 Estrategias Reproductivas</h3>
            <p>Las aves han desarrollado diversas estrategias reproductivas adaptadas a sus ambientes y estilos de vida.</p>
            
            <div class="highlight-box">
                <h4>🏠 Tipos de Nidos</h4>
                <ul>
                    <li><strong>Nidos en Copa:</strong> Forma clásica en árboles y arbustos</li>
                    <li><strong>Nidos en Cavidad:</strong> Huecos en árboles o acantilados</li>
                    <li><strong>Nidos en Plataforma:</strong> Estructuras planas y abiertas</li>
                    <li><strong>Nidos en el Suelo:</strong> Depresiones simples o elaboradas</li>
                </ul>
            </div>
            
            <h3>👶 Cuidado Parental</h3>
            <p>El cuidado de las crías varía enormemente entre especies:</p>
            <ul>
                <li><strong>Especies Altriciales:</strong> Polluelos nacen indefensos</li>
                <li><strong>Especies Precociales:</strong> Polluelos nacen desarrollados</li>
                <li><strong>Cuidado Biparental:</strong> Ambos padres cuidan las crías</li>
                <li><strong>Cuidado Cooperativo:</strong> Ayudantes asisten a los padres</li>
            </ul>
            '''
        },
        {
            'filename': '05-climate-change-impact.html',
            'title': 'Impacto del Cambio Climático',
            'subtitle': 'Desafíos del siglo XXI',
            'image': 'ecology-05-climate-change-impact.webp',
            'read_time': '10 minutos de lectura',
            'quote': 'El cambio climático está reescribiendo las reglas de la supervivencia.',
            'author': 'Climatólogo Aviar',
            'content': '''
            <h3>🌡️ Efectos del Calentamiento Global</h3>
            <p>El cambio climático afecta a las aves de múltiples maneras:</p>
            
            <div class="warning-box">
                <h4>⚠️ Principales Impactos</h4>
                <ul>
                    <li><strong>Cambios en Distribución:</strong> Desplazamiento hacia los polos</li>
                    <li><strong>Alteración de Migraciones:</strong> Cambios en timing y rutas</li>
                    <li><strong>Pérdida de Hábitat:</strong> Especialmente en zonas costeras</li>
                    <li><strong>Desincronización:</strong> Desajuste con recursos alimenticios</li>
                </ul>
            </div>
            
            <h3>🔄 Adaptaciones y Respuestas</h3>
            <p>Las aves responden al cambio climático de varias formas:</p>
            <ul>
                <li><strong>Cambios Comportamentales:</strong> Modificación de patrones migratorios</li>
                <li><strong>Cambios Fisiológicos:</strong> Adaptación a nuevas temperaturas</li>
                <li><strong>Cambios Evolutivos:</strong> Selección de características favorables</li>
            </ul>
            '''
        }
    ]
    
    # Crear cada artículo
    for article in articles:
        content = template.format(**article)
        filepath = f"es/ecology/{article['filename']}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已创建: {article['filename']}")

if __name__ == "__main__":
    print("开始创建剩余的西班牙语生态学文章...")
    create_remaining_articles()
    print("完成！")