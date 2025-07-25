#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 定义所有语言目录
languages = ['de', 'pt', 'ko', 'ja', 'es', 'fr', 'it', 'ru', 'zh']

def get_main_content(lang_code):
    """获取主要内容"""
    content = {
        'de': 'Professionelle Vogelforschung und ornithologische Studien erfordern spezialisierte Ausrüstung, die über grundlegende Vogelbeobachtungsgeräte hinausgeht. Diese wissenschaftlichen Werkzeuge ermöglichen es Forschern, detaillierte Studien durchzuführen, Daten zu sammeln und unser Verständnis der Vogelbiologie voranzutreiben<span class="emoji">🔬</span>. Dieser Leitfaden behandelt die wesentliche Ausrüstung für professionelle Vogelforschung und fortgeschrittene Studien.',
        'pt': 'A pesquisa profissional de aves e estudos ornitológicos requerem equipamentos especializados que vão além dos equipamentos básicos de observação de aves. Essas ferramentas científicas permitem aos pesquisadores conduzir estudos detalhados, coletar dados e avançar nossa compreensão da biologia aviária<span class="emoji">🔬</span>. Este guia aborda os equipamentos essenciais usados na pesquisa profissional de aves e estudos avançados.',
        'ko': '전문적인 조류 연구와 조류학 연구는 기본적인 조류 관찰 장비를 넘어서는 전문 장비가 필요합니다. 이러한 과학적 도구들은 연구자들이 상세한 연구를 수행하고, 데이터를 수집하며, 조류 생물학에 대한 우리의 이해를 발전시킬 수 있게 합니다<span class="emoji">🔬</span>. 이 가이드는 전문 조류 연구와 고급 연구에 사용되는 필수 장비를 다룹니다.',
        'ja': '専門的な鳥類研究と鳥類学研究には、基本的なバードウォッチング機器を超えた専門機器が必要です。これらの科学的ツールにより、研究者は詳細な研究を行い、データを収集し、鳥類生物学の理解を進めることができます<span class="emoji">🔬</span>。このガイドでは、専門的な鳥類研究と高度な研究で使用される必須機器について説明します。',
        'es': 'La investigación profesional de aves y los estudios ornitológicos requieren equipos especializados que van más allá del equipo básico de observación de aves. Estas herramientas científicas permiten a los investigadores realizar estudios detallados, recopilar datos y avanzar en nuestra comprensión de la biología aviaria<span class="emoji">🔬</span>. Esta guía cubre el equipo esencial utilizado en la investigación profesional de aves y estudios avanzados.',
        'fr': 'La recherche professionnelle sur les oiseaux et les études ornithologiques nécessitent des équipements spécialisés qui vont au-delà de l\'équipement de base d\'observation des oiseaux. Ces outils scientifiques permettent aux chercheurs de mener des études détaillées, de collecter des données et de faire progresser notre compréhension de la biologie aviaire<span class="emoji">🔬</span>. Ce guide couvre l\'équipement essentiel utilisé dans la recherche professionnelle sur les oiseaux et les études avancées.',
        'it': 'La ricerca professionale sugli uccelli e gli studi ornitologici richiedono attrezzature specializzate che vanno oltre l\'equipaggiamento di base per l\'osservazione degli uccelli. Questi strumenti scientifici consentono ai ricercatori di condurre studi dettagliati, raccogliere dati e far progredire la nostra comprensione della biologia aviaria<span class="emoji">🔬</span>. Questa guida copre l\'attrezzatura essenziale utilizzata nella ricerca professionale sugli uccelli e negli studi avanzati.',
        'ru': 'Профессиональные исследования птиц и орнитологические исследования требуют специализированного оборудования, выходящего за рамки базового оборудования для наблюдения за птицами. Эти научные инструменты позволяют исследователям проводить детальные исследования, собирать данные и продвигать наше понимание биологии птиц<span class="emoji">🔬</span>. Это руководство охватывает основное оборудование, используемое в профессиональных исследованиях птиц и продвинутых исследованиях.',
        'zh': '专业鸟类研究和鸟类学研究需要超越基本观鸟设备的专业设备。这些科学工具使研究人员能够进行详细研究、收集数据并推进我们对鸟类生物学的理解<span class="emoji">🔬</span>。本指南涵盖了专业鸟类研究和高级研究中使用的基本设备。'
    }
    return content.get(lang_code, content['zh'])

