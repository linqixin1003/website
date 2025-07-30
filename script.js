// 语言配置和翻译内容
const languages = {
    'en': { 
        name: 'English', 
        flag: '🇺🇸', 
        code: 'EN',
        translations: {
            'nav.home': 'Home',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
            'mockup.ai': 'AI Enhance',
            'mockup.scan': 'Scan',
            'mockup.sound': 'Sound',
            'features.title': 'Core Features',
            'features.scan.title': 'Capture & Identify',
            'features.scan.desc': 'Simply capture a photograph or upload an existing image to instantly identify bird species with precision',
            'features.sound.title': 'Acoustic Recognition',
            'features.sound.desc': 'Record avian vocalizations and identify species through sophisticated AI acoustic analysis',
            'features.nearby.title': 'Local Avian Species',
            'features.nearby.desc': 'Discover bird species in your vicinity and explore regional ecological patterns',
            'features.enhance.title': 'Intelligent Enhancement',
            'features.enhance.desc': 'Utilize advanced AI algorithms to enhance photographic quality and showcase avian subjects with stunning clarity',
            'features.collection.title': 'Personal Collections',
            'features.collection.desc': 'Curate personalized avian collections and document every birdwatching expedition with detailed records',
            'features.info.title': 'Comprehensive Database',
            'features.info.desc': 'Access extensive ornithological information and scientific knowledge repositories anytime, anywhere',
            'features.knowledge.title': 'Ornithological Insights',
            'features.knowledge.desc': 'Explore comprehensive birdwatching guides, scientific discoveries, avian care, ecological relationships, and cultural significance',
            'about.title': 'About BirdAiSnap',
            'about.desc1': 'BirdAiSnap is an intelligent recognition application designed specifically for avian enthusiasts and nature explorers. We are dedicated to helping users develop deeper understanding and appreciation for the magnificent birds in nature through cutting-edge AI technology.',
            'about.desc2': 'Whether you are a professional ornithologist or an inquisitive nature enthusiast, BirdAiSnap delivers precise and rapid bird identification services tailored to your needs.',
            'about.stats.downloads': 'Downloads',
            'about.stats.species': 'Bird Species',
            'about.stats.accuracy': 'Accuracy Rate',
            'contact.title': 'Contact Us',
            'contact.subtitle': 'Get More Information',
            'contact.desc': 'If you have any questions or suggestions, feel free to contact us',
            'contact.email': 'Email:',
            'contact.form.name': 'Your Name',
            'contact.form.email': 'Your Email',
            'contact.form.message': 'Your Message',
            'contact.form.submit': 'Send Message',
            'contact.email.title': '📧 Email Information',
            'contact.email.recipient': 'Recipient:',
            'contact.email.subject': 'Subject:',
            'contact.email.content': 'Content:',
            'contact.email.copy': 'Copy Email Information',
            'contact.email.open': 'Open Email Client',
            'footer.tagline': 'Smart Recognition, Explore Nature',
            'footer.product': 'Product',
            'footer.product.download': 'Download APP',
            'footer.product.features': 'Features',
            'footer.product.guide': 'User Guide',
            'footer.support': 'Support',
            'footer.support.help': 'Help Center',
            'footer.support.feedback': 'Feedback',
            'footer.support.privacy': 'Privacy Policy',
            'footer.contact': 'Contact Us',
            'footer.contact.email': 'Email Consultation',
            'footer.copyright': '© 2024 BirdAiSnap. All rights reserved',
            'knowledge.hero.title': 'Bird Knowledge Center',
            'knowledge.hero.description': 'Explore the fascinating world of birds through comprehensive knowledge resources',
            'knowledge.categories.birdwatching': 'Bird Watching',
            'knowledge.categories.birdwatching.desc': 'Learn the art of bird observation and identification techniques',
            'knowledge.categories.scientific': 'Scientific Wonders',
            'knowledge.categories.scientific.desc': 'Discover amazing scientific facts and research about birds',
            'knowledge.categories.petcare': 'Pet Bird Care',
            'knowledge.categories.petcare.desc': 'Essential care guides for pet bird owners and enthusiasts',
            'knowledge.categories.ecology': 'Bird Ecology',
            'knowledge.categories.ecology.desc': 'Understanding bird habitats, migration, and environmental roles',
            'knowledge.categories.cultural': 'Cultural Symbolism',
            'knowledge.categories.cultural.desc': 'Birds in mythology, art, literature, and cultural significance',
            'knowledge.latest.title': 'Latest Articles',
            'knowledge.articles.stats': 'Articles',
            'birdwatching.title': 'Birdwatching Guide - BirdAiSnap',
            'birdwatching.header.title': 'Birdwatching Guide',
            'birdwatching.intro.text': 'Welcome to our comprehensive birdwatching guide section. Here you\'ll find extensive birdwatching techniques and knowledge, from beginner basics to advanced identification skills, helping you better appreciate and understand the world of birds. Click on any article image below to dive deep into the mysteries of birdwatching.',
            'birdwatching.articles.getting-started.title': 'Getting Started Guide',
            'birdwatching.articles.getting-started.desc': 'Comprehensive birdwatching introduction for beginners',
            'birdwatching.articles.essential-equipment.title': 'Essential Equipment',
            'birdwatching.articles.essential-equipment.desc': 'Learn about various tools and equipment needed for birdwatching',
            'birdwatching.articles.identification-techniques.title': 'Identification Techniques',
            'birdwatching.articles.identification-techniques.desc': 'Master the art and methods of bird identification',
            'birdwatching.articles.best-locations.title': 'Best Locations',
            'birdwatching.articles.best-locations.desc': 'Explore birdwatching hotspots around the world',
            'birdwatching.articles.seasonal-guide.title': 'Seasonal Guide',
            'birdwatching.articles.seasonal-guide.desc': 'Plan your birdwatching activities according to seasonal changes',
            'birdwatching.articles.photography-tips.title': 'Photography Tips',
            'birdwatching.articles.photography-tips.desc': 'Practical advice for capturing stunning bird photographs',
            'birdwatching.articles.behavior-observation.title': 'Behavior Observation',
            'birdwatching.articles.behavior-observation.desc': 'Learn to observe and understand bird behavior',
            'birdwatching.articles.song-identification.title': 'Song Identification',
            'birdwatching.articles.song-identification.desc': 'Techniques for identifying different bird species by sound',
            'birdwatching.articles.ethics-conservation.title': 'Ethics & Conservation',
            'birdwatching.articles.ethics-conservation.desc': 'Responsible birdwatching and contributing to bird conservation',
            'birdwatching.articles.journal-keeping.title': 'Journal Keeping',
            'birdwatching.articles.journal-keeping.desc': 'How to record and organize your birdwatching experiences',
            'ecology.title': 'Bird Ecology - BirdAiSnap',
            'ecology.header.title': 'Bird Ecology',
            'ecology.intro.text': 'Explore the complex and fascinating relationships between birds and their environment. Bird ecology studies how birds adapt to different habitats, their roles in ecosystems, and the impact of environmental changes on bird populations. Understanding these ecological relationships helps us better protect birds and their habitats.',
            'ecology.articles.habitat-ecosystems.title': 'Habitats & Ecosystems',
            'ecology.articles.habitat-ecosystems.desc': 'Understanding the diversity of bird habitats and ecosystem functions',
            'ecology.articles.food-webs-chains.title': 'Food Webs & Chains',
            'ecology.articles.food-webs-chains.desc': 'Exploring the important position and role of birds in food webs',
            'ecology.articles.migration-patterns.title': 'Migration Patterns',
            'ecology.articles.migration-patterns.desc': 'Studying the complex patterns and ecological significance of bird migration',
            'ecology.articles.breeding-ecology.title': 'Breeding Ecology',
            'ecology.articles.breeding-ecology.desc': 'Understanding bird breeding behavior and ecological strategies',
            'ecology.articles.climate-change-impact.title': 'Climate Change Impact',
            'ecology.articles.climate-change-impact.desc': 'Analyzing the profound impact of climate change on bird ecology',
            'ecology.articles.urban-ecology.title': 'Urban Ecology',
            'ecology.articles.urban-ecology.desc': 'Exploring how birds adapt to urban environments',
            'ecology.articles.conservation-biology.title': 'Conservation Biology',
            'ecology.articles.conservation-biology.desc': 'Learning the scientific principles and practical methods of bird conservation',
            'ecology.articles.island-biogeography.title': 'Island Biogeography',
            'ecology.articles.island-biogeography.desc': 'Studying bird distribution and evolution in island environments',
            'ecology.articles.pollination-seed-dispersal.title': 'Pollination & Seed Dispersal',
            'ecology.articles.pollination-seed-dispersal.desc': 'Understanding the important role of birds in plant reproduction',
            'ecology.articles.community-dynamics.title': 'Community Dynamics',
            'ecology.articles.community-dynamics.desc': 'Exploring the structure and dynamic changes of bird communities'
        }
    },
    'zh': { 
        name: '中文', 
        flag: '🇨🇳', 
        code: 'ZH',
        translations: {
            'nav.home': '首页',
            'nav.features': '功能特色',
            'nav.about': '关于我们',
            'nav.contact': '联系我们',
            'hero.title': '智能识别，拍摄发现',
            'hero.description': 'BirdAiSnap是一款AI驱动的智能识别应用，帮助您快速识别周围的鸟类，探索自然世界的奥秘。',
            'hero.download': '立即下载',
            'hero.learn': '了解更多',
            'mockup.ai': 'AI增强',
            'mockup.scan': '扫描',
            'mockup.sound': '声音',
            'features.title': '核心功能',
            'features.scan.title': '拍摄识别',
            'features.scan.desc': '只需拍摄照片或上传现有图像，即可精确识别鸟类物种',
            'features.sound.title': '声音识别',
            'features.sound.desc': '录制鸟类叫声，通过先进的AI声学分析识别物种',
            'features.nearby.title': '附近鸟类',
            'features.nearby.desc': '发现您附近的鸟类物种，探索区域生态模式',
            'features.enhance.title': '智能增强',
            'features.enhance.desc': '利用先进的AI算法增强照片质量，以惊人的清晰度展示鸟类主体',
            'features.collection.title': '个人收藏',
            'features.collection.desc': '策划个性化的鸟类收藏，详细记录每次观鸟探险',
            'features.info.title': '综合数据库',
            'features.info.desc': '随时随地访问广泛的鸟类学信息和科学知识库',
            'features.knowledge.title': '鸟类学洞察',
            'features.knowledge.desc': '探索全面的观鸟指南、科学发现、鸟类护理、生态关系和文化意义',
            'about.title': '关于BirdAiSnap',
            'about.desc1': 'BirdAiSnap是专为鸟类爱好者和自然探索者设计的智能识别应用。我们致力于通过尖端AI技术帮助用户更深入地理解和欣赏自然界中的美丽鸟类。',
            'about.desc2': '无论您是专业鸟类学家还是好奇的自然爱好者，BirdAiSnap都能提供精确快速的鸟类识别服务。',
            'about.stats.downloads': '下载量',
            'about.stats.species': '鸟类物种',
            'about.stats.accuracy': '准确率',
            'contact.title': '联系我们',
            'contact.subtitle': '获取更多信息',
            'contact.desc': '如果您有任何问题或建议，请随时联系我们',
            'contact.email': '邮箱：',
            'contact.form.name': '您的姓名',
            'contact.form.email': '您的邮箱',
            'contact.form.message': '您的留言',
            'contact.form.submit': '发送消息',
            'contact.email.title': '📧 邮件信息',
            'contact.email.recipient': '收件人：',
            'contact.email.subject': '主题：',
            'contact.email.content': '内容：',
            'contact.email.copy': '复制邮件信息',
            'contact.email.open': '打开邮件客户端',
            'footer.tagline': '智能识别，探索自然',
            'footer.product': '产品',
            'footer.product.download': '下载应用',
            'footer.product.features': '功能特色',
            'footer.product.guide': '使用指南',
            'footer.support': '支持',
            'footer.support.help': '帮助中心',
            'footer.support.feedback': '意见反馈',
            'footer.support.privacy': '隐私政策',
            'footer.contact': '联系我们',
            'footer.contact.email': '邮件咨询',
            'footer.copyright': '© 2024 BirdAiSnap. 保留所有权利',
            'knowledge.hero.title': '鸟类知识中心',
            'knowledge.hero.description': '通过全面的知识资源探索鸟类的迷人世界',
            'knowledge.categories.birdwatching': '观鸟指南',
            'knowledge.categories.birdwatching.desc': '学习鸟类观察和识别技巧的艺术',
            'knowledge.categories.scientific': '科学奇观',
            'knowledge.categories.scientific.desc': '发现关于鸟类的惊人科学事实和研究',
            'knowledge.categories.petcare': '宠物鸟护理',
            'knowledge.categories.petcare.desc': '为宠物鸟主人和爱好者提供的基本护理指南',
            'knowledge.categories.ecology': '鸟类生态学',
            'knowledge.categories.ecology.desc': '了解鸟类栖息地、迁徙和环境作用',
            'knowledge.categories.cultural': '文化象征',
            'knowledge.categories.cultural.desc': '鸟类在神话、艺术、文学和文化意义中的体现',
            'knowledge.latest.title': '最新文章',
            'knowledge.articles.stats': '篇文章',
            'birdwatching.title': '观鸟指南 - BirdAiSnap',
            'birdwatching.header.title': '观鸟指南',
            'birdwatching.intro.text': '欢迎来到我们的观鸟指南专区。这里提供了全面的观鸟技巧和知识，从入门基础到高级识别技术，帮助您更好地欣赏和了解鸟类世界。点击下方任意文章图片，深入探索观鸟的奥秘。',
            'birdwatching.articles.getting-started.title': '观鸟入门指南',
            'birdwatching.articles.getting-started.desc': '为初学者提供的全面观鸟介绍',
            'birdwatching.articles.essential-equipment.title': '观鸟必备装备',
            'birdwatching.articles.essential-equipment.desc': '了解观鸟所需的各种工具和装备',
            'birdwatching.articles.identification-techniques.title': '鸟类识别技巧',
            'birdwatching.articles.identification-techniques.desc': '掌握鸟类识别的艺术和方法',
            'birdwatching.articles.best-locations.title': '最佳观鸟地点',
            'birdwatching.articles.best-locations.desc': '探索世界各地的观鸟胜地',
            'birdwatching.articles.seasonal-guide.title': '季节性观鸟指南',
            'birdwatching.articles.seasonal-guide.desc': '根据季节变化规划您的观鸟活动',
            'birdwatching.articles.photography-tips.title': '鸟类摄影技巧',
            'birdwatching.articles.photography-tips.desc': '拍摄精彩鸟类照片的实用建议',
            'birdwatching.articles.behavior-observation.title': '鸟类行为观察',
            'birdwatching.articles.behavior-observation.desc': '学习观察和理解鸟类行为',
            'birdwatching.articles.song-identification.title': '鸟鸣识别',
            'birdwatching.articles.song-identification.desc': '通过声音识别不同鸟类的技巧',
            'birdwatching.articles.ethics-conservation.title': '观鸟伦理与保护',
            'birdwatching.articles.ethics-conservation.desc': '负责任地观鸟并为鸟类保护做贡献',
            'birdwatching.articles.journal-keeping.title': '观鸟日志记录',
            'birdwatching.articles.journal-keeping.desc': '如何记录和整理您的观鸟经历',
            'ecology.title': '鸟类生态学 - BirdAiSnap',
            'ecology.header.title': '鸟类生态学',
            'ecology.intro.text': '探索鸟类与环境之间复杂而迷人的关系。鸟类生态学研究鸟类如何适应不同的栖息地、它们在生态系统中的作用，以及环境变化对鸟类种群的影响。了解这些生态关系有助于我们更好地保护鸟类及其栖息地。',
            'ecology.articles.habitat-ecosystems.title': '栖息地与生态系统',
            'ecology.articles.habitat-ecosystems.desc': '了解鸟类栖息地的多样性和生态系统功能',
            'ecology.articles.food-webs-chains.title': '食物网与食物链',
            'ecology.articles.food-webs-chains.desc': '探索鸟类在食物网中的重要地位和作用',
            'ecology.articles.migration-patterns.title': '迁徙模式',
            'ecology.articles.migration-patterns.desc': '研究鸟类迁徙的复杂模式和生态意义',
            'ecology.articles.breeding-ecology.title': '繁殖生态学',
            'ecology.articles.breeding-ecology.desc': '了解鸟类繁殖行为和生态策略',
            'ecology.articles.climate-change-impact.title': '气候变化影响',
            'ecology.articles.climate-change-impact.desc': '分析气候变化对鸟类生态的深远影响',
            'ecology.articles.urban-ecology.title': '城市生态学',
            'ecology.articles.urban-ecology.desc': '探索鸟类如何适应城市环境',
            'ecology.articles.conservation-biology.title': '保护生物学',
            'ecology.articles.conservation-biology.desc': '学习鸟类保护的科学原理和实践方法',
            'ecology.articles.island-biogeography.title': '岛屿生物地理学',
            'ecology.articles.island-biogeography.desc': '研究岛屿环境中的鸟类分布和进化',
            'ecology.articles.pollination-seed-dispersal.title': '授粉与种子传播',
            'ecology.articles.pollination-seed-dispersal.desc': '了解鸟类在植物繁殖中的重要作用',
            'ecology.articles.community-dynamics.title': '群落动态',
            'ecology.articles.community-dynamics.desc': '探索鸟类群落的结构和动态变化'
        }
    },
    'ko': { 
        name: '한국어', 
        flag: '🇰🇷', 
        code: 'KO',
        translations: {
            'nav.home': '홈페이지',
            'nav.features': '기능',
            'nav.about': '소개',
            'nav.contact': '연락처',
            'hero.title': '지능형 인식, 촬영 및 발견',
            'hero.description': 'BirdAiSnap은 AI 기반 지능형 인식 애플리케이션으로, 주변 조류를 빠르게 식별하고 자연 세계의 신비를 탐구할 수 있게 해줍니다.',
            'hero.download': '지금 다운로드',
            'hero.learn': '더 알아보기',
            'mockup.ai': 'AI 향상',
            'mockup.scan': '스캔',
            'mockup.sound': '소리',
            'features.title': '핵심 기능',
            'features.scan.title': '촬영 및 식별',
            'features.scan.desc': '사진을 촬영하거나 기존 이미지를 업로드하여 조류 종을 정확하게 식별하세요',
            'features.sound.title': '음향 인식',
            'features.sound.desc': '조류 울음소리를 녹음하고 정교한 AI 음향 분석을 통해 종을 식별하세요',
            'features.nearby.title': '지역 조류 종',
            'features.nearby.desc': '주변 조류 종을 발견하고 지역 생태 패턴을 탐구하세요',
            'features.enhance.title': '지능형 향상',
            'features.enhance.desc': '고급 AI 알고리즘을 활용하여 사진 품질을 향상시키고 놀라운 선명도로 조류를 보여주세요',
            'features.collection.title': '개인 컬렉션',
            'features.collection.desc': '개인화된 조류 컬렉션을 큐레이션하고 모든 조류 관찰 탐험을 자세히 기록하세요',
            'features.info.title': '종합 데이터베이스',
            'features.info.desc': '언제 어디서나 광범위한 조류학 정보와 과학 지식 저장소에 액세스하세요',
            'features.knowledge.title': '조류학 통찰',
            'features.knowledge.desc': '포괄적인 조류 관찰 가이드, 과학적 발견, 조류 관리, 생태 관계 및 문화적 의미를 탐구하세요',
            'about.title': 'BirdAiSnap 소개',
            'about.desc1': 'BirdAiSnap은 조류 애호가와 자연 탐험가를 위해 특별히 설계된 지능형 인식 애플리케이션입니다. 우리는 최첨단 AI 기술을 통해 사용자가 자연의 아름다운 새들을 더 깊이 이해하고 감상할 수 있도록 돕는 데 전념하고 있습니다.',
            'about.desc2': '전문 조류학자든 호기심 많은 자연 애호가든, BirdAiSnap은 정확하고 빠른 조류 식별 서비스를 제공합니다.',
            'about.stats.downloads': '다운로드',
            'about.stats.species': '조류 종',
            'about.stats.accuracy': '정확도',
            'contact.title': '연락처',
            'contact.subtitle': '더 많은 정보 얻기',
            'contact.desc': '질문이나 제안이 있으시면 언제든지 연락해 주세요',
            'contact.email': '이메일:',
            'contact.form.name': '성함',
            'contact.form.email': '이메일',
            'contact.form.message': '메시지',
            'contact.form.submit': '메시지 보내기',
            'contact.email.title': '📧 이메일 정보',
            'contact.email.recipient': '수신자:',
            'contact.email.subject': '제목:',
            'contact.email.content': '내용:',
            'contact.email.copy': '이메일 정보 복사',
            'contact.email.open': '이메일 클라이언트 열기',
            'footer.tagline': '스마트 인식, 자연 탐구',
            'footer.product': '제품',
            'footer.product.download': '앱 다운로드',
            'footer.product.features': '기능',
            'footer.product.guide': '사용자 가이드',
            'footer.support': '지원',
            'footer.support.help': '도움말 센터',
            'footer.support.feedback': '피드백',
            'footer.support.privacy': '개인정보 보호정책',
            'footer.contact': '연락처',
            'footer.contact.email': '이메일 상담',
            'footer.copyright': '© 2024 BirdAiSnap. 모든 권리 보유',
            'knowledge.hero.title': '조류 지식 센터',
            'knowledge.hero.description': '포괄적인 지식 자원을 통해 새들의 매혹적인 세계를 탐험하세요',
            'knowledge.categories.birdwatching': '조류 관찰',
            'knowledge.categories.birdwatching.desc': '조류 관찰과 식별 기술의 예술을 배우세요',
            'knowledge.categories.scientific': '과학적 경이',
            'knowledge.categories.scientific.desc': '조류에 대한 놀라운 과학적 사실과 연구를 발견하세요',
            'knowledge.categories.petcare': '애완조 관리',
            'knowledge.categories.petcare.desc': '애완조 주인과 애호가를 위한 필수 관리 가이드',
            'knowledge.categories.ecology': '조류 생태학',
            'knowledge.categories.ecology.desc': '조류 서식지, 이주, 환경적 역할 이해하기',
            'knowledge.categories.cultural': '문화적 상징',
            'knowledge.categories.cultural.desc': '신화, 예술, 문학, 문화적 의미에서의 조류',
            'knowledge.latest.title': '최신 기사',
            'knowledge.articles.stats': '기사',
            'birdwatching.title': '조류 관찰 가이드 - BirdAiSnap',
            'birdwatching.header.title': '조류 관찰 가이드',
            'birdwatching.intro.text': '포괄적인 조류 관찰 가이드 섹션에 오신 것을 환영합니다. 여기서는 초보자 기초부터 고급 식별 기술까지 광범위한 조류 관찰 기법과 지식을 찾을 수 있으며, 조류 세계를 더 잘 감상하고 이해하는 데 도움이 됩니다. 아래 기사 이미지를 클릭하여 조류 관찰의 신비를 깊이 탐구해보세요.',
            'birdwatching.articles.getting-started.title': '시작 가이드',
            'birdwatching.articles.getting-started.desc': '초보자를 위한 포괄적인 조류 관찰 소개',
            'birdwatching.articles.essential-equipment.title': '필수 장비',
            'birdwatching.articles.essential-equipment.desc': '조류 관찰에 필요한 다양한 도구와 장비에 대해 알아보기',
            'birdwatching.articles.identification-techniques.title': '식별 기법',
            'birdwatching.articles.identification-techniques.desc': '조류 식별의 예술과 방법 마스터하기',
            'birdwatching.articles.best-locations.title': '최고의 장소',
            'birdwatching.articles.best-locations.desc': '전 세계 조류 관찰 명소 탐험하기',
            'birdwatching.articles.seasonal-guide.title': '계절별 가이드',
            'birdwatching.articles.seasonal-guide.desc': '계절 변화에 따른 조류 관찰 활동 계획하기',
            'birdwatching.articles.photography-tips.title': '사진 촬영 팁',
            'birdwatching.articles.photography-tips.desc': '멋진 조류 사진 촬영을 위한 실용적인 조언',
            'birdwatching.articles.behavior-observation.title': '행동 관찰',
            'birdwatching.articles.behavior-observation.desc': '조류 행동 관찰하고 이해하는 법 배우기',
            'birdwatching.articles.song-identification.title': '울음소리 식별',
            'birdwatching.articles.song-identification.desc': '소리로 다양한 조류 종을 식별하는 기법',
            'birdwatching.articles.ethics-conservation.title': '윤리 및 보존',
            'birdwatching.articles.ethics-conservation.desc': '책임감 있는 조류 관찰과 조류 보존에 기여하기',
            'birdwatching.articles.journal-keeping.title': '일지 작성',
            'birdwatching.articles.journal-keeping.desc': '조류 관찰 경험을 기록하고 정리하는 방법',
            'ecology.title': '조류 생태학 - BirdAiSnap',
            'ecology.header.title': '조류 생태학',
            'ecology.intro.text': '조류와 환경 간의 복잡하고 매혹적인 관계를 탐구하세요. 조류 생태학은 조류가 다양한 서식지에 어떻게 적응하는지, 생태계에서의 역할, 환경 변화가 조류 개체군에 미치는 영향을 연구합니다. 이러한 생태학적 관계를 이해하면 조류와 그들의 서식지를 더 잘 보호할 수 있습니다.',
            'ecology.articles.habitat-ecosystems.title': '서식지 및 생태계',
            'ecology.articles.habitat-ecosystems.desc': '조류 서식지의 다양성과 생태계 기능 이해하기',
            'ecology.articles.food-webs-chains.title': '먹이망 및 먹이사슬',
            'ecology.articles.food-webs-chains.desc': '먹이망에서 조류의 중요한 위치와 역할 탐구하기',
            'ecology.articles.migration-patterns.title': '이주 패턴',
            'ecology.articles.migration-patterns.desc': '조류 이주의 복잡한 패턴과 생태학적 의미 연구하기',
            'ecology.articles.breeding-ecology.title': '번식 생태학',
            'ecology.articles.breeding-ecology.desc': '조류 번식 행동과 생태학적 전략 이해하기',
            'ecology.articles.climate-change-impact.title': '기후 변화 영향',
            'ecology.articles.climate-change-impact.desc': '기후 변화가 조류 생태에 미치는 심각한 영향 분석하기',
            'ecology.articles.urban-ecology.title': '도시 생태학',
            'ecology.articles.urban-ecology.desc': '조류가 도시 환경에 어떻게 적응하는지 탐구하기',
            'ecology.articles.conservation-biology.title': '보전 생물학',
            'ecology.articles.conservation-biology.desc': '조류 보전의 과학적 원리와 실용적 방법 학습하기',
            'ecology.articles.island-biogeography.title': '섬 생물지리학',
            'ecology.articles.island-biogeography.desc': '섬 환경에서 조류 분포와 진화 연구하기',
            'ecology.articles.pollination-seed-dispersal.title': '수분 및 종자 산포',
            'ecology.articles.pollination-seed-dispersal.desc': '식물 번식에서 조류의 중요한 역할 이해하기',
            'ecology.articles.community-dynamics.title': '군집 역학',
            'ecology.articles.community-dynamics.desc': '조류 군집의 구조와 동적 변화 탐구하기'
        }
    },
    'ja': { 
        name: '日本語', 
        flag: '🇯🇵', 
        code: 'JA',
        translations: {
            'nav.home': 'ホーム',
            'nav.features': '機能',
            'nav.about': '概要',
            'nav.contact': 'お問い合わせ',
            'birdwatching.title': 'バードウォッチングガイド - BirdAiSnap',
            'birdwatching.header.title': 'バードウォッチングガイド',
            'birdwatching.intro.text': '包括的なバードウォッチングガイドセクションへようこそ。ここでは初心者の基礎から高度な識別技術まで、広範囲なバードウォッチング技法と知識を見つけることができ、鳥類の世界をより良く鑑賞し理解するのに役立ちます。下の記事画像をクリックして、バードウォッチングの神秘を深く探求してください。',
            'birdwatching.articles.getting-started.title': '入門ガイド',
            'birdwatching.articles.getting-started.desc': '初心者のための包括的なバードウォッチング紹介',
            'birdwatching.articles.essential-equipment.title': '必須機器',
            'birdwatching.articles.essential-equipment.desc': 'バードウォッチングに必要な様々なツールと機器について学ぶ',
            'birdwatching.articles.identification-techniques.title': '識別技法',
            'birdwatching.articles.identification-techniques.desc': '鳥類識別の芸術と方法をマスターする',
            'birdwatching.articles.best-locations.title': '最高の場所',
            'birdwatching.articles.best-locations.desc': '世界中のバードウォッチングホットスポットを探索する',
            'birdwatching.articles.seasonal-guide.title': '季節ガイド',
            'birdwatching.articles.seasonal-guide.desc': '季節の変化に応じてバードウォッチング活動を計画する',
            'birdwatching.articles.photography-tips.title': '写真撮影のコツ',
            'birdwatching.articles.photography-tips.desc': '素晴らしい鳥の写真を撮るための実用的なアドバイス',
            'birdwatching.articles.behavior-observation.title': '行動観察',
            'birdwatching.articles.behavior-observation.desc': '鳥の行動を観察し理解することを学ぶ',
            'birdwatching.articles.song-identification.title': '鳴き声識別',
            'birdwatching.articles.song-identification.desc': '音によって異なる鳥種を識別する技法',
            'birdwatching.articles.ethics-conservation.title': '倫理と保護',
            'birdwatching.articles.ethics-conservation.desc': '責任あるバードウォッチングと鳥類保護への貢献',
            'birdwatching.articles.journal-keeping.title': '日誌の記録',
            'birdwatching.articles.journal-keeping.desc': 'バードウォッチング体験を記録し整理する方法',
            'ecology.title': '鳥類生態学 - BirdAiSnap',
            'ecology.header.title': '鳥類生態学',
            'ecology.intro.text': '鳥類と環境の間の複雑で魅力的な関係を探求してください。鳥類生態学は、鳥類がさまざまな生息地にどのように適応するか、生態系での役割、環境変化が鳥類個体群に与える影響を研究します。これらの生態学的関係を理解することで、鳥類とその生息地をより良く保護することができます。',
            'ecology.articles.habitat-ecosystems.title': '生息地と生態系',
            'ecology.articles.habitat-ecosystems.desc': '鳥類生息地の多様性と生態系機能の理解',
            'ecology.articles.food-webs-chains.title': '食物網と食物連鎖',
            'ecology.articles.food-webs-chains.desc': '食物網における鳥類の重要な位置と役割の探求',
            'ecology.articles.migration-patterns.title': '渡りのパターン',
            'ecology.articles.migration-patterns.desc': '鳥類の渡りの複雑なパターンと生態学的意義の研究',
            'ecology.articles.breeding-ecology.title': '繁殖生態学',
            'ecology.articles.breeding-ecology.desc': '鳥類の繁殖行動と生態学的戦略の理解',
            'ecology.articles.climate-change-impact.title': '気候変動の影響',
            'ecology.articles.climate-change-impact.desc': '気候変動が鳥類生態に与える深刻な影響の分析',
            'ecology.articles.urban-ecology.title': '都市生態学',
            'ecology.articles.urban-ecology.desc': '鳥類が都市環境にどのように適応するかの探求',
            'ecology.articles.conservation-biology.title': '保全生物学',
            'ecology.articles.conservation-biology.desc': '鳥類保全の科学的原理と実用的方法の学習',
            'ecology.articles.island-biogeography.title': '島嶼生物地理学',
            'ecology.articles.island-biogeography.desc': '島嶼環境における鳥類分布と進化の研究',
            'ecology.articles.pollination-seed-dispersal.title': '受粉と種子散布',
            'ecology.articles.pollination-seed-dispersal.desc': '植物繁殖における鳥類の重要な役割の理解',
            'ecology.articles.community-dynamics.title': '群集動態',
            'ecology.articles.community-dynamics.desc': '鳥類群集の構造と動的変化の探求',
            'hero.title': 'インテリジェント認識、撮影と発見',
            'hero.description': 'BirdAiSnapは、AI駆動のインテリジェント認識アプリケーションで、周囲の鳥類を迅速に識別し、自然界の神秘を解き明かします。',
            'hero.download': '今すぐダウンロード',
            'hero.learn': '詳細を見る',
            'mockup.ai': 'AI強化',
            'mockup.scan': 'スキャン',
            'mockup.sound': 'サウンド',
            'features.title': 'コア機能',
            'features.scan.title': '撮影と識別',
            'features.scan.desc': '写真を撮影するか既存の画像をアップロードして、鳥類の種を正確に識別します',
            'features.sound.title': '音響認識',
            'features.sound.desc': '鳥の鳴き声を録音し、高度なAI音響分析を通じて種を識別します',
            'features.nearby.title': '地域の鳥類種',
            'features.nearby.desc': '近くの鳥類種を発見し、地域の生態パターンを探索します',
            'features.enhance.title': 'インテリジェント強化',
            'features.enhance.desc': '高度なAIアルゴリズムを活用して写真品質を向上させ、驚くべき鮮明さで鳥類を表示します',
            'features.collection.title': '個人コレクション',
            'features.collection.desc': 'パーソナライズされた鳥類コレクションをキュレーションし、すべてのバードウォッチング探検を詳細に記録します',
            'features.info.title': '包括的データベース',
            'features.info.desc': 'いつでもどこでも広範な鳥類学情報と科学知識リポジトリにアクセスします',
            'features.knowledge.title': '鳥類学の洞察',
            'features.knowledge.desc': '包括的なバードウォッチングガイド、科学的発見、鳥類ケア、生態関係、文化的意義を探求します',
            'about.title': 'BirdAiSnapについて',
            'about.desc1': 'BirdAiSnapは、鳥類愛好家と自然探検家のために特別に設計されたインテリジェント認識アプリケーションです。最先端のAI技術を通じて、ユーザーが自然の美しい鳥たちをより深く理解し、感謝できるよう支援することに専念しています。',
            'about.desc2': 'プロの鳥類学者でも好奇心旺盛な自然愛好家でも、BirdAiSnapは正確で迅速な鳥類識別サービスを提供します。',
            'about.stats.downloads': 'ダウンロード',
            'about.stats.species': '鳥類種',
            'about.stats.accuracy': '精度',
            'contact.title': 'お問い合わせ',
            'contact.subtitle': '詳細情報の取得',
            'contact.desc': 'ご質問やご提案がございましたら、お気軽にお問い合わせください',
            'contact.email': 'メール:',
            'contact.form.name': 'お名前',
            'contact.form.email': 'メールアドレス',
            'contact.form.message': 'メッセージ',
            'contact.form.submit': 'メッセージを送信',
            'contact.email.title': '📧 メール情報',
            'contact.email.recipient': '宛先:',
            'contact.email.subject': '件名:',
            'contact.email.content': '内容:',
            'contact.email.copy': 'メール情報をコピー',
            'contact.email.open': 'メールクライアントを開く',
            'footer.tagline': 'スマート認識、自然を探求',
            'footer.product': '製品',
            'footer.product.download': 'アプリダウンロード',
            'footer.product.features': '機能',
            'footer.product.guide': 'ユーザーガイド',
            'footer.support': 'サポート',
            'footer.support.help': 'ヘルプセンター',
            'footer.support.feedback': 'フィードバック',
            'footer.support.privacy': 'プライバシーポリシー',
            'footer.contact': 'お問い合わせ',
            'footer.contact.email': 'メール相談',
            'footer.copyright': '© 2024 BirdAiSnap. 全著作権所有',
            'knowledge.hero.title': '鳥類知識センター',
            'knowledge.hero.description': '包括的な知識リソースを通じて鳥類の魅力的な世界を探求する',
            'knowledge.categories.birdwatching': 'バードウォッチング',
            'knowledge.categories.birdwatching.desc': '鳥類観察と識別技術の芸術を学ぶ',
            'knowledge.categories.scientific': '科学的驚異',
            'knowledge.categories.scientific.desc': '鳥類に関する驚くべき科学的事実と研究を発見する',
            'knowledge.categories.petcare': 'ペット鳥のケア',
            'knowledge.categories.petcare.desc': 'ペット鳥の飼い主と愛好家のための必須ケアガイド',
            'knowledge.categories.ecology': '鳥類生態学',
            'knowledge.categories.ecology.desc': '鳥類の生息地、移住、環境的役割を理解する',
            'knowledge.categories.cultural': '文化的象徴',
            'knowledge.categories.cultural.desc': '神話、芸術、文学、文化的意義における鳥類',
            'knowledge.latest.title': '最新記事',
            'knowledge.articles.stats': '記事'
        }
    },
    'de': { 
        name: 'Deutsch', 
        flag: '🇩🇪', 
        code: 'DE',
        translations: {
            'nav.home': 'Startseite',
            'nav.features': 'Funktionen',
            'nav.about': 'Über uns',
            'nav.contact': 'Kontakt',
            'birdwatching.title': 'Vogelbeobachtungsführer - BirdAiSnap',
            'birdwatching.header.title': 'Vogelbeobachtungsführer',
            'birdwatching.intro.text': 'Willkommen in unserem umfassenden Vogelbeobachtungsführer-Bereich. Hier finden Sie umfangreiche Vogelbeobachtungstechniken und -wissen, von Anfängergrundlagen bis hin zu fortgeschrittenen Identifikationsfähigkeiten, die Ihnen helfen, die Welt der Vögel besser zu schätzen und zu verstehen. Klicken Sie auf eines der Artikelbilder unten, um tief in die Geheimnisse der Vogelbeobachtung einzutauchen.',
            'birdwatching.articles.getting-started.title': 'Einsteigerführer',
            'birdwatching.articles.getting-started.desc': 'Umfassende Vogelbeobachtungseinführung für Anfänger',
            'birdwatching.articles.essential-equipment.title': 'Wesentliche Ausrüstung',
            'birdwatching.articles.essential-equipment.desc': 'Lernen Sie über verschiedene Werkzeuge und Ausrüstung für die Vogelbeobachtung',
            'birdwatching.articles.identification-techniques.title': 'Identifikationstechniken',
            'birdwatching.articles.identification-techniques.desc': 'Meistern Sie die Kunst und Methoden der Vogelidentifikation',
            'birdwatching.articles.best-locations.title': 'Beste Standorte',
            'birdwatching.articles.best-locations.desc': 'Erkunden Sie Vogelbeobachtungs-Hotspots auf der ganzen Welt',
            'birdwatching.articles.seasonal-guide.title': 'Saisonaler Führer',
            'birdwatching.articles.seasonal-guide.desc': 'Planen Sie Ihre Vogelbeobachtungsaktivitäten entsprechend den saisonalen Veränderungen',
            'birdwatching.articles.photography-tips.title': 'Fotografietipps',
            'birdwatching.articles.photography-tips.desc': 'Praktische Ratschläge für das Aufnehmen atemberaubender Vogelfotos',
            'birdwatching.articles.behavior-observation.title': 'Verhaltensbeobachtung',
            'birdwatching.articles.behavior-observation.desc': 'Lernen Sie, Vogelverhalten zu beobachten und zu verstehen',
            'birdwatching.articles.song-identification.title': 'Gesangsidentifikation',
            'birdwatching.articles.song-identification.desc': 'Techniken zur Identifikation verschiedener Vogelarten durch Klang',
            'birdwatching.articles.ethics-conservation.title': 'Ethik und Naturschutz',
            'birdwatching.articles.ethics-conservation.desc': 'Verantwortungsvolle Vogelbeobachtung und Beitrag zum Vogelschutz',
            'birdwatching.articles.journal-keeping.title': 'Tagebuchführung',
            'birdwatching.articles.journal-keeping.desc': 'Wie Sie Ihre Vogelbeobachtungserfahrungen aufzeichnen und organisieren',
            'ecology.title': 'Vogelökologie - BirdAiSnap',
            'ecology.header.title': 'Vogelökologie',
            'ecology.intro.text': 'Erkunden Sie die komplexen und faszinierenden Beziehungen zwischen Vögeln und ihrer Umwelt. Die Vogelökologie untersucht, wie sich Vögel an verschiedene Lebensräume anpassen, ihre Rollen in Ökosystemen und die Auswirkungen von Umweltveränderungen auf Vogelpopulationen. Das Verständnis dieser ökologischen Beziehungen hilft uns, Vögel und ihre Lebensräume besser zu schützen.',
            'ecology.articles.habitat-ecosystems.title': 'Lebensräume und Ökosysteme',
            'ecology.articles.habitat-ecosystems.desc': 'Die Vielfalt der Vogellebensräume und Ökosystemfunktionen verstehen',
            'ecology.articles.food-webs-chains.title': 'Nahrungsnetze und Nahrungsketten',
            'ecology.articles.food-webs-chains.desc': 'Die wichtige Position und Rolle der Vögel in Nahrungsnetzen erkunden',
            'ecology.articles.migration-patterns.title': 'Wanderungsmuster',
            'ecology.articles.migration-patterns.desc': 'Die komplexen Muster und ökologische Bedeutung der Vogelwanderung studieren',
            'ecology.articles.breeding-ecology.title': 'Brutökologie',
            'ecology.articles.breeding-ecology.desc': 'Vogelbrutverhaltensweisen und ökologische Strategien verstehen',
            'ecology.articles.climate-change-impact.title': 'Klimawandel-Auswirkungen',
            'ecology.articles.climate-change-impact.desc': 'Die tiefgreifenden Auswirkungen des Klimawandels auf die Vogelökologie analysieren',
            'ecology.articles.urban-ecology.title': 'Stadtökologie',
            'ecology.articles.urban-ecology.desc': 'Erkunden, wie sich Vögel an städtische Umgebungen anpassen',
            'ecology.articles.conservation-biology.title': 'Naturschutzbiologie',
            'ecology.articles.conservation-biology.desc': 'Die wissenschaftlichen Prinzipien und praktischen Methoden des Vogelschutzes lernen',
            'ecology.articles.island-biogeography.title': 'Insel-Biogeographie',
            'ecology.articles.island-biogeography.desc': 'Vogelverteilung und Evolution in Inselumgebungen studieren',
            'ecology.articles.pollination-seed-dispersal.title': 'Bestäubung und Samenausbreitung',
            'ecology.articles.pollination-seed-dispersal.desc': 'Die wichtige Rolle der Vögel bei der Pflanzenfortpflanzung verstehen',
            'ecology.articles.community-dynamics.title': 'Gemeinschaftsdynamik',
            'ecology.articles.community-dynamics.desc': 'Die Struktur und dynamischen Veränderungen von Vogelgemeinschaften erkunden',
            'hero.title': 'Intelligente Erkennung, Aufnahme und Entdeckung',
            'hero.description': 'BirdAiSnap ist eine KI-gestützte intelligente Erkennungsanwendung, die eine schnelle Vogelidentifikation in Ihrer Umgebung ermöglicht und die Geheimnisse der Natur enthüllt.',
            'hero.download': 'Jetzt herunterladen',
            'hero.learn': 'Mehr erfahren',
            'mockup.ai': 'KI-Verbesserung',
            'mockup.scan': 'Scannen',
            'mockup.sound': 'Ton',
            'features.title': 'Kernfunktionen',
            'features.scan.title': 'Aufnehmen und Identifizieren',
            'features.scan.desc': 'Machen Sie einfach ein Foto oder laden Sie ein vorhandenes Bild hoch, um Vogelarten präzise zu identifizieren',
            'features.sound.title': 'Akustische Erkennung',
            'features.sound.desc': 'Nehmen Sie Vogelrufe auf und identifizieren Sie Arten durch ausgeklügelte KI-Akustikanalyse',
            'features.nearby.title': 'Lokale Vogelarten',
            'features.nearby.desc': 'Entdecken Sie Vogelarten in Ihrer Nähe und erkunden Sie regionale ökologische Muster',
            'features.enhance.title': 'Intelligente Verbesserung',
            'features.enhance.desc': 'Nutzen Sie fortschrittliche KI-Algorithmen zur Verbesserung der Fotoqualität und zeigen Sie Vögel in atemberaubender Klarheit',
            'features.collection.title': 'Persönliche Sammlungen',
            'features.collection.desc': 'Kuratieren Sie personalisierte Vogelsammlungen und dokumentieren Sie jede Vogelbeobachtungsexpedition detailliert',
            'features.info.title': 'Umfassende Datenbank',
            'features.info.desc': 'Greifen Sie jederzeit und überall auf umfangreiche ornithologische Informationen und wissenschaftliche Wissensrepositorien zu',
            'features.knowledge.title': 'Ornithologische Einblicke',
            'features.knowledge.desc': 'Erkunden Sie umfassende Vogelbeobachtungsführer, wissenschaftliche Entdeckungen, Vogelpflege, ökologische Beziehungen und kulturelle Bedeutung',
            'about.title': 'Über BirdAiSnap',
            'about.desc1': 'BirdAiSnap ist eine intelligente Erkennungsanwendung, die speziell für Vogelliebhaber und Naturforscher entwickelt wurde. Wir sind bestrebt, Benutzern durch modernste KI-Technologie zu helfen, ein tieferes Verständnis und eine größere Wertschätzung für die prächtigen Vögel in der Natur zu entwickeln.',
            'about.desc2': 'Ob Sie ein professioneller Ornithologe oder ein neugieriger Naturliebhaber sind, BirdAiSnap bietet präzise und schnelle Vogelidentifikationsdienste.',
            'about.stats.downloads': 'Downloads',
            'about.stats.species': 'Vogelarten',
            'about.stats.accuracy': 'Genauigkeitsrate',
            'contact.title': 'Kontaktieren Sie uns',
            'contact.subtitle': 'Weitere Informationen erhalten',
            'contact.desc': 'Wenn Sie Fragen oder Vorschläge haben, kontaktieren Sie uns gerne',
            'contact.email': 'E-Mail:',
            'contact.form.name': 'Ihr Name',
            'contact.form.email': 'Ihre E-Mail',
            'contact.form.message': 'Ihre Nachricht',
            'contact.form.submit': 'Nachricht senden',
            'contact.email.title': '📧 E-Mail-Informationen',
            'contact.email.recipient': 'Empfänger:',
            'contact.email.subject': 'Betreff:',
            'contact.email.content': 'Inhalt:',
            'contact.email.copy': 'E-Mail-Informationen kopieren',
            'contact.email.open': 'E-Mail-Client öffnen',
            'footer.tagline': 'Intelligente Erkennung, Natur erkunden',
            'footer.product': 'Produkt',
            'footer.product.download': 'App herunterladen',
            'footer.product.features': 'Funktionen',
            'footer.product.guide': 'Benutzerhandbuch',
            'footer.support': 'Support',
            'footer.support.help': 'Hilfezentrum',
            'footer.support.feedback': 'Feedback',
            'footer.support.privacy': 'Datenschutzrichtlinie',
            'footer.contact': 'Kontakt',
            'footer.contact.email': 'E-Mail-Beratung',
            'footer.copyright': '© 2024 BirdAiSnap. Alle Rechte vorbehalten',
            'knowledge.hero.title': 'Vogelwissen-Zentrum',
            'knowledge.hero.description': 'Erkunden Sie die faszinierende Welt der Vögel durch umfassende Wissensressourcen',
            'knowledge.categories.birdwatching': 'Vogelbeobachtung',
            'knowledge.categories.birdwatching.desc': 'Lernen Sie die Kunst der Vogelbeobachtung und Identifikationstechniken',
            'knowledge.categories.scientific': 'Wissenschaftliche Wunder',
            'knowledge.categories.scientific.desc': 'Entdecken Sie erstaunliche wissenschaftliche Fakten und Forschung über Vögel',
            'knowledge.categories.petcare': 'Haustiervogel-Pflege',
            'knowledge.categories.petcare.desc': 'Wesentliche Pflegeanleitungen für Haustiervogel-Besitzer und Enthusiasten',
            'knowledge.categories.ecology': 'Vogelökologie',
            'knowledge.categories.ecology.desc': 'Verstehen Sie Vogellebensräume, Migration und Umweltrollen',
            'knowledge.categories.cultural': 'Kulturelle Symbolik',
            'knowledge.categories.cultural.desc': 'Vögel in Mythologie, Kunst, Literatur und kultureller Bedeutung',
            'knowledge.latest.title': 'Neueste Artikel',
            'knowledge.articles.stats': 'Artikel'
        }
    },
    'fr': { 
        name: 'Français', 
        flag: '🇫🇷', 
        code: 'FR',
        translations: {
            'nav.home': 'Accueil',
            'nav.features': 'Fonctionnalités',
            'nav.about': 'À propos',
            'nav.contact': 'Contact',
            'birdwatching.title': 'Guide d\'observation des oiseaux - BirdAiSnap',
            'birdwatching.header.title': 'Guide d\'observation des oiseaux',
            'birdwatching.intro.text': 'Bienvenue dans notre section complète de guide d\'observation des oiseaux. Ici, vous trouverez des techniques et connaissances étendues d\'observation des oiseaux, des bases pour débutants aux compétences d\'identification avancées, vous aidant à mieux apprécier et comprendre le monde des oiseaux. Cliquez sur n\'importe quelle image d\'article ci-dessous pour plonger profondément dans les mystères de l\'observation des oiseaux.',
            'birdwatching.articles.getting-started.title': 'Guide de démarrage',
            'birdwatching.articles.getting-started.desc': 'Introduction complète à l\'observation des oiseaux pour débutants',
            'birdwatching.articles.essential-equipment.title': 'Équipement essentiel',
            'birdwatching.articles.essential-equipment.desc': 'Apprenez sur les divers outils et équipements nécessaires pour l\'observation des oiseaux',
            'birdwatching.articles.identification-techniques.title': 'Techniques d\'identification',
            'birdwatching.articles.identification-techniques.desc': 'Maîtrisez l\'art et les méthodes d\'identification des oiseaux',
            'birdwatching.articles.best-locations.title': 'Meilleurs emplacements',
            'birdwatching.articles.best-locations.desc': 'Explorez les points chauds d\'observation des oiseaux dans le monde entier',
            'birdwatching.articles.seasonal-guide.title': 'Guide saisonnier',
            'birdwatching.articles.seasonal-guide.desc': 'Planifiez vos activités d\'observation des oiseaux selon les changements saisonniers',
            'birdwatching.articles.photography-tips.title': 'Conseils de photographie',
            'birdwatching.articles.photography-tips.desc': 'Conseils pratiques pour capturer de superbes photographies d\'oiseaux',
            'birdwatching.articles.behavior-observation.title': 'Observation du comportement',
            'birdwatching.articles.behavior-observation.desc': 'Apprenez à observer et comprendre le comportement des oiseaux',
            'birdwatching.articles.song-identification.title': 'Identification des chants',
            'birdwatching.articles.song-identification.desc': 'Techniques pour identifier différentes espèces d\'oiseaux par le son',
            'birdwatching.articles.ethics-conservation.title': 'Éthique et conservation',
            'birdwatching.articles.ethics-conservation.desc': 'Observation responsable des oiseaux et contribution à la conservation des oiseaux',
            'birdwatching.articles.journal-keeping.title': 'Tenue de journal',
            'birdwatching.articles.journal-keeping.desc': 'Comment enregistrer et organiser vos expériences d\'observation des oiseaux',
            'hero.title': 'Reconnaissance intelligente, capture et découverte',
            'hero.description': 'BirdAiSnap est une application de reconnaissance intelligente alimentée par IA qui permet une identification rapide des oiseaux dans votre environnement tout en dévoilant les mystères du monde naturel.',
            'hero.download': 'Télécharger maintenant',
            'hero.learn': 'En savoir plus',
            'mockup.ai': 'Amélioration IA',
            'mockup.scan': 'Scanner',
            'mockup.sound': 'Son',
            'features.title': 'Fonctionnalités principales',
            'features.scan.title': 'Capturer et identifier',
            'features.scan.desc': 'Prenez simplement une photo ou téléchargez une image existante pour identifier instantanément les espèces d\'oiseaux avec précision',
            'features.sound.title': 'Reconnaissance acoustique',
            'features.sound.desc': 'Enregistrez les vocalisations aviaires et identifiez les espèces grâce à une analyse acoustique IA sophistiquée',
            'features.nearby.title': 'Espèces aviaires locales',
            'features.nearby.desc': 'Découvrez les espèces d\'oiseaux dans votre région et explorez les modèles écologiques régionaux',
            'features.enhance.title': 'Amélioration intelligente',
            'features.enhance.desc': 'Utilisez des algorithmes IA avancés pour améliorer la qualité photographique et présenter les sujets aviaires avec une clarté époustouflante',
            'features.collection.title': 'Collections personnelles',
            'features.collection.desc': 'Organisez des collections aviaires personnalisées et documentez chaque expédition d\'observation d\'oiseaux avec des enregistrements détaillés',
            'features.info.title': 'Base de données complète',
            'features.info.desc': 'Accédez à de vastes informations ornithologiques et référentiels de connaissances scientifiques à tout moment, n\'importe où',
            'features.knowledge.title': 'Perspectives ornithologiques',
            'features.knowledge.desc': 'Explorez des guides complets d\'observation d\'oiseaux, des découvertes scientifiques, des soins aviaires, des relations écologiques et une signification culturelle',
            'about.title': 'À propos de BirdAiSnap',
            'about.desc1': 'BirdAiSnap est une application de reconnaissance intelligente conçue spécifiquement pour les passionnés d\'oiseaux et les explorateurs de la nature. Nous nous consacrons à aider les utilisateurs à développer une compréhension et une appréciation plus profondes des magnifiques oiseaux de la nature grâce à une technologie IA de pointe.',
            'about.desc2': 'Que vous soyez un ornithologue professionnel ou un passionné de nature curieux, BirdAiSnap offre des services d\'identification d\'oiseaux précis et rapides.',
            'about.stats.downloads': 'Téléchargements',
            'about.stats.species': 'Espèces d\'oiseaux',
            'about.stats.accuracy': 'Taux de précision',
            'contact.title': 'Contactez-nous',
            'contact.subtitle': 'Obtenir plus d\'informations',
            'contact.desc': 'Si vous avez des questions ou des suggestions, n\'hésitez pas à nous contacter',
            'contact.email': 'E-mail:',
            'contact.form.name': 'Votre nom',
            'contact.form.email': 'Votre e-mail',
            'contact.form.message': 'Votre message',
            'contact.form.submit': 'Envoyer le message',
            'contact.email.title': '📧 Informations e-mail',
            'contact.email.recipient': 'Destinataire:',
            'contact.email.subject': 'Sujet:',
            'contact.email.content': 'Contenu:',
            'contact.email.copy': 'Copier les informations e-mail',
            'contact.email.open': 'Ouvrir le client e-mail',
            'footer.tagline': 'Reconnaissance intelligente, explorer la nature',
            'footer.product': 'Produit',
            'footer.product.download': 'Télécharger l\'application',
            'footer.product.features': 'Fonctionnalités',
            'footer.product.guide': 'Guide utilisateur',
            'footer.support': 'Support',
            'footer.support.help': 'Centre d\'aide',
            'footer.support.feedback': 'Commentaires',
            'footer.support.privacy': 'Politique de confidentialité',
            'footer.contact': 'Contact',
            'footer.contact.email': 'Consultation par e-mail',
            'footer.copyright': '© 2024 BirdAiSnap. Tous droits réservés',
            'knowledge.hero.title': 'Centre de connaissances aviaires',
            'knowledge.hero.description': 'Explorez le monde fascinant des oiseaux à travers des ressources de connaissances complètes',
            'knowledge.categories.birdwatching': 'Observation d\'oiseaux',
            'knowledge.categories.birdwatching.desc': 'Apprenez l\'art de l\'observation et des techniques d\'identification des oiseaux',
            'knowledge.categories.scientific': 'Merveilles scientifiques',
            'knowledge.categories.scientific.desc': 'Découvrez des faits scientifiques étonnants et des recherches sur les oiseaux',
            'knowledge.categories.petcare': 'Soins des oiseaux domestiques',
            'knowledge.categories.petcare.desc': 'Guides de soins essentiels pour les propriétaires et passionnés d\'oiseaux domestiques',
            'knowledge.categories.ecology': 'Écologie aviaire',
            'knowledge.categories.ecology.desc': 'Comprendre les habitats, la migration et les rôles environnementaux des oiseaux',
            'knowledge.categories.cultural': 'Symbolisme culturel',
            'knowledge.categories.cultural.desc': 'Les oiseaux dans la mythologie, l\'art, la littérature et la signification culturelle',
            'knowledge.latest.title': 'Derniers articles',
            'knowledge.articles.stats': 'articles'
        }
    },
    'es': { 
        name: 'Español', 
        flag: '🇪🇸', 
        code: 'ES',
        translations: {
            'birdwatching.title': 'Guía de observación de aves - BirdAiSnap',
            'birdwatching.header.title': 'Guía de observación de aves',
            'birdwatching.intro.text': 'Bienvenido a nuestra sección completa de guía de observación de aves. Aquí encontrará técnicas y conocimientos extensos de observación de aves, desde conceptos básicos para principiantes hasta habilidades de identificación avanzadas, ayudándole a apreciar y comprender mejor el mundo de las aves. Haga clic en cualquier imagen de artículo a continuación para sumergirse profundamente en los misterios de la observación de aves.',
            'birdwatching.articles.getting-started.title': 'Guía de inicio',
            'birdwatching.articles.getting-started.desc': 'Introducción completa a la observación de aves para principiantes',
            'birdwatching.articles.essential-equipment.title': 'Equipo esencial',
            'birdwatching.articles.essential-equipment.desc': 'Aprenda sobre varias herramientas y equipos necesarios para la observación de aves',
            'birdwatching.articles.identification-techniques.title': 'Técnicas de identificación',
            'birdwatching.articles.identification-techniques.desc': 'Domine el arte y los métodos de identificación de aves',
            'birdwatching.articles.best-locations.title': 'Mejores ubicaciones',
            'birdwatching.articles.best-locations.desc': 'Explore puntos calientes de observación de aves en todo el mundo',
            'birdwatching.articles.seasonal-guide.title': 'Guía estacional',
            'birdwatching.articles.seasonal-guide.desc': 'Planifique sus actividades de observación de aves según los cambios estacionales',
            'birdwatching.articles.photography-tips.title': 'Consejos de fotografía',
            'birdwatching.articles.photography-tips.desc': 'Consejos prácticos para capturar fotografías impresionantes de aves',
            'birdwatching.articles.behavior-observation.title': 'Observación del comportamiento',
            'birdwatching.articles.behavior-observation.desc': 'Aprenda a observar y comprender el comportamiento de las aves',
            'birdwatching.articles.song-identification.title': 'Identificación de cantos',
            'birdwatching.articles.song-identification.desc': 'Técnicas para identificar diferentes especies de aves por sonido',
            'birdwatching.articles.ethics-conservation.title': 'Ética y conservación',
            'birdwatching.articles.ethics-conservation.desc': 'Observación responsable de aves y contribución a la conservación de aves',
            'birdwatching.articles.journal-keeping.title': 'Mantenimiento de diario',
            'birdwatching.articles.journal-keeping.desc': 'Cómo registrar y organizar sus experiencias de observación de aves',
            'nav.home': 'Inicio',
            'nav.features': 'Características',
            'nav.about': 'Acerca de',
            'nav.contact': 'Contacto',
            'hero.title': 'Reconocimiento inteligente, captura y descubrimiento',
            'hero.description': 'BirdAiSnap es una aplicación de reconocimiento inteligente impulsada por IA que permite la identificación rápida de aves en su entorno mientras revela los misterios del mundo natural.',
            'hero.download': 'Descargar ahora',
            'hero.learn': 'Saber más',
            'mockup.ai': 'Mejora IA',
            'mockup.scan': 'Escanear',
            'mockup.sound': 'Sonido',
            'features.title': 'Características principales',
            'features.scan.title': 'Capturar e identificar',
            'features.scan.desc': 'Simplemente tome una fotografía o cargue una imagen existente para identificar instantáneamente especies de aves con precisión',
            'features.sound.title': 'Reconocimiento acústico',
            'features.sound.desc': 'Grabe vocalizaciones aviares e identifique especies a través de análisis acústico IA sofisticado',
            'features.nearby.title': 'Especies aviares locales',
            'features.nearby.desc': 'Descubra especies de aves en su vecindario y explore patrones ecológicos regionales',
            'features.enhance.title': 'Mejora inteligente',
            'features.enhance.desc': 'Utilice algoritmos IA avanzados para mejorar la calidad fotográfica y mostrar sujetos aviares con claridad impresionante',
            'features.collection.title': 'Colecciones personales',
            'features.collection.desc': 'Organice colecciones aviares personalizadas y documente cada expedición de observación de aves con registros detallados',
            'features.info.title': 'Base de datos integral',
            'features.info.desc': 'Acceda a información ornitológica extensa y repositorios de conocimiento científico en cualquier momento, en cualquier lugar',
            'features.knowledge.title': 'Perspectivas ornitológicas',
            'features.knowledge.desc': 'Explore guías completas de observación de aves, descubrimientos científicos, cuidado aviar, relaciones ecológicas y significado cultural',
            'about.title': 'Acerca de BirdAiSnap',
            'about.desc1': 'BirdAiSnap es una aplicación de reconocimiento inteligente diseñada específicamente para entusiastas de las aves y exploradores de la naturaleza. Nos dedicamos a ayudar a los usuarios a desarrollar una comprensión y apreciación más profundas de las magníficas aves en la naturaleza a través de tecnología IA de vanguardia.',
            'about.desc2': 'Ya sea que sea un ornitólogo profesional o un entusiasta de la naturaleza curioso, BirdAiSnap ofrece servicios de identificación de aves precisos y rápidos.',
            'about.stats.downloads': 'Descargas',
            'about.stats.species': 'Especies de aves',
            'about.stats.accuracy': 'Tasa de precisión',
            'contact.title': 'Contáctanos',
            'contact.subtitle': 'Obtener más información',
            'contact.desc': 'Si tiene alguna pregunta o sugerencia, no dude en contactarnos',
            'contact.email': 'Correo electrónico:',
            'contact.form.name': 'Su nombre',
            'contact.form.email': 'Su correo electrónico',
            'contact.form.message': 'Su mensaje',
            'contact.form.submit': 'Enviar mensaje',
            'contact.email.title': '📧 Información de correo electrónico',
            'contact.email.recipient': 'Destinatario:',
            'contact.email.subject': 'Asunto:',
            'contact.email.content': 'Contenido:',
            'contact.email.copy': 'Copiar información de correo electrónico',
            'contact.email.open': 'Abrir cliente de correo electrónico',
            'footer.tagline': 'Reconocimiento inteligente, explorar la naturaleza',
            'footer.product': 'Producto',
            'footer.product.download': 'Descargar aplicación',
            'footer.product.features': 'Características',
            'footer.product.guide': 'Guía del usuario',
            'footer.support': 'Soporte',
            'footer.support.help': 'Centro de ayuda',
            'footer.support.feedback': 'Comentarios',
            'footer.support.privacy': 'Política de privacidad',
            'footer.contact': 'Contacto',
            'footer.contact.email': 'Consulta por correo electrónico',
            'footer.copyright': '© 2024 BirdAiSnap. Todos los derechos reservados',
            'knowledge.hero.title': 'Centro de conocimiento de aves',
            'knowledge.hero.description': 'Explore el fascinante mundo de las aves a través de recursos de conocimiento integral',
            'knowledge.categories.birdwatching': 'Observación de aves',
            'knowledge.categories.birdwatching.desc': 'Aprenda el arte de la observación de aves y técnicas de identificación',
            'knowledge.categories.scientific': 'Maravillas científicas',
            'knowledge.categories.scientific.desc': 'Descubra hechos científicos asombrosos e investigación sobre aves',
            'knowledge.categories.petcare': 'Cuidado de aves mascotas',
            'knowledge.categories.petcare.desc': 'Guías de cuidado esenciales para propietarios y entusiastas de aves mascotas',
            'knowledge.categories.ecology': 'Ecología aviar',
            'knowledge.categories.ecology.desc': 'Comprender los hábitats, migración y roles ambientales de las aves',
            'knowledge.categories.cultural': 'Simbolismo cultural',
            'knowledge.categories.cultural.desc': 'Aves en mitología, arte, literatura y significado cultural',
            'knowledge.latest.title': 'Últimos artículos',
            'knowledge.articles.stats': 'artículos'
        }
    },
    'it': { 
        name: 'Italiano', 
        flag: '🇮🇹', 
        code: 'IT',
        translations: {
            'birdwatching.title': 'Guida all\'osservazione degli uccelli - BirdAiSnap',
            'birdwatching.header.title': 'Guida all\'osservazione degli uccelli',
            'birdwatching.intro.text': 'Benvenuti nella nostra sezione completa di guida all\'osservazione degli uccelli. Qui troverete tecniche e conoscenze estese di osservazione degli uccelli, dalle basi per principianti alle competenze di identificazione avanzate, aiutandovi ad apprezzare e comprendere meglio il mondo degli uccelli. Cliccate su qualsiasi immagine di articolo qui sotto per immergervi profondamente nei misteri dell\'osservazione degli uccelli.',
            'birdwatching.articles.getting-started.title': 'Guida introduttiva',
            'birdwatching.articles.getting-started.desc': 'Introduzione completa all\'osservazione degli uccelli per principianti',
            'birdwatching.articles.essential-equipment.title': 'Attrezzatura essenziale',
            'birdwatching.articles.essential-equipment.desc': 'Imparate sui vari strumenti e attrezzature necessari per l\'osservazione degli uccelli',
            'birdwatching.articles.identification-techniques.title': 'Tecniche di identificazione',
            'birdwatching.articles.identification-techniques.desc': 'Padroneggiate l\'arte e i metodi di identificazione degli uccelli',
            'birdwatching.articles.best-locations.title': 'Migliori località',
            'birdwatching.articles.best-locations.desc': 'Esplorate i punti caldi di osservazione degli uccelli in tutto il mondo',
            'birdwatching.articles.seasonal-guide.title': 'Guida stagionale',
            'birdwatching.articles.seasonal-guide.desc': 'Pianificate le vostre attività di osservazione degli uccelli secondo i cambiamenti stagionali',
            'birdwatching.articles.photography-tips.title': 'Consigli di fotografia',
            'birdwatching.articles.photography-tips.desc': 'Consigli pratici per catturare fotografie mozzafiato di uccelli',
            'birdwatching.articles.behavior-observation.title': 'Osservazione del comportamento',
            'birdwatching.articles.behavior-observation.desc': 'Imparate ad osservare e comprendere il comportamento degli uccelli',
            'birdwatching.articles.song-identification.title': 'Identificazione dei canti',
            'birdwatching.articles.song-identification.desc': 'Tecniche per identificare diverse specie di uccelli tramite il suono',
            'birdwatching.articles.ethics-conservation.title': 'Etica e conservazione',
            'birdwatching.articles.ethics-conservation.desc': 'Osservazione responsabile degli uccelli e contributo alla conservazione degli uccelli',
            'birdwatching.articles.journal-keeping.title': 'Tenuta del diario',
            'birdwatching.articles.journal-keeping.desc': 'Come registrare e organizzare le vostre esperienze di osservazione degli uccelli',
            'nav.home': 'Home',
            'nav.features': 'Caratteristiche',
            'nav.about': 'Chi siamo',
            'nav.contact': 'Contatto',
            'hero.title': 'Riconoscimento intelligente, cattura e scoperta',
            'hero.description': 'BirdAiSnap è un\'applicazione di riconoscimento intelligente alimentata da IA che consente l\'identificazione rapida degli uccelli nel vostro ambiente rivelando i misteri del mondo naturale.',
            'hero.download': 'Scarica ora',
            'hero.learn': 'Scopri di più',
            'mockup.ai': 'Miglioramento IA',
            'mockup.scan': 'Scansiona',
            'mockup.sound': 'Suono',
            'features.title': 'Caratteristiche principali',
            'features.scan.title': 'Cattura e identifica',
            'features.scan.desc': 'Scatta semplicemente una fotografia o carica un\'immagine esistente per identificare istantaneamente le specie di uccelli con precisione',
            'features.sound.title': 'Riconoscimento acustico',
            'features.sound.desc': 'Registra le vocalizzazioni aviarie e identifica le specie attraverso sofisticate analisi acustiche IA',
            'features.nearby.title': 'Specie aviarie locali',
            'features.nearby.desc': 'Scopri le specie di uccelli nella tua zona ed esplora i modelli ecologici regionali',
            'features.enhance.title': 'Miglioramento intelligente',
            'features.enhance.desc': 'Utilizza algoritmi IA avanzati per migliorare la qualità fotografica e mostrare soggetti aviari con chiarezza straordinaria',
            'features.collection.title': 'Collezioni personali',
            'features.collection.desc': 'Cura collezioni aviarie personalizzate e documenta ogni spedizione di birdwatching con registrazioni dettagliate',
            'features.info.title': 'Database completo',
            'features.info.desc': 'Accedi a informazioni ornitologiche estese e repository di conoscenze scientifiche sempre, ovunque',
            'features.knowledge.title': 'Approfondimenti ornitologici',
            'features.knowledge.desc': 'Esplora guide complete per il birdwatching, scoperte scientifiche, cura degli uccelli, relazioni ecologiche e significato culturale',
            'about.title': 'Chi è BirdAiSnap',
            'about.desc1': 'BirdAiSnap è un\'applicazione di riconoscimento intelligente progettata specificamente per gli appassionati di uccelli e gli esploratori della natura. Ci dedichiamo ad aiutare gli utenti a sviluppare una comprensione e un apprezzamento più profondi dei magnifici uccelli in natura attraverso la tecnologia IA all\'avanguardia.',
            'about.desc2': 'Che tu sia un ornitologo professionista o un appassionato di natura curioso, BirdAiSnap offre servizi di identificazione degli uccelli precisi e rapidi.',
            'about.stats.downloads': 'Download',
            'about.stats.species': 'Specie di uccelli',
            'about.stats.accuracy': 'Tasso di precisione',
            'contact.title': 'Contattaci',
            'contact.subtitle': 'Ottieni maggiori informazioni',
            'contact.desc': 'Se hai domande o suggerimenti, non esitare a contattarci',
            'contact.email': 'Email:',
            'contact.form.name': 'Il tuo nome',
            'contact.form.email': 'La tua email',
            'contact.form.message': 'Il tuo messaggio',
            'contact.form.submit': 'Invia messaggio',
            'contact.email.title': '📧 Informazioni email',
            'contact.email.recipient': 'Destinatario:',
            'contact.email.subject': 'Oggetto:',
            'contact.email.content': 'Contenuto:',
            'contact.email.copy': 'Copia informazioni email',
            'contact.email.open': 'Apri client email',
            'footer.tagline': 'Riconoscimento intelligente, esplora la natura',
            'footer.product': 'Prodotto',
            'footer.product.download': 'Scarica app',
            'footer.product.features': 'Caratteristiche',
            'footer.product.guide': 'Guida utente',
            'footer.support': 'Supporto',
            'footer.support.help': 'Centro assistenza',
            'footer.support.feedback': 'Feedback',
            'footer.support.privacy': 'Informativa sulla privacy',
            'footer.contact': 'Contatto',
            'footer.contact.email': 'Consulenza email',
            'footer.copyright': '© 2024 BirdAiSnap. Tutti i diritti riservati',
            'knowledge.hero.title': 'Centro di conoscenza degli uccelli',
            'knowledge.hero.description': 'Esplora il mondo affascinante degli uccelli attraverso risorse di conoscenza complete',
            'knowledge.categories.birdwatching': 'Birdwatching',
            'knowledge.categories.birdwatching.desc': 'Impara l\'arte dell\'osservazione degli uccelli e le tecniche di identificazione',
            'knowledge.categories.scientific': 'Meraviglie scientifiche',
            'knowledge.categories.scientific.desc': 'Scopri fatti scientifici sorprendenti e ricerche sugli uccelli',
            'knowledge.categories.petcare': 'Cura degli uccelli domestici',
            'knowledge.categories.petcare.desc': 'Guide di cura essenziali per proprietari e appassionati di uccelli domestici',
            'knowledge.categories.ecology': 'Ecologia aviaria',
            'knowledge.categories.ecology.desc': 'Comprendere gli habitat, la migrazione e i ruoli ambientali degli uccelli',
            'knowledge.categories.cultural': 'Simbolismo culturale',
            'knowledge.categories.cultural.desc': 'Uccelli nella mitologia, arte, letteratura e significato culturale',
            'knowledge.latest.title': 'Ultimi articoli',
            'knowledge.articles.stats': 'articoli'
        }
    },
    'pt': { 
        name: 'Português', 
        flag: '🇵🇹', 
        code: 'PT',
        translations: {
            'birdwatching.title': 'Guia de observação de aves - BirdAiSnap',
            'birdwatching.header.title': 'Guia de observação de aves',
            'birdwatching.intro.text': 'Bem-vindos à nossa seção abrangente de guia de observação de aves. Aqui encontrará técnicas e conhecimentos extensos de observação de aves, desde conceitos básicos para iniciantes até habilidades de identificação avançadas, ajudando-o a apreciar e compreender melhor o mundo das aves. Clique em qualquer imagem de artigo abaixo para mergulhar profundamente nos mistérios da observação de aves.',
            'birdwatching.articles.getting-started.title': 'Guia de início',
            'birdwatching.articles.getting-started.desc': 'Introdução abrangente à observação de aves para iniciantes',
            'birdwatching.articles.essential-equipment.title': 'Equipamento essencial',
            'birdwatching.articles.essential-equipment.desc': 'Aprenda sobre várias ferramentas e equipamentos necessários para observação de aves',
            'birdwatching.articles.identification-techniques.title': 'Técnicas de identificação',
            'birdwatching.articles.identification-techniques.desc': 'Domine a arte e os métodos de identificação de aves',
            'birdwatching.articles.best-locations.title': 'Melhores localizações',
            'birdwatching.articles.best-locations.desc': 'Explore pontos quentes de observação de aves ao redor do mundo',
            'birdwatching.articles.seasonal-guide.title': 'Guia sazonal',
            'birdwatching.articles.seasonal-guide.desc': 'Planeie as suas atividades de observação de aves de acordo com as mudanças sazonais',
            'birdwatching.articles.photography-tips.title': 'Dicas de fotografia',
            'birdwatching.articles.photography-tips.desc': 'Conselhos práticos para capturar fotografias deslumbrantes de aves',
            'birdwatching.articles.behavior-observation.title': 'Observação de comportamento',
            'birdwatching.articles.behavior-observation.desc': 'Aprenda a observar e compreender o comportamento das aves',
            'birdwatching.articles.song-identification.title': 'Identificação de cantos',
            'birdwatching.articles.song-identification.desc': 'Técnicas para identificar diferentes espécies de aves pelo som',
            'birdwatching.articles.ethics-conservation.title': 'Ética e conservação',
            'birdwatching.articles.ethics-conservation.desc': 'Observação responsável de aves e contribuição para a conservação de aves',
            'birdwatching.articles.journal-keeping.title': 'Manutenção de diário',
            'birdwatching.articles.journal-keeping.desc': 'Como registar e organizar as suas experiências de observação de aves',
            'nav.home': 'Início',
            'nav.features': 'Recursos',
            'nav.about': 'Sobre',
            'nav.contact': 'Contato',
            'hero.title': 'Reconhecimento inteligente, captura e descoberta',
            'hero.description': 'BirdAiSnap é uma aplicação de reconhecimento inteligente alimentada por IA que permite identificação rápida de aves no seu ambiente enquanto revela os mistérios do mundo natural.',
            'hero.download': 'Baixar agora',
            'hero.learn': 'Saiba mais',
            'mockup.ai': 'Melhoria IA',
            'mockup.scan': 'Escanear',
            'mockup.sound': 'Som',
            'features.title': 'Recursos principais',
            'features.scan.title': 'Capturar e identificar',
            'features.scan.desc': 'Simplesmente tire uma fotografia ou carregue uma imagem existente para identificar instantaneamente espécies de aves com precisão',
            'features.sound.title': 'Reconhecimento acústico',
            'features.sound.desc': 'Grave vocalizações aviárias e identifique espécies através de análise acústica IA sofisticada',
            'features.nearby.title': 'Espécies aviárias locais',
            'features.nearby.desc': 'Descubra espécies de aves na sua vizinhança e explore padrões ecológicos regionais',
            'features.enhance.title': 'Melhoria inteligente',
            'features.enhance.desc': 'Utilize algoritmos IA avançados para melhorar a qualidade fotográfica e mostrar sujeitos aviários com clareza impressionante',
            'features.collection.title': 'Coleções pessoais',
            'features.collection.desc': 'Organize coleções aviárias personalizadas e documente cada expedição de observação de aves com registros detalhados',
            'features.info.title': 'Base de dados abrangente',
            'features.info.desc': 'Acesse informações ornitológicas extensas e repositórios de conhecimento científico a qualquer momento, em qualquer lugar',
            'features.knowledge.title': 'Perspectivas ornitológicas',
            'features.knowledge.desc': 'Explore guias abrangentes de observação de aves, descobertas científicas, cuidados aviários, relações ecológicas e significado cultural',
            'about.title': 'Sobre BirdAiSnap',
            'about.desc1': 'BirdAiSnap é uma aplicação de reconhecimento inteligente projetada especificamente para entusiastas de aves e exploradores da natureza. Dedicamo-nos a ajudar os usuários a desenvolver uma compreensão e apreciação mais profundas das magníficas aves na natureza através de tecnologia IA de ponta.',
            'about.desc2': 'Seja você um ornitólogo profissional ou um entusiasta da natureza curioso, BirdAiSnap oferece serviços de identificação de aves precisos e rápidos.',
            'about.stats.downloads': 'Downloads',
            'about.stats.species': 'Espécies de aves',
            'about.stats.accuracy': 'Taxa de precisão',
            'contact.title': 'Entre em contato',
            'contact.subtitle': 'Obter mais informações',
            'contact.desc': 'Se você tem alguma pergunta ou sugestão, sinta-se à vontade para nos contatar',
            'contact.email': 'E-mail:',
            'contact.form.name': 'Seu nome',
            'contact.form.email': 'Seu e-mail',
            'contact.form.message': 'Sua mensagem',
            'contact.form.submit': 'Enviar mensagem',
            'contact.email.title': '📧 Informações de e-mail',
            'contact.email.recipient': 'Destinatário:',
            'contact.email.subject': 'Assunto:',
            'contact.email.content': 'Conteúdo:',
            'contact.email.copy': 'Copiar informações de e-mail',
            'contact.email.open': 'Abrir cliente de e-mail',
            'footer.tagline': 'Reconhecimento inteligente, explorar a natureza',
            'footer.product': 'Produto',
            'footer.product.download': 'Baixar aplicativo',
            'footer.product.features': 'Recursos',
            'footer.product.guide': 'Guia do usuário',
            'footer.support': 'Suporte',
            'footer.support.help': 'Centro de ajuda',
            'footer.support.feedback': 'Feedback',
            'footer.support.privacy': 'Política de privacidade',
            'footer.contact': 'Contato',
            'footer.contact.email': 'Consulta por e-mail',
            'footer.copyright': '© 2024 BirdAiSnap. Todos os direitos reservados',
            'knowledge.hero.title': 'Centro de conhecimento de aves',
            'knowledge.hero.description': 'Explore o mundo fascinante das aves através de recursos de conhecimento abrangentes',
            'knowledge.categories.birdwatching': 'Observação de aves',
            'knowledge.categories.birdwatching.desc': 'Aprenda a arte da observação de aves e técnicas de identificação',
            'knowledge.categories.scientific': 'Maravilhas científicas',
            'knowledge.categories.scientific.desc': 'Descubra fatos científicos surpreendentes e pesquisas sobre aves',
            'knowledge.categories.petcare': 'Cuidados com aves de estimação',
            'knowledge.categories.petcare.desc': 'Guias de cuidados essenciais para proprietários e entusiastas de aves de estimação',
            'knowledge.categories.ecology': 'Ecologia aviária',
            'knowledge.categories.ecology.desc': 'Compreender habitats, migração e papéis ambientais das aves',
            'knowledge.categories.cultural': 'Simbolismo cultural',
            'knowledge.categories.cultural.desc': 'Aves na mitologia, arte, literatura e significado cultural',
            'knowledge.latest.title': 'Últimos artigos',
            'knowledge.articles.stats': 'artigos'
        }
    },
    'ru': { 
        name: 'Русский', 
        flag: '🇷🇺', 
        code: 'RU',
        translations: {
            'birdwatching.title': 'Руководство по наблюдению за птицами - BirdAiSnap',
            'birdwatching.header.title': 'Руководство по наблюдению за птицами',
            'birdwatching.intro.text': 'Добро пожаловать в наш всеобъемлющий раздел руководства по наблюдению за птицами. Здесь вы найдете обширные техники и знания наблюдения за птицами, от основ для начинающих до продвинутых навыков идентификации, помогающих вам лучше ценить и понимать мир птиц. Нажмите на любое изображение статьи ниже, чтобы глубоко погрузиться в тайны наблюдения за птицами.',
            'birdwatching.articles.getting-started.title': 'Руководство для начинающих',
            'birdwatching.articles.getting-started.desc': 'Всеобъемлющее введение в наблюдение за птицами для начинающих',
            'birdwatching.articles.essential-equipment.title': 'Необходимое оборудование',
            'birdwatching.articles.essential-equipment.desc': 'Узнайте о различных инструментах и оборудовании, необходимых для наблюдения за птицами',
            'birdwatching.articles.identification-techniques.title': 'Техники идентификации',
            'birdwatching.articles.identification-techniques.desc': 'Овладейте искусством и методами идентификации птиц',
            'birdwatching.articles.best-locations.title': 'Лучшие места',
            'birdwatching.articles.best-locations.desc': 'Исследуйте горячие точки наблюдения за птицами по всему миру',
            'birdwatching.articles.seasonal-guide.title': 'Сезонное руководство',
            'birdwatching.articles.seasonal-guide.desc': 'Планируйте свои активности наблюдения за птицами в соответствии с сезонными изменениями',
            'birdwatching.articles.photography-tips.title': 'Советы по фотографии',
            'birdwatching.articles.photography-tips.desc': 'Практические советы для съемки потрясающих фотографий птиц',
            'birdwatching.articles.behavior-observation.title': 'Наблюдение за поведением',
            'birdwatching.articles.behavior-observation.desc': 'Научитесь наблюдать и понимать поведение птиц',
            'birdwatching.articles.song-identification.title': 'Идентификация песен',
            'birdwatching.articles.song-identification.desc': 'Техники для идентификации различных видов птиц по звуку',
            'birdwatching.articles.ethics-conservation.title': 'Этика и сохранение',
            'birdwatching.articles.ethics-conservation.desc': 'Ответственное наблюдение за птицами и вклад в сохранение птиц',
            'birdwatching.articles.journal-keeping.title': 'Ведение дневника',
            'birdwatching.articles.journal-keeping.desc': 'Как записывать и организовывать ваши опыты наблюдения за птицами',
            'nav.home': 'Главная',
            'nav.features': 'Функции',
            'nav.about': 'О нас',
            'nav.contact': 'Контакты',
            'hero.title': 'Интеллектуальное распознавание, съемка и открытие',
            'hero.description': 'BirdAiSnap - это приложение интеллектуального распознавания на основе ИИ, которое обеспечивает быструю идентификацию птиц в вашем окружении, раскрывая тайны природного мира.',
            'hero.download': 'Скачать сейчас',
            'hero.learn': 'Узнать больше',
            'mockup.ai': 'Улучшение ИИ',
            'mockup.scan': 'Сканировать',
            'mockup.sound': 'Звук',
            'features.title': 'Основные функции',
            'features.scan.title': 'Захват и идентификация',
            'features.scan.desc': 'Просто сделайте фотографию или загрузите существующее изображение для мгновенной точной идентификации видов птиц',
            'features.sound.title': 'Акустическое распознавание',
            'features.sound.desc': 'Записывайте птичьи вокализации и идентифицируйте виды через сложный ИИ акустический анализ',
            'features.nearby.title': 'Местные виды птиц',
            'features.nearby.desc': 'Откройте для себя виды птиц в вашей окрестности и исследуйте региональные экологические модели',
            'features.enhance.title': 'Интеллектуальное улучшение',
            'features.enhance.desc': 'Используйте продвинутые ИИ алгоритмы для улучшения качества фотографий и демонстрации птичьих субъектов с потрясающей четкостью',
            'features.collection.title': 'Личные коллекции',
            'features.collection.desc': 'Курируйте персонализированные птичьи коллекции и документируйте каждую экспедицию наблюдения за птицами с подробными записями',
            'features.info.title': 'Комплексная база данных',
            'features.info.desc': 'Получайте доступ к обширной орнитологической информации и научным репозиториям знаний в любое время, в любом месте',
            'features.knowledge.title': 'Орнитологические перспективы',
            'features.knowledge.desc': 'Исследуйте комплексные руководства по наблюдению за птицами, научные открытия, уход за птицами, экологические отношения и культурное значение',
            'about.title': 'О BirdAiSnap',
            'about.desc1': 'BirdAiSnap - это приложение интеллектуального распознавания, специально разработанное для любителей птиц и исследователей природы. Мы посвящаем себя помощи пользователям в развитии более глубокого понимания и оценки великолепных птиц в природе через передовые ИИ технологии.',
            'about.desc2': 'Будь вы профессиональным орнитологом или любознательным любителем природы, BirdAiSnap предоставляет точные и быстрые услуги идентификации птиц.',
            'about.stats.downloads': 'Загрузки',
            'about.stats.species': 'Виды птиц',
            'about.stats.accuracy': 'Точность',
            'contact.title': 'Свяжитесь с нами',
            'contact.subtitle': 'Получить больше информации',
            'contact.desc': 'Если у вас есть вопросы или предложения, не стесняйтесь связаться с нами',
            'contact.email': 'Электронная почта:',
            'contact.form.name': 'Ваше имя',
            'contact.form.email': 'Ваша электронная почта',
            'contact.form.message': 'Ваше сообщение',
            'contact.form.submit': 'Отправить сообщение',
            'contact.email.title': '📧 Информация электронной почты',
            'contact.email.recipient': 'Получатель:',
            'contact.email.subject': 'Тема:',
            'contact.email.content': 'Содержание:',
            'contact.email.copy': 'Копировать информацию электронной почты',
            'contact.email.open': 'Открыть почтовый клиент',
            'footer.tagline': 'Интеллектуальное распознавание, исследуйте природу',
            'footer.product': 'Продукт',
            'footer.product.download': 'Скачать приложение',
            'footer.product.features': 'Функции',
            'footer.product.guide': 'Руководство пользователя',
            'footer.support': 'Поддержка',
            'footer.support.help': 'Центр помощи',
            'footer.support.feedback': 'Обратная связь',
            'footer.support.privacy': 'Политика конфиденциальности',
            'footer.contact': 'Контакты',
            'footer.contact.email': 'Консультация по электронной почте',
            'footer.copyright': '© 2024 BirdAiSnap. Все права защищены',
            'knowledge.hero.title': 'Центр знаний о птицах',
            'knowledge.hero.description': 'Исследуйте увлекательный мир птиц через комплексные ресурсы знаний',
            'knowledge.categories.birdwatching': 'Наблюдение за птицами',
            'knowledge.categories.birdwatching.desc': 'Изучите искусство наблюдения за птицами и техники идентификации',
            'knowledge.categories.scientific': 'Научные чудеса',
            'knowledge.categories.scientific.desc': 'Откройте для себя удивительные научные факты и исследования о птицах',
            'knowledge.categories.petcare': 'Уход за домашними птицами',
            'knowledge.categories.petcare.desc': 'Основные руководства по уходу для владельцев и любителей домашних птиц',
            'knowledge.categories.ecology': 'Птичья экология',
            'knowledge.categories.ecology.desc': 'Понимание среды обитания, миграции и экологических ролей птиц',
            'knowledge.categories.cultural': 'Культурная символика',
            'knowledge.categories.cultural.desc': 'Птицы в мифологии, искусстве, литературе и культурном значении',
            'knowledge.latest.title': 'Последние статьи',
            'knowledge.articles.stats': 'статей'
        }
    }
};

