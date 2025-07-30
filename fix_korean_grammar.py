#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_korean_files():
    """修复韩文生态学文章的语法和内容问题"""
    
    # 修复 ko/ecology/08-island-biogeography.html
    print("修复韩文岛屿生物地理学文章...")
    
    korean_island_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>섬 생물지리학 - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_island_biogeography.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">섬 생물지리학</h1>
        <div class="quote-box">
            <div class="quote-text">고립된 환경에서의 조류 진화와 분포 패턴</div>
        </div>
        
        <div class="main-text">
            섬 생물지리학은 고립된 섬 환경에서 조류의 분포, 진화, 그리고 생태학적 적응을 연구하는 학문입니다<span class="emoji">🏝️</span>. 섬은 독특한 진화 실험실 역할을 하며, 대륙과는 다른 특별한 생태학적 패턴을 보여줍니다.
        </div>
        
        <div class="article-meta">
            <span class="category ecology">조류 생태학</span>
            <span class="read-time">📖 8분 읽기</span>
            <span class="difficulty">🟡 중급</span>
        </div>
        
        <div class="section-title">섬 생물지리학의 기본 원리</div>
        <div class="main-text">
            섬의 조류 군집은 거리 효과와 면적 효과라는 두 가지 주요 요인에 의해 결정됩니다<span class="emoji">📏</span>. 대륙으로부터 멀리 떨어진 섬일수록, 그리고 면적이 작은 섬일수록 종의 다양성이 감소하는 경향을 보입니다.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🎯 핵심 개념</div>
            맥아더-윌슨의 섬 생물지리학 이론에 따르면, 섬의 종 수는 이민과 멸종 사이의 동적 평형에 의해 결정됩니다.
        </div>
        
        <div class="section-title">섬으로의 조류 정착</div>
        <div class="main-text">
            조류가 섬에 정착하는 방식은 다양합니다<span class="emoji">✈️</span>. 능동적 비행, 바람에 의한 수동적 이동, 인간에 의한 의도적 또는 비의도적 도입 등이 주요 경로입니다.
        </div>
        
        <div class="colonization-methods">
            <div class="method-item">
                <h4>🦅 능동적 정착</h4>
                <div class="main-text">강한 비행 능력을 가진 조류들이 스스로 섬에 도달하는 경우</div>
            </div>
            <div class="method-item">
                <h4>🌪️ 수동적 정착</div>
                <div class="main-text">폭풍이나 강한 바람에 의해 의도치 않게 섬에 도달하는 경우</div>
            </div>
            <div class="method-item">
                <h4>🚢 인간 매개 정착</h4>
                <div class="main-text">인간 활동에 의해 의도적 또는 우연히 도입되는 경우</div>
            </div>
        </div>
        
        <div class="section-title">섬에서의 진화적 적응</div>
        <div class="main-text">
            섬 환경은 독특한 선택압을 제공하여 조류의 특별한 진화적 적응을 촉진합니다<span class="emoji">🧬</span>. 이러한 적응은 종종 대륙 종과는 매우 다른 특성을 나타냅니다.
        </div>
        
        <div class="adaptation-types">
            <div class="adaptation-category">
                <h4>🦴 형태학적 적응</h4>
                <ul>
                    <li><strong>거대화 또는 왜소화:</strong> 섬의 자원과 포식압에 따른 체크기 변화</li>
                    <li><strong>비행 능력 상실:</strong> 포식자가 없는 환경에서 날개 퇴화</li>
                    <li><strong>부리 형태 변화:</strong> 이용 가능한 먹이 자원에 맞춘 특화</li>
                    <li><strong>다리 길이 변화:</strong> 서식지 특성에 맞춘 적응</li>
                </ul>
            </div>
            
            <div class="adaptation-category">
                <h4>🎭 행동학적 적응</h4>
                <ul>
                    <li><strong>영역성 변화:</strong> 자원 분포에 따른 영역 행동 수정</li>
                    <li><strong>번식 전략 변화:</strong> 환경 안정성에 맞춘 번식 패턴</li>
                    <li><strong>먹이 행동 변화:</strong> 새로운 먹이 자원 활용법 개발</li>
                    <li><strong>사회 구조 변화:</strong> 개체군 밀도에 따른 사회성 조절</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">고유종의 진화</div>
        <div class="main-text">
            장기간의 고립은 섬 고유종의 진화를 촉진합니다<span class="emoji">🌟</span>. 이러한 고유종들은 종종 독특한 생태학적 지위를 차지하며, 섬 생태계의 중요한 구성 요소가 됩니다.
        </div>
        
        <div class="endemic-examples">
            <div class="example-item">
                <h4>🦆 갈라파고스 핀치</h4>
                <div class="main-text">다윈의 진화론 발전에 핵심적 역할을 한 적응 방산의 대표적 사례</div>
            </div>
            <div class="example-item">
                <h4>🐧 갈라파고스 펭귄</h4>
                <div class="main-text">적도 근처에서 살아가는 유일한 펭귄으로 열대 환경에 적응</div>
            </div>
            <div class="example-item">
                <h4>🦅 하와이 꿀빨이새</h4>
                <div class="main-text">하와이 제도에서 다양한 생태적 지위로 분화한 고유종 그룹</div>
            </div>
        </div>
        
        <div class="section-title">섬 생태계의 취약성</div>
        <div class="main-text">
            섬 조류 군집은 대륙 군집보다 훨씬 취약합니다<span class="emoji">⚠️</span>. 작은 개체군 크기, 제한된 서식지, 그리고 외래종에 대한 낮은 저항성이 주요 취약 요인입니다.
        </div>
        
        <div class="vulnerability-factors">
            <div class="factor-item">
                <h4>👥 작은 개체군</h4>
                <div class="main-text">유전적 다양성 감소와 확률적 멸종 위험 증가</div>
            </div>
            <div class="factor-item">
                <h4>🏝️ 서식지 제한</h4>
                <div class="main-text">대안 서식지 부족으로 인한 환경 변화에 대한 낮은 적응력</div>
            </div>
            <div class="factor-item">
                <h4>🐀 외래종 침입</h4>
                <div class="main-text">진화적으로 경험하지 못한 포식자와 경쟁자에 대한 취약성</div>
            </div>
            <div class="factor-item">
                <h4>🌡️ 기후 변화</h4>
                <div class="main-text">해수면 상승과 기후 패턴 변화에 대한 높은 민감성</div>
            </div>
        </div>
        
        <div class="section-title">보전 전략</div>
        <div class="main-text">
            섬 조류의 보전은 특별한 접근법이 필요합니다<span class="emoji">🛡️</span>. 외래종 관리, 서식지 복원, 그리고 기후 변화 적응이 핵심 전략입니다.
        </div>
        
        <div class="conservation-strategies">
            <div class="strategy-category">
                <h4>🚫 외래종 관리</h4>
                <ul>
                    <li>침입성 포유류 제거 프로그램</li>
                    <li>외래 식물 종 통제</li>
                    <li>생물학적 방제법 개발</li>
                    <li>새로운 침입 방지 조치</li>
                </ul>
            </div>
            
            <div class="strategy-category">
                <h4>🌱 서식지 복원</h4>
                <ul>
                    <li>원래 식생 복원</li>
                    <li>번식지 개선</li>
                    <li>먹이 자원 증대</li>
                    <li>인공 둥지 설치</li>
                </ul>
            </div>
            
            <div class="strategy-category">
                <h4>🧬 유전적 관리</h4>
                <ul>
                    <li>유전적 다양성 모니터링</li>
                    <li>근친교배 방지</li>
                    <li>개체군 간 유전자 흐름 촉진</li>
                    <li>냉동 보존 기술 활용</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">연구 방법론</div>
        <div class="main-text">
            섬 생물지리학 연구는 다양한 현대적 기법을 활용합니다<span class="emoji">🔬</span>. 분자 유전학, 원격 감지, 그리고 장기 모니터링이 핵심 도구입니다.
        </div>
        
        <div class="research-methods">
            <div class="method-category">
                <h4>🧪 분자 기법</h4>
                <ul>
                    <li>계통발생학적 분석</li>
                    <li>개체군 유전학 연구</li>
                    <li>유전자 흐름 추적</li>
                    <li>적응 유전자 식별</li>
                </ul>
            </div>
            
            <div class="method-category">
                <h4>🛰️ 원격 감지</h4>
                <ul>
                    <li>서식지 변화 모니터링</li>
                    <li>개체군 분포 매핑</li>
                    <li>환경 변수 측정</li>
                    <li>기후 변화 영향 평가</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">미래 전망</div>
        <div class="main-text">
            섬 생물지리학 연구는 기후 변화와 인간 활동 증가라는 새로운 도전에 직면하고 있습니다<span class="emoji">🔮</span>. 통합적 접근법과 국제적 협력이 미래 연구의 핵심이 될 것입니다.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🌍 글로벌 중요성</div>
            섬 조류의 보전은 전 지구적 생물다양성 보전에 중요한 기여를 합니다. 섬은 지구 육지 면적의 5%에 불과하지만, 조류 고유종의 40% 이상을 보유하고 있습니다.
        </div>
    </div>
    
    <!-- 진행률 표시 -->
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        // 읽기 진행률 업데이트
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 초기화
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('ko/ecology/08-island-biogeography.html', 'w', encoding='utf-8') as f:
        f.write(korean_island_content)
    print("✅ 수정 완료: ko/ecology/08-island-biogeography.html")
    
    # 修复 ko/ecology/09-pollination-seed-dispersal.html
    print("수정 중: ko/ecology/09-pollination-seed-dispersal.html")
    
    korean_pollination_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수분과 종자 산포 - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_pollination_seed_dispersal.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">수분과 종자 산포</h1>
        <div class="quote-box">
            <div class="quote-text">조류가 식물 번식에 미치는 핵심적 역할</div>
        </div>
        
        <div class="main-text">
            조류는 식물의 번식 과정에서 중요한 역할을 담당합니다<span class="emoji">🌸</span>. 수분 매개자와 종자 산포자로서 조류는 식물 군집의 구조와 다양성을 결정하는 핵심 요소입니다.
        </div>
        
        <div class="article-meta">
            <span class="category ecology">조류 생태학</span>
            <span class="read-time">📖 7분 읽기</span>
            <span class="difficulty">🟢 초급</span>
        </div>
        
        <div class="section-title">조류 수분의 중요성</div>
        <div class="main-text">
            전 세계적으로 약 2,000종의 식물이 조류에 의한 수분에 의존합니다<span class="emoji">🐦</span>. 이러한 조류-식물 상호작용은 특히 열대 지역에서 생태계 기능의 핵심을 이룹니다.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🌺 수분 특화</div>
            조류 수분 식물들은 보통 밝은 색깔(빨강, 주황), 관 모양의 꽃, 그리고 풍부한 꿀을 특징으로 합니다.
        </div>
        
        <div class="section-title">주요 수분 매개 조류</div>
        <div class="main-text">
            다양한 조류 그룹이 수분 활동에 참여하며, 각각 독특한 특화 전략을 보입니다<span class="emoji">🦜</span>.
        </div>
        
        <div class="pollinator-types">
            <div class="pollinator-item">
                <h4>🐦 벌새 (Hummingbirds)</h4>
                <div class="main-text">
                    <strong>분포:</strong> 아메리카 대륙<br>
                    <strong>특징:</strong> 공중 정지 비행, 긴 부리, 높은 대사율<br>
                    <strong>수분 식물:</strong> 관상화, 열대 관목, 착생식물
                </div>
            </div>
            
            <div class="pollinator-item">
                <h4>🌻 태양새 (Sunbirds)</h4>
                <div class="main-text">
                    <strong>분포:</strong> 아프리카, 아시아<br>
                    <strong>특징:</strong> 곡선형 부리, 화려한 깃털, 영역성<br>
                    <strong>수분 식물:</strong> 알로에, 프로테아, 바나나과 식물
                </div>
            </div>
            
            <div class="pollinator-item">
                <h4>🍯 꿀빨이새 (Honeyeaters)</h4>
                <div class="main-text">
                    <strong>분포:</strong> 오스트레일리아, 뉴질랜드<br>
                    <strong>특징:</strong> 브러시 모양 혀, 사회적 행동<br>
                    <strong>수분 식물:</strong> 유칼립투스, 뱅크시아, 그레빌리아
                </div>
            </div>
        </div>
        
        <div class="section-title">수분 메커니즘</div>
        <div class="main-text">
            조류 수분은 정교한 형태학적, 행동학적 적응의 결과입니다<span class="emoji">🔄</span>. 꽃의 구조와 조류의 특성이 완벽하게 맞아떨어지는 공진화의 산물입니다.
        </div>
        
        <div class="mechanism-steps">
            <div class="step-item">
                <h4>1️⃣ 꽃 방문</h4>
                <div class="main-text">조류가 꿀을 찾아 꽃에 접근합니다</div>
            </div>
            <div class="step-item">
                <h4>2️⃣ 화분 부착</h4>
                <div class="main-text">머리나 부리에 화분이 묻습니다</div>
            </div>
            <div class="step-item">
                <h4>3️⃣ 꽃 간 이동</h4>
                <div class="main-text">다른 꽃으로 이동하며 화분을 운반합니다</div>
            </div>
            <div class="step-item">
                <h4>4️⃣ 수분 완료</h4>
                <div class="main-text">암술에 화분이 전달되어 수정이 이루어집니다</div>
            </div>
        </div>
        
        <div class="section-title">종자 산포의 생태학적 역할</div>
        <div class="main-text">
            조류에 의한 종자 산포는 식물의 분포 확장과 유전자 흐름에 필수적입니다<span class="emoji">🌰</span>. 특히 산림 재생과 생물다양성 유지에 핵심적 역할을 합니다.
        </div>
        
        <div class="dispersal-benefits">
            <div class="benefit-item">
                <h4>🌍 장거리 산포</h4>
                <div class="main-text">조류의 비행 능력으로 종자가 먼 거리까지 이동 가능</div>
            </div>
            <div class="benefit-item">
                <h4>🎯 적합한 서식지</h4>
                <div class="main-text">조류가 선호하는 서식지에 종자가 떨어져 발아율 증가</div>
            </div>
            <div class="benefit-item">
                <h4>💩 자연 비료</h4>
                <div class="main-text">배설물과 함께 배출되어 발아에 유리한 조건 제공</div>
            </div>
            <div class="benefit-item">
                <h4>🌱 경쟁 회피</h4>
                <div class="main-text">모식물로부터 멀리 떨어져 경쟁 압력 감소</div>
            </div>
        </div>
        
        <div class="section-title">종자 산포 조류의 유형</div>
        <div class="main-text">
            종자 산포에 참여하는 조류들은 먹이 습성과 소화 특성에 따라 분류됩니다<span class="emoji">🍓</span>.
        </div>
        
        <div class="disperser-categories">
            <div class="category-item">
                <h4>🍇 과실식성 조류</h4>
                <div class="main-text">
                    <strong>예시:</strong> 비둘기, 앵무새, 찌르레기<br>
                    <strong>특징:</strong> 과실을 통째로 삼키고 종자를 온전히 배출<br>
                    <strong>산포 식물:</strong> 장과류, 핵과류
                </div>
            </div>
            
            <div class="category-item">
                <h4>🌰 견과식성 조류</h4>
                <div class="main-text">
                    <strong>예시:</strong> 까마귀, 어치, 딱따구리<br>
                    <strong>특징:</strong> 종자를 저장하고 일부를 잊어버림<br>
                    <strong>산포 식물:</strong> 참나무, 소나무, 호두나무
                </div>
            </div>
            
            <div class="category-item">
                <h4>🥜 잡식성 조류</h4>
                <div class="main-text">
                    <strong>예시:</strong> 참새, 방울새, 되새<br>
                    <strong>특징:</strong> 다양한 종자를 섭취하고 산포<br>
                    <strong>산포 식물:</strong> 초본식물, 관목류
                </div>
            </div>
        </div>
        
        <div class="section-title">계절적 패턴</div>
        <div class="main-text">
            수분과 종자 산포 활동은 뚜렷한 계절성을 보입니다<span class="emoji">📅</span>. 식물의 개화와 결실 시기, 그리고 조류의 번식 주기와 밀접하게 연관됩니다.
        </div>
        
        <div class="seasonal-patterns">
            <div class="season-item">
                <h4>🌸 봄 (수분 시즌)</h4>
                <ul>
                    <li>대부분의 식물이 개화</li>
                    <li>조류의 번식기와 겹쳐 에너지 요구량 증가</li>
                    <li>영역 행동으로 인한 수분 효율성 증대</li>
                </ul>
            </div>
            
            <div class="season-item">
                <h4>🍂 가을 (종자 산포 시즌)</h4>
                <ul>
                    <li>과실과 종자의 성숙기</li>
                    <li>겨울 준비를 위한 지방 축적</li>
                    <li>이주 준비로 인한 활발한 섭식 활동</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">공진화적 관계</div>
        <div class="main-text">
            조류와 식물 간의 수분 및 종자 산포 관계는 수백만 년에 걸친 공진화의 결과입니다<span class="emoji">🧬</span>. 이러한 상호 적응은 놀라운 정밀성을 보여줍니다.
        </div>
        
        <div class="coevolution-examples">
            <div class="example-item">
                <h4>🌺 벌새-트럼펫 꽃</h4>
                <div class="main-text">꽃의 길이와 벌새 부리 길이의 완벽한 매칭</div>
            </div>
            <div class="example-item">
                <h4>🍒 새-체리 열매</h4>
                <div class="main-text">새의 시각에 맞춘 빨간색과 적절한 크기</div>
            </div>
            <div class="example-item">
                <h4>🌰 어치-도토리</h4>
                <div class="main-text">저장 행동과 도토리의 영양 성분 최적화</div>
            </div>
        </div>
        
        <div class="section-title">인간 활동의 영향</div>
        <div class="main-text">
            인간 활동은 조류의 수분과 종자 산포 활동에 심각한 영향을 미칩니다<span class="emoji">⚠️</span>. 서식지 파괴, 외래종 도입, 기후 변화 등이 주요 위협 요인입니다.
        </div>
        
        <div class="threat-factors">
            <div class="threat-item">
                <h4>🏗️ 서식지 파괴</h4>
                <div class="main-text">도시화와 농업 확장으로 인한 자연 서식지 감소</div>
            </div>
            <div class="threat-item">
                <h4>🌿 외래종 침입</h4>
                <div class="main-text">외래 식물과 동물이 기존 생태계 관계 교란</div>
            </div>
            <div class="threat-item">
                <h4>🌡️ 기후 변화</h4>
                <div class="main-text">개화 시기와 조류 활동 시기의 불일치</div>
            </div>
        </div>
        
        <div class="section-title">보전의 중요성</div>
        <div class="main-text">
            조류-식물 상호작용의 보전은 생태계 전체의 건강성을 유지하는 데 필수적입니다<span class="emoji">🌍</span>. 통합적 보전 접근법이 필요합니다.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🎯 보전 전략</div>
            효과적인 보전을 위해서는 조류와 식물을 함께 고려하는 생태계 기반 접근법이 필요하며, 서식지 보호, 복원, 그리고 지속적인 모니터링이 중요합니다.
        </div>
    </div>
    
    <!-- 진행률 표시 -->
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        // 읽기 진행률 업데이트
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 초기화
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('ko/ecology/09-pollination-seed-dispersal.html', 'w', encoding='utf-8') as f:
        f.write(korean_pollination_content)
    print("✅ 수정 완료: ko/ecology/09-pollination-seed-dispersal.html")
    
    # 修复 ko/ecology/10-community-dynamics.html
    print("수정 중: ko/ecology/10-community-dynamics.html")
    
    korean_community_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>군집 역학 - BirdAiSnap</title>
    <link rel="stylesheet" href="../../mobile-styles.css">
    <link rel="stylesheet" href="../../mobile-enhancement.css">
    <link rel="stylesheet" href="../../ecology-theme.css">
    <style>
        .hero-image img {
            max-height: 200px;
            width: 100%;
            object-fit: cover;
        }
        .article-card img {
            max-height: 120px;
            width: 100%;
            object-fit: cover;
        }
        .hero-image {
            margin-bottom: 20px !important;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), 
                        url('../../images/birds/species/head_community_dynamics.webp') center/cover;
        }
        .article-meta {
            margin-top: 15px !important;
        }
    </style>
