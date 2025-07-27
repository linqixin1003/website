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
            'footer.copyright': '© 2024 BirdAiSnap. All rights reserved'
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
            'footer.copyright': '© 2024 BirdAiSnap. 保留所有权利'
        }
    },
    'ko': { 
        name: '한국어', 
        flag: '🇰🇷', 
        code: 'KO',
        translations: {
            'nav.home': '홈',
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
            'footer.copyright': '© 2024 BirdAiSnap. 모든 권리 보유'
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
            'footer.copyright': '© 2024 BirdAiSnap. 全著作権所有'
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
            'footer.copyright': '© 2024 BirdAiSnap. Alle Rechte vorbehalten'
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
            'footer.copyright': '© 2024 BirdAiSnap. Tous droits réservés'
        }
    },
    'es': { 
        name: 'Español', 
        flag: '🇪🇸', 
        code: 'ES',
        translations: {
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
            'footer.copyright': '© 2024 BirdAiSnap. Todos los derechos reservados'
        }
    },
    'it': { 
        name: 'Italiano', 
        flag: '🇮🇹', 
        code: 'IT',
        translations: {
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
            'footer.copyright': '© 2024 BirdAiSnap. Tutti i diritti riservati'
        }
    },
    'pt': { 
        name: 'Português', 
        flag: '🇵🇹', 
        code: 'PT',
        translations: {
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
            'footer.copyright': '© 2024 BirdAiSnap. Todos os direitos reservados'
        }
    },
    'ru': { 
        name: 'Русский', 
        flag: '🇷🇺', 
        code: 'RU',
        translations: {
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
            'footer.copyright': '© 2024 BirdAiSnap. Все права защищены'
        }
    }
};

let currentLang = 'en';

// 创建语言下拉菜单
function createLanguageDropdown() {
    const languageSwitcher = document.querySelector('.language-switcher');
    if (!languageSwitcher) {
        console.log('Language switcher container not found');
        return;
    }

    const dropdown = document.createElement('div');
    dropdown.className = 'lang-dropdown';

    const button = document.createElement('button');
    button.className = 'lang-btn';
    button.innerHTML = `
        <span class="lang-icon">🌐</span>
        <span class="lang-text">Language</span>
        <span id="currentLang">${languages[currentLang].code}</span>
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
    const translations = languages[langCode].translations;
    if (!translations) return;

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
    if (!languages[langCode]) return;
    
    currentLang = langCode;
    
    // 更新下拉菜单显示
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = languages[langCode].code;
    }

    // 更新选中状态
    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.remove('active');
    });
    
    const activeOption = Array.from(document.querySelectorAll('.lang-option')).find(option => 
        option.innerHTML.includes(languages[langCode].code)
    );
    if (activeOption) {
        activeOption.classList.add('active');
    }

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
    setTimeout(() => {
        createLanguageDropdown();
    }, 100);
});