// 从 localStorage 获取保存的语言设置，如果没有则默认为英文
let currentLang = localStorage.getItem('selectedLanguage') || 'en';

// 创建语言下拉菜单
function createLanguageDropdown() {
    const languageSwitcher = document.querySelector('.language-switcher');
    if (!languageSwitcher) {
        console.log('Language switcher container not found');
        return;
    }

    // 清空现有内容
    languageSwitcher.innerHTML = '';

    const dropdown = document.createElement('div');
    dropdown.className = 'lang-dropdown';

    const button = document.createElement('button');
    button.className = 'lang-btn';
    button.innerHTML = `
        <span class="lang-icon">🌐</span>
        <span class="lang-text">Language</span>
        <span id="currentLang">${languages[currentLang] ? languages[currentLang].code : 'EN'}</span>
        <span class="dropdown-arrow">▼</span>
    `;

    const menu = document.createElement('div');
    menu.className = 'lang-menu';

    Object.keys(languages).forEach(langCode => {
        const option = document.createElement('div');
        option.className = `lang-option ${langCode === currentLang ? 'active' : ''}`;
        option.innerHTML = `
            <span class="flag">${languages[langCode].flag}</span>
            <span class="name">${languages[langCode].name}</span>
            <span class="code">${languages[langCode].code}</span>
        `;
        option.addEventListener('click', () => switchLanguage(langCode));
        menu.appendChild(option);
    });

    dropdown.appendChild(button);
    dropdown.appendChild(menu);
    languageSwitcher.appendChild(dropdown);

    button.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdown.classList.toggle('active');
    });

    document.addEventListener('click', () => {
        dropdown.classList.remove('active');
    });

    console.log('Language dropdown created successfully');
}

