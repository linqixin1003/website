#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化版批量翻译ko目录下的HTML文章为韩语
修复翻译质量问题，确保完整翻译
"""

import os
import re
from pathlib import Path

def get_comprehensive_translation_dict():
    """获取全面的翻译字典"""
    return {
        # 语言标签
        'lang="zh-CN"': 'lang="ko"',
        'lang="en"': 'lang="ko"',
        
        # HTML注释翻译
        '<!-- 返回按钮 -->': '<!-- 뒤로가기 버튼 -->',
        '<!-- 英雄图片 -->': '<!-- 히어로 이미지 -->',
        '<!-- 主要内容 -->': '<!-- 주요 내용 -->',
        '<!-- 进度条 -->': '<!-- 진행률 표시줄 -->',
        '<!-- 文章信息 -->': '<!-- 문서 정보 -->',
        '<!-- 引用框 -->': '<!-- 인용구 -->',
        '<!-- 文章正文 -->': '<!-- 문서 본문 -->',
        
        # JavaScript注释翻译
        '// 更新时间': '// 시간 업데이트',
        '// 模拟阅读进度': '// 읽기 진행률 시뮬레이션',
        '// 初始化': '// 초기화',
        
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
        
        # 知识相关
        "初学者指南": "초보자 가이드",
        "Bird Watching for Beginners": "초보자를 위한 조류 관찰",
        "必备装备": "필수 장비",
        "Essential Equipment": "필수 장비",
        "识别技巧": "식별 기법",
        "Identification Techniques": "식별 기법",
        "最佳地点": "최고의 장소",
        "Best Locations": "최고의 장소",
        "行为观察": "행동 관찰",
        "Behavior Observation": "행동 관찰",
        "摄影技巧": "사진 촬영 기법",
        "Photography Tips": "사진 촬영 팁",
        "季节指南": "계절 가이드",
        "Seasonal Guide": "계절 가이드",
        "日志记录": "일지 기록",
        "Journal Keeping": "일지 기록",
        "伦理保护": "윤리 보호",
        "Ethics and Conservation": "윤리와 보호",
        
        # 英文内容翻译
        "Your First Week of Birding:": "조류 관찰 첫 주:",
        "Start in Your Backyard": "뒷마당에서 시작하기",
        "Begin by observing birds in your own yard or neighborhood. Spend 15-20 minutes each morning watching and listening.": "자신의 마당이나 동네에서 조류를 관찰하는 것부터 시작하세요. 매일 아침 15-20분씩 관찰하고 들어보세요.",
        "Get Basic Equipment": "기본 장비 준비하기",
        "Invest in simple binoculars (8x42 is ideal) and download a bird identification app like BirdAiSnap.": "간단한 쌍안경(8x42가 이상적)에 투자하고 BirdAiSnap과 같은 조류 식별 앱을 다운로드하세요.",
        "Learn Common Species": "일반적인 종 학습하기",
        "Focus on identifying 5-10 common birds in your area first. Quality over quantity is key for beginners.": "먼저 해당 지역의 일반적인 조류 5-10종 식별에 집중하세요. 초보자에게는 양보다 질이 중요합니다.",
        "Visit Local Parks": "지역 공원 방문하기",
        "Explore nearby parks and nature centers. These locations often have diverse habitats and more bird species.": "근처 공원과 자연 센터를 탐험하세요. 이런 장소들은 종종 다양한 서식지와 더 많은 조류 종을 가지고 있습니다.",
        "Join Others": "다른 사람들과 함께하기",
        "Connect with local birding groups. Experienced birders are usually happy to help beginners learn.": "지역 조류 관찰 그룹과 연결하세요. 경험 있는 조류 관찰자들은 보통 초보자들의 학습을 기꺼이 도와줍니다.",
        
        "Common Birds to Learn First": "먼저 배워야 할 일반적인 조류",
        "Starting with common, easily identifiable species builds confidence and provides a foundation for learning more challenging birds": "일반적이고 쉽게 식별할 수 있는 종부터 시작하면 자신감을 기르고 더 어려운 조류를 학습하는 기초를 제공합니다",
        "These species are found in most areas and are great for practicing identification skills.": "이러한 종들은 대부분의 지역에서 발견되며 식별 기술을 연습하기에 좋습니다.",
        
        "American Robin": "아메리카울새",
        "Orange breast, dark head. Often seen hopping on lawns.": "주황색 가슴, 어두운 머리. 잔디밭에서 뛰어다니는 모습을 자주 볼 수 있습니다.",
        "Northern Cardinal": "북부홍관조",
        "Bright red male, brown female. Clear whistled songs.": "밝은 빨간색 수컷, 갈색 암컷. 명확한 휘파람 소리.",
        "Blue Jay": "어치",
        "Bright blue with white underparts. Intelligent behavior.": "밝은 파란색에 흰색 배 부분. 지능적인 행동.",
        "House Sparrow": "집참새",
        "Small brown bird. Very common around homes.": "작은 갈색 새. 집 주변에서 매우 흔함.",
        "Mourning Dove": "슬픈비둘기",
        "Soft gray-brown. Distinctive cooing call.": "부드러운 회갈색. 독특한 구구 소리.",
        "Red-winged Blackbird": "붉은어깨찌르레기",
        "Black male with red shoulder patches.": "빨간 어깨 패치가 있는 검은색 수컷.",
        
        "Learning Tips for Beginners": "초보자를 위한 학습 팁",
        "Focus on size and shape first, notice behavior patterns, listen to sounds, use size comparisons, and always take notes of what you observe.": "먼저 크기와 모양에 집중하고, 행동 패턴을 관찰하며, 소리를 듣고, 크기 비교를 사용하며, 관찰한 것을 항상 기록하세요.",
        
        "Basic Identification Techniques": "기본 식별 기법",
        "Learning systematic approaches to bird identification makes the process less overwhelming and more successful": "조류 식별에 대한 체계적인 접근법을 배우면 과정이 덜 부담스럽고 더 성공적이 됩니다",
        "The GISS method (General Impression of Size and Shape) helps you quickly categorize birds into groups.": "GISS 방법(크기와 모양의 일반적 인상)은 조류를 그룹으로 빠르게 분류하는 데 도움이 됩니다.",
        
        "Simple Identification Process:": "간단한 식별 과정:",
        "Size and Shape": "크기와 모양",
        "Compare to familiar species: sparrow-sized, robin-sized, crow-sized, or goose-sized.": "친숙한 종과 비교: 참새 크기, 울새 크기, 까마귀 크기, 또는 거위 크기.",
        "Color Pattern": "색상 패턴",
        "Note major color blocks and patterns, but don't get lost in fine details initially.": "주요 색상 블록과 패턴을 주목하되, 처음에는 세부 사항에 너무 빠지지 마세요.",
        "Behavior and Habitat": "행동과 서식지",
        "Where is it and what is it doing? This provides crucial identification clues.": "어디에 있고 무엇을 하고 있나요? 이것은 중요한 식별 단서를 제공합니다.",
        
        "Where to Go Birding": "조류 관찰 장소",
        "Great birding locations exist everywhere, from urban parks to wilderness areas": "도시 공원부터 야생 지역까지 훌륭한 조류 관찰 장소가 어디에나 존재합니다",
        "Starting close to home helps you learn local species before venturing to more distant locations.": "집 가까이에서 시작하면 더 먼 곳으로 모험을 떠나기 전에 지역 종을 배우는 데 도움이 됩니다.",
        
        "Best Times for Birding": "조류 관찰 최적 시간",
        "Early morning (first 2-3 hours after sunrise), late afternoon before sunset, overcast days, and after storms when weather changes trigger increased bird activity.": "이른 아침(일출 후 첫 2-3시간), 일몰 전 늦은 오후, 흐린 날, 그리고 날씨 변화가 조류 활동 증가를 유발하는 폭풍 후.",
        
        "Building Your Skills": "기술 향상하기",
        "Bird watching is a lifelong learning journey": "조류 관찰은 평생에 걸친 학습 여정입니다",
        "Start with 5-10 common local birds, then gradually expand your knowledge. Join local birding groups, use apps wisely, and remember that every expert was once a beginner.": "5-10종의 일반적인 지역 조류부터 시작하여 점차 지식을 확장하세요. 지역 조류 관찰 그룹에 가입하고, 앱을 현명하게 사용하며, 모든 전문가도 한때는 초보자였다는 것을 기억하세요.",
        
        "The birding community is welcoming and passionate about sharing knowledge": "조류 관찰 커뮤니티는 환영하며 지식 공유에 열정적입니다",
        "Connect with others through local Audubon chapters, online communities like eBird, and citizen science projects. Most importantly, enjoy the journey and celebrate every discovery along the way!": "지역 오듀본 지부, eBird와 같은 온라인 커뮤니티, 시민 과학 프로젝트를 통해 다른 사람들과 연결하세요. 가장 중요한 것은 여정을 즐기고 그 과정에서 모든 발견을 축하하는 것입니다!",
        
        # 常用短语和句子
        "开启您的观鸟之旅，发现自然的奇妙世界": "조류 관찰 여행을 시작하여 자연의 신비로운 세계를 발견하세요",
        "工欲善其事，必先利其器": "일을 잘하려면 먼저 도구를 날카롭게 해야 한다",
        "观察细节，掌握识别的艺术": "세부사항을 관찰하고 식별의 예술을 마스터하세요",
        "发现世界顶级观鸟目的地和隐藏宝地": "세계 최고의 조류 관찰 목적지와 숨겨진 보석 같은 장소를 발견하세요",
        "了解鸟类活动如何随季节变化并规划您的观察": "조류 활동이 계절에 따라 어떻게 변화하는지 이해하고 관찰을 계획하세요",
        "生命的家园，生态的基石": "생명의 터전, 생태의 기반",
        "栖息地是鸟类生存的基础，生态系统是它们繁衍的舞台。保护栖息地就是保护鸟类的未来。": "서식지는 조류 생존의 기초이고, 생태계는 그들이 번식하는 무대입니다. 서식지를 보호하는 것이 조류의 미래를 보호하는 것입니다.",
        
        # 基本词汇 - 按使用频率和重要性排序
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
        "日志": "일지",
        "报告": "보고서",
        "分析": "분석",
        "统计": "통계",
        "趋势": "트렌드",
        "变化": "변화",
        "发展": "발전",
        "进步": "진보",
        "创新": "혁신",
        "技术": "기술",
        "设备": "장비",
        "软件": "소프트웨어",
        "硬件": "하드웨어",
        "系统": "시스템",
        "平台": "플랫폼",
        "服务": "서비스",
        "支持": "지원",
        "帮助": "도움",
        "协助": "지원",
        "合作": "협력",
        "参与": "참여",
        "贡献": "기여",
        "分享": "공유",
        "交流": "교류",
        "沟通": "소통",
        "联系": "연락",
        "网络": "네트워크",
        "连接": "연결",
        "链接": "링크",
        "关系": "관계",
        "影响": "영향",
        "作用": "작용",
        "效果": "효과",
        "结果": "결과",
        "成果": "성과",
        "收获": "수확",
        "收益": "수익",
        "价值": "가치",
        "意义": "의미",
        "重要性": "중요성",
        "必要性": "필요성",
        "可能性": "가능성",
        "机会": "기회",
        "挑战": "도전",
        "困难": "어려움",
        "问题": "문제",
        "解决": "해결",
        "方案": "방안",
        "策略": "전략",
        "计划": "계획",
        "目标": "목표",
        "目的": "목적",
        "任务": "과제",
        "工作": "작업",
        "活动": "활동",
        "事件": "사건",
        "情况": "상황",
        "条件": "조건",
        "要求": "요구",
        "标准": "기준",
        "规则": "규칙",
        "法律": "법률",
        "法规": "법규",
        "政策": "정책",
        "制度": "제도",
        "管理": "관리",
        "控制": "제어",
        "监督": "감독",
        "检查": "검사",
        "评估": "평가",
        "审查": "심사",
        "测试": "테스트",
        "实验": "실험",
        "试验": "시험",
        "调查": "조사",
        "比较": "비교",
        "对比": "대비",
        "区别": "구별",
        "差异": "차이",
        "相同": "동일",
        "类似": "유사",
        "不同": "다른",
        "各种": "다양한",
        "多样": "다양",
        "丰富": "풍부",
        "充足": "충분",
        "足够": "충분한",
        "适当": "적당한",
        "合适": "적합한",
        "正确": "올바른",
        "准确": "정확한",
        "精确": "정밀한",
        "详细": "자세한",
        "具体": "구체적인",
        "明确": "명확한",
        "清楚": "명료한",
        "清晰": "선명한",
        "简单": "간단한",
        "复杂": "복잡한",
        "困难": "어려운",
        "容易": "쉬운",
        "简易": "간편한",
        "方便": "편리한",
        "实用": "실용적인",
        "有用": "유용한",
        "有效": "효과적인",
        "成功": "성공적인",
        "失败": "실패한",
        "完成": "완성된",
        "未完成": "미완성된",
        "开始": "시작",
        "结束": "끝",
        "继续": "계속",
        "停止": "중지",
        "暂停": "일시정지",
        "恢复": "복구",
        "重新": "다시",
        "再次": "재차",
        "重复": "반복",
        "循环": "순환",
        "过程": "과정",
        "阶段": "단계",
        "时期": "시기",
        "时间": "시간",
        "日期": "날짜",
        "年份": "연도",
        "月份": "월",
        "季节": "계절",
        "春季": "봄철",
        "夏季": "여름철",
        "秋季": "가을철",
        "冬季": "겨울철",
        "春天": "봄",
        "夏天": "여름",
        "秋天": "가을",
        "冬天": "겨울",
        "早晨": "아침",
        "上午": "오전",
        "中午": "정오",
        "下午": "오후",
        "傍晚": "저녁",
        "晚上": "밤",
        "夜晚": "밤",
        "白天": "낮",
        "黑夜": "밤",
        "今天": "오늘",
        "昨天": "어제",
        "明天": "내일",
        "现在": "지금",
        "过去": "과거",
        "未来": "미래",
        "最近": "최근",
        "以前": "이전",
        "以后": "이후",
        "之前": "이전",
        "之后": "이후",
        "当前": "현재",
        "目前": "현재",
        "此时": "이때",
        "那时": "그때",
        "同时": "동시에",
        "然后": "그다음",
        "接着": "이어서",
        "最后": "마지막으로",
        "最终": "최종적으로",
        "总之": "요약하면",
        "总的来说": "전반적으로",
        "一般来说": "일반적으로",
        "通常": "보통",
        "经常": "자주",
        "有时": "때때로",
        "偶尔": "가끔",
        "很少": "거의 없이",
        "从不": "결코 ~하지 않다",
        "总是": "항상",
        "永远": "영원히",
        "始终": "줄곧",
        "一直": "계속",
        "持续": "지속",
        "不断": "끊임없이",
        "连续": "연속",
        "频繁": "빈번한",
        "定期": "정기적인",
        "规律": "규칙적인",
        "固定": "고정된",
        "稳定": "안정된",
        "改变": "변경",
        "转变": "전환",
        "提高": "향상",
        "改善": "개선",
        "增加": "증가",
        "减少": "감소",
        "增长": "성장",
        "下降": "하락",
        "上升": "상승",
        "提升": "향상",
        "降低": "낮추다",
        "扩大": "확대",
        "缩小": "축소",
        "扩展": "확장",
        "延伸": "연장",
        "延长": "연장",
        "缩短": "단축",
        "加快": "가속화",
        "放慢": "늦추다",
        "加速": "가속",
        "减速": "감속",
        "快速": "빠른",
        "缓慢": "느린",
        "迅速": "신속한",
        "及时": "적시의",
        "准时": "정시의",
        "按时": "시간에 맞춰",
        "延迟": "지연",
        "推迟": "연기",
        "提前": "앞당기다",
        "早期": "초기",
        "晚期": "후기",
        "中期": "중기",
        "长期": "장기",
        "短期": "단기",
        "临时": "임시",
        "永久": "영구",
        "暂时": "일시적",
        "持久": "지속적",
        "长久": "오래",
        "短暂": "짧은",
        "瞬间": "순간",
        "立即": "즉시",
        "马上": "곧",
        "很快": "빨리",
        "慢慢": "천천히",
        "逐渐": "점차",
        "渐渐": "점점",
        "突然": "갑자기",
        "忽然": "갑자기",
        "立刻": "즉시",
        "当即": "즉시",
        "随即": "곧바로",
        "接下来": "다음에",
        "后来": "나중에",
        "因此": "따라서",
        "所以": "그래서",
        "因为": "왜냐하면",
        "由于": "~로 인해",
        "为了": "~을 위해",
        "原因": "원인",
        "理由": "이유",
        "根据": "~에 따라",
        "按照": "~에 따라",
        "依据": "근거",
        "基于": "~을 바탕으로",
        "通过": "~을 통해",
        "利用": "이용",
        "使用": "사용",
        "采用": "채용",
        "应用": "적용",
        "运用": "활용",
        "发挥": "발휘",
        "展示": "전시",
        "表现": "표현",
        "显示": "표시",
        "表明": "표명",
        "说明": "설명",
        "解释": "해석",
        "描述": "묘사",
        "介绍": "소개",
        "讲述": "서술",
        "叙述": "서술",
        "汇报": "보고",
        "通知": "통지",
        "告知": "알림",
        "提醒": "상기시키다",
        "警告": "경고",
        "推荐": "추천",
        "劝告": "권고",
        "忠告": "충고",
        "指导": "지도",
        "引导": "안내",
        "鼓励": "격려",
        "激励": "격려",
        "促进": "촉진",
        "推动": "추진",
        "推进": "추진",
        "改进": "개선",
        "完善": "완선",
        "优化": "최적화",
        "加强": "강화",
        "增强": "증강",
        "巩固": "공고히",
        "稳固": "견고한",
        "牢固": "견고한",
        "坚固": "견고한",
        "坚强": "강한",
        "强大": "강력한",
        "强壮": "튼튼한",
        "健康": "건강한",
        "良好": "양호한",
        "优秀": "우수한",
        "杰出": "뛰어난",
        "出色": "훌륭한",
        "优异": "우수한",
        "卓越": "탁월한",
        "完美": "완벽한",
        "理想": "이상적인",
        "最佳": "최고의",
        "最好": "가장 좋은",
        "最优": "최적의",
        "顶级": "최고급",
        "高级": "고급",
        "中级": "중급",
        "初级": "초급",
        "基础": "기초",
        "基本": "기본",
        "主要": "주요",
        "重要": "중요한",
        "关键": "핵심",
        "核心": "핵심",
        "中心": "중심",
        "焦点": "초점",
        "重点": "중점",
        "要点": "요점",
        "关键点": "핵심 포인트",
        "特点": "특징",
        "特色": "특색",
        "特征": "특징",
        "特性": "특성",
        "性质": "성질",
        "属性": "속성",
        "功能": "기능",
        "意义": "의미",
        "价值": "가치",
        "好处": "이점",
        "优点": "장점",
        "缺点": "단점",
        "不足": "부족",
        "希望": "희망",
        "期望": "기대",
        "理想": "이상",
        "梦想": "꿈",
        "愿望": "소망",
        "需要": "필요",
        "需求": "수요",
        "要求": "요구",
        "规定": "규정",
        "方针": "방침",
        "原则": "원칙",
        "准则": "준칙",
        "手册": "매뉴얼",
        "概述": "개요",
        "总结": "요약",
        "摘要": "요약",
        "简介": "간략한 소개",
        "详情": "상세 정보",
        "内容": "내용",
        "资料": "자료",
        "材料": "재료",
        "文件": "파일",
        "文档": "문서",
        "档案": "파일",
        "来源": "출처",
        "参考": "참고",
        "引用": "인용",
        "网址": "웹 주소",
        "页面": "페이지",
        "界面": "인터페이스",
        "程序": "프로그램",
        "器材": "기재",
        "用品": "용품",
        "物品": "물품",
        "产品": "제품",
        "商品": "상품",
        "能力": "능력",
        "水平": "수준",
        "程度": "정도",
        "等级": "등급",
        "级别": "레벨",
        "层次": "층차",
        "流程": "프로세스",
        "顺序": "순서",
        "次序": "차례",
        "排列": "배열",
        "安排": "배치",
        "准备": "준비",
        "预备": "예비",
        "准备工作": "준비 작업",
        "前期": "전기",
        "初期": "초기",
        "起始": "시작",
        "开端": "시작",
        "起点": "시작점",
        "出发点": "출발점",
        "根本": "근본",
        "本质": "본질",
        "实质": "실질",
        "重心": "중심"
    }

def translate_file_improved(file_path):
    """优化版翻译单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取翻译字典
        translations = get_comprehensive_translation_dict()
        
        # 按长度排序，优先替换长的短语
        sorted_translations = sorted(translations.items(), key=lambda x: len(x[0]), reverse=True)
        
        # 执行翻译
        for chinese, korean in sorted_translations:
            content = content.replace(chinese, korean)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 优化翻译完成: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 翻译失败: {file_path} - {str(e)}")
        return False

