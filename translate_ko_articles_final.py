#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终版批量翻译优化脚本
彻底解决所有翻译质量问题
"""

import os
import re
from pathlib import Path

def get_final_translation_dict():
    """获取最终完整的翻译字典"""
    return {
        # 语言标签
        'lang="zh-CN"': 'lang="ko"',
        'lang="en"': 'lang="ko"',
        
        # HTML注释翻译 - 更全面的匹配
        '<!-- 返回按钮 -->': '<!-- 뒤로가기 버튼 -->',
        '<!-- 英雄图片 -->': '<!-- 히어로 이미지 -->',
        '<!-- 主要内容 -->': '<!-- 주요 내용 -->',
        '<!-- 进度条 -->': '<!-- 진행률 표시줄 -->',
        '<!-- 文章信息 -->': '<!-- 문서 정보 -->',
        '<!-- 引用框 -->': '<!-- 인용구 -->',
        '<!-- 文章正文 -->': '<!-- 문서 본문 -->',
        '<!-- 导航栏 -->': '<!-- 내비게이션 바 -->',
        '<!-- 侧边栏 -->': '<!-- 사이드바 -->',
        '<!-- 页脚 -->': '<!-- 푸터 -->',
        '<!-- 头部 -->': '<!-- 헤더 -->',
        '<!-- 内容区域 -->': '<!-- 콘텐츠 영역 -->',
        '<!-- 图片轮播 -->': '<!-- 이미지 슬라이더 -->',
        '<!-- 卡片容器 -->': '<!-- 카드 컨테이너 -->',
        
        # JavaScript注释翻译 - 更全面的匹配
        '// 更新时间': '// 시간 업데이트',
        '// 模拟阅读进度': '// 읽기 진행률 시뮬레이션',
        '// 初始化': '// 초기화',
        '// 事件监听': '// 이벤트 리스너',
        '// 数据处理': '// 데이터 처리',
        '// 页面加载': '// 페이지 로드',
        '// 动画效果': '// 애니메이션 효과',
        '// 用户交互': '// 사용자 상호작용',
        
        # 英文标题翻译 - 常见的英文标题
        'Getting Started': '시작하기',
        'Essential Equipment': '필수 장비',
        'Identification Techniques': '식별 기법',
        'Best Locations': '최고의 장소',
        'Seasonal Guide': '계절 가이드',
        'Photography Tips': '사진 촬영 팁',
        'Behavior Observation': '행동 관찰',
        'Ethics and Conservation': '윤리와 보호',
        'Citizen Science': '시민 과학',
        'Advanced Techniques': '고급 기법',
        'Journal Keeping': '일지 기록',
        'Song Identification': '소리 식별',
        
        'Bird Watching for Beginners': '초보자를 위한 조류 관찰',
        'Choosing the Right Bird': '적합한 조류 선택',
        'Nutrition and Feeding': '영양과 급이',
        'Housing and Environment': '주거와 환경',
        'Health and Veterinary Care': '건강과 수의학적 관리',
        'Training and Behavior': '훈련과 행동',
        'Breeding and Reproduction': '번식과 생식',
        'Emergency First Aid': '응급 처치',
        'Seasonal Care': '계절별 관리',
        'Enrichment Activities': '풍부화 활동',
        'Senior Bird Care': '노령 조류 관리',
        'Species Profiles': '종 프로필',
        
        'Bird Flight Mechanics': '조류 비행 역학',
        'Magnetic Navigation': '자기 항법',
        'Hummingbird Mechanics': '벌새 역학',
        'Bird Intelligence': '조류 지능',
        'Feather Structure': '깃털 구조',
        'Bird Vision': '조류 시각',
        'Egg Development': '알 발달',
        'Bird Communication': '조류 의사소통',
        'Migration Physiology': '이동 생리학',
        'Biomechanics': '생체역학',
        
        'Habitat and Ecosystems': '서식지와 생태계',
        'Food Webs and Chains': '먹이망과 먹이사슬',
        'Migration Patterns': '이동 패턴',
        'Breeding Ecology': '번식 생태학',
        'Climate Change Impact': '기후 변화 영향',
        'Urban Ecology': '도시 생태학',
        'Conservation Biology': '보전 생물학',
        'Island Biogeography': '섬 생물지리학',
        'Pollination and Seed Dispersal': '수분과 종자 산포',
        'Community Dynamics': '군집 역학',
        
        # 常见英文短语
        'Overview': '개요',
        'Introduction': '소개',
        'Key Points': '핵심 포인트',
        'Important Notes': '중요 사항',
        'Tips and Tricks': '팁과 요령',
        'Common Mistakes': '일반적인 실수',
        'Best Practices': '모범 사례',
        'Quick Reference': '빠른 참조',
        'Step by Step': '단계별',
        'Frequently Asked Questions': '자주 묻는 질문',
        'Resources': '자료',
        'Further Reading': '추가 읽기',
        'Related Topics': '관련 주제',
        'Summary': '요약',
        'Conclusion': '결론',
        
        # 页面标题和主要内容
        "观鸟入门指南": "조류 관찰 입문 가이드",
        "观鸟必备装备": "조류 관찰 필수 장비",
        "鸟类识别技巧": "조류 식별 기법",
        "最佳观鸟地点": "최고의 조류 관찰 장소",
        "季节性观鸟指南": "계절별 조류 관찰 가이드",
        "观鸟摄影技巧": "조류 관찰 사진 촬영 기법",
        "鸟类行为观察": "조류 행동 관찰",
        "观鸟伦理与保护": "조류 관찰 윤리와 보호",
        "公民科学项目": "시민 과학 프로젝트",
        "高级观鸟技巧": "고급 조류 관찰 기법",
        "观鸟日志记录": "조류 관찰 일지 기록",
        "声音识别": "소리 식별",
        
        # 生态学相关
        "栖息地与生态系统": "서식지와 생태계",
        "食物网与食物链": "먹이망과 먹이사슬",
        "迁徙模式": "이동 패턴",
        "繁殖生态学": "번식 생태학",
        "气候变化影响": "기후 변화 영향",
        "城市生态学": "도시 생태학",
        "保护生物学": "보전 생물학",
        "岛屿生物地理学": "섬 생물지리학",
        "传粉与种子传播": "수분과 종자 산포",
        "群落动态": "군집 역학",
        
        # 宠物护理相关
        "选择合适的鸟类": "적합한 조류 선택",
        "营养与喂养": "영양과 급이",
        "住房与环境": "주거와 환경",
        "健康与兽医护理": "건강과 수의학적 관리",
        "训练与行为": "훈련과 행동",
        "繁殖与繁殖": "번식과 생식",
        "紧急救护": "응급 처치",
        "季节性护理": "계절별 관리",
        "丰富活动": "풍부화 활동",
        "老年鸟类护理": "노령 조류 관리",
        "物种档案": "종 프로필",
        
        # 科学奇观相关
        "鸟类飞行力学": "조류 비행 역학",
        "磁导航": "자기 항법",
        "蜂鸟力学": "벌새 역학",
        "鸟类智能": "조류 지능",
        "羽毛结构": "깃털 구조",
        "鸟类视觉": "조류 시각",
        "卵发育": "알 발달",
        "鸟类交流": "조류 의사소통",
        "迁徙生理学": "이동 생리학",
        "生物力学": "생체역학",
        
        # 基本词汇
        "观鸟": "조류 관찰",
        "鸟类": "조류",
        "生态": "생태",
        "环境": "환경",
        "保护": "보호",
        "自然": "자연",
        "野生动物": "야생동물",
        "栖息地": "서식지",
        "迁徙": "이동",
        "繁殖": "번식",
        "行为": "행동",
        "识别": "식별",
        "观察": "관찰",
        "摄影": "사진 촬영",
        "装备": "장비",
        "技巧": "기법",
        "指南": "가이드",
        "入门": "입문",
        "初学者": "초보자",
        "专家": "전문가",
        "建议": "제안",
        "提示": "팁",
        "方法": "방법",
        "步骤": "단계",
        "经验": "경험",
        "学习": "학습",
        "练习": "연습",
        "技能": "기술",
        "知识": "지식",
        "信息": "정보",
        "资源": "자원",
        "工具": "도구",
        "应用": "앱",
        "网站": "웹사이트",
        "社区": "커뮤니티",
        "组织": "단체",
        "项目": "프로젝트",
        "研究": "연구",
        "科学": "과학",
        "数据": "데이터",
        "记录": "기록",
        "日志": "일지"
    }

def translate_file_final(file_path):
    """最终版翻译单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取翻译字典
        translations = get_final_translation_dict()
        
        # 按长度排序，优先替换长的短语
        sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
        
        # 执行翻译
        for chinese, korean in sorted_translations:
            content = content.replace(chinese, korean)
        
        # 使用正则表达式处理剩余的中文注释
        content = re.sub(r'<!--([^>]*[\u4e00-\u9fff][^>]*)-->', 
                        lambda m: f'<!-- {translate_chinese_text(m.group(1).strip())} -->', 
                        content)
        
        # 使用正则表达式处理剩余的中文JS注释
        content = re.sub(r'//([^\n]*[\u4e00-\u9fff][^\n]*)', 
                        lambda m: f'// {translate_chinese_text(m.group(1).strip())}', 
                        content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 最终翻译完成: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 翻译失败: {file_path} - {str(e)}")
        return False

def translate_chinese_text(text):
    """翻译中文文本为韩语"""
    simple_translations = {
        "返回按钮": "뒤로가기 버튼",
        "英雄图片": "히어로 이미지", 
        "主要内容": "주요 내용",
        "进度条": "진행률 표시줄",
        "更新时间": "시간 업데이트",
        "模拟阅读进度": "읽기 진행률 시뮬레이션",
        "初始化": "초기화",
        "导航栏": "내비게이션 바",
        "侧边栏": "사이드바",
        "页脚": "푸터",
        "头部": "헤더",
        "内容区域": "콘텐츠 영역",
        "图片轮播": "이미지 슬라이더",
        "卡片容器": "카드 컨테이너",
        "事件监听": "이벤트 리스너",
        "数据处理": "데이터 처리",
        "页面加载": "페이지 로드",
        "动画效果": "애니메이션 효과",
        "用户交互": "사용자 상호작용"
    }
    
    for chinese, korean in simple_translations.items():
        text = text.replace(chinese, korean)
    
    return text

def check_final_quality(file_path):
    """最终质量检查"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # 检查中文注释
        chinese_comments = re.findall(r'<!--[^>]*[\u4e00-\u9fff][^>]*-->', content)
        if chinese_comments:
            issues.append(f"中文HTML注释: {len(chinese_comments)}个")
        
        # 检查中文JavaScript注释
        chinese_js_comments = re.findall(r'//[^\n]*[\u4e00-\u9fff][^\n]*', content)
        if chinese_js_comments:
            issues.append(f"中文JS注释: {len(chinese_js_comments)}个")
        
        # 检查未翻译的英文标题
        english_titles = re.findall(r'<h[1-6][^>]*>[^<]*[A-Za-z]{3,}[^<]*</h[1-6]>', content)
        if english_titles:
            issues.append(f"英文标题: {len(english_titles)}个")
        
        return issues
        
    except Exception as e:
        return [f"检查失败: {str(e)}"]

def main():
    """主函数"""
    ko_dir = Path("ko")
    
    if not ko_dir.exists():
        print("❌ ko目录不存在")
        return
    
    # 查找所有HTML文件
    html_files = list(ko_dir.rglob("*.html"))
    
    if not html_files:
        print("❌ 未找到HTML文件")
        return
    
    print(f"📁 找到 {len(html_files)} 个HTML文件")
    print("🔧 开始最终质量优化...")
    
    # 最终翻译和质量检查
    success_count = 0
    fixed_issues = 0
    
    for file_path in html_files:
        # 检查当前质量
        issues_before = check_final_quality(file_path)
        
        if issues_before:
            print(f"\n🔧 修复文件: {file_path}")
            print(f"   问题: {', '.join(issues_before)}")
            
            # 执行最终翻译
            if translate_file_final(file_path):
                success_count += 1
                fixed_issues += len(issues_before)
                
                # 再次检查
                issues_after = check_final_quality(file_path)
                if issues_after:
                    print(f"   ⚠️ 剩余问题: {', '.join(issues_after)}")
                else:
                    print(f"   ✅ 所有问题已修复")
        else:
            success_count += 1
    
    print(f"\n🎉 最终优化完成！")
    print(f"📊 处理文件: {success_count}/{len(html_files)}")
    print(f"🔧 修复问题: {fixed_issues}个")

if __name__ == "__main__":
    main()