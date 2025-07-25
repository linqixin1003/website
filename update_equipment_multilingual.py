#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 定义所有语言目录
languages = {
    'de': 'Deutsch',
    'pt': 'Português', 
    'ko': '한국어',
    'ja': '日本語',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
    'ru': 'Русский',
    'zh': '中文'
}

# 翻译映射字典
translations = {
    'de': {
        'title': 'Vogelforschungsausrüstung und Forschungswerkzeuge - BirdAiSnap',
        'main_title': '🔬 Vogelforschungsausrüstung und Forschungswerkzeuge',
        'quote': 'Entdecken Sie die wissenschaftlichen Werkzeuge und Ausrüstungen für ornithologische Forschung und professionelle Vogelstudien',
        'intro': 'Professionelle Vogelstudien und ornithologische Forschung erfordern spezialisierte Ausrüstung über die grundlegende Vogelbeobachtungsausrüstung hinaus. Diese wissenschaftlichen Werkzeuge ermöglichen es Forschern, detaillierte Studien durchzuführen, Daten zu sammeln und unser Verständnis der Vogelbiologie zu erweitern<span class="emoji">🔬</span>. Dieser Leitfaden behandelt die wesentliche Ausrüstung für professionelle Vogelforschung und fortgeschrittene Studien.',
        'banding_title': 'Beringungs- und Markierungsausrüstung',
        'banding_text': 'Vogelberingung ist eine entscheidende Forschungstechnik zur Verfolgung einzelner Vögel über die Zeit. Professionelle Forscher verwenden spezialisierte Ausrüstung einschließlich nummerierter Metallringe, Farbringe und Anwendungswerkzeuge<span class="emoji">🏷️</span>. Moderne Studien verwenden auch GPS-Sender und Radiotelemetrie-Geräte zur Verfolgung von Wanderungsmustern und Verhalten.',
        'capture_title': 'Fang- und Handhabungsausrüstung',
        'capture_text': 'Sicherer Vogelfang für die Forschung erfordert spezialisierte Netze und Fallen, die darauf ausgelegt sind, Stress und Verletzungen zu minimieren. Nebelnetze sind die häufigste Fangmethode und erfordern ordnungsgemäße Aufstellung und ständige Überwachung<span class="emoji">🕸️</span>. Professionelle Handhabungstechniken und -ausrüstung gewährleisten die Vogelsicherheit während Forschungsverfahren.',
        'safety_title': '⚠️ Sicherheitsprotokoll',
        'safety_text': 'Vogelfang und -handhabung erfordern ordnungsgemäße Ausbildung, Genehmigungen und die Einhaltung strenger ethischer Richtlinien. Nur lizenzierte Forscher sollten diese Techniken verwenden.',
        'measurement_title': 'Mess- und Datensammlungswerkzeuge',
        'measurement_text': 'Präzise Messungen sind für ornithologische Forschung unerlässlich. Spezialisierte Messschieber, Lineale und Waagen für Vogelforschung liefern genaue morphometrische Daten<span class="emoji">📏</span>. Digitale Datenlogger und Feldcomputer rationalisieren die Datensammlung und reduzieren Transkriptionsfehler.',
        'nest_title': 'Nestüberwachungsausrüstung',
        'nest_text': 'Brutökologie-Studien erfordern spezialisierte Ausrüstung zur Überwachung von Nestern ohne Störung. Fernkameras, Temperaturlogger und ausziehbare Spiegel ermöglichen es Forschern, Nistverhalten und Erfolgsraten zu studieren<span class="emoji">🥚</span>. Moderne Technologie ermöglicht kontinuierliche Überwachung mit minimaler menschlicher Einmischung.',
        'acoustic_title': 'Akustische Forschungsausrüstung',
        'acoustic_text': 'Vogelstimmenstudien verwenden professionelle Aufnahmegeräte und Analysesoftware. Richtmikrofone, digitale Rekorder und Spektrogramm-Analyseprogramme ermöglichen detaillierte Studien der Vogelkommunikation<span class="emoji">🎵</span>. Automatisierte Aufnahmestationen können Vogelaktivität kontinuierlich über große Gebiete überwachen.',
        'research_title': '🔬 Forschungsanwendungen',
        'research_text': 'Diese Werkzeuge unterstützen verschiedene Forschungsbereiche einschließlich Wanderungsökologie, Brutbiologie, Populationsdynamik, Verhaltensstudien und Naturschutzbiologie.',
        'lab_title': 'Laborausrüstung',
        'lab_text': 'Laboranalyse von Vogelproben erfordert spezialisierte Ausrüstung für genetische, physiologische und pathologische Studien. Mikroskope, Zentrifugen und molekularbiologische Ausrüstung ermöglichen detaillierte Analyse von Federn, Blut und Gewebeproben<span class="emoji">🧪</span>. Diese Ausrüstung unterstützt Forschung in Evolution, Krankheitsökologie und Naturschutzgenetik.',
        'conclusion': 'Professionelle Vogelforschungsausrüstung stellt eine erhebliche Investition dar und erfordert ordnungsgemäße Ausbildung für sichere und effektive Nutzung. Diese Werkzeuge ermöglichen es Wissenschaftlern, präzise Daten zu sammeln, die unser Verständnis der Vogelbiologie fördern und Naturschutzbemühungen unterstützen<span class="emoji">🌟</span>. Die Wahl der Ausrüstung hängt von spezifischen Forschungszielen, Zielarten und Studiendesign-Anforderungen ab.'
    },
    'pt': {
        'title': 'Equipamentos de Estudo de Aves e Ferramentas de Pesquisa - BirdAiSnap',
        'main_title': '🔬 Equipamentos de Estudo de Aves e Ferramentas de Pesquisa',
        'quote': 'Explore as ferramentas científicas e equipamentos usados em pesquisa ornitológica e estudo profissional de aves',
        'intro': 'O estudo profissional de aves e a pesquisa ornitológica requerem equipamentos especializados além dos equipamentos básicos de observação de aves. Essas ferramentas científicas permitem aos pesquisadores conduzir estudos detalhados, coletar dados e avançar nosso entendimento da biologia aviária<span class="emoji">🔬</span>. Este guia cobre os equipamentos essenciais usados em pesquisa profissional de aves e estudo avançado.',
        'banding_title': 'Equipamentos de Anilhamento e Marcação',
        'banding_text': 'O anilhamento de aves é uma técnica de pesquisa crucial para rastrear aves individuais ao longo do tempo. Pesquisadores profissionais usam equipamentos especializados incluindo anilhas metálicas numeradas, anilhas coloridas e ferramentas de aplicação<span class="emoji">🏷️</span>. Estudos modernos também empregam transmissores GPS e dispositivos de radiotelemetria para rastrear padrões de migração e comportamento.',
        'capture_title': 'Equipamentos de Captura e Manuseio',
        'capture_text': 'A captura segura de aves para pesquisa requer redes e armadilhas especializadas projetadas para minimizar estresse e lesões. Redes de neblina são o método de captura mais comum, requerendo configuração adequada e monitoramento constante<span class="emoji">🕸️</span>. Técnicas e equipamentos profissionais de manuseio garantem a segurança das aves durante procedimentos de pesquisa.',
        'safety_title': '⚠️ Protocolo de Segurança',
        'safety_text': 'A captura e manuseio de aves requer treinamento adequado, licenças e aderência a diretrizes éticas rigorosas. Apenas pesquisadores licenciados devem usar essas técnicas.',
        'measurement_title': 'Ferramentas de Medição e Coleta de Dados',
        'measurement_text': 'Medições precisas são essenciais para pesquisa ornitológica. Paquímetros especializados, réguas e balanças projetadas para pesquisa de aves fornecem dados morfométricos precisos<span class="emoji">📏</span>. Registradores de dados digitais e computadores de campo simplificam a coleta de dados e reduzem erros de transcrição.',
        'nest_title': 'Equipamentos de Monitoramento de Ninhos',
        'nest_text': 'Estudos de ecologia reprodutiva requerem equipamentos especializados para monitorar ninhos sem perturbação. Câmeras remotas, registradores de temperatura e espelhos extensíveis permitem aos pesquisadores estudar comportamento de nidificação e taxas de sucesso<span class="emoji">🥚</span>. A tecnologia moderna permite monitoramento contínuo com interferência humana mínima.',
        'acoustic_title': 'Equipamentos de Pesquisa Acústica',
        'acoustic_text': 'Estudos de vocalização de aves usam equipamentos de gravação de nível profissional e software de análise. Microfones direcionais, gravadores digitais e programas de análise de espectrograma permitem estudo detalhado da comunicação aviária<span class="emoji">🎵</span>. Estações de gravação automatizadas podem monitorar atividade de aves continuamente em grandes áreas.',
        'research_title': '🔬 Aplicações de Pesquisa',
        'research_text': 'Essas ferramentas apoiam várias áreas de pesquisa incluindo ecologia de migração, biologia reprodutiva, dinâmica populacional, estudos comportamentais e biologia da conservação.',
        'lab_title': 'Equipamentos de Laboratório',
        'lab_text': 'A análise laboratorial de amostras de aves requer equipamentos especializados para estudos genéticos, fisiológicos e patológicos. Microscópios, centrífugas e equipamentos de biologia molecular permitem análise detalhada de penas, sangue e amostras de tecido<span class="emoji">🧪</span>. Esses equipamentos apoiam pesquisa em evolução, ecologia de doenças e genética da conservação.',
        'conclusion': 'Equipamentos profissionais de pesquisa de aves representam um investimento significativo e requerem treinamento adequado para uso seguro e eficaz. Essas ferramentas permitem aos cientistas coletar dados precisos que avançam nosso entendimento da biologia aviária e apoiam esforços de conservação<span class="emoji">🌟</span>. A escolha do equipamento depende de objetivos de pesquisa específicos, espécies-alvo e requisitos de design do estudo.'
    },
    'ko': {
        'title': '조류 연구 장비 및 연구 도구 - BirdAiSnap',
        'main_title': '🔬 조류 연구 장비 및 연구 도구',
        'quote': '조류학 연구와 전문적인 조류 연구에 사용되는 과학적 도구와 장비를 탐구하세요',
        'intro': '전문적인 조류 연구와 조류학 연구는 기본적인 조류 관찰 장비를 넘어서는 전문 장비가 필요합니다. 이러한 과학적 도구들은 연구자들이 상세한 연구를 수행하고, 데이터를 수집하며, 조류 생물학에 대한 우리의 이해를 발전시킬 수 있게 합니다<span class="emoji">🔬</span>. 이 가이드는 전문적인 조류 연구와 고급 연구에 사용되는 필수 장비를 다룹니다.',
        'banding_title': '밴딩 및 표시 장비',
        'banding_text': '조류 밴딩은 시간에 따른 개별 조류를 추적하는 중요한 연구 기법입니다. 전문 연구자들은 번호가 매겨진 금속 밴드, 색깔 밴드, 적용 도구를 포함한 전문 장비를 사용합니다<span class="emoji">🏷️</span>. 현대 연구는 또한 GPS 송신기와 무선 원격 측정 장치를 사용하여 이동 패턴과 행동을 추적합니다.',
        'capture_title': '포획 및 취급 장비',
        'capture_text': '연구를 위한 안전한 조류 포획은 스트레스와 부상을 최소화하도록 설계된 전문 그물과 함정이 필요합니다. 안개망은 가장 일반적인 포획 방법으로, 적절한 설치와 지속적인 모니터링이 필요합니다<span class="emoji">🕸️</span>. 전문적인 취급 기법과 장비는 연구 절차 중 조류의 안전을 보장합니다.',
        'safety_title': '⚠️ 안전 프로토콜',
        'safety_text': '조류 포획과 취급은 적절한 훈련, 허가, 엄격한 윤리 지침 준수가 필요합니다. 허가받은 연구자만이 이러한 기법을 사용해야 합니다.',
        'measurement_title': '측정 및 데이터 수집 도구',
        'measurement_text': '정밀한 측정은 조류학 연구에 필수적입니다. 조류 연구를 위해 설계된 전문 캘리퍼, 자, 저울은 정확한 형태학적 데이터를 제공합니다<span class="emoji">📏</span>. 디지털 데이터 로거와 필드 컴퓨터는 데이터 수집을 간소화하고 전사 오류를 줄입니다.',
        'nest_title': '둥지 모니터링 장비',
        'nest_text': '번식 생태학 연구는 방해 없이 둥지를 모니터링하기 위한 전문 장비가 필요합니다. 원격 카메라, 온도 로거, 확장 가능한 거울은 연구자들이 둥지 행동과 성공률을 연구할 수 있게 합니다<span class="emoji">🥚</span>. 현대 기술은 최소한의 인간 간섭으로 지속적인 모니터링을 가능하게 합니다.',
        'acoustic_title': '음향 연구 장비',
        'acoustic_text': '조류 발성 연구는 전문급 녹음 장비와 분석 소프트웨어를 사용합니다. 지향성 마이크, 디지털 레코더, 스펙트로그램 분석 프로그램은 조류 의사소통의 상세한 연구를 가능하게 합니다<span class="emoji">🎵</span>. 자동화된 녹음 스테이션은 넓은 지역에서 조류 활동을 지속적으로 모니터링할 수 있습니다.',
        'research_title': '🔬 연구 응용',
        'research_text': '이러한 도구들은 이동 생태학, 번식 생물학, 개체군 역학, 행동 연구, 보전 생물학을 포함한 다양한 연구 분야를 지원합니다.',
        'lab_title': '실험실 장비',
        'lab_text': '조류 샘플의 실험실 분석은 유전학적, 생리학적, 병리학적 연구를 위한 전문 장비가 필요합니다. 현미경, 원심분리기, 분자생물학 장비는 깃털, 혈액, 조직 샘플의 상세한 분석을 가능하게 합니다<span class="emoji">🧪</span>. 이 장비는 진화, 질병 생태학, 보전 유전학 연구를 지원합니다.',
        'conclusion': '전문적인 조류 연구 장비는 상당한 투자를 나타내며 안전하고 효과적인 사용을 위한 적절한 훈련이 필요합니다. 이러한 도구들은 과학자들이 조류 생물학에 대한 우리의 이해를 발전시키고 보전 노력을 지원하는 정밀한 데이터를 수집할 수 있게 합니다<span class="emoji">🌟</span>. 장비의 선택은 특정 연구 목표, 대상 종, 연구 설계 요구사항에 따라 달라집니다.'
    },
    'ja': {
        'title': '鳥類研究機器と研究ツール - BirdAiSnap',
        'main_title': '🔬 鳥類研究機器と研究ツール',
        'quote': '鳥類学研究と専門的な鳥類研究で使用される科学的ツールと機器を探求しましょう',
        'intro': '専門的な鳥類研究と鳥類学研究には、基本的なバードウォッチング機器を超えた専門機器が必要です。これらの科学的ツールにより、研究者は詳細な研究を行い、データを収集し、鳥類生物学の理解を深めることができます<span class="emoji">🔬</span>。このガイドでは、専門的な鳥類研究と高度な研究で使用される必須機器を扱います。',
        'banding_title': 'バンディングとマーキング機器',
        'banding_text': '鳥類バンディングは、時間を通じて個々の鳥を追跡する重要な研究技術です。専門研究者は、番号付き金属バンド、カラーバンド、適用ツールを含む専門機器を使用します<span class="emoji">🏷️</span>。現代の研究では、GPS送信機と無線テレメトリー装置も使用して、移動パターンと行動を追跡します。',
        'capture_title': '捕獲と取り扱い機器',
        'capture_text': '研究のための安全な鳥類捕獲には、ストレスと怪我を最小限に抑えるよう設計された専門ネットとトラップが必要です。かすみ網は最も一般的な捕獲方法で、適切な設置と継続的な監視が必要です<span class="emoji">🕸️</span>。専門的な取り扱い技術と機器により、研究手順中の鳥の安全が確保されます。',
        'safety_title': '⚠️ 安全プロトコル',
        'safety_text': '鳥類の捕獲と取り扱いには、適切な訓練、許可、厳格な倫理ガイドラインの遵守が必要です。ライセンスを持つ研究者のみがこれらの技術を使用すべきです。',
        'measurement_title': '測定とデータ収集ツール',
        'measurement_text': '正確な測定は鳥類学研究に不可欠です。鳥類研究用に設計された専門キャリパー、定規、スケールは正確な形態学的データを提供します<span class="emoji">📏</span>。デジタルデータロガーとフィールドコンピューターはデータ収集を合理化し、転写エラーを減らします。',
        'nest_title': '巣監視機器',
        'nest_text': '繁殖生態学研究には、妨害なしに巣を監視するための専門機器が必要です。リモートカメラ、温度ロガー、伸縮ミラーにより、研究者は営巣行動と成功率を研究できます<span class="emoji">🥚</span>。現代技術により、最小限の人間の干渉で継続的な監視が可能になります。',
        'acoustic_title': '音響研究機器',
        'acoustic_text': '鳥類発声研究では、プロ仕様の録音機器と分析ソフトウェアを使用します。指向性マイク、デジタルレコーダー、スペクトログラム分析プログラムにより、鳥類コミュニケーションの詳細な研究が可能になります<span class="emoji">🎵</span>。自動録音ステーションは広域で鳥類活動を継続的に監視できます。',
        'research_title': '🔬 研究応用',
        'research_text': 'これらのツールは、移動生態学、繁殖生物学、個体群動態、行動研究、保全生物学を含む様々な研究分野を支援します。',
        'lab_title': '実験室機器',
        'lab_text': '鳥類サンプルの実験室分析には、遺伝学的、生理学的、病理学的研究のための専門機器が必要です。顕微鏡、遠心分離機、分子生物学機器により、羽毛、血液、組織サンプルの詳細な分析が可能になります<span class="emoji">🧪</span>。この機器は進化、疾病生態学、保全遺伝学の研究を支援します。',
        'conclusion': '専門的な鳥類研究機器は重要な投資を表し、安全で効果的な使用のための適切な訓練が必要です。これらのツールにより、科学者は鳥類生物学の理解を深め、保全努力を支援する正確なデータを収集できます<span class="emoji">🌟</span>。機器の選択は、特定の研究目標、対象種、研究設計要件によって異なります。'
    },
    'es': {
        'title': 'Equipos de Estudio de Aves y Herramientas de Investigación - BirdAiSnap',
        'main_title': '🔬 Equipos de Estudio de Aves y Herramientas de Investigación',
        'quote': 'Explora las herramientas científicas y equipos utilizados en investigación ornitológica y estudio profesional de aves',
        'intro': 'El estudio profesional de aves y la investigación ornitológica requieren equipos especializados más allá del equipo básico de observación de aves. Estas herramientas científicas permiten a los investigadores realizar estudios detallados, recopilar datos y avanzar nuestro entendimiento de la biología aviar<span class="emoji">🔬</span>. Esta guía cubre el equipo esencial utilizado en investigación profesional de aves y estudio avanzado.',
        'banding_title': 'Equipos de Anillamiento y Marcado',
        'banding_text': 'El anillamiento de aves es una técnica de investigación crucial para rastrear aves individuales a lo largo del tiempo. Los investigadores profesionales utilizan equipos especializados incluyendo anillas metálicas numeradas, anillas de colores y herramientas de aplicación<span class="emoji">🏷️</span>. Los estudios modernos también emplean transmisores GPS y dispositivos de radiotelemetría para rastrear patrones de migración y comportamiento.',
        'capture_title': 'Equipos de Captura y Manejo',
        'capture_text': 'La captura segura de aves para investigación requiere redes y trampas especializadas diseñadas para minimizar el estrés y las lesiones. Las redes de niebla son el método de captura más común, requiriendo configuración adecuada y monitoreo constante<span class="emoji">🕸️</span>. Las técnicas y equipos profesionales de manejo aseguran la seguridad de las aves durante los procedimientos de investigación.',
        'safety_title': '⚠️ Protocolo de Seguridad',
        'safety_text': 'La captura y manejo de aves requiere entrenamiento adecuado, permisos y adherencia a pautas éticas estrictas. Solo investigadores licenciados deben usar estas técnicas.',
        'measurement_title': 'Herramientas de Medición y Recolección de Datos',
        'measurement_text': 'Las mediciones precisas son esenciales para la investigación ornitológica. Calibradores especializados, reglas y balanzas diseñadas para investigación de aves proporcionan datos morfométricos precisos<span class="emoji">📏</span>. Los registradores de datos digitales y computadoras de campo agilizan la recolección de datos y reducen errores de transcripción.',
        'nest_title': 'Equipos de Monitoreo de Nidos',
        'nest_text': 'Los estudios de ecología reproductiva requieren equipos especializados para monitorear nidos sin perturbación. Cámaras remotas, registradores de temperatura y espejos extensibles permiten a los investigadores estudiar el comportamiento de anidación y las tasas de éxito<span class="emoji">🥚</span>. La tecnología moderna permite monitoreo continuo con interferencia humana mínima.',
        'acoustic_title': 'Equipos de Investigación Acústica',
        'acoustic_text': 'Los estudios de vocalización de aves utilizan equipos de grabación de grado profesional y software de análisis. Micrófonos direccionales, grabadores digitales y programas de análisis de espectrogramas permiten el estudio detallado de la comunicación aviar<span class="emoji">🎵</span>. Las estaciones de grabación automatizadas pueden monitorear la actividad de aves continuamente en áreas grandes.',
        'research_title': '🔬 Aplicaciones de Investigación',
        'research_text': 'Estas herramientas apoyan varias áreas de investigación incluyendo ecología de migración, biología reproductiva, dinámicas poblacionales, estudios de comportamiento y biología de conservación.',
        'lab_title': 'Equipos de Laboratorio',
        'lab_text': 'El análisis de laboratorio de muestras de aves requiere equipos especializados para estudios genéticos, fisiológicos y patológicos. Microscopios, centrífugas y equipos de biología molecular permiten análisis detallado de plumas, sangre y muestras de tejido<span class="emoji">🧪</span>. Este equipo apoya la investigación en evolución, ecología de enfermedades y genética de conservación.',
        'conclusion': 'El equipo profesional de investigación de aves representa una inversión significativa y requiere entrenamiento adecuado para uso seguro y efectivo. Estas herramientas permiten a los científicos recopilar datos precisos que avanzan nuestro entendimiento de la biología aviar y apoyan los esfuerzos de conservación<span class="emoji">🌟</span>. La elección del equipo depende de objetivos de investigación específicos, especies objetivo y requisitos de diseño del estudio.'
    },
    'fr': {
        'title': 'Équipements d\'Étude des Oiseaux et Outils de Recherche - BirdAiSnap',
        'main_title': '🔬 Équipements d\'Étude des Oiseaux et Outils de Recherche',
        'quote': 'Explorez les outils scientifiques et équipements utilisés dans la recherche ornithologique et l\'étude professionnelle des oiseaux',
        'intro': 'L\'étude professionnelle des oiseaux et la recherche ornithologique nécessitent des équipements spécialisés au-delà de l\'équipement de base d\'observation des oiseaux. Ces outils scientifiques permettent aux chercheurs de mener des études détaillées, de collecter des données et de faire progresser notre compréhension de la biologie aviaire<span class="emoji">🔬</span>. Ce guide couvre l\'équipement essentiel utilisé dans la recherche professionnelle sur les oiseaux et l\'étude avancée.',
        'banding_title': 'Équipements de Baguage et de Marquage',
        'banding_text': 'Le baguage des oiseaux est une technique de recherche cruciale pour suivre les oiseaux individuels dans le temps. Les chercheurs professionnels utilisent des équipements spécialisés incluant des bagues métalliques numérotées, des bagues colorées et des outils d\'application<span class="emoji">🏷️</span>. Les études modernes emploient également des transmetteurs GPS et des dispositifs de radiotélémétrie pour suivre les modèles de migration et le comportement.',
        'capture_title': 'Équipements de Capture et de Manipulation',
        'capture_text': 'La capture sécurisée d\'oiseaux pour la recherche nécessite des filets et pièges spécialisés conçus pour minimiser le stress et les blessures. Les filets japonais sont la méthode de capture la plus courante, nécessitant une installation appropriée et une surveillance constante<span class="emoji">🕸️</span>. Les techniques et équipements professionnels de manipulation assurent la sécurité des oiseaux pendant les procédures de recherche.',
        'safety_title': '⚠️ Protocole de Sécurité',
        'safety_text': 'La capture et manipulation d\'oiseaux nécessite une formation appropriée, des permis et l\'adhésion à des directives éthiques strictes. Seuls les chercheurs licenciés devraient utiliser ces techniques.',
        'measurement_title': 'Outils de Mesure et de Collecte de Données',
        'measurement_text': 'Les mesures précises sont essentielles pour la recherche ornithologique. Les pieds à coulisse spécialisés, règles et balances conçues pour la recherche aviaire fournissent des données morphométriques précises<span class="emoji">📏</span>. Les enregistreurs de données numériques et ordinateurs de terrain rationalisent la collecte de données et réduisent les erreurs de transcription.',
        'nest_title': 'Équipements de Surveillance des Nids',
        'nest_text': 'Les études d\'écologie de reproduction nécessitent des équipements spécialisés pour surveiller les nids sans perturbation. Les caméras à distance, enregistreurs de température et miroirs extensibles permettent aux chercheurs d\'étudier le comportement de nidification et les taux de succès<span class="emoji">🥚</span>. La technologie moderne permet une surveillance continue avec une interférence humaine minimale.',
        'acoustic_title': 'Équipements de Recherche Acoustique',
        'acoustic_text': 'Les études de vocalisation aviaire utilisent des équipements d\'enregistrement de qualité professionnelle et des logiciels d\'analyse. Les microphones directionnels, enregistreurs numériques et programmes d\'analyse de spectrogrammes permettent l\'étude détaillée de la communication aviaire<span class="emoji">🎵</span>. Les stations d\'enregistrement automatisées peuvent surveiller l\'activité aviaire en continu sur de grandes zones.',
        'research_title': '🔬 Applications de Recherche',
        'research_text': 'Ces outils soutiennent diverses zones de recherche incluant l\'écologie de migration, la biologie de reproduction, la dynamique des populations, les études comportementales et la biologie de conservation.',
        'lab_title': 'Équipements de Laboratoire',
        'lab_text': 'L\'analyse de laboratoire d\'échantillons aviaires nécessite des équipements spécialisés pour les études génétiques, physiologiques et pathologiques. Les microscopes, centrifugeuses et équipements de biologie moléculaire permettent l\'analyse détaillée des plumes, sang et échantillons de tissus<span class="emoji">🧪</span>. Cet équipement soutient la recherche en évolution, écologie des maladies et génétique de conservation.',
        'conclusion': 'L\'équipement professionnel de recherche aviaire représente un investissement significatif et nécessite une formation appropriée pour une utilisation sûre et efficace. Ces outils permettent aux scientifiques de collecter des données précises qui font progresser notre compréhension de la biologie aviaire et soutiennent les efforts de conservation<span class="emoji">🌟</span>. Le choix de l\'équipement dépend des objectifs de recherche spécifiques, des espèces cibles et des exigences de conception d\'étude.'
    },
    'it': {
        'title': 'Attrezzature per lo Studio degli Uccelli e Strumenti di Ricerca - BirdAiSnap',
        'main_title': '🔬 Attrezzature per lo Studio degli Uccelli e Strumenti di Ricerca',
        'quote': 'Esplora gli strumenti scientifici e le attrezzature utilizzate nella ricerca ornitologica e nello studio professionale degli uccelli',
        'intro': 'Lo studio professionale degli uccelli e la ricerca ornitologica richiedono attrezzature specializzate oltre all\'equipaggiamento base per il birdwatching. Questi strumenti scientifici permettono ai ricercatori di condurre studi dettagliati, raccogliere dati e avanzare la nostra comprensione della biologia aviaria<span class="emoji">🔬</span>. Questa guida copre l\'attrezzatura essenziale utilizzata nella ricerca professionale sugli uccelli e nello studio avanzato.',
        'banding_title': 'Attrezzature per Inanellamento e Marcatura',
        'banding_text': 'L\'inanellamento degli uccelli è una tecnica di ricerca cruciale per tracciare singoli uccelli nel tempo. I ricercatori professionali utilizzano attrezzature specializzate inclusi anelli metallici numerati, anelli colorati e strumenti di applicazione<span class="emoji">🏷️</span>. Gli studi moderni impiegano anche trasmettitori GPS e dispositivi di radiotelemetria per tracciare i modelli di migrazione e il comportamento.',
        'capture_title': 'Attrezzature per Cattura e Manipolazione',
        'capture_text': 'La cattura sicura di uccelli per la ricerca richiede reti e trappole specializzate progettate per minimizzare stress e lesioni. Le reti nebbia sono il metodo di cattura più comune, richiedendo installazione appropriata e monitoraggio costante<span class="emoji">🕸️</span>. Tecniche e attrezzature professionali di manipolazione assicurano la sicurezza degli uccelli durante le procedure di ricerca.',
        'safety_title': '⚠️ Protocollo di Sicurezza',
        'safety_text': 'La cattura e manipolazione di uccelli richiede addestramento appropriato, permessi e aderenza a linee guida etiche rigorose. Solo ricercatori autorizzati dovrebbero utilizzare queste tecniche.',
        'measurement_title': 'Strumenti di Misurazione e Raccolta Dati',
        'measurement_text': 'Misurazioni precise sono essenziali per la ricerca ornitologica. Calibri specializzati, righelli e bilance progettate per la ricerca aviaria forniscono dati morfometrici accurati<span class="emoji">📏</span>. Registratori di dati digitali e computer da campo semplificano la raccolta dati e riducono errori di trascrizione.',
        'nest_title': 'Attrezzature per Monitoraggio Nidi',
        'nest_text': 'Gli studi di ecologia riproduttiva richiedono attrezzature specializzate per monitorare i nidi senza disturbo. Telecamere remote, registratori di temperatura e specchi estensibili permettono ai ricercatori di studiare il comportamento di nidificazione e i tassi di successo<span class="emoji">🥚</span>. La tecnologia moderna permette monitoraggio continuo con interferenza umana minima.',
        'acoustic_title': 'Attrezzature per Ricerca Acustica',
        'acoustic_text': 'Gli studi di vocalizzazione aviaria utilizzano attrezzature di registrazione di livello professionale e software di analisi. Microfoni direzionali, registratori digitali e programmi di analisi spettrogramma permettono studio dettagliato della comunicazione aviaria<span class="emoji">🎵</span>. Stazioni di registrazione automatizzate possono monitorare l\'attività aviaria continuamente su aree ampie.',
        'research_title': '🔬 Applicazioni di Ricerca',
        'research_text': 'Questi strumenti supportano varie aree di ricerca inclusa ecologia di migrazione, biologia riproduttiva, dinamiche di popolazione, studi comportamentali e biologia della conservazione.',
        'lab_title': 'Attrezzature di Laboratorio',
        'lab_text': 'L\'analisi di laboratorio di campioni aviari richiede attrezzature specializzate per studi genetici, fisiologici e patologici. Microscopi, centrifughe e attrezzature di biologia molecolare permettono analisi dettagliata di piume, sangue e campioni di tessuto<span class="emoji">🧪</span>. Questa attrezzatura supporta ricerca in evoluzione, ecologia delle malattie e genetica della conservazione.',
        'conclusion': 'L\'attrezzatura professionale per ricerca aviaria rappresenta un investimento significativo e richiede addestramento appropriato per uso sicuro ed efficace. Questi strumenti permettono agli scienziati di raccogliere dati precisi che avanzano la nostra comprensione della biologia aviaria e supportano gli sforzi di conservazione<span class="emoji">🌟</span>. La scelta dell\'attrezzatura dipende da obiettivi di ricerca specifici, specie target e requisiti di design dello studio.'
    },
    'ru': {
        'title': 'Оборудование для Изучения Птиц и Исследовательские Инструменты - BirdAiSnap',
        'main_title': '🔬 Оборудование для Изучения Птиц и Исследовательские Инструменты',
        'quote': 'Исследуйте научные инструменты и оборудование, используемые в орнитологических исследованиях и профессиональном изучении птиц',
        'intro': 'Профессиональное изучение птиц и орнитологические исследования требуют специализированного оборудования помимо базового оборудования для наблюдения за птицами. Эти научные инструменты позволяют исследователям проводить детальные исследования, собирать данные и развивать наше понимание биологии птиц<span class="emoji">🔬</span>. Это руководство охватывает основное оборудование, используемое в профессиональных исследованиях птиц и продвинутых исследованиях.',
        'banding_title': 'Оборудование для Кольцевания и Маркировки',
        'banding_text': 'Кольцевание птиц является важной исследовательской техникой для отслеживания отдельных птиц во времени. Профессиональные исследователи используют специализированное оборудование, включая пронумерованные металлические кольца, цветные кольца и инструменты для применения<span class="emoji">🏷️</span>. Современные исследования также используют GPS-передатчики и радиотелеметрические устройства для отслеживания миграционных паттернов и поведения.',
        'capture_title': 'Оборудование для Отлова и Обращения',
        'capture_text': 'Безопасный отлов птиц для исследований требует специализированных сетей и ловушек, разработанных для минимизации стресса и травм. Паутинные сети являются наиболее распространенным методом отлова, требующим правильной установки и постоянного мониторинга<span class="emoji">🕸️</span>. Профессиональные техники и оборудование для обращения обеспечивают безопасность птиц во время исследовательских процедур.',
        'safety_title': '⚠️ Протокол Безопасности',
        'safety_text': 'Отлов и обращение с птицами требует надлежащего обучения, разрешений и соблюдения строгих этических руководящих принципов. Только лицензированные исследователи должны использовать эти техники.',
        'measurement_title': 'Инструменты для Измерения и Сбора Данных',
        'measurement_text': 'Точные измерения необходимы для орнитологических исследований. Специализированные штангенциркули, линейки и весы, разработанные для исследований птиц, предоставляют точные морфометрические данные<span class="emoji">📏</span>. Цифровые регистраторы данных и полевые компьютеры упрощают сбор данных и уменьшают ошибки транскрипции.',
        'nest_title': 'Оборудование для Мониторинга Гнезд',
        'nest_text': 'Исследования экологии размножения требуют специализированного оборудования для мониторинга гнезд без беспокойства. Удаленные камеры, регистраторы температуры и выдвижные зеркала позволяют исследователям изучать поведение гнездования и показатели успеха<span class="emoji">🥚</span>. Современные технологии обеспечивают непрерывный мониторинг с минимальным человеческим вмешательством.',
        'acoustic_title': 'Оборудование для Акустических Исследований',
        'acoustic_text': 'Исследования вокализации птиц используют профессиональное записывающее оборудование и программное обеспечение для анализа. Направленные микрофоны, цифровые рекордеры и программы анализа спектрограмм обеспечивают детальное изучение птичьей коммуникации<span class="emoji">🎵</span>. Автоматизированные записывающие станции могут непрерывно мониторить активность птиц на больших территориях.',
        'research_title': '🔬 Исследовательские Применения',
        'research_text': 'Эти инструменты поддерживают различные области исследований, включая экологию миграции, биологию размножения, популационную динамику, поведенческие исследования и биологию сохранения.',
        'lab_title': 'Лабораторное Оборудование',
        'lab_text': 'Лабораторный анализ образцов птиц требует специализированного оборудования для генетических, физиологических и патологических исследований. Микроскопы, центрифуги и оборудование молекулярной биологии обеспечивают детальный анализ перьев, крови и образцов тканей<span class="emoji">🧪</span>. Это оборудование поддерживает исследования в области эволюции, экологии болезней и генетики сохранения.',
        'conclusion': 'Профессиональное оборудование для исследований птиц представляет значительную инвестицию и требует надлежащего обучения для безопасного и эффективного использования. Эти инструменты позволяют ученым собирать точные данные, которые развивают наше понимание биологии птиц и поддерживают усилия по сохранению<span class="emoji">🌟</span>. Выбор оборудования зависит от конкретных исследовательских целей, целевых видов и требований дизайна исследования.'
    },
    'zh': {
        'title': '鸟类研究设备和研究工具 - BirdAiSnap',
        'main_title': '🔬 鸟类研究设备和研究工具',
        'quote': '探索鸟类学研究和专业鸟类研究中使用的科学工具和设备',
        'intro': '专业鸟类研究和鸟类学研究需要超越基本观鸟设备的专业设备。这些科学工具使研究人员能够进行详细研究、收集数据并推进我们对鸟类生物学的理解<span class="emoji">🔬</span>。本指南涵盖了专业鸟类研究和高级研究中使用的基本设备。',
        'banding_title': '环志和标记设备',
        'banding_text': '鸟类环志是追踪个体鸟类随时间变化的重要研究技术。专业研究人员使用专门设备，包括编号金属环、彩色环和应用工具<span class="emoji">🏷️</span>。现代研究还采用GPS发射器和无线电遥测设备来追踪迁徙模式和行为。',
        'capture_title': '捕获和处理设备',
        'capture_text': '研究用的安全鸟类捕获需要专门设计的网具和陷阱，以最大限度地减少压力和伤害。雾网是最常见的捕获方法，需要适当的设置和持续监控<span class="emoji">🕸️</span>。专业的处理技术和设备确保研究过程中鸟类的安全。',
        'safety_title': '⚠️ 安全协议',
        'safety_text': '鸟类捕获和处理需要适当的培训、许可证和遵守严格的伦理准则。只有持证研究人员才应使用这些技术。',
        'measurement_title': '测量和数据收集工具',
        'measurement_text': '精确测量对鸟类学研究至关重要。专为鸟类研究设计的专业卡尺、尺子和天平提供准确的形态学数据<span class="emoji">📏</span>。数字数据记录器和野外计算机简化数据收集并减少转录错误。',
        'nest_title': '巢穴监测设备',
        'nest_text': '繁殖生态学研究需要专门设备来监测巢穴而不造成干扰。远程摄像头、温度记录器和可伸缩镜子使研究人员能够研究筑巢行为和成功率<span class="emoji">🥚</span>。现代技术实现了最少人为干预的连续监测。',
        'acoustic_title': '声学研究设备',
        'acoustic_text': '鸟类发声研究使用专业级录音设备和分析软件。定向麦克风、数字录音机和频谱图分析程序实现了对鸟类交流的详细研究<span class="emoji">🎵</span>。自动录音站可以在大面积区域连续监测鸟类活动。',
        'research_title': '🔬 研究应用',
        'research_text': '这些工具支持各种研究领域，包括迁徙生态学、繁殖生物学、种群动态、行为研究和保护生物学。',
        'lab_title': '实验室设备',
        'lab_text': '鸟类样本的实验室分析需要专门设备进行遗传学、生理学和病理学研究。显微镜、离心机和分子生物学设备实现了对羽毛、血液和组织样本的详细分析<span class="emoji">🧪</span>。这些设备支持进化、疾病生态学和保护遗传学研究。',
        'conclusion': '专业鸟类研究设备代表着重大投资，需要适当培训才能安全有效地使用。这些工具使科学家能够收集精确数据，推进我们对鸟类生物学的理解并支持保护工作<span class="emoji">🌟</span>。设备选择取决于具体研究目标、目标物种和研究设计要求。'
    }
}

