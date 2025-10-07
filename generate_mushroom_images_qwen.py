#!/usr/bin/env python3
"""
使用阿里云通义千问 qwen-image-plus 模型为蘑菇文章生成配图
"""

import os
import requests
import time
import json
from pathlib import Path

# 配置
API_KEY = "sk-2969688c18494729b792af05b64ffbad"
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "X-DashScope-Async": "enable"  # 使用异步模式
}

def read_article_content(file_path):
    """读取文章的标题和内容摘要"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
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
            if len(' '.join(text_content)) > 300:  # 收集约300字符的内容
                break
        
        summary = ' '.join(text_content)[:300]
        
        return title, summary
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None, None

def generate_image_prompt(title, summary, category):
    """根据文章标题、内容摘要和类别生成图片提示词（美式写实风格）"""
    
    # 美式写实摄影风格描述
    category_descriptions = {
        'culinary-mushrooms': 'Authentic food photography, fresh wild mushrooms on rustic wooden cutting board, natural daylight from window, professional kitchen setting, clean and minimalist composition, shot with Canon 5D, realistic texture, no filters, documentary style',
        
        'mushroom-ecology': 'Nature documentary photography, real mushrooms growing in American forest floor, natural lighting, Pacific Northwest woodland, authentic wilderness, National Geographic style, photojournalism, realistic forest environment, no digital manipulation',
        
        'mushroom-identification': 'Field guide photography, real mushroom specimens in natural habitat, educational reference photo, clean white background or natural forest floor, authentic scientific documentation, precise detail, natural colors, professional macro lens',
        
        'mushroom-safety': 'Documentary educational photography, real mushrooms in natural setting, clear instructional image, authentic warning visual, realistic and honest depiction, public health campaign style, no dramatization',
        
        'mushroom-science': 'Scientific photography, authentic laboratory or field research setting, real mycology study, documentary realism, natural academic style, research journal quality, honest scientific documentation'
    }
    
    base_desc = category_descriptions.get(category, 'authentic documentary photography of real mushrooms')
    
    # 提取文章核心主题词
    core_concept = title.split(':')[0] if ':' in title else title[:50]
    
    # 组合提示词 - 强调真实、自然、无AI感
    prompt = f"Photorealistic documentary photograph: {core_concept}. {base_desc}. Shot on professional camera, natural lighting, authentic and realistic, no AI artifacts, no over-saturation, honest representation, American photography aesthetic, clean composition, real world scene."
    
    # 限制提示词长度
    if len(prompt) > 500:
        prompt = prompt[:500]
    
    return prompt

def generate_image(prompt, save_path, max_retries=3):
    """调用阿里云通义千问API生成图片"""
    
    # 构建请求数据
    data = {
        "model": "wanx-v1",  # 通义万相模型
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": "1024*1024",
            "n": 1
        }
    }
    
    for attempt in range(max_retries):
        try:
            print(f"  🎨 生成中... (尝试 {attempt + 1}/{max_retries})")
            
            # 发送请求
            response = requests.post(API_URL, json=data, headers=HEADERS, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                
                # 检查响应
                if 'output' in result and 'task_id' in result['output']:
                    task_id = result['output']['task_id']
                    print(f"  ⏳ 任务ID: {task_id}, 等待生成...")
                    
                    # 轮询获取结果
                    image_url = wait_for_task(task_id)
                    
                    if image_url:
                        # 下载图片
                        if download_image(image_url, save_path):
                            return True
                    else:
                        print(f"  ⚠️ 任务失败，重试中...")
                        time.sleep(2)
                        
                elif 'output' in result and 'results' in result['output']:
                    # 同步模式直接返回结果
                    results = result['output']['results']
                    if results and len(results) > 0:
                        image_url = results[0].get('url')
                        if image_url and download_image(image_url, save_path):
                            return True
                else:
                    print(f"  ⚠️ API 返回异常: {result}")
                    time.sleep(2)
            else:
                print(f"  ⚠️ HTTP {response.status_code}: {response.text}")
                time.sleep(2)
                
        except Exception as e:
            print(f"  ⚠️ 错误: {e}")
            time.sleep(2)
    
    print(f"  ❌ 失败: 已达到最大重试次数")
    return False

def wait_for_task(task_id, max_wait=120):
    """轮询获取异步任务结果"""
    query_url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        try:
            response = requests.get(query_url, headers=HEADERS, timeout=30)
            if response.status_code == 200:
                result = response.json()
                
                if 'output' in result:
                    task_status = result['output'].get('task_status', '')
                    
                    if task_status == 'SUCCEEDED':
                        results = result['output'].get('results', [])
                        if results and len(results) > 0:
                            return results[0].get('url')
                    elif task_status in ['FAILED', 'UNKNOWN']:
                        print(f"  ❌ 任务失败: {task_status}")
                        return None
                    else:
                        # 任务还在进行中
                        time.sleep(3)
                        continue
            else:
                print(f"  ⚠️ 查询任务失败: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"  ⚠️ 查询任务出错: {e}")
            return None
    
    print(f"  ⏰ 任务超时")
    return None

def download_image(image_url, save_path):
    """从URL下载图片"""
    try:
        response = requests.get(image_url, timeout=60)
        if response.status_code == 200:
            # 确保目录存在
            save_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 直接保存图片二进制数据
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print(f"  ✅ 成功保存: {save_path}")
            return True
        else:
            print(f"  ❌ 下载失败: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  ❌ 下载出错: {e}")
        return False

def main():
    # 基础路径
    base_dir = Path("/Users/infno/Documents/work-code/bird-web/website/mushroom")
    en_dir = base_dir / "en"
    
    # 创建统一的图片目录
    images_dir = base_dir / "images"
    images_dir.mkdir(exist_ok=True)
    
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
    
    print("🍄 开始使用通义千问生成蘑菇文章配图...")
    print(f"📁 源目录: {en_dir}")
    print(f"🖼️  图片目录: {images_dir}")
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
            
            # 确定保存路径：category_编号.jpg
            image_filename = f"{category}_{txt_file.stem}.jpg"
            save_path = images_dir / image_filename
            
            # 如果图片已存在，跳过
            if save_path.exists():
                print(f"⏭️  [{total_files}/55] 已存在，跳过: {txt_file.name}")
                success_count += 1
                continue
            
            print(f"\n📄 [{total_files}/55] 处理: {txt_file.name}")
            print(f"  📝 标题: {title[:60]}...")
            print(f"  🎯 提示词: {prompt[:100]}...")
            
            # 生成图片
            if generate_image(prompt, save_path):
                success_count += 1
            else:
                failed_files.append(str(txt_file))
            
            # API限制：每秒2次请求，适当延迟
            time.sleep(3)
    
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
