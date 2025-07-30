#!/usr/bin/env python3
"""
专家级德语翻译质量审核脚本
基于英语版本进行深度专业翻译质量检查
重点关注手机端显示适配
"""
import os
import re
from bs4 import BeautifulSoup
import difflib

class GermanTranslationAuditor:
    def __init__(self):
        # 专业鸟类学术语德英对照词典
        self.ornithology_terms = {
            'birdwatching': 'Vogelbeobachtung',
            'ornithology': 'Ornithologie', 
            'ornithological': 'ornithologisch',
            'avian': 'Vogel-',
            'species': 'Arten',
            'migration': 'Wanderung',
            'breeding': 'Brut',
            'habitat': 'Lebensraum',
            'ecosystem': 'Ökosystem',
            'biodiversity': 'Biodiversität',
            'conservation': 'Naturschutz',
            'ecology': 'Ökologie',
            'binoculars': 'Fernglas',
            'field guide': 'Feldführer',
            'bird identification': 'Vogelbestimmung',
            'plumage': 'Gefieder',
            'molt': 'Mauser',
            'territorial': 'territorial',
            'courtship': 'Balz',
            'nesting': 'Nistung',
            'fledgling': 'Jungvogel',
            'molt pattern': 'Mausermuster',
            'wing chord': 'Flügellänge',
            'tarsus': 'Lauf',
            'bill': 'Schnabel',
            'cloaca': 'Kloake',
            'syrinx': 'Syrinx',
        }
        
        # 移动端优化检查点
        self.mobile_optimization_checks = [
            'viewport meta tag',
            'responsive design',
            'touch-friendly navigation',
            'readable font sizes',
            'appropriate line spacing',
            'mobile-friendly images'
        ]

    def extract_text_content(self, html_content):
        """提取HTML中的主要文本内容"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 移除script和style标签
            for script in soup(["script", "style"]):
                script.decompose()
            
            # 提取主要内容区域
            main_content = soup.find('main') or soup.find('div', class_='content') or soup.find('body')
            
            if main_content:
                return main_content.get_text(separator=' ', strip=True)
            return soup.get_text(separator=' ', strip=True)
        except Exception as e:
            return f"解析错误: {e}"

    def check_professional_terminology(self, german_text, english_text, filename):
        """检查专业术语翻译质量"""
        issues = []
        
        # 检查关键术语是否正确翻译
        for en_term, de_term in self.ornithology_terms.items():
            if en_term.lower() in english_text.lower():
                # 检查德语版本是否包含相应的德语术语
                if de_term.lower() not in german_text.lower():
                    # 检查是否使用了其他可接受的翻译
                    alternatives = self.get_alternative_translations(en_term)
                    found_alternative = any(alt.lower() in german_text.lower() for alt in alternatives)
                    
                    if not found_alternative:
                        issues.append(f"术语翻译缺失: '{en_term}' 应翻译为 '{de_term}' 或其同义词")
        
        return issues

    def get_alternative_translations(self, english_term):
        """获取英语术语的可接受德语替代翻译"""
        alternatives = {
            'birdwatching': ['Vogelkunde', 'Birding'],
            'habitat': ['Biotop', 'Lebensbereich'],
            'species': ['Spezies', 'Art'],
            'migration': ['Zug', 'Migration'],
            'conservation': ['Erhaltung', 'Schutz'],
        }
        return alternatives.get(english_term, [])

    def check_mobile_optimization(self, html_content, filename):
        """检查移动端优化"""
        issues = []
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 检查viewport meta标签
            viewport = soup.find('meta', {'name': 'viewport'})
            if not viewport:
                issues.append("缺少viewport meta标签，影响移动端显示")
            elif 'width=device-width' not in viewport.get('content', ''):
                issues.append("viewport设置不正确，应包含width=device-width")
            
            # 检查响应式CSS
            has_responsive_css = False
            for style_tag in soup.find_all('style'):
                if '@media' in style_tag.text:
                    has_responsive_css = True
                    break
            
            if not has_responsive_css:
                # 检查外部CSS文件引用
                css_links = soup.find_all('link', {'rel': 'stylesheet'})
                mobile_css = any('mobile' in link.get('href', '') for link in css_links)
                if not mobile_css:
                    issues.append("缺少移动端响应式CSS")
            
            # 检查图片是否有合适的属性
            images = soup.find_all('img')
            for img in images:
                if not img.get('alt'):
                    issues.append("图片缺少alt属性，影响移动端可访问性")
                
                # 检查图片是否使用了响应式属性
                style = img.get('style', '')
                if 'max-width' not in style and 'width: 100%' not in style:
                    css_classes = img.get('class', [])
                    if not any('responsive' in cls or 'img-fluid' in cls for cls in css_classes):
                        issues.append("图片可能不是响应式的，影响移动端显示")
            
            # 检查字体大小是否适合移动端
            style_tags = soup.find_all('style')
            for style in style_tags:
                style_text = style.text
                if 'font-size' in style_text:
                    # 检查是否有过小的字体
                    font_sizes = re.findall(r'font-size:\s*(\d+(?:\.\d+)?)px', style_text)
                    for size in font_sizes:
                        if float(size) < 14:
                            issues.append(f"字体大小 {size}px 可能在移动端过小（建议 ≥14px）")
            
        except Exception as e:
            issues.append(f"移动端检查时出错: {e}")
        
        return issues

    def check_translation_completeness(self, german_text, english_text, filename):
        """检查翻译完整性"""
        issues = []
        
        # 简单的内容长度比较（德语通常比英语长15-25%）
        en_length = len(english_text.split())
        de_length = len(german_text.split())
        
        if de_length < en_length * 0.8:
            issues.append(f"德语内容可能不完整（德语:{de_length}词 vs 英语:{en_length}词）")
        elif de_length > en_length * 1.5:
            issues.append(f"德语内容可能过长（德语:{de_length}词 vs 英语:{en_length}词）")
        
        # 检查是否有英语残留
        english_words = ['the', 'and', 'or', 'but', 'with', 'from', 'that', 'this', 'when', 'where', 'how', 'what', 'why']
        found_english = []
        for word in english_words:
            if re.search(r'\b' + word + r'\b', german_text, re.IGNORECASE):
                found_english.append(word)
        
        if found_english:
            issues.append(f"发现英语残留: {', '.join(found_english)}")
        
        return issues

    def check_professional_style(self, german_text, filename):
        """检查专业写作风格"""
        issues = []
        
        # 检查是否使用了适当的专业术语
        professional_indicators = [
            'wissenschaftlich', 'Forschung', 'Studien', 'Beobachtung', 
            'Methode', 'Analyse', 'Verhalten', 'Ökologie'
        ]
        
        found_indicators = sum(1 for indicator in professional_indicators 
                             if indicator in german_text)
        
        if found_indicators < 2:
            issues.append("专业术语使用不足，可能影响学术权威性")
        
        # 检查句子结构复杂性（德语学术文本特点）
        sentences = re.split(r'[.!?]', german_text)
        long_sentences = [s for s in sentences if len(s.split()) > 25]
        
        if len(long_sentences) < len(sentences) * 0.1:
            issues.append("缺少复杂句式，可能不符合德语学术写作风格")
        
        return issues

    def audit_file_pair(self, german_file, english_file):
        """审核德英文件对"""
        results = {
            'filename': german_file,
            'terminology_issues': [],
            'mobile_issues': [], 
            'completeness_issues': [],
            'style_issues': [],
            'overall_score': 0
        }
        
        try:
            # 读取文件内容
            with open(german_file, 'r', encoding='utf-8') as f:
                german_content = f.read()
            
            with open(english_file, 'r', encoding='utf-8') as f:
                english_content = f.read()
            
            # 提取文本内容
            german_text = self.extract_text_content(german_content)
            english_text = self.extract_text_content(english_content)
            
            # 进行各项检查
            results['terminology_issues'] = self.check_professional_terminology(
                german_text, english_text, german_file)
            
            results['mobile_issues'] = self.check_mobile_optimization(
                german_content, german_file)
            
            results['completeness_issues'] = self.check_translation_completeness(
                german_text, english_text, german_file)
            
            results['style_issues'] = self.check_professional_style(
                german_text, german_file)
            
            # 计算总体评分
            total_issues = (len(results['terminology_issues']) + 
                          len(results['mobile_issues']) + 
                          len(results['completeness_issues']) + 
                          len(results['style_issues']))
            
            # 评分系统：100 - (问题数 * 5)，最低0分
            results['overall_score'] = max(0, 100 - (total_issues * 5))
            
        except Exception as e:
            results['terminology_issues'] = [f"文件读取错误: {e}"]
            results['overall_score'] = 0
        
        return results

def main():
    """主函数"""
    print("🔬 开始专家级德语翻译质量审核...")
    print("专注于专业术语、移动端适配和翻译质量")
    print("=" * 70)
    
    auditor = GermanTranslationAuditor()
    
    # 德语和英语文件目录映射
    categories = ['birdwatching', 'knowledge', 'ecology', 'pet-care', 'scientific-wonders']
    
    all_results = []
    total_files = 0
    excellent_files = 0  # 95分以上
    good_files = 0       # 85-94分
    needs_improvement = 0 # 85分以下
    
    for category in categories:
        german_dir = f'de/{category}'
        english_dir = f'en/{category}'
        
        if os.path.exists(german_dir) and os.path.exists(english_dir):
            print(f"\n📁 审核类别: {category}")
            print("-" * 50)
            
            # 获取德语文件列表
            german_files = [f for f in os.listdir(german_dir) 
                          if f.endswith('.html') and '.backup' not in f]
            
            for german_filename in sorted(german_files):
                german_path = os.path.join(german_dir, german_filename)
                english_path = os.path.join(english_dir, german_filename)
                
                if os.path.exists(english_path):
                    total_files += 1
                    result = auditor.audit_file_pair(german_path, english_path)
                    all_results.append(result)
                    
                    # 分类统计
                    score = result['overall_score']
                    if score >= 95:
                        excellent_files += 1
                        status = "🌟 优秀"
                    elif score >= 85:
                        good_files += 1
                        status = "✅ 良好"
                    else:
                        needs_improvement += 1
                        status = "⚠️ 需改进"
                    
                    print(f"{status} {german_filename}: {score}分")
                    
                    # 显示主要问题
                    total_issues = (len(result['terminology_issues']) + 
                                  len(result['mobile_issues']) + 
                                  len(result['completeness_issues']) + 
                                  len(result['style_issues']))
                    
                    if total_issues > 0:
                        if result['terminology_issues']:
                            print(f"   🔸 术语问题: {len(result['terminology_issues'])}个")
                        if result['mobile_issues']:
                            print(f"   📱 移动端问题: {len(result['mobile_issues'])}个")
                        if result['completeness_issues']:
                            print(f"   📝 完整性问题: {len(result['completeness_issues'])}个")
                        if result['style_issues']:
                            print(f"   ✍️ 风格问题: {len(result['style_issues'])}个")
                else:
                    print(f"⚠️ 缺少对应英语文件: {english_path}")
    
    # 生成详细报告
    print("\n" + "=" * 70)
    print("📊 专家级德语翻译质量审核报告")
    print("=" * 70)
    
    if total_files > 0:
        avg_score = sum(r['overall_score'] for r in all_results) / total_files
        print(f"📄 审核文件总数: {total_files}")
        print(f"📈 平均质量评分: {avg_score:.1f}/100")
        print(f"🌟 优秀文件 (≥95分): {excellent_files} ({excellent_files/total_files*100:.1f}%)")
        print(f"✅ 良好文件 (85-94分): {good_files} ({good_files/total_files*100:.1f}%)")
        print(f"⚠️ 需改进文件 (<85分): {needs_improvement} ({needs_improvement/total_files*100:.1f}%)")
        
        # 问题统计
        terminology_total = sum(len(r['terminology_issues']) for r in all_results)
        mobile_total = sum(len(r['mobile_issues']) for r in all_results)
        completeness_total = sum(len(r['completeness_issues']) for r in all_results)
        style_total = sum(len(r['style_issues']) for r in all_results)
        
        print(f"\n🔍 问题分析:")
        print(f"   🎯 术语翻译问题: {terminology_total}")
        print(f"   📱 移动端适配问题: {mobile_total}")
        print(f"   📝 翻译完整性问题: {completeness_total}")
        print(f"   ✍️ 专业风格问题: {style_total}")
        
        # 显示需要重点关注的文件
        problematic_files = [r for r in all_results if r['overall_score'] < 85]
        if problematic_files:
            print(f"\n🔧 需要重点改进的文件:")
            problematic_files.sort(key=lambda x: x['overall_score'])
            for i, result in enumerate(problematic_files[:5]):
                print(f"{i+1}. {result['filename']}: {result['overall_score']}分")
                
                # 显示具体问题
                for issue in result['terminology_issues'][:2]:
                    print(f"     🎯 {issue}")
                for issue in result['mobile_issues'][:2]:
                    print(f"     📱 {issue}")
                for issue in result['completeness_issues'][:2]:
                    print(f"     📝 {issue}")
                for issue in result['style_issues'][:2]:
                    print(f"     ✍️ {issue}")
        
        # 总体评价
        if avg_score >= 95:
            print(f"\n🏆 总体评价: 优秀！德语翻译达到专家级水准")
        elif avg_score >= 85:
            print(f"\n👍 总体评价: 良好！德语翻译质量很高，少量细节需完善")
        elif avg_score >= 70:
            print(f"\n📈 总体评价: 中等！德语翻译基本合格，需要改进专业性")
        else:
            print(f"\n⚠️ 总体评价: 需要显著改进专业性和翻译质量")
        
        print(f"\n📱 移动端适配建议:")
        print(f"   - 确保所有页面都有正确的viewport设置")
        print(f"   - 使用响应式图片和字体大小")
        print(f"   - 测试在不同尺寸手机上的显示效果")
        print(f"   - 优化触摸交互和导航体验")
    
    else:
        print("❌ 未找到可审核的文件")

if __name__ == "__main__":
    main() 