def get_section_title_1(lang_code):
    """获取第一个章节标题"""
    titles = {
        'de': 'Beringung und Markierungsausrüstung',
        'pt': 'Equipamentos de Anilhamento e Marcação',
        'ko': '링잉 및 마킹 장비',
        'ja': 'リンギングとマーキング機器',
        'es': 'Equipos de Anillamiento y Marcado',
        'fr': 'Équipements de Baguage et de Marquage',
        'it': 'Attrezzature per Inanellamento e Marcatura',
        'ru': 'Оборудование для Кольцевания и Маркировки',
        'zh': '环志和标记设备'
    }
    return titles.get(lang_code, titles['zh'])

def get_section_content_1(lang_code):
    """获取第一个章节内容"""
    content = {
        'de': 'Die Vogelberingung ist eine wichtige Forschungstechnik zur Verfolgung einzelner Vögel über die Zeit. Professionelle Forscher verwenden spezialisierte Ausrüstung, einschließlich nummerierter Metallringe, Farbringe und Anwendungswerkzeuge<span class="emoji">🏷️</span>. Moderne Forschung nutzt auch GPS-Sender und Radiotelemetrie-Geräte zur Verfolgung von Zugmustern und Verhalten.',
        'pt': 'O anilhamento de aves é uma técnica de pesquisa importante para rastrear aves individuais ao longo do tempo. Pesquisadores profissionais usam equipamentos especializados, incluindo anéis metálicos numerados, anéis coloridos e ferramentas de aplicação<span class="emoji">🏷️</span>. A pesquisa moderna também emprega transmissores GPS e dispositivos de radiotelemetria para rastrear padrões de migração e comportamento.',
        'ko': '조류 링잉은 시간에 따른 개별 조류를 추적하는 중요한 연구 기법입니다. 전문 연구자들은 번호가 매겨진 금속 링, 컬러 링, 적용 도구를 포함한 전문 장비를 사용합니다<span class="emoji">🏷️</span>. 현대 연구는 또한 GPS 송신기와 무선 원격 측정 장치를 사용하여 이주 패턴과 행동을 추적합니다.',
        'ja': '鳥類のリンギングは、時間の経過とともに個々の鳥を追跡する重要な研究技術です。専門研究者は、番号付き金属リング、カラーリング、適用ツールを含む専門機器を使用します<span class="emoji">🏷️</span>。現代の研究では、GPS送信機と無線テレメトリー装置も使用して、移住パターンと行動を追跡します。',
        'es': 'El anillamiento de aves es una técnica de investigación importante para rastrear aves individuales a lo largo del tiempo. Los investigadores profesionales utilizan equipos especializados, incluyendo anillos metálicos numerados, anillos de colores y herramientas de aplicación<span class="emoji">🏷️</span>. La investigación moderna también emplea transmisores GPS y dispositivos de radiotelemetría para rastrear patrones de migración y comportamiento.',
        'fr': 'Le baguage des oiseaux est une technique de recherche importante pour suivre les oiseaux individuels dans le temps. Les chercheurs professionnels utilisent des équipements spécialisés, y compris des bagues métalliques numérotées, des bagues colorées et des outils d\'application<span class="emoji">🏷️</span>. La recherche moderne emploie également des émetteurs GPS et des dispositifs de radiotélémétrie pour suivre les modèles de migration et le comportement.',
        'it': 'L\'inanellamento degli uccelli è una tecnica di ricerca importante per tracciare singoli uccelli nel tempo. I ricercatori professionali utilizzano attrezzature specializzate, inclusi anelli metallici numerati, anelli colorati e strumenti di applicazione<span class="emoji">🏷️</span>. La ricerca moderna impiega anche trasmettitori GPS e dispositivi di radiotelemetria per tracciare i modelli di migrazione e il comportamento.',
        'ru': 'Кольцевание птиц является важной исследовательской техникой для отслеживания отдельных птиц во времени. Профессиональные исследователи используют специализированное оборудование, включая пронумерованные металлические кольца, цветные кольца и инструменты для применения<span class="emoji">🏷️</span>. Современные исследования также используют GPS-передатчики и радиотелеметрические устройства для отслеживания миграционных паттернов и поведения.',
        'zh': '鸟类环志是追踪个体鸟类随时间变化的重要研究技术。专业研究人员使用专门设备，包括编号金属环、彩色环和应用工具<span class="emoji">🏷️</span>。现代研究还采用GPS发射器和无线电遥测设备来追踪迁徙模式和行为。'
    }
    return content.get(lang_code, content['zh'])

