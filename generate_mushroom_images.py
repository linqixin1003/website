#!/usr/bin/env python3
"""
批量为蘑菇文章生成配图
使用 Pollinations.AI 免费 API
"""

import os
import requests
import time
from pathlib import Path
import urllib.parse

def read_article_content(file_path):
    """读取文章的标题和内容摘要"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 读取前1000个字符作为内容摘要
        lines = content.split('\n')
        
        # 提取标题（第一行）
        title = lines[0].lstrip('#').strip() if lines else ""
        
        # 提取正文内容（跳过空行和标题）
        text_content = []
        for line in lines[1:]:
            line = line.strip()
            # 跳过空行、markdown标题、和特殊符号开头的行
            if line and not line.startswith('#') and not line.startswith('**') and not line.startswith('-'):
                text_content.append(line)
            if len(' '.join(text_content)) > 500:  # 收集约500字符的内容
                break
        
        summary = ' '.join(text_content)[:500]  # 限制在500字符
        
        return title, summary
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None, None

def generate_image_prompt(title, summary, category):
    """根据文章标题、内容摘要和类别生成图片提示词"""
    # 添加蘑菇相关的视觉描述，让生成的图片更专业
    category_styles = {
        'culinary-mushrooms': 'professional food photography, gourmet cooking, fresh mushrooms, culinary preparation, kitchen setting, natural lighting',
        'mushroom-ecology': 'nature photography, forest ecosystem, mushrooms in natural habitat, wildlife, botanical illustration, scientific documentation',
        'mushroom-identification': 'field guide style, detailed mushroom specimen, identification features, close-up photography, educational illustration',
        'mushroom-safety': 'warning illustration, safety guide, informative graphic, educational poster, clear visual communication',
        'mushroom-science': 'scientific illustration, microscopy, research, laboratory, mycology study, academic style'
    }
    
    base_style = category_styles.get(category, 'professional mushroom photography')
    
    # 从摘要中提取关键概念（取前150字符）
    content_keywords = summary[:150] if summary else title
    
    # 组合提示词：内容关键词 + 标题 + 类别风格 + 通用质量要求
    prompt = f"{content_keywords}, {title}, {base_style}, high quality, detailed, professional photography, 4K resolution, unique perspective"
    
    return prompt

def download_image(prompt, save_path, max_retries=3):
    """从 Pollinations.AI 下载图片"""
    # URL 编码提示词
    encoded_prompt = urllib.parse.quote(prompt)
    
    # Pollinations.AI API 端点
    # 添加参数：width=1024&height=768 可以指定尺寸
    api_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=800&nologo=true"
    
    for attempt in range(max_retries):
        try:
            print(f"  🎨 生成中... (尝试 {attempt + 1}/{max_retries})")
            response = requests.get(api_url, timeout=60)
            
            if response.status_code == 200:
                # 确保目录存在
                save_path.parent.mkdir(parents=True, exist_ok=True)
                
                # 保存图片
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                
                print(f"  ✅ 成功保存: {save_path}")
                return True
            else:
                print(f"  ⚠️ HTTP {response.status_code}, 重试中...")
                time.sleep(2)
                
        except Exception as e:
            print(f"  ⚠️ 错误: {e}, 重试中...")
            time.sleep(2)
    
    print(f"  ❌ 失败: 已达到最大重试次数")
    return False

def main():
    # 基础路径
    base_dir = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom")
    en_dir = base_dir / "en"
    
    # 类别列表
    categories = [
        'culinary-mushrooms',
        'mushroom-ecology',
        'mushroom-identification',
        'mushroom-safety',
        'mushroom-science'
    ]
    
    total_files = 0
    success_count = 0
    failed_files = []
    
    print("🍄 开始批量生成蘑菇文章配图...")
    print(f"📁 源目录: {en_dir}")
    print("=" * 80)
    
    # 遍历所有类别
    for category in categories:
        category_dir = en_dir / category
        
        if not category_dir.exists():
            print(f"⚠️ 目录不存在: {category_dir}")
            continue
        
        print(f"\n📂 处理类别: {category}")
        print("-" * 80)
        
        # 获取该类别下所有 .txt 文件
        txt_files = sorted(category_dir.glob("*.txt"))
        
        for txt_file in txt_files:
            total_files += 1
            
            # 读取标题和内容摘要
            title, summary = read_article_content(txt_file)
            if not title:
                failed_files.append(str(txt_file))
                continue
            
            # 生成提示词
            prompt = generate_image_prompt(title, summary, category)
            
            # 确定保存路径：同名但扩展名为 .jpg
            image_filename = txt_file.stem + ".jpg"
            save_path = category_dir / image_filename
            
            # 如果图片已存在，跳过
            if save_path.exists():
                print(f"⏭️  [{total_files}/55] 已存在，跳过: {txt_file.name}")
                success_count += 1
                continue
            
            print(f"\n📄 [{total_files}/55] 处理: {txt_file.name}")
            print(f"  📝 标题: {title[:60]}...")
            print(f"  📋 内容: {summary[:60]}...")
            print(f"  🎯 提示词: {prompt[:100]}...")
            
            # 下载图片
            if download_image(prompt, save_path):
                success_count += 1
            else:
                failed_files.append(str(txt_file))
            
            # 避免请求过快，稍微延迟
            time.sleep(1)
    
    # 总结
    print("\n" + "=" * 80)
    print("🎉 处理完成！")
    print(f"✅ 成功: {success_count}/{total_files}")
    print(f"❌ 失败: {len(failed_files)}/{total_files}")
    
    if failed_files:
        print("\n失败的文件列表:")
        for f in failed_files:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
