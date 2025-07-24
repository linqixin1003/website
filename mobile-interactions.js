// Enhanced Mobile Interactions for Bird Watching Pages

document.addEventListener('DOMContentLoaded', function() {
    // Mobile-specific enhancements
    if (window.innerWidth <= 768) {
        initMobileEnhancements();
    }
    
    // Re-initialize on resize
    window.addEventListener('resize', function() {
        if (window.innerWidth <= 768) {
            initMobileEnhancements();
        }
    });
});

function initMobileEnhancements() {
    // Smooth scroll animations
    initScrollAnimations();
    
    // Touch interactions
    initTouchInteractions();
    
    // Mobile navigation enhancements
    enhanceMobileNavigation();
    
    // Image lazy loading
    initLazyLoading();
    
    // Performance optimizations
    initPerformanceOptimizations();
}

// Scroll animations for mobile
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                // Stagger animation for cards
                if (entry.target.classList.contains('content-section')) {
                    const cards = entry.target.querySelectorAll('.beginner-card, .journal-card, .ethics-card, .song-card, .behavior-card, .technique-card, .location-card, .season-card, .equipment-card, .identification-card');
                    cards.forEach((card, index) => {
                        setTimeout(() => {
                            card.style.animation = `fadeInUp 0.6s ease-out ${index * 0.1}s both`;
                        }, index * 100);
                    });
                }
            }
        });
    }, observerOptions);

    // Observe content sections
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        observer.observe(section);
    });
}

// Enhanced touch interactions
function initTouchInteractions() {
    // Add touch feedback to cards
    const cards = document.querySelectorAll('.beginner-card, .journal-card, .ethics-card, .song-card, .behavior-card, .technique-card, .location-card, .season-card, .equipment-card, .identification-card');
    
    cards.forEach(card => {
        // Touch start
        card.addEventListener('touchstart', function(e) {
            this.style.transform = 'scale(0.98)';
            this.style.transition = 'transform 0.1s ease';
        }, { passive: true });
        
        // Touch end
        card.addEventListener('touchend', function(e) {
            this.style.transform = 'scale(1)';
            this.style.transition = 'transform 0.3s ease';
        }, { passive: true });
        
        // Touch cancel
        card.addEventListener('touchcancel', function(e) {
            this.style.transform = 'scale(1)';
            this.style.transition = 'transform 0.3s ease';
        }, { passive: true });
    });
    
    // Enhanced image interactions
    const images = document.querySelectorAll('.bird-image');
    images.forEach(image => {
        image.addEventListener('touchstart', function(e) {
            this.style.transform = 'scale(1.02)';
            this.style.transition = 'transform 0.2s ease';
        }, { passive: true });
        
        image.addEventListener('touchend', function(e) {
            this.style.transform = 'scale(1)';
            this.style.transition = 'transform 0.4s ease';
        }, { passive: true });
    });
}

// Enhanced mobile navigation
function enhanceMobileNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    if (!navToggle || !navMenu) return;
    
    // Close menu when clicking outside
    document.addEventListener('touchstart', function(e) {
        if (navMenu.classList.contains('active') && 
            !navMenu.contains(e.target) && 
            !navToggle.contains(e.target)) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        }
    }, { passive: true });
    
    // Close menu when clicking on links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });
    
    // Prevent body scroll when menu is open
    navToggle.addEventListener('click', function() {
        if (navMenu.classList.contains('active')) {
            document.body.style.overflow = '';
        } else {
            document.body.style.overflow = 'hidden';
        }
    });
    
    // Smooth scroll for anchor links
    navLinks.forEach(link => {
        if (link.getAttribute('href').startsWith('#')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        }
    });
}

// Lazy loading for images
function initLazyLoading() {
    const images = document.querySelectorAll('.bird-image');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.add('loaded');
                        imageObserver.unobserve(img);
                    }
                }
            });
        }, {
            rootMargin: '50px 0px'
        });
        
        images.forEach(img => {
            imageObserver.observe(img);
        });
    }
}

// Performance optimizations
function initPerformanceOptimizations() {
    // Debounced scroll handler
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(function() {
            updateScrollProgress();
        }, 16); // ~60fps
    }, { passive: true });
    
    // Optimize animations
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (prefersReducedMotion.matches) {
        // Disable animations for users who prefer reduced motion
        const style = document.createElement('style');
        style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        `;
        document.head.appendChild(style);
    }
}

// Update scroll progress (optional visual enhancement)
function updateScrollProgress() {
    const scrollTop = window.pageYOffset;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = (scrollTop / docHeight) * 100;
    
    // Update any progress indicators if they exist
    const progressBar = document.querySelector('.scroll-progress');
    if (progressBar) {
        progressBar.style.width = scrollPercent + '%';
    }
}

// Language switching enhancement for mobile
function enhanceLanguageSwitching() {
    const langBtn = document.querySelector('.lang-btn');
    if (langBtn) {
        langBtn.addEventListener('click', function() {
            // Add visual feedback
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    }
}

// Initialize language switching enhancement
document.addEventListener('DOMContentLoaded', enhanceLanguageSwitching);

// Swipe gestures for mobile (optional enhancement)
function initSwipeGestures() {
    let startX, startY, distX, distY;
    const threshold = 100; // minimum distance for swipe
    
    document.addEventListener('touchstart', function(e) {
        const touch = e.touches[0];
        startX = touch.clientX;
        startY = touch.clientY;
    }, { passive: true });
    
    document.addEventListener('touchmove', function(e) {
        if (!startX || !startY) return;
        
        const touch = e.touches[0];
        distX = touch.clientX - startX;
        distY = touch.clientY - startY;
    }, { passive: true });
    
    document.addEventListener('touchend', function(e) {
        if (!startX || !startY) return;
        
        // Check if it's a horizontal swipe
        if (Math.abs(distX) > Math.abs(distY) && Math.abs(distX) > threshold) {
            if (distX > 0) {
                // Swipe right - could trigger navigation or other actions
                handleSwipeRight();
            } else {
                // Swipe left - could trigger navigation or other actions
                handleSwipeLeft();
            }
        }
        
        // Reset values
        startX = startY = distX = distY = null;
    }, { passive: true });
}

function handleSwipeRight() {
    // Could implement navigation to previous page or open menu
    const navMenu = document.querySelector('.nav-menu');
    const navToggle = document.querySelector('.nav-toggle');
    
    if (navMenu && !navMenu.classList.contains('active')) {
        navMenu.classList.add('active');
        navToggle.classList.add('active');
    }
}

function handleSwipeLeft() {
    // Could implement navigation to next page or close menu
    const navMenu = document.querySelector('.nav-menu');
    const navToggle = document.querySelector('.nav-toggle');
    
    if (navMenu && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Initialize swipe gestures
document.addEventListener('DOMContentLoaded', initSwipeGestures);

// Viewport height fix for mobile browsers
function fixViewportHeight() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
}

window.addEventListener('resize', fixViewportHeight);
document.addEventListener('DOMContentLoaded', fixViewportHeight);

// Enhanced form interactions for mobile (if forms exist)
function enhanceFormInteractions() {
    const inputs = document.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        // Add focus enhancement
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
        
        // Prevent zoom on input focus for iOS
        if (/iPad|iPhone|iPod/.test(navigator.userAgent)) {
            input.addEventListener('focus', function() {
                this.style.fontSize = '16px';
            });
        }
    });
}

document.addEventListener('DOMContentLoaded', enhanceFormInteractions);