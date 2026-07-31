#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 mushroom/en 文章页的内容质量问题：
  1. 句号后缺空格（enjoyment.In → enjoyment. In）
  2. 残留 markdown 粗体（**text** → <strong>text</strong>）
  3. 英文正文中混入的中文词
  4. 根据正文刷新 meta / og:description

用法:
    python3 fix_en_mushroom_content.py [--dry-run]
"""

import argparse
import glob
import html
import os
import re
import sys

from restyle_mushroom_articles import build_description, strip_tags

ROOT = os.path.dirname(os.path.abspath(__file__))

RE_HEAD_TITLE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
RE_META_DESC = re.compile(r'<meta name="description" content="([^"]*)"', re.I)
RE_OG_DESC = re.compile(r'<meta property="og:description" content="([^"]*)"', re.I)

# 中文残留 → 正确英文（按长度降序匹配，避免短词抢先）
ZH_FIXES = [
    ('已经开始腐烂、无法辨认的', 'already rotting and unidentifiable'),
    ('配合温湿度计配合', 'with a thermo-hygrometer and'),
    ('深入研究', 'deeply study'),
    ('人工辅助', 'artificially assisted'),
    ('各自的', 'their own'),
    ('分流', 'route'),
    ('公认', 'recognized'),
    ('反而', 'instead'),
    ('盲目', 'blind'),
    ('偏离', 'deviating from'),
    ('功能', ' capability'),
    ('配合', 'matching'),
    ('技巧', ' tip'),
    ('赋予', 'gives'),
    ('体质', 'constitution'),
]

ABBR_GUARD = re.compile(
    r'(?:Ph|Dr|Mr|Mrs|Ms|Jr|Sr|vs|etc|e\.g|i\.e|U\.S|U\.K|Fig|Vol|No|'
    r'approx|Inc|Ltd|Co|Prof|Gen|Corp|al|St|Ave|Rd)\.$',
    re.I,
)

RE_STUCK_PERIOD = re.compile(r'([a-z])\.([A-Z])')
RE_MD_BOLD = re.compile(r'\*\*([^*\n]+?)\*\*')


def page_title(raw):
    match = RE_HEAD_TITLE.search(raw)
    if not match:
        return ''
    title = strip_tags(match.group(1))
    return re.sub(r'\s*-\s*MushroomAiSnap\s*$', '', title).strip()


def sync_meta_descriptions(raw, body_html, fallback_title):
    """用正文首段生成 description，写回 meta 与 og:description。"""
    desc = build_description(body_html, fallback_title)
    esc = html.escape(desc, quote=True)

    updated = raw
    updated, n1 = RE_META_DESC.subn(
        '<meta name="description" content="{}"'.format(esc), updated, count=1)
    updated, n2 = RE_OG_DESC.subn(
        '<meta property="og:description" content="{}"'.format(esc), updated, count=1)

    if n1 == 0 or n2 == 0:
        return raw, False
    return updated, updated != raw


def fix_stuck_periods(text):
    parts = re.split(r'(<[^>]+>)', text)
    out = []
    for part in parts:
        if part.startswith('<'):
            out.append(part)
            continue

        def repl(m):
            left = part[max(0, m.start() - 12):m.start() + 1]
            if ABBR_GUARD.search(left):
                return m.group(0)
            if re.search(r'\b[A-Z]\.$', left):
                return m.group(0)
            return '{}. {}'.format(m.group(1), m.group(2))

        out.append(RE_STUCK_PERIOD.sub(repl, part))
    return ''.join(out)


def fix_markdown_bold(text):
    parts = re.split(r'(<[^>]+>)', text)
    out = []
    for part in parts:
        if part.startswith('<'):
            out.append(part)
        else:
            out.append(RE_MD_BOLD.sub(r'<strong>\1</strong>', part))
    return ''.join(out)


def fix_chinese(text):
    for zh, en in ZH_FIXES:
        if zh in text:
            text = text.replace(zh, en)
    return re.sub(r' {2,}', ' ', text)


def process(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as fh:
        raw = fh.read()

    body_match = re.search(r'(<main class="content">)(.*)(</main>)', raw, re.S)
    if not body_match:
        return False, 'no main'

    before = body_match.group(2)
    after = fix_stuck_periods(fix_markdown_bold(fix_chinese(before)))

    title = page_title(raw)
    new_raw = raw[:body_match.start(2)] + after + raw[body_match.end(2):]
    new_raw, meta_changed = sync_meta_descriptions(new_raw, after, title)

    if new_raw == raw:
        return False, 'unchanged'

    stats = {
        'body': before != after,
        'meta': meta_changed,
        'zh': sum(1 for zh, _ in ZH_FIXES if zh in before),
        'md': len(RE_MD_BOLD.findall(before)),
        'period': len(RE_STUCK_PERIOD.findall(before)),
    }

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_raw)

    return True, stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(ROOT, 'mushroom/en/*/*.html')))
    changed = skipped = 0
    totals = {'body': 0, 'meta': 0, 'zh': 0, 'md': 0, 'period': 0}

    for path in files:
        ok, info = process(path, args.dry_run)
        if ok:
            changed += 1
            if isinstance(info, dict):
                for k in totals:
                    if k in ('body', 'meta'):
                        totals[k] += 1 if info.get(k) else 0
                    else:
                        totals[k] += info.get(k, 0)
        else:
            skipped += 1

    print('EN 内容修复：改写 {} 个，跳过 {} 个{}'.format(
        changed, skipped, '（演练）' if args.dry_run else ''))
    print('  正文: {}  meta: {}  中文: {}  markdown: {}  句号: {}'.format(
        totals['body'], totals['meta'], totals['zh'], totals['md'], totals['period']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
