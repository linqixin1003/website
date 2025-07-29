#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

def create_spanish_content():
    """创建完整的西班牙语内容"""
    return '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hábitats y Ecosistemas - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Hábitats y Ecosistemas</h1>
        <div class="quote-box">
            <div class="quote-text">Explorando las complejas relaciones ecológicas de la naturaleza</div>
        </div>
        <div class="main-text">
            Comprender las complejas relaciones entre las aves y su entorno es crucial para la conservación y el equilibrio ecológico<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">¿Qué es un Hábitat de Aves?</div>
        <div class="main-text">
            Un hábitat es el entorno natural donde las aves viven y se reproducen, incluyendo fuentes de alimento, sitios de anidación, fuentes de agua y refugio. Diferentes aves tienen requisitos de hábitat muy distintos, y esta diversidad crea ricos ecosistemas aviares<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Elementos Esenciales del Hábitat</div>
            Todo hábitat de aves debe proporcionar cuatro elementos básicos: alimento, agua, refugio y sitios de anidación adecuados. La calidad y disponibilidad de estos elementos determina la capacidad de carga del hábitat.
        </div>
        
        <div class="section-title">Hábitats Forestales</div>
        <div class="main-text">
            Los hábitats forestales proporcionan ricos recursos alimentarios y sitios de anidación, apoyando numerosas especies aviares<span class="emoji">🌲</span>. Estos ecosistemas complejos ofrecen múltiples capas verticales que diferentes especies de aves utilizan para alimentarse, anidar y refugiarse.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Bosques de Coníferas</h4>
                <p>Hogar de urogallos, pájaros carpinteros y córvidos que se han adaptado a los árboles de hoja perenne</p>
            </div>
            <div class="habitat-item">
                <h4>Bosques Caducifolios</h4>
                <p>Apoyan a aves cantoras, rapaces y aves trepadoras con cambios estacionales de hojas</p>
            </div>
            <div class="habitat-item">
                <h4>Bosques Mixtos</h4>
                <p>Hábitats con la mayor diversidad de especies, combinando beneficios de ambos tipos de bosque</p>
            </div>
        </div>
        
        <div class="section-title">Ecosistemas de Humedales</div>
        <div class="main-text">
            Los hábitats de humedales están entre los ecosistemas más productivos de la Tierra, apoyando una increíble diversidad de aves acuáticas<span class="emoji">💧</span>. Estas áreas sirven como puntos críticos de parada durante la migración y proporcionan terrenos de reproducción esenciales.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Importancia de los Humedales</div>
            Los humedales apoyan más del 40% de todas las especies de aves a pesar de cubrir solo el 6% de la superficie terrestre, haciéndolos cruciales para la conservación global de aves.
        </div>
        
        <div class="section-title">Papel de las Aves en los Ecosistemas</div>
        <div class="main-text">
            Las aves desempeñan múltiples roles en los ecosistemas, sirviendo tanto como consumidores como proveedores de servicios ecosistémicos esenciales<span class="emoji">🌍</span>. Sus diversas estrategias de alimentación y comportamientos crean redes ecológicas complejas que apoyan la biodiversidad.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Roles de Consumidores</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Consumidores Primarios</h5>
                        <p>Aves herbívoras: gansos, patos, palomas</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumidores Secundarios</h5>
                        <p>Aves insectívoras: golondrinas, papamoscas, reyezuelos</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumidores Superiores</h5>
                        <p>Rapaces: halcones, águilas, búhos</p>
                    </div>
                    <div class="role-item">
                        <h5>Asistentes de Descomposición</h5>
                        <p>Aves carroñeras: buitres, cuervos, urracas</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Proveedores de Servicios Ecosistémicos</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Servicios de Polinización</h5>
                        <p>Colibríes, nectarínidos y melífagos polinizan plantas, manteniendo la diversidad vegetal</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Dispersión de Semillas</h5>
                        <p>Las aves frugívoras ayudan a las plantas a dispersar semillas, promoviendo la regeneración forestal</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Control de Plagas</h5>
                        <p>Las aves insectívoras controlan poblaciones de plagas, manteniendo el equilibrio ecológico agrícola y forestal</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Ciclo de Nutrientes</h5>
                        <p>Los excrementos de aves proporcionan nutrientes importantes para los ecosistemas</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Amenazas a los Hábitats</div>
        <div class="main-text">
            Las actividades humanas representan serias amenazas para los hábitats de aves, requiriendo acción de conservación urgente<span class="emoji">⚠️</span>. Entender estas amenazas es el primer paso hacia la protección efectiva del hábitat.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Pérdida de Hábitat</h4>
                <p>La urbanización y expansión agrícola reducen el área de hábitat natural</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Fragmentación del Hábitat</h4>
                <p>Carreteras y edificios dividen hábitats continuos en parches más pequeños</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Contaminación Ambiental</h4>
                <p>La contaminación química y acústica afecta la calidad del hábitat</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Cambio Climático</h4>
                <p>Los cambios en patrones de temperatura y precipitación afectan la idoneidad del hábitat</p>
            </div>
        </div>
        
        <div class="section-title">Estrategias de Conservación</div>
        <div class="main-text">
            Proteger los hábitats de aves requiere estrategias de conservación integrales que aborden múltiples escalas y partes interesadas<span class="emoji">🛡️</span>. La conservación efectiva combina investigación científica, implementación de políticas y participación comunitaria.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Establecimiento de Áreas Protegidas</h4>
                <ul>
                    <li>Establecer reservas naturales y parques nacionales</li>
                    <li>Designar Áreas Importantes para las Aves</li>
                    <li>Proteger sitios críticos de parada migratoria</li>
                    <li>Crear corredores de hábitat para conectar áreas fragmentadas</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Restauración Ecológica</h4>
                <ul>
                    <li>Convertir tierras agrícolas de vuelta a bosques y pastizales</li>
                    <li>Proyectos de restauración de humedales</li>
                    <li>Reforestación artificial y restauración de vegetación</li>
                    <li>Restauración de ecosistemas fluviales</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 Lo que Pueden Hacer los Individuos</h4>
            <ul>
                <li>Plantar especies nativas en patios y jardines</li>
                <li>Instalar bebederos y comederos para aves</li>
                <li>Reducir el uso de pesticidas y fertilizantes</li>
                <li>Participar en actividades de monitoreo y conservación de aves</li>
                <li>Apoyar proyectos de conservación de hábitats</li>
                <li>Crear conciencia ambiental e influir en otros</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_italian_content():
    """创建完整的意大利语内容"""
    return '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habitat e Ecosistemi - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Habitat e Ecosistemi</h1>
        <div class="quote-box">
            <div class="quote-text">Esplorando le complesse relazioni ecologiche della natura</div>
        </div>
        <div class="main-text">
            Comprendere le complesse relazioni tra gli uccelli e il loro ambiente è cruciale per la conservazione e l'equilibrio ecologico<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">Cos'è un Habitat degli Uccelli</div>
        <div class="main-text">
            Un habitat è l'ambiente naturale dove gli uccelli vivono e si riproducono, incluse le fonti di cibo, i siti di nidificazione, le fonti d'acqua e il riparo. Diversi uccelli hanno requisiti di habitat molto diversi, e questa diversità crea ricchi ecosistemi aviari<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Elementi Essenziali dell'Habitat</div>
            Ogni habitat degli uccelli deve fornire quattro elementi base: cibo, acqua, riparo e siti di nidificazione adatti. La qualità e disponibilità di questi elementi determina la capacità portante dell'habitat.
        </div>
        
        <div class="section-title">Habitat Forestali</div>
        <div class="main-text">
            Gli habitat forestali forniscono ricche risorse alimentari e siti di nidificazione, supportando numerose specie aviarie<span class="emoji">🌲</span>. Questi ecosistemi complessi offrono molteplici strati verticali che diverse specie di uccelli utilizzano per nutrirsi, nidificare e ripararsi.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Foreste di Conifere</h4>
                <p>Casa di tetraonidi, picchi e corvidi che si sono adattati agli alberi sempreverdi</p>
            </div>
            <div class="habitat-item">
                <h4>Foreste Decidue</h4>
                <p>Supportano uccelli canori, rapaci e uccelli rampicanti con cambiamenti stagionali delle foglie</p>
            </div>
            <div class="habitat-item">
                <h4>Foreste Miste</h4>
                <p>Habitat con la più alta diversità di specie, combinando i benefici di entrambi i tipi di foresta</p>
            </div>
        </div>
        
        <div class="section-title">Ecosistemi delle Zone Umide</div>
        <div class="main-text">
            Gli habitat delle zone umide sono tra gli ecosistemi più produttivi della Terra, supportando un'incredibile diversità di uccelli acquatici<span class="emoji">💧</span>. Queste aree servono come punti di sosta critici durante la migrazione e forniscono terreni di riproduzione essenziali.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Importanza delle Zone Umide</div>
            Le zone umide supportano oltre il 40% di tutte le specie di uccelli nonostante coprano solo il 6% della superficie terrestre, rendendole cruciali per la conservazione globale degli uccelli.
        </div>
        
        <div class="section-title">Ruolo degli Uccelli negli Ecosistemi</div>
        <div class="main-text">
            Gli uccelli svolgono ruoli multipli negli ecosistemi, servendo sia come consumatori che come fornitori di servizi ecosistemici essenziali<span class="emoji">🌍</span>. Le loro diverse strategie alimentari e comportamenti creano reti ecologiche complesse che supportano la biodiversità.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Ruoli di Consumatori</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Consumatori Primari</h5>
                        <p>Uccelli erbivori: oche, anatre, piccioni</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumatori Secondari</h5>
                        <p>Uccelli insettivori: rondini, pigliamosche, scriccioli</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumatori Superiori</h5>
                        <p>Rapaci: falchi, aquile, gufi</p>
                    </div>
                    <div class="role-item">
                        <h5>Assistenti Decompositori</h5>
                        <p>Uccelli spazzini: avvoltoi, corvi, gazze</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Fornitori di Servizi Ecosistemici</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Servizi di Impollinazione</h5>
                        <p>Colibrì, nettarinidi e mellifagi impollinano le piante, mantenendo la diversità vegetale</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Dispersione dei Semi</h5>
                        <p>Gli uccelli frugivori aiutano le piante a disperdere i semi, promuovendo la rigenerazione forestale</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Controllo dei Parassiti</h5>
                        <p>Gli uccelli insettivori controllano le popolazioni di parassiti, mantenendo l'equilibrio ecologico agricolo e forestale</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Ciclo dei Nutrienti</h5>
                        <p>Gli escrementi degli uccelli forniscono nutrienti importanti per gli ecosistemi</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Minacce agli Habitat</div>
        <div class="main-text">
            Le attività umane rappresentano serie minacce agli habitat degli uccelli, richiedendo azioni di conservazione urgenti<span class="emoji">⚠️</span>. Comprendere queste minacce è il primo passo verso una protezione efficace dell'habitat.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Perdita di Habitat</h4>
                <p>L'urbanizzazione e l'espansione agricola riducono l'area di habitat naturale</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Frammentazione dell'Habitat</h4>
                <p>Strade e edifici dividono habitat continui in patch più piccole</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Inquinamento Ambientale</h4>
                <p>L'inquinamento chimico e acustico influisce sulla qualità dell'habitat</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Cambiamento Climatico</h4>
                <p>I cambiamenti nei modelli di temperatura e precipitazioni influenzano l'idoneità dell'habitat</p>
            </div>
        </div>
        
        <div class="section-title">Strategie di Conservazione</div>
        <div class="main-text">
            Proteggere gli habitat degli uccelli richiede strategie di conservazione complete che affrontino scale multiple e parti interessate<span class="emoji">🛡️</span>. La conservazione efficace combina ricerca scientifica, implementazione di politiche e coinvolgimento della comunità.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Istituzione di Aree Protette</h4>
                <ul>
                    <li>Stabilire riserve naturali e parchi nazionali</li>
                    <li>Designare Aree Importanti per gli Uccelli</li>
                    <li>Proteggere siti critici di sosta migratoria</li>
                    <li>Creare corridoi di habitat per connettere aree frammentate</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Restauro Ecologico</h4>
                <ul>
                    <li>Convertire terreni agricoli in foreste e praterie</li>
                    <li>Progetti di restauro delle zone umide</li>
                    <li>Riforestazione artificiale e restauro della vegetazione</li>
                    <li>Restauro degli ecosistemi fluviali</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 Cosa Possono Fare gli Individui</h4>
            <ul>
                <li>Piantare specie native in cortili e giardini</li>
                <li>Installare abbeveratoi e mangiatoie per uccelli</li>
                <li>Ridurre l'uso di pesticidi e fertilizzanti</li>
                <li>Partecipare ad attività di monitoraggio e conservazione degli uccelli</li>
                <li>Supportare progetti di conservazione degli habitat</li>
                <li>Creare consapevolezza ambientale e influenzare altri</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_japanese_content():
    """创建完整的日语内容"""
    return '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>生息地と生態系 - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">生息地と生態系</h1>
        <div class="quote-box">
            <div class="quote-text">自然の複雑な生態学的関係を探る</div>
        </div>
        <div class="main-text">
            鳥類とその環境の複雑な関係を理解することは、保全と生態学的バランスにとって重要です<span class="emoji">🌿</span>。
        </div>
        
        <div class="section-title">鳥類の生息地とは</div>
        <div class="main-text">
            生息地とは、鳥類が生活し繁殖する自然環境で、食料源、営巣地、水源、避難場所を含みます。異なる鳥類は非常に異なる生息地要件を持ち、この多様性が豊かな鳥類生態系を作り出します<span class="emoji">🏠</span>。
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 生息地の必須要素</div>
            すべての鳥類生息地は4つの基本要素を提供する必要があります：食料、水、避難場所、適切な営巣地。これらの要素の質と利用可能性が生息地の収容力を決定します。
        </div>
        
        <div class="section-title">森林生息地</div>
        <div class="main-text">
            森林生息地は豊富な食料資源と営巣地を提供し、多数の鳥類種を支えています<span class="emoji">🌲</span>。これらの複雑な生態系は、異なる鳥類種が採餌、営巣、避難に利用する複数の垂直層を提供します。
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>針葉樹林</h4>
                <p>常緑樹に適応したライチョウ、キツツキ、カラス科の鳥類の住処</p>
            </div>
            <div class="habitat-item">
                <h4>落葉樹林</h4>
                <p>季節的な葉の変化とともに鳴禽類、猛禽類、登攀性鳥類を支援</p>
            </div>
            <div class="habitat-item">
                <h4>混交林</h4>
                <p>両方の森林タイプの利点を組み合わせた、最も高い種多様性を持つ生息地</p>
            </div>
        </div>
        
        <div class="section-title">湿地生態系</div>
        <div class="main-text">
            湿地生息地は地球上で最も生産性の高い生態系の一つで、信じられないほど多様な水鳥を支えています<span class="emoji">💧</span>。これらの地域は渡りの際の重要な中継地として機能し、必須の繁殖地を提供します。
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 湿地の重要性</div>
            湿地は地球表面のわずか6%しか占めていないにもかかわらず、全鳥類種の40%以上を支えており、世界的な鳥類保全にとって重要です。
        </div>
        
        <div class="section-title">生態系における鳥類の役割</div>
        <div class="main-text">
            鳥類は生態系で複数の役割を果たし、消費者と重要な生態系サービスの提供者の両方として機能します<span class="emoji">🌍</span>。その多様な摂食戦略と行動は、生物多様性を支える複雑な生態学的ネットワークを作り出します。
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>消費者の役割</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>一次消費者</h5>
                        <p>草食性鳥類：ガン、カモ、ハト</p>
                    </div>
                    <div class="role-item">
                        <h5>二次消費者</h5>
                        <p>昆虫食鳥類：ツバメ、ヒタキ、ミソサザイ</p>
                    </div>
                    <div class="role-item">
                        <h5>高次消費者</h5>
                        <p>猛禽類：タカ、ワシ、フクロウ</p>
                    </div>
                    <div class="role-item">
                        <h5>分解補助者</h5>
                        <p>腐肉食鳥類：ハゲワシ、カラス、カササギ</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>生態系サービスの提供者</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 受粉サービス</h5>
                        <p>ハチドリ、タイヨウチョウ、ミツスイは植物の受粉を助け、植物の多様性を維持します</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 種子散布</h5>
                        <p>果実食鳥類は植物が種子を散布するのを助け、森林再生を促進します</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 害虫駆除</h5>
                        <p>昆虫食鳥類は害虫の個体数を制御し、農業および森林の生態学的バランスを維持します</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 栄養循環</h5>
                        <p>鳥の糞は生態系に重要な栄養素を提供します</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">生息地への脅威</div>
        <div class="main-text">
            人間の活動は鳥類の生息地に深刻な脅威をもたらし、緊急の保全活動が必要です<span class="emoji">⚠️</span>。これらの脅威を理解することが、効果的な生息地保護の第一歩です。
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ 生息地の喪失</h4>
                <p>都市化と農地拡大が自然生息地の面積を減少させます</p>
            </div>
            <div class="threat-item">
                <h4>🧩 生息地の断片化</h4>
                <p>道路や建物が連続した生息地をより小さなパッチに分断します</p>
            </div>
            <div class="threat-item">
                <h4>🏭 環境汚染</h4>
                <p>化学汚染や騒音公害が生息地の質に影響を与えます</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ 気候変動</h4>
                <p>気温と降水パターンの変化が生息地の適性に影響を与えます</p>
            </div>
        </div>
        
        <div class="section-title">保全戦略</div>
        <div class="main-text">
            鳥類の生息地を保護するには、複数のスケールと利害関係者に対応する包括的な保全戦略が必要です<span class="emoji">🛡️</span>。効果的な保全は、科学的研究、政策実施、地域社会の参加を組み合わせます。
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ 保護地域の設立</h4>
                <ul>
                    <li>自然保護区と国立公園を設立する</li>
                    <li>重要野鳥生息地を指定する</li>
                    <li>重要な渡りの中継地を保護する</li>
                    <li>断片化された地域をつなぐ生息地回廊を作成する</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 生態学的復元</h4>
                <ul>
                    <li>農地を森林や草原に戻す</li>
                    <li>湿地復元プロジェクト</li>
                    <li>人工的な再植林と植生回復</li>
                    <li>河川生態系の復元</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 個人ができること</h4>
            <ul>
                <li>庭や庭園に在来種を植える</li>
                <li>鳥の水飲み場や餌台を設置する</li>
                <li>農薬や化学肥料の使用を減らす</li>
                <li>野鳥のモニタリングや保護活動に参加する</li>
                <li>生息地保全プロジェクトを支援する</li>
                <li>環境意識を高め、他者に影響を与える</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_french_content():
    """创建完整的法语内容"""
    return '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habitats et Écosystèmes - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Habitats et Écosystèmes</h1>
        <div class="quote-box">
            <div class="quote-text">Explorer les relations écologiques complexes de la nature</div>
        </div>
        <div class="main-text">
            Comprendre les relations complexes entre les oiseaux et leur environnement est crucial pour la conservation et l'équilibre écologique<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">Qu'est-ce qu'un Habitat d'Oiseau ?</div>
        <div class="main-text">
            Un habitat est l'environnement naturel où les oiseaux vivent et se reproduisent, y compris les sources de nourriture, les sites de nidification, les points d'eau et les abris. Différents oiseaux ont des exigences d'habitat très différentes, et cette diversité crée de riches écosystèmes aviaires<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Éléments Essentiels de l'Habitat</div>
            Chaque habitat d'oiseau doit fournir quatre éléments de base : nourriture, eau, abri et sites de nidification appropriés. La qualité et la disponibilité de ces éléments déterminent la capacité de charge de l'habitat.
        </div>
        
        <div class="section-title">Habitats Forestiers</div>
        <div class="main-text">
            Les habitats forestiers fournissent de riches ressources alimentaires et des sites de nidification, soutenant de nombreuses espèces aviaires<span class="emoji">🌲</span>. Ces écosystèmes complexes offrent de multiples couches verticales que différentes espèces d'oiseaux utilisent pour se nourrir, nicher et s'abriter.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Forêts de Conifères</h4>
                <p>Abritent des tétras, des pics et des corvidés qui se sont adaptés aux arbres à feuilles persistantes</p>
            </div>
            <div class="habitat-item">
                <h4>Forêts de Feuillus</h4>
                <p>Soutiennent les oiseaux chanteurs, les rapaces et les oiseaux grimpeurs avec des changements de feuilles saisonniers</p>
            </div>
            <div class="habitat-item">
                <h4>Forêts Mixtes</h4>
                <p>Habitats avec la plus grande diversité d'espèces, combinant les avantages des deux types de forêts</p>
            </div>
        </div>
        
        <div class="section-title">Écosystèmes des Zones Humides</div>
        <div class="main-text">
            Les habitats des zones humides sont parmi les écosystèmes les plus productifs de la Terre, soutenant une incroyable diversité d'oiseaux aquatiques<span class="emoji">💧</span>. Ces zones servent de haltes migratoires critiques et fournissent des aires de reproduction essentielles.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Importance des Zones Humides</div>
            Les zones humides soutiennent plus de 40 % de toutes les espèces d'oiseaux bien qu'elles ne couvrent que 6 % de la surface terrestre, ce qui les rend cruciales pour la conservation mondiale des oiseaux.
        </div>
        
        <div class="section-title">Rôle des Oiseaux dans les Écosystèmes</div>
        <div class="main-text">
            Les oiseaux jouent de multiples rôles dans les écosystèmes, servant à la fois de consommateurs et de fournisseurs de services écosystémiques essentiels<span class="emoji">🌍</span>. Leurs diverses stratégies alimentaires et comportements créent des réseaux écologiques complexes qui soutiennent la biodiversité.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Rôles des Consommateurs</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Consommateurs Primaires</h5>
                        <p>Oiseaux herbivores : oies, canards, pigeons</p>
                    </div>
                    <div class="role-item">
                        <h5>Consommateurs Secondaires</h5>
                        <p>Oiseaux insectivores : hirondelles, gobemouches, troglodytes</p>
                    </div>
                    <div class="role-item">
                        <h5>Consommateurs Supérieurs</h5>
                        <p>Rapaces : faucons, aigles, hiboux</p>
                    </div>
                    <div class="role-item">
                        <h5>Aides à la Décomposition</h5>
                        <p>Oiseaux nécrophages : vautours, corbeaux, pies</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Fournisseurs de Services Écosystémiques</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Services de Pollinisation</h5>
                        <p>Les colibris, souimangas et méliphages pollinisent les plantes, maintenant la diversité végétale</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Dispersion des Graines</h5>
                        <p>Les oiseaux frugivores aident les plantes à disperser leurs graines, favorisant la régénération des forêts</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Contrôle des Ravageurs</h5>
                        <p>Les oiseaux insectivores contrôlent les populations de ravageurs, maintenant l'équilibre écologique agricole et forestier</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Cycle des Nutriments</h5>
                        <p>Les déjections d'oiseaux fournissent des nutriments importants aux écosystèmes</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Menaces sur les Habitats</div>
        <div class="main-text">
            Les activités humaines représentent de graves menaces pour les habitats des oiseaux, nécessitant une action de conservation urgente<span class="emoji">⚠️</span>. Comprendre ces menaces est la première étape vers une protection efficace de l'habitat.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Perte d'Habitat</h4>
                <p>L'urbanisation et l'expansion agricole réduisent la superficie de l'habitat naturel</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Fragmentation de l'Habitat</h4>
                <p>Les routes et les bâtiments divisent les habitats continus en parcelles plus petites</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Pollution Environnementale</h4>
                <p>La pollution chimique et sonore affecte la qualité de l'habitat</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Changement Climatique</h4>
                <p>Les changements de température et de précipitations affectent l'adéquation de l'habitat</p>
            </div>
        </div>
        
        <div class="section-title">Stratégies de Conservation</div>
        <div class="main-text">
            La protection des habitats d'oiseaux nécessite des stratégies de conservation complètes qui abordent plusieurs échelles et parties prenantes<span class="emoji">🛡️</span>. Une conservation efficace combine la recherche scientifique, la mise en œuvre de politiques et la participation communautaire.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Création de Zones Protégées</h4>
                <ul>
                    <li>Établir des réserves naturelles et des parcs nationaux</li>
                    <li>Désigner des Zones Importantes pour la Conservation des Oiseaux</li>
                    <li>Protéger les haltes migratoires critiques</li>
                    <li>Créer des corridors d'habitat pour relier les zones fragmentées</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Restauration Écologique</h4>
                <ul>
                    <li>Reconvertir des terres agricoles en forêts et prairies</li>
                    <li>Projets de restauration des zones humides</li>
                    <li>Reboisement artificiel et restauration de la végétation</li>
                    <li>Restauration des écosystèmes fluviaux</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 Ce que les Individus Peuvent Faire</h4>
            <ul>
                <li>Planter des espèces indigènes dans les cours et les jardins</li>
                <li>Installer des abreuvoirs et des mangeoires pour oiseaux</li>
                <li>Réduire l'utilisation de pesticides et d'engrais</li>
                <li>Participer à des activités de surveillance et de conservation des oiseaux</li>
                <li>Soutenir les projets de conservation de l'habitat</li>
                <li>Sensibiliser à l'environnement et influencer les autres</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_german_content():
    """创建完整的德语内容"""
    return '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lebensräume und Ökosysteme - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Lebensräume und Ökosysteme</h1>
        <div class="quote-box">
            <div class="quote-text">Erkundung der komplexen ökologischen Beziehungen der Natur</div>
        </div>
        <div class="main-text">
            Das Verständnis der komplexen Beziehungen zwischen Vögeln und ihrer Umwelt ist entscheidend für den Schutz und das ökologische Gleichgewicht<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">Was ist ein Vogellebensraum?</div>
        <div class="main-text">
            Ein Lebensraum ist die natürliche Umgebung, in der Vögel leben und sich vermehren, einschließlich Nahrungsquellen, Nistplätzen, Wasserquellen und Schutz. Verschiedene Vögel haben sehr unterschiedliche Lebensraumanforderungen, und diese Vielfalt schafft reiche Vogelökosysteme<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Wesentliche Elemente des Lebensraums</div>
            Jeder Vogellebensraum muss vier grundlegende Elemente bereitstellen: Nahrung, Wasser, Schutz und geeignete Nistplätze. Die Qualität und Verfügbarkeit dieser Elemente bestimmt die Tragfähigkeit des Lebensraums.
        </div>
        
        <div class="section-title">Waldlebensräume</div>
        <div class="main-text">
            Waldlebensräume bieten reiche Nahrungsressourcen und Nistplätze und unterstützen zahlreiche Vogelarten<span class="emoji">🌲</span>. Diese komplexen Ökosysteme bieten mehrere vertikale Schichten, die verschiedene Vogelarten zum Fressen, Nisten und als Schutz nutzen.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Nadelwälder</h4>
                <p>Heimat von Raufußhühnern, Spechten und Rabenvögeln, die sich an immergrüne Bäume angepasst haben</p>
            </div>
            <div class="habitat-item">
                <h4>Laubwälder</h4>
                <p>Unterstützen Singvögel, Greifvögel und Klettervögel mit saisonalen Blattwechseln</p>
            </div>
            <div class="habitat-item">
                <h4>Mischwälder</h4>
                <p>Lebensräume mit der höchsten Artenvielfalt, die die Vorteile beider Waldtypen kombinieren</p>
            </div>
        </div>
        
        <div class="section-title">Feuchtgebietsökosysteme</div>
        <div class="main-text">
            Feuchtgebietslebensräume gehören zu den produktivsten Ökosystemen der Erde und unterstützen eine unglaubliche Vielfalt an Wasservögeln<span class="emoji">💧</span>. Diese Gebiete dienen als wichtige Rastplätze während des Zugs und bieten wesentliche Brutgebiete.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Bedeutung von Feuchtgebieten</div>
            Feuchtgebiete unterstützen über 40 % aller Vogelarten, obwohl sie nur 6 % der Landoberfläche ausmachen, was sie für den globalen Vogelschutz entscheidend macht.
        </div>
        
        <div class="section-title">Rolle der Vögel in Ökosystemen</div>
        <div class="main-text">
            Vögel spielen vielfältige Rollen in Ökosystemen und dienen sowohl als Verbraucher als auch als Anbieter wesentlicher Ökosystemdienstleistungen<span class="emoji">🌍</span>. Ihre vielfältigen Ernährungsstrategien und Verhaltensweisen schaffen komplexe ökologische Netzwerke, die die Biodiversität unterstützen.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Verbraucherrollen</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Primärverbraucher</h5>
                        <p>Pflanzenfressende Vögel: Gänse, Enten, Tauben</p>
                    </div>
                    <div class="role-item">
                        <h5>Sekundärverbraucher</h5>
                        <p>Insektenfressende Vögel: Schwalben, Fliegenschnäpper, Zaunkönige</p>
                    </div>
                    <div class="role-item">
                        <h5>Spitzenverbraucher</h5>
                        <p>Greifvögel: Falken, Adler, Eulen</p>
                    </div>
                    <div class="role-item">
                        <h5>Zersetzungshelfer</h5>
                        <p>Aasfressende Vögel: Geier, Krähen, Elstern</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Anbieter von Ökosystemdienstleistungen</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Bestäubungsdienste</h5>
                        <p>Kolibris, Nektarvögel und Honigfresser bestäuben Pflanzen und erhalten die Pflanzenvielfalt</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Samenverbreitung</h5>
                        <p>Fruchtfressende Vögel helfen Pflanzen bei der Verbreitung von Samen und fördern die Waldregeneration</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Schädlingsbekämpfung</h5>
                        <p>Insektenfressende Vögel kontrollieren Schädlingspopulationen und erhalten das ökologische Gleichgewicht in Land- und Forstwirtschaft</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Nährstoffkreislauf</h5>
                        <p>Vogelkot liefert wichtige Nährstoffe für Ökosysteme</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Bedrohungen für Lebensräume</div>
        <div class="main-text">
            Menschliche Aktivitäten stellen ernsthafte Bedrohungen für Vogellebensräume dar und erfordern dringende Schutzmaßnahmen<span class="emoji">⚠️</span>. Das Verständnis dieser Bedrohungen ist der erste Schritt zu einem wirksamen Lebensraumschutz.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Lebensraumverlust</h4>
                <p>Urbanisierung und landwirtschaftliche Expansion reduzieren die Fläche natürlicher Lebensräume</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Lebensraumfragmentierung</h4>
                <p>Straßen und Gebäude teilen zusammenhängende Lebensräume in kleinere Parzellen</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Umweltverschmutzung</h4>
                <p>Chemische und Lärmbelästigung beeinträchtigen die Lebensraumqualität</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Klimawandel</h4>
                <p>Änderungen der Temperatur- und Niederschlagsmuster beeinträchtigen die Eignung von Lebensräumen</p>
            </div>
        </div>
        
        <div class="section-title">Schutzstrategien</div>
        <div class="main-text">
            Der Schutz von Vogellebensräumen erfordert umfassende Schutzstrategien, die mehrere Ebenen und Interessengruppen ansprechen<span class="emoji">🛡️</span>. Effektiver Schutz kombiniert wissenschaftliche Forschung, politische Umsetzung und Beteiligung der Gemeinschaft.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Einrichtung von Schutzgebieten</h4>
                <ul>
                    <li>Einrichtung von Naturschutzgebieten und Nationalparks</li>
                    <li>Ausweisung wichtiger Vogelschutzgebiete</li>
                    <li>Schutz kritischer Rastplätze für Zugvögel</li>
                    <li>Schaffung von Lebensraumkorridoren zur Verbindung fragmentierter Gebiete</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Ökologische Wiederherstellung</h4>
                <ul>
                    <li>Umwandlung von Ackerland in Wälder und Grünland</li>
                    <li>Projekte zur Wiederherstellung von Feuchtgebieten</li>
                    <li>Künstliche Aufforstung und Wiederherstellung der Vegetation</li>
                    <li>Wiederherstellung von Flussökosystemen</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 Was Einzelpersonen tun können</h4>
            <ul>
                <li>Einheimische Pflanzen in Höfen und Gärten anbauen</li>
                <li>Vogeltränken und Futterstellen installieren</li>
                <li>Verwendung von Pestiziden und Düngemitteln reduzieren</li>
                <li>An Vogelbeobachtungs- und Schutzaktivitäten teilnehmen</li>
                <li>Lebensraumschutzprojekte unterstützen</li>
                <li>Umweltbewusstsein schaffen und andere beeinflussen</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_portuguese_content():
    """创建完整的葡萄牙语内容"""
    return '''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habitats e Ecossistemas - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Habitats e Ecossistemas</h1>
        <div class="quote-box">
            <div class="quote-text">Explorando as complexas relações ecológicas da natureza</div>
        </div>
        <div class="main-text">
            Compreender as complexas relações entre as aves e seu ambiente é crucial para a conservação e o equilíbrio ecológico<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">O que é um Habitat de Aves?</div>
        <div class="main-text">
            Um habitat é o ambiente natural onde as aves vivem e se reproduzem, incluindo fontes de alimento, locais de nidificação, fontes de água e abrigo. Diferentes aves têm requisitos de habitat muito distintos, e essa diversidade cria ricos ecossistemas aviários<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Elementos Essenciais do Habitat</div>
            Todo habitat de aves deve fornecer quatro elementos básicos: alimento, água, abrigo e locais de nidificação adequados. A qualidade e disponibilidade desses elementos determina a capacidade de suporte do habitat.
        </div>
        
        <div class="section-title">Habitats Florestais</div>
        <div class="main-text">
            Os habitats florestais fornecem ricos recursos alimentares e locais de nidificação, apoiando numerosas espécies de aves<span class="emoji">🌲</span>. Esses ecossistemas complexos oferecem múltiplas camadas verticais que diferentes espécies de aves usam para se alimentar, nidificar e se abrigar.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Florestas de Coníferas</h4>
                <p>Lar de tetrazes, pica-paus e corvídeos que se adaptaram a árvores perenes</p>
            </div>
            <div class="habitat-item">
                <h4>Florestas Decíduas</h4>
                <p>Apoiam aves canoras, aves de rapina e aves trepadeiras com mudanças sazonais de folhas</p>
            </div>
            <div class="habitat-item">
                <h4>Florestas Mistas</h4>
                <p>Habitats com a maior diversidade de espécies, combinando benefícios de ambos os tipos de floresta</p>
            </div>
        </div>
        
        <div class="section-title">Ecossistemas de Zonas Úmidas</div>
        <div class="main-text">
            Os habitats de zonas úmidas estão entre os ecossistemas mais produtivos da Terra, apoiando uma incrível diversidade de aves aquáticas<span class="emoji">💧</span>. Essas áreas servem como pontos de parada críticos durante a migração e fornecem terrenos de reprodução essenciais.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Importância das Zonas Úmidas</div>
            As zonas úmidas apoiam mais de 40% de todas as espécies de aves, apesar de cobrirem apenas 6% da superfície terrestre, tornando-as cruciais para a conservação global de aves.
        </div>
        
        <div class="section-title">Papel das Aves nos Ecossistemas</div>
        <div class="main-text">
            As aves desempenham múltiplos papéis nos ecossistemas, servindo tanto como consumidores quanto como provedores de serviços ecossistêmicos essenciais<span class="emoji">🌍</span>. Suas diversas estratégias de alimentação e comportamentos criam redes ecológicas complexas que apoiam a biodiversidade.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Papéis de Consumidores</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Consumidores Primários</h5>
                        <p>Aves herbívoras: gansos, patos, pombos</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumidores Secundários</h5>
                        <p>Aves insetívoras: andorinhas, papa-moscas, carriças</p>
                    </div>
                    <div class="role-item">
                        <h5>Consumidores Superiores</h5>
                        <p>Aves de rapina: falcões, águias, corujas</p>
                    </div>
                    <div class="role-item">
                        <h5>Assistentes de Decomposição</h5>
                        <p>Aves necrófagas: abutres, corvos, pegas</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Provedores de Serviços Ecossistêmicos</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Serviços de Polinização</h5>
                        <p>Beija-flores, nectariniídeos e melifagídeos polinizam plantas, mantendo a diversidade vegetal</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Dispersão de Sementes</h5>
                        <p>Aves frugívoras ajudam as plantas a dispersar sementes, promovendo a regeneração florestal</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Controle de Pragas</h5>
                        <p>Aves insetívoras controlam populações de pragas, mantendo o equilíbrio ecológico agrícola e florestal</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Ciclagem de Nutrientes</h5>
                        <p>Os excrementos de aves fornecem nutrientes importantes para os ecossistemas</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Ameaças aos Habitats</div>
        <div class="main-text">
            As atividades humanas representam sérias ameaças aos habitats das aves, exigindo ação de conservação urgente<span class="emoji">⚠️</span>. Entender essas ameaças é o primeiro passo para a proteção eficaz do habitat.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Perda de Habitat</h4>
                <p>A urbanização e a expansão agrícola reduzem a área de habitat natural</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Fragmentação de Habitat</h4>
                <p>Estradas e edifícios dividem habitats contínuos em manchas menores</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Poluição Ambiental</h4>
                <p>A poluição química e sonora afeta a qualidade do habitat</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Mudanças Climáticas</h4>
                <p>As mudanças nos padrões de temperatura e precipitação afetam a adequação do habitat</p>
            </div>
        </div>
        
        <div class="section-title">Estratégias de Conservação</div>
        <div class="main-text">
            Proteger os habitats das aves requer estratégias de conservação abrangentes que abordem múltiplas escalas e partes interessadas<span class="emoji">🛡️</span>. A conservação eficaz combina pesquisa científica, implementação de políticas e envolvimento da comunidade.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Estabelecimento de Áreas Protegidas</h4>
                <ul>
                    <li>Estabelecer reservas naturais e parques nacionais</li>
                    <li>Designar Áreas Importantes para Aves</li>
                    <li>Proteger locais críticos de parada migratória</li>
                    <li>Criar corredores de habitat para conectar áreas fragmentadas</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Restauração Ecológica</h4>
                <ul>
                    <li>Converter terras agrícolas de volta para florestas e pastagens</li>
                    <li>Projetos de restauração de zonas úmidas</li>
                    <li>Reflorestamento artificial e restauração da vegetação</li>
                    <li>Restauração de ecossistemas fluviais</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 O que os Indivíduos Podem Fazer</h4>
            <ul>
                <li>Plantar espécies nativas em quintais e jardins</li>
                <li>Instalar bebedouros e comedouros para pássaros</li>
                <li>Reduzir o uso de pesticidas e fertilizantes</li>
                <li>Participar de atividades de monitoramento e conservação de aves</li>
                <li>Apoiar projetos de conservação de habitat</li>
                <li>Criar consciência ambiental e influenciar outros</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_russian_content():
    """创建完整的俄语内容"""
    return '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Среда обитания и экосистемы - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">Среда обитания и экосистемы</h1>
        <div class="quote-box">
            <div class="quote-text">Исследование сложных экологических взаимосвязей в природе</div>
        </div>
        <div class="main-text">
            Понимание сложных взаимосвязей между птицами и их средой обитания имеет решающее значение для сохранения и экологического баланса<span class="emoji">🌿</span>.
        </div>
        
        <div class="section-title">Что такое среда обитания птиц?</div>
        <div class="main-text">
            Среда обитания — это естественная среда, где птицы живут и размножаются, включая источники пищи, места для гнездования, источники воды и укрытия. У разных птиц очень разные требования к среде обитания, и это разнообразие создает богатые птичьи экосистемы<span class="emoji">🏠</span>.
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 Основные элементы среды обитания</div>
            Каждая среда обитания птиц должна обеспечивать четыре основных элемента: пищу, воду, укрытие и подходящие места для гнездования. Качество и доступность этих элементов определяют емкость среды обитания.
        </div>
        
        <div class="section-title">Лесные среды обитания</div>
        <div class="main-text">
            Лесные среды обитания предоставляют богатые пищевые ресурсы и места для гнездования, поддерживая многочисленные виды птиц<span class="emoji">🌲</span>. Эти сложные экосистемы предлагают несколько вертикальных ярусов, которые разные виды птиц используют для кормления, гнездования и укрытия.
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>Хвойные леса</h4>
                <p>Дом для тетеревиных, дятлов и врановых, приспособившихся к вечнозеленым деревьям</p>
            </div>
            <div class="habitat-item">
                <h4>Лиственные леса</h4>
                <p>Поддерживают певчих птиц, хищников и лазающих птиц с сезонными изменениями листвы</p>
            </div>
            <div class="habitat-item">
                <h4>Смешанные леса</h4>
                <p>Среды обитания с наибольшим видовым разнообразием, сочетающие преимущества обоих типов лесов</p>
            </div>
        </div>
        
        <div class="section-title">Водно-болотные экосистемы</div>
        <div class="main-text">
            Водно-болотные угодья являются одними из самых продуктивных экосистем на Земле, поддерживая невероятное разнообразие водоплавающих птиц<span class="emoji">💧</span>. Эти районы служат критически важными остановочными пунктами во время миграции и предоставляют необходимые места для размножения.
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 Важность водно-болотных угодий</div>
            Водно-болотные угодья поддерживают более 40% всех видов птиц, несмотря на то, что занимают всего 6% суши, что делает их решающими для глобального сохранения птиц.
        </div>
        
        <div class="section-title">Роль птиц в экосистемах</div>
        <div class="main-text">
            Птицы играют множество ролей в экосистемах, выступая как в качестве потребителей, так и в качестве поставщиков основных экосистемных услуг<span class="emoji">🌍</span>. Их разнообразные стратегии питания и поведение создают сложные экологические сети, поддерживающие биоразнообразие.
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>Роли потребителей</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>Первичные потребители</h5>
                        <p>Растительноядные птицы: гуси, утки, голуби</p>
                    </div>
                    <div class="role-item">
                        <h5>Вторичные потребители</h5>
                        <p>Насекомоядные птицы: ласточки, мухоловки, крапивники</p>
                    </div>
                    <div class="role-item">
                        <h5>Высшие потребители</h5>
                        <p>Хищные птицы: ястребы, орлы, совы</p>
                    </div>
                    <div class="role-item">
                        <h5>Помощники в разложении</h5>
                        <p>Птицы-падальщики: грифы, вороны, сороки</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>Поставщики экосистемных услуг</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 Услуги по опылению</h5>
                        <p>Колибри, нектарницы и медососы опыляют растения, поддерживая разнообразие растений</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 Распространение семян</h5>
                        <p>Плодоядные птицы помогают растениям распространять семена, способствуя восстановлению лесов</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 Борьба с вредителями</h5>
                        <p>Насекомоядные птицы контролируют популяции вредителей, поддерживая экологический баланс в сельском и лесном хозяйстве</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 Круговорот питательных веществ</h5>
                        <p>Птичий помет обеспечивает важные питательные вещества для экосистем</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">Угрозы для сред обитания</div>
        <div class="main-text">
            Деятельность человека представляет серьезную угрозу для сред обитания птиц, требуя срочных мер по сохранению<span class="emoji">⚠️</span>. Понимание этих угроз — первый шаг к эффективной защите среды обитания.
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ Потеря среды обитания</h4>
                <p>Урбанизация и расширение сельского хозяйства сокращают площадь естественных сред обитания</p>
            </div>
            <div class="threat-item">
                <h4>🧩 Фрагментация среды обитания</h4>
                <p>Дороги и здания разделяют сплошные среды обитания на более мелкие участки</p>
            </div>
            <div class="threat-item">
                <h4>🏭 Загрязнение окружающей среды</h4>
                <p>Химическое и шумовое загрязнение влияет на качество среды обитания</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ Изменение климата</h4>
                <p>Изменения в температурных и осадочных режимах влияют на пригодность среды обитания</p>
            </div>
        </div>
        
        <div class="section-title">Стратегии сохранения</div>
        <div class="main-text">
            Защита сред обитания птиц требует комплексных стратегий сохранения, охватывающих несколько масштабов и заинтересованных сторон<span class="emoji">🛡️</span>. Эффективное сохранение сочетает научные исследования, реализацию политики и участие общественности.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ Создание охраняемых территорий</h4>
                <ul>
                    <li>Создание заповедников и национальных парков</li>
                    <li>Определение ключевых орнитологических территорий</li>
                    <li>Защита критически важных миграционных остановок</li>
                    <li>Создание коридоров среды обитания для соединения фрагментированных территорий</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 Экологическое восстановление</h4>
                <ul>
                    <li>Преобразование сельскохозяйственных земель обратно в леса и луга</li>
                    <li>Проекты по восстановлению водно-болотных угодий</li>
                    <li>Искусственное лесовосстановление и восстановление растительности</li>
                    <li>Восстановление речных экосистем</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 Что могут сделать отдельные лица</h4>
            <ul>
                <li>Сажать местные виды растений во дворах и садах</li>
                <li>Устанавливать поилки и кормушки для птиц</li>
                <li>Сократить использование пестицидов и удобрений</li>
                <li>Участвовать в мероприятиях по мониторингу и сохранению птиц</li>
                <li>Поддерживать проекты по сохранению среды обитания</li>
                <li>Повышать экологическую осведомленность и влиять на других</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def create_chinese_content():
    """创建完整的中文内容"""
    return '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>栖息地与生态系统 - BirdAiSnap</title>
    <link href="../../mobile-styles.css" rel="stylesheet"/>
    <link href="../../mobile-enhancement.css" rel="stylesheet"/>
    <link href="../../ecology-theme.css" rel="stylesheet"/>
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-075.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">栖息地与生态系统</h1>
        <div class="quote-box">
            <div class="quote-text">探索自然界复杂的生态关系</div>
        </div>
        <div class="main-text">
            理解鸟类与其环境之间的复杂关系，对于保护和生态平衡至关重要<span class="emoji">🌿</span>。
        </div>
        
        <div class="section-title">什么是鸟类栖息地</div>
        <div class="main-text">
            栖息地是鸟类生活和繁殖的自然环境，包括食物来源、筑巢地点、水源和庇护所。不同的鸟类有截然不同的栖息地要求，这种多样性造就了丰富的鸟类生态系统<span class="emoji">🏠</span>。
        </div>
        <div class="tip-box">
            <div class="tip-title">🌱 栖息地的基本要素</div>
            每个鸟类栖息地都必须提供四个基本要素：食物、水源、庇护所和合适的筑巢地点。这些要素的质量和可得性决定了栖息地的承载能力。
        </div>
        
        <div class="section-title">森林栖息地</div>
        <div class="main-text">
            森林栖息地提供丰富的食物资源和筑巢地点，支持着众多鸟类物种<span class="emoji">🌲</span>。这些复杂的生态系统提供了多个垂直层次，不同种类的鸟类利用这些层次进行觅食、筑巢和躲避。
        </div>
        <div class="habitat-types">
            <div class="habitat-item">
                <h4>针叶林</h4>
                <p>适应了常绿树木的松鸡、啄木鸟和鸦科鸟类的家园</p>
            </div>
            <div class="habitat-item">
                <h4>落叶林</h4>
                <p>支持鸣禽、猛禽和攀禽，叶片有季节性变化</p>
            </div>
            <div class="habitat-item">
                <h4>混交林</h4>
                <p>物种多样性最高的栖息地，结合了两种森林类型的优点</p>
            </div>
        </div>
        
        <div class="section-title">湿地生态系统</div>
        <div class="main-text">
            湿地栖息地是地球上生产力最高的生态系统之一，支持着令人难以置信的水鸟多样性<span class="emoji">💧</span>。这些区域在迁徙期间作为关键的停歇点，并提供必要的繁殖地。
        </div>
        <div class="tip-box">
            <div class="tip-title">🦆 湿地的重要性</div>
            湿地仅占地球陆地面积的6%，却支持着超过40%的鸟类物种，使其对全球鸟类保护至关重要。
        </div>
        
        <div class="section-title">鸟类在生态系统中的作用</div>
        <div class="main-text">
            鸟类在生态系统中扮演着多重角色，既是消费者，也是重要的生态系统服务提供者<span class="emoji">🌍</span>。它们多样的觅食策略和行为创造了支持生物多样性的复杂生态网络。
        </div>
        
        <div class="ecological-roles">
            <div class="role-category">
                <h4>消费者角色</h4>
                <div class="role-grid">
                    <div class="role-item">
                        <h5>初级消费者</h5>
                        <p>食草鸟类：雁、鸭、鸽</p>
                    </div>
                    <div class="role-item">
                        <h5>次级消费者</h5>
                        <p>食虫鸟类：燕子、捕蝇鸟、鹪鹩</p>
                    </div>
                    <div class="role-item">
                        <h5>顶级消费者</h5>
                        <p>猛禽：鹰、雕、猫头鹰</p>
                    </div>
                    <div class="role-item">
                        <h5>分解协助者</h5>
                        <p>食腐鸟类：秃鹫、乌鸦、喜鹊</p>
                    </div>
                </div>
            </div>
            
            <div class="role-category">
                <h4>生态系统服务提供者</h4>
                <div class="service-list">
                    <div class="service-item">
                        <h5>🌸 传粉服务</h5>
                        <p>蜂鸟、太阳鸟和蜜鸟为植物授粉，维持植物多样性</p>
                    </div>
                    <div class="service-item">
                        <h5>🌰 种子传播</h5>
                        <p>食果鸟类帮助植物传播种子，促进森林再生</p>
                    </div>
                    <div class="service-item">
                        <h5>🐛 害虫控制</h5>
                        <p>食虫鸟类控制害虫数量，维持农业和森林生态平衡</p>
                    </div>
                    <div class="service-item">
                        <h5>💩 养分循环</h5>
                        <p>鸟粪为生态系统提供重要的养分</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section-title">对栖息地的威胁</div>
        <div class="main-text">
            人类活动对鸟类栖息地构成严重威胁，需要采取紧急的保护行动<span class="emoji">⚠️</span>。了解这些威胁是有效保护栖息地的第一步。
        </div>
        
        <div class="threats-grid">
            <div class="threat-item">
                <h4>🏗️ 栖息地丧失</h4>
                <p>城市化和农业扩张减少了自然栖息地的面积</p>
            </div>
            <div class="threat-item">
                <h4>🧩 栖息地破碎化</h4>
                <p>道路和建筑物将连续的栖息地分割成更小的斑块</p>
            </div>
            <div class="threat-item">
                <h4>🏭 环境污染</h4>
                <p>化学污染和噪音污染影响栖息地质量</p>
            </div>
            <div class="threat-item">
                <h4>🌡️ 气候变化</h4>
                <p>温度和降水模式的变化影响栖息地的适宜性</p>
            </div>
        </div>
        
        <div class="section-title">保护策略</div>
        <div class="main-text">
            保护鸟类栖息地需要综合性的保护策略，涵盖多个尺度和利益相关者<span class="emoji">🛡️</span>。有效的保护结合了科学研究、政策实施和社区参与。
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🏞️ 建立保护区</h4>
                <ul>
                    <li>建立自然保护区和国家公园</li>
                    <li>指定重要鸟类栖息地</li>
                    <li>保护关键的迁徙停歇地</li>
                    <li>创建栖息地走廊连接破碎化的区域</li>
                </ul>
            </div>
            <div class="strategy-category">
                <h4>🌱 生态恢复</h4>
                <ul>
                    <li>将农田恢复为森林和草原</li>
                    <li>湿地恢复项目</li>
                    <li>人工造林和植被恢复</li>
                    <li>河流生态系统恢复</li>
                </ul>
            </div>
        </div>
        
        <div class="action-tips">
            <h4>🤝 个人可以做什么</h4>
            <ul>
                <li>在院子和花园里种植本地物种</li>
                <li>安装鸟浴盆和喂食器</li>
                <li>减少使用杀虫剂和化肥</li>
                <li>参与鸟类监测和保护活动</li>
                <li>支持栖息地保护项目</li>
                <li>提高环境意识并影响他人</li>
            </ul>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        // 模拟阅读进度
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 初始化
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''

def main():
    """主函数，用于创建所有翻译文件"""
    translations = {
        "es": create_spanish_content,
        "it": create_italian_content,
        "ja": create_japanese_content,
        "fr": create_french_content,
        "de": create_german_content,
        "pt": create_portuguese_content,
        "ru": create_russian_content,
        "zh": create_chinese_content
    }

    base_dir = Path(__file__).resolve().parent
    
    for lang, content_func in translations.items():
        lang_dir = base_dir / lang / "ecology"
        lang_dir.mkdir(parents=True, exist_ok=True)
        file_path = lang_dir / "01-habitat-ecosystems.html"
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content_func())
            print(f"Successfully created: {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

if __name__ == "__main__":
    main()
