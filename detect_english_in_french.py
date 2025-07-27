import os
import re
import sys

# 英语单词列表，用于检测英语内容
english_words = [
    "the", "and", "with", "for", "that", "this", "these", "those", "from", "your",
    "bird", "birds", "photography", "behavior", "camera", "settings", "techniques",
    "understanding", "essential", "composition", "ethical", "considerations", "post",
    "processing", "tips", "successful", "requires", "patience", "approach", "avoid",
    "sudden", "movements", "natural", "cover", "like", "when", "possible", "many",
    "have", "predictable", "routines", "observe", "before", "shooting", "anticipate",
    "best", "moments", "apply", "rule", "thirds", "placing", "eye", "along", "intersection",
    "points", "ensure", "sharp", "well", "lit", "most", "critical", "element", "any",
    "portrait", "leave", "space", "direction", "looking", "moving", "capture", "interaction",
    "use", "shallow", "depth", "field", "isolate", "subjects", "include", "environmental",
    "context", "shoot", "level", "more", "engaging", "images", "always", "prioritize",
    "welfare", "over", "getting", "shot", "maintain", "appropriate", "distances", "disturbing",
    "nests", "roosting", "sites", "never", "playback", "near", "nesting", "respect", "private",
    "property", "protected", "areas", "format", "maximum", "editing", "flexibility", "focus",
    "enhancing", "colors", "details", "rather", "than", "crop", "judiciously", "improve",
    "quality", "noise", "reduction", "software", "help", "high", "practice", "makes", "perfect",
    "start", "common", "approachable", "species", "backyard", "local", "parks", "skills",
    "develop", "tackle", "challenging", "situations", "remember"
]

def detect_english_content(file_path):
    """检测文件中的英语内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有文本内容（排除HTML标签和脚本）
    text_content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    text_content = re.sub(r'<style.*?</style>', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'<[^>]*>', ' ', text_content)
    
    # 分割成单词
    words = re.findall(r'\b\w+\b', text_content.lower())
    
    # 计算英语单词的数量
    english_count = sum(1 for word in words if word in english_words)
    
    # 如果英语单词数量超过阈值，认为文件包含英语内容
    if english_count > 10:
        return True, english_count
    return False, english_count

def main():
    """主函数"""
    fr_dir = './fr'
    
    if not os.path.exists(fr_dir):
        print(f"目录 {fr_dir} 不存在")
        return
    
    files_with_english = []
    
    # 遍历所有法语HTML文件
    for root, _, files in os.walk(fr_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                has_english, count = detect_english_content(file_path)
                if has_english:
                    files_with_english.append((file_path, count))
    
    # 按英语单词数量排序
    files_with_english.sort(key=lambda x: x[1], reverse=True)
    
    # 输出结果
    print(f"发现 {len(files_with_english)} 个包含英语内容的法语文件:")
    for file_path, count in files_with_english:
        print(f"{file_path}: {count} 个英语单词")

if __name__ == "__main__":
    main()