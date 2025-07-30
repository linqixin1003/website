#!/usr/bin/env python3
"""
德语翻译质量全面检查脚本
验证所有修复是否完成
"""
import os
import re
from bs4 import BeautifulSoup

def check_german_errors(content, filename):
    """检查德语翻译错误"""
    errors = []
    
    # 1. 检查常见的德语语法错误
    grammar_errors = [
        (r'\bsterben\b', "错误使用'sterben'作为定冠词"),
        (r'\bder/sterben/das\b', "错误的德语定冠词格式"),
        (r'\bjener/jene/jenes\b', "应该使用'diese'而不是'jener/jene/jenes'"),
    ]
    
    for pattern, description in grammar_errors:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"语法错误: {description} - 找到{len(matches)}处")
    
    # 2. 检查HTML标签错误
    html_errors = [
        (r'<stark>', "错误的HTML标签'stark'，应该是'strong'"),
        (r'</stark>', "错误的HTML结束标签'stark'"),
    ]
    
    for pattern, description in html_errors:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"HTML错误: {description} - 找到{len(matches)}处")
    
    # 3. 检查CSS类名错误
    css_errors = [
        (r'equipment-Beschreibung', "错误的CSS类名，应该是'equipment-description'"),
        (r'haupt-text', "错误的CSS类名，应该是'main-text'"),
    ]
    
    for pattern, description in css_errors:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"CSS错误: {description} - 找到{len(matches)}处")
    
    # 4. 检查中文内容残留
    chinese_patterns = [
        (r'[观鸟指南]', "中文：观鸟指南"),
        (r'[知识库]', "中文：知识库"),
        (r'[科学奇观]', "中文：科学奇观"),
        (r'[生态学]', "中文：生态学"),
        (r'[宠物护理]', "中文：宠物护理"),
        (r'[\u4e00-\u9fff]+', "其他中文字符"),
    ]
    
    for pattern, description in chinese_patterns:
        matches = re.findall(pattern, content)
        if matches:
            errors.append(f"中文残留: {description} - 找到{len(matches)}处: {matches[:3]}")
    
    # 5. 检查英德混合错误
    mixed_errors = [
        (r'\bist\s+usually\b', "英德混合：'ist usually'"),
        (r'\bist\s+minimal\b', "英德混合：'ist minimal'"),
        (r'\bwhen\s+Sie\b', "英德混合：'when Sie'"),
        (r'\bas\s+these\s+sind\b', "英德混合：'as these sind'"),
        (r'\bas\s+they\s+sind\b', "英德混合：'as they sind'"),
        (r'\bmore\s+wichtig\s+than\b', "英德混合：'more wichtig than'"),
        (r'\bif\s+Sie\b', "英德混合：'if Sie'"),
        (r'\bto\s+improve\b', "英德混合：'to improve'"),
        (r'\bpeak\s+activity\s+times\b', "英德混合：'peak activity times'"),
        (r'\bin\s+most\s+Gebiete\b', "英德混合：'in most Gebiete'"),
        (r'\bfor\s+discovery\s+und\s+wonder\b', "英德混合：'for discovery und wonder'"),
    ]
    
    for pattern, description in mixed_errors:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            errors.append(f"英德混合: {description} - 找到{len(matches)}处")
    
    return errors

def check_content_quality(content, filename):
    """检查内容质量"""
    quality_issues = []
    
    try:
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查标题语言
        title = soup.find('title')
        if title and title.text:
            if re.search(r'[\u4e00-\u9fff]', title.text):
                quality_issues.append("标题包含中文字符")
        
        # 检查meta信息
        lang_attr = soup.find('html', {'lang': True})
        if lang_attr and lang_attr.get('lang') != 'de':
            quality_issues.append(f"HTML lang属性不正确: {lang_attr.get('lang')}")
        
        # 检查主要内容是否为德语
        main_content = soup.get_text()
        chinese_count = len(re.findall(r'[\u4e00-\u9fff]', main_content))
        if chinese_count > 5:  # 允许少量中文字符（可能在注释中）
            quality_issues.append(f"内容包含过多中文字符: {chinese_count}个")
        
        # 检查是否有合理的德语内容
        german_indicators = ['der', 'die', 'das', 'und', 'oder', 'für', 'von', 'zu', 'mit']
        german_count = sum(len(re.findall(r'\b' + word + r'\b', main_content, re.IGNORECASE)) for word in german_indicators)
        
        if german_count < 10:
            quality_issues.append("德语特征词汇过少，可能不是德语内容")
            
    except Exception as e:
        quality_issues.append(f"解析HTML时出错: {e}")
    
    return quality_issues

