#!/usr/bin/env python3
import os
import re

def translate_ecology_articles():
    """完整翻译所有西班牙语生态学文章"""
    
    # 英语到西班牙语的翻译映射
    translations = {
        # 文章1: 栖息地与生态系统
        "01-habitat-ecosystems.html": {
            "title": "Hábitats y Ecosistemas de Aves - BirdAiSnap",
            "header_title": "Hábitats y Ecosistemas de Aves",
            "intro": "Los hábitats de las aves son increíblemente diversos, desde bosques tropicales hasta desiertos áridos, desde humedales hasta montañas alpinas. Cada ecosistema proporciona recursos únicos y presenta desafíos específicos que han moldeado la evolución y adaptación de las especies de aves. Comprender estos hábitats es fundamental para la conservación de las aves y la preservación de la biodiversidad.",
            "content": """
            <h2>Tipos de Hábitats de Aves</h2>
            
            <h3>1. Ecosistemas Forestales</h3>
            <p>Los bosques proporcionan hábitats complejos en múltiples capas para las aves:</p>
            <ul>
                <li><strong>Dosel Superior:</strong> Hogar de especies como águilas, halcones y muchas aves cantoras</li>
                <li><strong>Subdosel:</strong> Refugio para pájaros carpinteros, trepatroncos y algunas especies de loros</li>
                <li><strong>Sotobosque:</strong> Hábitat para tordos, currucas y muchas especies terrestres</li>
                <li><strong>Suelo del Bosque:</strong> Hogar de especies como urogallos, codornices y muchas aves que se alimentan en el suelo</li>
            </ul>
            
            <h3>2. Ecosistemas Acuáticos</h3>
            <p>Los ambientes acuáticos sustentan una rica diversidad de aves:</p>
            <ul>
                <li><strong>Humedales de Agua Dulce:</strong> Patos, gansos, garzas y muchas aves zancudas</li>
                <li><strong>Ambientes Marinos:</strong> Gaviotas, alcatraces, pelícanos y aves marinas</li>
                <li><strong>Costas y Playas:</strong> Playeros, correlimos y otras aves costeras</li>
                <li><strong>Ríos y Arroyos:</strong> Martín pescador, lavanderas y aves ribereñas</li>
            </ul>
            
            <h3>3. Ecosistemas de Pastizales</h3>
            <p>Las praderas y sabanas albergan especies especializadas:</p>
            <ul>
                <li><strong>Praderas Templadas:</strong> Alondras, escribanos y aves de pastizal</li>
                <li><strong>Sabanas Tropicales:</strong> Avestruces, secretarios y muchas especies africanas</li>
                <li><strong>Estepas:</strong> Avutardas, sisones y aves adaptadas a ambientes áridos</li>
            </ul>
            
            <h3>4. Ecosistemas Montañosos</h3>
            <p>Las montañas ofrecen gradientes altitudinales únicos:</p>
            <ul>
                <li><strong>Zonas Alpinas:</strong> Perdices nivales, chovas y especies adaptadas al frío</li>
                <li><strong>Bosques Montanos:</strong> Especies endémicas y aves migratorias altitudinales</li>
                <li><strong>Acantilados:</strong> Halcones peregrinos, águilas y aves rupícolas</li>
            </ul>
            
            <h2>Funciones Ecológicas de las Aves</h2>
            
            <h3>Polinización</h3>
            <p>Muchas aves, especialmente colibríes y nectarínidos, son polinizadores importantes de plantas con flores. Su papel es crucial para la reproducción de muchas especies vegetales.</p>
            
            <h3>Dispersión de Semillas</h3>
            <p>Las aves frugívoras ayudan a dispersar semillas a través de sus excrementos, facilitando la regeneración forestal y la colonización de nuevos hábitats por las plantas.</p>
            
            <h3>Control de Plagas</h3>
            <p>Las aves insectívoras consumen enormes cantidades de insectos, ayudando a controlar las poblaciones de plagas y manteniendo el equilibrio ecológico.</p>
            
            <h3>Reciclaje de Nutrientes</h3>
            <p>A través de sus excrementos, las aves transfieren nutrientes entre diferentes ecosistemas, enriqueciendo los suelos y apoyando el crecimiento de las plantas.</p>
            
            <h2>Adaptaciones al Hábitat</h2>
            
            <h3>Adaptaciones Morfológicas</h3>
            <ul>
                <li><strong>Forma del Pico:</strong> Especializada según la dieta y método de alimentación</li>
                <li><strong>Forma de las Alas:</strong> Adaptada al tipo de vuelo y ambiente</li>
                <li><strong>Patas y Garras:</strong> Modificadas según el sustrato y comportamiento</li>
                <li><strong>Plumaje:</strong> Coloración y textura adaptadas al camuflaje y termorregulación</li>
            </ul>
            
            <h3>Adaptaciones Comportamentales</h3>
            <ul>
                <li><strong>Estrategias de Alimentación:</strong> Técnicas especializadas para explotar recursos específicos</li>
                <li><strong>Comportamiento Social:</strong> Formación de bandadas, territorialidad y cooperación</li>
                <li><strong>Patrones de Actividad:</strong> Adaptación a ciclos diurnos, nocturnos o crepusculares</li>
                <li><strong>Migración:</strong> Movimientos estacionales para aprovechar recursos temporales</li>
            </ul>
            
            <h2>Amenazas a los Hábitats</h2>
            
            <h3>Pérdida de Hábitat</h3>
            <p>La deforestación, urbanización y conversión de tierras para agricultura son las principales causas de pérdida de hábitat para las aves.</p>
            
            <h3>Fragmentación</h3>
            <p>La división de hábitats continuos en parches pequeños y aislados afecta negativamente a muchas especies de aves, especialmente a las que requieren territorios grandes.</p>
            
            <h3>Contaminación</h3>
            <p>La contaminación química, acústica y lumínica puede alterar los comportamientos naturales de las aves y afectar su supervivencia y reproducción.</p>
            
            <h3>Cambio Climático</h3>
            <p>Los cambios en temperatura y patrones de precipitación están alterando la distribución de hábitats y forzando a las aves a adaptarse o migrar.</p>
            
            <h2>Conservación de Hábitats</h2>
            
            <h3>Áreas Protegidas</h3>
            <p>El establecimiento de parques nacionales, reservas naturales y áreas de conservación es fundamental para proteger los hábitats críticos de las aves.</p>
            
            <h3>Corredores Ecológicos</h3>
            <p>La creación de corredores que conecten hábitats fragmentados permite el movimiento de aves y el intercambio genético entre poblaciones.</p>
            
            <h3>Restauración de Hábitats</h3>
            <p>Los proyectos de restauración pueden recuperar hábitats degradados y crear nuevas oportunidades para las especies de aves.</p>
            
            <h3>Manejo Sostenible</h3>
            <p>La implementación de prácticas de manejo sostenible en tierras agrícolas y forestales puede beneficiar tanto a las actividades humanas como a la conservación de aves.</p>
            """
        },
        
        # 文章2: 食物网与食物链
        "02-food-webs-chains.html": {
            "title": "Redes y Cadenas Alimentarias de Aves - BirdAiSnap",
            "header_title": "Redes y Cadenas Alimentarias de Aves",
            "intro": "Las aves ocupan posiciones cruciales en las redes alimentarias de los ecosistemas, actuando como depredadores, presas y enlaces vitales entre diferentes niveles tróficos. Su diversidad dietética y estrategias de alimentación las convierten en componentes esenciales para el funcionamiento y estabilidad de los ecosistemas. Comprender estas relaciones alimentarias es fundamental para la conservación y el manejo de ecosistemas.",
            "content": """
            <h2>Niveles Tróficos de las Aves</h2>
            
            <h3>1. Productores Primarios y Aves</h3>
            <p>Aunque las aves no son productores primarios, muchas especies dependen directamente de la vegetación:</p>
            <ul>
                <li><strong>Granívoras:</strong> Se alimentan de semillas y granos</li>
                <li><strong>Frugívoras:</strong> Consumen frutas y bayas</li>
                <li><strong>Nectarívoras:</strong> Se alimentan del néctar de las flores</li>
                <li><strong>Folívoras:</strong> Algunas especies consumen hojas y brotes</li>
            </ul>
            
            <h3>2. Consumidores Primarios</h3>
            <p>Las aves herbívoras actúan como consumidores primarios:</p>
            <ul>
                <li><strong>Patos y Gansos:</strong> Consumen plantas acuáticas y terrestres</li>
                <li><strong>Perdices y Codornices:</strong> Se alimentan de semillas, hojas y brotes</li>
                <li><strong>Palomas:</strong> Principalmente granívoras</li>
                <li><strong>Loros:</strong> Consumen frutas, semillas y néctar</li>
            </ul>
            
            <h3>3. Consumidores Secundarios</h3>
            <p>Las aves insectívoras y algunas omnívoras:</p>
            <ul>
                <li><strong>Pájaros Cantores:</strong> Muchas especies se alimentan principalmente de insectos</li>
                <li><strong>Golondrinas:</strong> Especializadas en capturar insectos en vuelo</li>
                <li><strong>Pájaros Carpinteros:</strong> Se alimentan de larvas de insectos en la madera</li>
                <li><strong>Currucas y Vireos:</strong> Buscan insectos en el follaje</li>
            </ul>
            
            <h3>4. Consumidores Terciarios</h3>
            <p>Las aves rapaces y otros depredadores especializados:</p>
            <ul>
                <li><strong>Águilas:</strong> Depredan mamíferos medianos y otras aves</li>
                <li><strong>Halcones:</strong> Especializados en cazar otras aves</li>
                <li><strong>Búhos:</strong> Depredadores nocturnos de roedores y aves pequeñas</li>
                <li><strong>Secretarios:</strong> Cazan serpientes y otros reptiles</li>
            </ul>
            
            <h2>Estrategias de Alimentación</h2>
            
            <h3>Especialización Dietética</h3>
            <p>Muchas aves han desarrollado especializaciones extremas:</p>
            <ul>
                <li><strong>Colibríes:</strong> Especializados en néctar, con picos y lenguas adaptados</li>
                <li><strong>Flamencos:</strong> Filtran pequeños organismos del agua</li>
                <li><strong>Quebrantahuesos:</strong> Especializados en consumir médula ósea</li>
                <li><strong>Ostreros:</strong> Especializados en abrir moluscos</li>
            </ul>
            
            <h3>Generalistas vs. Especialistas</h3>
            <p><strong>Especialistas:</strong></p>
            <ul>
                <li>Mayor eficiencia en la explotación de recursos específicos</li>
                <li>Más vulnerables a cambios ambientales</li>
                <li>Menor competencia interespecífica</li>
            </ul>
            
            <p><strong>Generalistas:</strong></p>
            <ul>
                <li>Mayor flexibilidad dietética</li>
                <li>Mejor adaptación a cambios ambientales</li>
                <li>Mayor competencia pero también más oportunidades</li>
            </ul>
            
            <h3>Técnicas de Caza y Alimentación</h3>
            <ul>
                <li><strong>Caza al Acecho:</strong> Garzas esperando inmóviles a sus presas</li>
                <li><strong>Caza en Vuelo:</strong> Halcones persiguiendo a sus presas</li>
                <li><strong>Buceo:</strong> Somormujos y cormoranes bajo el agua</li>
                <li><strong>Filtración:</strong> Patos tamizando el agua</li>
                <li><strong>Sondeo:</strong> Aves limícolas buscando en el lodo</li>
            </ul>
            
            <h2>Interacciones Tróficas Complejas</h2>
            
            <h3>Competencia Interespecífica</h3>
            <p>Las aves compiten por recursos limitados:</p>
            <ul>
                <li><strong>Competencia por Alimento:</strong> Especies con dietas similares</li>
                <li><strong>Competencia por Sitios de Nidificación:</strong> Cavidades y territorios</li>
                <li><strong>Partición de Recursos:</strong> Uso de diferentes microhábitats</li>
            </ul>
            
            <h3>Mutualismo y Comensalismo</h3>
            <ul>
                <li><strong>Aves Limpiadoras:</strong> Garrapateros que limpian mamíferos grandes</li>
                <li><strong>Seguimiento de Hormigas:</strong> Aves que siguen columnas de hormigas legionarias</li>
                <li><strong>Asociaciones con Mamíferos:</strong> Aves que se benefician de mamíferos pastoreadores</li>
            </ul>
            
            <h3>Cascadas Tróficas</h3>
            <p>Los cambios en las poblaciones de aves pueden tener efectos en cascada:</p>
            <ul>
                <li><strong>Pérdida de Depredadores:</strong> Aumento de presas y efectos en niveles inferiores</li>
                <li><strong>Introducción de Especies:</strong> Alteración de redes alimentarias establecidas</li>
                <li><strong>Cambios Estacionales:</strong> Migración que altera dinámicas locales</li>
            </ul>
            
            <h2>Adaptaciones Morfológicas para la Alimentación</h2>
            
            <h3>Diversidad de Picos</h3>
            <ul>
                <li><strong>Picos Cónicos:</strong> Para romper semillas (pinzones, gorriones)</li>
                <li><strong>Picos Curvos:</strong> Para extraer néctar (colibríes)</li>
                <li><strong>Picos Ganchudos:</strong> Para desgarrar carne (rapaces)</li>
                <li><strong>Picos Largos y Finos:</strong> Para sondear (aves limícolas)</li>
                <li><strong>Picos Anchos:</strong> Para filtrar (patos)</li>
            </ul>
            
            <h3>Adaptaciones Digestivas</h3>
            <ul>
                <li><strong>Buche:</strong> Para almacenar alimento temporalmente</li>
                <li><strong>Molleja:</strong> Para triturar alimentos duros</li>
                <li><strong>Intestinos Largos:</strong> En especies herbívoras para mejor digestión</li>
                <li><strong>Ciegos:</strong> Para fermentación en algunas especies</li>
            </ul>
            
            <h2>Impacto Humano en las Redes Alimentarias</h2>
            
            <h3>Alteración de Hábitats</h3>
            <p>Los cambios en el uso del suelo afectan las redes alimentarias:</p>
            <ul>
                <li>Pérdida de especies de plantas nativas</li>
                <li>Reducción de poblaciones de insectos</li>
                <li>Fragmentación de cadenas alimentarias</li>
            </ul>
            
            <h3>Introducción de Especies Invasoras</h3>
            <ul>
                <li>Competencia con especies nativas</li>
                <li>Depredación de especies no adaptadas</li>
                <li>Alteración de relaciones coevolutivas</li>
            </ul>
            
            <h3>Contaminación</h3>
            <ul>
                <li><strong>Pesticidas:</strong> Reducción de poblaciones de insectos</li>
                <li><strong>Bioacumulación:</strong> Concentración de toxinas en depredadores</li>
                <li><strong>Contaminación Acuática:</strong> Afecta a aves acuáticas y sus presas</li>
            </ul>
            
            <h2>Conservación de Redes Alimentarias</h2>
            
            <h3>Enfoque Ecosistémico</h3>
            <p>La conservación debe considerar toda la red alimentaria:</p>
            <ul>
                <li>Protección de especies clave</li>
                <li>Mantenimiento de la diversidad trófica</li>
                <li>Conservación de hábitats diversos</li>
            </ul>
            
            <h3>Restauración Ecológica</h3>
            <ul>
                <li>Reintroducción de especies nativas</li>
                <li>Control de especies invasoras</li>
                <li>Restauración de hábitats degradados</li>
            </ul>
            """
        }
    }
    
    # 处理每个文章
    for filename, translation in translations.items():
        file_path = f"es/ecology/{filename}"
        
        # 读取英语版本作为模板
        en_file_path = f"en/ecology/{filename}"
        if os.path.exists(en_file_path):
            with open(en_file_path, 'r', encoding='utf-8') as f:
                template = f.read()
            
            # 替换内容
            translated_content = template
            
            # 替换标题
            translated_content = re.sub(
                r'<title[^>]*>.*?</title>',
                f'<title>{translation["title"]}</title>',
                translated_content,
                flags=re.DOTALL
            )
            
            # 替换头部标题
            translated_content = re.sub(
                r'<h1[^>]*class="hero-title"[^>]*>.*?</h1>',
                f'<h1 class="hero-title">{translation["header_title"]}</h1>',
                translated_content,
                flags=re.DOTALL
            )
            
            # 替换介绍文本
            translated_content = re.sub(
                r'<p class="intro-text">.*?</p>',
                f'<p class="intro-text">{translation["intro"]}</p>',
                translated_content,
                flags=re.DOTALL
            )
            
            # 替换主要内容
            content_start = translated_content.find('<div class="content-section">')
            content_end = translated_content.find('</div>', content_start)
            
            if content_start != -1 and content_end != -1:
                before_content = translated_content[:content_start]
                after_content = translated_content[content_end:]
                
                new_content = f'<div class="content-section">\n{translation["content"]}\n'
                translated_content = before_content + new_content + after_content
            
            # 写入文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            print(f"✅ 已翻译: {filename}")
        else:
            print(f"❌ 英语模板不存在: {en_file_path}")

if __name__ == "__main__":
    print("开始翻译西班牙语生态学文章...")
    translate_ecology_articles()
    print("翻译完成！")