def get_equipment_title_1(lang_code):
    """获取设备标题1"""
    titles = {
        'de': '🏷️ Beringungsausrüstung',
        'pt': '🏷️ Equipamentos de Anilhamento',
        'ko': '🏷️ 링잉 장비',
        'ja': '🏷️ リンギング機器',
        'es': '🏷️ Equipos de Anillamiento',
        'fr': '🏷️ Équipements de Baguage',
        'it': '🏷️ Attrezzature per Inanellamento',
        'ru': '🏷️ Оборудование для Кольцевания',
        'zh': '🏷️ 环志设备'
    }
    return titles.get(lang_code, titles['zh'])

def get_equipment_desc_1(lang_code):
    """获取设备描述1"""
    desc = {
        'de': '<strong>Metallringe:</strong> Nummerierte Aluminiumringe für permanente Identifikation<br><strong>Farbringe:</strong> Kunststoffringe für Feldidentifikation<br><strong>Beringungszangen:</strong> Spezialisierte Werkzeuge für sichere Ringanbringung<br><strong>Ringgrößenführer:</strong> Referenztabellen für korrekte Ringgrößen',
        'pt': '<strong>Anéis Metálicos:</strong> Anéis de alumínio numerados para identificação permanente<br><strong>Anéis Coloridos:</strong> Anéis de plástico para identificação em campo<br><strong>Alicates de Anilhamento:</strong> Ferramentas especializadas para aplicação segura de anéis<br><strong>Guias de Tamanho de Anéis:</strong> Tabelas de referência para tamanhos corretos de anéis',
        'ko': '<strong>금속 링:</strong> 영구 식별을 위한 번호가 매겨진 알루미늄 링<br><strong>컬러 링:</strong> 야외 식별을 위한 플라스틱 링<br><strong>링잉 플라이어:</strong> 안전한 링 적용을 위한 전문 도구<br><strong>링 크기 가이드:</strong> 올바른 링 크기를 위한 참조 차트',
        'ja': '<strong>金属リング:</strong> 永続的な識別のための番号付きアルミニウムリング<br><strong>カラーリング:</strong> フィールド識別のためのプラスチックリング<br><strong>リンギングプライヤー:</strong> 安全なリング適用のための専門ツール<br><strong>リングサイズガイド:</strong> 正しいリングサイズのための参照チャート',
        'es': '<strong>Anillos Metálicos:</strong> Anillos de aluminio numerados para identificación permanente<br><strong>Anillos de Colores:</strong> Anillos de plástico para identificación en campo<br><strong>Alicates de Anillamiento:</strong> Herramientas especializadas para aplicación segura de anillos<br><strong>Guías de Tamaño de Anillos:</strong> Tablas de referencia para tamaños correctos de anillos',
        'fr': '<strong>Bagues Métalliques:</strong> Bagues en aluminium numérotées pour identification permanente<br><strong>Bagues Colorées:</strong> Bagues en plastique pour identification sur le terrain<br><strong>Pinces à Baguer:</strong> Outils spécialisés pour application sécurisée des bagues<br><strong>Guides de Taille de Bagues:</strong> Tableaux de référence pour les tailles correctes de bagues',
        'it': '<strong>Anelli Metallici:</strong> Anelli di alluminio numerati per identificazione permanente<br><strong>Anelli Colorati:</strong> Anelli di plastica per identificazione sul campo<br><strong>Pinze per Inanellamento:</strong> Strumenti specializzati per applicazione sicura degli anelli<br><strong>Guide delle Dimensioni degli Anelli:</strong> Tabelle di riferimento per le dimensioni corrette degli anelli',
        'ru': '<strong>Металлические Кольца:</strong> Пронумерованные алюминиевые кольца для постоянной идентификации<br><strong>Цветные Кольца:</strong> Пластиковые кольца для полевой идентификации<br><strong>Щипцы для Кольцевания:</strong> Специализированные инструменты для безопасного применения колец<br><strong>Руководства по Размерам Колец:</strong> Справочные таблицы для правильных размеров колец',
        'zh': '<strong>金属环:</strong> 用于永久识别的编号铝环<br><strong>彩色环:</strong> 用于野外识别的塑料环<br><strong>环志钳:</strong> 安全应用环的专用工具<br><strong>环尺寸指南:</strong> 正确环尺寸的参考图表'
    }
    return desc.get(lang_code, desc['zh'])

