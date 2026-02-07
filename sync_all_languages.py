#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完全同步系统 - 将所有T1语言同步到中文版本结构
方案A：完全同步，确保100%一致性
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path('/Users/conalin/website')

# T1语言配置
T1_LANGUAGES = {
    'fr': {
        'name': '法语',
        'category_map': {'Bowel Health': 'Santé Intestinale', 'Urinary Health': 'Santé Urinaire', 'Menstrual Health': 'Santé Menstruelle', 'Hydration': 'Hydratation', 'Weight Management': 'Gestion du Poids', 'Physical Fitness': 'Forme Physique', 'Nutrition': 'Nutrition', 'Digestion': 'Digestion', 'Body Self-Check': 'Auto-Surveillance'},
        'read_time_map': {'min read': 'min de lecture'},
        'tldr_title': '⚡ Lecture Rapide (TL;DR)',
        'back_text': '← Retour à la liste',
    },
    'de': {
        'name': '德语',
        'category_map': {'Bowel Health': 'Darmgesundheit', 'Urinary Health': 'Harnwegsgesundheit', 'Menstrual Health': 'Menstruationsgesundheit', 'Hydration': 'Flüssigkeitszufuhr', 'Weight Management': 'Gewichtsmanagement', 'Physical Fitness': 'Körperliche Fitness', 'Nutrition': 'Ernährung', 'Digestion': 'Verdauung', 'Body Self-Check': 'Selbstkontrolle'},
        'read_time_map': {'min read': 'Min. Lesezeit'},
        'tldr_title': '⚡ Schnellübersicht (TL;DR)',
        'back_text': '← Zurück',
    },
    'es': {
        'name': '西班牙语',
        'category_map': {'Bowel Health': 'Salud Intestinal', 'Urinary Health': 'Salud Urinaria', 'Menstrual Health': 'Salud Menstrual', 'Hydration': 'Hidratación', 'Weight Management': 'Control de Peso', 'Physical Fitness': 'Aptitud Física', 'Nutrition': 'Nutrición', 'Digestion': 'Digestión', 'Body Self-Check': 'Autocontrol'},
        'read_time_map': {'min read': 'min de lectura'},
        'tldr_title': '⚡ Resumen Rápido (TL;DR)',
        'back_text': '← Volver',
    },
    'it': {
        'name': '意大利语',
        'category_map': {'Bowel Health': 'Salute Intestinale', 'Urinary Health': 'Salute Urinaria', 'Menstrual Health': 'Salute Mestruale', 'Hydration': 'Idratazione', 'Weight Management': 'Gestione del Peso', 'Physical Fitness': 'Fitness Fisico', 'Nutrition': 'Nutrizione', 'Digestion': 'Digestione', 'Body Self-Check': 'Autocontrollo'},
        'read_time_map': {'min read': 'min di lettura'},
        'tldr_title': '⚡ Lettura Rapida (TL;DR)',
        'back_text': '← Indietro',
    },
    'ja': {
        'name': '日语',
        'category_map': {'Bowel Health': '腸の健康', 'Urinary Health': '泌尿器の健康', 'Menstrual Health': '月経の健康', 'Hydration': '水分補給', 'Weight Management': '体重管理', 'Physical Fitness': '身体の健康', 'Nutrition': '栄養', 'Digestion': '消化', 'Body Self-Check': '自己チェック'},
        'read_time_map': {'min read': '分で読める'},
        'tldr_title': '⚡ 30秒で読む (TL;DR)',
        'back_text': '← 戻る',
    },
    'ko': {
        'name': '韩语',
        'category_map': {'Bowel Health': '장 건강', 'Urinary Health': '비뇨기 건강', 'Menstrual Health': '생리 건강', 'Hydration': '수분 섭취', 'Weight Management': '체중 관리', 'Physical Fitness': '신체 건강', 'Nutrition': '영양', 'Digestion': '소화', 'Body Self-Check': '자가 점검'},
        'read_time_map': {'min read': '분 읽기'},
        'tldr_title': '⚡ 빠른 읽기 (TL;DR)',
        'back_text': '← 뒤로',
    },
    'pt': {
        'name': '葡萄牙语',
        'category_map': {'Bowel Health': 'Saúde Intestinal', 'Urinary Health': 'Saúde Urinária', 'Menstrual Health': 'Saúde Menstrual', 'Hydration': 'Hidratação', 'Weight Management': 'Gestão de Peso', 'Physical Fitness': 'Fitness Físico', 'Nutrition': 'Nutrição', 'Digestion': 'Digestão', 'Body Self-Check': 'Auto-verificação'},
        'read_time_map': {'min read': 'min de leitura'},
        'tldr_title': '⚡ Leitura Rápida (TL;DR)',
        'back_text': '← Voltar',
    },
    'ru': {
        'name': '俄语',
        'category_map': {'Bowel Health': 'Здоровье кишечника', 'Urinary Health': 'Здоровье мочевыводящих путей', 'Menstrual Health': 'Менструальное здоровье', 'Hydration': 'Гидратация', 'Weight Management': 'Управление весом', 'Physical Fitness': 'Физическая форма', 'Nutrition': 'Питание', 'Digestion': 'Пищеварение', 'Body Self-Check': 'Самоконтроль'},
        'read_time_map': {'min read': 'мин чтения'},
        'tldr_title': '⚡ Быстрое чтение (TL;DR)',
        'back_text': '← Назад',
    },
}

