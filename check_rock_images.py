#!/usr/bin/env python3
import os
import re

def check_image_exists(file_path):
    """检查文章中的图片路径是否存在"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找CSS背景图片路径
        bg_match = re.search(r"url\('([^']+)'\)", content)
        if bg_match:
            image_path = bg_match.group(1)
            # 转换相对路径为绝对路径
            if image_path.startswith('../../'):
                actual_path = image_path[6:]  # 移除 ../../
            else:
                actual_path = image_path
            
            exists = os.path.exists(actual_path)
            return {
                'found_path': image_path,
                'actual_path': actual_path,
                'exists': exists
            }
        
        return {'error': 'No image path found'}
        
    except Exception as e:
        return {'error': str(e)}

def main():
    """检查所有岩石文章的图片"""
    directories = [
        'en/rock-collecting',
        'en/rock-formation', 
        'en/rock-formation-types',
        'en/rock-identification',
        'en/rock-mineral-science'
    ]
    
    total_files = 0
    working_images = 0
    missing_images = []
    
    print("🔍 检查岩石文章头图显示情况:\n")
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"📁 {directory}:")
            html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
            
            for html_file in sorted(html_files):
                file_path = os.path.join(directory, html_file)
                total_files += 1
                
                result = check_image_exists(file_path)
                
                if 'error' in result:
                    print(f"  ❌ {html_file} - {result['error']}")
                    continue
                
                if result['exists']:
                    print(f"  ✅ {html_file} - 图片正常")
                    working_images += 1
                else:
                    print(f"  ❌ {html_file} - 图片缺失: {result['actual_path']}")
                    missing_images.append({
                        'file': file_path,
                        'missing_image': result['actual_path']
                    })
            print()
    
    print(f"📊 总结:")
    print(f"总文件数: {total_files}")
    print(f"图片正常: {working_images}")
    print(f"图片缺失: {len(missing_images)}")
    print(f"成功率: {working_images/total_files*100:.1f}%")
    
    if missing_images:
        print(f"\n❌ 缺失的图片:")
        for item in missing_images:
            print(f"  {item['file']} -> {item['missing_image']}")

if __name__ == "__main__":
    main()