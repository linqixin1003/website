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
            专业鸟类研究和鸟类学研究需要超越基本观鸟设备的专业设备。这些科学工具使研究人员能够进行详细研究、收集数据并推进我们对鸟类生物学的理解<span class="emoji">🔬</span>。本指南涵盖了专业鸟类研究和高级研究中使用的基本设备。
        </div>
        
        <div class="section-title">环志和标记设备</div>
        <div class="main-text">
            鸟类环志是追踪个体鸟类随时间变化的重要研究技术。专业研究人员使用专门设备，包括编号金属环、彩色环和应用工具<span class="emoji">🏷️</span>。现代研究还采用GPS发射器和无线电遥测设备来追踪迁徙模式和行为。
        </div>
        
        <div class="equipment-grid">
            <div class="equipment-card">
                <div class="equipment-title">🏷️ 环志设备</div>
                <div class="equipment-description">
                    <strong>金属环:</strong> 用于永久识别的编号铝环<br>
                    <strong>彩色环:</strong> 用于野外识别的塑料环<br>
                    <strong>环志钳:</strong> 安全应用环的专用工具<br>
                    <strong>环尺寸指南:</strong> 正确环尺寸的参考图表
                </div>
            </div>
            
            <div class="equipment-card">
                <div class="equipment-title">📡 追踪技术</div>
                <div class="equipment-description">
                    <strong>GPS发射器:</strong> 用于迁徙研究的卫星追踪设备<br>
                    <strong>无线电发射器:</strong> 用于本地追踪的VHF发射器<br>
                    <strong>地理定位器:</strong> 基于光线的位置记录器<br>
                    <strong>接收设备:</strong> 用于信号检测的天线和接收器
                </div>
            </div>
        </div>
        
        <div class="section-title">捕获和处理设备</div>
        <div class="main-text">
            研究用的安全鸟类捕获需要专门设计的网具和陷阱，以最大限度地减少压力和伤害。雾网是最常见的捕获方法，需要适当的设置和持续监控<span class="emoji">🕸️</span>。专业的处理技术和设备确保研究过程中鸟类的安全。
        </div>
        
        <div class="tip-box">
            <div class="tip-title">⚠️ 安全协议</div>
            鸟类捕获和处理需要适当的培训、许可证和遵守严格的伦理准则。只有持证研究人员才应使用这些技术。
        </div>
        
        <div class="section-title">测量和数据收集工具</div>
        <div class="main-text">
            精确测量对鸟类学研究至关重要。专为鸟类研究设计的专业卡尺、尺子和天平提供准确的形态学数据<span class="emoji">📏</span>。数字数据记录器和野外计算机简化数据收集并减少转录错误。
        </div>
        
        <div class="section-title">实验室设备</div>
        <div class="main-text">
            鸟类样本的实验室分析需要专门设备进行遗传学、生理学和病理学研究。显微镜、离心机和分子生物学设备实现了对羽毛、血液和组织样本的详细分析<span class="emoji">🧪</span>。这些设备支持进化、疾病生态学和保护遗传学研究。
        </div>
        
        <div class="main-text">
            专业鸟类研究设备代表着重大投资，需要适当培训才能安全有效地使用。这些工具使科学家能够收集精确数据，推进我们对鸟类生物学的理解并支持保护工作<span class="emoji">🌟</span>。设备选择取决于具体研究目标、目标物种和研究设计要求。
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