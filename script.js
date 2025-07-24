// 语言数据
const languages = {
    'en': {
        'nav.home': 'Home',
        'nav.features': 'Features',
        'nav.about': 'About',
        'nav.contact': 'Contact',
        'nav.language': 'Language',
        'hero.title': 'Smart Recognition, Snap & Know',
        'hero.description': 'BirdAiSnap is an AI-powered smart recognition app that helps you quickly identify birds around you and explore the unknown world.',
        'hero.download': 'Download Now',
        'hero.learn': 'Learn More',
        'mockup.ai': 'AI Enhance',
        'mockup.scan': 'Scan',
        'mockup.sound': 'Sound',
        'features.title': 'Core Features',
        'features.scan.title': 'Scan & Identify',
        'features.scan.desc': 'Simply take a photo or upload an image to quickly identify bird species',
        'features.sound.title': 'Sound Recognition',
        'features.sound.desc': 'Record bird calls and identify species through AI analysis',
        'features.nearby.title': 'Nearby Birds',
        'features.nearby.desc': 'Search for birds near your location and learn about local ecology',
        'features.enhance.title': 'AI Enhancement',
        'features.enhance.desc': 'Intelligently enhance photo effects to make your bird photos more beautiful',
        'features.collection.title': 'Collection Management',
        'features.collection.desc': 'Create personal bird collections and record every birdwatching experience',
        'features.info.title': 'Detailed Information',
        'features.info.desc': 'Access detailed bird information and scientific knowledge anytime, anywhere',
        'features.knowledge.title': 'More Bird Knowledge',
        'features.knowledge.desc': 'Explore bird watching, scientific wonders, pet care, ecology, and cultural symbolism',
        'about.title': 'About BirdAiSnap',
        'about.desc1': 'BirdAiSnap is an intelligent recognition app designed specifically for bird enthusiasts and nature explorers. We are committed to helping users better understand and appreciate the beautiful birds in nature through advanced AI technology.',
        'about.desc2': 'Whether you are a professional ornithologist or a curious nature lover, BirdAiSnap can provide you with accurate and fast bird identification services.',
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
        // Birdwatching page translations
        'nav.knowledge': 'Knowledge',
        'birdwatching.hero.title': '🔍 Bird Watching',
        'birdwatching.hero.subtitle': 'Master the art of bird observation and identification techniques',
        'birdwatching.category': 'Bird Watching',
        'birdwatching.readmore': 'Read More',
        'birdwatching.articles.equipment.title': 'Essential Bird Watching Equipment',
        'birdwatching.articles.equipment.desc': 'Discover the must-have tools and equipment for successful bird watching adventures, from binoculars to field guides.',
        'birdwatching.articles.identification.title': 'Bird Identification Techniques',
        'birdwatching.articles.identification.desc': 'Learn proven methods for identifying birds by size, shape, color, behavior, and habitat.',
        'birdwatching.articles.locations.title': 'Best Bird Watching Locations',
        'birdwatching.articles.locations.desc': 'Explore the top bird watching destinations around the world and what makes them special.',
        'birdwatching.articles.seasonal.title': 'Seasonal Bird Watching Guide',
        'birdwatching.articles.seasonal.desc': 'Understand how bird activity changes throughout the year and plan your observations accordingly.',
        'birdwatching.articles.photography.title': 'Photography Tips for Bird Watchers',
        'birdwatching.articles.photography.desc': 'Capture stunning bird photos with these essential photography techniques and equipment recommendations.',
        'birdwatching.articles.behavior.title': 'Bird Behavior Observation',
        'birdwatching.articles.behavior.desc': 'Learn to interpret bird behaviors and understand what different actions and postures mean.',
        'birdwatching.articles.songs.title': 'Bird Song Identification',
        'birdwatching.articles.songs.desc': 'Master the art of identifying birds by their songs and calls, a crucial skill for bird watchers.',
        'birdwatching.articles.ethics.title': 'Bird Watching Ethics and Conservation',
        'birdwatching.articles.ethics.desc': 'Understand the importance of ethical bird watching practices and how to minimize your impact on birds.',
        'birdwatching.articles.journal.title': 'Keeping a Bird Watching Journal',
        'birdwatching.articles.journal.desc': 'Learn how to maintain detailed records of your bird watching experiences and observations.',
        'birdwatching.articles.beginners.title': 'Bird Watching for Beginners',
        'birdwatching.articles.beginners.desc': 'A comprehensive guide for newcomers to bird watching, covering basics and getting started tips.',
        'footer.description': 'Smart bird recognition powered by AI technology',
        'footer.quicklinks': 'Quick Links',
        'footer.download': 'Download App',
        'footer.email': 'Email: lingjuetech@gmail.com',
        // Detailed page translations
        'equipment.hero.title': '🔭 Essential Bird Watching Equipment',
        'equipment.hero.subtitle': 'Discover the must-have tools and equipment for successful bird watching adventures',
        'identification.hero.title': '🔍 Bird Identification Techniques',
        'identification.hero.subtitle': 'Master the art of identifying birds through systematic observation',
        'locations.hero.title': '🌍 Best Bird Watching Locations',
        'locations.hero.subtitle': 'Discover the world\'s premier birding destinations and hidden gems',
        'seasonal.hero.title': '📅 Seasonal Bird Watching Guide',
        'seasonal.hero.subtitle': 'Discover how bird activity changes throughout the year and plan your observations',
        'photography.hero.title': '📸 Photography Tips for Bird Watchers',
        'photography.hero.subtitle': 'Capture stunning bird photos with essential techniques and equipment',
        'behavior.hero.title': '🎭 Bird Behavior Observation',
        'behavior.hero.subtitle': 'Learn to interpret bird behaviors and understand their fascinating world',
        'songs.hero.title': '🎵 Bird Song Identification',
        'songs.hero.subtitle': 'Master the art of identifying birds by their songs and calls',
        'ethics.hero.title': '🤝 Bird Watching Ethics and Conservation',
        'ethics.hero.subtitle': 'Responsible birding practices that protect the birds we love to observe',
        'journal.hero.title': '📔 Keeping a Bird Watching Journal',
        'journal.hero.subtitle': 'Document your birding adventures and build a personal record of discoveries',
        'beginners.hero.title': '🌟 Bird Watching for Beginners',
        'beginners.hero.subtitle': 'Your complete guide to starting an amazing birding journey',
        
        // Scientific Wonders translations
        'scientific.hero.title': '🔬 Scientific Wonders',
        'scientific.hero.subtitle': 'Amazing discoveries and scientific insights about birds',
        'scientific.category': 'Scientific Wonders',
        'scientific.articles.flight.title': 'The Mechanics of Bird Flight',
        'scientific.articles.flight.desc': 'Discover the fascinating physics and biomechanics behind bird flight, from wing structure to aerodynamic principles.',
        'scientific.articles.magnetic.title': 'Magnetic Navigation in Birds',
        'scientific.articles.magnetic.desc': 'Explore how birds use Earth\'s magnetic field for navigation during migration and daily activities.',
        'scientific.articles.hummingbird.title': 'Hummingbird Flight Mechanics',
        'scientific.articles.hummingbird.desc': 'Uncover the unique flight capabilities of hummingbirds, including hovering and backward flight.',
        'scientific.articles.intelligence.title': 'Bird Intelligence and Cognition',
        'scientific.articles.intelligence.desc': 'Delve into the remarkable intelligence of birds, from problem-solving to tool use.',
        'scientific.articles.feathers.title': 'The Structure and Function of Feathers',
        'scientific.articles.feathers.desc': 'Learn about the complex structure of feathers and their multiple functions.',
        'scientific.articles.vision.title': 'Extraordinary Bird Vision',
        'scientific.articles.vision.desc': 'Discover how birds see the world with their superior vision capabilities.',
        'scientific.articles.eggs.title': 'The Science of Egg Development',
        'scientific.articles.eggs.desc': 'Explore the remarkable process of avian embryonic development.',
        'scientific.articles.communication.title': 'Bird Communication and Vocalizations',
        'scientific.articles.communication.desc': 'Understand the complex world of bird communication and song learning.',
        'scientific.articles.migration.title': 'Migration Physiology',
        'scientific.articles.migration.desc': 'Learn about the physiological adaptations that enable long-distance migration.',
        'scientific.articles.biomechanics.title': 'Biomechanics of Bird Movement',
        'scientific.articles.biomechanics.desc': 'Explore the biomechanical principles behind various bird movements.',
        
        // Pet Care translations
        'petcare.hero.title': '🐦 Pet Care',
        'petcare.hero.subtitle': 'Complete guide to caring for your feathered companions',
        'petcare.category': 'Pet Care',
        
        // Ecology translations
        'ecology.hero.title': '🌿 Ecology',
        'ecology.hero.subtitle': 'Understanding bird ecology and environmental relationships',
        'ecology.category': 'Ecology'
    },
    'zh': {
        'nav.home': '首页',
        'nav.features': '功能',
        'nav.about': '关于',
        'nav.contact': '联系',
        'nav.language': '语言',
        'hero.title': '智能识别，一拍即知',
        'hero.description': 'BirdAiSnap是一款基于AI技术的智能识别应用，帮助您快速识别身边的鸟类，探索未知的世界。',
        'hero.download': '立即下载',
        'hero.learn': '了解更多',
        'mockup.ai': 'AI增强',
        'mockup.scan': '拍照识别',
        'mockup.sound': '声音识别',
        'features.title': '核心功能',
        'features.scan.title': '扫描识别',
        'features.scan.desc': '只需拍照或上传图片，即可快速识别鸟类品种',
        'features.sound.title': '声音识别',
        'features.sound.desc': '录制鸟类叫声，通过AI分析识别鸟类品种',
        'features.nearby.title': '附近鸟类',
        'features.nearby.desc': '根据位置搜索附近的鸟类，了解当地生态',
        'features.enhance.title': 'AI美化',
        'features.enhance.desc': '智能增强照片效果，让您的鸟类照片更加精美',
        'features.collection.title': '收藏管理',
        'features.collection.desc': '创建个人鸟类收藏，记录每一次观鸟体验',
        'features.info.title': '详细信息',
        'features.info.desc': '随时随地查看鸟类详细信息和科普知识',
        'features.knowledge.title': '更多鸟类知识',
        'features.knowledge.desc': '探索鸟类观察、科学奇闻、宠物护理、生态学和文化象征',
        'about.title': '关于 BirdAiSnap',
        'about.desc1': 'BirdAiSnap是一款专为鸟类爱好者和自然探索者设计的智能识别应用。我们致力于通过先进的AI技术，帮助用户更好地了解和欣赏自然界的美丽鸟类。',
        'about.desc2': '无论您是专业的鸟类学家，还是对自然充满好奇的普通用户，BirdAiSnap都能为您提供准确、快速的鸟类识别服务。',
        'about.stats.downloads': '用户下载',
        'about.stats.species': '鸟类物种',
        'about.stats.accuracy': '识别准确率',
        'contact.title': '联系我们',
        'contact.subtitle': '获取更多信息',
        'contact.desc': '如果您有任何问题或建议，欢迎联系我们',
        'contact.email': '邮箱：',
        'contact.form.name': '您的姓名',
        'contact.form.email': '您的邮箱',
        'contact.form.message': '您的消息',
        'contact.form.submit': '发送消息',
        'contact.email.title': '📧 邮件信息',
        'contact.email.recipient': '收件人：',
        'contact.email.subject': '主题：',
        'contact.email.content': '内容：',
        'contact.email.copy': '复制邮件信息',
        'contact.email.open': '打开邮件客户端',
        'footer.tagline': '智能识别，探索自然',
        'footer.product': '产品',
        'footer.product.download': '下载APP',
        'footer.product.features': '功能介绍',
        'footer.product.guide': '使用指南',
        'footer.support': '支持',
        'footer.support.help': '帮助中心',
        'footer.support.feedback': '反馈意见',
        'footer.support.privacy': '隐私政策',
        'footer.contact': '联系我们',
        'footer.contact.email': '邮箱咨询',
        'footer.copyright': '© 2024 BirdAiSnap. 版权所有',
        // Birdwatching page translations
        'nav.knowledge': '知识中心',
        'birdwatching.hero.title': '🔍 观鸟指南',
        'birdwatching.hero.subtitle': '掌握鸟类观察和识别的艺术技巧',
        'birdwatching.category': '观鸟指南',
        'birdwatching.readmore': '阅读更多',
        'birdwatching.articles.equipment.title': '观鸟必备装备',
        'birdwatching.articles.equipment.desc': '发现成功观鸟冒险所需的必备工具和装备，从双筒望远镜到野外指南。',
        'birdwatching.articles.identification.title': '鸟类识别技巧',
        'birdwatching.articles.identification.desc': '学习通过大小、形状、颜色、行为和栖息地识别鸟类的经验证方法。',
        'birdwatching.articles.locations.title': '最佳观鸟地点',
        'birdwatching.articles.locations.desc': '探索世界各地顶级观鸟目的地及其特色之处。',
        'birdwatching.articles.seasonal.title': '季节性观鸟指南',
        'birdwatching.articles.seasonal.desc': '了解鸟类活动如何随季节变化，并相应规划您的观察活动。',
        'birdwatching.articles.photography.title': '观鸟者摄影技巧',
        'birdwatching.articles.photography.desc': '通过这些基本摄影技巧和设备推荐，拍摄令人惊叹的鸟类照片。',
        'birdwatching.articles.behavior.title': '鸟类行为观察',
        'birdwatching.articles.behavior.desc': '学会解读鸟类行为，理解不同动作和姿态的含义。',
        'birdwatching.articles.songs.title': '鸟类鸣声识别',
        'birdwatching.articles.songs.desc': '掌握通过鸟类鸣声和叫声识别鸟类的艺术，这是观鸟者的重要技能。',
        'birdwatching.articles.ethics.title': '观鸟伦理与保护',
        'birdwatching.articles.ethics.desc': '了解道德观鸟实践的重要性以及如何最小化对鸟类的影响。',
        'birdwatching.articles.journal.title': '观鸟日志记录',
        'birdwatching.articles.journal.desc': '学习如何详细记录您的观鸟体验和观察结果。',
        'birdwatching.articles.beginners.title': '观鸟入门指南',
        'birdwatching.articles.beginners.desc': '为观鸟新手提供的综合指南，涵盖基础知识和入门技巧。',
        'footer.description': '基于AI技术的智能鸟类识别',
        'footer.quicklinks': '快速链接',
        'footer.download': '下载应用',
        'footer.email': '邮箱：lingjuetech@gmail.com',
        
        // Detailed page translations
        // Essential Equipment page
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'equipment.binoculars.title': '🔍 双筒望远镜 - 您的主要工具',
        'equipment.binoculars.desc': '双筒望远镜是任何观鸟者最重要的装备。它们将远处的鸟类清晰地呈现在眼前，让您能够观察到肉眼无法看到的细节。',
        'equipment.guides.title': '📚 野外指南和参考资料',
        'equipment.guides.desc': '全面的野外指南是您识别遇到的鸟类的伙伴。现代野外指南包含详细的插图、分布图和行为描述。',
        'equipment.camera.title': '📷 鸟类摄影设备',
        'equipment.camera.desc': '虽然不是观鸟的必需品，但相机可以让您捕捉和分享您的发现。鸟类摄影需要特殊考虑。',
        'equipment.gear.title': '🎒 其他必需装备',
        'equipment.gear.desc': '除了基础装备外，一些额外的物品可以显著改善您的观鸟体验和野外舒适度。',
        
        // Identification Techniques page
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '通过系统观察掌握鸟类识别的艺术',
        'identification.giss.title': '🎯 GISS 方法',
        'identification.giss.desc': 'GISS代表"整体大小和形状印象" - 这是经验丰富的观鸟者用来快速缩小鸟类识别范围的基本技术。',
        'identification.fieldmarks.title': '🏷️ 关键野外特征',
        'identification.fieldmarks.desc': '野外特征是区分一个物种与另一个物种的特定物理特征。学会快速发现和评估这些特征对准确识别至关重要。',
        'identification.behavior.title': '🦅 行为识别',
        'identification.behavior.desc': '鸟类行为通常提供最可靠的识别线索。鸟类如何移动、觅食和与环境互动可能比外观更具特色。',
        
        // Best Locations page
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝地',
        'locations.parks.title': '🏞️ 国家公园和保护区',
        'locations.parks.desc': '国家公园和野生动物保护区提供世界上一些最好的观鸟机会。这些保护区维护着多样的栖息地。',
        'locations.wetlands.title': '💧 湿地和海岸地区',
        'locations.wetlands.desc': '湿地是地球上最富有生产力的鸟类栖息地之一。这些地区支持着令人难以置信的多样性。',
        'locations.tropical.title': '🌴 热带热点',
        'locations.tropical.desc': '热带地区拥有地球上最大的鸟类多样性。这些地区提供观赏其他地方找不到的奇异物种的机会。',
        
        // Seasonal Guide page
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随年份变化并规划您的观察',
        'seasonal.spring.title': '🌸 春季：更新的季节',
        'seasonal.spring.desc': '春季可以说是观鸟最令人兴奋的时候。随着气温回暖和日照时间增加，鸟类变得非常活跃。',
        'seasonal.summer.title': '☀️ 夏季：家庭生活和丰富',
        'seasonal.summer.desc': '夏季观鸟专注于繁殖行为、家庭群体和常驻物种的丰富性。',
        'seasonal.fall.title': '🍂 秋季：南迁的伟大旅程',
        'seasonal.fall.desc': '秋季迁徙比春季更为持久，为观察迁徙鸟类提供了更长的机会。',
        'seasonal.winter.title': '❄️ 冬季：顽强的幸存者和访客',
        'seasonal.winter.desc': '冬季观鸟揭示了勇敢面对寒冷温度和有限食物来源的顽强物种。',
        
        // Photography Tips page
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '用基本技巧和设备拍摄令人惊叹的鸟类照片',
        'photography.equipment.title': '📷 相机设备要点',
        'photography.equipment.desc': '鸟类摄影需要专门的设备来捕捉远距离、快速移动的主体。',
        'photography.lens.title': '🔍 镜头选择和焦距',
        'photography.lens.desc': '镜头可以说是鸟类摄影最重要的组件。更长的焦距让您能够保持距离。',
        'photography.settings.title': '⚙️ 鸟类摄影的相机设置',
        'photography.settings.desc': '正确的相机设置对于清晰、曝光良好的鸟类照片至关重要。',
        
        // Behavior Observation page
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为，理解它们迷人的世界',
        'behavior.territorial.title': '🏠 领域和社会行为',
        'behavior.territorial.desc': '理解领域和社会行为提供了对鸟类心理的洞察，有助于预测它们的行动。',
        'behavior.feeding.title': '🍽️ 觅食行为和策略',
        'behavior.feeding.desc': '觅食行为揭示了鸟类的生态位，并提供了极好的观察机会。',
        'behavior.courtship.title': '💕 求偶和交配行为',
        'behavior.courtship.desc': '求偶行为是最壮观和复杂的鸟类行为之一。',
        
        // Song Identification page
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'songs.understanding.title': '🎼 理解鸟类发声',
        'songs.understanding.desc': '鸟类的鸣声和叫声服务于不同目的，提供重要的识别线索。',
        'songs.patterns.title': '🔤 学习鸣声模式和助记符',
        'songs.patterns.desc': '助记符是帮助观鸟者记住和识别鸟类鸣声的记忆辅助工具。',
        'songs.listening.title': '👂 发展您的听力技能',
        'songs.listening.desc': '有效的鸟类鸣声识别需要发展敏锐的听力技能。',
        
        // Ethics and Conservation page
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'ethics.foundation.title': '🌱 道德观鸟的基础',
        'ethics.foundation.desc': '道德观鸟建立在鸟类和其栖息地的福利必须始终优先于我们观察或拍摄它们的愿望这一原则之上。',
        'ethics.guidelines.title': '✅ 道德观鸟指南',
        'ethics.guidelines.desc': '遵循既定指南有助于确保您的观鸟活动产生最小的负面影响。',
        'ethics.breeding.title': '🥚 繁殖季节的特殊考虑',
        'ethics.breeding.desc': '繁殖季节需要观鸟者格外谨慎和敏感。',
        
        // Journal Keeping page
        'journal.hero.title': '📔 观鸟日志记录',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'journal.why.title': '📝 为什么要记录观鸟日志？',
        'journal.why.desc': '观鸟日志将随意的观察转化为有价值的个人体验、模式和发现数据库。',
        'journal.information.title': '📋 记录的基本信息',
        'journal.information.desc': '有效的观鸟日志既捕捉基本识别信息，也记录提供背景的详细观察。',
        'journal.digital.title': '📱 数字 vs 纸质日志',
        'journal.digital.desc': '数字和传统纸质日志都有优势。最佳选择取决于您的个人偏好。',
        
        // Beginners Guide page
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始令人惊叹的观鸟之旅的完整指南',
        'beginners.welcome.title': '🚀 欢迎来到观鸟世界！',
        'beginners.welcome.desc': '观鸟是世界上最有回报和最容易接触的爱好之一。',
        'beginners.getting.title': '🎒 入门：您的第一步',
        'beginners.getting.desc': '开始您的观鸟之旅不需要昂贵的设备或广泛的知识。',
        'beginners.common.title': '🏠 首先学习的常见鸟类',
        'beginners.common.desc': '从常见、易于识别的物种开始建立信心，为学习更具挑战性的鸟类提供基础。',
        'beginners.techniques.title': '🔍 基本识别技巧',
        'beginners.techniques.desc': '学习系统的鸟类识别方法使过程不那么令人困惑，更加成功。',
        
        // Detailed page translations
        // Essential Equipment page
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'equipment.binoculars.title': '🔍 双筒望远镜 - 您的主要工具',
        'equipment.binoculars.choosing': '选择合适的双筒望远镜',
        'equipment.fieldguides.title': '📚 野外指南和参考资料',
        'equipment.camera.title': '📷 鸟类摄影相机设备',
        'equipment.additional.title': '🎒 其他必需装备',
        'equipment.specialized.title': '🔧 专业装备',
        'equipment.budget.title': '💡 预算友好的替代方案',
        
        // Identification Techniques page
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '通过系统观察掌握识别鸟类的艺术',
        'identification.giss.title': '🎯 GISS 方法',
        'identification.fieldmarks.title': '🏷️ 关键野外特征',
        'identification.behavior.title': '🦅 行为识别',
        'identification.feeding.title': '🍽️ 觅食行为分析',
        'identification.habitat.title': '🌲 基于栖息地的识别',
        'identification.seasonal.title': '📅 季节和时间线索',
        'identification.advanced.title': '🔧 高级识别技巧',
        
        // Best Locations page
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝石',
        'locations.parks.title': '🏞️ 国家公园和保护区',
        'locations.wetlands.title': '💧 湿地和海岸地区',
        'locations.tropical.title': '🌴 热带热点',
        'locations.mountain.title': '⛰️ 山地和高山地区',
        'locations.urban.title': '🏙️ 城市观鸟宝地',
        'locations.migration.title': '🛤️ 迁徙走廊',
        'locations.local.title': '🏡 寻找本地热点',
        
        // Seasonal Guide page
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随年份变化并规划您的观察',
        'seasonal.spring.title': '🌸 春季：更新的季节',
        'seasonal.summer.title': '☀️ 夏季：家庭生活和丰富',
        'seasonal.fall.title': '🍂 秋季：南迁的伟大旅程',
        'seasonal.winter.title': '❄️ 冬季：顽强的幸存者和访客',
        'seasonal.planning.title': '📊 规划您的观鸟年',
        
        // Photography Tips page
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '通过基本技巧和设备拍摄令人惊叹的鸟类照片',
        'photography.equipment.title': '📷 相机设备要点',
        'photography.lens.title': '🔍 镜头选择和焦距',
        'photography.settings.title': '⚙️ 鸟类摄影相机设置',
        'photography.composition.title': '🎨 构图和艺术技巧',
        'photography.behavior.title': '🎭 捕捉行为和动作',
        'photography.ethics.title': '🤝 道德鸟类摄影',
        'photography.processing.title': '🖥️ 鸟类照片后期处理',
        
        // Behavior Observation page
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为，理解它们迷人的世界',
        'behavior.territorial.title': '🏠 领域和社会行为',
        'behavior.feeding.title': '🍽️ 觅食行为和策略',
        'behavior.courtship.title': '💕 求偶和交配行为',
        'behavior.parental.title': '👨‍👩‍👧‍👦 亲子关系和家庭动态',
        'behavior.flocking.title': '🐦‍⬛ 群体和群体动态',
        'behavior.communication.title': '📢 沟通和发声',
        
        // Song Identification page
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'songs.understanding.title': '🎼 理解鸟类发声',
        'songs.mnemonics.title': '🔤 学习鸣声模式和助记符',
        'songs.listening.title': '👂 发展您的听力技能',
        'songs.variations.title': '🌍 地区变异和方言',
        'songs.technology.title': '📱 鸣声学习的技术和工具',
        'songs.seasonal.title': '📅 发声的季节变化',
        
        // Ethics and Conservation page
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'ethics.foundation.title': '🌱 道德观鸟的基础',
        'ethics.guidelines.title': '✅ 道德观鸟指南',
        'ethics.breeding.title': '🥚 繁殖季节的特殊考虑',
        'ethics.threats.title': '🌍 保护威胁和挑战',
        'ethics.contributing.title': '📊 通过观鸟为保护做贡献',
        'ethics.habitat.title': '🌿 支持栖息地保护',
        'ethics.future.title': '🔮 道德观鸟的未来',
        
        // Journal Keeping page
        'journal.hero.title': '📔 观鸟日志记录',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'journal.why.title': '📝 为什么要记录观鸟日志？',
        'journal.information.title': '📋 记录的基本信息',
        'journal.digital.title': '📱 数字 vs 纸质日志',
        'journal.sketches.title': '🎨 添加素描和视觉元素',
        'journal.analyzing.title': '📊 分析您的记录',
        'journal.sharing.title': '🤝 分享和贡献您的记录',
        
        // Beginners Guide page
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始令人惊叹的观鸟之旅的完整指南',
        'beginners.welcome.title': '🚀 欢迎来到观鸟世界！',
        'beginners.getting.title': '🎒 入门：您的第一步',
        'beginners.common.title': '🏠 首先学习的常见鸟类',
        'beginners.identification.title': '🔍 基本识别技巧',
        'beginners.where.title': '📍 去哪里观鸟',
        'beginners.mistakes.title': '⚠️ 避免常见的初学者错误',
        'beginners.building.title': '📈 随时间建立您的技能',
        'beginners.community.title': '🤝 与观鸟社区联系',
        
        // Detailed page translations
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '掌握通过系统观察识别鸟类的艺术',
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝地',
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随季节变化并规划观察',
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '通过基本技巧和设备拍摄令人惊叹的鸟类照片',
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为，理解它们的迷人世界',
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'journal.hero.title': '📔 观鸟日志记录',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始精彩观鸟之旅的完整指南',
        // Equipment page
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'equipment.binoculars.title': '🔍 双筒望远镜 - 您的主要工具',
        'equipment.binoculars.desc': '双筒望远镜是任何观鸟者最重要的装备。它们能让远处的鸟类清晰可见，让您观察到肉眼无法看到的细节。',
        'equipment.guides.title': '📚 野外指南和参考资料',
        'equipment.guides.desc': '全面的野外指南是您识别遇到的鸟类的伴侣。现代野外指南包括详细的插图、分布图和行为描述。',
        'equipment.camera.title': '📷 鸟类摄影相机设备',
        'equipment.camera.desc': '虽然不是观鸟必需品，但相机可以让您捕捉和分享您的发现。鸟类摄影需要特殊考虑。',
        'equipment.additional.title': '🎒 其他必需装备',
        'equipment.additional.desc': '除了基础装备，还有几个额外物品可以显著改善您的观鸟体验和野外舒适度。',
        // Identification page
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '通过系统观察掌握识别鸟类的艺术',
        'identification.giss.title': '🎯 GISS 方法',
        'identification.giss.desc': 'GISS代表"整体大小和形状印象" - 这是经验丰富的观鸟者用来快速缩小鸟类识别范围的基本技术。',
        'identification.fieldmarks.title': '🏷️ 关键野外特征',
        'identification.fieldmarks.desc': '野外特征是区分一个物种与另一个物种的特定物理特征。学会快速发现和评估这些特征对准确识别至关重要。',
        'identification.behavior.title': '🦅 行为识别',
        'identification.behavior.desc': '鸟类行为通常提供最可靠的识别线索。鸟类如何移动、觅食和与环境互动可能比外观更具特色。',
        // Locations page
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝石',
        'locations.parks.title': '🏞️ 国家公园和保护区',
        'locations.parks.desc': '国家公园和野生动物保护区提供世界上一些最好的观鸟机会。这些保护区域维护着多样的栖息地。',
        'locations.wetlands.title': '💧 湿地和海岸地区',
        'locations.wetlands.desc': '湿地是地球上最富有生产力的鸟类栖息地之一。这些地区支持令人难以置信的多样性。',
        'locations.tropical.title': '🌴 热带热点',
        'locations.tropical.desc': '热带地区拥有地球上最大的鸟类多样性。这些地区提供观看其他地方找不到的奇异物种的机会。',
        // Seasonal page
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随年份变化并规划您的观察',
        'seasonal.spring.title': '🌸 春季：更新的季节',
        'seasonal.spring.desc': '春季可以说是观鸟最令人兴奋的时候。随着气温回暖和日照时间增加，鸟类变得非常活跃。',
        'seasonal.summer.title': '☀️ 夏季：家庭生活和丰富',
        'seasonal.summer.desc': '夏季观鸟专注于繁殖行为、家庭群体和常驻物种的丰富性。',
        'seasonal.fall.title': '🍂 秋季：南迁的伟大旅程',
        'seasonal.fall.desc': '秋季迁徙比春季更持久，为观察迁徙鸟类提供了更长的机会。',
        'seasonal.winter.title': '❄️ 冬季：顽强的幸存者和访客',
        'seasonal.winter.desc': '冬季观鸟揭示了勇敢面对寒冷温度和有限食物来源的顽强物种。',
        // Photography page
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '用基本技巧和设备拍摄令人惊叹的鸟类照片',
        'photography.equipment.title': '📷 相机设备要点',
        'photography.equipment.desc': '鸟类摄影需要专门的设备来捕捉远距离、快速移动的主体。',
        'photography.lens.title': '🔍 镜头选择和焦距',
        'photography.lens.desc': '镜头可以说是鸟类摄影最重要的组件。更长的焦距让您保持距离的同时用主体填满画面。',
        'photography.settings.title': '⚙️ 鸟类摄影相机设置',
        'photography.settings.desc': '正确的相机设置对于清晰、曝光良好的鸟类照片至关重要。',
        // Behavior page
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为并理解它们迷人的世界',
        'behavior.territorial.title': '🏠 领域和社会行为',
        'behavior.territorial.desc': '理解领域和社会行为提供了对鸟类心理的洞察，有助于预测它们的行动。',
        'behavior.feeding.title': '🍽️ 觅食行为和策略',
        'behavior.feeding.desc': '觅食行为揭示了鸟类的生态位，并提供了极好的观察机会。',
        'behavior.courtship.title': '💕 求偶和交配行为',
        'behavior.courtship.desc': '求偶行为是最壮观和复杂的鸟类行为之一。',
        // Song identification page
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'songs.understanding.title': '🎼 理解鸟类发声',
        'songs.understanding.desc': '鸟类的鸣声和叫声服务于不同目的，提供关键的识别线索。',
        'songs.mnemonics.title': '🔤 学习鸣声模式和助记符',
        'songs.mnemonics.desc': '助记符是帮助观鸟者记住和识别鸟类鸣声的记忆辅助工具。',
        'songs.listening.title': '👂 发展您的听力技能',
        'songs.listening.desc': '有效的鸟类鸣声识别需要发展敏锐的听力技能。',
        // Ethics page
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'ethics.foundation.title': '🌱 道德观鸟的基础',
        'ethics.foundation.desc': '道德观鸟建立在鸟类和其栖息地的福利必须始终优先于我们观察或拍摄它们的愿望这一原则之上。',
        'ethics.guidelines.title': '✅ 道德观鸟指南',
        'ethics.guidelines.desc': '遵循既定指南有助于确保您的观鸟活动对环境的负面影响最小。',
        'ethics.breeding.title': '🥚 繁殖季节的特殊考虑',
        'ethics.breeding.desc': '繁殖季节需要观鸟者格外谨慎和敏感。干扰筑巢鸟类可能对繁殖成功产生严重后果。',
        // Journal page
        'journal.hero.title': '📔 保持观鸟日志',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'journal.why.title': '📝 为什么要保持观鸟日志？',
        'journal.why.desc': '观鸟日志将随意观察转化为有价值的个人体验、模式和发现数据库。',
        'journal.information.title': '📋 记录的基本信息',
        'journal.information.desc': '有效的观鸟日志捕获基本识别信息和提供背景的详细观察。',
        'journal.digital.title': '📱 数字 vs 模拟日志',
        'journal.digital.desc': '数字和传统纸质日志都有优势。最佳选择取决于您的个人偏好。',
        // Beginners page
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始令人惊叹的观鸟之旅的完整指南',
        'beginners.welcome.title': '🚀 欢迎来到观鸟世界！',
        'beginners.welcome.desc': '观鸟是世界上最有回报和最容易接触的爱好之一。',
        'beginners.getting.title': '🎒 入门：您的第一步',
        'beginners.getting.desc': '开始您的观鸟之旅不需要昂贵的设备或广泛的知识。',
        'beginners.common.title': '🏠 首先学习的常见鸟类',
        'beginners.common.desc': '从常见、易于识别的物种开始建立信心，为学习更具挑战性的鸟类提供基础。'
        // Equipment page
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'equipment.binoculars.title': '🔍 双筒望远镜 - 您的主要工具',
        'equipment.binoculars.desc': '双筒望远镜是任何观鸟者最重要的装备。它们能让远处的鸟类清晰可见，让您观察到肉眼无法看到的细节。',
        'equipment.guides.title': '📚 野外指南和参考资料',
        'equipment.guides.desc': '全面的野外指南是您识别遇到的鸟类的伴侣。现代野外指南包括详细的插图、分布图和行为描述。',
        'equipment.camera.title': '📷 鸟类摄影相机设备',
        'equipment.camera.desc': '虽然不是观鸟必需品，但相机可以让您捕捉和分享您的发现。鸟类摄影需要特殊考虑。',
        'equipment.additional.title': '🎒 其他必需装备',
        'equipment.additional.desc': '除了基础装备，还有几个额外物品可以显著改善您的观鸟体验和野外舒适度。',
        // Identification page
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '通过系统观察掌握识别鸟类的艺术',
        'identification.giss.title': '🎯 GISS 方法',
        'identification.giss.desc': 'GISS代表"整体大小和形状印象" - 这是经验丰富的观鸟者用来快速缩小鸟类识别范围的基本技术。',
        'identification.fieldmarks.title': '🏷️ 关键野外特征',
        'identification.fieldmarks.desc': '野外特征是区分一个物种与另一个物种的特定物理特征。学会快速发现和评估这些特征对准确识别至关重要。',
        'identification.behavior.title': '🦅 行为识别',
        'identification.behavior.desc': '鸟类行为通常提供最可靠的识别线索。鸟类如何移动、觅食和与环境互动可能比外观更具特色。',
        // Locations page
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝石',
        'locations.parks.title': '🏞️ 国家公园和保护区',
        'locations.parks.desc': '国家公园和野生动物保护区提供世界上一些最好的观鸟机会。这些保护区域维护着多样的栖息地。',
        'locations.wetlands.title': '💧 湿地和海岸地区',
        'locations.wetlands.desc': '湿地是地球上最富有生产力的鸟类栖息地之一。这些地区支持令人难以置信的多样性。',
        'locations.tropical.title': '🌴 热带热点',
        'locations.tropical.desc': '热带地区拥有地球上最大的鸟类多样性。这些地区提供观看其他地方找不到的奇异物种的机会。',
        // Seasonal page
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随年份变化并规划您的观察',
        'seasonal.spring.title': '🌸 春季：更新的季节',
        'seasonal.spring.desc': '春季可以说是观鸟最令人兴奋的时候。随着气温回暖和日照时间增加，鸟类变得非常活跃。',
        'seasonal.summer.title': '☀️ 夏季：家庭生活和丰富',
        'seasonal.summer.desc': '夏季观鸟专注于繁殖行为、家庭群体和常驻物种的丰富性。',
        'seasonal.fall.title': '🍂 秋季：南迁的伟大旅程',
        'seasonal.fall.desc': '秋季迁徙比春季更持久，为观察迁徙鸟类提供了更长的机会。',
        'seasonal.winter.title': '❄️ 冬季：顽强的幸存者和访客',
        'seasonal.winter.desc': '冬季观鸟揭示了勇敢面对寒冷温度和有限食物来源的顽强物种。',
        // Photography page
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '用基本技巧和设备拍摄令人惊叹的鸟类照片',
        'photography.equipment.title': '📷 相机设备要点',
        'photography.equipment.desc': '鸟类摄影需要专门的设备来捕捉远距离、快速移动的主体。',
        'photography.lens.title': '🔍 镜头选择和焦距',
        'photography.lens.desc': '镜头可以说是鸟类摄影最重要的组件。更长的焦距让您保持距离的同时用主体填满画面。',
        'photography.settings.title': '⚙️ 鸟类摄影相机设置',
        'photography.settings.desc': '正确的相机设置对于清晰、曝光良好的鸟类照片至关重要。',
        // Behavior page
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为并理解它们迷人的世界',
        'behavior.territorial.title': '🏠 领域和社会行为',
        'behavior.territorial.desc': '理解领域和社会行为提供了对鸟类心理的洞察，有助于预测它们的行动。',
        'behavior.feeding.title': '🍽️ 觅食行为和策略',
        'behavior.feeding.desc': '觅食行为揭示了鸟类的生态位，并提供了极好的观察机会。',
        'behavior.courtship.title': '💕 求偶和交配行为',
        'behavior.courtship.desc': '求偶行为是最壮观和复杂的鸟类行为之一。',
        // Song identification page
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'songs.understanding.title': '🎼 理解鸟类发声',
        'songs.understanding.desc': '鸟类的鸣声和叫声服务于不同目的，提供关键的识别线索。',
        'songs.mnemonics.title': '🔤 学习鸣声模式和助记符',
        'songs.mnemonics.desc': '助记符是帮助观鸟者记住和识别鸟类鸣声的记忆辅助工具。',
        'songs.listening.title': '👂 发展您的听力技能',
        'songs.listening.desc': '有效的鸟类鸣声识别需要发展敏锐的听力技能。',
        // Ethics page
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'ethics.foundation.title': '🌱 道德观鸟的基础',
        'ethics.foundation.desc': '道德观鸟建立在鸟类和其栖息地的福利必须始终优先于我们观察或拍摄它们的愿望这一原则之上。',
        'ethics.guidelines.title': '✅ 道德观鸟指南',
        'ethics.guidelines.desc': '遵循既定指南有助于确保您的观鸟活动对环境的负面影响最小。',
        'ethics.breeding.title': '🥚 繁殖季节的特殊考虑',
        'ethics.breeding.desc': '繁殖季节需要观鸟者格外谨慎和敏感。干扰筑巢鸟类可能对繁殖成功产生严重后果。',
        // Journal page
        'journal.hero.title': '📔 保持观鸟日志',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'journal.why.title': '📝 为什么要保持观鸟日志？',
        'journal.why.desc': '观鸟日志将随意观察转化为有价值的个人体验、模式和发现数据库。',
        'journal.information.title': '📋 记录的基本信息',
        'journal.information.desc': '有效的观鸟日志捕获基本识别信息和提供背景的详细观察。',
        'journal.digital.title': '📱 数字 vs 模拟日志',
        'journal.digital.desc': '数字和传统纸质日志都有优势。最佳选择取决于您的个人偏好。',
        // Beginners page
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始令人惊叹的观鸟之旅的完整指南',
        'beginners.welcome.title': '🚀 欢迎来到观鸟世界！',
        'beginners.welcome.desc': '观鸟是世界上最有回报和最容易接触的爱好之一。',
        'beginners.getting.title': '🎒 入门：您的第一步',
        'beginners.getting.desc': '开始您的观鸟之旅不需要昂贵的设备或广泛的知识。',
        'beginners.common.title': '🏠 首先学习的常见鸟类',
        'beginners.common.desc': '从常见、易于识别的物种开始建立信心，为学习更具挑战性的鸟类提供基础。'
        'birdwatching.hero.title': '🔍 观鸟指南',
        'birdwatching.hero.subtitle': '掌握鸟类观察和识别的艺术技巧',
        'birdwatching.category': '观鸟指南',
        'birdwatching.readmore': '阅读更多',
        'birdwatching.articles.equipment.title': '观鸟必备装备',
        'birdwatching.articles.equipment.desc': '发现成功观鸟冒险所需的必备工具和装备，从双筒望远镜到野外指南。',
        'birdwatching.articles.identification.title': '鸟类识别技巧',
        'birdwatching.articles.identification.desc': '学习通过大小、形状、颜色、行为和栖息地识别鸟类的经验证方法。',
        'birdwatching.articles.locations.title': '最佳观鸟地点',
        'birdwatching.articles.locations.desc': '探索世界各地顶级观鸟目的地及其特色之处。',
        'birdwatching.articles.seasonal.title': '季节性观鸟指南',
        'birdwatching.articles.seasonal.desc': '了解鸟类活动如何随季节变化，并相应规划您的观察活动。',
        'birdwatching.articles.photography.title': '观鸟者摄影技巧',
        'birdwatching.articles.photography.desc': '通过这些基本摄影技巧和设备推荐，拍摄令人惊叹的鸟类照片。',
        'birdwatching.articles.behavior.title': '鸟类行为观察',
        'birdwatching.articles.behavior.desc': '学会解读鸟类行为，理解不同动作和姿态的含义。',
        'birdwatching.articles.songs.title': '鸟类鸣声识别',
        'birdwatching.articles.songs.desc': '掌握通过鸟类鸣声和叫声识别鸟类的艺术，这是观鸟者的重要技能。',
        'birdwatching.articles.ethics.title': '观鸟伦理与保护',
        'birdwatching.articles.ethics.desc': '了解道德观鸟实践的重要性以及如何最小化对鸟类的影响。',
        'birdwatching.articles.journal.title': '观鸟日志记录',
        'birdwatching.articles.journal.desc': '学习如何详细记录您的观鸟体验和观察结果。',
        'birdwatching.articles.beginners.title': '观鸟入门指南',
        'birdwatching.articles.beginners.desc': '为观鸟新手提供的综合指南，涵盖基础知识和入门技巧。',
        'footer.description': '基于AI技术的智能鸟类识别',
        'footer.quicklinks': '快速链接',
        'footer.download': '下载应用',
        'footer.email': '邮箱：lingjuetech@gmail.com',
        
        // Detailed page translations
        'equipment.hero.title': '🔭 观鸟必备装备',
        'equipment.hero.subtitle': '发现成功观鸟冒险所需的必备工具和装备',
        'equipment.binoculars.title': '🔍 双筒望远镜 - 您的主要工具',
        'equipment.binoculars.desc': '双筒望远镜是任何观鸟者最重要的装备。它们能将远处的鸟类清晰地呈现在眼前，让您观察到肉眼无法看到的细节。',
        'equipment.guides.title': '📚 野外指南和参考资料',
        'equipment.guides.desc': '全面的野外指南是您识别遇到的鸟类的伙伴。现代野外指南包含详细的插图、分布图和行为描述。',
        'equipment.camera.title': '📷 鸟类摄影设备',
        'equipment.camera.desc': '虽然不是观鸟的必需品，但相机可以让您捕捉和分享您的发现。鸟类摄影需要特殊考虑。',
        'equipment.gear.title': '🎒 其他必需装备',
        'equipment.gear.desc': '除了基础装备外，还有几件物品可以显著改善您的观鸟体验和野外舒适度。',
        'equipment.specialized.title': '🔧 专业装备',
        'equipment.specialized.desc': '随着观鸟技能的发展，您可能想要投资专业装备来增强特定方面的观鸟体验。',
        'equipment.budget.title': '💡 预算友好的替代方案',
        'equipment.budget.desc': '观鸟不必昂贵。许多优秀的观鸟体验可以用基础装备获得，大多数装备都有预算友好的替代方案。',
        
        'identification.hero.title': '🔍 鸟类识别技巧',
        'identification.hero.subtitle': '通过系统观察掌握识别鸟类的艺术',
        'identification.giss.title': '🎯 GISS 方法',
        'identification.giss.desc': 'GISS代表"整体大小和形状印象" - 这是经验丰富的观鸟者用来快速缩小鸟类识别范围的基本技术。',
        'identification.fieldmarks.title': '🏷️ 关键野外特征',
        'identification.fieldmarks.desc': '野外特征是区分不同物种的特定物理特征。学会快速发现和评估这些特征对准确识别至关重要。',
        'identification.behavior.title': '🦅 行为识别',
        'identification.behavior.desc': '鸟类行为通常提供最可靠的识别线索。鸟类如何移动、觅食和与环境互动可能比外观更具特色。',
        'identification.feeding.title': '🍽️ 觅食行为分析',
        'identification.feeding.desc': '鸟类如何以及在哪里觅食提供了重要的识别线索。不同物种已经进化出专门的觅食技术。',
        'identification.habitat.title': '🌲 基于栖息地的识别',
        'identification.habitat.desc': '了解栖息地偏好可以大大缩小识别可能性。大多数鸟类物种都有特定的栖息地要求。',
        'identification.seasonal.title': '📅 季节和时间线索',
        'identification.seasonal.desc': '时间可以是强大的识别工具。许多物种只在特定季节出现，日常活动模式在物种间有所不同。',
        'identification.advanced.title': '🔧 高级识别技术',
        'identification.advanced.desc': '随着技能的发展，您可以使用更复杂的识别方法，结合多种观察技术来应对具有挑战性的识别。',
        
        'locations.hero.title': '🌍 最佳观鸟地点',
        'locations.hero.subtitle': '发现世界顶级观鸟目的地和隐藏宝石',
        'locations.parks.title': '🏞️ 国家公园和保护区',
        'locations.parks.desc': '国家公园和野生动物保护区提供世界上一些最好的观鸟机会。这些保护区维护着多样的栖息地。',
        'locations.wetlands.title': '💧 湿地和海岸地区',
        'locations.wetlands.desc': '湿地是地球上最富有生产力的鸟类栖息地之一。这些地区支持令人难以置信的多样性。',
        'locations.tropical.title': '🌴 热带热点',
        'locations.tropical.desc': '热带地区拥有地球上最大的鸟类多样性。这些地区提供观察异国物种的机会。',
        'locations.mountain.title': '⛰️ 山地和高山地区',
        'locations.mountain.desc': '山地环境提供独特的观鸟机会，有专门的高海拔物种。',
        'locations.urban.title': '🏙️ 城市观鸟宝地',
        'locations.urban.desc': '城市提供令人惊讶的观鸟机会，城市公园和绿地支持多样的鸟类群落。',
        'locations.migration.title': '🛤️ 迁徙走廊',
        'locations.migration.desc': '迁徙路线提供一些最壮观的观鸟体验，在迁徙高峰期有数千只鸟类通过。',
        'locations.local.title': '🏡 寻找本地热点',
        'locations.local.desc': '最好的观鸟地点可能比您想象的更近。当地公园、自然中心，甚至您的后院都能提供优秀的观鸟机会。',
        
        'seasonal.hero.title': '📅 季节性观鸟指南',
        'seasonal.hero.subtitle': '了解鸟类活动如何随年份变化并规划您的观察',
        'seasonal.spring.title': '🌸 春季：更新的季节',
        'seasonal.spring.desc': '春季可以说是观鸟最令人兴奋的时候。随着气温回暖和日照时间增加，鸟类变得非常活跃。',
        'seasonal.summer.title': '☀️ 夏季：家庭生活和丰富',
        'seasonal.summer.desc': '夏季观鸟专注于繁殖行为、家庭群体和留鸟物种的丰富性。',
        'seasonal.fall.title': '🍂 秋季：南迁的伟大旅程',
        'seasonal.fall.desc': '秋季迁徙比春季更持久，为观察迁徙鸟类提供了更长的机会。',
        'seasonal.winter.title': '❄️ 冬季：顽强的幸存者和访客',
        'seasonal.winter.desc': '冬季观鸟揭示了勇敢面对寒冷温度和有限食物来源的顽强物种。',
        'seasonal.planning.title': '📊 规划您的观鸟年',
        'seasonal.planning.desc': '成功的观鸟需要了解季节模式并相应规划。每个季节都提供不应错过的独特机会。',
        
        'photography.hero.title': '📸 观鸟者摄影技巧',
        'photography.hero.subtitle': '用基本技巧和装备捕捉令人惊叹的鸟类照片',
        'photography.equipment.title': '📷 相机设备要点',
        'photography.equipment.desc': '鸟类摄影需要专门的设备来捕捉远距离、快速移动的主体。',
        'photography.lens.title': '🔍 镜头选择和焦距',
        'photography.lens.desc': '镜头可以说是鸟类摄影最重要的组件。更长的焦距让您保持距离的同时用主体填满画面。',
        'photography.settings.title': '⚙️ 鸟类摄影的相机设置',
        'photography.settings.desc': '正确的相机设置对于清晰、曝光良好的鸟类照片至关重要。',
        'photography.composition.title': '🎨 构图和艺术技巧',
        'photography.composition.desc': '技术卓越只是开始。创造引人注目的鸟类照片需要理解构图、光线和艺术视觉。',
        'photography.behavior.title': '🎭 捕捉行为和动作',
        'photography.behavior.desc': '最引人注目的鸟类照片捕捉自然行为和互动。',
        'photography.ethics.title': '🤝 道德鸟类摄影',
        'photography.ethics.desc': '负责任的鸟类摄影将鸟类的福利置于获得完美照片之上。',
        'photography.processing.title': '🖥️ 鸟类照片后期处理',
        'photography.processing.desc': '数字处理可以增强您的鸟类照片，同时保持自然外观。',
        
        'behavior.hero.title': '🎭 鸟类行为观察',
        'behavior.hero.subtitle': '学会解读鸟类行为并理解它们迷人的世界',
        'behavior.territorial.title': '🏠 领域和社会行为',
        'behavior.territorial.desc': '理解领域和社会行为提供了对鸟类心理的洞察，有助于预测它们的行动。',
        'behavior.feeding.title': '🍽️ 觅食行为和策略',
        'behavior.feeding.desc': '觅食行为揭示了鸟类的生态位，并提供了优秀的观察机会。',
        'behavior.courtship.title': '💕 求偶和交配行为',
        'behavior.courtship.desc': '求偶行为是最壮观和复杂的鸟类行为之一。',
        'behavior.parental.title': '👨‍👩‍👧‍👦 亲子关怀和家庭动态',
        'behavior.parental.desc': '亲子行为提供了对鸟类家庭生活的迷人洞察。',
        'behavior.flocking.title': '🐦‍⬛ 群集和群体动态',
        'behavior.flocking.desc': '许多鸟类为了觅食、栖息或迁徙而形成群体。',
        'behavior.communication.title': '📢 沟通和发声',
        'behavior.communication.desc': '鸟类沟通远远超出简单的歌声。理解鸟类发声和肢体语言的细微差别。',
        
        'songs.hero.title': '🎵 鸟类鸣声识别',
        'songs.hero.subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
        'songs.understanding.title': '🎼 理解鸟类发声',
        'songs.understanding.desc': '鸟类的歌声和叫声服务于不同目的，提供重要的识别线索。',
        'songs.mnemonics.title': '🔤 学习鸣声模式和助记符',
        'songs.mnemonics.desc': '助记符是帮助观鸟者记住和识别鸟类歌声的记忆辅助工具。',
        'songs.listening.title': '👂 发展您的听力技能',
        'songs.listening.desc': '有效的鸟类鸣声识别需要发展敏锐的听力技能。',
        'songs.variations.title': '🌍 地区变异和方言',
        'songs.variations.desc': '鸟类歌声可能因地理位置而异，具有与野外指南标准描述不同的地区"方言"。',
        'songs.technology.title': '📱 鸣声学习的技术和工具',
        'songs.technology.desc': '现代技术为学习和识别鸟类歌声提供了强大的工具。',
        'songs.seasonal.title': '📅 发声的季节变化',
        'songs.seasonal.desc': '鸟类发声在一年中会发生变化，以响应繁殖周期、迁徙和社会动态。',
        
        'ethics.hero.title': '🤝 观鸟伦理与保护',
        'ethics.hero.subtitle': '保护我们喜爱观察的鸟类的负责任观鸟实践',
        'ethics.foundation.title': '🌱 道德观鸟的基础',
        'ethics.foundation.desc': '道德观鸟建立在鸟类和其栖息地的福利必须始终优先于我们观察或拍摄它们的愿望这一原则之上。',
        'ethics.guidelines.title': '✅ 道德观鸟指南',
        'ethics.guidelines.desc': '遵循既定指南有助于确保您的观鸟活动对环境的负面影响最小。',
        'ethics.breeding.title': '🥚 繁殖季节的特殊考虑',
        'ethics.breeding.desc': '繁殖季节需要观鸟者格外谨慎和敏感。干扰筑巢鸟类可能对繁殖成功产生严重后果。',
        'ethics.threats.title': '🌍 保护威胁和挑战',
        'ethics.threats.desc': '了解鸟类种群面临的主要威胁有助于观鸟者就保护支持做出明智决定。',
        'ethics.contributing.title': '📊 通过观鸟为保护做贡献',
        'ethics.contributing.desc': '观鸟者可以通过公民科学、栖息地保护和倡导努力为鸟类保护做出重大贡献。',
        'ethics.habitat.title': '🌿 支持栖息地保护',
        'ethics.habitat.desc': '栖息地保护是保护鸟类种群最有效的方式。',
        'ethics.future.title': '🔮 道德观鸟的未来',
        'ethics.future.desc': '随着观鸟继续受到欢迎，维护道德标准变得越来越重要。',
        
        'journal.hero.title': '📔 记录观鸟日志',
        'journal.hero.subtitle': '记录您的观鸟冒险并建立个人发现记录',
        'journal.why.title': '📝 为什么要记录观鸟日志？',
        'journal.why.desc': '观鸟日志将随意观察转化为有价值的个人体验、模式和发现数据库。',
        'journal.information.title': '📋 记录的基本信息',
        'journal.information.desc': '有效的观鸟日志既捕捉基本识别信息，也记录提供背景的详细观察。',
        'journal.digital.title': '📱 数字 vs 纸质日志',
        'journal.digital.desc': '数字和传统纸质日志都有优势。最佳选择取决于您的个人偏好。',
        'journal.sketches.title': '🎨 添加素描和视觉元素',
        'journal.sketches.desc': '视觉元素增强日志条目，有助于捕捉仅凭文字无法传达的细节。',
        'journal.analyzing.title': '📊 分析您的记录',
        'journal.analyzing.desc': '定期审查和分析您的日志条目揭示模式，跟踪进展。',
        'journal.sharing.title': '🤝 分享和贡献您的记录',
        'journal.sharing.desc': '您的日志记录具有超越个人享受的价值。',
        
        'beginners.hero.title': '🌟 观鸟入门指南',
        'beginners.hero.subtitle': '开始令人惊叹的观鸟之旅的完整指南',
        'beginners.welcome.title': '🚀 欢迎来到观鸟世界！',
        'beginners.welcome.desc': '观鸟是世界上最有回报和最容易接触的爱好之一。',
        'beginners.getting.title': '🎒 入门：您的第一步',
        'beginners.getting.desc': '开始您的观鸟之旅不需要昂贵的设备或广泛的知识。',
        'beginners.common.title': '🏠 首先学习的常见鸟类',
        'beginners.common.desc': '从常见、易于识别的物种开始建立信心。',
        'beginners.identification.title': '🔍 基本识别技术',
        'beginners.identification.desc': '学习系统的鸟类识别方法使过程不那么令人困惑。',
        'beginners.where.title': '📍 去哪里观鸟',
        'beginners.where.desc': '优秀的观鸟地点无处不在，从城市公园到荒野地区。',
        'beginners.mistakes.title': '⚠️ 避免常见的初学者错误',
        'beginners.mistakes.desc': '从常见错误中学习有助于新观鸟者更快进步。',
        'beginners.building.title': '📈 随时间建立您的技能',
        'beginners.building.desc': '观鸟是终身学习之旅。',
        'beginners.community.title': '🤝 与观鸟社区联系',
        'beginners.community.desc': '观鸟社区以热情好客、乐于助人和热衷于分享知识而闻名。'
    }
};

