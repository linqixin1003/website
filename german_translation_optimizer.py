#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def create_optimized_german_content():
    """创建优化的德语科学研究设备内容"""
    
    html_content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vogelforschungsausrüstung und Forschungswerkzeuge - BirdAiSnap</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.95);
            margin-top: 20px;
            margin-bottom: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .title {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .quote-box {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .quote-text {
            font-size: 1.2em;
            font-style: italic;
        }
        
        .section-title {
            color: #2c3e50;
            font-size: 1.5em;
            margin: 25px 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        
        .main-text {
            color: #34495e;
            margin: 15px 0;
            font-size: 1.1em;
            text-align: justify;
        }
        
        .tip-box {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }
        
        .tip-title {
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 1.1em;
        }
        
        .equipment-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        
        .equipment-card {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .equipment-title {
            color: #2c3e50;
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .equipment-description {
            color: #34495e;
            font-size: 1em;
            line-height: 1.5;
        }
        
        .emoji {
            font-size: 1.2em;
            margin: 0 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">🔬 Vogelforschungsausrüstung und Forschungswerkzeuge</h1>
        
        <div class="quote-box">
            <div class="quote-text">
                Entdecken Sie die wissenschaftlichen Werkzeuge und Ausrüstungen für ornithologische Forschung und professionelle Vogelstudien
            </div>
        </div>
        
        <div class="main-text">
            Professionelle Vogelforschung und ornithologische Studien erfordern spezialisierte Ausrüstung, die über grundlegende Vogelbeobachtungsgeräte hinausgeht. Diese wissenschaftlichen Werkzeuge ermöglichen es Forschern, detaillierte Studien durchzuführen, Daten zu sammeln und unser Verständnis der Vogelbiologie voranzutreiben<span class="emoji">🔬</span>. Dieser Leitfaden behandelt die wesentliche Ausrüstung für professionelle Vogelforschung und fortgeschrittene Studien.
        </div>
        
        <div class="section-title">Beringung und Markierungsausrüstung</div>
        <div class="main-text">
            Die Vogelberingung ist eine wichtige Forschungstechnik zur Verfolgung einzelner Vögel über die Zeit. Professionelle Forscher verwenden spezialisierte Ausrüstung, einschließlich nummerierter Metallringe, Farbringe und Anwendungswerkzeuge<span class="emoji">🏷️</span>. Moderne Forschung nutzt auch GPS-Sender und Radiotelemetrie-Geräte zur Verfolgung von Zugmustern und Verhalten.
        </div>
        
        <div class="equipment-grid">
            <div class="equipment-card">
                <div class="equipment-title">🏷️ Beringungsausrüstung</div>
                <div class="equipment-description">
                    <strong>Metallringe:</strong> Nummerierte Aluminiumringe für permanente Identifikation<br>
                    <strong>Farbringe:</strong> Kunststoffringe für Feldidentifikation<br>
                    <strong>Beringungszangen:</strong> Spezialisierte Werkzeuge für sichere Ringanbringung<br>
                    <strong>Ringgrößenführer:</strong> Referenztabellen für korrekte Ringgrößen
                </div>
            </div>
            
            <div class="equipment-card">
                <div class="equipment-title">📡 Verfolgungstechnologie</div>
                <div class="equipment-description">
                    <strong>GPS-Sender:</strong> Satellitenbasierte Verfolgungsgeräte für Zugstudien<br>
                    <strong>Radiosender:</strong> VHF-Sender für lokale Verfolgung<br>
                    <strong>Geolokatoren:</strong> Lichtbasierte Positionsrekorder<br>
                    <strong>Empfangsgeräte:</strong> Antennen und Empfänger für Signaldetektion
                </div>
            </div>
        </div>
        
        <div class="section-title">Fang- und Handhabungsausrüstung</div>
        <div class="main-text">
            Sicherer Vogelfang für Forschungszwecke erfordert speziell entwickelte Netze und Fallen, um Stress und Verletzungen zu minimieren. Nebelnetze sind die häufigste Fangmethode und erfordern ordnungsgemäße Aufstellung und kontinuierliche Überwachung<span class="emoji">🕸️</span>. Professionelle Handhabungstechniken und -ausrüstung gewährleisten die Sicherheit der Vögel während der Forschung.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">⚠️ Sicherheitsprotokolle</div>
            Vogelfang und -handhabung erfordern angemessene Ausbildung, Genehmigungen und die Einhaltung strenger ethischer Richtlinien. Nur lizenzierte Forscher sollten diese Techniken anwenden.
        </div>
        
        <div class="section-title">Mess- und Datenerfassungswerkzeuge</div>
        <div class="main-text">
            Präzise Messungen sind für ornithologische Forschung von entscheidender Bedeutung. Professionelle Messschieber, Lineale und Waagen, die speziell für die Vogelforschung entwickelt wurden, liefern genaue morphologische Daten<span class="emoji">📏</span>. Digitale Datenlogger und Feldcomputer vereinfachen die Datenerfassung und reduzieren Transkriptionsfehler.
        </div>
        
        <div class="section-title">Laborausrüstung</div>
        <div class="main-text">
            Die Laboranalyse von Vogelproben erfordert spezialisierte Ausrüstung für genetische, physiologische und pathologische Studien. Mikroskope, Zentrifugen und molekularbiologische Ausrüstung ermöglichen detaillierte Analysen von Federn-, Blut- und Gewebeproben<span class="emoji">🧪</span>. Diese Ausrüstung unterstützt Forschung in Evolution, Krankheitsökologie und Naturschutzgenetik.
        </div>
        
        <div class="main-text">
            Professionelle Vogelforschungsausrüstung stellt eine erhebliche Investition dar und erfordert angemessene Ausbildung für sichere und effektive Nutzung. Diese Werkzeuge ermöglichen es Wissenschaftlern, präzise Daten zu sammeln, unser Verständnis der Vogelbiologie voranzutreiben und Naturschutzmaßnahmen zu unterstützen<span class="emoji">🌟</span>. Die Ausrüstungsauswahl hängt von spezifischen Forschungszielen, Zielarten und Studiendesign-Anforderungen ab.
        </div>
    </div>
</body>
</html>'''
    
    return html_content

def update_german_file():
    """更新德语设备文件"""
    
    # 创建目录路径
    file_path = "de/knowledge/02-essential-equipment.html"
    
    # 检查目录是否存在
    os.makedirs("de/knowledge", exist_ok=True)
    
    # 获取优化的德语内容
    content = create_optimized_german_content()
    
    # 写入文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 德语翻译已优化并更新: {file_path}")
        return True
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {e}")
        return False

def optimize_other_german_files():
    """优化其他德语文件的翻译质量"""
    
    # 需要优化的文件列表
    files_to_optimize = [
        "de/birdwatching/01-getting-started.html",
        "de/knowledge/01-beginners-guide.html",
        "de/pet-care/01-choosing-right-bird.html",
        "de/scientific-wonders/01-bird-flight-mechanics.html"
    ]
    
    optimized_count = 0
    
    for file_path in files_to_optimize:
        if os.path.exists(file_path):
            try:
                # 读取现有文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 执行基本的德语翻译优化
                optimized_content = improve_german_translation(content)
                
                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(optimized_content)
                
                print(f"✅ 已优化: {file_path}")
                optimized_count += 1
                
            except Exception as e:
                print(f"❌ 优化失败 {file_path}: {e}")
        else:
            print(f"⚠️ 文件不存在: {file_path}")
    
    return optimized_count

def improve_german_translation(content):
    """改进德语翻译质量"""
    
    # 常见的翻译改进映射
    improvements = {
        # 修复常见的翻译错误
        'Vogel watching': 'Vogelbeobachtung',
        'Vogel watcher': 'Vogelbeobachter',
        'bird watching': 'Vogelbeobachtung',
        'bird watcher': 'Vogelbeobachter',
        'Fernglas sind': 'Ferngläser sind',
        'meiste wesentlich': 'wichtigste',
        'piece von': 'Teil der',
        'any Vogel': 'jeden Vogel',
        'der meiste': 'die meisten',
        'beliebt Wahl': 'beliebte Wahl',
        'among birders': 'unter Vogelbeobachtern',
        'ist 8x42': 'sind 8x42',
        'which offer': 'die bieten',
        'gut balance': 'gute Balance',
        'von magnification': 'der Vergrößerung',
        'field von view': 'Sichtfeld',
        'light-gathering Fähigkeit': 'Lichtsammelfähigkeit',
        'wann selecting': 'bei der Auswahl',
        'für Vogel watching': 'für die Vogelbeobachtung',
        'consider der': 'berücksichtigen Sie die',
        'und objective': 'und Objektivlinsen',
        'lens diameter': 'Durchmesser',
        'Higher magnification für': 'Höhere Vergrößerung für',
        'distant Vögel': 'entfernte Vögel',
        'but requires': 'aber erfordert',
        'steadier hands': 'ruhigere Hände',
        'und hat a': 'und hat ein',
        'narrower field': 'schmaleres Sichtfeld',
        'comprehensive field': 'umfassender Feld',
        'Leitfaden ist': 'Leitfaden ist',
        'Ihr companion': 'Ihr Begleiter',
        'für identifying': 'zur Identifizierung',
        'der Vögel': 'der Vögel',
        'Sie encounter': 'Sie antreffen',
        'modern field': 'moderne Feld',
        'guides include': 'Leitfäden enthalten',
        'detailed illustrations': 'detaillierte Illustrationen',
        'range maps': 'Verbreitungskarten',
        'behavioral descriptions': 'Verhaltensbeschreibungen',
        'das helfen': 'die helfen',
        'Sie distinguish': 'Ihnen zu unterscheiden',
        'between ähnlich': 'zwischen ähnlichen',
        'Art': 'Arten',
        'While not': 'Obwohl nicht',
        'wesentlich für': 'wesentlich für',
        'allows Sie': 'ermöglicht es Ihnen',
        'zu capture': 'zu erfassen',
        'und share': 'und zu teilen',
        'Ihr discoveries': 'Ihre Entdeckungen',
        'requires spezifische': 'erfordert spezifische',
        'considerations due': 'Überlegungen aufgrund',
        'zu der': 'der',
        'oft distant': 'oft entfernten',
        'und schnell-moving': 'und sich schnell bewegenden',
        'Natur von': 'Natur der',
        'Ihr subjects': 'Ihre Motive'
    }
    
    # 应用改进
    improved_content = content
    for old, new in improvements.items():
        improved_content = improved_content.replace(old, new)
    
    return improved_content

def create_comprehensive_german_optimizer():
    """创建全面的德语优化工具"""
    
    print("🔧 创建全面的德语翻译优化工具...")
    
    # 检查德语目录结构
    german_dirs = ['de/birdwatching', 'de/knowledge', 'de/pet-care', 'de/scientific-wonders', 'de/ecology']
    
    for dir_path in german_dirs:
        if os.path.exists(dir_path):
            files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
            print(f"📁 {dir_path}: {len(files)} 个HTML文件")
        else:
            print(f"⚠️ 目录不存在: {dir_path}")

def main():
    """主函数"""
    print("🚀 开始德语翻译优化...")
    print("=" * 50)
    
    # 1. 优化设备页面
    print("1️⃣ 优化科学研究设备页面...")
    equipment_success = update_german_file()
    
    # 2. 检查项目结构
    print("\n2️⃣ 检查德语文件结构...")
    create_comprehensive_german_optimizer()
    
    # 3. 优化其他文件
    print("\n3️⃣ 优化其他德语文件...")
    other_files_count = optimize_other_german_files()
    
    # 总结
    print("\n" + "=" * 50)
    print("🎉 德语翻译优化完成！")
    print(f"✅ 设备页面优化: {'成功' if equipment_success else '失败'}")
    print(f"✅ 其他文件优化: {other_files_count} 个文件")
    print("\n主要改进:")
    print("- 使用更自然的德语表达")
    print("- 专业术语翻译更准确")
    print("- 语法结构更符合德语习惯")
    print("- 修复常见翻译错误")
    print("- 保持科学研究设备的专业性")

if __name__ == "__main__":
    main()