// 翻译页面内容
function translatePage(langCode) {
    if (!languages[langCode] || !languages[langCode].translations) {
        console.log('Translation not found for language:', langCode);
        return;
    }

    const translations = languages[langCode].translations;

    // 翻译所有带有data-i18n属性的元素
    const elementsToTranslate = document.querySelectorAll('[data-i18n]');
    
    elementsToTranslate.forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[key]) {
            element.textContent = translations[key];
        }
    });

    // 翻译placeholder属性
    const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
    placeholderElements.forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        if (translations[key]) {
            element.placeholder = translations[key];
        }
    });

    console.log('页面内容已翻译为:', languages[langCode].name);
}

// 切换语言
function switchLanguage(langCode) {
    if (!languages[langCode]) {
        console.log('Language not found:', langCode);
        return;
    }
    
    currentLang = langCode;
    
    // 保存语言设置到 localStorage
    localStorage.setItem('selectedLanguage', langCode);
    
    // 更新下拉菜单显示
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = languages[langCode].code;
    }

    // 更新选中状态
    const langOptions = document.querySelectorAll('.lang-option');
    langOptions.forEach(option => {
        option.classList.remove('active');
        if (option.innerHTML.includes(languages[langCode].code)) {
            option.classList.add('active');
        }
    });

    // 关闭下拉菜单
    const dropdown = document.querySelector('.lang-dropdown');
    if (dropdown) {
        dropdown.classList.remove('active');
    }

    // 翻译页面内容
    translatePage(langCode);

    console.log('切换到语言:', languages[langCode].name);
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, creating language dropdown...');
    
    // 检查 URL 参数中是否有语言设置
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang && languages[urlLang]) {
        currentLang = urlLang;
        localStorage.setItem('selectedLanguage', urlLang);
    }
    
    setTimeout(() => {
        // 只有在找到语言切换器容器时才创建下拉菜单
        if (document.querySelector('.language-switcher')) {
            createLanguageDropdown();
        }
        // 初始化时应用当前语言
        translatePage(currentLang);
    }, 100);
});