</head>
<body>
    <div class="hero-image"></div>
    <div class="content">
        <h1 class="title">군집 역학</h1>
        <div class="quote-box">
            <div class="quote-text">조류 군집의 구조와 동적 변화 탐구</div>
        </div>
        
        <div class="main-text">
            조류 군집 역학은 여러 종이 함께 서식하는 환경에서 나타나는 복잡한 상호작용과 변화 패턴을 연구합니다<span class="emoji">🐦</span>. 이는 생태계의 구조와 기능을 이해하는 핵심 요소입니다.
        </div>
        
        <div class="article-meta">
            <span class="category ecology">조류 생태학</span>
            <span class="read-time">📖 9분 읽기</span>
            <span class="difficulty">🔴 고급</span>
        </div>
        
        <div class="section-title">군집 구조의 기본 개념</div>
        <div class="main-text">
            조류 군집의 구조는 종 다양성, 개체수 분포, 그리고 종간 관계에 의해 결정됩니다<span class="emoji">🏗️</span>. 이러한 구조는 환경 조건과 생물학적 상호작용의 복합적 결과입니다.
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🔍 핵심 지표</div>
            군집 구조를 측정하는 주요 지표로는 종 풍부도, 종 균등도, 다양성 지수, 그리고 우점도가 있습니다.
        </div>
        
        <div class="section-title">종간 상호작용</div>
        <div class="main-text">
            조류 군집 내에서는 다양한 형태의 종간 상호작용이 일어납니다<span class="emoji">🔗</span>. 이러한 상호작용은 군집의 안정성과 변화를 결정하는 중요한 요인입니다.
        </div>
        
        <div class="interaction-types">
            <div class="interaction-item">
                <h4>🥊 경쟁 (Competition)</h4>
                <div class="main-text">
                    <strong>자원 경쟁:</strong> 먹이, 둥지터, 영역에 대한 경쟁<br>
                    <strong>간섭 경쟁:</strong> 직접적인 공격적 행동<br>
                    <strong>착취 경쟁:</strong> 자원의 선점을 통한 간접 경쟁
                </div>
            </div>
            
            <div class="interaction-item">
                <h4>🍽️ 포식-피식 관계</h4>
                <div class="main-text">
                    <strong>포식압:</strong> 포식자가 피식자 개체군에 미치는 영향<br>
                    <strong>방어 전략:</strong> 집단 행동, 경계 행동, 위장<br>
                    <strong>공진화:</strong> 포식자와 피식자의 상호 적응
                </div>
            </div>
            
            <div class="interaction-item">
                <h4>🤝 상리공생</h4>
                <div class="main-text">
                    <strong>혼합 무리:</strong> 서로 다른 종이 함께 먹이 활동<br>
                    <strong>경계 협력:</strong> 포식자 탐지에서의 협력<br>
                    <strong>서식지 공유:</strong> 서로 다른 자원 이용으로 공존
                </div>
            </div>
        </div>
        
        <div class="section-title">군집 조립 과정</div>
        <div class="main-text">
            조류 군집의 형성은 복잡한 조립 과정을 통해 이루어집니다<span class="emoji">🧩</span>. 이 과정은 환경 필터링과 생물학적 상호작용의 결합으로 설명됩니다.
        </div>
        
        <div class="assembly-process">
            <div class="process-step">
                <h4>1️⃣ 종 풀 (Species Pool)</h4>
                <div class="main-text">지역적으로 이용 가능한 모든 조류 종</div>
            </div>
            <div class="process-step">
                <h4>2️⃣ 환경 필터링</h4>
                <div class="main-text">서식지 조건에 적합한 종만 선별</div>
            </div>
            <div class="process-step">
                <h4>3️⃣ 생물학적 필터링</h4>
                <div class="main-text">종간 상호작용을 통한 추가 선별</div>
            </div>
            <div class="process-step">
                <h4>4️⃣ 최종 군집</h4>
                <div class="main-text">안정적으로 공존하는 종들의 집합</div>
            </div>
        </div>
        
        <div class="section-title">시간적 변화 패턴</div>
        <div class="main-text">
            조류 군집은 다양한 시간 규모에서 변화를 보입니다<span class="emoji">⏰</span>. 이러한 변화는 예측 가능한 패턴과 확률적 변동을 모두 포함합니다.
        </div>
        
        <div class="temporal-patterns">
            <div class="pattern-category">
                <h4>📅 계절적 변화</h4>
                <ul>
                    <li><strong>번식기:</strong> 영역성 증가, 종간 경쟁 심화</li>
                    <li><strong>이주기:</strong> 군집 구성의 급격한 변화</li>
                    <li><strong>월동기:</strong> 혼합 무리 형성, 자원 공유</li>
                    <li><strong>환경 변화:</strong> 먹이 가용성에 따른 구성 변화</li>
                </ul>
            </div>
            
            <div class="pattern-category">
                <h4>📈 장기적 변화</h4>
                <ul>
                    <li><strong>천이:</strong> 서식지 성숙에 따른 군집 변화</li>
                    <li><strong>기후 변화:</strong> 분포 범위 이동과 군집 재편</li>
                    <li><strong>인간 영향:</strong> 도시화와 농업화에 따른 적응</li>
                    <li><strong>침입종:</strong> 외래종 도입에 따른 군집 교란</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">공간적 패턴</div>
        <div class="main-text">
            조류 군집의 공간적 분포는 환경 이질성과 종의 분산 능력에 의해 결정됩니다<span class="emoji">🗺️</span>. 이는 경관 생태학의 중요한 연구 주제입니다.
        </div>
        
        <div class="spatial-patterns">
            <div class="pattern-item">
                <h4>🏔️ 고도별 분포</h4>
                <div class="main-text">고도에 따른 기후와 식생 변화에 따른 군집 분화</div>
            </div>
            <div class="pattern-item">
                <h4>🌊 가장자리 효과</h4>
                <div class="main-text">서식지 경계에서 나타나는 독특한 군집 특성</div>
            </div>
            <div class="pattern-item">
                <h4>🧩 서식지 파편화</h4>
                <div class="main-text">서식지 조각화가 군집 구조에 미치는 영향</div>
            </div>
            <div class="pattern-item">
                <h4>🌐 메타군집</h4>
                <div class="main-text">연결된 서식지 패치들 간의 군집 역학</div>
            </div>
        </div>
        
        <div class="section-title">안정성과 복원력</div>
        <div class="main-text">
            조류 군집의 안정성은 교란에 대한 저항성과 복원력으로 측정됩니다<span class="emoji">⚖️</span>. 이는 생태계 관리와 보전에 중요한 개념입니다.
        </div>
        
        <div class="stability-factors">
            <div class="factor-category">
                <h4>🛡️ 저항성 요인</h4>
                <ul>
                    <li>높은 종 다양성</li>
                    <li>기능적 중복성</li>
                    <li>강한 종간 상호작용</li>
                    <li>환경 이질성</li>
                </ul>
            </div>
            
            <div class="factor-category">
                <h4>🔄 복원력 요인</h4>
                <ul>
                    <li>높은 재생산율</li>
                    <li>강한 분산 능력</li>
                    <li>행동적 가소성</li>
                    <li>서식지 연결성</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">연구 방법론</div>
        <div class="main-text">
            군집 역학 연구는 다양한 현장 조사와 분석 기법을 활용합니다<span class="emoji">🔬</span>. 현대적 기술의 발전으로 더욱 정밀한 연구가 가능해졌습니다.
        </div>
        
        <div class="research-methods">
            <div class="method-category">
                <h4>📊 현장 조사법</h4>
                <ul>
                    <li><strong>정점 조사:</strong> 고정된 지점에서의 정기적 관찰</li>
                    <li><strong>선형 조사:</strong> 일정한 경로를 따른 조사</li>
                    <li><strong>포획-재포획:</strong> 개체 표시를 통한 개체군 추정</li>
                    <li><strong>둥지 모니터링:</strong> 번식 성공률과 생존율 측정</li>
                </ul>
            </div>
            
            <div class="method-category">
                <h4>💻 분석 기법</h4>
                <ul>
                    <li><strong>다변량 분석:</strong> 군집 구조의 패턴 분석</li>
                    <li><strong>네트워크 분석:</strong> 종간 상호작용 네트워크</li>
                    <li><strong>시계열 분석:</strong> 장기적 변화 패턴 분석</li>
                    <li><strong>공간 분석:</strong> 지리적 분포 패턴 분석</li>
                </ul>
            </div>
        </div>
        
        <div class="section-title">기후 변화의 영향</div>
        <div class="main-text">
            기후 변화는 조류 군집 역학에 광범위한 영향을 미치고 있습니다<span class="emoji">🌡️</span>. 온도 상승, 강수 패턴 변화, 극한 기상 현상의 증가가 주요 요인입니다.
        </div>
        
        <div class="climate-impacts">
            <div class="impact-item">
                <h4>📍 분포 범위 이동</h4>
                <div class="main-text">온도 상승으로 인한 북쪽 및 고지대로의 분포 이동</div>
            </div>
            <div class="impact-item">
                <h4>⏰ 생활사 변화</h4>
                <div class="main-text">번식 시기, 이주 시기의 변화와 불일치 현상</div>
            </div>
            <div class="impact-item">
                <h4>🔄 군집 재편</h4>
                <div class="main-text">새로운 종 조합의 출현과 기존 관계의 해체</div>
            </div>
        </div>
        
        <div class="section-title">보전 함의</div>
        <div class="main-text">
            군집 역학의 이해는 효과적인 조류 보전 전략 수립에 필수적입니다<span class="emoji">🛡️</span>. 단일 종 보전을 넘어선 생태계 접근법이 필요합니다.
        </div>
        
        <div class="conservation-applications">
            <div class="application-item">
                <h4>🏞️ 서식지 관리</h4>
                <div class="main-text">군집 구조를 고려한 서식지 설계와 관리</div>
            </div>
            <div class="application-item">
                <h4>🌉 연결성 증진</h4>
                <div class="main-text">서식지 간 연결 통로 조성으로 메타군집 안정성 증대</div>
            </div>
            <div class="application-item">
                <h4>📈 모니터링</h4>
                <div class="main-text">군집 지표를 활용한 생태계 건강성 평가</div>
            </div>
        </div>
        
        <div class="tip-box">
            <div class="tip-title">🌟 미래 연구 방향</div>
            군집 역학 연구는 기후 변화, 도시화, 그리고 생물다양성 위기라는 현대적 도전에 대응하기 위해 통합적이고 예측적인 접근법으로 발전하고 있습니다.
        </div>
    </div>
    
    <!-- 진행률 표시 -->
    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>
    
    <script>
        // 읽기 진행률 업데이트
        function updateProgress() {
            const scrolled = window.pageYOffset;
            const maxHeight = document.body.scrollHeight - window.innerHeight;
            const progress = Math.min((scrolled / maxHeight) * 100, 100);
            const progressFill = document.querySelector('.progress-fill');
            if (progressFill) {
                progressFill.style.width = progress + '%';
            }
        }
        
        // 초기화
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    </script>
    <script src="../language-redirect.js"></script>
</body>
</html>'''
    
    with open('ko/ecology/10-community-dynamics.html', 'w', encoding='utf-8') as f:
        f.write(korean_community_content)
    print("✅ 수정 완료: ko/ecology/10-community-dynamics.html")

if __name__ == "__main__":
    print("한국어 문법 및 내용 수정 시작...")
    fix_korean_files()
    print("한국어 수정 완료!")