def get_equipment_title_2(lang_code):
    """获取设备标题2"""
    titles = {
        'de': '📡 Verfolgungstechnologie',
        'pt': '📡 Tecnologia de Rastreamento',
        'ko': '📡 추적 기술',
        'ja': '📡 追跡技術',
        'es': '📡 Tecnología de Seguimiento',
        'fr': '📡 Technologie de Suivi',
        'it': '📡 Tecnologia di Tracciamento',
        'ru': '📡 Технология Отслеживания',
        'zh': '📡 追踪技术'
    }
    return titles.get(lang_code, titles['zh'])

def get_equipment_desc_2(lang_code):
    """获取设备描述2"""
    desc = {
        'de': '<strong>GPS-Sender:</strong> Satellitenbasierte Verfolgungsgeräte für Zugstudien<br><strong>Radiosender:</strong> VHF-Sender für lokale Verfolgung<br><strong>Geolokatoren:</strong> Lichtbasierte Positionsrekorder<br><strong>Empfangsgeräte:</strong> Antennen und Empfänger für Signaldetektion',
        'pt': '<strong>Transmissores GPS:</strong> Dispositivos de rastreamento por satélite para estudos de migração<br><strong>Transmissores de Rádio:</strong> Transmissores VHF para rastreamento local<br><strong>Geolocalizadores:</strong> Registradores de posição baseados em luz<br><strong>Equipamentos de Recepção:</strong> Antenas e receptores para detecção de sinais',
        'ko': '<strong>GPS 송신기:</strong> 이주 연구를 위한 위성 기반 추적 장치<br><strong>무선 송신기:</strong> 지역 추적을 위한 VHF 송신기<br><strong>지오로케이터:</strong> 빛 기반 위치 기록기<br><strong>수신 장비:</strong> 신호 감지를 위한 안테나와 수신기',
        'ja': '<strong>GPS送信機:</strong> 移住研究のための衛星ベースの追跡装置<br><strong>無線送信機:</strong> 地域追跡のためのVHF送信機<br><strong>ジオロケーター:</strong> 光ベースの位置記録装置<br><strong>受信機器:</strong> 信号検出のためのアンテナと受信機',
        'es': '<strong>Transmisores GPS:</strong> Dispositivos de seguimiento satelital para estudios de migración<br><strong>Transmisores de Radio:</strong> Transmisores VHF para seguimiento local<br><strong>Geolocalizadores:</strong> Registradores de posición basados en luz<br><strong>Equipos de Recepción:</strong> Antenas y receptores para detección de señales',
        'fr': '<strong>Émetteurs GPS:</strong> Dispositifs de suivi par satellite pour études de migration<br><strong>Émetteurs Radio:</strong> Émetteurs VHF pour suivi local<br><strong>Géolocalisateurs:</strong> Enregistreurs de position basés sur la lumière<br><strong>Équipements de Réception:</strong> Antennes et récepteurs pour détection de signaux',
        'it': '<strong>Trasmettitori GPS:</strong> Dispositivi di tracciamento satellitare per studi di migrazione<br><strong>Trasmettitori Radio:</strong> Trasmettitori VHF per tracciamento locale<br><strong>Geolocatori:</strong> Registratori di posizione basati sulla luce<br><strong>Attrezzature di Ricezione:</strong> Antenne e ricevitori per rilevamento segnali',
        'ru': '<strong>GPS-Передатчики:</strong> Спутниковые устройства слежения для исследований миграции<br><strong>Радиопередатчики:</strong> VHF-передатчики для локального отслеживания<br><strong>Геолокаторы:</strong> Световые регистраторы положения<br><strong>Приемное Оборудование:</strong> Антенны и приемники для обнаружения сигналов',
        'zh': '<strong>GPS发射器:</strong> 用于迁徙研究的卫星追踪设备<br><strong>无线电发射器:</strong> 用于本地追踪的VHF发射器<br><strong>地理定位器:</strong> 基于光线的位置记录器<br><strong>接收设备:</strong> 用于信号检测的天线和接收器'
    }
    return desc.get(lang_code, desc['zh'])