def analyze_file(file_path):
    """分析单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查翻译错误
        translation_errors = check_german_errors(content, file_path)
        
        # 检查内容质量
        quality_issues = check_content_quality(content, file_path)
        
        return {
            'file': file_path,
            'translation_errors': translation_errors,
            'quality_issues': quality_issues,
            'total_issues': len(translation_errors) + len(quality_issues)
        }
        
    except Exception as e:
        return {
            'file': file_path,
            'translation_errors': [f"文件读取错误: {e}"],
            'quality_issues': [],
            'total_issues': 1
        }

def main():
    """主函数"""
    print("🔍 开始德语翻译质量全面检查...")
    print("=" * 60)
    
    # 德语文件目录
    german_dirs = [
        'de/birdwatching',
        'de/knowledge', 
        'de/ecology',
        'de/pet-care',
        'de/scientific-wonders'
    ]
    
    all_results = []
    total_files = 0
    problematic_files = 0
    
    for dir_path in german_dirs:
        if os.path.exists(dir_path):
            print(f"\n📁 检查目录: {dir_path}")
            
            for filename in os.listdir(dir_path):
                if filename.endswith('.html') and not '.backup' in filename:
                    file_path = os.path.join(dir_path, filename)
                    total_files += 1
                    
                    result = analyze_file(file_path)
                    all_results.append(result)
                    
                    if result['total_issues'] > 0:
                        problematic_files += 1
                        print(f"❌ {filename}: {result['total_issues']} 个问题")
                        
                        for error in result['translation_errors']:
                            print(f"   🔸 翻译错误: {error}")
                        
                        for issue in result['quality_issues']:
                            print(f"   🔸 质量问题: {issue}")
                    else:
                        print(f"✅ {filename}: 无问题")
    
    # 生成总结报告
    print("\n" + "=" * 60)
    print("📊 检查总结报告")
    print("=" * 60)
    print(f"📁 检查目录数: {len(german_dirs)}")
    print(f"📄 检查文件数: {total_files}")
    print(f"❌ 有问题文件: {problematic_files}")
    print(f"✅ 无问题文件: {total_files - problematic_files}")
    print(f"🎯 质量评分: {((total_files - problematic_files) / total_files * 100):.1f}%")
    
    # 统计各类问题
    translation_error_count = sum(len(r['translation_errors']) for r in all_results)
    quality_issue_count = sum(len(r['quality_issues']) for r in all_results)
    
    print(f"\n🔸 翻译错误总数: {translation_error_count}")
    print(f"🔸 质量问题总数: {quality_issue_count}")
    print(f"🔸 总问题数: {translation_error_count + quality_issue_count}")
    
    if problematic_files == 0:
        print("\n🎉 恭喜！所有德语文件都已通过质量检查！")
        print("✨ 德语翻译质量达到发布标准")
    else:
        print(f"\n⚠️  还有 {problematic_files} 个文件需要进一步修复")
        
        # 显示最需要关注的文件
        problematic_results = [r for r in all_results if r['total_issues'] > 0]
        problematic_results.sort(key=lambda x: x['total_issues'], reverse=True)
        
        print("\n🔧 最需要关注的文件:")
        for i, result in enumerate(problematic_results[:5]):
            print(f"{i+1}. {result['file']}: {result['total_issues']} 个问题")

if __name__ == "__main__":
    main() 