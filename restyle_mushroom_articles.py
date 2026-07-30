#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量重构 mushroom/{lang}/{category}/*.html 文章页。

做四件事：
  1. 修正失效的样式表引用（原为 ../../ 指向不存在的 mushroom/*.css），改用统一的
     mushroom/assets/article.css + article.js
  2. 套用新的版式模板：hero、上浮内容卡、顶栏、阅读进度、回到顶部、页脚
  3. 注入 loading 遮罩与骨架屏
  4. 修正 <html lang> 并把元信息标签（分类 / 阅读时长 / 难度）本地化

正文 DOM 原样保留，只重排外壳，因此可重复执行。

用法:
    python3 restyle_mushroom_articles.py [--dry-run] [--lang zh] [--limit 5]
"""

import argparse
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MUSHROOM_DIR = os.path.join(ROOT, 'mushroom')

LANGS = ['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
CATEGORIES = [
    'culinary-mushrooms',
    'mushroom-ecology',
    'mushroom-identification',
    'mushroom-safety',
    'mushroom-science',
]

# 主题色，与 assets/article.css 中的 data-category 主题保持一致
THEME_COLOR = {
    'culinary-mushrooms': '#a0522d',
    'mushroom-ecology': '#2d6a4f',
    'mushroom-identification': '#2b6cb0',
    'mushroom-safety': '#c0392b',
    'mushroom-science': '#6b46c1',
}

CATEGORY_EMOJI = {
    'culinary-mushrooms': '🍳',
    'mushroom-ecology': '🌿',
    'mushroom-identification': '🔍',
    'mushroom-safety': '⚠️',
    'mushroom-science': '🔬',
}

DIFFICULTY_EMOJI = {
    'Beginner': '🟢',
    'Intermediate': '🟡',
    'Advanced': '🟠',
    'Critical': '🔴',
}

# 全站 550 页共用同一句英文副标题，按语言替换
KICKER_SOURCE = 'Professional Mycology Guide'
KICKER = {
    'en': 'Professional Mycology Guide',
    'zh': '专业真菌学指南',
    'ja': '専門家による菌類ガイド',
    'ko': '전문 균학 가이드',
    'de': 'Professioneller Mykologie-Leitfaden',
    'fr': 'Guide de mycologie professionnel',
    'es': 'Guía profesional de micología',
    'it': 'Guida professionale di micologia',
    'pt': 'Guia profissional de micologia',
    'ru': 'Профессиональное руководство по микологии',
}

# --------------------------------------------------------------------------
# 本地化文案
# --------------------------------------------------------------------------
UI = {
    'en': {
        'loading': 'Loading article…', 'back': 'Back', 'share': 'Share',
        'totop': 'Back to top', 'cta': 'Explore MushroomAiSnap',
        'note': 'For education only. Never eat a wild mushroom without expert confirmation.',
        'read': '{n} min read',
        'cat': {
            'culinary-mushrooms': 'Culinary Mushrooms', 'mushroom-ecology': 'Mushroom Ecology',
            'mushroom-identification': 'Identification', 'mushroom-safety': 'Mushroom Safety',
            'mushroom-science': 'Mushroom Science',
        },
        'diff': {'Beginner': 'Beginner', 'Intermediate': 'Intermediate',
                 'Advanced': 'Advanced', 'Critical': 'Critical'},
    },
    'zh': {
        'loading': '正在加载文章…', 'back': '返回', 'share': '分享',
        'totop': '回到顶部', 'cta': '了解 MushroomAiSnap',
        'note': '本文仅供学习参考。未经专家确认，切勿食用任何野生蘑菇。',
        'read': '{n} 分钟阅读',
        'cat': {
            'culinary-mushrooms': '蘑菇烹饪', 'mushroom-ecology': '蘑菇生态',
            'mushroom-identification': '蘑菇鉴定', 'mushroom-safety': '安全指南',
            'mushroom-science': '真菌科学',
        },
        'diff': {'Beginner': '入门', 'Intermediate': '进阶',
                 'Advanced': '高阶', 'Critical': '重要'},
    },
    'ja': {
        'loading': '記事を読み込み中…', 'back': '戻る', 'share': '共有',
        'totop': 'トップへ', 'cta': 'MushroomAiSnap を見る',
        'note': '本記事は教育目的のみ。専門家の確認なしに野生キノコを食べないでください。',
        'read': '{n} 分で読めます',
        'cat': {
            'culinary-mushrooms': 'キノコ料理', 'mushroom-ecology': 'キノコ生態',
            'mushroom-identification': 'キノコ同定', 'mushroom-safety': '安全ガイド',
            'mushroom-science': '菌類科学',
        },
        'diff': {'Beginner': '初級', 'Intermediate': '中級',
                 'Advanced': '上級', 'Critical': '重要'},
    },
    'ko': {
        'loading': '기사를 불러오는 중…', 'back': '뒤로', 'share': '공유',
        'totop': '맨 위로', 'cta': 'MushroomAiSnap 알아보기',
        'note': '교육 목적으로만 제공됩니다. 전문가 확인 없이 야생 버섯을 섭취하지 마세요.',
        'read': '{n}분 소요',
        'cat': {
            'culinary-mushrooms': '버섯 요리', 'mushroom-ecology': '버섯 생태',
            'mushroom-identification': '버섯 식별', 'mushroom-safety': '안전 가이드',
            'mushroom-science': '균류 과학',
        },
        'diff': {'Beginner': '입문', 'Intermediate': '중급',
                 'Advanced': '고급', 'Critical': '중요'},
    },
    'de': {
        'loading': 'Artikel wird geladen…', 'back': 'Zurück', 'share': 'Teilen',
        'totop': 'Nach oben', 'cta': 'MushroomAiSnap entdecken',
        'note': 'Nur zu Bildungszwecken. Essen Sie nie Wildpilze ohne fachliche Bestätigung.',
        'read': '{n} Min. Lesezeit',
        'cat': {
            'culinary-mushrooms': 'Pilzküche', 'mushroom-ecology': 'Pilzökologie',
            'mushroom-identification': 'Bestimmung', 'mushroom-safety': 'Pilzsicherheit',
            'mushroom-science': 'Pilzwissenschaft',
        },
        'diff': {'Beginner': 'Einsteiger', 'Intermediate': 'Fortgeschritten',
                 'Advanced': 'Experte', 'Critical': 'Kritisch'},
    },
    'fr': {
        'loading': 'Chargement de l’article…', 'back': 'Retour', 'share': 'Partager',
        'totop': 'Haut de page', 'cta': 'Découvrir MushroomAiSnap',
        'note': 'À but éducatif uniquement. Ne consommez jamais un champignon sauvage sans avis d’expert.',
        'read': '{n} min de lecture',
        'cat': {
            'culinary-mushrooms': 'Cuisine des champignons', 'mushroom-ecology': 'Écologie fongique',
            'mushroom-identification': 'Identification', 'mushroom-safety': 'Sécurité',
            'mushroom-science': 'Science fongique',
        },
        'diff': {'Beginner': 'Débutant', 'Intermediate': 'Intermédiaire',
                 'Advanced': 'Avancé', 'Critical': 'Critique'},
    },
    'es': {
        'loading': 'Cargando artículo…', 'back': 'Volver', 'share': 'Compartir',
        'totop': 'Ir arriba', 'cta': 'Descubre MushroomAiSnap',
        'note': 'Solo con fines educativos. Nunca comas setas silvestres sin confirmación de un experto.',
        'read': '{n} min de lectura',
        'cat': {
            'culinary-mushrooms': 'Cocina con setas', 'mushroom-ecology': 'Ecología fúngica',
            'mushroom-identification': 'Identificación', 'mushroom-safety': 'Seguridad',
            'mushroom-science': 'Ciencia fúngica',
        },
        'diff': {'Beginner': 'Principiante', 'Intermediate': 'Intermedio',
                 'Advanced': 'Avanzado', 'Critical': 'Crítico'},
    },
    'it': {
        'loading': 'Caricamento articolo…', 'back': 'Indietro', 'share': 'Condividi',
        'totop': 'Torna su', 'cta': 'Scopri MushroomAiSnap',
        'note': 'Solo a scopo educativo. Non mangiare mai funghi selvatici senza conferma di un esperto.',
        'read': '{n} min di lettura',
        'cat': {
            'culinary-mushrooms': 'Cucina con i funghi', 'mushroom-ecology': 'Ecologia fungina',
            'mushroom-identification': 'Identificazione', 'mushroom-safety': 'Sicurezza',
            'mushroom-science': 'Scienza fungina',
        },
        'diff': {'Beginner': 'Principiante', 'Intermediate': 'Intermedio',
                 'Advanced': 'Avanzato', 'Critical': 'Critico'},
    },
    'pt': {
        'loading': 'Carregando artigo…', 'back': 'Voltar', 'share': 'Partilhar',
        'totop': 'Ir para o topo', 'cta': 'Conheça o MushroomAiSnap',
        'note': 'Apenas para fins educativos. Nunca coma cogumelos silvestres sem confirmação de um especialista.',
        'read': '{n} min de leitura',
        'cat': {
            'culinary-mushrooms': 'Cozinha com cogumelos', 'mushroom-ecology': 'Ecologia fúngica',
            'mushroom-identification': 'Identificação', 'mushroom-safety': 'Segurança',
            'mushroom-science': 'Ciência fúngica',
        },
        'diff': {'Beginner': 'Iniciante', 'Intermediate': 'Intermédio',
                 'Advanced': 'Avançado', 'Critical': 'Crítico'},
    },
    'ru': {
        'loading': 'Загрузка статьи…', 'back': 'Назад', 'share': 'Поделиться',
        'totop': 'Наверх', 'cta': 'Узнать о MushroomAiSnap',
        'note': 'Только в образовательных целях. Никогда не ешьте дикие грибы без подтверждения эксперта.',
        'read': '{n} мин чтения',
        'cat': {
            'culinary-mushrooms': 'Кулинария', 'mushroom-ecology': 'Экология грибов',
            'mushroom-identification': 'Определение', 'mushroom-safety': 'Безопасность',
            'mushroom-science': 'Наука о грибах',
        },
        'diff': {'Beginner': 'Начальный', 'Intermediate': 'Средний',
                 'Advanced': 'Продвинутый', 'Critical': 'Критично'},
    },
}

# --------------------------------------------------------------------------
# 解析
# --------------------------------------------------------------------------
RE_TITLE = re.compile(r'<h1[^>]*class="[^"]*\btitle\b[^"]*"[^>]*>(.*?)</h1>', re.S | re.I)
RE_HEAD_TITLE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
RE_QUOTE = re.compile(r'<div[^>]*class="[^"]*\bquote-text\b[^"]*"[^>]*>(.*?)</div>', re.S | re.I)
RE_META_BLOCK = re.compile(r'<div[^>]*class="[^"]*\barticle-meta\b[^"]*"[^>]*>.*?</div>', re.S | re.I)
RE_READ_MIN = re.compile(r'class="read-time"[^>]*>[^<0-9]*(\d+)', re.I)
RE_DIFFICULTY = re.compile(r'class="difficulty"[^>]*>\s*(?:[^\w\s<]+\s*)?([A-Za-z]+)', re.I)
RE_BODY = re.compile(r'<body[^>]*>(.*)</body>', re.S | re.I)
RE_TAGS = re.compile(r'<[^>]+>')


def strip_tags(text):
    return html.unescape(RE_TAGS.sub('', text)).strip()


def extract_article_body(raw):
    """取出正文：article-meta 之后、</body> 之前，剥离多余的收尾标签。"""
    body_match = RE_BODY.search(raw)
    inner = body_match.group(1) if body_match else raw

    meta_match = RE_META_BLOCK.search(inner)
    if meta_match:
        inner = inner[meta_match.end():]
    else:
        # 没有 article-meta 时退回到标题之后
        title_match = RE_TITLE.search(inner)
        if title_match:
            inner = inner[title_match.end():]

    # 去掉本脚本上一次生成的外壳元素
    inner = re.sub(r'<footer[^>]*class="[^"]*\bm-footer\b.*?</footer>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'<button[^>]*class="[^"]*\bm-totop\b.*?</button>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'<script.*?</script>', '', inner, flags=re.S | re.I)
    inner = re.sub(r'</main>', '', inner, flags=re.I)

    # 正文里未转义的 "<"（如 "快速冲洗（<30秒）"）会被浏览器当成标签，
    # 把后面的内容一并吞掉，必须转义
    inner = re.sub(r'<(?![a-zA-Z/!])', '&lt;', inner)

    # 内容分隔符与排版残留
    inner = re.sub(r'<p>\s*-{3,}\s*</p>', '', inner)
    inner = re.sub(r'<p>\s*</p>', '', inner)
    inner = re.sub(r'^(?:\s*<br\s*/?>)+', '', inner.strip(), flags=re.I)
    inner = re.sub(r'(?:<br\s*/?>\s*)+$', '', inner.strip(), flags=re.I)

    # 剥离尾部多余的 </div>（原文件 content 容器被重复闭合）
    opens = len(re.findall(r'<div\b', inner, re.I))
    closes = len(re.findall(r'</div>', inner, re.I))
    extra = closes - opens
    while extra > 0:
        stripped = re.sub(r'</div>\s*$', '', inner.rstrip(), count=1)
        if stripped == inner.rstrip():
            break
        inner = stripped
        extra -= 1

    return normalize_lists(inner.strip())