def create_html_template(lang_code, translations):
    """创建HTML模板"""
    trans = translations[lang_code]
    
    return f'''<!DOCTYPE html>
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
        
        ul {{
            color: #34495e;
            padding-left: 20px;
        }}
        
        li {{
            margin: 8px 0;
        }}
        
        .highlight {{
            background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
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
            {trans['intro']}
        </div>
        
        <div class="section-title">{trans['banding_title']}</div>
        <div class="main-text">
            {trans['banding_text']}
        </div>
        
        <div class="section-title">{trans['capture_title']}</div>
        <div class="main-text">
            {trans['capture_text']}
        </div>
        
        <div class="tip-box">
            <div class="tip-title">{trans['safety_title']}</div>
            {trans['safety_text']}
        </div>
        
        <div class="section-title">{trans['measurement_title']}</div>
        <div class="main-text">
            {trans['measurement_text']}
        </div>
        
        <div class="section-title">{trans['nest_title']}</div>
        <div class="main-text">
            {trans['nest_text']}
        </div>
        
        <div class="section-title">{trans['acoustic_title']}</div>
        <div class="main-text">
            {trans['acoustic_text']}
        </div>
        
        <div class="tip-box">
            <div class="tip-title">{trans['research_title']}</div>
            {trans['research_text']}
        </div>
        
        <div class="section-title">{trans['lab_title']}</div>
        <div class="main-text">
            {trans['lab_text']}
        </div>
        
        <div class="main-text">
            {trans['conclusion']}
        </div>
    </div>
</body>
</html>'''