// 当前语言
let currentLanguage = 'en';

// DOM元素
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-menu a');
const contactForm = document.querySelector('.contact-form form');

// 移动端导航菜单切换
navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    navToggle.classList.toggle('active');
});

// 点击导航链接时关闭移动端菜单
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
    });
});

// 平滑滚动到锚点
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            const offsetTop = targetSection.offsetTop - 80; // 考虑固定导航栏高度
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// 滚动时导航栏样式变化
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.15)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    }
});

// 表单提交处理
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // 获取表单数据
        const name = document.getElementById('userName').value;
        const email = document.getElementById('userEmail').value;
        const message = document.getElementById('userMessage').value;
        const submitButton = document.getElementById('submitBtn');
        const formStatus = document.getElementById('formStatus');
        
        // 简单的表单验证
        if (!name || !email || !message) {
            const errorMsg = currentLanguage === 'zh' ? '请填写所有必填字段' : 'Please fill in all required fields';
            showFormStatus(errorMsg, 'error');
            return;
        }
        
        // 显示发送中状态
        const sendingMsg = currentLanguage === 'zh' ? '发送中...' : 'Sending...';
        submitButton.textContent = sendingMsg;
        submitButton.disabled = true;
        
        // 使用mailto链接发送邮件
        sendEmailWithMailto(name, email, message, submitButton);
    });
}

