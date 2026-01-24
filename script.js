// 语言配置和翻译内容
const languages = {
    'en': { 
        name: 'English', 
        flag: '🇺🇸', 
        code: 'EN',
        translations: {
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Discover Nature with AI',
            'hero.description': 'Explore the natural world with our comprehensive suite of AI-powered recognition apps. Identify birds, rocks, mushrooms, and insects with advanced artificial intelligence technology.',
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
            'apps.stillalive.desc': 'Your personal safety guardian with daily check-ins and automatic emergency alerts for people living alone.',
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
            'footer.apps.stillalive': 'Still Alive?',
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
    'de': { 
        name: 'Deutsch', 
        flag: '🇩🇪', 
        code: 'DE',
        translations: {
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Entdecke die Natur mit KI',
            'hero.description': 'Erkunde die natürliche Welt mit unserer umfassenden Suite von KI-gestützten Erkennungsapps. Identifiziere Vögel, Steine, Pilze und Insekten mit fortschrittlicher künstlicher Intelligenz.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'es': { 
        name: 'Español', 
        flag: '🇪🇸', 
        code: 'ES',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'fr': { 
        name: 'Français', 
        flag: '🇫🇷', 
        code: 'FR',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'it': { 
        name: 'Italiano', 
        flag: '🇮🇹', 
        code: 'IT',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'ja': { 
        name: '日本語', 
        flag: '🇯🇵', 
        code: 'JP',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'ko': { 
        name: '한국어', 
        flag: '🇰🇷', 
        code: 'KR',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
    'pt': { 
        name: 'Português', 
        flag: '🇵🇹', 
        code: 'PT',
        translations: {
            // 使用英文内容作为基础
            'nav.home': 'Home',
            'nav.apps': 'Apps',
            'nav.features': 'Features',
            'nav.about': 'About',
            'nav.contact': 'Contact',
            'hero.title': 'Intelligent Recognition, Capture & Discover',
            'hero.description': 'BirdAiSnap is an AI-powered intelligent recognition application that enables rapid bird identification in your surroundings while unveiling the mysteries of the natural world.',
            'hero.download': 'Download Now',
            'hero.learn': 'Learn More',
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
            'nav.apps': '应用',
            'nav.features': '功能',
            'nav.about': '关于',
            'nav.contact': '联系',
            'hero.title': '用AI探索自然',
            'hero.description': '通过我们全面的AI识别应用套件探索自然世界。使用先进的人工智能技术识别鸟类、岩石、蘑菇和昆虫。',
            'hero.download': '立即下载',
            'hero.learn': '了解更多',
            'features.title': '核心功能',
            'features.scan.title': '拍摄与识别',
            'features.scan.desc': '只需拍摄照片或上传现有图像，即可精确识别鸟类物种',
            'features.sound.title': '声音识别',
            'features.sound.desc': '录制鸟类声音，通过先进的AI声学分析识别物种',
            'features.nearby.title': '本地鸟种',
            'features.nearby.desc': '发现您附近的鸟类物种，探索区域生态模式',
            'features.enhance.title': '智能增强',
            'features.enhance.desc': '利用先进的AI算法提升照片质量，以惊人的清晰度展现鸟类主体',
            'features.collection.title': '个人收藏',
            'features.collection.desc': '策划个性化鸟类收藏，详细记录每次观鸟探险',
            'features.info.title': '综合数据库',
            'features.info.desc': '随时随地访问丰富的鸟类学信息和科学知识库',
            'features.knowledge.title': '鸟类学见解',
            'features.knowledge.desc': '探索全面的观鸟指南、科学发现、鸟类护理、生态关系和文化意义',
            'apps.stillalive.desc': '您的个人安全守护者，为独居人群提供每日签到和自动紧急警报功能。',
            'about.title': '关于BirdAiSnap',
            'about.desc1': 'BirdAiSnap是专为鸟类爱好者和自然探索者设计的智能识别应用。我们致力于通过前沿AI技术帮助用户更深入地理解和欣赏自然界中的美丽鸟类。',
            'about.desc2': '无论您是专业鸟类学家还是好奇的自然爱好者，BirdAiSnap都能为您提供精确快速的鸟类识别服务。',
            'about.stats.downloads': '下载量',
            'about.stats.species': '鸟类物种',
            'about.stats.accuracy': '识别准确率',
            'contact.title': '联系我们',
            'contact.subtitle': '获取更多信息',
            'contact.desc': '如果您有任何问题或建议，请随时联系我们',
            'contact.email': '邮箱：',
            'contact.form.name': '您的姓名',
            'contact.form.email': '您的邮箱',
            'contact.form.message': '您的留言',
            'contact.form.submit': '发送消息',
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
            'footer.apps.stillalive': '活着么？',
            'footer.copyright': '© 2024 BirdAiSnap. 版权所有',
            // RockAiSnap 相关翻译
            'rock.nav.home': '首页',
            'rock.nav.features': '功能',
            'rock.nav.about': '关于',
            'rock.nav.contact': '联系',
            'rock.hero.title': '发现地球的隐藏宝藏',
            'rock.hero.description': 'RockAiSnap 使用先进的AI技术识别岩石、矿物和地质构造。通过精确识别和全面的地质信息探索迷人的地质学世界。',
            'rock.hero.download': '立即下载',
            'rock.hero.learn': '了解更多',
            'rock.hero.available': '现已上线',
            'rock.hero.notify': '获取通知',
            'rock.features.title': '计划功能',
            'rock.features.identification.title': '矿物识别',
            'rock.features.identification.desc': '使用先进的计算机视觉和地质数据库识别超过5000种矿物和岩石类型',
            'rock.features.composition.title': '成分分析',
            'rock.features.composition.desc': '获取有关矿物成分、晶体结构和形成过程的详细信息',
            'rock.features.geological.title': '地质背景',
            'rock.features.geological.desc': '了解您发现的标本的地质历史和形成环境',
            'rock.features.properties.title': '物理性质',
            'rock.features.properties.desc': '了解矿物的硬度、密度、光泽和其他物理特征',
            'rock.features.value.title': '价值评估',
            'rock.features.value.desc': '获取有关矿物发现的稀有性、收藏价值和潜在价值的见解',
            'rock.features.educational.title': '教育内容',
            'rock.features.educational.desc': '访问全面的地质指南、形成理论和矿物学教育',
            'rock.about.title': '关于 RockAiSnap',
            'rock.about.desc1': 'RockAiSnap 将成为地质学家、岩石爱好者、矿物收藏家以及所有对地球地质宝藏着迷的人的终极伴侣。我们的AI驱动识别系统将帮助您发现和了解周围的岩石和矿物。',
            'rock.about.desc2': '从常见的石英到稀有的宝石，RockAiSnap 将提供即时识别，包含详细的地质信息、形成历史以及对收藏家和爱好者的实用见解。',
            'rock.about.stats.minerals': '矿物类型',
            'rock.about.stats.accuracy': '目标准确率',
            'rock.about.stats.database': '全球数据库',
            'rock.contact.title': '保持更新',
            'rock.contact.subtitle': '在 RockAiSnap 发布时获得通知',
            'rock.contact.desc': '成为第一批了解 RockAiSnap 何时可用的人。发送您的邮箱，我们会通知您！',
            'rock.contact.form.name': '您的姓名',
            'rock.contact.form.email': '您的邮箱',
            'rock.contact.form.message': '告诉我们您对岩石/矿物识别的兴趣...',
            'rock.contact.form.submit': '有新版本时通知我',
            'rock.footer.tagline': '智能岩石和矿物识别',
            'rock.footer.apps': '其他应用',
            'rock.footer.bird': 'BirdAiSnap (已上线)',
            'rock.footer.mushroom': 'MushroomAiSnap (即将推出)',
            'rock.footer.insect': 'InsectAiSnap (即将推出)',
            'rock.footer.contact': '联系方式',
            'rock.footer.email': '邮件支持',
            'rock.footer.copyright': '© 2024 AiSnap Suite. 版权所有'
        }
    },
    'ru': { 
        name: 'Русский', 
        flag: '🇷🇺', 
        code: 'RU',
        translations: {
            'nav.home': 'Главная',
            'nav.apps': 'Приложения',
            'nav.features': 'Функции',
            'nav.about': 'О нас',
            'nav.contact': 'Контакты',
            'hero.title': 'Откройте природу с ИИ',
            'hero.description': 'Исследуйте природный мир с нашим комплексным набором приложений распознавания на основе ИИ. Определяйте птиц, камни, грибы и насекомых с помощью передовых технологий искусственного интеллекта.',
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
// 在主页上不自动切换语言，保持当前页面语言
let currentLang = localStorage.getItem('selectedLanguage') || 'en';

// 创建语言下拉菜单
function createLanguageDropdown() {
    try {
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
            <span id="currentLang">${languages[currentLang] ? languages[currentLang].code : 'EN'}</span>
            <span class="dropdown-arrow">▼</span>
        `;

        const menu = document.createElement('div');
        menu.className = 'lang-menu';

        // 显示所有可用语言
        Object.keys(languages).forEach(langCode => {
            try {
                const option = document.createElement('div');
                option.className = `lang-option ${langCode === currentLang ? 'active' : ''}`;
                option.innerHTML = `
                    <span class="flag">${languages[langCode].flag}</span>
                    <span class="lang-name">${languages[langCode].name}</span>
                    <span class="lang-code">${languages[langCode].code}</span>
                `;
                option.addEventListener('click', () => switchLanguage(langCode));
                menu.appendChild(option);
            } catch (error) {
                console.log('Error creating language option:', error);
            }
        });

        dropdown.appendChild(button);
        dropdown.appendChild(menu);
        languageSwitcher.appendChild(dropdown);

        // 修复点击事件 - 使用更简单的方法
        button.onclick = function(e) {
            try {
                e.preventDefault();
                e.stopPropagation();
                console.log('Language button clicked');
                dropdown.classList.toggle('active');
            } catch (error) {
                console.log('Button click error:', error);
            }
        };

        // 点击页面其他地方关闭下拉菜单
        document.onclick = function(e) {
            try {
                if (!dropdown.contains(e.target)) {
                    dropdown.classList.remove('active');
                }
            } catch (error) {
                console.log('Document click error:', error);
            }
        };

        console.log('Language dropdown created successfully');
    } catch (error) {
        console.log('Language dropdown creation error:', error);
    }
}

// 翻译页面内容
function translatePage(langCode) {
    if (!languages[langCode]) {
        console.log('Language not found:', langCode);
        return;
    }
    
    // 如果没有翻译内容，使用英语作为基础
    let translations = languages[langCode].translations || {};
    
    // 对于除中文和英文外的语言，使用英文内容作为默认
    if (langCode !== 'en' && langCode !== 'zh' && Object.keys(translations).length === 0) {
        console.log('Using English as base for:', langCode);
        // 使用英文内容，但保持语言标识
        translations = languages['en'].translations || {};
    }

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

    // 关闭下拉菜单 - 使用统一的CSS类控制
    const dropdown = document.querySelector('.lang-dropdown');
    if (dropdown) {
        dropdown.classList.remove('active');
    }

    // 在主页上只进行翻译，不跳转
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        // 主页 - 仅翻译内容，不跳转
        translatePage(langCode);
    } else {
        // 其他页面使用查询参数格式
        const currentPath = window.location.pathname;
        const currentSearch = window.location.search.replace(/[?&]lang=[^&]*/, '');
        const separator = currentSearch ? '&' : '?';
        const newUrl = currentPath + currentSearch + separator + 'lang=' + langCode;
        window.location.href = newUrl;
    }

    console.log('切换到语言:', languages[langCode].name);
}

// 防止重复初始化的标志
let isInitialized = false;

// 统一初始化函数
function initializePage() {
    if (isInitialized) {
        console.log('Page already initialized, skipping...');
        return;
    }
    isInitialized = true;
    
    // 防闪屏逻辑已移至index.html内联脚本（visibility方案）
    
    console.log('DOM loaded, initializing page...');
    
    // 检查 URL 参数中是否有语言设置
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang && languages[urlLang]) {
        currentLang = urlLang;
        localStorage.setItem('selectedLanguage', urlLang);
    }
    
    // 创建语言下拉菜单
    if (document.querySelector('.language-switcher')) {
        createLanguageDropdown();
    }
    
    // 初始化时应用当前语言
    translatePage(currentLang);
    
    // 为应用卡片添加点击处理
    setupAppCardHandlers();
    
    // 初始化现代 UI 交互
    initModernInteractions();
    
    console.log('Page initialization complete');
}

/**
 * 初始化现代 UI 交互
 */
function initModernInteractions() {
    // 1. 导航栏滚动效果
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. 移动端菜单切换
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // 点击菜单项后关闭菜单
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // 3. 滚动显示动画已禁用 - 防止闪烁
    // 所有元素直接可见，不使用 reveal-hidden/reveal-visible

    // 4. 磁性按钮效果已禁用 - 防止闪烁
    /*
    const magneticBtns = document.querySelectorAll('.btn.enhanced');
    magneticBtns.forEach(btn => {
        // ... (removed to prevent flicker)
    });
    */

    // 5. 3D 应用图标悬停已禁用 - 防止闪烁
    /*
    const appIcons = document.querySelectorAll('.apps-showcase.enhanced .app-icon');
    appIcons.forEach(icon => {
        // ... (removed to prevent flicker)
    });
    */
}

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
        
        // 跳转到新URL路径
        console.log('Article link navigation:', newHref);
        window.location.href = newHref;
    } catch (error) {
        console.log('Link navigation error:', error);
    }
}

// 为分类页面导航的函数（根据语言跳转到对应页面）
function navigateWithLanguage(pageName) {
    try {
        if (!pageName) return;
        
        const currentLang = localStorage.getItem('selectedLanguage') || 'en';
        
        // 对于分类页面，根据当前语言构建正确的URL
        let newUrl;
        if (currentLang === 'en') {
            // 英文版本直接使用原页面名
            newUrl = pageName;
        } else {
            // 其他语言版本使用查询参数格式，让服务器重定向到对应的语言目录
            const separator = pageName.includes('?') ? '&' : '?';
            newUrl = pageName + separator + 'lang=' + currentLang;
        }
        
        // 跳转到新URL
        console.log('Navigating to:', newUrl);
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
                    // 移除强制重定向，尊重用户的直接访问意图
                    // // 禁用强制重定向，尊重用户直接访问意图
 // window.location.href = newUrl;
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

// 安全的页面加载处理 - 仅用于文章页面
function safeInitialize() {
    try {
        handleArticleLanguageRedirect();
    } catch (error) {
        console.log('Initialization error:', error);
    }
}

// 在页面加载时执行初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        safeInitialize();
        initializePage();
    });
} else {
    // DOM已加载完成，直接执行
    safeInitialize();
    initializePage();
}

// ==================== 应用卡片点击处理 ====================
/**
 * 处理应用卡片点击事件
 * - 点击下载按钮 → 跳转应用商店
 * - 点击卡片其他区域 → 跳转详情页
 */
function setupAppCardHandlers() {
    // 为所有应用卡片添加点击处理
    document.querySelectorAll('.app-card[data-detail-url]').forEach(card => {
        const detailUrl = card.getAttribute('data-detail-url');
        
        // 为卡片添加点击事件
        card.addEventListener('click', function(e) {
            // 检查点击的是否是下载按钮或其子元素
            const isDownloadButton = e.target.closest('.btn-download, .ios-download, .android-download');
            
            // 如果点击的不是下载按钮，则跳转到详情页
            if (!isDownloadButton && detailUrl) {
                window.location.href = detailUrl;
            }
            // 如果点击的是下载按钮，不做任何处理，让按钮的默认行为生效
        });
        
        // 为卡片添加悬停样式提示
        card.style.cursor = 'pointer';
    });
    
    // 确保下载按钮的点击事件不会冒泡到卡片
    document.querySelectorAll('.app-card .btn-download').forEach(button => {
        button.addEventListener('click', function(e) {
            // 阻止事件冒泡到父元素（卡片）
            e.stopPropagation();
        });
    });
    
    console.log('App card click handlers initialized');
}
