
// 图片加载和懒加载脚本
document.addEventListener('DOMContentLoaded', function() {
    // 图片加载完成处理
    function handleImageLoad(img) {
        img.classList.add('loaded');
        img.style.opacity = '1';
    }
    
    // 图片加载错误处理
    function handleImageError(img) {
        img.src = 'images/ui/placeholders/image-not-found.svg';
        img.alt = 'Image not found';
        img.classList.add('loaded');
    }
    
    // 处理所有图片
    const images = document.querySelectorAll('.responsive-image');
    images.forEach(img => {
        if (img.complete) {
            handleImageLoad(img);
        } else {
            img.addEventListener('load', () => handleImageLoad(img));
            img.addEventListener('error', () => handleImageError(img));
        }
    });
    
    // 懒加载观察器
    if ('IntersectionObserver' in window) {
        const lazyImageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    img.classList.remove('image-placeholder');
                    lazyImageObserver.unobserve(img);
                }
            });
        });
        
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => {
            img.classList.add('image-placeholder');
            lazyImageObserver.observe(img);
        });
    }
});