def main():
    """主函数"""
    print("开始更新多语言设备文件...")
    
    for lang_code, lang_name in languages.items():
        print(f"正在处理 {lang_name} ({lang_code})...")
        
        # 创建目录路径
        file_path = f"{lang_code}/knowledge/02-essential-equipment.html"
        
        # 检查目录是否存在
        os.makedirs(f"{lang_code}/knowledge", exist_ok=True)
        
        # 生成HTML内容
        html_content = create_html_template(lang_code, translations)
        
        # 写入文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ 已更新: {file_path}")
    
    print("🎉 所有语言的设备文件更新完成！")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 定义所有语言目录
languages = {
    'de': 'Deutsch',
    'pt': 'Português', 
    'ko': '한국어',
    'ja': '日本語',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
    'ru': 'Русский',
    'zh': '中文'
}

# 翻译映射字典
translations = {
    'de': {
        'title': 'Vogelforschungsausrüstung und Forschungswerkzeuge - BirdAiSnap',
        'main_title': '🔬 Vogelforschungsausrüstung und Forschungswerkzeuge',
        'quote': 'Entdecken Sie die wissenschaftlichen Werkzeuge und Ausrüstungen für ornithologische Forschung und professionelle Vogelstudien',
        'intro': 'Professionelle Vogelstudien und ornithologische Forschung erfordern spezialisierte Ausrüstung über die grundlegende Vogelbeobachtungsausrüstung hinaus. Diese wissenschaftlichen Werkzeuge ermöglichen es Forschern, detaillierte Studien durchzuführen, Daten zu sammeln und unser Verständnis der Vogelbiologie zu erweitern<span class="emoji">🔬</span>. Dieser Leitfaden behandelt die wesentliche Ausrüstung für professionelle Vogelforschung und fortgeschrittene Studien.',
        'banding_title': 'Beringungs- und Markierungsausrüstung',
        'banding_text': 'Vogelberingung ist eine entscheidende Forschungstechnik zur Verfolgung einzelner Vögel über die Zeit. Professionelle Forscher verwenden spezialisierte Ausrüstung einschließlich nummerierter Metallringe, Farbringe und Anwendungswerkzeuge<span class="emoji">🏷️</span>. Moderne Studien verwenden auch GPS-Sender und Radiotelemetrie-Geräte zur Verfolgung von Wanderungsmustern und Verhalten.',
        'capture_title': 'Fang- und Handhabungsausrüstung',
        'capture_text': 'Sicherer Vogelfang für die Forschung erfordert spezialisierte Netze und Fallen, die darauf ausgelegt sind, Stress und Verletzungen zu minimieren. Nebelnetze sind die häufigste Fangmethode und erfordern ordnungsgemäße Aufstellung und ständige Überwachung<span class="emoji">🕸️</span>. Professionelle Handhabungstechniken und -ausrüstung gewährleisten die Vogelsicherheit während Forschungsverfahren.',
        'safety_title': '⚠️ Sicherheitsprotokoll',
        'safety_text': 'Vogelfang und -handhabung erfordern ordnungsgemäße Ausbildung, Genehmigungen und die Einhaltung strenger ethischer Richtlinien. Nur lizenzierte Forscher sollten diese Techniken verwenden.',
        'measurement_title': 'Mess- und Datensammlungswerkzeuge',
        'measurement_text': 'Präzise Messungen sind für ornithologische Forschung unerlässlich. Spezialisierte Messschieber, Lineale und Waagen für Vogelforschung liefern genaue morphometrische Daten<span class="emoji">📏</span>. Digitale Datenlogger und Feldcomputer rationalisieren die Datensammlung und reduzieren Transkriptionsfehler.',
        'nest_title': 'Nestüberwachungsausrüstung',
        'nest_text': 'Brutökologie-Studien erfordern spezialisierte Ausrüstung zur Überwachung von Nestern ohne Störung. Fernkameras, Temperaturlogger und ausziehbare Spiegel ermöglichen es Forschern, Nistverhalten und Erfolgsraten zu studieren<span class="emoji">🥚</span>. Moderne Technologie ermöglicht kontinuierliche Überwachung mit minimaler menschlicher Einmischung.',
        'acoustic_title': 'Akustische Forschungsausrüstung',
        'acoustic_text': 'Vogelstimmenstudien verwenden professionelle Aufnahmegeräte und Analysesoftware. Richtmikrofone, digitale Rekorder und Spektrogramm-Analyseprogramme ermöglichen detaillierte Studien der Vogelkommunikation<span class="emoji">🎵</span>. Automatisierte Aufnahmestationen können Vogelaktivität kontinuierlich über große Gebiete überwachen.',
        'research_title': '🔬 Forschungsanwendungen',
        'research_text': 'Diese Werkzeuge unterstützen verschiedene Forschungsbereiche einschließlich Wanderungsökologie, Brutbiologie, Populationsdynamik, Verhaltensstudien und Naturschutzbiologie.',
        'lab_title': 'Laborausrüstung',
        'lab_text': 'Laboranalyse von Vogelproben erfordert spezialisierte Ausrüstung für genetische, physiologische und pathologische Studien. Mikroskope, Zentrifugen und molekularbiologische Ausrüstung ermöglichen detaillierte Analyse von Federn, Blut und Gewebeproben<span class="emoji">🧪</span>. Diese Ausrüstung unterstützt Forschung in Evolution, Krankheitsökologie und Naturschutzgenetik.',
        'conclusion': 'Professionelle Vogelforschungsausrüstung stellt eine erhebliche Investition dar und erfordert ordnungsgemäße Ausbildung für sichere und effektive Nutzung. Diese Werkzeuge ermöglichen es Wissenschaftlern, präzise Daten zu sammeln, die unser Verständnis der Vogelbiologie fördern und Naturschutzbemühungen unterstützen<span class="emoji">🌟</span>. Die Wahl der Ausrüstung hängt von spezifischen Forschungszielen, Zielarten und Studiendesign-Anforderungen ab.'
    },
    'pt': {
        'title': 'Equipamentos de Estudo de Aves e Ferramentas de Pesquisa - BirdAiSnap',
        'main_title': '🔬 Equipamentos de Estudo de Aves e Ferramentas de Pesquisa',
        'quote': 'Explore as ferramentas científicas e equipamentos usados em pesquisa ornitológica e estudo profissional de aves',
        'intro': 'O estudo profissional de aves e a pesquisa ornitológica requerem equipamentos especializados além dos equipamentos básicos de observação de aves. Essas ferramentas científicas permitem aos pesquisadores conduzir estudos detalhados, coletar dados e avançar nosso entendimento da biologia aviária<span class="emoji">🔬</span>. Este guia cobre os equipamentos essenciais usados em pesquisa profissional de aves e estudo avançado.',
        'banding_title': 'Equipamentos de Anilhamento e Marcação',
        'banding_text': 'O anilhamento de aves é uma técnica de pesquisa crucial para rastrear aves individuais ao longo do tempo. Pesquisadores profissionais usam equipamentos especializados incluindo anilhas metálicas numeradas, anilhas coloridas e ferramentas de aplicação<span class="emoji">🏷️</span>. Estudos modernos também empregam transmissores GPS e dispositivos de radiotelemetria para rastrear padrões de migração e comportamento.',
        'capture_title': 'Equipamentos de Captura e Manuseio',
        'capture_text': 'A captura segura de aves para pesquisa requer redes e armadilhas especializadas projetadas para minimizar estresse e lesões. Redes de neblina são o método de captura mais comum, requerendo configuração adequada e monitoramento constante<span class="emoji">🕸️</span>. Técnicas e equipamentos profissionais de manuseio garantem a segurança das aves durante procedimentos de pesquisa.',
        'safety_title': '⚠️ Protocolo de Segurança',
        'safety_text': 'A captura e manuseio de aves requer treinamento adequado, licenças e aderência a diretrizes éticas rigorosas. Apenas pesquisadores licenciados devem usar essas técnicas.',
        'measurement_title': 'Ferramentas de Medição e Coleta de Dados',
        'measurement_text': 'Medições precisas são essenciais para pesquisa ornitológica. Paquímetros especializados, réguas e balanças projetadas para pesquisa de aves fornecem dados morfométricos precisos<span class="emoji">📏</span>. Registradores de dados digitais e computadores de campo simplificam a coleta de dados e reduzem erros de transcrição.',
        'nest_title': 'Equipamentos de Monitoramento de Ninhos',
        'nest_text': 'Estudos de ecologia reprodutiva requerem equipamentos especializados para monitorar ninhos sem perturbação. Câmeras remotas, registradores de temperatura e espelhos extensíveis permitem aos pesquisadores estudar comportamento de nidificação e taxas de sucesso<span class="emoji">🥚</span>. A tecnologia moderna permite monitoramento contínuo com interferência humana mínima.',
        'acoustic_title': 'Equipamentos de Pesquisa Acústica',
        'acoustic_text': 'Estudos de vocalização de aves usam equipamentos de gravação de nível profissional e software de análise. Microfones direcionais, gravadores digitais e programas de análise de espectrograma permitem estudo detalhado da comunicação aviária<span class="emoji">🎵</span>. Estações de gravação automatizadas podem monitorar atividade de aves continuamente em grandes áreas.',
        'research_title': '🔬 Aplicações de Pesquisa',
        'research_text': 'Essas ferramentas apoiam várias áreas de pesquisa incluindo ecologia de migração, biologia reprodutiva, dinâmica populacional, estudos comportamentais e biologia da conservação.',
        'lab_title': 'Equipamentos de Laboratório',
        'lab_text': 'A análise laboratorial de amostras de aves requer equipamentos especializados para estudos genéticos, fisiológicos e patológicos. Microscópios, centrífugas e equipamentos de biologia molecular permitem análise detalhada de penas, sangue e amostras de tecido<span class="emoji">🧪</span>. Esses equipamentos apoiam pesquisa em evolução, ecologia de doenças e genética da conservação.',
        'conclusion': 'Equipamentos profissionais de pesquisa de aves representam um investimento significativo e requerem treinamento adequado para uso seguro e eficaz. Essas ferramentas permitem aos cientistas coletar dados precisos que avançam nosso entendimento da biologia aviária e apoiam esforços de conservação<span class="emoji">🌟</span>. A escolha do equipamento depende de objetivos de pesquisa específicos, espécies-alvo e requisitos de design do estudo.'
    },
    'ko': {
        'title': '조류 연구 장비 및 연구 도구 - BirdAiSnap',
        'main_title': '🔬 조류 연구 장비 및 연구 도구',
        'quote': '조류학 연구와 전문적인 조류 연구에 사용되는 과학적 도구와 장비를 탐구하세요',
        'intro': '전문적인 조류 연구와 조류학 연구는 기본적인 조류 관찰 장비를 넘어서는 전문 장비가 필요합니다. 이러한 과학적 도구들은 연구자들이 상세한 연구를 수행하고, 데이터를 수집하며, 조류 생물학에 대한 우리의 이해를 발전시킬 수 있게 합니다<span class="emoji">🔬</span>. 이 가이드는 전문적인 조류 연구와 고급 연구에 사용되는 필수 장비를 다룹니다.',
        'banding_title': '밴딩 및 표시 장비',
        'banding_text': '조류 밴딩은 시간에 따른 개별 조류를 추적하는 중요한 연구 기법입니다. 전문 연구자들은 번호가 매겨진 금속 밴드, 색깔 밴드, 적용 도구를 포함한 전문 장비를 사용합니다<span class="emoji">🏷️</span>. 현대 연구는 또한 GPS 송신기와 무선 원격 측정 장치를 사용하여 이동 패턴과 행동을 추적합니다.',
        'capture_title': '포획 및 취급 장비',
        'capture_text': '연구를 위한 안전한 조류 포획은 스트레스와 부상을 최소화하도록 설계된 전문 그물과 함정이 필요합니다. 안개망은 가장 일반적인 포획 방법으로, 적절한 설치와 지속적인 모니터링이 필요합니다<span class="emoji">🕸️</span>. 전문적인 취급 기법과 장비는 연구 절차 중 조류의 안전을 보장합니다.',
        'safety_title': '⚠️ 안전 프로토콜',
        'safety_text': '조류 포획과 취급은 적절한 훈련, 허가, 엄격한 윤리 지침 준수가 필요합니다. 허가받은 연구자만이 이러한 기법을 사용해야 합니다.',
        'measurement_title': '측정 및 데이터 수집 도구',
        'measurement_text': '정밀한 측정은 조류학 연구에 필수적입니다. 조류 연구를 위해 설계된 전문 캘리퍼, 자, 저울은 정확한 형태학적 데이터를 제공합니다<span class="emoji">📏</span>. 디지털 데이터 로거와 필드 컴퓨터는 데이터 수집을 간소화하고 전사 오류를 줄입니다.',
        'nest_title': '둥지 모니터링 장비',
        'nest_text': '번식 생태학 연구는 방해 없이 둥지를 모니터링하기 위한 전문 장비가 필요합니다. 원격 카메라, 온도 로거, 확장 가능한 거울은 연구자들이 둥지 행동과 성공률을 연구할 수 있게 합니다<span class="emoji">🥚</span>. 현대 기술은 최소한의 인간 간섭으로 지속적인 모니터링을 가능하게 합니다.',
        'acoustic_title': '음향 연구 장비',
        'acoustic_text': '조류 발성 연구는 전문급 녹음 장비와 분석 소프트웨어를 사용합니다. 지향성 마이크, 디지털 레코더, 스펙트로그램 분석 프로그램은 조류 의사소통의 상세한 연구를 가능하게 합니다<span class="emoji">🎵</span>. 자동화된 녹음 스테이션은 넓은 지역에서 조류 활동을 지속적으로 모니터링할 수 있습니다.',
        'research_title': '🔬 연구 응용',
        'research_text': '이러한 도구들은 이동 생태학, 번식 생물학, 개체군 역학, 행동 연구, 보전 생물학을 포함한 다양한 연구 분야를 지원합니다.',
        'lab_title': '실험실 장비',
        'lab_text': '조류 샘플의 실험실 분석은 유전학적, 생리학적, 병리학적 연구를 위한 전문 장비가 필요합니다. 현미경, 원심분리기, 분자생물학 장비는 깃털, 혈액, 조직 샘플의 상세한 분석을 가능하게 합니다<span class="emoji">🧪</span>. 이 장비는 진화, 질병 생태학, 보전 유전학 연구를 지원합니다.',
        'conclusion': '전문적인 조류 연구 장비는 상당한 투자를 나타내며 안전하고 효과적인 사용을 위한 적절한 훈련이 필요합니다. 이러한 도구들은 과학자들이 조류 생물학에 대한 우리의 이해를 발전시키고 보전 노력을 지원하는 정밀한 데이터를 수집할 수 있게 합니다<span class="emoji">🌟</span>. 장비의 선택은 특정 연구 목표, 대상 종, 연구 설계 요구사항에 따라 달라집니다.'
    },
    'ja': {
        'title': '鳥類研究機器と研究ツール - BirdAiSnap',
        'main_title': '🔬 鳥類研究機器と研究ツール',
        'quote': '鳥類学研究と専門的な鳥類研究で使用される科学的ツールと機器を探求しましょう',
        'intro': '専門的な鳥類研究と鳥類学研究には、基本的なバードウォッチング機器を超えた専門機器が必要です。これらの科学的ツールにより、研究者は詳細な研究を行い、データを収集し、鳥類生物学の理解を深めることができます<span class="emoji">🔬</span>。このガイドでは、専門的な鳥類研究と高度な研究で使用される必須機器を扱います。',
        'banding_title': 'バンディングとマーキング機器',
        'banding_text': '鳥類バンディングは、時間を通じて個々の鳥を追跡する重要な研究技術です。専門研究者は、番号付き金属バンド、カラーバンド、適用ツールを含む専門機器を使用します<span class="emoji">🏷️</span>。現代の研究では、GPS送信機と無線テレメトリー装置も使用して、移動パターンと行動を追跡します。',
        'capture_title': '捕獲と取り扱い機器',
        'capture_text': '研究のための安全な鳥類捕獲には、ストレスと怪我を最小限に抑えるよう設計された専門ネットとトラップが必要です。かすみ網は最も一般的な捕獲方法で、適切な設置と継続的な監視が必要です<span class="emoji">🕸️</span>。専門的な取り扱い技術と機器により、研究手順中の鳥の安全が確保されます。',
        'safety_title': '⚠️ 安全プロトコル',
        'safety_text': '鳥類の捕獲と取り扱いには、適切な訓練、許可、厳格な倫理ガイドラインの遵守が必要です。ライセンスを持つ研究者のみがこれらの技術を使用すべきです。',
        'measurement_title': '測定とデータ収集ツール',
        'measurement_text': '正確な測定は鳥類学研究に不可欠です。鳥類研究用に設計された専門キャリパー、定規、スケールは正確な形態学的データを提供します<span class="emoji">📏</span>。デジタルデータロガーとフィールドコンピューターはデータ収集を合理化し、転写エラーを減らします。',
        'nest_title': '巣監視機器',
        'nest_text': '繁殖生態学研究には、妨害なしに巣を監視するための専門機器が必要です。リモートカメラ、温度ロガー、伸縮ミラーにより、研究者は営巣行動と成功率を研究できます<span class="emoji">🥚</span>。現代技術により、最小限の人間の干渉で継続的な監視が可能になります。',
        'acoustic_title': '音響研究機器',
        'acoustic_text': '鳥類発声研究では、プロ仕様の録音機器と分析ソフトウェアを使用します。指向性マイク、デジタルレコーダー、スペクトログラム分析プログラムにより、鳥類コミュニケーションの詳細な研究が可能になります<span class="emoji">🎵</span>。自動録音ステーションは広域で鳥類活動を継続的に監視できます。',
        'research_title': '🔬 研究応用',
        'research_text': 'これらのツールは、移動生態学、繁殖生物学、個体群動態、行動研究、保全生物学を含む様々な研究分野を支援します。',
        'lab_title': '実験室機器',
        'lab_text': '鳥類サンプルの実験室分析には、遺伝学的、生理学的、病理学的研究のための専門機器が必要です。顕微鏡、遠心分離機、分子生物学機器により、羽毛、血液、組織サンプルの詳細な分析が可能になります<span class="emoji">🧪</span>。この機器は進化、疾病生態学、保全遺伝学の研究を支援します。',
        'conclusion': '専門的な鳥類研究機器は重要な投資を表し、安全で効果的な使用のための適切な訓練が必要です。これらのツールにより、科学者は鳥類生物学の理解を深め、保全努力を支援する正確なデータを収集できます<span class="emoji">🌟</span>。機器の選択は、特定の研究目標、対象種、研究設計要件によって異なります。'
    },
    'es': {
        'title': 'Equipos de Estudio de Aves y Herramientas de Investigación - BirdAiSnap',
        'main_title': '🔬 Equipos de Estudio de Aves y Herramientas de Investigación',
        'quote': 'Explora las herramientas científicas y equipos utilizados en investigación ornitológica y estudio profesional de aves',
        'intro': 'El estudio profesional de aves y la investigación ornitológica requieren equipos especializados más allá del equipo básico de observación de aves. Estas herramientas científicas permiten a los investigadores realizar estudios detallados, recopilar datos y avanzar nuestro entendimiento de la biología aviar<span class="emoji">🔬</span>. Esta guía cubre el equipo esencial utilizado en investigación profesional de aves y estudio avanzado.',
        'banding_title': 'Equipos de Anillamiento y Marcado',
        'banding_text': 'El anillamiento de aves es una técnica de investigación crucial para rastrear aves individuales a lo largo del tiempo. Los investigadores profesionales utilizan equipos especializados incluyendo anillas metálicas numeradas, anillas de colores y herramientas de aplicación<span class="emoji">🏷️</span>. Los estudios modernos también emplean transmisores GPS y dispositivos de radiotelemetría para rastrear patrones de migración y comportamiento.',
        'capture_title': 'Equipos de Captura y Manejo',
        'capture_text': 'La captura segura de aves para investigación requiere redes y trampas especializadas diseñadas para minimizar el estrés y las lesiones. Las redes de niebla son el método de captura más común, requiriendo configuración adecuada y monitoreo constante<span class="emoji">🕸️</span>. Las técnicas y equipos profesionales de manejo aseguran la seguridad de las aves durante los procedimientos de investigación.',
        'safety_title': '⚠️ Protocolo de Seguridad',
        'safety_text': 'La captura y manejo de aves requiere entrenamiento adecuado, permisos y adherencia a pautas éticas estrictas. Solo investigadores licenciados deben usar estas técnicas.',
        'measurement_title': 'Herramientas de Medición y Recolección de Datos',
        'measurement_text': 'Las mediciones precisas son esenciales para la investigación ornitológica. Calibradores especializados, reglas y balanzas diseñadas para investigación de aves proporcionan datos morfométricos precisos<span class="emoji">📏</span>. Los registradores de datos digitales y computadoras de campo agilizan la recolección de datos y reducen errores de transcripción.',
        'nest_title': 'Equipos de Monitoreo de Nidos',
        'nest_text': 'Los estudios de ecología reproductiva requieren equipos especializados para monitorear nidos sin perturbación. Cámaras remotas, registradores de temperatura y espejos extensibles permiten a los investigadores estudiar el comportamiento de anidación y las tasas de éxito<span class="emoji">🥚</span>. La tecnología moderna permite monitoreo continuo con interferencia humana mínima.',
        'acoustic_title': 'Equipos de Investigación Acústica',
        'acoustic_text': 'Los estudios de vocalización de aves utilizan equipos de grabación de grado profesional y software de análisis. Micrófonos direccionales, grabadores digitales y programas de análisis de espectrogramas permiten el estudio detallado de la comunicación aviar<span class="emoji">🎵</span>. Las estaciones de grabación automatizadas pueden monitorear la actividad de aves continuamente en áreas grandes.',
        'research_title': '🔬 Aplicaciones de Investigación',
        'research_text': 'Estas herramientas apoyan varias áreas de investigación incluyendo ecología de migración, biología reproductiva, dinámicas poblacionales, estudios de comportamiento y biología de conservación.',
        'lab_title': 'Equipos de Laboratorio',
        'lab_text': 'El análisis de laboratorio de muestras de aves requiere equipos especializados para estudios genéticos, fisiológicos y patológicos. Microscopios, centrífugas y equipos de biología molecular permiten análisis detallado de plumas, sangre y muestras de tejido<span class="emoji">🧪</span>. Este equipo apoya la investigación en evolución, ecología de enfermedades y genética de conservación.',
        'conclusion': 'El equipo profesional de investigación de aves representa una inversión significativa y requiere entrenamiento adecuado para uso seguro y efectivo. Estas herramientas permiten a los científicos recopilar datos precisos que avanzan nuestro entendimiento de la biología aviar y apoyan los esfuerzos de conservación<span class="emoji">🌟</span>. La elección del equipo depende de objetivos de investigación específicos, especies objetivo y requisitos de diseño del estudio.'
    },
    'fr': {
        'title': 'Équipements d\'Étude des Oiseaux et Outils de Recherche - BirdAiSnap',
        'main_title': '🔬 Équipements d\'Étude des Oiseaux et Outils de Recherche',
        'quote': 'Explorez les outils scientifiques et équipements utilisés dans la recherche ornithologique et l\'étude professionnelle des oiseaux',
        'intro': 'L\'étude professionnelle des oiseaux et la recherche ornithologique nécessitent des équipements spécialisés au-delà de l\'équipement de base d\'observation des oiseaux. Ces outils scientifiques permettent aux chercheurs de mener des études détaillées, de collecter des données et de faire progresser notre compréhension de la biologie aviaire<span class="emoji">🔬</span>. Ce guide couvre l\'équipement essentiel utilisé dans la recherche professionnelle sur les oiseaux et l\'étude avancée.',
        'banding_title': 'Équipements de Baguage et de Marquage',
        'banding_text': 'Le baguage des oiseaux est une technique de recherche cruciale pour suivre les oiseaux individuels dans le temps. Les chercheurs professionn