// 使用mailto链接发送邮件
function sendEmailWithMailto(name, email, message, submitButton) {
    const isZh = currentLanguage === 'zh';
    const subject = isZh ? 'BirdAiSnap官网联系表单 - ' + name : 'BirdAiSnap Website Contact Form - ' + name;
    const emailBody = isZh ? 
        `姓名: ${name}\n` +
        `邮箱: ${email}\n\n` +
        `消息内容:\n${message}\n\n` +
        `---\n发送时间: ${new Date().toLocaleString()}\n来源: BirdAiSnap官网` :
        `Name: ${name}\n` +
        `Email: ${email}\n\n` +
        `Message:\n${message}\n\n` +
        `---\nSent at: ${new Date().toLocaleString()}\nFrom: BirdAiSnap Website`;
    
    const encodedSubject = encodeURIComponent(subject);
    const encodedBody = encodeURIComponent(emailBody);
    const mailtoLink = `mailto:lingjuetech@gmail.com?subject=${encodedSubject}&body=${encodedBody}`;
    
    // 显示邮件信息
    showEmailInfo(subject, emailBody, mailtoLink);
    
    // 模拟发送延迟，提供更好的用户体验
    setTimeout(() => {
        try {
            // 尝试打开邮件客户端
            window.location.href = mailtoLink;
            const successMsg = isZh ? 
                '邮件客户端已尝试打开。如果没有打开，请使用下面的邮件信息手动发送。' :
                'Email client has been attempted to open. If not opened, please use the email information below to send manually.';
            showFormStatus(successMsg, 'info');
            
        } catch (error) {
            console.error('Mailto link failed:', error);
            const errorMsg = isZh ? 
                '无法自动打开邮件客户端，请使用下面的邮件信息手动发送。' :
                'Unable to open email client automatically, please use the email information below to send manually.';
            showFormStatus(errorMsg, 'error');
        }
        
        const resetText = isZh ? '发送消息' : 'Send Message';
        submitButton.textContent = resetText;
        submitButton.disabled = false;
    }, 1000);
}

