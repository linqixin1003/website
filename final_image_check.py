#!/usr/bin/env python3
import os
import re
import urllib.parse

def check_image_accessibility(file_path):
    """检查文章中的图片是否可以访问"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS背景图片路径
        bg_match = re.search(r"url\('([^']+)'\)", content)
        if bg_match:
            url_path = bg_match.group(1)
            
            # 转换URL路径为文件系统路径
            if url_path.startswith('../../'):
                # 解码URL编码的字符
                decoded_path = urllib.parse.unquote(url_path[6:])
                file_system_path = decoded_path
                
                exists = os.path.exists(file_system_path)
                
                return {
                    'url_path': url_path,
                    'file_path': file_system_path,
                    'exists': exists
                }
        
        return {'error': 'No image path found'}
        
    except Exception as e:
        return {'error': str(e)}

def main():
    """最终检查所有岩石文章的图片可访问性"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    total_files = 0
    accessible_images = 0
    issues = []
    
    print("🔍 最终检查岩石文章头图可访问性:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"📁 {directory}:")
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in sorted(html_files):
                file_path = os.path.join(directory, html_file)
                total_files += 1
                
                result = check_image_accessibility(file_path)
                
                if 'error' in result:
                    print(f"  ❌ {html_file} - {result['error']}")
                    issues.append(f"{file_path}: {result['error']}")
                    continue
                
                if result['exists']:
                    print(f"  ✅ {html_file}")
                    accessible_images += 1
                else:
                    print(f"  ❌ {html_file} - 图片文件不存在: {result['file_path']}")
                    issues.append(f"{file_path}: 图片不存在 - {result['file_path']}")
            print()
    
    print(f"📊 最终结果:")
    print(f"总文件数: {total_files}")
    print(f"图片可访问: {accessible_images}")
    print(f"有问题的: {len(issues)}")
    print(f"成功率: {accessible_images/total_files*100:.1f}%")
    
    if issues:
        print(f"\n❌ 需要解决的问题:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print(f"\n🎉 所有岩石文章的头图都可以正常显示！")

if __name__ == "__main__":
    main()