// 为链接添加语言参数的函数
function addLanguageParam(event, linkElement) {
    try {
        if (event) event.preventDefault();
        if (!linkElement) return;
        
        const currentLang = localStorage.getItem('selectedLanguage') || 'en';
        const originalHref = linkElement.getAttribute('href');
        
        if (!originalHref) return;
        
        // 根据当前语言构建对应的URL路径（不使用URL参数）
        let newHref = originalHref;
        if (currentLang !== 'en') {
            // 将 en/ 替换为对应语言的路径
            newHref = originalHref.replace('en/', currentLang + '/');
        }
        
        // 直接跳转到新URL路径，不添加lang参数
        window.location.href = newHref;
    } catch (error) {
        console.log('Link navigation error:', error);
    }
}

// 为分类页面导航的函数（直接使用路径，不添加URL参数）
function navigateWithLanguage(pageName) {
    try {
        if (!pageName) return;
        
        const currentLang = localStorage.getItem('selectedLanguage') || 'en';
        
        // 对于分类页面，如果不是英文，需要检查是否已经包含语言前缀
        let newUrl = pageName;
        if (currentLang !== 'en' && !pageName.startsWith(currentLang + '/')) {
            // 如果页面名称不包含语言前缀，添加语言参数
            const separator = pageName.includes('?') ? '&' : '?';
            newUrl = pageName + separator + 'lang=' + currentLang;
        }
        
        // 跳转到新URL
        window.location.href = newUrl;
    } catch (error) {
        console.log('Navigation error:', error);
    }
}