# 保留 <p> 之后的前导空格，缩进决定列表层级
RE_LINE_P = re.compile(r'^\s*<p(?:\s[^>]*)?>(.*?)</p>\s*$', re.S | re.I)
RE_ORDERED = re.compile(r'^(\d{1,2})\s*[.、)]\s+(.+)$', re.S)
RE_BULLET = re.compile(r'^[-•*]\s+(.+)$', re.S)


def normalize_lists(body):
    """原始内容里的列表被写成了普通段落（"1. xxx" / "  - xxx"），还原为 ol/ul。

    带缩进的 "- xxx" 紧跟在有序项之后时，作为该项的子列表。
    """
    out = []
    block = []          # [(kind, indent, content, number, raw_line)]

    def flush():
        if not block:
            return

        # 单独一项不构成列表，原样保留
        if len(block) < 2:
            out.append(block[0][4])
            block.clear()
            return

        top_kind = block[0][0]
        items = []      # [(content, [children])]

        for kind, indent, content, _num, _raw in block:
            if indent > 0 and items and top_kind == 'ol':
                items[-1][1].append(content)
            else:
                items.append((content, []))

        pieces = []
        for content, children in items:
            if children:
                nested = ''.join('<li>{}</li>'.format(c) for c in children)
                pieces.append('<li>{}<ul>{}</ul></li>'.format(content, nested))
            else:
                pieces.append('<li>{}</li>'.format(content))

        if top_kind == 'ol':
            start = block[0][3] or 1
            attr = ' start="{}"'.format(start) if start != 1 else ''
            out.append('<ol class="m-steps"{}>{}</ol>'.format(attr, ''.join(pieces)))
        else:
            out.append('<ul class="m-points">{}</ul>'.format(''.join(pieces)))

        block.clear()

    for line in body.split('\n'):
        match = RE_LINE_P.match(line)
        item = None

        if match:
            inner_raw = match.group(1)
            indent = len(inner_raw) - len(inner_raw.lstrip())
            inner = inner_raw.strip()

            ordered = RE_ORDERED.match(inner)
            bullet = RE_BULLET.match(inner)

            if ordered:
                item = ('ol', indent, ordered.group(2).strip(), int(ordered.group(1)), line)
            elif bullet:
                item = ('ul', indent, bullet.group(1).strip(), None, line)

        if item:
            # 顶层类型切换时先收尾，避免 ol/ul 混在同一个列表里
            if block and item[0] != block[0][0] and item[1] == 0:
                flush()
            block.append(item)
        else:
            flush()
            out.append(line)

    flush()
    return '\n'.join(out)


