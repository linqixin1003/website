#!/usr/bin/env python3
import os
import re

def count_rock_articles():
    """统计正式的岩石文章数量（只包含编号文章）"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    total_articles = 0
    articles_by_series = {}
    
    print("📊 统计正式的岩石文章（编号文章）:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            # 只统计编号文章 (01-xxx.html 到 10-xxx.html)
            html_files = [f for f in os.listdir(directory) 
                         if f.endswith('.html') and re.match(r'^\d{2}-.*\.html$', f)]
            
            series_name = directory.split('/')[-1]
            articles_by_series[series_name] = len(html_files)
            total_articles += len(html_files)
            
            print(f"📁 {directory}: {len(html_files)} 篇")
            for html_file in sorted(html_files):
                print(f"  - {html_file}")
            print()
    
    print(f"📊 总结:")
    for series, count in articles_by_series.items():
        print(f"  {series}: {count} 篇")
    print(f"\n🎯 总计: {total_articles} 篇正式文章")
    
    # 检查是否有非编号文章
    print(f"\n🔍 检查非编号文章:")
    for directory in directories:
        if os.path.exists(directory):
            all_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            numbered_files = [f for f in all_files if re.match(r'^\d{2}-.*\.html$', f)]
            other_files = [f for f in all_files if f not in numbered_files]
            
            if other_files:
                print(f"  {directory}: {other_files}")

if __name__ == "__main__":
    count_rock_articles()