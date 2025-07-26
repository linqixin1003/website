#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 从之前读取的 HTML 内容中提取的样式部分
test_content = """
        .hero-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/bird-image-001.png') center/cover;
            position: relative;
            margin-top: 0;
        }
"""

def test_patterns():
    patterns = [
        r'background:\s*linear-gradient\([^)]+\),\s*\n?\s*url\([\'"]?([^\'")]+)[\'"]?\)',
        r'background:\s*linear-gradient\([^)]+\),\s*url\([\'"]?([^\'")]+)[\'"]?\)',
        r'url\([\'"]?([^\'")]+)[\'"]?\)',
        r'background:[^;]*url\([\'"]?([^\'")]+)[\'"]?\)',
    ]
    
    for i, pattern in enumerate(patterns, 1):
        print(f"Pattern {i}: {pattern}")
        match = re.search(pattern, test_content, re.MULTILINE | re.DOTALL)
        if match:
            print(f"  ✓ Match found: {match.group(1)}")
        else:
            print(f"  ✗ No match")
        print()

if __name__ == "__main__":
    test_patterns()