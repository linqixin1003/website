/**
 * 日间/夜间模式切换系统
 * 支持系统偏好检测、本地存储、平滑过渡
 */

class DarkModeToggle {
    constructor() {
        this.storageKey = 'theme-preference';
        this.theme = this.getStoredTheme() || this.getSystemTheme();
        
        this.init();
    }
    
    init() {
        // 创建切换按钮
        this.createToggleButton();
        
        // 应用初始主题
        this.applyTheme(this.theme, false);
        
        // 监听系统主题变化
        this.watchSystemTheme();
        
        console.log(`🌓 暗色模式系统已初始化 (当前: ${this.theme})`);
    }
    
    createToggleButton() {
        // 检查按钮是否已存在
        if (document.querySelector('.theme-toggle')) return;
        
        const button = document.createElement('button');
        button.className = 'theme-toggle';
        button.setAttribute('aria-label', 'Toggle dark mode');
        button.setAttribute('title', 'Toggle dark mode');
        
        button.innerHTML = `
            <div class="theme-toggle-icons">
                <span class="theme-icon sun">☀️</span>
                <span class="theme-icon moon">🌙</span>
            </div>
            <span class="theme-toggle-tooltip">Switch to ${this.theme === 'dark' ? 'light' : 'dark'} mode</span>
        `;
        
        button.addEventListener('click', () => this.toggle());
        
        // 添加到页面
        document.body.appendChild(button);
        
        this.button = button;
    }
    
    toggle() {
        const newTheme = this.theme === 'light' ? 'dark' : 'light';
        this.applyTheme(newTheme, true);
        this.storeTheme(newTheme);
        this.theme = newTheme;
        
        // 更新提示文本
        const tooltip = this.button.querySelector('.theme-toggle-tooltip');
        if (tooltip) {
            tooltip.textContent = `Switch to ${newTheme === 'dark' ? 'light' : 'dark'} mode`;
        }
        
        // 触发自定义事件
        window.dispatchEvent(new CustomEvent('themechange', {
            detail: { theme: newTheme }
        }));
        
        // 反馈动画
        this.playFeedbackAnimation();
        
        console.log(`🌓 主题已切换到: ${newTheme}`);
    }
    
    applyTheme(theme, animate = true) {
        const html = document.documentElement;
        
        if (animate) {
            // 添加过渡类
            html.classList.add('theme-transitioning');
            
            // 移除过渡类
            setTimeout(() => {
                html.classList.remove('theme-transitioning');
            }, 300);
        }
        
        // 设置主题属性
        html.setAttribute('data-theme', theme);
        
        // 更新meta主题色
        this.updateMetaThemeColor(theme);
    }
    
    updateMetaThemeColor(theme) {
        let metaThemeColor = document.querySelector('meta[name="theme-color"]');
        
        if (!metaThemeColor) {
            metaThemeColor = document.createElement('meta');
            metaThemeColor.name = 'theme-color';
            document.head.appendChild(metaThemeColor);
        }
        
        metaThemeColor.content = theme === 'dark' ? '#0f172a' : '#ffffff';
    }
    
    getStoredTheme() {
        try {
            return localStorage.getItem(this.storageKey);
        } catch (e) {
            console.warn('无法访问 localStorage:', e);
            return null;
        }
    }
    
    storeTheme(theme) {
        try {
            localStorage.setItem(this.storageKey, theme);
        } catch (e) {
            console.warn('无法保存主题偏好:', e);
        }
    }
    
    getSystemTheme() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }
    
    watchSystemTheme() {
        if (!window.matchMedia) return;
        
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        // 现代浏览器
        if (mediaQuery.addEventListener) {
            mediaQuery.addEventListener('change', (e) => {
                // 只有在用户没有手动设置时才跟随系统
                if (!this.getStoredTheme()) {
                    const newTheme = e.matches ? 'dark' : 'light';
                    this.applyTheme(newTheme, true);
                    this.theme = newTheme;
                    console.log(`🌓 系统主题变化: ${newTheme}`);
                }
            });
        }
        // 旧浏览器
        else if (mediaQuery.addListener) {
            mediaQuery.addListener((e) => {
                if (!this.getStoredTheme()) {
                    const newTheme = e.matches ? 'dark' : 'light';
                    this.applyTheme(newTheme, true);
                    this.theme = newTheme;
                }
            });
        }
    }
    
    playFeedbackAnimation() {
        // 创建粒子效果
        const particles = 12;
        const colors = this.theme === 'dark' ? ['#667eea', '#764ba2', '#ffffff'] : ['#fbbf24', '#f59e0b', '#ffffff'];
        
        for (let i = 0; i < particles; i++) {
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: fixed;
                bottom: ${30 + 30}px;
                right: ${30 + 30}px;
                width: 8px;
                height: 8px;
                background: ${colors[Math.floor(Math.random() * colors.length)]};
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
            `;
            
            document.body.appendChild(particle);
            
            const angle = (i / particles) * Math.PI * 2;
            const velocity = 50 + Math.random() * 50;
            const tx = Math.cos(angle) * velocity;
            const ty = Math.sin(angle) * velocity;
            
            particle.animate([
                {
                    transform: 'translate(0, 0) scale(1)',
                    opacity: 1
                },
                {
                    transform: `translate(${tx}px, ${ty}px) scale(0)`,
                    opacity: 0
                }
            ], {
                duration: 600,
                easing: 'cubic-bezier(0.4, 0, 1, 1)'
            }).onfinish = () => particle.remove();
        }
    }
    
    // 公共API
    setTheme(theme) {
        if (theme !== 'light' && theme !== 'dark') {
            console.warn('无效的主题值:', theme);
            return;
        }
        
        this.applyTheme(theme, true);
        this.storeTheme(theme);
        this.theme = theme;
    }
    
    getTheme() {
        return this.theme;
    }
    
    resetToSystem() {
        localStorage.removeItem(this.storageKey);
        const systemTheme = this.getSystemTheme();
        this.applyTheme(systemTheme, true);
        this.theme = systemTheme;
        console.log('🌓 已重置为系统主题');
    }
}

// 主题检测已移至 index.html <head> 内联脚本中，确保在 CSS 加载前执行
// 这里不再重复设置 data-theme，避免闪屏

// DOM加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    // 移除 no-transition 类，恢复用户手动切换主题时的过渡动画
    // 使用 requestAnimationFrame 确保首帧渲染完成后再移除
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            document.documentElement.classList.remove('no-transition');
        });
    });
    
    window.darkModeToggle = new DarkModeToggle();
    
    // 导出到全局供外部使用
    window.setTheme = (theme) => window.darkModeToggle.setTheme(theme);
    window.getTheme = () => window.darkModeToggle.getTheme();
    window.resetThemeToSystem = () => window.darkModeToggle.resetToSystem();
});

// 监听主题变化事件
window.addEventListener('themechange', (e) => {
    console.log('主题变化事件:', e.detail.theme);
    
    // 可以在这里添加其他需要响应主题变化的逻辑
    // 例如：更新图表颜色、重新渲染某些组件等
});

// 导出类供模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DarkModeToggle;
}
