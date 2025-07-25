#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

class MultilingualTranslationOptimizer:
    """多语言翻译优化器"""
    
    def __init__(self):
        self.languages = {
            'de': 'German',
            'fr': 'French', 
            'es': 'Spanish',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'zh': 'Chinese'
        }
        
        # 德语翻译改进映射
        self.german_improvements = {
            'Vogel watching': 'Vogelbeobachtung',
            'Vogel watcher': 'Vogelbeobachter',
            'bird watching': 'Vogelbeobachtung',
            'bird watcher': 'Vogelbeobachter',
            'Fernglas sind': 'Ferngläser sind',
            'meiste wesentlich': 'wichtigste',
            'piece von': 'Teil der',
            'any Vogel': 'jeden Vogel',
            'der meiste': 'die meisten',
            'beliebt Wahl': 'beliebte Wahl',
            'among birders': 'unter Vogelbeobachtern',
            'ist 8x42': 'sind 8x42',
            'which offer': 'die bieten',
            'gut balance': 'gute Balance',
            'von magnification': 'der Vergrößerung',
            'field von view': 'Sichtfeld',
            'light-gathering Fähigkeit': 'Lichtsammelfähigkeit',
            'wann selecting': 'bei der Auswahl',
            'für Vogel watching': 'für die Vogelbeobachtung',
            'consider der': 'berücksichtigen Sie die',
            'und objective': 'und Objektivlinsen',
            'lens diameter': 'Durchmesser',
            'Higher magnification für': 'Höhere Vergrößerung für',
            'distant Vögel': 'entfernte Vögel',
            'but requires': 'aber erfordert',
            'steadier hands': 'ruhigere Hände',
            'und hat a': 'und hat ein',
            'narrower field': 'schmaleres Sichtfeld'
        }
        
        # 法语翻译改进映射
        self.french_improvements = {
            'Observation des Oiseaux': 'Observation des Oiseaux',
            'le/la most': 'le plus',
            'le/la': 'le',
            'vous à': 'vous de',
            'avec le/la': 'avec le',
            'dans le/la': 'dans le',
            'pour le/la': 'pour le',
            'de le/la': 'du',
            'et le/la': 'et le',
            'comme le/la': 'comme le',
            'sur le/la': 'sur le',
            'par le/la': 'par le'
        }
        
        # 日语翻译改进映射
        self.japanese_improvements = {
            'Bird Wchg': 'バードウォッチング',
            'Essentil': 'エッセンシャル',
            'Equipment': '機器',
            'Dす覆う': '発見する',
            '必要があります-持っています': '必須の',
            '道具s': 'ツール',
            '装備': '機器',
            'のために': 'のための',
            '成功ful': '成功した',
            '鳥 見るg': 'バードウォッチング',
            '冒険s': '冒険',
            'Boculrs': '双眼鏡',
            'す': 'は',
            'ほとんどの': '最も',
            '必須の': '重要な',
            '部分': '部分',
            'の': 'の',
            '装備': '機器',
            'のために': 'のための',
            'y': 'あらゆる',
            '鳥 見るer': 'バードウォッチャー'
        }
    
    def optimize_german_file(self, file_path):
        """优化德语文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 应用德语改进
            for old, new in self.german_improvements.items():
                content = content.replace(old, new)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"❌ 德语文件优化失败 {file_path}: {e}")
            return False
    
    def optimize_french_file(self, file_path):
        """优化法语文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 应用法语改进
            for old, new in self.french_improvements.items():
                content = content.replace(old, new)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"❌ 法语文件优化失败 {file_path}: {e}")
            return False
    
    def optimize_japanese_file(self, file_path):
        """优化日语文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 应用日语改进
            for old, new in self.japanese_improvements.items():
                content = content.replace(old, new)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"❌ 日语文件优化失败 {file_path}: {e}")
            return False
    
    def scan_language_directory(self, lang_code):
        """扫描语言目录中的HTML文件"""
        html_files = []
        lang_dir = lang_code
        
        if os.path.exists(lang_dir):
            for root, dirs, files in os.walk(lang_dir):
                for file in files:
                    if file.endswith('.html'):
                        html_files.append(os.path.join(root, file))
        
        return html_files
    
    def optimize_language(self, lang_code, max_files=10):
        """优化指定语言的翻译"""
        print(f"\n🔧 开始优化 {self.languages.get(lang_code, lang_code)} 翻译...")
        
        html_files = self.scan_language_directory(lang_code)
        
        if not html_files:
            print(f"⚠️ 未找到 {lang_code} 语言的HTML文件")
            return 0
        
        print(f"📁 找到 {len(html_files)} 个HTML文件")
        
        # 限制处理文件数量
        files_to_process = html_files[:max_files]
        optimized_count = 0
        
        for file_path in files_to_process:
            success = False
            
            if lang_code == 'de':
                success = self.optimize_german_file(file_path)
            elif lang_code == 'fr':
                success = self.optimize_french_file(file_path)
            elif lang_code == 'ja':
                success = self.optimize_japanese_file(file_path)
            else:
                print(f"⚠️ 暂不支持 {lang_code} 语言的自动优化")
                continue
            
            if success:
                print(f"✅ 已优化: {file_path}")
                optimized_count += 1
            else:
                print(f"❌ 优化失败: {file_path}")
        
        return optimized_count
    
    def generate_optimization_report(self):
        """生成优化报告"""
        print("\n" + "="*60)
        print("📊 多语言翻译优化报告")
        print("="*60)
        
        total_optimized = 0
        
        for lang_code in ['de', 'fr', 'ja']:
            html_files = self.scan_language_directory(lang_code)
            print(f"{self.languages[lang_code]:12} ({lang_code}): {len(html_files):3d} 个HTML文件")
        
        print("="*60)
        return total_optimized

def main():
    """主函数"""
    print("🚀 启动多语言翻译优化器")
    print("="*50)
    
    optimizer = MultilingualTranslationOptimizer()
    
    # 生成报告
    optimizer.generate_optimization_report()
    
    # 优化德语翻译
    german_count = optimizer.optimize_language('de', max_files=5)
    
    # 优化法语翻译
    french_count = optimizer.optimize_language('fr', max_files=5)
    
    # 优化日语翻译
    japanese_count = optimizer.optimize_language('ja', max_files=5)
    
    # 总结
    total_optimized = german_count + french_count + japanese_count
    
    print("\n" + "="*50)
    print("🎉 多语言翻译优化完成！")
    print(f"✅ 德语文件优化: {german_count} 个")
    print(f"✅ 法语文件优化: {french_count} 个")
    print(f"✅ 日语文件优化: {japanese_count} 个")
    print(f"📊 总计优化文件: {total_optimized} 个")
    print("\n主要改进:")
    print("- 修复常见翻译错误")
    print("- 改进语法结构")
    print("- 统一专业术语")
    print("- 提升翻译自然度")

if __name__ == "__main__":
    main()