def translate_text(text, target_lang):
    """
    使用AI翻译中文文本到目标语言
    这是一个占位函数，实际应该调用AI翻译API
    由于工作量巨大，这里返回标记，表示需要翻译
    """
    # TODO: 集成真实的AI翻译API（OpenAI, DeepL等）
    # 目前返回标记，实际使用时需要替换
    return f"[需要翻译到{target_lang}] {text}"

def extract_zh_structure(zh_soup):
    """从中文HTML中提取完整结构"""
    
    structure = {
        'title': '',
        'category': '',
        'read_time': '',
        'theme': 'bowel',
        'svg': '',
        'tldr_items': [],
        'intro': '',
        'sections': [],
    }
    
    # 标题
    title_elem = zh_soup.find('h1', class_='hero-title')
    if title_elem:
        structure['title'] = title_elem.get_text(strip=True)
    
    # 分类和阅读时间
    meta_top = zh_soup.find('div', class_='article-meta-top')
    if meta_top:
        spans = meta_top.find_all('span')
        if len(spans) >= 1:
            structure['category'] = spans[0].get_text(strip=True)
        if len(spans) >= 3:
            structure['read_time'] = spans[2].get_text(strip=True)
    
    # 主题
    html_elem = zh_soup.find('html')
    if html_elem and html_elem.get('data-theme'):
        structure['theme'] = html_elem.get('data-theme')
    
    # SVG
    svg_elem = zh_soup.find('svg')
    if svg_elem:
        structure['svg'] = str(svg_elem)
    
    # TL;DR
    tldr_elem = zh_soup.find('div', class_='summary-card')
    if tldr_elem:
        tldr_items = tldr_elem.find_all('li')
        for item in tldr_items:
            # 保留HTML格式（如strong标签）
            structure['tldr_items'].append(str(item))
    
    # 引言
    intro_elem = zh_soup.find('p', class_='intro-text')
    if intro_elem:
        structure['intro'] = intro_elem.get_text(strip=True)
    
    # 提取所有sections（按H2分组）
    content_block = zh_soup.find('div', class_='content-block')
    if content_block:
        current_section = None
        
        for elem in content_block.children:
            if hasattr(elem, 'name') and elem.name == 'h2':
                # 保存上一个section
                if current_section:
                    structure['sections'].append(current_section)
                
                # 开始新section
                current_section = {
                    'h2': elem.get_text(strip=True),
                    'content': []
                }
            
            elif current_section and hasattr(elem, 'name'):
                if elem.name == 'p':
                    # 检查是否是info-box或warning-box内的p
                    parent = elem.find_parent(['div'])
                    if parent and ('info-box' in parent.get('class', []) or 'warning-box' in parent.get('class', [])):
                        continue
                    
                    current_section['content'].append({
                        'type': 'p',
                        'text': elem.get_text(strip=True)
                    })
                
                elif elem.name == 'ul':
                    items = []
                    for li in elem.find_all('li'):
                        # 保留HTML格式
                        items.append(str(li))
                    current_section['content'].append({
                        'type': 'ul',
                        'items': items
                    })
                
                elif elem.name == 'div':
                    div_classes = elem.get('class', [])
                    
                    if 'checklist' in div_classes:
                        checklist_items = []
                        for item in elem.find_all('div', class_='checklist-item'):
                            # 提取完整HTML
                            item_html = item.find('div', recursive=False)
                            if item_html:
                                checklist_items.append(str(item_html))
                        current_section['content'].append({
                            'type': 'checklist',
                            'items': checklist_items
                        })
                    
                    elif 'info-box' in div_classes:
                        box_text = elem.get_text(strip=True)
                        current_section['content'].append({
                            'type': 'info-box',
                            'text': box_text
                        })
                    
                    elif 'warning-box' in div_classes:
                        warning_items = []
                        for item in elem.find_all('li'):
                            warning_items.append(str(item))
                        current_section['content'].append({
                            'type': 'warning-box',
                            'items': warning_items
                        })
        
        # 保存最后一个section
        if current_section:
            structure['sections'].append(current_section)
    
    return structure

