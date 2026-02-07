#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Happy Poop 文章多语言准确性和完整性测试脚本
测试30篇 still-alive-tips 文章的所有语言版本
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json
from datetime import datetime

# 支持的语言列表
LANGUAGES = ['en', 'zh', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'ko', 'ru']

# 语言名称映射
LANGUAGE_NAMES = {
    'en': 'English',
    'zh': '中文',
    'es': 'Español',
    'fr': 'Français',
    'de': 'Deutsch',
    'it': 'Italiano',
    'pt': 'Português',
    'ja': '日本語',
    'ko': '한국어',
    'ru': 'Русский'
}

# 文章列表（30篇）
ARTICLES = [
    '01-emergency-kit-essentials.html',
    '02-personal-check-in-plan.html',
    '03-prevent-falls-at-home.html',
    '04-power-outage-readiness.html',
    '05-home-fire-escape-basics.html',
    '06-emergency-prep-older-adults.html',
    '07-fall-risk-facts.html',
    '08-evacuation-ready-checklist.html',
    '09-water-storage-basics.html',
    '10-shelter-in-place-planning.html',
    '11-menstrual-pain-relief.html',
    '12-menstrual-flow-check.html',
    '13-sex-during-period.html',
    '14-period-hygiene-basics.html',
    '15-diet-exercise-period.html',
    '16-trusted-contacts-list.html',
    '17-missed-check-in-steps.html',
    '18-travel-check-in-routine.html',
    '19-share-medical-notes.html',
    '20-smoke-alarm-maintenance.html',
    '21-carbon-monoxide-safety.html',
    '22-safer-bathroom-setup.html',
    '23-heat-safety-routine.html',
    '24-cold-weather-readiness.html',
    '25-medication-organization.html',
    '26-stress-reset-after-emergency.html',
    '27-emergency-alerts-wea.html',
    '28-weather-watches-warnings.html',
    '29-hydration-basics.html',
    '30-social-connection-safety.html'
]

