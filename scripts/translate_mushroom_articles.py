#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
蘑菇文章翻译脚本
使用 Deepseek API 将中文文章翻译为其他语言
"""

import os
import json
import time
from pathlib import Path
from typing import Optional
import requests

# ==================== 配置区 ====================

# API配置（可以通过环境变量设置）
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')  # 从环境变量读取
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# 翻译配置
SOURCE_LANG = "zh"  # 源语言：简体中文
TARGET_LANG = "en"  # 目标语言：英文
SOURCE_DIR = Path("mushroom/zh")
TARGET_DIR = Path("mushroom/en")

# API参数
MODEL = "deepseek-chat"
TEMPERATURE = 0.3  # 较低的温度保证翻译质量和一致性
MAX_TOKENS = 4000

# 重试配置
MAX_RETRIES = 3
RETRY_DELAY = 2  # 秒

# ==================== 辅助函数 ====================

def check_api_key():
    """检查API密钥是否配置"""
    if not DEEPSEEK_API_KEY:
        print("❌ 错误：未配置 DEEPSEEK_API_KEY")
        print("\n请使用以下方式之一配置API密钥：")
        print("1. 设置环境变量：")
        print("   Windows PowerShell: $env:DEEPSEEK_API_KEY='your-api-key'")
        print("   Linux/Mac: export DEEPSEEK_API_KEY='your-api-key'")
        print("\n2. 或者直接修改脚本中的 DEEPSEEK_API_KEY 变量（不推荐）")
        return False
    return True


def translate_text(text: str, retry_count: int = 0) -> Optional[str]:
    """
    调用Deepseek API翻译文本
    
    Args:
        text: 要翻译的文本
        retry_count: 当前重试次数
        
    Returns:
        翻译后的文本，失败返回None
    """
    if not text.strip():
        return text
    
    # 构建翻译提示词
    system_prompt = f"""你是一个专业的真菌学和科普翻译专家。请将以下中文文章翻译成英文。

翻译要求：
1. 保持专业术语的准确性（真菌学、生物学术语）
2. 保持原文的结构和格式
3. 语言流畅自然，符合英语表达习惯
4. 保留中文中的要点和关键信息
5. 标题、小节标题等也要翻译
6. 不要添加任何解释或注释，只返回翻译结果"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"请翻译以下内容：\n\n{text}"}
    ]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }
    
    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers=headers,
            json=data,
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            translated_text = result['choices'][0]['message']['content']
            return translated_text
        else:
            error_msg = f"API返回错误 {response.status_code}: {response.text}"
            print(f"   ⚠️  {error_msg}")
            
            # 如果还有重试次数，尝试重试
            if retry_count < MAX_RETRIES:
                print(f"   🔄 {RETRY_DELAY}秒后重试... (第{retry_count + 1}次重试)")
                time.sleep(RETRY_DELAY)
                return translate_text(text, retry_count + 1)
            return None
            
    except Exception as e:
        print(f"   ❌ 请求异常: {str(e)}")
        
        # 如果还有重试次数，尝试重试
        if retry_count < MAX_RETRIES:
            print(f"   🔄 {RETRY_DELAY}秒后重试... (第{retry_count + 1}次重试)")
            time.sleep(RETRY_DELAY)
            return translate_text(text, retry_count + 1)
        return None


def get_all_source_files():
    """获取所有需要翻译的源文件"""
    if not SOURCE_DIR.exists():
        print(f"❌ 源目录不存在: {SOURCE_DIR}")
        return []
    
    txt_files = list(SOURCE_DIR.rglob("*.txt"))
    print(f"📁 找到 {len(txt_files)} 个文件待翻译")
    return sorted(txt_files)


def get_target_file_path(source_file: Path) -> Path:
    """根据源文件路径生成目标文件路径"""
    relative_path = source_file.relative_to(SOURCE_DIR)
    target_file = TARGET_DIR / relative_path
    return target_file


def translate_file(source_file: Path):
    """翻译单个文件"""
    target_file = get_target_file_path(source_file)
    
    # 检查目标文件是否已存在
    if target_file.exists():
        print(f"   ⏭️  已存在，跳过")
        return True
    
    # 读取源文件
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            source_text = f.read()
    except Exception as e:
        print(f"   ❌ 读取失败: {str(e)}")
        return False
    
    if not source_text.strip():
        print(f"   ⚠️  文件为空，跳过")
        return True
    
    # 翻译
    print(f"   🔄 翻译中... ({len(source_text)} 字符)")
    translated_text = translate_text(source_text)
    
    if translated_text is None:
        print(f"   ❌ 翻译失败")
        return False
    
    # 创建目标目录
    target_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 保存翻译结果
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        print(f"   ✅ 翻译完成 -> {target_file}")
        return True
    except Exception as e:
        print(f"   ❌ 保存失败: {str(e)}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("🍄 蘑菇文章翻译脚本 (Deepseek API)")
    print("=" * 60)
    print()
    
    # 检查API密钥
    if not check_api_key():
        return
    
    print(f"📖 源语言: {SOURCE_LANG}")
    print(f"🌍 目标语言: {TARGET_LANG}")
    print(f"📂 源目录: {SOURCE_DIR}")
    print(f"📂 目标目录: {TARGET_DIR}")
    print(f"🤖 模型: {MODEL}")
    print()
    
    # 获取所有文件
    source_files = get_all_source_files()
    if not source_files:
        return
    
    # 统计信息
    total = len(source_files)
    success = 0
    skipped = 0
    failed = 0
    
    # 翻译每个文件
    print("开始翻译...\n")
    for i, source_file in enumerate(source_files, 1):
        relative_path = source_file.relative_to(SOURCE_DIR)
        print(f"[{i}/{total}] {relative_path}")
        
        target_file = get_target_file_path(source_file)
        if target_file.exists():
            skipped += 1
            print(f"   ⏭️  已存在，跳过\n")
            continue
        
        result = translate_file(source_file)
        
        if result:
            success += 1
        else:
            failed += 1
        
        # 避免API限流，每个文件之间暂停
        if i < total:
            time.sleep(1)
        
        print()
    
    # 输出统计
    print("=" * 60)
    print("📊 翻译完成统计：")
    print(f"   ✅ 成功: {success}")
    print(f"   ⏭️  跳过: {skipped}")
    print(f"   ❌ 失败: {failed}")
    print(f"   📝 总计: {total}")
    print("=" * 60)


if __name__ == "__main__":
    main()

