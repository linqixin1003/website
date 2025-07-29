#!/usr/bin/env python3
import os

def create_final_articles():
    """创建最后5篇西班牙语生态学文章"""
    
    # 文章模板（简化版）
    template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - BirdAiSnap</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; background: #f8f9fa; padding-bottom: 80px; }}
        .hero-image {{ width: 100%; height: 250px; background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.5)), url('../../images/birds/species/{image}') center/cover; display: flex; align-items: center; justify-content: center; color: white; text-align: center; }}
        .hero-content h1 {{ font-size: 24px; font-weight: 700; margin-bottom: 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }}
        .hero-content p {{ font-size: 16px; opacity: 0.9; }}
        .content {{ background: white; margin: -20px 15px 20px 15px; border-radius: 15px; padding: 25px 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
        .article-meta {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-size: 14px; }}
        .category {{ background: #e3f2fd; color: #1976d2; padding: 4px 12px; border-radius: 20px; font-weight: 500; }}
        .read-time {{ background: #f5f5f5; padding: 4px 12px; border-radius: 20px; color: #666; }}
        .quote-box {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 12px; margin: 20px 0; font-style: italic; }}
        .article-body h3 {{ color: #2c3e50; font-size: 20px; margin: 25px 0 15px 0; font-weight: 600; }}
        .article-body h4 {{ color: #34495e; font-size: 18px; margin: 20px 0 10px 0; font-weight: 600; }}
        .article-body p {{ margin-bottom: 15px; text-align: justify; }}
        .article-body ul {{ margin: 15px 0; padding-left: 20px; }}
        .article-body li {{ margin-bottom: 8px; }}
        .highlight-box {{ background: #f8f9fa; border-left: 4px solid #007bff; padding: 15px; margin: 20px 0; border-radius: 0 8px 8px 0; }}
        .tip-box {{ background: #e8f5e8; border: 1px solid #4caf50; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .warning-box {{ background: #fff3cd; border: 1px solid #ffc107; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .bottom-nav {{ position: fixed; bottom: 0; left: 0; right: 0; background: white; border-top: 1px solid #e0e0e0; display: flex; justify-content: space-around; padding: 8px 0; z-index: 1000; }}
        .nav-item {{ display: flex; flex-direction: column; align-items: center; text-decoration: none; color: #666; font-size: 12px; padding: 4px; }}
        .nav-item.active {{ color: #007bff; }}
        .nav-icon {{ font-size: 20px; margin-bottom: 2px; }}
        @media (max-width: 480px) {{ .hero-image {{ height: 200px; }} .content {{ margin: -15px 10px 15px 10px; padding: 20px 15px; }} .hero-content h1 {{ font-size: 20px; }} }}
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

    # 最后5篇文章数据
    articles = [
        {
            'filename': '06-urban-ecology.html',
            'title': 'Ecología Urbana',
            'subtitle': 'Adaptación a la jungla de concreto',
            'image': 'ecology-06-urban-ecology.webp',
            'read_time': '7 minutos de lectura',
            'quote': 'Las ciudades son nuevos ecosistemas donde las aves más adaptables prosperan.',
            'author': 'Ecólogo Urbano',
            'content': '''
            <h3>🏙️ Aves en la Ciudad</h3>
            <p>Los entornos urbanos presentan desafíos únicos para las aves, pero también nuevas oportunidades. Muchas especies han logrado adaptarse exitosamente a la vida en las ciudades.</p>
            
            <div class="highlight-box">
                <h4>🏠 Adaptaciones Urbanas</h4>
                <ul>
                    <li><strong>Nidificación:</strong> Uso de edificios y estructuras artificiales</li>
                    <li><strong>Alimentación:</strong> Aprovechamiento de desechos y alimentación artificial</li>
                    <li><strong>Comportamiento:</strong> Mayor tolerancia a la presencia humana</li>
                    <li><strong>Comunicación:</strong> Modificación de cantos para superar el ruido urbano</li>
                </ul>
            </div>
            
            <h3>🌳 Espacios Verdes Urbanos</h3>
            <p>Los parques, jardines y áreas verdes son cruciales para la biodiversidad urbana:</p>
            <ul>
                <li><strong>Refugio:</strong> Proporcionan hábitat en medio de la ciudad</li>
                <li><strong>Corredores:</strong> Conectan diferentes áreas verdes</li>
                <li><strong>Recursos:</strong> Ofrecen alimento y agua</li>
                <li><strong>Reproducción:</strong> Sitios seguros para anidar</li>
            </ul>
            '''
        },
        {
            'filename': '07-conservation-biology.html',
            'title': 'Biología de la Conservación',
            'subtitle': 'Ciencia para la protección',
            'image': 'ecology-07-conservation-biology.webp',
            'read_time': '9 minutos de lectura',
            'quote': 'La conservación no es solo proteger especies, es preservar los procesos ecológicos.',
            'author': 'Biólogo Conservacionista',
            'content': '''
            <h3>🛡️ Principios de Conservación</h3>
            <p>La biología de la conservación aplica principios científicos para proteger la biodiversidad aviar y sus ecosistemas.</p>
            
            <div class="warning-box">
                <h4>⚠️ Amenazas Principales</h4>
                <ul>
                    <li><strong>Pérdida de Hábitat:</strong> La mayor amenaza para las aves</li>
                    <li><strong>Cambio Climático:</strong> Alteración de patrones ambientales</li>
                    <li><strong>Especies Invasoras:</strong> Competencia y depredación</li>
                    <li><strong>Contaminación:</strong> Química, acústica y lumínica</li>
                    <li><strong>Sobreexplotación:</strong> Caza y comercio ilegal</li>
                </ul>
            </div>
            
            <h3>📊 Estrategias de Conservación</h3>
            <ul>
                <li><strong>Áreas Protegidas:</strong> Reservas y parques nacionales</li>
                <li><strong>Restauración:</strong> Recuperación de hábitats degradados</li>
                <li><strong>Manejo de Poblaciones:</strong> Programas de cría en cautiverio</li>
                <li><strong>Educación:</strong> Concienciación pública</li>
            </ul>
            '''
        },
        {
            'filename': '08-island-biogeography.html',
            'title': 'Biogeografía Insular',
            'subtitle': 'Evolución en islas aisladas',
            'image': 'ecology-08-island-biogeography.webp',
            'read_time': '8 minutos de lectura',
            'quote': 'Las islas son laboratorios naturales de evolución.',
            'author': 'Biogeógrafo',
            'content': '''
            <h3>🏝️ Características de las Islas</h3>
            <p>Las islas presentan condiciones únicas que influyen en la evolución y distribución de las aves.</p>
            
            <div class="highlight-box">
                <h4>🧬 Procesos Evolutivos</h4>
                <ul>
                    <li><strong>Endemismo:</strong> Especies únicas de cada isla</li>
                    <li><strong>Radiación Adaptativa:</strong> Diversificación rápida</li>
                    <li><strong>Pérdida de Vuelo:</strong> Común en islas sin depredadores</li>
                    <li><strong>Gigantismo/Enanismo:</strong> Cambios de tamaño</li>
                </ul>
            </div>
            
            <h3>⚖️ Teoría de Biogeografía Insular</h3>
            <p>La diversidad de especies en islas depende de:</p>
            <ul>
                <li><strong>Tamaño de la Isla:</strong> Islas más grandes = más especies</li>
                <li><strong>Distancia al Continente:</strong> Islas más cercanas = más colonización</li>
                <li><strong>Equilibrio:</strong> Balance entre inmigración y extinción</li>
            </ul>
            '''
        },
        {
            'filename': '09-pollination-seed-dispersal.html',
            'title': 'Polinización y Dispersión',
            'subtitle': 'Servicios ecosistémicos esenciales',
            'image': 'ecology-09-pollination-seed-dispersal.webp',
            'read_time': '7 minutos de lectura',
            'quote': 'Las aves son jardineros de la naturaleza, plantando bosques.',
            'author': 'Ecólogo de Plantas',
            'content': '''
            <h3>🌸 Polinización por Aves</h3>
            <p>Muchas plantas dependen de las aves para su reproducción sexual a través de la polinización.</p>
            
            <div class="tip-box">
                <h4>🐦 Polinizadores Aviares</h4>
                <ul>
                    <li><strong>Colibríes:</strong> Principales polinizadores en América</li>
                    <li><strong>Suimangas:</strong> Polinizadores en África y Asia</li>
                    <li><strong>Melífagos:</strong> Importantes en Australia</li>
                    <li><strong>Loros:</strong> Polinizadores ocasionales</li>
                </ul>
            </div>
            
            <h3>🌰 Dispersión de Semillas</h3>
            <p>Las aves frugívoras ayudan a las plantas a colonizar nuevos territorios:</p>
            <ul>
                <li><strong>Dispersión a Larga Distancia:</strong> Aves migratorias</li>
                <li><strong>Dispersión Local:</strong> Aves residentes</li>
                <li><strong>Germinación:</strong> Paso por el tracto digestivo mejora germinación</li>
            </ul>
            '''
        },
        {
            'filename': '10-community-dynamics.html',
            'title': 'Dinámicas Comunitarias',
            'subtitle': 'Interacciones complejas en la naturaleza',
            'image': 'ecology-10-community-dynamics.webp',
            'read_time': '8 minutos de lectura',
            'quote': 'Una comunidad de aves es como una orquesta, donde cada especie toca su parte.',
            'author': 'Ecólogo Comunitario',
            'content': '''
            <h3>🎭 Estructura de Comunidades</h3>
            <p>Las comunidades de aves están organizadas por múltiples factores que determinan qué especies coexisten.</p>
            
            <div class="highlight-box">
                <h4>🔗 Factores Estructurales</h4>
                <ul>
                    <li><strong>Diversidad de Hábitats:</strong> Más nichos = más especies</li>
                    <li><strong>Recursos Disponibles:</strong> Alimento, agua, sitios de nidificación</li>
                    <li><strong>Competencia:</strong> Interacciones entre especies similares</li>
                    <li><strong>Depredación:</strong> Presión de depredadores</li>
                </ul>
            </div>
            
            <h3>⚖️ Equilibrio y Cambio</h3>
            <p>Las comunidades aviares son dinámicas y cambian con el tiempo:</p>
            <ul>
                <li><strong>Sucesión:</strong> Cambios predecibles en composición</li>
                <li><strong>Perturbaciones:</strong> Eventos que alteran la comunidad</li>
                <li><strong>Estabilidad:</strong> Resistencia y resilencia a cambios</li>