// 显示邮件信息
function showEmailInfo(subject, body, mailtoLink) {
    const emailInfo = document.getElementById('emailInfo');
    const emailSubject = document.getElementById('emailSubject');
    const emailContent = document.getElementById('emailContent');
    
    emailSubject.textContent = subject;
    emailContent.textContent = body;
    emailInfo.style.display = 'block';
    
    // 存储邮件信息供复制使用
    window.currentEmailInfo = {
        subject: subject,
        body: body,
        mailto: mailtoLink
    };
}

// 复制邮件信息到剪贴板 - 全局函数
window.copyEmailInfo = function() {
    if (window.currentEmailInfo) {
        const isZh = currentLanguage === 'zh';
        const fullEmailText = isZh ?
            `收件人: lingjuetech@gmail.com\n` +
            `主题: ${window.currentEmailInfo.subject}\n\n` +
            `内容:\n${window.currentEmailInfo.body}` :
            `Recipient: lingjuetech@gmail.com\n` +
            `Subject: ${window.currentEmailInfo.subject}\n\n` +
            `Content:\n${window.currentEmailInfo.body}`;
        
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(fullEmailText).then(() => {
                const successMsg = isZh ? '邮件信息已复制到剪贴板！' : 'Email information copied to clipboard!';
                showFormStatus(successMsg, 'success');
            }).catch(err => {
                console.error('复制失败:', err);
                fallbackCopyTextToClipboard(fullEmailText);
            });
        } else {
            fallbackCopyTextToClipboard(fullEmailText);
        }
    }
}

