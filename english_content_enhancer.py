#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英语内容增强脚本 - 提升英语版本的专业性和可读性
"""

import os
import re
from pathlib import Path

class EnglishContentEnhancer:
    def __init__(self):
        self.base_dir = Path('.')
        
        # 英语内容增强词典
        self.content_enhancements = {
            # 更专业的表达
            'Bird watching is one of the most rewarding and accessible hobbies in the world.': 'Birdwatching is one of the most rewarding and accessible nature-based hobbies worldwide, offering endless opportunities for discovery, learning, and connection with the natural world.',
            
            'Whether you\'re drawn to the beauty of birds, fascinated by their behaviors, or simply enjoy being outdoors, birding offers endless opportunities for discovery and wonder': 'Whether you\'re captivated by avian beauty, intrigued by complex bird behaviors, or seeking meaningful outdoor experiences, birdwatching provides limitless opportunities for scientific discovery, personal growth, and natural wonder',
            
            'Bird watching combines outdoor adventure, scientific learning, and peaceful observation in a way that appeals to people of all ages and backgrounds': 'Birdwatching uniquely combines outdoor adventure, citizen science participation, and mindful observation, creating an inclusive hobby that transcends age, background, and experience level',
            
            'It\'s a hobby that grows with you, offering new challenges and rewards at every level.': 'This dynamic pursuit evolves with your expertise, continuously presenting fresh challenges, deeper insights, and increasingly meaningful rewards as your skills develop.',
            
            'Starting your birding journey doesn\'t require expensive equipment or extensive knowledge': 'Beginning your birdwatching journey requires minimal initial investment in equipment or prior knowledge, making it one of the most accessible nature-based activities',
            
            'With just a few basics, you can begin enjoying birds immediately.': 'With fundamental tools and techniques, you can immediately begin experiencing the joy and fascination of bird observation.',
            
            'Starting with common, easily identifiable species builds confidence and provides a foundation for learning more challenging birds': 'Beginning with abundant, distinctive species builds identification confidence while establishing the observational skills and pattern recognition abilities essential for identifying more challenging species',
            
            'These species are found in most areas and are great for practicing identification skills.': 'These widespread species offer consistent practice opportunities and serve as reliable reference points for developing core identification competencies.',
            
            'Learning systematic approaches to bird identification makes the process less overwhelming and more successful': 'Mastering systematic identification methodologies transforms what initially seems overwhelming into a structured, logical, and highly successful process',
            
            'The GISS method (General Impression of Size and Shape) helps you quickly categorize birds into groups.': 'The GISS method (General Impression of Size and Shape) enables rapid initial categorization, providing a systematic framework for efficient field identification.',
            
            'Great birding locations exist everywhere, from urban parks to wilderness areas': 'Exceptional birdwatching opportunities exist across diverse habitats, from urban green spaces and suburban neighborhoods to pristine wilderness areas and specialized ecosystems',
            
            'Starting close to home helps you learn local species before venturing to more distant locations.': 'Developing expertise with local avifauna provides essential foundational knowledge before exploring distant locations and unfamiliar species assemblages.',
            
            'Bird watching is a lifelong learning journey': 'Birdwatching represents a lifelong journey of continuous learning, skill development, and deepening appreciation for avian diversity and ecological complexity',
            
            'Start with 5-10 common local birds, then gradually expand your knowledge.': 'Begin by mastering 5-10 abundant local species, then systematically expand your knowledge through progressive exposure to new families, habitats, and seasonal variations.',
            
            'Join local birding groups, use apps wisely, and remember that every expert was once a beginner.': 'Engage with local birding communities, leverage technology thoughtfully as a learning tool, and remember that expertise develops through patient practice and mentorship from experienced birders.',
            
            'The birding community is welcoming and passionate about sharing knowledge': 'The global birding community is remarkably inclusive and enthusiastic about knowledge sharing, mentorship, and collaborative learning experiences',
            
            'Connect with others through local Audubon chapters, online communities like eBird, and citizen science projects.': 'Build connections through local Audubon chapters, participate in online platforms like eBird for data sharing, and contribute to meaningful citizen science initiatives that advance ornithological research.',
            
            'Most importantly, enjoy the journey and celebrate every discovery along the way!': 'Above all, embrace the journey with curiosity and wonder, celebrating each new discovery as a meaningful step in your developing relationship with the natural world.'
        }
        
        # 专业术语增强
        self.terminology_enhancements = {
            'bird identification': 'avian identification',
            'bird species': 'avian species',
            'bird behavior': 'avian behavior',
            'bird sounds': 'vocalizations',
            'bird calls': 'vocalizations and songs',
            'bird watching': 'birdwatching',
            'birding': 'birdwatching',
            'bird activity': 'avian activity',
            'bird diversity': 'avian diversity'
        }
        
        # 技术描述增强
        self.technical_enhancements = {
            'Invest in quality binoculars (8x42 is ideal)': 'Invest in quality binoculars with 8x42 configuration (optimal balance of magnification, field of view, and light-gathering capability)',
            'Focus on identifying 5-10 common birds': 'Concentrate on mastering identification of 5-10 locally abundant species',
            'Quality over quantity is key for beginners': 'Prioritizing thorough understanding over species count accelerates learning progression',
            'Compare to familiar species: sparrow-sized, robin-sized, crow-sized, or goose-sized': 'Use relative size comparisons with familiar reference species: sparrow-sized (5-6 inches), robin-sized (8-10 inches), crow-sized (17-20 inches), or goose-sized (25+ inches)',
            'Note major color blocks and patterns': 'Observe primary field marks including distinctive color patterns, wing bars, eye rings, and bill characteristics',
            'Where is it and what is it doing?': 'Document habitat preferences, foraging behavior, flight patterns, and social interactions for comprehensive identification'
        }
    
    def enhance_content(self, content):
        """增强内容质量"""
        # 应用内容增强
        for original, enhanced in self.content_enhancements.items():
            content = content.replace(original, enhanced)
        
        # 应用术语增强
        for original, enhanced in self.terminology_enhancements.items():
            # 使用词边界确保精确匹配
            pattern = r'\b' + re.escape(original) + r'\b'
            content = re.sub(pattern, enhanced, content, flags=re.IGNORECASE)
        
        # 应用技术描述增强
        for original, enhanced in self.technical_enhancements.items():
            content = content.replace(original, enhanced)
        
        return content
    
    def add_professional_sections(self, content):
        """添加专业内容部分"""
        # 在适当位置添加更多专业内容
        additional_content = '''
        
        <div class="section-title">Understanding Bird Behavior</div>
        
        <div class="main-text">
            Observing avian behavior provides crucial identification clues and deeper insights into species ecology<span class="emoji">🔍</span>. Different bird families exhibit characteristic behavioral patterns that aid in field identification.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🎯 Key Behavioral Indicators</div>
            Foraging techniques, flight patterns, social interactions, territorial displays, and habitat preferences all provide valuable identification information beyond physical appearance.
        </div>

        <div class="section-title">Seasonal Considerations</div>
        
        <div class="main-text">
            Bird populations and behaviors change dramatically throughout the year<span class="emoji">🍂</span>. Understanding seasonal patterns enhances identification success and reveals the dynamic nature of local avifauna.
        </div>
        
        <div class="step-container">
            <h4 style="color: #2e7d32; margin-bottom: 20px; font-size: 18px;">Seasonal Birding Calendar:</h4>
            <div class="step-item">
                <div class="step-number">🌸</div>
                <div class="step-content">
                    <h4>Spring Migration (March-May)</h4>
                    <p>Peak diversity as migrants return. Focus on warblers, vireos, and flycatchers. Dawn chorus reaches maximum intensity.</p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">☀️</div>
                <div class="step-content">
                    <h4>Breeding Season (May-July)</h4>
                    <p>Territorial behaviors, courtship displays, and nest-building activities. Males in peak plumage with active vocalizations.</p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">🍂</div>
                <div class="step-content">
                    <h4>Fall Migration (August-October)</h4>
                    <p>Mixed-age flocks, challenging juvenile plumages. Excellent for practicing identification skills with varied appearances.</p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">❄️</div>
                <div class="step-content">
                    <h4>Winter Residents (November-February)</h4>
                    <p>Concentrated populations at feeders and reliable food sources. Ideal for extended observation and photography.</p>
                </div>
            </div>
        </div>'''
        
        # 在"Building Your Skills"部分之前插入
        insertion_point = content.find('<div class="section-title">Building Your Skills</div>')
        if insertion_point != -1:
            content = content[:insertion_point] + additional_content + '\n        ' + content[insertion_point:]
        
        return content
    
    def enhance_file(self, file_path):
        """增强单个文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"增强 {file_path}")
            
            # 应用所有增强
            content = self.enhance_content(content)
            content = self.add_professional_sections(content)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            print(f"增强 {file_path} 时出错: {e}")
            return False
    
    def enhance_english_directory(self):
        """增强英语目录"""
        en_dir = self.base_dir / 'en'
        if not en_dir.exists():
            print("英语目录不存在")
            return
        
        print("🚀 开始增强英语内容...")
        
        # 查找所有HTML文件
        html_files = list(en_dir.rglob('*.html'))
        
        success_count = 0
        total_count = len(html_files)
        
        for html_file in html_files:
            if self.enhance_file(html_file):
                success_count += 1
        
        print(f"✅ 英语内容增强完成: {success_count}/{total_count} 文件成功")
    
    def run_enhancement(self):
        """运行增强过程"""
        print("🎯 开始英语内容专业化增强...")
        
        self.enhance_english_directory()
        
        print("\n🎉 英语内容增强完成！")
        self.generate_enhancement_report()
    
    def generate_enhancement_report(self):
        """生成增强报告"""
        print("\n📊 英语内容增强报告:")
        print("=" * 50)
        
        en_dir = self.base_dir / 'en'
        if en_dir.exists():
            html_files = list(en_dir.rglob('*.html'))
            print(f"英语 (en): {len(html_files)} 个文件已专业化增强")
        
        print("\n🎯 增强内容:")
        print("- ✅ 提升专业术语使用")
        print("- ✅ 增强技术描述准确性")
        print("- ✅ 改进内容深度和广度")
        print("- ✅ 添加季节性观鸟指导")
        print("- ✅ 强化行为观察技巧")
        print("- ✅ 提升整体可读性和专业性")

if __name__ == "__main__":
    enhancer = EnglishContentEnhancer()
    enhancer.run_enhancement()