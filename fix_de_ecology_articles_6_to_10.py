#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def create_article_06():
    """创建德语版本的第6篇文章 - 城市生态学"""
    content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stadtökologie - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_urban_ecology.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .hero-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            color: white;
        }
        
        .hero-overlay h1 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 40px 20px 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .article-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .category {
            background: #4caf50;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .read-time, .difficulty {
            background: #f5f5f5;
            color: #666;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .difficulty.intermediate {
            background: #fff3e0;
            color: #f57c00;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #4caf50;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 16px;
            font-weight: 600;
            color: #2e7d32;
            margin-left: 25px;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .quote-author {
            font-size: 14px;
            color: #388e3c;
            margin-left: 25px;
            font-style: italic;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #4caf50;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .urban-section {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .urban-factors h4 {
            color: #2e7d32;
            font-size: 16px;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .urban-factors ul {
            list-style: none;
            padding: 0;
        }
        
        .urban-factors li {
            background: white;
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 8px;
            border-left: 3px solid #81c784;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(to top, rgba(255,255,255,0.95), transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 998;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(0,0,0,0.1);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #81c784);
            width: 0%;
            border-radius: 2px;
            transition: width 0.3s ease;
        }
        
        @media (max-width: 768px) {
            .hero-overlay h1 {
                font-size: 24px;
            }
            
            .content {
                margin: -20px 15px 15px 15px;
                padding: 25px 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-image">
        <div class="hero-overlay">
            <h1>Vitalität zwischen Beton und Stahl</h1>
        </div>
    </div>
    
    <div class="content">
        <div class="article-meta">
            <span class="category">Vogelökologie</span>
            <span class="read-time">📖 9 Minuten Lesezeit</span>
            <span class="difficulty intermediate">🟡 Mittelstufe</span>
        </div>
        
        <div class="quote-box">
            <div class="quote-text">Städte bieten Vögeln neue Möglichkeiten und Herausforderungen; diejenigen, die sich erfolgreich an das städtische Leben anpassen, zeigen bemerkenswerte Plastizität.</div>
            <div class="quote-author">— Stadtökologe</div>
        </div>
        
        <div class="section-title">🏙️ Merkmale städtischer Umgebungen</div>
        <div class="main-text">
            Städtische Umgebungen unterscheiden sich erheblich von natürlichen Lebensräumen und stellen Vögel vor einzigartige Überlebensherausforderungen und -möglichkeiten.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🏢 Physische Umgebung</h4>
                <ul>
                    <li>Dichte Bebauung, fragmentierte Grünflächen</li>
                    <li>Erhöhte Hartflächen, reduzierte Durchlässigkeit</li>
                    <li>Künstliche Lichtquellen, nächtliche Beleuchtung</li>
                    <li>Erhöhte Temperaturen (Wärmeinseleffekt)</li>
                    <li>Veränderte Windrichtungen und Luftströmungsmuster</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🌱 Biologische Umgebung</h4>
                <ul>
                    <li>Begrenzte Pflanzenarten, meist nicht-einheimisch</li>
                    <li>Künstlich bereitgestellte Nahrung</li>
                    <li>Veränderungen bei Raubtierarten und -zahlen</li>
                    <li>Veränderte Krankheitsübertragungsmuster</li>
                    <li>Reduzierte Biodiversität</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>👥 Soziale Umgebung</h4>
                <ul>
                    <li>Häufige menschliche Aktivitäten</li>
                    <li>Starke Lärmbelastung</li>
                    <li>Hohes Verkehrsaufkommen</li>
                    <li>Erhöhte chemische Schadstoffe</li>
                    <li>Häufige menschliche Störungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🦅 Anpassungsstrategien städtischer Vögel</div>
        <div class="main-text">
            Vögel, die erfolgreich in Städten überleben, haben verschiedene Anpassungsstrategien entwickelt.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🎭 Verhaltensanpassungen</h4>
                <ul>
                    <li>Änderung der Ruffrequenz und -lautstärke</li>
                    <li>Anpassung der Aktivitätszeiten zur Vermeidung von Stoßzeiten</li>
                    <li>Erlernen der Nutzung künstlicher Strukturen zum Nisten</li>
                    <li>Änderung des Nahrungssuchverhaltens und der Ernährung</li>
                    <li>Erhöhte Toleranz gegenüber Menschen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🧬 Physiologische Anpassungen</h4>
                <ul>
                    <li>Regulation der Stresshormonspiegel</li>
                    <li>Veränderungen der Immunsystemfunktion</li>
                    <li>Anpassungen der Stoffwechselrate</li>
                    <li>Regulation der Brutzyklen</li>
                    <li>Veränderungen der Sinnessystemempfindlichkeit</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📏 Morphologische Anpassungen</h4>
                <ul>
                    <li>Veränderungen der Körpergröße</li>
                    <li>Anpassungen der Flügelform</li>
                    <li>Modifikationen der Schnabelstruktur</li>
                    <li>Veränderungen der Gefiederfärbung</li>
                    <li>Anpassungen der Beinstruktur</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🏠 Städtische Lebensraumtypen</div>
        <div class="main-text">
            Städte enthalten mehrere Arten von Vogellebensräumen, jeder mit seinen eigenen Merkmalen und unterstützten Vogelgemeinschaften.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🌳 Stadtparks</h4>
                <ul>
                    <li>Relativ große Grünflächen</li>
                    <li>Höhere Pflanzenvielfalt</li>
                    <li>Unterstützung mehrerer Vogelarten</li>
                    <li>Hohe Intensität menschlicher Verwaltung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏘️ Wohngrünflächen</h4>
                <ul>
                    <li>Kleine, verstreute Grünflächen</li>
                    <li>Relativ begrenzte Pflanzenarten</li>
                    <li>Häufige menschliche Störungen</li>
                    <li>Hochanpassungsfähige Arten dominieren</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>💧 Städtische Gewässer</h4>
                <ul>
                    <li>Künstliche Seen und Flüsse</li>
                    <li>Wasserqualität kann verschmutzt sein</li>
                    <li>Unterstützung des Überlebens von Wasservögeln</li>
                    <li>Umgebende Grüngürtel sind wichtig</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏢 Gebaute Umgebung</h4>
                <ul>
                    <li>Hohe Gebäude bieten Nistplätze</li>
                    <li>Dachgärten erhöhen Grünflächen</li>
                    <li>Gebäudespalten werden zu Lebensräumen</li>
                    <li>Künstliche Strukturen imitieren natürliche Umgebungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🍎 Nahrungsquellen für städtische Vögel</div>
        <div class="main-text">
            Städtische Umgebungen bieten Vögeln vielfältige Nahrungsquellen, einschließlich natürlicher und künstlicher Quellen.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🌿 Natürliche Nahrungsquellen</h4>
                <ul>
                    <li>Früchte und Samen von Stadtpflanzen</li>
                    <li>Insekten und andere wirbellose Tiere</li>
                    <li>Kleine Wirbeltiere</li>
                    <li>Nektar und Pollen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏠 Künstliche Nahrungsquellen</h4>
                <ul>
                    <li>Von Menschen bereitgestellte Nahrung</li>
                    <li>Nahrungsreste im Müll</li>
                    <li>Haustierfutter</li>
                    <li>Vogelfutterstellen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>⚠️ Auswirkungen künstlicher Fütterung</h4>
                <ul>
                    <li>Veränderung natürlicher Verhaltensweisen der Vögel</li>
                    <li>Mögliche Verursachung von Nährstoffungleichgewichten</li>
                    <li>Erhöhung der Krankheitsübertragungsrisiken</li>
                    <li>Beeinflussung der Populationsstrukturen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🏗️ Ökologische Auswirkungen der Urbanisierung</div>
        <div class="main-text">
            Der Urbanisierungsprozess hat tiefgreifende Auswirkungen auf Vogelgemeinschaften.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🦜 Veränderungen der Artenzusammensetzung</h4>
                <ul>
                    <li>Zunahme hochanpassungsfähiger Arten</li>
                    <li>Abnahme spezialisierter Arten</li>
                    <li>Invasion nicht-einheimischer Arten</li>
                    <li>Verschwinden einheimischer Arten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📊 Veränderungen der Populationsdynamik</h4>
                <ul>
                    <li>Dramatische Zunahmen bestimmter Arten</li>
                    <li>Weitere Reduzierung seltener Arten</li>
                    <li>Ungleichmäßige Populationsdichteverteilung</li>
                    <li>Veränderungen der Bruterfolgsraten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🌐 Veränderungen der Gemeinschaftsstruktur</h4>
                <ul>
                    <li>Reduzierte Artenvielfalt</li>
                    <li>Verringerte funktionale Vielfalt</li>
                    <li>Vereinfachte Nahrungsnetze</li>
                    <li>Erhöhte Nischenüberlappung</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🚧 Bedrohungen für städtische Vögel</div>
        <div class="main-text">
            Städtische Umgebungen stellen mehrere Bedrohungen für Vögel dar.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>💥 Kollisionsbedrohungen</h4>
                <ul>
                    <li>Kollisionen mit Gebäudeglas</li>
                    <li>Fahrzeugkollisionen</li>
                    <li>Windturbinenverletzungen</li>
                    <li>Stromschläge an Stromleitungen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏭 Verschmutzungsbedrohungen</h4>
                <ul>
                    <li>Luftverschmutzung</li>
                    <li>Wasserverschmutzung</li>
                    <li>Lärmverschmutzung</li>
                    <li>Lichtverschmutzung</li>
                    <li>Chemische Verschmutzung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🐱 Biologische Bedrohungen</h4>
                <ul>
                    <li>Beutegreifung durch streunende Katzen</li>
                    <li>Krankheitsübertragung</li>
                    <li>Konkurrenz durch nicht-einheimische Arten</li>
                    <li>Parasiteninfektionen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🌱 Naturschutzstrategien für städtische Vögel</div>
        <div class="main-text">
            Der Schutz städtischer Vögel erfordert umfassende Managementstrategien.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🏞️ Lebensraummanagement</h4>
                <ul>
                    <li>Erhöhung der städtischen Grünflächenfläche</li>
                    <li>Verbesserung der Grünflächenverbindung</li>
                    <li>Anpflanzung einheimischer Vegetation</li>
                    <li>Schaffung mehrschichtiger Vegetationsstrukturen</li>
                    <li>Schutz und Wiederherstellung von Feuchtgebieten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏢 Verbesserungen des Gebäudedesigns</h4>
                <ul>
                    <li>Verwendung vogelfreundlichen Glases</li>
                    <li>Gestaltung von Gründächern</li>
                    <li>Bereitstellung künstlicher Nistkästen</li>
                    <li>Reduzierung der Lichtverschmutzung</li>
                    <li>Schaffung vertikaler Begrünung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📋 Politische Maßnahmen</h4>
                <ul>
                    <li>Entwicklung städtischer Vogelschutzvorschriften</li>
                    <li>Regulierung der Stadtentwicklung</li>
                    <li>Kontrolle streunender Katzenpopulationen</li>
                    <li>Begrenzung des Chemikalieneinsatzes</li>
                    <li>Förderung von Öko-Stadt-Konzepten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>👥 Öffentliche Beteiligung</h4>
                <ul>
                    <li>Durchführung von Vogelüberwachungsaktivitäten</li>
                    <li>Verbreitung von Vogelschutzwissen</li>
                    <li>Förderung wissenschaftlicher Vogelfütterung</li>
                    <li>Aufbau von Freiwilligennetzwerken</li>
                    <li>Unterstützung von Naturschutzprojekten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🔮 Zukünftige Entwicklungsrichtungen</h4>
                <ul>
                    <li>Integration von Smart Cities und Vogelschutz</li>
                    <li>Big Data-basierte Vogelüberwachung</li>
                    <li>Ökologische Stadtplanung und -gestaltung</li>
                    <li>Modelle für harmonisches Zusammenleben von Mensch und Vogel</li>
                    <li>Städtischer Biodiversitätsschutz</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('de/ecology/06-urban-ecology.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已更新: 06-urban-ecology.html")

def create_article_07():
    """创建德语版本的第7篇文章 - 保护生物学"""
    content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Naturschutzbiologie - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_conservation_biology.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .hero-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            color: white;
        }
        
        .hero-overlay h1 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 40px 20px 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .article-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .category {
            background: #4caf50;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .read-time, .difficulty {
            background: #f5f5f5;
            color: #666;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .difficulty.advanced {
            background: #ffebee;
            color: #c62828;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #4caf50;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 16px;
            font-weight: 600;
            color: #2e7d32;
            margin-left: 25px;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .quote-author {
            font-size: 14px;
            color: #388e3c;
            margin-left: 25px;
            font-style: italic;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #4caf50;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .conservation-section {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .conservation-factors h4 {
            color: #2e7d32;
            font-size: 16px;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .conservation-factors ul {
            list-style: none;
            padding: 0;
        }
        
        .conservation-factors li {
            background: white;
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 8px;
            border-left: 3px solid #81c784;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(to top, rgba(255,255,255,0.95), transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 998;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(0,0,0,0.1);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #81c784);
            width: 0%;
            border-radius: 2px;
            transition: width 0.3s ease;
        }
        
        @media (max-width: 768px) {
            .hero-overlay h1 {
                font-size: 24px;
            }
            
            .content {
                margin: -20px 15px 15px 15px;
                padding: 25px 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-image">
        <div class="hero-overlay">
            <h1>Wissenschaft für den Schutz der Natur</h1>
        </div>
    </div>
    
    <div class="content">
        <div class="article-meta">
            <span class="category">Vogelökologie</span>
            <span class="read-time">📖 12 Minuten Lesezeit</span>
            <span class="difficulty advanced">🔴 Fortgeschritten</span>
        </div>
        
        <div class="quote-box">
            <div class="quote-text">Naturschutzbiologie ist die Wissenschaft, die sich der Erhaltung der biologischen Vielfalt und dem Schutz bedrohter Arten widmet.</div>
            <div class="quote-author">— Naturschutzbiologe</div>
        </div>
        
        <div class="section-title">🔬 Grundlagen der Naturschutzbiologie</div>
        <div class="main-text">
            Die Naturschutzbiologie ist eine interdisziplinäre Wissenschaft, die biologische, ökologische, soziale und wirtschaftliche Prinzipien integriert, um die biologische Vielfalt zu erhalten.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🎯 Hauptziele der Naturschutzbiologie</h4>
                <ul>
                    <li>Erhaltung der genetischen Vielfalt</li>
                    <li>Schutz von Arten vor dem Aussterben</li>
                    <li>Bewahrung von Ökosystemen und Lebensräumen</li>
                    <li>Nachhaltige Nutzung natürlicher Ressourcen</li>
                    <li>Wiederherstellung degradierter Ökosysteme</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>📊 Wissenschaftliche Methoden</h4>
                <ul>
                    <li>Populationsökologie und -dynamik</li>
                    <li>Genetische Analysen und Molekularbiologie</li>
                    <li>Landschaftsökologie und Habitatmodellierung</li>
                    <li>Klimawandelforschung und Anpassungsstrategien</li>
                    <li>Sozioökonomische Bewertungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">⚠️ Bedrohungen für Vögel</div>
        <div class="main-text">
            Vögel stehen vor verschiedenen Bedrohungen, die ihre Populationen und ihr Überleben gefährden.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🏗️ Lebensraumverlust und -fragmentierung</h4>
                <ul>
                    <li>Urbanisierung und Infrastrukturentwicklung</li>
                    <li>Landwirtschaftliche Intensivierung</li>
                    <li>Entwaldung und Habitatzerstörung</li>
                    <li>Feuchtgebietsdrainage und -umwandlung</li>
                    <li>Küstenerosion und Meeresspiegelanstieg</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>🌡️ Klimawandel</h4>
                <ul>
                    <li>Verschiebung von Temperatur- und Niederschlagsmustern</li>
                    <li>Veränderungen der Vegetationszonen</li>
                    <li>Störung der Zugmuster und -zeiten</li>
                    <li>Extreme Wetterereignisse</li>
                    <li>Ozeanversauerung und Meereserwärmung</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>🏭 Umweltverschmutzung</h4>
                <ul>
                    <li>Pestizide und chemische Kontamination</li>
                    <li>Plastikverschmutzung und Mikroplastik</li>
                    <li>Lärm- und Lichtverschmutzung</li>
                    <li>Luftverschmutzung und saurer Regen</li>
                    <li>Ölverschmutzung in Meeresgebieten</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>🐱 Invasive Arten und Krankheiten</h4>
                <ul>
                    <li>Eingeführte Raubtiere (Katzen, Ratten)</li>
                    <li>Konkurrierende nicht-einheimische Vogelarten</li>
                    <li>Krankheitserreger und Parasiten</li>
                    <li>Invasive Pflanzenarten</li>
                    <li>Genetische Verschmutzung durch Hybridisierung</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🛡️ Schutzstrategien</div>
        <div class="main-text">
            Effektive Vogelschutzstrategien erfordern einen vielschichtigen Ansatz, der verschiedene Schutzmaßnahmen kombiniert.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🏞️ In-situ-Schutz</h4>
                <ul>
                    <li>Einrichtung und Verwaltung von Schutzgebieten</li>
                    <li>Habitatwiederherstellung und -verbesserung</li>
                    <li>Korridore und Vernetzung von Lebensräumen</li>
                    <li>Überwachung und Forschung in natürlichen Habitaten</li>
                    <li>Gemeinschaftsbasierte Schutzprogramme</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>🏢 Ex-situ-Schutz</h4>
                <ul>
                    <li>Zuchtprogramme in Gefangenschaft</li>
                    <li>Genbanken und Kryokonservierung</li>
                    <li>Wiederansiedlungsprogramme</li>
                    <li>Rettungszentren und Rehabilitation</li>
                    <li>Forschung in kontrollierten Umgebungen</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>📋 Politische und rechtliche Maßnahmen</h4>
                <ul>
                    <li>Artenschutzgesetze und -verordnungen</li>
                    <li>Internationale Abkommen und Verträge</li>
                    <li>Umweltverträglichkeitsprüfungen</li>
                    <li>Handelsbeschränkungen (CITES)</li>
                    <li>Subventionen für naturfreundliche Praktiken</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">📊 Überwachung und Bewertung</div>
        <div class="main-text">
            Systematische Überwachung ist entscheidend für die Bewertung des Erhaltungsstatus und den Erfolg von Schutzmaßnahmen.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🔍 Überwachungsmethoden</h4>
                <ul>
                    <li>Populationszählungen und Bestandsaufnahmen</li>
                    <li>Bruterfolgsmessungen</li>
                    <li>Überlebensraten und Sterblichkeitsanalysen</li>
                    <li>Habitatqualitätsbewertungen</li>
                    <li>Genetische Diversitätsstudien</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>📈 Bewertungsindikatoren</h4>
                <ul>
                    <li>Populationstrends und -größe</li>
                    <li>Verbreitungsgebiet und Habitatqualität</li>
                    <li>Reproduktionserfolg</li>
                    <li>Genetische Vielfalt</li>
                    <li>Bedrohungsintensität</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🌍 Internationale Zusammenarbeit</div>
        <div class="main-text">
            Vogelschutz erfordert internationale Koordination, insbesondere für Zugvögel, die Grenzen überschreiten.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🤝 Internationale Abkommen</h4>
                <ul>
                    <li>Bonner Konvention (CMS)</li>
                    <li>Ramsar-Konvention für Feuchtgebiete</li>
                    <li>Übereinkommen über die biologische Vielfalt (CBD)</li>
                    <li>CITES-Abkommen</li>
                    <li>Regionale Flyway-Initiativen</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>🌐 Globale Initiativen</h4>
                <ul>
                    <li>BirdLife International Partnership</li>
                    <li>Important Bird Areas (IBA) Programm</li>
                    <li>Migratory Bird Joint Ventures</li>
                    <li>World Migratory Bird Day</li>
                    <li>Global Big Day und eBird</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">💡 Innovative Ansätze</div>
        <div class="main-text">
            Moderne Technologien und innovative Ansätze revolutionieren den Vogelschutz.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🔬 Technologische Innovationen</h4>
                <ul>
                    <li>Satellitentelemetrie und GPS-Tracking</li>
                    <li>Umwelt-DNA (eDNA) Analysen</li>
                    <li>Künstliche Intelligenz für Artenidentifikation</li>
                    <li>Drohnen für Überwachung und Forschung</li>
                    <li>Bioacoustic Monitoring</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>👥 Bürgerwissenschaft</h4>
                <ul>
                    <li>eBird und andere Datensammlungsplattformen</li>
                    <li>Christmas Bird Count</li>
                    <li>Breeding Bird Surveys</li>
                    <li>Migration Count Networks</li>
                    <li>Nest Monitoring Programs</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🎯 Erfolgsgeschichten</div>
        <div class="main-text">
            Erfolgreiche Naturschutzprogramme zeigen, dass gezielte Maßnahmen Arten vor dem Aussterben retten können.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🦅 Bemerkenswerte Erfolge</h4>
                <ul>
                    <li>Weißkopfseeadler-Wiederherstellung in Nordamerika</li>
                    <li>Kalifornischer Kondor-Rettung</li>
                    <li>Wanderfalken-Erholung nach DDT-Verbot</li>
                    <li>Kranich-Populationserholung in Europa</li>
                    <li>Neuseeland-Kakapo-Schutzprogramm</li>
                </ul>
            </div>
            
            <div class="conservation-factors">
                <h4>📚 Gelernte Lektionen</h4>
                <ul>
                    <li>Frühe Intervention ist entscheidend</li>
                    <li>Habitatschutz ist fundamental</li>
                    <li>Gemeinschaftsbeteiligung ist wesentlich</li>
                    <li>Langfristige Finanzierung ist notwendig</li>
                    <li>Adaptive Managementansätze sind effektiv</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🔮 Zukunftsperspektiven</div>
        <div class="main-text">
            Die Zukunft der Naturschutzbiologie liegt in integrativen Ansätzen, die Wissenschaft, Technologie und gesellschaftliches Engagement kombinieren.
        </div>
        
        <div class="conservation-section">
            <div class="conservation-factors">
                <h4>🚀 Emerging Trends</h4>
                <ul>
                    <li>Precision Conservation mit Big Data</li>
                    <li>Genomik und Genrettung</li>
                    <li>Ökosystemleistungen und Naturkapital</li>
                    <li>Climate-Smart Conservation</li>
                    <li>One Health Ansätze</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('de/ecology/07-conservation-biology.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已更新: 07-conservation-biology.html")

def create_remaining_articles():
    """创建剩余的德语文章 8-10"""
    
    # 第8篇文章 - 岛屿生物地理学
    article_08 = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insel-Biogeographie - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_island_biogeography.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .hero-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            color: white;
        }
        
        .hero-overlay h1 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 40px 20px 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .article-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .category {
            background: #4caf50;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .read-time, .difficulty {
            background: #f5f5f5;
            color: #666;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .difficulty.advanced {
            background: #ffebee;
            color: #c62828;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #4caf50;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 16px;
            font-weight: 600;
            color: #2e7d32;
            margin-left: 25px;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .quote-author {
            font-size: 14px;
            color: #388e3c;
            margin-left: 25px;
            font-style: italic;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #4caf50;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .island-section {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .island-factors h4 {
            color: #2e7d32;
            font-size: 16px;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .island-factors ul {
            list-style: none;
            padding: 0;
        }
        
        .island-factors li {
            background: white;
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 8px;
            border-left: 3px solid #81c784;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(to top, rgba(255,255,255,0.95), transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 998;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(0,0,0,0.1);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #81c784);
            width: 0%;
            border-radius: 2px;
            transition: width 0.3s ease;
        }
        
        @media (max-width: 768px) {
            .hero-overlay h1 {
                font-size: 24px;
            }
            
            .content {
                margin: -20px 15px 15px 15px;
                padding: 25px 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-image">
        <div class="hero-overlay">
            <h1>Evolutionslabore der Natur</h1>
        </div>
    </div>
    
    <div class="content">
        <div class="article-meta">
            <span class="category">Vogelökologie</span>
            <span class="read-time">📖 10 Minuten Lesezeit</span>
            <span class="difficulty advanced">🔴 Fortgeschritten</span>
        </div>
        
        <div class="quote-box">
            <div class="quote-text">Inseln sind natürliche Laboratorien der Evolution, in denen Isolation und begrenzte Ressourcen einzigartige Vogelgemeinschaften formen.</div>
            <div class="quote-author">— Insel-Biogeograph</div>
        </div>
        
        <div class="section-title">🏝️ Grundlagen der Insel-Biogeographie</div>
        <div class="main-text">
            Die Insel-Biogeographie untersucht die Verteilungsmuster von Arten auf Inseln und die Faktoren, die diese Muster beeinflussen. Diese Disziplin hat unser Verständnis von Evolution, Ökologie und Naturschutz revolutioniert.
        </div>
        
        <div class="island-section">
            <div class="island-factors">
                <h4>📊 MacArthur-Wilson-Theorie</h4>
                <ul>
                    <li>Gleichgewicht zwischen Einwanderung und Aussterben</li>
                    <li>Einfluss der Inselgröße auf Artenvielfalt</li>
                    <li>Bedeutung der Entfernung zum Festland</li>
                    <li>Dynamische Natur der Artengemeinschaften</li>
                    <li>Vorhersagbare Muster der Artenzahl</li>
                </ul>
            </div>
            
            <div class="island-factors">
                <h4>🎯 Schlüsselfaktoren</h4>
                <ul>
                    <li>Inselgröße und verfügbare Lebensräume</li>
                    <li>Isolation und Entfernung zu Quellpopulationen</li>
                    <li>Inseltyp (ozeanisch vs. kontinental)</li>
                    <li>Geologisches Alter und Stabilität</li>
                    <li>Klimatische Bedingungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🦅 Einwanderung und Kolonisation</div>
        <div class="main-text">
            Die Ankunft von Vögeln auf Inseln erfolgt durch verschiedene Mechanismen, die ihre Fähigkeit zur Überquerung von Wasserbarrieren widerspiegeln.
        </div>
        
        <div class="island-section">
            <div class="island-factors">
                <h4>✈️ Einwanderungsmechanismen</h4>
                <ul>
                    <li>Aktiver Flug über Wasserflächen</li>
                    <li>Passive Verbreitung durch Winde</li>
                    <li>Rafting auf schwimmenden Objekten</li>
                    <li>Menschlich vermittelte Einführung</li>
                    <li>Schrittweise Inselhopping</li>
                </ul>
            </div>
            
            <div class="island-factors">
                <h4>🎯 Kolonisationserfolg</h4>
                <ul>
                    <li>Verfügbarkeit geeigneter Lebensräume</li>
                    <li>Abwesenheit von Konkurrenten</li>
                    <li>Gründerpopulationsgröße</li>
                    <li>Genetische Vielfalt der Gründer</li>
                    <li>Ökologische Flexibilität der Art</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🧬 Evolution auf Inseln</div>
        <div class="main-text">
            Inseln bieten einzigartige evolutionäre Bedingungen, die zu bemerkenswerten Anpassungen und Artbildungsprozessen führen.
        </div>
        
        <div class="island-section">
            <div class="island-factors">
                <h4>🔄 Evolutionäre Prozesse</h4>
                <ul>
                    <li>Adaptive Radiation und Artbildung</li>
                    <li>Gründereffekte und genetische Drift</li>
                    <li>Inselgigantismus und -zwergwuchs</li>
                    <li>Verlust der Flugfähigkeit</li>
                    <li>Ökologische Freisetzung</li>
                </ul>
            </div>
            
            <div class="island-factors">
                <h4>🦜 Bemerkenswerte Anpassungen</h4>
                <ul>
                    <li>Darwin-Finken auf den Galápagos-Inseln</li>
                    <li>Hawaiianische Kleidervögel (Drepanidinae)</li>
                    <li>Neuseeländische flugunfähige Vögel</li>
                    <li>Madagassische Vangidae</li>
                    <li>Karibische Todies und Todis</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">⚖️ Ökologische Nischen</div>
        <div class="main-text">
            Auf Inseln können Vögel ökologische Nischen besetzen, die auf dem Festland von anderen Arten besetzt sind.
        </div>
        
        <div class="island-section">
            <div class="island-factors">
                <h4>🔄 Nischenerweiterung</h4>
                <ul>
                    <li>Expansion in unbesetzte ökologische Rollen</li>
                    <li>Veränderte Ernährungsgewohnheiten</li>
                    <li>Neue Lebensraumnutzung</li>
                    <li>Veränderte Verhaltensweisen</li>
                    <li>Morphologische Anpassungen</li>
                </ul>
            </div>
            
            <div class="island-factors">
                <h4>🎭 Ökologische Rollen</h4>
                <ul>
                    <li>Vögel als Hauptbestäuber</li>
                    <li>Samenausbreitung durch Vögel</li>
                    <li>Insektenfresser in verschiedenen Schichten</li>
                    <li>Nektarfresser und Frugivore</li>
                    <li>Bodenbrütende Spezialisten</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">💀 Aussterben auf Inseln</div>
        <div class="main-text">
            Inselvögel sind besonders anfällig für das Aussterben aufgrund ihrer kleinen Populationen und begrenzten Lebensräume.
        </div>
        
        <div class="island-section">
            <div class="island-factors">
                <h4>⚠️ Aussterbefaktoren</h4>
                <ul>
                    <li>Kleine Populationsgrößen</li>
                    <li>Begrenzte genetische Vielfalt</li>
                    <li>Habitatverlust und -degradation</li>
                    <li>Eingeführte Raubtiere</li>
                    <li>Krankheiten und Parasiten</li>
                </ul>
            </div>
            
            <div class="island-factors">
                <h4>📉 Historische Verluste</h4>
                <ul>
                    <li>Dodo und andere Mauritius-Arten</li>
                    <li>Große Auk (Pinguinus impennis)</li>
                    <li>Hawaiianische Vogelarten</li>
                    <li>Neuseeländische Moa-Arten</li>
                    <li>Karibische und pazifische Inselarten</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🌊 Meeresinseln vs. Kontinentalinseln</div>
        <div class
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def create_article_06():
    """创建德语版本的第6篇文章 - 城市生态学"""
    content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stadtökologie - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_urban_ecology.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .hero-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            color: white;
        }
        
        .hero-overlay h1 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 40px 20px 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .article-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .category {
            background: #4caf50;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .read-time, .difficulty {
            background: #f5f5f5;
            color: #666;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .difficulty.intermediate {
            background: #fff3e0;
            color: #f57c00;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #4caf50;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 16px;
            font-weight: 600;
            color: #2e7d32;
            margin-left: 25px;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .quote-author {
            font-size: 14px;
            color: #388e3c;
            margin-left: 25px;
            font-style: italic;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #4caf50;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .urban-section {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .urban-factors h4 {
            color: #2e7d32;
            font-size: 16px;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .urban-factors ul {
            list-style: none;
            padding: 0;
        }
        
        .urban-factors li {
            background: white;
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 8px;
            border-left: 3px solid #81c784;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(to top, rgba(255,255,255,0.95), transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 998;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(0,0,0,0.1);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #81c784);
            width: 0%;
            border-radius: 2px;
            transition: width 0.3s ease;
        }
        
        @media (max-width: 768px) {
            .hero-overlay h1 {
                font-size: 24px;
            }
            
            .content {
                margin: -20px 15px 15px 15px;
                padding: 25px 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero-image">
        <div class="hero-overlay">
            <h1>Vitalität zwischen Beton und Stahl</h1>
        </div>
    </div>
    
    <div class="content">
        <div class="article-meta">
            <span class="category">Vogelökologie</span>
            <span class="read-time">📖 9 Minuten Lesezeit</span>
            <span class="difficulty intermediate">🟡 Mittelstufe</span>
        </div>
        
        <div class="quote-box">
            <div class="quote-text">Städte bieten Vögeln neue Möglichkeiten und Herausforderungen; diejenigen, die sich erfolgreich an das städtische Leben anpassen, zeigen bemerkenswerte Plastizität.</div>
            <div class="quote-author">— Stadtökologe</div>
        </div>
        
        <div class="section-title">🏙️ Merkmale städtischer Umgebungen</div>
        <div class="main-text">
            Städtische Umgebungen unterscheiden sich erheblich von natürlichen Lebensräumen und stellen Vögel vor einzigartige Überlebensherausforderungen und -möglichkeiten.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🏢 Physische Umgebung</h4>
                <ul>
                    <li>Dichte Bebauung, fragmentierte Grünflächen</li>
                    <li>Erhöhte Hartflächen, reduzierte Durchlässigkeit</li>
                    <li>Künstliche Lichtquellen, nächtliche Beleuchtung</li>
                    <li>Erhöhte Temperaturen (Wärmeinseleffekt)</li>
                    <li>Veränderte Windrichtungen und Luftströmungsmuster</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🌱 Biologische Umgebung</h4>
                <ul>
                    <li>Begrenzte Pflanzenarten, meist nicht-einheimisch</li>
                    <li>Künstlich bereitgestellte Nahrung</li>
                    <li>Veränderungen bei Raubtierarten und -zahlen</li>
                    <li>Veränderte Krankheitsübertragungsmuster</li>
                    <li>Reduzierte Biodiversität</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>👥 Soziale Umgebung</h4>
                <ul>
                    <li>Häufige menschliche Aktivitäten</li>
                    <li>Starke Lärmbelastung</li>
                    <li>Hohes Verkehrsaufkommen</li>
                    <li>Erhöhte chemische Schadstoffe</li>
                    <li>Häufige menschliche Störungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🦅 Anpassungsstrategien städtischer Vögel</div>
        <div class="main-text">
            Vögel, die erfolgreich in Städten überleben, haben verschiedene Anpassungsstrategien entwickelt.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🎭 Verhaltensanpassungen</h4>
                <ul>
                    <li>Änderung der Ruffrequenz und -lautstärke</li>
                    <li>Anpassung der Aktivitätszeiten zur Vermeidung von Stoßzeiten</li>
                    <li>Erlernen der Nutzung künstlicher Strukturen zum Nisten</li>
                    <li>Änderung des Nahrungssuchverhaltens und der Ernährung</li>
                    <li>Erhöhte Toleranz gegenüber Menschen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🧬 Physiologische Anpassungen</h4>
                <ul>
                    <li>Regulation der Stresshormonspiegel</li>
                    <li>Veränderungen der Immunsystemfunktion</li>
                    <li>Anpassungen der Stoffwechselrate</li>
                    <li>Regulation der Brutzyklen</li>
                    <li>Veränderungen der Sinnessystemempfindlichkeit</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📏 Morphologische Anpassungen</h4>
                <ul>
                    <li>Veränderungen der Körpergröße</li>
                    <li>Anpassungen der Flügelform</li>
                    <li>Modifikationen der Schnabelstruktur</li>
                    <li>Veränderungen der Gefiederfärbung</li>
                    <li>Anpassungen der Beinstruktur</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🏠 Städtische Lebensraumtypen</div>
        <div class="main-text">
            Städte enthalten mehrere Arten von Vogellebensräumen, jeder mit seinen eigenen Merkmalen und unterstützten Vogelgemeinschaften.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🌳 Stadtparks</h4>
                <ul>
                    <li>Relativ große Grünflächen</li>
                    <li>Höhere Pflanzenvielfalt</li>
                    <li>Unterstützung mehrerer Vogelarten</li>
                    <li>Hohe Intensität menschlicher Verwaltung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏘️ Wohngrünflächen</h4>
                <ul>
                    <li>Kleine, verstreute Grünflächen</li>
                    <li>Relativ begrenzte Pflanzenarten</li>
                    <li>Häufige menschliche Störungen</li>
                    <li>Hochanpassungsfähige Arten dominieren</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>💧 Städtische Gewässer</h4>
                <ul>
                    <li>Künstliche Seen und Flüsse</li>
                    <li>Wasserqualität kann verschmutzt sein</li>
                    <li>Unterstützung des Überlebens von Wasservögeln</li>
                    <li>Umgebende Grüngürtel sind wichtig</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏢 Gebaute Umgebung</h4>
                <ul>
                    <li>Hohe Gebäude bieten Nistplätze</li>
                    <li>Dachgärten erhöhen Grünflächen</li>
                    <li>Gebäudespalten werden zu Lebensräumen</li>
                    <li>Künstliche Strukturen imitieren natürliche Umgebungen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🍎 Nahrungsquellen für städtische Vögel</div>
        <div class="main-text">
            Städtische Umgebungen bieten Vögeln vielfältige Nahrungsquellen, einschließlich natürlicher und künstlicher Quellen.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🌿 Natürliche Nahrungsquellen</h4>
                <ul>
                    <li>Früchte und Samen von Stadtpflanzen</li>
                    <li>Insekten und andere wirbellose Tiere</li>
                    <li>Kleine Wirbeltiere</li>
                    <li>Nektar und Pollen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏠 Künstliche Nahrungsquellen</h4>
                <ul>
                    <li>Von Menschen bereitgestellte Nahrung</li>
                    <li>Nahrungsreste im Müll</li>
                    <li>Haustierfutter</li>
                    <li>Vogelfutterstellen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>⚠️ Auswirkungen künstlicher Fütterung</h4>
                <ul>
                    <li>Veränderung natürlicher Verhaltensweisen der Vögel</li>
                    <li>Mögliche Verursachung von Nährstoffungleichgewichten</li>
                    <li>Erhöhung der Krankheitsübertragungsrisiken</li>
                    <li>Beeinflussung der Populationsstrukturen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🏗️ Ökologische Auswirkungen der Urbanisierung</div>
        <div class="main-text">
            Der Urbanisierungsprozess hat tiefgreifende Auswirkungen auf Vogelgemeinschaften.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🦜 Veränderungen der Artenzusammensetzung</h4>
                <ul>
                    <li>Zunahme hochanpassungsfähiger Arten</li>
                    <li>Abnahme spezialisierter Arten</li>
                    <li>Invasion nicht-einheimischer Arten</li>
                    <li>Verschwinden einheimischer Arten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📊 Veränderungen der Populationsdynamik</h4>
                <ul>
                    <li>Dramatische Zunahmen bestimmter Arten</li>
                    <li>Weitere Reduzierung seltener Arten</li>
                    <li>Ungleichmäßige Populationsdichteverteilung</li>
                    <li>Veränderungen der Bruterfolgsraten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🌐 Veränderungen der Gemeinschaftsstruktur</h4>
                <ul>
                    <li>Reduzierte Artenvielfalt</li>
                    <li>Verringerte funktionale Vielfalt</li>
                    <li>Vereinfachte Nahrungsnetze</li>
                    <li>Erhöhte Nischenüberlappung</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🚧 Bedrohungen für städtische Vögel</div>
        <div class="main-text">
            Städtische Umgebungen stellen mehrere Bedrohungen für Vögel dar.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>💥 Kollisionsbedrohungen</h4>
                <ul>
                    <li>Kollisionen mit Gebäudeglas</li>
                    <li>Fahrzeugkollisionen</li>
                    <li>Windturbinenverletzungen</li>
                    <li>Stromschläge an Stromleitungen</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏭 Verschmutzungsbedrohungen</h4>
                <ul>
                    <li>Luftverschmutzung</li>
                    <li>Wasserverschmutzung</li>
                    <li>Lärmverschmutzung</li>
                    <li>Lichtverschmutzung</li>
                    <li>Chemische Verschmutzung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🐱 Biologische Bedrohungen</h4>
                <ul>
                    <li>Beutegreifung durch streunende Katzen</li>
                    <li>Krankheitsübertragung</li>
                    <li>Konkurrenz durch nicht-einheimische Arten</li>
                    <li>Parasiteninfektionen</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">🌱 Naturschutzstrategien für städtische Vögel</div>
        <div class="main-text">
            Der Schutz städtischer Vögel erfordert umfassende Managementstrategien.
        </div>
        
        <div class="urban-section">
            <div class="urban-factors">
                <h4>🏞️ Lebensraummanagement</h4>
                <ul>
                    <li>Erhöhung der städtischen Grünflächenfläche</li>
                    <li>Verbesserung der Grünflächenverbindung</li>
                    <li>Anpflanzung einheimischer Vegetation</li>
                    <li>Schaffung mehrschichtiger Vegetationsstrukturen</li>
                    <li>Schutz und Wiederherstellung von Feuchtgebieten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🏢 Verbesserungen des Gebäudedesigns</h4>
                <ul>
                    <li>Verwendung vogelfreundlichen Glases</li>
                    <li>Gestaltung von Gründächern</li>
                    <li>Bereitstellung künstlicher Nistkästen</li>
                    <li>Reduzierung der Lichtverschmutzung</li>
                    <li>Schaffung vertikaler Begrünung</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>📋 Politische Maßnahmen</h4>
                <ul>
                    <li>Entwicklung städtischer Vogelschutzvorschriften</li>
                    <li>Regulierung der Stadtentwicklung</li>
                    <li>Kontrolle streunender Katzenpopulationen</li>
                    <li>Begrenzung des Chemikalieneinsatzes</li>
                    <li>Förderung von Öko-Stadt-Konzepten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>👥 Öffentliche Beteiligung</h4>
                <ul>
                    <li>Durchführung von Vogelüberwachungsaktivitäten</li>
                    <li>Verbreitung von Vogelschutzwissen</li>
                    <li>Förderung wissenschaftlicher Vogelfütterung</li>
                    <li>Aufbau von Freiwilligennetzwerken</li>
                    <li>Unterstützung von Naturschutzprojekten</li>
                </ul>
            </div>
            
            <div class="urban-factors">
                <h4>🔮 Zukünftige Entwicklungsrichtungen</h4>
                <ul>
                    <li>Integration von Smart Cities und Vogelschutz</li>
                    <li>Big Data-basierte Vogelüberwachung</li>
                    <li>Ökologische Stadtplanung und -gestaltung</li>
                    <li>Modelle für harmonisches Zusammenleben von Mensch und Vogel</li>
                    <li>Städtischer Biodiversitätsschutz</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('de/ecology/06-urban-ecology.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已更新: 06-urban-ecology.html")

def create_article_07():
    """创建德语版本的第7篇文章 - 保护生物学"""
    content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Naturschutzbiologie - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_conservation_biology.webp') center/cover;
            position: relative;
            margin-top: 0;
        }
        
        .hero-overlay {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            color: white;
        }
        
        .hero-overlay h1 {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .content {
            background: white;
            margin: -30px 20px 20px 20px;
            border-radius: 20px;
            padding: 40px 20px 30px 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            min-height: 80vh;
        }
        
        .article-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .category {
            background: #4caf50;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .read-time, .difficulty {
            background: #f5f5f5;
            color: #666;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .difficulty.advanced {
            background: #ffebee;
            color: #c62828;
        }
        
        .quote-box {
            background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 25px 0;
            border-radius: 8px;
            position: relative;
        }
        
        .quote-box::before {
            content: '"';
            font-size: 48px;
            color: #4caf50;
            position: absolute;
            top: -5px;
            left: 15px;
            font-family: serif;
            line-height: 1;
        }
        
        .quote-text {
            font-size: 16px;
            font-weight: 600;
            color: #2e7d32;
            margin-left: 25px;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .quote-author {
            font-size: 14px;
            color: #388e3c;
            margin-left: 25px;
            font-style: italic;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #4caf50;
            margin: 30px 0 15px 0;
            border-bottom: 2px solid #c8e6c9;
            padding-bottom: 8px;
        }
        
        .main-text {
            font-size: 16px;
            line-height: 1.8;
            color: #333;
            margin: 20px 0;
            text-align: justify;
        }
        
        .conservation-section {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .conservation-factors h4 {
            color: #2e7d32;
            font-size: 16px;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .conservation-factors ul {
            list-style: none;
            padding: 0;
        }
        
        .conservation-factors li {
            background: white;
            margin: 8px 0;
            padding: 10px 15px;
            border-radius: 8px;
            border-left: 3px solid #81c784;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .progress-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(to top, rgba(255,255,255,0.95), transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 998;
        }
        
        .progress-bar {
            width: 200px;
            height: 4px;
            background: rgba(0,0,0,0.1);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4caf50, #81c784);
            width: 0%;
            border-radius: 2px;
            transition: width 0.3s ease;
        }
        
        @media