// 备用复制方法
function fallbackCopyTextToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        const successful = document.execCommand('copy');
        const isZh = currentLanguage === 'zh';
        if (successful) {
            const successMsg = isZh ? '邮件信息已复制到剪贴板！' : 'Email information copied to clipboard!';
            showFormStatus(successMsg, 'success');
        } else {
            const errorMsg = isZh ? '复制失败，请手动复制邮件信息' : 'Copy failed, please manually copy email information';
            showFormStatus(errorMsg, 'error');
        }
    } catch (err) {
        console.error('复制失败:', err);
        const errorMsg = currentLanguage === 'zh' ? '复制失败，请手动复制邮件信息' : 'Copy failed, please manually copy email information';
        showFormStatus(errorMsg, 'error');
    }
    
    document.body.removeChild(textArea);
}

// 重新打开邮件客户端 - 全局函数
window.openEmailClient = function() {
    if (window.currentEmailInfo) {
        try {
            window.location.href = window.currentEmailInfo.mailto;
            const infoMsg = currentLanguage === 'zh' ? '正在尝试打开邮件客户端...' : 'Trying to open email client...';
            showFormStatus(infoMsg, 'info');
        } catch (error) {
            console.error('打开邮件客户端失败:', error);
            const errorMsg = currentLanguage === 'zh' ? 
                '无法打开邮件客户端，请复制邮件信息手动发送' : 
                'Unable to open email client, please copy email information and send manually';
            showFormStatus(errorMsg, 'error');
        }
    }
}

