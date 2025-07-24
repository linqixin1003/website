// 文章多语言数据
const articleTranslations = {
    // Birdwatching articles (10篇)
    'birdwatching': {
        '01-getting-started': {
            'en': {
                'title': 'Getting Started with Bird Watching',
                'subtitle': 'Your complete guide to beginning an amazing birding journey',
                'content': {
                    'intro': 'Bird watching is one of the most rewarding outdoor activities that connects you with nature...',
                    'section1': 'What is Bird Watching?',
                    'section2': 'Getting Started',
                    'section3': 'Basic Equipment',
                    'section4': 'First Steps'
                }
            },
            'zh': {
                'title': '观鸟入门指南',
                'subtitle': '开始精彩观鸟之旅的完整指南',
                'content': {
                    'intro': '观鸟是最有意义的户外活动之一，让您与自然建立联系...',
                    'section1': '什么是观鸟？',
                    'section2': '入门指南',
                    'section3': '基础装备',
                    'section4': '第一步'
                }
            }
        },
        '02-essential-equipment': {
            'en': {
                'title': 'Essential Bird Watching Equipment',
                'subtitle': 'Must-have tools and equipment for successful bird watching adventures',
                'content': {
                    'intro': 'Having the right equipment can make the difference between a frustrating and rewarding birding experience...',
                    'section1': 'Binoculars',
                    'section2': 'Field Guides',
                    'section3': 'Clothing and Accessories',
                    'section4': 'Optional Equipment'
                }
            },
            'zh': {
                'title': '观鸟必备装备',
                'subtitle': '成功观鸟冒险所需的必备工具和装备',
                'content': {
                    'intro': '拥有合适的装备能够决定观鸟体验是令人沮丧还是令人满意...',
                    'section1': '双筒望远镜',
                    'section2': '野外指南',
                    'section3': '服装和配件',
                    'section4': '可选装备'
                }
            }
        },
        '03-identification-techniques': {
            'en': {
                'title': 'Bird Identification Techniques',
                'subtitle': 'Master the art of identifying birds through systematic observation',
                'content': {
                    'intro': 'Learning to identify birds is a skill that develops over time with practice and patience...',
                    'section1': 'Size and Shape',
                    'section2': 'Color and Markings',
                    'section3': 'Behavior and Habitat',
                    'section4': 'Sounds and Calls'
                }
            },
            'zh': {
                'title': '鸟类识别技巧',
                'subtitle': '通过系统观察掌握鸟类识别的艺术',
                'content': {
                    'intro': '学习识别鸟类是一项需要时间、练习和耐心才能发展的技能...',
                    'section1': '大小和形状',
                    'section2': '颜色和标记',
                    'section3': '行为和栖息地',
                    'section4': '声音和叫声'
                }
            }
        },
        '04-best-locations': {
            'en': {
                'title': 'Best Bird Watching Locations',
                'subtitle': 'Discover the world\'s premier birding destinations and hidden gems',
                'content': {
                    'intro': 'The world is full of incredible birding locations, each offering unique species and experiences...',
                    'section1': 'Local Parks and Reserves',
                    'section2': 'Wetlands and Coastal Areas',
                    'section3': 'Mountain and Forest Regions',
                    'section4': 'International Destinations'
                }
            },
            'zh': {
                'title': '最佳观鸟地点',
                'subtitle': '发现世界顶级观鸟目的地和隐藏的宝石',
                'content': {
                    'intro': '世界上有许多令人难以置信的观鸟地点，每个都提供独特的物种和体验...',
                    'section1': '当地公园和保护区',
                    'section2': '湿地和沿海地区',
                    'section3': '山区和森林地区',
                    'section4': '国际目的地'
                }
            }
        },
        '05-seasonal-guide': {
            'en': {
                'title': 'Seasonal Bird Watching Guide',
                'subtitle': 'Discover how bird activity changes throughout the year',
                'content': {
                    'intro': 'Bird behavior and activity patterns change dramatically with the seasons...',
                    'section1': 'Spring Migration',
                    'section2': 'Summer Breeding',
                    'section3': 'Fall Migration',
                    'section4': 'Winter Residents'
                }
            },
            'zh': {
                'title': '季节性观鸟指南',
                'subtitle': '发现鸟类活动如何随季节变化',
                'content': {
                    'intro': '鸟类的行为和活动模式随季节发生显著变化...',
                    'section1': '春季迁徙',
                    'section2': '夏季繁殖',
                    'section3': '秋季迁徙',
                    'section4': '冬季留鸟'
                }
            }
        },
        '06-photography-tips': {
            'en': {
                'title': 'Photography Tips for Bird Watchers',
                'subtitle': 'Capture stunning bird photos with essential techniques',
                'content': {
                    'intro': 'Bird photography combines the patience of birding with the technical skills of photography...',
                    'section1': 'Camera Equipment',
                    'section2': 'Composition Techniques',
                    'section3': 'Lighting and Settings',
                    'section4': 'Ethical Considerations'
                }
            },
            'zh': {
                'title': '观鸟者摄影技巧',
                'subtitle': '用基本技巧拍摄令人惊叹的鸟类照片',
                'content': {
                    'intro': '鸟类摄影结合了观鸟的耐心和摄影的技术技能...',
                    'section1': '相机设备',
                    'section2': '构图技巧',
                    'section3': '光线和设置',
                    'section4': '伦理考虑'
                }
            }
        },
        '07-behavior-observation': {
            'en': {
                'title': 'Bird Behavior Observation',
                'subtitle': 'Learn to interpret bird behaviors and understand their world',
                'content': {
                    'intro': 'Understanding bird behavior adds depth and meaning to your birding experience...',
                    'section1': 'Feeding Behaviors',
                    'section2': 'Social Interactions',
                    'section3': 'Territorial Displays',
                    'section4': 'Mating Rituals'
                }
            },
            'zh': {
                'title': '鸟类行为观察',
                'subtitle': '学会解读鸟类行为并理解它们的世界',
                'content': {
                    'intro': '理解鸟类行为为您的观鸟体验增添深度和意义...',
                    'section1': '觅食行为',
                    'section2': '社会互动',
                    'section3': '领域展示',
                    'section4': '交配仪式'
                }
            }
        },
        '08-song-identification': {
            'en': {
                'title': 'Bird Song Identification',
                'subtitle': 'Master the art of identifying birds by their songs and calls',
                'content': {
                    'intro': 'Learning bird songs opens up a whole new dimension to birding...',
                    'section1': 'Types of Vocalizations',
                    'section2': 'Learning Techniques',
                    'section3': 'Recording and Apps',
                    'section4': 'Common Song Patterns'
                }
            },
            'zh': {
                'title': '鸟类鸣声识别',
                'subtitle': '掌握通过鸣声和叫声识别鸟类的艺术',
                'content': {
                    'intro': '学习鸟类鸣声为观鸟开启了全新的维度...',
                    'section1': '发声类型',
                    'section2': '学习技巧',
                    'section3': '录音和应用',
                    'section4': '常见鸣声模式'
                }
            }
        },
        '09-ethics-conservation': {
            'en': {
                'title': 'Bird Watching Ethics and Conservation',
                'subtitle': 'Responsible birding practices that protect the birds we love',
                'content': {
                    'intro': 'Ethical birding ensures that our hobby contributes to bird conservation...',
                    'section1': 'Minimizing Disturbance',
                    'section2': 'Habitat Protection',
                    'section3': 'Citizen Science',
                    'section4': 'Conservation Support'
                }
            },
            'zh': {
                'title': '观鸟伦理与保护',
                'subtitle': '保护我们所爱鸟类的负责任观鸟实践',
                'content': {
                    'intro': '道德观鸟确保我们的爱好有助于鸟类保护...',
                    'section1': '减少干扰',
                    'section2': '栖息地保护',
                    'section3': '公民科学',
                    'section4': '保护支持'
                }
            }
        },
        '10-journal-keeping': {
            'en': {
                'title': 'Keeping a Bird Watching Journal',
                'subtitle': 'Document your birding adventures and build a personal record',
                'content': {
                    'intro': 'A birding journal becomes a treasured record of your experiences and observations...',
                    'section1': 'What to Record',
                    'section2': 'Journal Formats',
                    'section3': 'Digital vs Paper',
                    'section4': 'Long-term Benefits'
                }
            },
            'zh': {
                'title': '观鸟日志记录',
                'subtitle': '记录您的观鸟冒险并建立个人记录',
                'content': {
                    'intro': '观鸟日志成为您体验和观察的珍贵记录...',
                    'section1': '记录内容',
                    'section2': '日志格式',
                    'section3': '数字vs纸质',
                    'section4': '长期益处'
                }
            }
        }
    },
    
    // Scientific Wonders articles (10篇)
    'scientific-wonders': {
        '01-bird-flight-mechanics': {
            'en': {
                'title': 'The Mechanics of Bird Flight',
                'subtitle': 'Discover the fascinating physics behind bird flight',
                'content': {
                    'intro': 'Bird flight is one of nature\'s most remarkable achievements...',
                    'section1': 'Wing Structure and Design',
                    'section2': 'Aerodynamic Principles',
                    'section3': 'Flight Muscles and Energy',
                    'section4': 'Different Flight Styles'
                }
            },
            'zh': {
                'title': '鸟类飞行机制',
                'subtitle': '发现鸟类飞行背后的迷人物理学',
                'content': {
                    'intro': '鸟类飞行是自然界最卓越的成就之一...',
                    'section1': '翅膀结构和设计',
                    'section2': '空气动力学原理',
                    'section3': '飞行肌肉和能量',
                    'section4': '不同的飞行方式'
                }
            }
        },
        '02-magnetic-navigation': {
            'en': {
                'title': 'Magnetic Navigation in Birds',
                'subtitle': 'How birds use Earth\'s magnetic field for navigation',
                'content': {
                    'intro': 'Birds possess an extraordinary ability to navigate using magnetic fields...',
                    'section1': 'Magnetoreception Mechanisms',
                    'section2': 'Internal Compass Systems',
                    'section3': 'Migration Routes',
                    'section4': 'Research Discoveries'
                }
            },
            'zh': {
                'title': '鸟类磁导航',
                'subtitle': '鸟类如何使用地球磁场进行导航',
                'content': {
                    'intro': '鸟类拥有使用磁场导航的非凡能力...',
                    'section1': '磁感受机制',
                    'section2': '内部指南针系统',
                    'section3': '迁徙路线',
                    'section4': '研究发现'
                }
            }
        }
        // ... 继续添加其他文章
    }
    
    // 继续添加其他分类的文章...
};

// 导出翻译数据
if (typeof module !== 'undefined' && module.exports) {
    module.exports = articleTranslations;
} else {
    window.articleTranslations = articleTranslations;
}