def get_section_title_2(lang_code):
    """获取第二个章节标题"""
    titles = {
        'de': 'Fang- und Handhabungsausrüstung',
        'pt': 'Equipamentos de Captura e Manuseio',
        'ko': '포획 및 처리 장비',
        'ja': '捕獲と取り扱い機器',
        'es': 'Equipos de Captura y Manejo',
        'fr': 'Équipements de Capture et de Manipulation',
        'it': 'Attrezzature per Cattura e Manipolazione',
        'ru': 'Оборудование для Отлова и Обращения',
        'zh': '捕获和处理设备'
    }
    return titles.get(lang_code, titles['zh'])

def get_section_content_2(lang_code):
    """获取第二个章节内容"""
    content = {
        'de': 'Sicherer Vogelfang für Forschungszwecke erfordert speziell entwickelte Netze und Fallen, um Stress und Verletzungen zu minimieren. Nebelnetze sind die häufigste Fangmethode und erfordern ordnungsgemäße Aufstellung und kontinuierliche Überwachung<span class="emoji">🕸️</span>. Professionelle Handhabungstechniken und -ausrüstung gewährleisten die Sicherheit der Vögel während der Forschung.',
        'pt': 'A captura segura de aves para fins de pesquisa requer redes e armadilhas especialmente projetadas para minimizar o estresse e lesões. Redes de neblina são o método de captura mais comum, exigindo configuração adequada e monitoramento contínuo<span class="emoji">🕸️</span>. Técnicas e equipamentos de manuseio profissionais garantem a segurança das aves durante a pesquisa.',
        'ko': '연구 목적의 안전한 조류 포획은 스트레스와 부상을 최소화하기 위해 특별히 설
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 定义所有语言目录
languages = ['de', 'pt', 'ko', 'ja', 'es', 'fr', 'it', 'ru', 'zh']

def update_language_file(lang_code):
    """为指定语言更新设备文件"""
    
    # 语言特定的翻译
    translations = {
        'de': {
            'title': 'Vogelforschungsausrüstung und Forschungswerkzeuge - BirdAiSnap',
            'main_title': '🔬 Vogelforschungsausrüstung und Forschungswerkzeuge',
            'quote': 'Entdecken Sie die wissenschaftlichen Werkzeuge und Ausrüstungen für ornithologische Forschung und professionelle Vogelstudien'
        },
        'pt': {
            'title': 'Equipamentos de Estudo de Aves e Ferramentas de Pesquisa - BirdAiSnap',
            'main_title': '🔬 Equipamentos de Estudo de Aves e Ferramentas de Pesquisa',
            'quote': 'Explore as ferramentas científicas e equipamentos usados em pesquisa ornitológica e estudo profissional de aves'
        },
        'ko': {
            'title': '조류 연구 장비 및 연구 도구 - BirdAiSnap',
            'main_title': '🔬 조류 연구 장비 및 연구 도구',
            'quote': '조류학 연구와 전문적인 조류 연구에 사용되는 과학적 도구와 장비를 탐구하세요'
        },
        'ja': {
            'title': '鳥類研究機器と研究ツール - BirdAiSnap',
            'main_title': '🔬 鳥類研究機器と研究ツール',
            'quote': '鳥類学研究と専門的な鳥類研究で使用される科学的ツールと機器を探求しましょう'
        },
        'es': {
            'title': 'Equipos de Estudio de Aves y Herramientas de Investigación - BirdAiSnap',
            'main_title': '🔬 Equipos de Estudio de Aves y Herramientas de Investigación',
            'quote': 'Explora las herramientas científicas y equipos utilizados en investigación ornitológica y estudio profesional de aves'
        },
        'fr': {
            'title': 'Équipements d\'Étude des Oiseaux et Outils de Recherche - BirdAiSnap',
            'main_title': '🔬 Équipements d\'Étude des Oiseaux et Outils de Recherche',
            'quote': 'Explorez les outils scientifiques et équipements utilisés dans la recherche ornithologique et l\'étude professionnelle des oiseaux'
        },
        'it': {
            'title': 'Attrezzature per lo Studio degli Uccelli e Strumenti di Ricerca - BirdAiSnap',
            'main_title': '🔬 Attrezzature per lo Studio degli Uccelli e Strumenti di Ricerca',
            'quote': 'Esplora gli strumenti scientifici e le attrezzature utilizzate nella ricerca ornitologica e nello studio professionale degli uccelli'
        },
        'ru': {
            'title': 'Оборудование для Изучения Птиц и Исследовательские Инструменты - BirdAiSnap',
            'main_title': '🔬 Оборудование для Изучения Птиц и Исследовательские Инструменты',
            'quote': 'Исследуйте научные инструменты и оборудование, используемые в орнитологических исследованиях и профессиональном изучении птиц'
        },
        'zh': {
            'title': '鸟类研究设备和研究工具 - BirdAiSnap',
            'main_title': '🔬 鸟类研究设备和研究工具',
            'quote': '探索鸟类学研究和专业鸟类研究中使用的科学工具和设备'
        }
    }
    
    if lang_code not in translations:
        print(f"❌ 语言 {lang_code} 的翻译未定义")
        return False
    
    trans = translations[lang_code]
    
    # 创建HTML内容（简化版本）
    html_content = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{trans['title']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.95);
            margin-top: 20px;
            margin-bottom: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        
        .title {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        .quote-box {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .quote-text {{
            font-size: 1.2em;
            font-style: italic;
        }}
        
        .section-title {{
            color: #2c3e50;
            font-size: 1.5em;
            margin: 25px 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .main-text {{
            color: #34495e;
            margin: 15px 0;
            font-size: 1.1em;
            text-align: justify;
        }}
        
        .tip-box {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }}
        
        .tip-title {{
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 1.1em;
        }}
        
        .equipment-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .equipment-card {{
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .equipment-title {{
            color: #2c3e50;
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .equipment-description {{
            color: #34495e;
            font-size: 1em;
            line-height: 1.5;
        }}
        
        .emoji {{
            font-size: 1.2em;
            margin: 0 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">{trans['main_title']}</h1>
        
        <div class="quote-box">
            <div class="quote-text">
                {trans['quote']}
            </div>
        </div>
        
        <div class="main-text">
            {get_main_content(lang_code)}
        </div>
        
        <div class="section-title">{get_section_title_1(lang_code)}</div>
        <div class="main-text">
            {get_section_content_1(lang_code)}
        </div>
        
        <div class="equipment-grid">
            <div class="equipment-card">
                <div class="equipment-title">{get_equipment_title_1(lang_code)}</div>
                <div class="equipment-description">
                    {get_equipment_desc_1(lang_code)}
                </div>
            </div>
            
            <div class="equipment-card">
                <div class="equipment-title">{get_equipment_title_2(lang_code)}</div>
                <div class="equipment-description">
                    {get_equipment_desc_2(lang_code)}
                </div>
            </div>
        </div>
        
        <div class="section-title">{get_section_title_2(lang_code)}</div>
        <div class="main-text">
            {get_section_content_2(lang_code)}
        </div>
        
        <div class="tip-box">
            <div class="tip-title">{get_tip_title(lang_code)}</div>
            {get_tip_content(lang_code)}
        </div>
        
        <div class="section-title">{get_section_title_3(lang_code)}</div>
        <div class="main-text">
            {get_section_content_3(lang_code)}
        </div>
        
        <div class="section-title">{get_section_title_4(lang_code)}</div>
        <div class="main-text">
            {get_section_content_4(lang_code)}
        </div>
        
        <div class="main-text">
            {get_conclusion(lang_code)}
        </div>
    </div>
</body>
</html>'''
    
    # 创建目录路径
    file_path = f"{lang_code}/knowledge/02-essential-equipment.html"
    
    # 检查目录是否存在
    os.makedirs(f"{lang_code}/knowledge", exist_ok=True)
    
    # 写入文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ 已更新: {file_path}")
        return True
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("开始更新多语言设备文件...")
    
    success_count = 0
    for lang_code in languages:
        if update_language_file(lang_code):
            success_count += 1
    
    print(f"🎉 完成！成功更新了 {success_count}/{len(languages)} 个语言文件")

if __name__ == "__main__":
    main()