def generate_lang_html(structure, lang_code, lang_config):
    """根据提取的结构生成目标语言HTML"""
    
    # 翻译标题
    fr_title = translate_text(structure['title'], lang_code)
    
    # 翻译分类
    fr_category = lang_config['category_map'].get(structure['category'], structure['category'])
    
    # 翻译阅读时间
    fr_read_time = structure['read_time']
    for en, translated in lang_config['read_time_map'].items():
        fr_read_time = fr_read_time.replace(en, translated)
    
    # 翻译TL;DR
    fr_tldr_items = []
    for item_html in structure['tldr_items']:
        # 提取文本并翻译
        item_soup = BeautifulSoup(item_html, 'html.parser')
        item_text = item_soup.get_text(strip=True)
        translated_text = translate_text(item_text, lang_code)
        
        # 保留strong标签
        if '<strong>' in item_html:
            strong_match = re.search(r'<strong>(.*?)</strong>', item_html)
            if strong_match:
                strong_text = strong_match.group(1)
                translated_strong = translate_text(strong_text, lang_code)
                translated_text = translated_text.replace(strong_text, translated_strong)
                # 重建HTML
                translated_html = item_html.replace(strong_text, translated_strong)
                translated_html = translated_html.replace(item_text, translated_text)
                fr_tldr_items.append(translated_html)
            else:
                fr_tldr_items.append(f'<li>{translated_text}</li>')
        else:
            fr_tldr_items.append(f'<li>{translated_text}</li>')
    
    # 翻译引言
    fr_intro = translate_text(structure['intro'], lang_code)
    
    # 翻译sections
    fr_sections = []
    for section in structure['sections']:
        fr_section = {
            'h2': translate_text(section['h2'], lang_code),
            'content': []
        }
        
        for content in section['content']:
            if content['type'] == 'p':
                fr_section['content'].append({
                    'type': 'p',
                    'text': translate_text(content['text'], lang_code)
                })
            elif content['type'] == 'ul':
                translated_items = []
                for item_html in content['items']:
                    item_soup = BeautifulSoup(item_html, 'html.parser')
                    item_text = item_soup.get_text(strip=True)
                    translated_text = translate_text(item_text, lang_code)
                    translated_items.append(f'<li>{translated_text}</li>')
                fr_section['content'].append({
                    'type': 'ul',
                    'items': translated_items
                })
            elif content['type'] == 'checklist':
                translated_items = []
                for item_html in content['items']:
                    item_soup = BeautifulSoup(item_html, 'html.parser')
                    item_text = item_soup.get_text(strip=True)
                    translated_text = translate_text(item_text, lang_code)
                    # 保留strong标签
                    if '<strong>' in item_html:
                        strong_match = re.search(r'<strong>(.*?)</strong>', item_html)
                        if strong_match:
                            strong_text = strong_match.group(1)
                            translated_strong = translate_text(strong_text, lang_code)
                            translated_text = translated_text.replace(strong_text, translated_strong)
                            translated_html = f'<strong>{translated_strong}</strong> {translated_text.replace(strong_text, "").strip()}'
                        else:
                            translated_html = translated_text
                    else:
                        translated_html = translated_text
                    translated_items.append(f'<div class="checklist-item"><div class="check-icon">✓</div><div>{translated_html}</div></div>')
                fr_section['content'].append({
                    'type': 'checklist',
                    'items': translated_items
                })
            elif content['type'] == 'info-box':
                fr_section['content'].append({
                    'type': 'info-box',
                    'text': translate_text(content['text'], lang_code)
                })
            elif content['type'] == 'warning-box':
                translated_items = []
                for item_html in content['items']:
                    item_soup = BeautifulSoup(item_html, 'html.parser')
                    item_text = item_soup.get_text(strip=True)
                    translated_text = translate_text(item_text, lang_code)
                    # 保留strong标签
                    if '<strong>' in item_html:
                        strong_match = re.search(r'<strong>(.*?)</strong>', item_html)
                        if strong_match:
                            strong_text = strong_match.group(1)
                            translated_strong = translate_text(strong_text, lang_code)
                            translated_text = translated_text.replace(strong_text, translated_strong)
                            translated_html = f'<li><strong>{translated_strong}</strong> {translated_text.replace(strong_text, "").strip()}</li>'
                        else:
                            translated_html = f'<li>{translated_text}</li>'
                    else:
                        translated_html = f'<li>{translated_text}</li>'
                    translated_items.append(translated_html)
                fr_section['content'].append({
                    'type': 'warning-box',
                    'items': translated_items
                })
        
        fr_sections.append(fr_section)
    
    # 生成HTML
    html_template = '''<!DOCTYPE html>
<html lang="{lang_code}" data-theme="{theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title} - Happy Poop</title>
    <link rel="stylesheet" href="../../article-theme-v2.css">
</head>
<body>
    <header class="hero-section">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="article-meta-top">
                <span>{category}</span>
                <span>•</span>
                <span>{read_time}</span>
            </div>
            <h1 class="hero-title">{title}</h1>
            <div class="hero-image">{svg}</div>
        </div>
    </header>

    <div class="summary-card">
        <div class="summary-title">{tldr_title}</div>
        <ul class="summary-list">
{tldr_items}
        </ul>
    </div>

    <article class="content-container">
        <div class="content-block">
            <p class="intro-text">{intro}</p>
{sections}
        </div>
    </article>

    <nav class="floating-nav">
        <a href="../../happy-poop-mobile.html" class="back-btn">{back_text}</a>
        <a href="#" class="share-btn" onclick="navigator.share({{title: '{title}', url: window.location.href}}); return false;">📤</a>
    </nav>
    <script>
        document.querySelectorAll('.checklist-item').forEach(item => {{
            item.addEventListener('click', () => {{
                item.style.backgroundColor = '#F3F4F6';
                setTimeout(() => item.style.backgroundColor = 'transparent', 200);
            }});
        }});
    </script>
</body>
</html>'''
    
    # 构建TL;DR HTML
    tldr_html = '\n'.join([f'            {item}' for item in fr_tldr_items])
    
    # 构建sections HTML
    sections_html = []
    for section in fr_sections:
        section_html = f'\n            <h2>{section["h2"]}</h2>'
        
        for content in section['content']:
            if content['type'] == 'p':
                section_html += f'\n            <p>{content["text"]}</p>'
            elif content['type'] == 'ul':
                section_html += '\n            <ul>'
                for item in content['items']:
                    section_html += f'\n                {item}'
                section_html += '\n            </ul>'
            elif content['type'] == 'checklist':
                section_html += '\n            <div class="checklist">'
                for item in content['items']:
                    section_html += f'\n                {item}'
                section_html += '\n            </div>'
            elif content['type'] == 'info-box':
                section_html += f'\n            <div class="info-box"><p>{content["text"]}</p></div>'
            elif content['type'] == 'warning-box':
                section_html += '\n            <div class="warning-box"><ul class="warning-list">'
                for item in content['items']:
                    section_html += f'\n                {item}'
                section_html += '\n            </ul></div>'
        
        sections_html.append(section_html)
    
    sections = '\n'.join(sections_html)
    
    html = html_template.format(
        lang_code=lang_code,
        theme=structure['theme'],
        title=fr_title,
        category=fr_category,
        read_time=fr_read_time,
        svg=structure['svg'],
        tldr_title=lang_config['tldr_title'],
        tldr_items=tldr_html,
        intro=fr_intro,
        sections=sections,
        back_text=lang_config['back_text']
    )
    
    return html

def sync_article(zh_file, lang_code, lang_config):
    """同步单篇文章"""
    
    # 读取中文原文
    zh_content = zh_file.read_text(encoding='utf-8')
    zh_soup = BeautifulSoup(zh_content, 'html.parser')
    
    # 提取结构
    structure = extract_zh_structure(zh_soup)
    
    # 生成目标语言HTML
    lang_html = generate_lang_html(structure, lang_code, lang_config)
    
    return lang_html

if __name__ == '__main__':
    print(f"🚀 完全同步系统启动")
    print(f"{'='*70}\n")
    print(f"⚠️  注意：此脚本需要集成真实的AI翻译API")
    print(f"   当前版本会生成标记，表示需要翻译的内容\n")
    print(f"💡 建议：先处理少量文章测试，确认流程后再批量处理")
    print(f"{'='*70}\n")
