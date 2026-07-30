#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
校验 mushroom 文章页重构结果。

对每个页面比对 git HEAD 版本与当前版本的正文纯文本，确认批量改写没有丢内容，
同时检查资源引用、lang 属性、必需的结构元素。

用法:
    python3 audit_mushroom_restyle.py [--lang en] [--verbose]
"""

import argparse
import html
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MUSHROOM_DIR = os.path.join(ROOT, 'mushroom')

LANGS = ['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'ru', 'zh']
CATEGORIES = [
    'culinary-mushrooms', 'mushroom-ecology', 'mushroom-identification',
    'mushroom-safety', 'mushroom-science',
]

RE_TAGS = re.compile(r'<[^>]+>')
RE_STYLE = re.compile(r'<style.*?</style>', re.S | re.I)
RE_SCRIPT = re.compile(r'<script.*?</script>', re.S | re.I)
RE_HEAD = re.compile(r'<head.*?</head>', re.S | re.I)
RE_WS = re.compile(r'\s+')

RE_BLOCK_END = re.compile(
    r'</(p|div|li|h[1-6]|ul|ol|main|header|footer|section|blockquote|tr)>', re.I)
RE_BREAK = re.compile(r'<(br|hr)\s*/?>', re.I)
RE_EMOJI = re.compile(r'[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u2190-\u21FF]')

# 模板文案改造前后本就不同，比对时剔除整段
TEMPLATE_NOISE = re.compile(
    r'(Professional Mycology Guide|\d+\s*(?:minute|min)\s*read|'
    r'Beginner|Intermediate|Advanced|Critical|'
    r'Culinary Mushrooms|Mushroom Ecology|Mushroom Safety|Mushroom Science|'
    r'Identification)', re.I)


def content_blocks(raw):
    """按块级元素切出可见文本，避免跨元素拼接造成的误判。"""
    body = re.search(r'<body[^>]*>(.*)</body>', raw, re.S | re.I)
    text = body.group(1) if body else RE_HEAD.sub('', raw)

    text = RE_STYLE.sub('', text)
    text = RE_SCRIPT.sub('', text)
    # 原文存在未转义的 "<"，先补齐再比对，否则原文会被当成标签吞掉
    text = re.sub(r'<(?![a-zA-Z/!])', '&lt;', text)
    # 改造新增的外壳元素不参与比对
    text = re.sub(r'<div[^>]*class="[^"]*\bm-loader\b.*?</div>\s*</div>', '', text, flags=re.S | re.I)
    text = re.sub(r'<header[^>]*class="[^"]*\bm-topbar\b.*?</header>', '', text, flags=re.S | re.I)
    text = re.sub(r'<footer[^>]*class="[^"]*\bm-footer\b.*?</footer>', '', text, flags=re.S | re.I)
    text = re.sub(r'<button[^>]*class="[^"]*\bm-totop\b.*?</button>', '', text, flags=re.S | re.I)
    text = re.sub(r'<a[^>]*class="[^"]*\bm-hero-back\b.*?</a>', '', text, flags=re.S | re.I)
    text = re.sub(r'<noscript>.*?</noscript>', '', text, flags=re.S | re.I)

    text = RE_BLOCK_END.sub('\n', text)
    text = RE_BREAK.sub('\n', text)
    text = html.unescape(RE_TAGS.sub('', text))
    text = TEMPLATE_NOISE.sub('', text)
    text = RE_EMOJI.sub('', text)

    blocks = []
    for line in text.split('\n'):
        # 列表化会去掉行首的 "1." / "- " 前缀，比对前统一抹掉。
        # bullet 后必须有空格，否则 "-80°C" 这类负数会被误伤。
        line = re.sub(r'^\s*(?:\d{1,2}\s*[.、)]\s+|[-•*]\s+)', '', line)
        line = RE_WS.sub(' ', line).strip()
        if line:
            blocks.append(line)
    return blocks


def visible_text(raw):
    return ' '.join(content_blocks(raw))


def git_show(rel_path):
    try:
        return subprocess.check_output(
            ['git', 'show', 'HEAD:' + rel_path],
            cwd=ROOT, stderr=subprocess.DEVNULL).decode('utf-8')
    except subprocess.CalledProcessError:
        return None


def audit(path, rel_path, lang, category, verbose=False):
    issues = []

    with open(path, 'r', encoding='utf-8') as fh:
        now = fh.read()

    # --- 结构检查 -------------------------------------------------------
    checks = [
        ('lang 属性', '<html lang="{}">'.format(lang)),
        ('样式表', 'href="../../assets/article.css"'),
        ('脚本', 'src="../../assets/article.js"'),
        ('loading 遮罩', 'class="m-loader"'),
        ('阅读进度', 'class="m-progress"'),
        ('顶栏', 'class="m-topbar"'),
        ('分类主题', 'data-category="{}"'.format(category)),
        ('内容容器', '<main class="content">'),
    ]
    for name, needle in checks:
        if needle not in now:
            issues.append('缺少{}'.format(name))

    # --- 残留的坏引用 ---------------------------------------------------
    for bad in ('../../mobile-styles.css', '../../mobile-enhancement.css',
                '../../ecology-theme.css'):
        if bad in now:
            issues.append('残留坏链 {}'.format(bad))

    # --- hero 图存在性 --------------------------------------------------
    hero = re.search(r"background-image:\s*url\('([^']+)'\)", now)
    if not hero:
        issues.append('缺少 hero 背景图')
    else:
        img_path = os.path.normpath(os.path.join(os.path.dirname(path), hero.group(1)))
        if not os.path.isfile(img_path):
            issues.append('hero 图不存在: {}'.format(hero.group(1)))

    # --- 标签闭合 -------------------------------------------------------
    for tag in ('div', 'main', 'ul', 'ol', 'li'):
        opens = len(re.findall(r'<{}\b'.format(tag), now, re.I))
        closes = len(re.findall(r'</{}>'.format(tag), now, re.I))
        if opens != closes:
            issues.append('{} 标签不配对（{} 开 / {} 闭）'.format(tag, opens, closes))

    # --- 正文完整性 -----------------------------------------------------
    before = git_show(rel_path)
    if before is None:
        issues.append('无法读取 HEAD 版本')
    else:
        old_blocks = content_blocks(before)
        new_blocks = content_blocks(now)
        new_joined = ' '.join(new_blocks)

        old_len = sum(len(b) for b in old_blocks)
        new_len = sum(len(b) for b in new_blocks)

        if old_len:
            ratio = new_len / old_len
            if ratio < 0.98:
                issues.append('正文疑似丢失：{} → {} 字符（{:.1%}）'.format(
                    old_len, new_len, ratio))
            elif verbose and ratio > 1.02:
                issues.append('正文变长：{} → {} 字符'.format(old_len, new_len))

        # 逐块核对：原文每个实义段落都应在新页面中保留
        missing = [b for b in old_blocks if len(b) > 12 and b not in new_joined]
        if missing:
            issues.append('{} 个段落在新页面中找不到，例如：{}'.format(
                len(missing), missing[0][:70]))

    return issues


def main():
    parser = argparse.ArgumentParser(description='校验 mushroom 重构结果')
    parser.add_argument('--lang', help='只检查指定语言')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    langs = [args.lang] if args.lang else LANGS
    total = clean = 0
    failures = []

    for lang in langs:
        for category in CATEGORIES:
            folder = os.path.join(MUSHROOM_DIR, lang, category)
            if not os.path.isdir(folder):
                continue

            for name in sorted(os.listdir(folder)):
                if not name.endswith('.html'):
                    continue

                path = os.path.join(folder, name)
                rel = os.path.relpath(path, ROOT)
                total += 1

                issues = audit(path, rel, lang, category, args.verbose)
                if issues:
                    failures.append((rel, issues))
                else:
                    clean += 1

    print('检查 {} 个页面：{} 个通过，{} 个有问题'.format(total, clean, len(failures)))

    for rel, issues in failures[:25]:
        print('\n  {}'.format(rel))
        for issue in issues:
            print('    - {}'.format(issue))

    if len(failures) > 25:
        print('\n  … 另有 {} 个页面存在问题'.format(len(failures) - 25))

    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