// 语言切换功能 - 全局函数
window.toggleLanguage = function() {
    currentLanguage = currentLanguage === 'en' ? 'zh' : 'en';
    updateLanguage();
    updateLanguageButton();
    
    // 保存到localStorage
    localStorage.setItem('language', currentLanguage);
}

// 更新页面语言
function updateLanguage() {
    const lang = languages[currentLanguage];
    
    // 更新所有带有data-i18n属性的元素
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (lang[key]) {
            element.textContent = lang[key];
        }
    });
    
    // 更新placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        if (lang[key]) {
            element.placeholder = lang[key];
        }
    });
    
    // 更新html lang属性
    document.documentElement.lang = currentLanguage === 'zh' ? 'zh-CN' : 'en';
    
    // 更新页面标题
    document.title = currentLanguage === 'zh' ? 'BirdAiSnap - 智能识别APP' : 'BirdAiSnap - Smart Recognition App';
}

// 更新语言切换按钮
function updateLanguageButton() {
    const langText = document.getElementById('currentLang');
    if (langText) {
        langText.textContent = currentLanguage === 'en' ? 'EN' : '中文';
    }
}

// 页面加载时初始化所有功能
document.addEventListener('DOMContentLoaded', function() {
    // 初始化语言
    const savedLanguage = localStorage.getItem('language') || 'en';
    currentLanguage = savedLanguage;
    
    // 初始化页面动画
    initPageAnimation();
    
    // 等待DOM完全加载后再更新语言
    setTimeout(() => {
        updateLanguage();
        updateLanguageButton();
    }, 100);
    
    // 初始化其他功能
    initializeFeatures();
});



