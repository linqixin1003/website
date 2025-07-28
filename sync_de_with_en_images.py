#!/usr/bin/env python3
"""
同步德语文章头图与英语文章保持一致
"""

import os
import re

def extract_image_from_file(filepath):
    """从文件中提取头图编号"""
    if not os.path.exists(filepath):
        return None
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找CSS背景图片
    css_match = re.search(r'bird-image-(\d+(?:-alt-\d+)?)\.webp', content)
    if css_match:
        return css_match.group(1)
    
    return None

def update_de_image(de_filepath, en_image_num):
    """更新德语文件的头图编号"""
    if not os.path.exists(de_filepath) or not en_image_num:
        return False
        
    with open(de_filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    correct_path = f'../../images/birds/species/bird-image-{en_image_num}.webp'
    
    # 修复CSS背景图片
    content = re.sub(
        r'(background:[^;]*url\([\'"]?)../../images/birds/species/bird-image-\d+(?:-alt-\d+)?\.webp([\'"]?\))',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    # 修复HTML img标签
    content = re.sub(
        r'(src=[\'"])../../images/birds/species/bird-image-\d+(?:-alt-\d+)?\.webp([\'"])',
        rf'\g<1>{correct_path}\g<2>',
        content
    )
    
    with open(de_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def sync_directories():
    """同步德语和英语目录的头图"""
    categories = ['birdwatching', 'scientific-wonders', 'pet-care', 'ecology', 'knowledge']
    
    fixed_count = 0
    total_count = 0
    
    for category in categories:
        print(f"\n📁 同步类别: {category}")
        
        de_dir = f'de/{category}'
        en_dir = f'en/{category}'
        
        if not os.path.exists(de_dir) or not os.path.exists(en_dir):
            print(f"⚠️  目录不存在: {de_dir} 或 {en_dir}")
            continue
        
        # 获取所有HTML文件
        de_files = [f for f in os.listdir(de_dir) if f.endswith('.html')]
        en_files = [f for f in os.listdir(en_dir) if f.endswith('.html')]
        
        # 找到共同的文件
        common_files = set(de_files) & set(en_files)
        
        for filename in sorted(common_files):
            de_path = os.path.join(de_dir, filename)
            en_path = os.path.join(en_dir, filename)
            
            en_image = extract_image_from_file(en_path)
            
            if en_image:
                total_count += 1
                if update_de_image(de_path, en_image):
                    fixed_count += 1
                    print(f"  ✅ {filename}: 同步为 bird-image-{en_image}.webp")
                else:
                    print(f"  ❌ {filename}: 同步失败")
            else:
                print(f"  ⚠️  {filename}: 英语版没有头图，跳过")
    
    return fixed_count, total_count

def main():
    print("🔄 同步德语文章头图与英语版本...")
    
    fixed_count, total_count = sync_directories()
    
    print(f"\n📊 同步结果:")
    print(f"  ✅ 成功同步: {fixed_count} 个文件")
    print(f"  📝 总处理: {total_count} 个文件")
    
    if total_count > 0:
        success_rate = fixed_count / total_count * 100
        print(f"  🎯 成功率: {success_rate:.1f}%")
    
    return fixed_count == total_count

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 德语文章头图已与英语版本完全同步！")
    else:
        print("\n⚠️  部分文件同步失败，请检查。")