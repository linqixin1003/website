/**
 * 社交分享系统
 * 支持多平台分享、复制链接、邮件、打印
 */

class SocialShare {
    constructor() {
        this.url = window.location.href;
        this.title = document.title;
        this.description = document.querySelector('meta[name="description"]')?.content || '';
        
        this.init();
    }
    
    init() {
        this.createShareButtons();
        this.attachEvents();
        
        console.log('📱 社交分享系统已初始化');
    }
    
    createShareButtons() {
        // 检查是否已存在
        if (document.querySelector('.social-share')) return;
        
        const shareContainer = document.createElement('div');
        shareContainer.className = 'social-share';
        shareContainer.innerHTML = `
            <button class="social-share-btn share-twitter" data-platform="twitter" aria-label="Share on Twitter">
                <span>𝕏</span>
                <span class="share-tooltip">Share on X</span>
            </button>
            <button class="social-share-btn share-facebook" data-platform="facebook" aria-label="Share on Facebook">
                <span>f</span>
                <span class="share-tooltip">Share on Facebook</span>
            </button>
            <button class="social-share-btn share-linkedin" data-platform="linkedin" aria-label="Share on LinkedIn">
                <span>in</span>
                <span class="share-tooltip">Share on LinkedIn</span>
            </button>
            <button class="social-share-btn share-whatsapp" data-platform="whatsapp" aria-label="Share on WhatsApp">
                <span>💬</span>
                <span class="share-tooltip">Share on WhatsApp</span>
            </button>
            <button class="social-share-btn share-email" data-platform="email" aria-label="Share via Email">
                <span>✉️</span>
                <span class="share-tooltip">Share via Email</span>
            </button>
            <button class="social-share-btn share-copy" data-platform="copy" aria-label="Copy Link">
                <span>🔗</span>
                <span class="share-tooltip">Copy Link</span>
            </button>
        `;
        
        document.body.appendChild(shareContainer);
    }
    
    attachEvents() {
        document.querySelectorAll('.social-share-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const platform = btn.dataset.platform;
                this.share(platform);
                
                // GA4 事件追踪
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'share', {
                        'method': platform,
                        'content_type': 'website',
                        'item_id': this.url
                    });
                }
            });
        });
    }
    
    share(platform) {
        const encodedUrl = encodeURIComponent(this.url);
        const encodedTitle = encodeURIComponent(this.title);
        const encodedDesc = encodeURIComponent(this.description);
        
        const shareUrls = {
            twitter: `https://twitter.com/intent/tweet?url=${encodedUrl}&text=${encodedTitle}`,
            facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`,
            linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`,
            whatsapp: `https://wa.me/?text=${encodedTitle}%20${encodedUrl}`,
            email: `mailto:?subject=${encodedTitle}&body=${encodedDesc}%0A%0A${encodedUrl}`,
        };
        
        if (platform === 'copy') {
            this.copyToClipboard(this.url);
        } else if (shareUrls[platform]) {
            window.open(shareUrls[platform], '_blank', 'width=600,height=400');
        }
    }
    
    async copyToClipboard(text) {
        try {
            if (navigator.clipboard && navigator.clipboard.writeText) {
                await navigator.clipboard.writeText(text);
                this.showSuccess('Link copied to clipboard!');
            } else {
                // 降级方案
                const textarea = document.createElement('textarea');
                textarea.value = text;
                textarea.style.position = 'fixed';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                this.showSuccess('Link copied to clipboard!');
            }
        } catch (err) {
            console.error('复制失败:', err);
            this.showSuccess('Failed to copy link', 'error');
        }
    }
    
    showSuccess(message, type = 'success') {
        // 移除已存在的提示
        const existing = document.querySelector('.share-success');
        if (existing) existing.remove();
        
        const successDiv = document.createElement('div');
        successDiv.className = 'share-success';
        successDiv.innerHTML = `
            <span class="share-success-icon">${type === 'success' ? '✓' : '✗'}</span>
            <span>${message}</span>
        `;
        
        document.body.appendChild(successDiv);
        
        // 显示动画
        setTimeout(() => successDiv.classList.add('show'), 100);
        
        // 3秒后移除
        setTimeout(() => {
            successDiv.classList.remove('show');
            setTimeout(() => successDiv.remove(), 400);
        }, 3000);
    }
    
    // 原生分享API（如果支持）
    async nativeShare() {
        if (navigator.share) {
            try {
                await navigator.share({
                    title: this.title,
                    text: this.description,
                    url: this.url
                });
                console.log('✓ 原生分享成功');
            } catch (err) {
                if (err.name !== 'AbortError') {
                    console.error('原生分享失败:', err);
                }
            }
        }
    }
}

// 添加分享按钮到特定元素
function addInlineShareButtons(selector) {
    const elements = document.querySelectorAll(selector);
    
    elements.forEach(element => {
        const shareBtn = document.createElement('button');
        shareBtn.className = 'inline-share-btn';
        shareBtn.innerHTML = '📤 Share';
        shareBtn.style.cssText = `
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            margin: 10px 0;
            transition: all 0.3s ease;
        `;
        
        shareBtn.addEventListener('mouseover', () => {
            shareBtn.style.transform = 'scale(1.05)';
            shareBtn.style.boxShadow = '0 10px 25px rgba(102, 126, 234, 0.3)';
        });
        
        shareBtn.addEventListener('mouseout', () => {
            shareBtn.style.transform = 'scale(1)';
            shareBtn.style.boxShadow = 'none';
        });
        
        shareBtn.addEventListener('click', () => {
            if (window.socialShare) {
                // 检查是否支持原生分享
                if (navigator.share) {
                    window.socialShare.nativeShare();
                } else {
                    // 打开分享选项
                    alert('Please use the share buttons on the left side of the page');
                }
            }
        });
        
        element.appendChild(shareBtn);
    });
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    window.socialShare = new SocialShare();
    
    // 可选：为特定内容添加内联分享按钮
    // addInlineShareButtons('.review-card');
    
    // 监听滚动，自动隐藏/显示分享按钮
    let lastScroll = 0;
    const shareContainer = document.querySelector('.social-share');
    
    if (shareContainer) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 300) {
                shareContainer.style.opacity = '1';
                shareContainer.style.pointerEvents = 'auto';
            } else {
                shareContainer.style.opacity = '0.5';
            }
            
            lastScroll = currentScroll;
        }, { passive: true });
    }
});

// 导出供外部使用
window.addInlineShareButtons = addInlineShareButtons;