// 显示表单状态信息
function showFormStatus(message, type) {
    const formStatus = document.getElementById('formStatus');
    formStatus.textContent = message;
    formStatus.className = `form-status ${type}`;
    formStatus.style.display = 'block';
    
    // 3秒后自动隐藏
    setTimeout(() => {
        formStatus.style.display = 'none';
    }, 3000);
}

// 初始化其他功能
function initializeFeatures() {
    // 功能卡片悬停效果
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1)';
        });
    });

    // 按钮点击效果
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            const buttonText = button.textContent.trim();
            if (buttonText === '了解更多' || buttonText === 'Learn More') {
                // 滚动到功能区域
                const featuresSection = document.querySelector('#features');
                if (featuresSection) {
                    featuresSection.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
    
    // 初始化滚动动画
    initScrollAnimations();
    
    // 初始化手机样机动画
    initPhoneAnimations();
    
    // 初始化统计数字动画
    initStatsAnimation();
}

// 页面加载动画
function initPageAnimation() {
    // 添加页面加载完成的淡入效果
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease-in-out';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
}

// 滚动动画效果
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // 观察需要动画的元素
    const animatedElements = document.querySelectorAll('.feature-card, .stat, .about-text, .contact-info');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// 手机样机中的动态效果
function initPhoneAnimations() {
    const phoneScreen = document.querySelector('.phone-screen');
    if (phoneScreen) {
        // 模拟相机识别动画
        setInterval(() => {
            const birdPreview = document.querySelector('.bird-preview');
            if (birdPreview) {
                birdPreview.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    birdPreview.style.transform = 'scale(1)';
                }, 500);
            }
        }, 3000);
        
        // 模拟模式切换动画
        const modes = document.querySelectorAll('.mode');
        setInterval(() => {
            modes.forEach(mode => mode.classList.remove('active'));
            const randomMode = modes[Math.floor(Math.random() * modes.length)];
            randomMode.classList.add('active');
        }, 4000);
    }
}

