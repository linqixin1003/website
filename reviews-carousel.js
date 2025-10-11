/**
 * 用户评价轮播系统
 * 包含自动播放、手动导航、触摸支持
 */

class ReviewsCarousel {
    constructor(selector) {
        this.carousel = document.querySelector(selector);
        if (!this.carousel) return;
        
        this.track = this.carousel.querySelector('.reviews-track');
        this.cards = Array.from(this.track.querySelectorAll('.review-card'));
        this.prevBtn = document.querySelector('.prev-btn');
        this.nextBtn = document.querySelector('.next-btn');
        this.dotsContainer = document.querySelector('.reviews-dots');
        
        this.currentIndex = 0;
        this.cardsPerView = this.getCardsPerView();
        this.autoPlayInterval = null;
        this.autoPlayDelay = 5000;
        
        this.init();
    }
    
    init() {
        this.createDots();
        this.updateCarousel();
        this.attachEvents();
        this.startAutoPlay();
        
        // 响应式调整
        window.addEventListener('resize', () => {
            clearTimeout(this.resizeTimer);
            this.resizeTimer = setTimeout(() => {
                this.cardsPerView = this.getCardsPerView();
                this.updateCarousel();
            }, 250);
        });
    }
    
    getCardsPerView() {
        const width = window.innerWidth;
        if (width >= 1200) return 3;
        if (width >= 768) return 2;
        return 1;
    }
    
    createDots() {
        if (!this.dotsContainer) return;
        
        const totalDots = Math.ceil(this.cards.length - this.cardsPerView + 1);
        this.dotsContainer.innerHTML = '';
        
        for (let i = 0; i < totalDots; i++) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (i === 0) dot.classList.add('active');
            dot.addEventListener('click', () => this.goToSlide(i));
            this.dotsContainer.appendChild(dot);
        }
        
        this.dots = Array.from(this.dotsContainer.querySelectorAll('.dot'));
    }
    
    updateCarousel() {
        const cardWidth = this.cards[0].offsetWidth;
        const gap = 30;
        const offset = -(this.currentIndex * (cardWidth + gap));
        
        this.track.style.transform = `translateX(${offset}px)`;
        
        // 更新导航按钮状态
        if (this.prevBtn) {
            this.prevBtn.disabled = this.currentIndex === 0;
        }
        
        if (this.nextBtn) {
            const maxIndex = this.cards.length - this.cardsPerView;
            this.nextBtn.disabled = this.currentIndex >= maxIndex;
        }
        
        // 更新指示点
        this.updateDots();
        
        // 更新卡片活跃状态
        this.updateActiveCards();
    }
    
    updateDots() {
        if (!this.dots) return;
        
        this.dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === this.currentIndex);
        });
    }
    
    updateActiveCards() {
        this.cards.forEach((card, index) => {
            const isVisible = index >= this.currentIndex && 
                            index < this.currentIndex + this.cardsPerView;
            card.style.opacity = isVisible ? '1' : '0.5';
            card.style.pointerEvents = isVisible ? 'auto' : 'none';
        });
    }
    
    next() {
        const maxIndex = this.cards.length - this.cardsPerView;
        if (this.currentIndex < maxIndex) {
            this.currentIndex++;
            this.updateCarousel();
            this.resetAutoPlay();
        }
    }
    
    prev() {
        if (this.currentIndex > 0) {
            this.currentIndex--;
            this.updateCarousel();
            this.resetAutoPlay();
        }
    }
    
    goToSlide(index) {
        this.currentIndex = index;
        this.updateCarousel();
        this.resetAutoPlay();
    }
    
    startAutoPlay() {
        this.autoPlayInterval = setInterval(() => {
            const maxIndex = this.cards.length - this.cardsPerView;
            if (this.currentIndex >= maxIndex) {
                this.currentIndex = 0;
            } else {
                this.currentIndex++;
            }
            this.updateCarousel();
        }, this.autoPlayDelay);
    }
    
    stopAutoPlay() {
        if (this.autoPlayInterval) {
            clearInterval(this.autoPlayInterval);
            this.autoPlayInterval = null;
        }
    }
    
    resetAutoPlay() {
        this.stopAutoPlay();
        this.startAutoPlay();
    }
    
    attachEvents() {
        // 按钮导航
        if (this.prevBtn) {
            this.prevBtn.addEventListener('click', () => this.prev());
        }
        
        if (this.nextBtn) {
            this.nextBtn.addEventListener('click', () => this.next());
        }
        
        // 键盘导航
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.prev();
            if (e.key === 'ArrowRight') this.next();
        });
        
        // 鼠标悬停暂停自动播放
        this.carousel.addEventListener('mouseenter', () => this.stopAutoPlay());
        this.carousel.addEventListener('mouseleave', () => this.startAutoPlay());
        
        // 触摸滑动支持
        this.addTouchSupport();
    }
    
    addTouchSupport() {
        let touchStartX = 0;
        let touchEndX = 0;
        let touchStartY = 0;
        let touchEndY = 0;
        
        this.track.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
            this.stopAutoPlay();
        }, { passive: true });
        
        this.track.addEventListener('touchmove', (e) => {
            touchEndX = e.touches[0].clientX;
            touchEndY = e.touches[0].clientY;
        }, { passive: true });
        
        this.track.addEventListener('touchend', () => {
            const deltaX = touchStartX - touchEndX;
            const deltaY = Math.abs(touchStartY - touchEndY);
            
            // 只有水平滑动距离大于50px且垂直距离小于30px时才触发
            if (Math.abs(deltaX) > 50 && deltaY < 30) {
                if (deltaX > 0) {
                    // 向左滑动，显示下一个
                    this.next();
                } else {
                    // 向右滑动，显示上一个
                    this.prev();
                }
            }
            
            this.startAutoPlay();
        });
    }
}

// 初始化轮播
document.addEventListener('DOMContentLoaded', () => {
    const reviewsCarousel = new ReviewsCarousel('.reviews-carousel');
    
    // 导出到全局供调试使用
    window.reviewsCarousel = reviewsCarousel;
    
    console.log('🎠 用户评价轮播已初始化');
});
