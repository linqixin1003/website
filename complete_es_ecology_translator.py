#!/usr/bin/env python3
import os
import shutil

def create_complete_spanish_ecology_articles():
    """创建完整的西班牙语生态学文章"""
    
    # 确保目录存在
    os.makedirs("es/ecology", exist_ok=True)
    
    articles = {
        "01-habitat-ecosystems.html": {
            "title": "Hábitats y Ecosistemas de Aves - BirdAiSnap",
            "hero_title": "Hábitats y Ecosistemas de Aves",
            "hero_subtitle": "Hogar de vida, piedra angular ecológica",
            "category": "Ecología de Aves",
            "read_time": "8 minutos de lectura",
            "quote": "El hábitat es la base para la supervivencia de las aves, y el ecosistema es el escenario para su reproducción. Proteger el hábitat es proteger el futuro de las aves.",
            "quote_author": "Ecólogo de Aves"
        },
        
        "02-food-webs-chains.html": {
            "title": "Redes y Cadenas Alimentarias - BirdAiSnap", 
            "hero_title": "Redes y Cadenas Alimentarias",
            "hero_subtitle": "Conexiones vitales en los ecosistemas",
            "category": "Ecología de Aves",
            "read_time": "7 minutos de lectura",
            "quote": "Las aves son los hilos que tejen la compleja red de la vida, conectando todos los niveles del ecosistema.",
            "quote_author": "Ecólogo Especialista"
        },
        
        "03-migration-patterns.html": {
            "title": "Patrones de Migración - BirdAiSnap",
            "hero_title": "Patrones de Migración de Aves", 
            "hero_subtitle": "Viajes épicos a través del mundo",
            "category": "Ecología de Aves",
            "read_time": "9 minutos de lectura",
            "quote": "La migración es una de las maravillas más extraordinarias de la naturaleza, un testimonio de la resistencia y navegación de las aves.",
            "quote_author": "Ornitólogo Migratorio"
        },
        
        "04-breeding-ecology.html": {
            "title": "Ecología Reproductiva - BirdAiSnap",
            "hero_title": "Ecología Reproductiva de las Aves",
            "hero_subtitle": "Estrategias para la continuidad de la vida",
            "category": "Ecología de Aves", 
            "read_time": "8 minutos de lectura",
            "quote": "El éxito reproductivo determina el futuro de las especies. Cada estrategia de anidación es una adaptación perfecta al ambiente.",
            "quote_author": "Biólogo Reproductivo"
        },
        
        "05-climate-change-impact.html": {
            "title": "Impacto del Cambio Climático - BirdAiSnap",
            "hero_title": "Impacto del Cambio Climático en las Aves",
            "hero_subtitle": "Desafíos del siglo XXI",
            "category": "Ecología de Aves",
            "read_time": "10 minutos de lectura", 
            "quote": "El cambio climático está reescribiendo las reglas de la supervivencia. Las aves deben adaptarse o enfrentar la extinción.",
            "quote_author": "Climatólogo Aviar"
        },
        
        "06-urban-ecology.html": {
            "title": "Ecología Urbana - BirdAiSnap",
            "hero_title": "Aves en Entornos Urbanos",
            "hero_subtitle": "Adaptación a la jungla de concreto",
            "category": "Ecología de Aves",
            "read_time": "7 minutos de lectura",
            "quote": "Las ciudades son nuevos ecosistemas donde las aves más adaptables prosperan, creando una nueva forma de coexistencia.",
            "quote_author": "Ecólogo Urbano"
        },
        
        "07-conservation-biology.html": {
            "title": "Biología de la Conservación - BirdAiSnap", 
            "hero_title": "Biología de la Conservación de Aves",
            "hero_subtitle": "Ciencia para la protección",
            "category": "Ecología de Aves",
            "read_time": "9 minutos de lectura",
            "quote": "La conservación no es solo proteger especies, es preservar los procesos ecológicos que sustentan la vida en la Tierra.",
            "quote_author": "Biólogo Conservacionista"
        },
        
        "08-island-biogeography.html": {
            "title": "Biogeografía Insular - BirdAiSnap",
            "hero_title": "Biogeografía Insular de las Aves", 
            "hero_subtitle": "Evolución en islas aisladas",
            "category": "Ecología de Aves",
            "read_time": "8 minutos de lectura",
            "quote": "Las islas son laboratorios naturales de evolución, donde las aves desarrollan características únicas en aislamiento.",
            "quote_author": "Biogeógrafo"
        },
        
        "09-pollination-seed-dispersal.html": {
            "title": "Polinización y Dispersión - BirdAiSnap",
            "hero_title": "Polinización y Dispersión de Semillas",
            "hero_subtitle": "Servicios ecosistémicos esenciales", 
            "category": "Ecología de Aves",
            "read_time": "7 minutos de lectura",
            "quote": "Las aves son jardineros de la naturaleza, plantando bosques y manteniendo la diversidad vegetal del planeta.",
            "quote_author": "Ecólogo de Plantas"
        },
        
        "10-community-dynamics.html": {
            "title": "Dinámicas Comunitarias - BirdAiSnap",
            "hero_title": "Dinámicas de Comunidades Aviares",
            "hero_subtitle": "Interacciones complejas en la naturaleza",
            "category": "Ecología de Aves", 
            "read_time": "8 minutos de lectura",
            "quote": "Una comunidad de aves es como una orquesta, donde cada especie toca su parte en la sinfonía de la vida.",
            "quote_author": "Ecólogo Comunitario"
        }
    }
    
    # Plantilla HTML base optimizada para móvil
    html_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
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
        }}
        
        .hero-image {{
            width: 100%;
            height: 250px;
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.5)), 
                        url('../../images/birds/species/{image_name}') center/cover;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            margin-bottom: 20px;
        }}
        
        .hero-overlay {{
            text-align: center;
            color: white;
            padding: 20px;
        }}
        
        .hero-overlay h1 {{
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }}
        
        .hero-overlay h2 {{
            font-size: 16px;
            font-weight: 400;
            opacity: 0.9;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5);
        }}
        
        .content {{
            background: white;
            margin: -20px 15px 20px 15px;
            border-radius: 15px;
            padding: 25px 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            min-height: 80vh;
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
        
        .read-time, .difficulty {{
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
            position: relative;
        }}
        
        .quote-box::before {{
            content: '"';
            font-size: 60px;
            position: absolute;
            top: -10px;
            left: 15px;
            opacity: 0.3;
        }}
        
        .quote-box p {{
            margin-bottom: 10px;
            font-size: 16px;
            line-height: 1.5;
        }}
        
        .quote-box cite {{
            font-size: 14px;
            opacity: 0.8;
        }}
        
        .article-body {{
            font-size: 16px;
            line-height: 1.7;
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
        
        .tip-box h4 {{
            color: #2e7d32;
            margin-bottom: 10px;
        }}
        
        .warning-box {{
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .warning-box h4 {{
            color: #856404;
            margin-bottom: 10px;
        }}
        
        .related-articles {{
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #f0f0f0;
        }}
        
        .related-articles h3 {{
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 20px;
        }}
        
        .article-grid {{
            display: grid;
            gap: 15px;
        }}
        
        .article-card {{
            display: block;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-decoration: none;
            color: inherit;
            transition: transform 0.2s ease;
        }}
        
        .article-card:hover {{
            transform: translateY(-2px);
        }}
        
        .article-card img {{
            width: 100%;
            height: 120px;
            object-fit: cover;
        }}
        
        .article-card-content {{
            padding: 15px;
        }}
        
        .article-card h4 {{
            font-size: 16px;
            margin-bottom: 8px;
            color: #2c3e50;
        }}
        
        .article-card p {{
            font-size: 14px;
            color: #666;
            line-height: 1.4;
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
        
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: rgba(0,0,0,0.1);
            z-index: 1001;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #007bff, #0056b3);
            width: 0%;
            transition: width 0.3s ease;
        }}
        
        @media (max-width: 480px) {{
            .hero-image {{
                height: 200px;
            }}
            
            .content {{
                margin: -15px 10px 15px 10px;
                padding: 20px 15px;
            }}
            
            .hero-overlay h1 {{
                font-size: 20px;
            }}
            
            .hero-overlay h2 {{
                font-size: 14px;
            }}
            
            .article-body {{
                font-size: 15px;
            }}
            
            .article-body h3 {{
                font-size: 18px;
            }}
        }}
        
        /* 添加底部间距避免被导航栏遮挡 */
        body {{
            padding-bottom: 70px;
        }}
    </style>
</head>
<body>
    <!-- 进度条 -->
    <div class="progress-bar">
        <div class="progress-fill"></div>
    </div>

    <!-- 英雄图片 -->
    <div class="hero-image">
        <div class="hero-overlay">
            <h1>{hero_title}</h1>
            <h2>{hero_subtitle}</h2>
        </div>
    </div>

    <!-- 主要内容 -->
    <div class="content">
        <!-- 文章信息 -->
        <div class="article-meta">
            <span class="category">{category}</span>
            <span class="read-time">📖 {read_time}</span>
            <span class="difficulty">🟢 Principiante</span>
        </div>

        <!-- 引用框 -->
        <div class="quote-box">
            <p>{quote}</p>
            <cite>— {quote_author}</cite>
        </div>

        <!-- 文章正文 -->
        <div class="article-body">
            {content}
        </div>

        <!-- 相关文章推荐 -->
        <div class="related-articles">
            <h3>Artículos Relacionados</h3>
            <div class="article-grid">
                {related_articles}
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

    <script>
        // 阅读进度条
        function updateProgress() {{
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {{
                progressFill.style.width = progress + '%';
            }}
        }}
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

    # 文章内容
    article_contents = {
        "01-habitat-ecosystems.html": '''
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

            <h3>🔄 Cambios Estacionales</h3>
            <p>Los hábitats cambian dramáticamente con las estaciones:</p>

            <div class="tip-box">
                <h4>🌸 Primavera - Renovación</h4>
                <p>La vegetación emerge, los insectos se activan y comienza la temporada reproductiva. Las aves migratorias regresan a sus áreas de cría.</p>
            </div>

            <div class="tip-box">
                <h4>☀️ Verano - Abundancia</h4>
                <p>Recursos alimenticios abundantes, actividad reproductiva en su pico, y los polluelos aprenden habilidades de supervivencia.</p>
            </div>

            <div class="tip-box">
                <h4>🍂 Otoño - Preparación</h4>
                <p>Frutos maduros, preparación para la migración, acumulación de reservas de grasa y aumento de comportamientos grupales.</p>
            </div>

            <div class="tip-box">
                <h4>❄️ Invierno - Supervivencia</h4>
                <p>Recursos escasos, calidad del hábitat reducida, competencia intensificada y comportamientos adaptativos reforzados.</p>
            </div>

            <h3>⚠️ Amenazas a los Hábitats</h3>
            <p>Las actividades humanas representan serias amenazas:</p>

            <div class="warning-box">
                <h4>🏗️ Principales Amenazas</h4>
                <ul>
                    <li><strong>Pérdida de Hábitat:</strong> Urbanización y expansión agrícola</li>
                    <li><strong>Fragmentación:</strong> División de hábitats continuos</li>
                    <li><strong>Contaminación:</strong> Química, acústica y lumínica</li>
                    <li><strong>Cambio Climático:</strong> Alteración de patrones ambientales</li>
                    <li><strong>Especies Invasoras:</strong> Competencia y depredación</li>
                    <li><strong>Perturbación Humana:</strong> Turismo y actividades recreativas</li>
                </ul>
            </div>

            <h3>🛡️ Estrategias de Conservación</h3>
            <p>La protección requiere enfoques integrales:</p>

            <h4>🏞️ Áreas Protegidas</h4>
            <ul>
                <li>Establecimiento de reservas naturales y parques nacionales</li>
                <li>Designación de Áreas Importantes para la Conservación de Aves</li>
                <li>Protección de sitios críticos de parada migratoria</li>
                <li>Creación de corredores ecológicos</li>
            </ul>

            <h4>🌱 Restauración Ecológica</h4>
            <ul>
                <li>Conversión de tierras agrícolas a hábitats naturales</li>
                <li>Proyectos de restauración de humedales</li>
                <li>Reforestación y restauración de vegetación nativa</li>
                <li>Restauración de ecosistemas fluviales</li>
            </ul>

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
        ''',
        
        "02-food-webs-chains.html": '''
            <h3>🍽️ Niveles Tróficos de las Aves</h3>
            <p>Las aves ocupan múltiples niveles en las cadenas alimentarias, desde consumidores primarios hasta depredadores tope.</p>

            <div class="highlight-box">
                <h4>🌱 Consumidores Primarios</h4>
                <p>Aves que se alimentan directamente de plantas:</p>
                <ul>
                    <li><strong>Granívoras:</strong> Pinzones, gorriones, palomas</li>
                    <li><strong>Frugívoras:</strong> Tucanes, loros, tordos</li>
                    <li><strong>Nectarívoras:</strong> Colibríes, suimangas, melífagos</li>
                    <li><strong>Folívoras:</strong> Algunas especies de gansos y patos</li>
                </ul>
            </div>

            <h4>🐛 Consumidores Secundarios</h4>
            <p>Aves insectívoras que controlan poblaciones de invertebrados:</p>
            <ul>
                <li><strong>Cazadores Aéreos:</strong> Golondrinas, vencejos, papamoscas</li>
                <li><strong>Buscadores de Corteza:</strong> Pájaros carpinteros, trepatroncos</li>
                <li><strong>Cazadores de Follaje:</strong> Currucas, vireos, reinitas</li>
                <li><strong>Cazadores Terrestres:</strong> Petirrojos, mirlos, zorzales</li>
            </ul>

            <h4>🦅 Consumidores Terciarios</h4>
            <p>Rapaces y otros depredadores especializados:</p>
            <ul>
                <li><strong>Cazadores Diurnos:</strong> Águilas, halcones, azores</li>
                <li><strong>Cazadores Nocturnos:</strong> Búhos, lechuzas, autillos</li>
                <li><strong>Especialistas:</strong> Secretarios, caracaras, serpentarios</li>
            </ul>

            <h3>🔄 Interacciones Complejas</h3>
            <p>Las redes alimentarias son más complejas que las cadenas lineales:</p>

            <div class="tip-box">
                <h4>🤝 Mutualismo</h4>
                <p>Relaciones donde ambas especies se benefician:</p>
                <ul>
                    <li><strong>Aves Limpiadoras:</strong> Garrapateros que limpian mamíferos</li>
                    <li><strong>Polinización:</strong> Colibríes y plantas con flores</li>
                    <li><strong>Dispersión:</strong> Aves frugívoras y plantas con frutos</li>
                </ul>
            </div>

            <h4>⚔️ Competencia</h4>
            <p>Las aves compiten por recursos limitados:</p>
            <ul>
                <li><strong>Competencia Interespecífica:</strong> Entre diferentes especies</li>
                <li><strong>Competencia Intraespecífica:</strong> Dentro de la misma especie</li>
                <li><strong>Partición de Recursos:</strong> Uso de diferentes microhábitats</li>
            </ul>

            <h3>🧬 Adaptaciones para la Alimentación</h3>
            <p>Las aves han desarrollado increíbles adaptaciones:</p>

            <h4>👄 Diversidad de Picos</h4>
            <ul>
                <li><strong>Cónicos:</strong> Para romper semillas (pinzones)</li>
                <li><strong>Curvos:</strong> Para extraer néctar (colibríes)</li>
                <li><strong>Ganchudos:</strong> Para desgarrar carne (rapaces)</li>
                <li><strong>Largos y Finos:</strong> Para sondear (limícolas)</li>
                <li><strong>Anchos y Planos:</strong> Para filtrar (patos)</li>
                <li><strong>Cruzados:</strong> Para extraer semillas de coníferas</li>
            </ul>

            <h4>🏃 Técnicas de Caza</h4>
            <ul>
                <li><strong>Caza al Acecho:</strong> Garzas esperando inmóviles</li>
                <li><strong>Caza en Vuelo:</strong> Halcones persiguiendo presas</li>
                <li><strong>Buceo:</strong> Cormoranes bajo el agua</li>
                <li><strong>Filtración:</strong> Flamencos tamizando agua</li>
                <li><strong>Cooperativa:</strong> Pelícanos cazando en grupo</li>
            </ul>

            <div class="warning-box">
                <h4>⚠️ Impactos Humanos</h4>
                <p>