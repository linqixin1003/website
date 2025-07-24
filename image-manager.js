/**
 * 图片管理工具类
 * 提供图片加载、优化和多语言支持功能
 */

class ImageManager {
    constructor() {
        this.baseImagePath = 'images/';
        this.supportedFormats = ['webp', 'jpg', 'jpeg', 'png'];
        this.currentLanguage = this.detectLanguage();
        this.imageCache = new Map();
        this.lazyLoadObserver = null;
        this.initLazyLoading();
    }

    /**
     * 检测当前语言
     */
    detectLanguage() {
        // 从URL检测语言
        const pathLang = window.location.pathname.match(/^\/([a-z]{2})\//);
        if (pathLang) return pathLang[1];
        
        // 从localStorage检测
        const savedLang = localStorage.getItem('preferred-language');
        if (savedLang) return savedLang;
        
        // 默认英语
        return 'en';
    }

    /**
     * 获取本地化图片路径
     */
    getLocalizedImagePath(imagePath, language = null) {
        const lang = language || this.currentLanguage;
        
        // 如果是英语或者不需要本地化，返回原路径
        if (lang === 'en') {
            return `${this.baseImagePath}${imagePath}`;
        }
        
        // 尝试本地化路径
        const localizedPath = `${this.baseImagePath}localized/${lang}/${imagePath}`;
        const defaultPath = `${this.baseImagePath}${imagePath}`;
        
        return this.checkImageExists(localizedPath).then(exists => 
            exists ? localizedPath : defaultPath
        );
    }

    /**
     * 检查图片是否存在
     */
    async checkImageExists(imagePath) {
        if (this.imageCache.has(imagePath)) {
            return this.imageCache.get(imagePath);
        }

        try {
            const response = await fetch(imagePath, { method: 'HEAD' });
            const exists = response.ok;
            this.imageCache.set(imagePath, exists);
            return exists;
        } catch (error) {
            this.imageCache.set(imagePath, false);
            return false;
        }
    }

    /**
     * 获取响应式图片源集
     */
    getResponsiveSrcSet(imagePath, sizes = ['small', 'medium', 'large']) {
        const srcSet = [];
        const filename = imagePath.split('/').pop().split('.')[0];
        const extension = imagePath.split('.').pop();

        sizes.forEach(size => {
            const width = this.getSizeWidth(size);
            srcSet.push(`${this.baseImagePath}thumbnails/${size}/${filename}.${extension} ${width}w`);
        });

        return srcSet.join(', ');
    }

    /**
     * 获取尺寸对应的宽度
     */
    getSizeWidth(size) {
        const widths = {
            'small': 300,
            'medium': 600,
            'large': 1200
        };
        return widths[size] || 300;
    }

    /**
     * 创建响应式图片元素
     */
    createResponsiveImage(imagePath, alt, options = {}) {
        const {
            sizes = '(max-width: 768px) 300px, (max-width: 1200px) 600px, 1200px',
            className = 'responsive-image',
            loading = 'lazy',
            language = null
        } = options;

        const img = document.createElement('img');
        
        // 设置基本属性
        img.alt = alt;
        img.className = className;
        img.loading = loading;

        // 获取本地化路径
        this.getLocalizedImagePath(imagePath, language).then(localizedPath => {
            img.src = localizedPath;
            img.srcset = this.getResponsiveSrcSet(imagePath);
            img.sizes = sizes;
        });

        return img;
    }

    /**
     * 创建图片容器
     */
    createImageContainer(imagePath, alt, caption = null, options = {}) {
        const container = document.createElement('figure');
        container.className = 'image-container';

        const img = this.createResponsiveImage(imagePath, alt, options);
        container.appendChild(img);

        if (caption) {
            const figcaption = document.createElement('figcaption');
            figcaption.textContent = caption;
            container.appendChild(figcaption);
        }

        return container;
    }

    /**
     * 初始化懒加载
     */
    initLazyLoading() {
        if ('IntersectionObserver' in window) {
            this.lazyLoadObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        this.loadImage(img);
                        this.lazyLoadObserver.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });
        }
    }

    /**
     * 添加懒加载图片
     */
    addLazyImage(img) {
        if (this.lazyLoadObserver) {
            img.classList.add('lazy-loading');
            this.lazyLoadObserver.observe(img);
        } else {
            // 降级处理
            this.loadImage(img);
        }
    }

    /**
     * 加载图片
     */
    loadImage(img) {
        const src = img.dataset.src || img.src;
        const srcset = img.dataset.srcset;

        if (src) {
            img.src = src;
            img.removeAttribute('data-src');
        }

        if (srcset) {
            img.srcset = srcset;
            img.removeAttribute('data-srcset');
        }

        img.classList.remove('lazy-loading');
        img.classList.add('loaded');
    }

    /**
     * 预加载关键图片
     */
    preloadImages(imagePaths) {
        imagePaths.forEach(path => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = `${this.baseImagePath}${path}`;
            document.head.appendChild(link);
        });
    }

    /**
     * 获取文章相关图片
     */
    getArticleImages(category, articleId) {
        const articleImagePath = `articles/${category}/${articleId}/`;
        return this.getImagesInDirectory(articleImagePath);
    }

    /**
     * 获取目录中的图片列表
     */
    async getImagesInDirectory(directoryPath) {
        // 这里需要服务器端支持或者预定义图片列表
        // 简化实现，返回常见的图片文件名
        const commonImages = [
            'hero.jpg',
            'thumbnail.jpg',
            'diagram.png',
            'example-1.jpg',
            'example-2.jpg'
        ];

        const existingImages = [];
        for (const image of commonImages) {
            const fullPath = `${directoryPath}${image}`;
            if (await this.checkImageExists(`${this.baseImagePath}${fullPath}`)) {
                existingImages.push(fullPath);
            }
        }

        return existingImages;
    }

    /**
     * 图片错误处理
     */
    handleImageError(img, fallbackPath = null) {
        img.onerror = () => {
            if (fallbackPath) {
                img.src = `${this.baseImagePath}${fallbackPath}`;
            } else {
                // 使用默认占位符
                img.src = `${this.baseImagePath}ui/placeholders/image-not-found.png`;
            }
            img.classList.add('image-error');
        };
    }

    /**
     * 生成图片画廊
     */
    createGallery(images, containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const gallery = document.createElement('div');
        gallery.className = 'image-gallery';

        images.forEach((imageData, index) => {
            const item = document.createElement('div');
            item.className = 'gallery-item';
            
            const img = this.createResponsiveImage(
                imageData.path, 
                imageData.alt, 
                { className: 'gallery-image' }
            );
            
            // 添加点击事件打开大图
            img.addEventListener('click', () => {
                this.openLightbox(images, index);
            });

            item.appendChild(img);
            gallery.appendChild(item);
        });

        container.appendChild(gallery);
    }

    /**
     * 打开灯箱效果
     */
    openLightbox(images, currentIndex) {
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox';
        lightbox.innerHTML = `
            <div class="lightbox-content">
                <span class="lightbox-close">&times;</span>
                <img class="lightbox-image" src="" alt="">
                <div class="lightbox-nav">
                    <button class="lightbox-prev">&#10094;</button>
                    <button class="lightbox-next">&#10095;</button>
                </div>
                <div class="lightbox-caption"></div>
            </div>
        `;

        document.body.appendChild(lightbox);
        this.showLightboxImage(lightbox, images, currentIndex);

        // 事件监听
        lightbox.querySelector('.lightbox-close').onclick = () => {
            document.body.removeChild(lightbox);
        };

        lightbox.onclick = (e) => {
            if (e.target === lightbox) {
                document.body.removeChild(lightbox);
            }
        };
    }

    /**
     * 显示灯箱图片
     */
    showLightboxImage(lightbox, images, index) {
        const img = lightbox.querySelector('.lightbox-image');
        const caption = lightbox.querySelector('.lightbox-caption');
        
        img.src = `${this.baseImagePath}${images[index].path}`;
        img.alt = images[index].alt;
        caption.textContent = images[index].caption || images[index].alt;
    }
}

// 全局实例
const imageManager = new ImageManager();

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    // 处理现有的懒加载图片
    const lazyImages = document.querySelectorAll('img[data-src]');
    lazyImages.forEach(img => imageManager.addLazyImage(img));

    // 处理图片错误
    const allImages = document.querySelectorAll('img');
    allImages.forEach(img => imageManager.handleImageError(img));
});

// 导出供其他脚本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ImageManager;
} else {
    window.ImageManager = ImageManager;
    window.imageManager = imageManager;
}