def build_description(body_html, fallback):
    """从正文首个实义段落生成 meta description。"""
    for pattern in (r'<div[^>]*class="[^"]*\bmain-text\b[^"]*"[^>]*>(.*?)</div>',
                    r'<p[^>]*class="[^"]*\barticle-text\b[^"]*"[^>]*>(.*?)</p>',
                    r'<p[^>]*>(.*?)</p>'):
        match = re.search(pattern, body_html, re.S | re.I)
        if match:
            text = strip_tags(match.group(1))
            if len(text) > 40:
                return text[:155].rstrip() + ('…' if len(text) > 155 else '')
    return fallback


def render(lang, category, slug, title, quote, minutes, difficulty, body_html):
    ui = UI.get(lang, UI['en'])
    theme = THEME_COLOR[category]
    hero = '../../images/{}_{}.webp'.format(category, slug)

    esc_title = html.escape(title, quote=True)
    description = build_description(body_html, title)
    esc_desc = html.escape(description, quote=True)

    cat_label = '{} {}'.format(CATEGORY_EMOJI[category], ui['cat'][category])
    read_label = '⏱ ' + ui['read'].format(n=minutes) if minutes else ''
    diff_label = ''
    if difficulty:
        diff_label = '{} {}'.format(
            DIFFICULTY_EMOJI.get(difficulty, '🟢'),
            ui['diff'].get(difficulty, difficulty),
        )

    meta_items = ['<span class="category">{}</span>'.format(html.escape(cat_label))]
    if read_label:
        meta_items.append('<span class="read-time">{}</span>'.format(html.escape(read_label)))
    if diff_label:
        meta_items.append('<span class="difficulty">{}</span>'.format(html.escape(diff_label)))
    meta_html = '\n'.join(meta_items)

    quote_html = ''
    if quote:
        quote_html = (
            '<div class="quote-box m-reveal">\n'
            '<p class="quote-text">{}</p>\n'
            '</div>\n'
        ).format(html.escape(quote))

    return TEMPLATE.format(
        lang=lang,
        category=category,
        theme=theme,
        hero=hero,
        title=esc_title,
        description=esc_desc,
        quote_block=quote_html,
        meta=meta_html,
        body=body_html,
        loading=html.escape(ui['loading']),
        back=html.escape(ui['back']),
        share=html.escape(ui['share']),
        totop=html.escape(ui['totop']),
        cta=html.escape(ui['cta']),
        note=html.escape(ui['note']),
    )


TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
<meta name="theme-color" content="{theme}"/>
<title>{title} - MushroomAiSnap</title>
<meta name="description" content="{description}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:image" content="{hero}"/>
<link rel="icon" type="image/svg+xml" href="../../../favicon.svg"/>
<link rel="preload" as="image" href="{hero}"/>
<link rel="stylesheet" href="../../assets/article.css"/>
<style>
.hero-image {{
    background-image: url('{hero}');
}}
</style>
</head>
<body class="is-loading" data-category="{category}">

<div class="m-loader" id="m-loader" role="status" aria-live="polite">
<div class="m-loader__mark">
<span class="m-loader__ring"></span>
<span class="m-loader__cap">🍄</span>
</div>
<p class="m-loader__text">{loading}</p>
<div class="m-loader__skeleton" aria-hidden="true">
<span class="m-loader__bar"></span>
<span class="m-loader__bar"></span>
<span class="m-loader__bar"></span>
<span class="m-loader__bar"></span>
</div>
</div>
<noscript><style>.m-loader{{display:none!important}}body.is-loading{{overflow:auto!important}}.m-reveal{{opacity:1!important;transform:none!important}}</style></noscript>

<div class="m-progress" aria-hidden="true"><div class="m-progress__fill"></div></div>

<header class="m-topbar">
<a class="m-topbar__back" href="../../../mushroom-app.html" aria-label="{back}">←</a>
<span class="m-topbar__title">{title}</span>
<button class="m-topbar__share" type="button" aria-label="{share}">↗</button>
</header>

