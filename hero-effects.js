/**
 * Hero区域动效系统
 * 包含粒子动画、实时数据、交互效果
 */

// ==================== 粒子系统 ====================
class ParticleSystem {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.particleCount = 50;
        this.colors = ['#667eea', '#764ba2', '#4A90E2', '#8B7355'];
        this.isAnimating = true;
        this.animationId = null;
        
        this.resize();
        this.init();
        this.animate();
        
        window.addEventListener('resize', () => this.resize());
        
        // 页面不可见时暂停动画以节省资源
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.pause();
            } else {
                this.resume();
            }
        });
    }
    
    pause() {
        this.isAnimating = false;
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }
    
    resume() {
        if (!this.isAnimating) {
            this.isAnimating = true;
            this.animate();
        }
    }
    
    resize() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
    }
    
    init() {
        this.particles = [];
        for (let i = 0; i < this.particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 3 + 1,
                color: this.colors[Math.floor(Math.random() * this.colors.length)],
                opacity: Math.random() * 0.5 + 0.3
            });
        }
    }
    
    animate() {
        if (!this.isAnimating) return;
        
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.particles.forEach((particle, index) => {
            // 更新位置
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // 边界检测
            if (particle.x < 0 || particle.x > this.canvas.width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > this.canvas.height) particle.vy *= -1;
            
            // 绘制粒子
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = particle.color;
            this.ctx.globalAlpha = particle.opacity;
            this.ctx.fill();
            
            // 绘制连线
            this.particles.slice(index + 1).forEach(otherParticle => {
                const dx = particle.x - otherParticle.x;
                const dy = particle.y - otherParticle.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 150) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(particle.x, particle.y);
                    this.ctx.lineTo(otherParticle.x, otherParticle.y);
                    this.ctx.strokeStyle = particle.color;
                    this.ctx.globalAlpha = (1 - distance / 150) * 0.2;
                    this.ctx.lineWidth = 1;
                    this.ctx.stroke();
                }
            });
        });
        
        this.ctx.globalAlpha = 1;
        this.animationId = requestAnimationFrame(() => this.animate());
    }
}

// ==================== 实时数据计数器 ====================
class DataCounter {
    constructor(elementId, targetValue, duration = 2000, suffix = '') {
        this.element = document.getElementById(elementId);
        if (!this.element) return;
        
        this.targetValue = targetValue;
        this.duration = duration;
        this.suffix = suffix;
        this.currentValue = 0;
        this.startTime = null;
        this.isAnimating = false;
    }
    
    start() {
        if (this.isAnimating) return;
        this.isAnimating = true;
        this.startTime = Date.now();
        this.animate();
    }
    
    animate() {
        const now = Date.now();
        const progress = Math.min((now - this.startTime) / this.duration, 1);
        
        // 使用缓动函数
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        this.currentValue = Math.floor(this.targetValue * easeOutQuart);
        
        this.element.textContent = this.formatNumber(this.currentValue) + this.suffix;
        
        if (progress < 1) {
            requestAnimationFrame(() => this.animate());
        } else {
            this.isAnimating = false;
        }
    }
    
    formatNumber(num) {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        } else if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }
}

// ==================== 在线用户模拟 ====================
class OnlineUsersSimulator {
    constructor(elementId, baseCount = 2341) {
        this.element = document.getElementById(elementId);
        if (!this.element) return;
        
        this.baseCount = baseCount;
        this.currentCount = baseCount;
        this.update();
        
        // 每5-10秒随机更新
        setInterval(() => this.update(), Math.random() * 5000 + 5000);
    }
    
    update() {
        // 随机增减5-20人
        const change = Math.floor(Math.random() * 15) - 7;
        this.currentCount = Math.max(this.baseCount - 100, 
                           Math.min(this.baseCount + 100, this.currentCount + change));
        
        this.element.textContent = this.currentCount.toLocaleString();
    }
}

// ==================== 应用图标3D效果 ====================
class AppIcon3DEffect {
    constructor(selector) {
        this.icons = document.querySelectorAll(selector);
        this.init();
    }
    
    init() {
        this.icons.forEach(icon => {
            icon.addEventListener('mousemove', (e) => this.handleMouseMove(e, icon));
            icon.addEventListener('mouseleave', (e) => this.handleMouseLeave(e, icon));
        });
    }
    
    handleMouseMove(e, icon) {
        const rect = icon.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        icon.style.transform = `
            perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            translateY(-15px)
            scale(1.05)
        `;
    }
    
    handleMouseLeave(e, icon) {
        icon.style.transform = '';
    }
}

// ==================== Intersection Observer 延迟加载 ====================
class LazyAnimator {
    constructor(selector, animationClass = 'animate') {
        this.elements = document.querySelectorAll(selector);
        this.animationClass = animationClass;
        this.init();
    }
    
    init() {
        const options = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add(this.animationClass);
                    observer.unobserve(entry.target);
                }
            });
        }, options);
        
        this.elements.forEach(el => observer.observe(el));
    }
}

// ==================== 按钮波纹效果 ====================
class ButtonRippleEffect {
    constructor(selector) {
        this.buttons = document.querySelectorAll(selector);
        this.init();
    }
    
    init() {
        this.buttons.forEach(button => {
            button.addEventListener('click', (e) => this.createRipple(e, button));
        });
    }
    
    createRipple(event, button) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple-effect');
        
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        button.style.position = 'relative';
        button.style.overflow = 'hidden';
        button.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
}

// 添加波纹效果CSS
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
.ripple-effect {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.6);
    transform: scale(0);
    animation: ripple-animation 0.6s ease-out;
    pointer-events: none;
}

@keyframes ripple-animation {
    to {
        transform: scale(4);
        opacity: 0;
    }
}
`;
document.head.appendChild(rippleStyle);

// ==================== 初始化所有效果 ====================
document.addEventListener('DOMContentLoaded', () => {
    // 粒子系统
    if (document.getElementById('particles-canvas')) {
        new ParticleSystem('particles-canvas');
    }
    
    // 实时数据计数器
    const downloadCounter = new DataCounter('downloads-count', 156340, 2500);
    const identificationCounter = new DataCounter('identifications-count', 1283420, 2800);
    
    // 使用Intersection Observer触发计数器
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                downloadCounter.start();
                identificationCounter.start();
                heroObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });
    
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        heroObserver.observe(heroSection);
    }
    
    // 在线用户模拟
    new OnlineUsersSimulator('online-users');
    
    // 应用图标3D效果
    new AppIcon3DEffect('.apps-showcase.enhanced .app-icon');
    
    // 延迟动画
    new LazyAnimator('.hero-content > *');
    
    // 按钮波纹效果
    new ButtonRippleEffect('.btn.enhanced');
    
    console.log('🎨 Hero增强效果已加载');
});

// ==================== 导出供外部使用 ====================
window.HeroEffects = {
    ParticleSystem,
    DataCounter,
    OnlineUsersSimulator,
    AppIcon3DEffect,
    LazyAnimator,
    ButtonRippleEffect
};