// 为文章页面添加语言检测和跳转功能
function handleArticleLanguageRedirect() {
    try {
        // 检查当前页面是否是文章页面
        const path = window.location.pathname;
        if (path.includes('/knowledge/') || path.includes('/birdwatching/') || 
            path.includes('/pet-care/') || path.includes('/scientific-wonders/') || 
            path.includes('/ecology/') || path.includes('/cultural-symbolism/')) {
            
            const pathParts = path.split('/').filter(part => part.length > 0);
            const currentPageLang = pathParts[0]; // 获取路径中的语言代码
            const savedLang = localStorage.getItem('selectedLanguage') || 'en';
            
            // 优先使用路径中的语言，如果路径中没有语言或语言不匹配，则使用保存的语言
            let targetLang = savedLang;
            
            // 检查URL参数中是否有语言设置（用于兼容旧链接）
            const urlParams = new URLSearchParams(window.location.search);
            const urlLang = urlParams.get('lang');
            if (urlLang && languages[urlLang]) {
                targetLang = urlLang;
                // 如果URL参数中有语言，更新localStorage并重定向到纯路径版本
                localStorage.setItem('selectedLanguage', urlLang);
                if (pathParts.length > 0) {
                    pathParts[0] = urlLang;
                    const newPath = '/' + pathParts.join('/');
                    const newUrl = window.location.origin + newPath;
                    window.location.href = newUrl;
                    return;
                }
            }
            
            // 如果当前页面有有效的语言代码，更新localStorage为当前语言
            if (languages[currentPageLang]) {
                // 用户直接访问了特定语言页面，更新localStorage为当前语言
                localStorage.setItem('selectedLanguage', currentPageLang);
                console.log(`Article page language updated to: ${currentPageLang}`);
            }
            
            // 不再进行自动语言跳转，尊重用户的直接访问意图
        }
    } catch (error) {
        console.log('Language redirect error:', error);
    }
}

// 安全的页面加载处理
function safeInitialize() {
    try {
        handleArticleLanguageRedirect();
    } catch (error) {
        console.log('Initialization error:', error);
    }
}

// 在页面加载时检查语言跳转
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', safeInitialize);
} else {
    safeInitialize();
}