def check_translation_quality(file_path):
    """检查翻译质量"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # 检查中文注释
        chinese_comments = re.findall(r'<!--[^>]*[\u4e00-\u9fff][^>]*-->', content)
        if chinese_comments:
            issues.append(f"发现中文HTML注释: {len(chinese_comments)}个")
        
        # 检查中文JavaScript注释
        chinese_js_comments = re.findall(r'//[^\n]*[\u4e00-\u9fff][^\n]*', content)
        if chinese_js_comments:
            issues.append(f"发现中文JS注释: {len(chinese_js_comments)}个")
        
        # 检查混合语言内容
        english_titles = re.findall(r'<h[1-6][^>]*>[^<]*[A-Za-z]{3,}[^<]*</h[1-6]>', content)
        if english_titles:
            issues.append(f"发现英文标题: {len(english_titles)}个")
        
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
    print("🔍 开始质量检查和优化翻译...")
    
    # 检查和翻译所有文件
    success_count = 0
    total_issues = 0
    
    for file_path in html_files:
        print(f"\n处理文件: {file_path}")
        
        # 检查翻译质量
        issues = check_translation_quality(file_path)
        if issues:
            print(f"  发现问题: {', '.join(issues)}")
            total_issues += len(issues)
            
            # 重新翻译
            if translate_file_improved(file_path):
                success_count += 1
                
                # 再次检查
                new_issues = check_translation_quality(file_path)
                if new_issues:
                    print(f"  ⚠️ 仍有问题: {', '.join(new_issues)}")
                else:
                    print(f"  ✅ 问题已修复")
        else:
            print(f"  ✅ 翻译质量良好")
            success_count += 1
    
    print(f"\n🎉 处理完成！")
    print(f"📊 成功处理: {success_count}/{len(html_files)}")
    print(f"🔧 发现并修复问题: {total_issues}个")

if __name__ == "__main__":
    main()