// 统计数字动画效果
function initStatsAnimation() {
    const animateNumber = (element, start, end, duration) => {
        const startTime = performance.now();
        
        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            const currentNumber = Math.floor(start + (end - start) * progress);
            if (end === 95) {
                element.textContent = currentNumber + '%';
            } else if (end === 100000) {
                element.textContent = Math.floor(currentNumber / 1000) + 'K+';
            } else {
                element.textContent = currentNumber.toLocaleString() + '+';
            }
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    };

    // 当统计区域进入视口时开始动画
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const stats = entry.target.querySelectorAll('.stat h3');
                stats.forEach((stat, index) => {
                    const values = [100000, 30000, 95]; // 对应的数值
                    setTimeout(() => {
                        animateNumber(stat, 0, values[index], 2000);
                    }, index * 200);
                });
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('.stats');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
}

// 导航菜单移动端样式
const style = document.createElement('style');
style.textContent = `
    @media (max-width: 768px) {
        .nav-menu {
            position: fixed;
            top: 80px;
            right: -100%;
            width: 80%;
            height: calc(100vh - 80px);
            background: white;
            flex-direction: column;
            justify-content: start;
            align-items: center;
            padding-top: 2rem;
            box-shadow: -2px 0 10px rgba(0, 0, 0, 0.1);
            transition: right 0.3s ease;
            z-index: 999;
        }
        
        .nav-menu.active {
            right: 0;
        }
        
        .nav-menu li {
            margin: 1rem 0;
        }
        
        .nav-menu a {
            font-size: 1.2rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: background 0.3s ease;
        }
        
        .nav-menu a:hover {
            background: #f3f4f6;
        }
        
        .nav-toggle.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }
        
        .nav-toggle.active span:nth-child(2) {
            opacity: 0;
        }
        
        .nav-toggle.active span:nth-child(3) {
            transform: rotate(-45deg) translate(7px, -6px);
        }
    }
`;
document.head.appendChild(style);

// 知识中心功能
function openKnowledgeCenter() {
    console.log('openKnowledgeCenter 被调用');
    window.location.href = 'knowledge.html';
}

// 全局函数
window.openKnowledgeCenter = openKnowledgeCenter;

// DOM加载完成后添加事件监听器
document.addEventListener('DOMContentLoaded', function() {
    const knowledgeCard = document.getElementById('knowledgeCard');
    if (knowledgeCard) {
        console.log('知识卡片找到，添加点击事件');
        
        // 添加多种点击事件处理
        knowledgeCard.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('知识卡片被点击');
            openKnowledgeCenter();
        });
        
        // 添加键盘事件支持
        knowledgeCard.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                console.log('知识卡片键盘激活');
                openKnowledgeCenter();
            }
        });
        
        // 设置可访问性属性
        knowledgeCard.setAttribute('tabindex', '0');
        knowledgeCard.setAttribute('role', 'button');
        knowledgeCard.setAttribute('aria-label', 'More Bird Knowledge - Click to explore');
        
        // 添加hover效果确认
        knowledgeCard.addEventListener('mouseenter', function() {
            console.log('鼠标进入知识卡片');
        });
        
    } else {
        console.error('未找到知识卡片元素');
    }
});