<div class="hero-image">
<a class="m-hero-back" href="../../../mushroom-app.html">← {back}</a>
</div>

<main class="content">
<h1 class="title m-reveal">{title}</h1>
{quote_block}<div class="article-meta m-reveal">
{meta}
</div>

{body}
</main>

<footer class="m-footer">
<a class="m-footer__cta" href="../../../mushroom-app.html">🍄 {cta}</a>
<p class="m-footer__note">{note}</p>
</footer>

<button class="m-totop" type="button" aria-label="{totop}">↑</button>

<script src="../../assets/article.js"></script>
</body>
</html>
'''


def process(path, lang, category, dry_run=False):
    slug = os.path.splitext(os.path.basename(path))[0]

    with open(path, 'r', encoding='utf-8') as fh:
        raw = fh.read()

    title_match = RE_TITLE.search(raw)
    if title_match:
        title = strip_tags(title_match.group(1))
    else:
        head_match = RE_HEAD_TITLE.search(raw)
        title = strip_tags(head_match.group(1)) if head_match else slug
    title = re.sub(r'\s*-\s*MushroomAiSnap\s*$', '', title).strip()

    quote_match = RE_QUOTE.search(raw)
    quote = strip_tags(quote_match.group(1)) if quote_match else ''
    # 已本地化过的页面用 <p class="quote-text">，兼容读取
    if not quote:
        alt = re.search(r'<p[^>]*class="[^"]*\bquote-text\b[^"]*"[^>]*>(.*?)</p>', raw, re.S | re.I)
        quote = strip_tags(alt.group(1)) if alt else ''

    # 通用副标题按语言替换（重复执行时也能命中已翻译的版本）
    if quote == KICKER_SOURCE or quote in KICKER.values():
        quote = KICKER.get(lang, KICKER['en'])

    read_match = RE_READ_MIN.search(raw)
    minutes = read_match.group(1) if read_match else ''

    diff_match = RE_DIFFICULTY.search(raw)
    difficulty = ''
    if diff_match:
        found = diff_match.group(1).strip().capitalize()
        if found in DIFFICULTY_EMOJI:
            difficulty = found
    if not difficulty:
        # 已本地化的页面回读原文难度失败时，保留分类默认值
        difficulty = 'Critical' if category == 'mushroom-safety' else 'Intermediate'

    body_html = extract_article_body(raw)
    if not body_html:
        return False, 'empty body'

    output = render(lang, category, slug, title, quote, minutes, difficulty, body_html)

    if output == raw:
        return False, 'unchanged'

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(output)

    return True, 'ok'


def main():
    parser = argparse.ArgumentParser(description='批量重构 mushroom 文章页')
    parser.add_argument('--dry-run', action='store_true', help='只演练，不写文件')
    parser.add_argument('--lang', help='只处理指定语言')
    parser.add_argument('--category', help='只处理指定分类')
    parser.add_argument('--limit', type=int, help='最多处理的文件数')
    args = parser.parse_args()

    langs = [args.lang] if args.lang else LANGS
    cats = [args.category] if args.category else CATEGORIES

    changed = skipped = failed = 0
    problems = []

    for lang in langs:
        for category in cats:
            folder = os.path.join(MUSHROOM_DIR, lang, category)
            if not os.path.isdir(folder):
                continue

            for name in sorted(os.listdir(folder)):
                if not name.endswith('.html'):
                    continue
                if args.limit and changed + skipped >= args.limit:
                    break

                path = os.path.join(folder, name)
                try:
                    ok, reason = process(path, lang, category, args.dry_run)
                except Exception as exc:                      # noqa: BLE001
                    failed += 1
                    problems.append('{}: {}'.format(path, exc))
                    continue

                if ok:
                    changed += 1
                else:
                    skipped += 1
                    if reason != 'unchanged':
                        problems.append('{}: {}'.format(path, reason))

    print('已重构 {} 个页面，跳过 {} 个，失败 {} 个{}'.format(
        changed, skipped, failed, '（演练模式）' if args.dry_run else ''))

    for item in problems[:20]:
        print('  ! ' + item)

    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
