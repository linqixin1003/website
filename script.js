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
        'footer.copyright': '© 2024 BirdAiSnap. All rights reserved'
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
        'footer.copyright': '© 2024 BirdAiSnap. 版权所有'
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