class ArticleAnalyzer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.results = {
            'test_date': datetime.now().isoformat(),
            'total_articles': len(ARTICLES),
            'languages': LANGUAGES,
            'summary': {},
            'articles': {},
            'issues': []
        }
    
    def get_article_path(self, article_name, lang):
        """获取文章路径"""
        if lang == 'en':
            return self.base_path / 'still-alive-tips' / article_name
        else:
            return self.base_path / lang / 'still-alive-tips' / article_name
    
    def parse_html(self, file_path):
        """解析HTML文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                return soup, content
        except Exception as e:
            return None, None
    
    def extract_metadata(self, soup):
        """提取文章元数据"""
        if not soup:
            return None
        
        metadata = {
            'title': '',
            'lang': '',
            'description': '',
            'reading_time': '',
            'category': '',
            'content_length': 0,
            'has_tldr': False,
            'sections_count': 0,
            'images_count': 0,
            'links_count': 0
        }
        
        # 提取标题
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.text.strip()
        
        # 提取 lang 属性
        html_tag = soup.find('html')
        if html_tag and html_tag.get('lang'):
            metadata['lang'] = html_tag.get('lang')
        
        # 提取描述
        desc_tag = soup.find('meta', {'name': 'description'})
        if desc_tag and desc_tag.get('content'):
            metadata['description'] = desc_tag.get('content')
        
        # 提取阅读时间
        reading_time = soup.find('span', string=re.compile(r'\d+\s*(min|分钟|minutos|minutes|Minuten|minuti|minutos|分|분|минут)'))
        if reading_time:
            metadata['reading_time'] = reading_time.text.strip()
        
        # 提取分类
        category = soup.find('span', class_=re.compile(r'category|tag'))
        if category:
            metadata['category'] = category.text.strip()
        
        # 提取正文内容长度
        article_body = soup.find('article') or soup.find('main') or soup.find('body')
        if article_body:
            text_content = article_body.get_text(strip=True)
            metadata['content_length'] = len(text_content)
        
        # 检查是否有 TL;DR
        tldr = soup.find(string=re.compile(r'TL;DR|太长不看|Resumen|Résumé|Zusammenfassung|Sommario|Resumo|要約|요약|Краткое содержание', re.IGNORECASE))
        metadata['has_tldr'] = tldr is not None
        
        # 统计章节数
        sections = soup.find_all(['h2', 'h3'])
        metadata['sections_count'] = len(sections)
        
        # 统计图片数
        images = soup.find_all('img')
        metadata['images_count'] = len(images)
        
        # 统计链接数
        links = soup.find_all('a')
        metadata['links_count'] = len(links)
        
        return metadata
    
    def check_css_references(self, content, lang):
        """检查CSS引用路径是否正确"""
        if not content:
            return False, "无法读取文件内容"
        
        # 英文版本应该使用 ../
        # 其他语言版本应该使用 ../../
        expected_prefix = '../' if lang == 'en' else '../../'
        
        css_pattern = r'href=["\']([^"\']*\.css)["\']'
        css_refs = re.findall(css_pattern, content)
        
        for ref in css_refs:
            if not ref.startswith('http') and not ref.startswith(expected_prefix):
                return False, f"CSS路径错误: {ref} (期望前缀: {expected_prefix})"
        
        return True, "CSS引用正确"
    
    def compare_structure(self, base_metadata, target_metadata):
        """比较两个版本的结构相似度"""
        if not base_metadata or not target_metadata:
            return 0, []
        
        issues = []
        score = 100
        
        # 检查内容长度差异（允许30%的差异）
        if base_metadata['content_length'] > 0:
            length_ratio = target_metadata['content_length'] / base_metadata['content_length']
            if length_ratio < 0.7 or length_ratio > 1.3:
                issues.append(f"内容长度差异过大: {target_metadata['content_length']} vs {base_metadata['content_length']}")
                score -= 20
        
        # 检查章节数是否一致
        if base_metadata['sections_count'] != target_metadata['sections_count']:
            issues.append(f"章节数不一致: {target_metadata['sections_count']} vs {base_metadata['sections_count']}")
            score -= 15
        
        # 检查是否都有TL;DR
        if base_metadata['has_tldr'] != target_metadata['has_tldr']:
            issues.append(f"TL;DR存在性不一致")
            score -= 10
        
        # 检查图片数是否一致
        if base_metadata['images_count'] != target_metadata['images_count']:
            issues.append(f"图片数不一致: {target_metadata['images_count']} vs {base_metadata['images_count']}")
            score -= 10
        
        return max(0, score), issues
    
    def test_article(self, article_name):
        """测试单篇文章的所有语言版本"""
        print(f"\n测试文章: {article_name}")
        
        article_results = {
            'name': article_name,
            'languages': {},
            'completeness': 0,
            'quality_score': 0,
            'issues': []
        }
        
        # 首先读取英文版本作为基准
        en_path = self.get_article_path(article_name, 'en')
        en_soup, en_content = self.parse_html(en_path)
        en_metadata = self.extract_metadata(en_soup)
        
        if not en_metadata:
            article_results['issues'].append("❌ 英文版本不存在或无法解析")
            return article_results
        
        # 测试所有语言版本
        available_count = 0
        total_quality = 0
        
        for lang in LANGUAGES:
            lang_result = {
                'exists': False,
                'metadata': None,
                'css_check': None,
                'structure_score': 0,
                'issues': []
            }
            
            file_path = self.get_article_path(article_name, lang)
            
            # 检查文件是否存在
            if not file_path.exists():
                lang_result['issues'].append(f"❌ 文件不存在: {file_path}")
                article_results['languages'][lang] = lang_result
                continue
            
            lang_result['exists'] = True
            available_count += 1
            
            # 解析文件
            soup, content = self.parse_html(file_path)
            if not soup:
                lang_result['issues'].append("❌ 文件解析失败")
                article_results['languages'][lang] = lang_result
                continue
            
            # 提取元数据
            metadata = self.extract_metadata(soup)
            lang_result['metadata'] = metadata
            
            # 检查CSS引用
            css_ok, css_msg = self.check_css_references(content, lang)
            lang_result['css_check'] = {'ok': css_ok, 'message': css_msg}
            if not css_ok:
                lang_result['issues'].append(f"⚠️ {css_msg}")
            
            # 检查lang属性
            if metadata['lang']:
                expected_lang = 'zh-CN' if lang == 'zh' else lang
                if not metadata['lang'].startswith(expected_lang):
                    lang_result['issues'].append(f"⚠️ lang属性错误: {metadata['lang']} (期望: {expected_lang})")
            else:
                lang_result['issues'].append("⚠️ 缺少lang属性")
            
            # 与英文版本比较结构
            if lang != 'en':
                structure_score, structure_issues = self.compare_structure(en_metadata, metadata)
                lang_result['structure_score'] = structure_score
                lang_result['issues'].extend([f"⚠️ {issue}" for issue in structure_issues])
                total_quality += structure_score
            else:
                lang_result['structure_score'] = 100
                total_quality += 100
            
            # 检查基本内容完整性
            if metadata['content_length'] < 500:
                lang_result['issues'].append("⚠️ 内容过短，可能不完整")
            
            if not metadata['title']:
                lang_result['issues'].append("❌ 缺少标题")
            
            if not metadata['description']:
                lang_result['issues'].append("⚠️ 缺少描述")
            
            article_results['languages'][lang] = lang_result
            
            # 打印进度
            status = "✅" if len(lang_result['issues']) == 0 else "⚠️"
            print(f"  {status} {LANGUAGE_NAMES[lang]}: {len(lang_result['issues'])} 个问题")
        
        # 计算完整性和质量分数
        article_results['completeness'] = (available_count / len(LANGUAGES)) * 100
        article_results['quality_score'] = total_quality / len(LANGUAGES) if available_count > 0 else 0
        
        return article_results
    
    def run_full_test(self):
        """运行完整测试"""
        print("=" * 80)
        print("Happy Poop 文章多语言测试")
        print("=" * 80)
        print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"文章总数: {len(ARTICLES)}")
        print(f"语言数量: {len(LANGUAGES)}")
        print(f"预期文件总数: {len(ARTICLES) * len(LANGUAGES)}")
        print("=" * 80)
        
        # 测试每篇文章
        for article in ARTICLES:
            result = self.test_article(article)
            self.results['articles'][article] = result
        
        # 生成汇总统计
        self.generate_summary()
        
        # 保存结果
        self.save_results()
        
        # 打印报告
        self.print_report()
    
    def generate_summary(self):
        """生成汇总统计"""
        summary = {
            'total_files_expected': len(ARTICLES) * len(LANGUAGES),
            'total_files_found': 0,
            'total_files_missing': 0,
            'language_stats': {},
            'average_completeness': 0,
            'average_quality': 0,
            'articles_with_issues': 0,
            'critical_issues': 0,
            'warnings': 0
        }
        
        # 统计每种语言的情况
        for lang in LANGUAGES:
            summary['language_stats'][lang] = {
                'name': LANGUAGE_NAMES[lang],
                'available': 0,
                'missing': 0,
                'issues': 0
            }
        
        total_completeness = 0
        total_quality = 0
        
        for article_name, article_data in self.results['articles'].items():
            total_completeness += article_data['completeness']
            total_quality += article_data['quality_score']
            
            has_issues = False
            for lang, lang_data in article_data['languages'].items():
                if lang_data['exists']:
                    summary['total_files_found'] += 1
                    summary['language_stats'][lang]['available'] += 1
                    
                    if lang_data['issues']:
                        summary['language_stats'][lang]['issues'] += len(lang_data['issues'])
                        has_issues = True
                        
                        for issue in lang_data['issues']:
                            if '❌' in issue:
                                summary['critical_issues'] += 1
                            elif '⚠️' in issue:
                                summary['warnings'] += 1
                else:
                    summary['total_files_missing'] += 1
                    summary['language_stats'][lang]['missing'] += 1
            
            if has_issues:
                summary['articles_with_issues'] += 1
        
        summary['average_completeness'] = total_completeness / len(ARTICLES)
        summary['average_quality'] = total_quality / len(ARTICLES)
        
        self.results['summary'] = summary
    
    def save_results(self):
        """保存测试结果到JSON文件"""
        output_file = self.base_path / 'poop-multilingual-test-results.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 详细结果已保存到: {output_file}")
    
    def print_report(self):
        """打印测试报告"""
        summary = self.results['summary']
        
        print("\n" + "=" * 80)
        print("测试报告汇总")
        print("=" * 80)
        
        print(f"\n📊 整体统计:")
        print(f"  预期文件总数: {summary['total_files_expected']}")
        print(f"  实际找到文件: {summary['total_files_found']} ({summary['total_files_found']/summary['total_files_expected']*100:.1f}%)")
        print(f"  缺失文件数量: {summary['total_files_missing']}")
        print(f"  平均完整性: {summary['average_completeness']:.1f}%")
        print(f"  平均质量分数: {summary['average_quality']:.1f}/100")
        
        print(f"\n⚠️ 问题统计:")
        print(f"  有问题的文章: {summary['articles_with_issues']}/{len(ARTICLES)}")
        print(f"  严重问题: {summary['critical_issues']}")
        print(f"  警告: {summary['warnings']}")
        
        print(f"\n🌍 各语言统计:")
        for lang in LANGUAGES:
            stats = summary['language_stats'][lang]
            status = "✅" if stats['missing'] == 0 else "❌"
            print(f"  {status} {stats['name']:12s}: {stats['available']}/{len(ARTICLES)} 篇 "
                  f"(缺失: {stats['missing']}, 问题: {stats['issues']})")
        
        # 列出有问题的文章
        print(f"\n📋 有问题的文章列表:")
        problem_count = 0
        for article_name, article_data in self.results['articles'].items():
            article_issues = []
            for lang, lang_data in article_data['languages'].items():
                if lang_data['issues']:
                    article_issues.extend([f"  [{LANGUAGE_NAMES[lang]}] {issue}" for issue in lang_data['issues']])
            
            if article_issues:
                problem_count += 1
                print(f"\n  {problem_count}. {article_name}")
                for issue in article_issues[:5]:  # 只显示前5个问题
                    print(issue)
                if len(article_issues) > 5:
                    print(f"    ... 还有 {len(article_issues) - 5} 个问题")
        
        # 总体评分
        print(f"\n" + "=" * 80)
        print("总体评分")
        print("=" * 80)
        
        overall_score = (summary['average_completeness'] + summary['average_quality']) / 2
        
        if overall_score >= 95:
            grade = "A+ 优秀"
            emoji = "🌟"
        elif overall_score >= 90:
            grade = "A 良好"
            emoji = "✅"
        elif overall_score >= 80:
            grade = "B 合格"
            emoji = "👍"
        elif overall_score >= 70:
            grade = "C 需改进"
            emoji = "⚠️"
        else:
            grade = "D 不合格"
            emoji = "❌"
        
        print(f"\n{emoji} 综合评分: {overall_score:.1f}/100 - {grade}")
        print(f"  - 完整性: {summary['average_completeness']:.1f}%")
        print(f"  - 质量分数: {summary['average_quality']:.1f}/100")
        
        print("\n" + "=" * 80)

def main():
    # 获取当前脚本所在目录
    base_path = Path(__file__).parent
    
    # 创建分析器并运行测试
    analyzer = ArticleAnalyzer(base_path)
    analyzer.run_full_test()
    
    print("\n✅ 测试完成！")

if __name__ == '__main__':
    main()

