/**
 * 智能下载系统 - 根据设备类型跳转到对应应用商店
 * 修复版本 - 解决iPhone跳转问题
 */

// 应用商店链接配置
const APP_STORE_LINKS = {
    bird: {
        ios: 'https://apps.apple.com/us/app/birdaisnap-bird-identify/id6747970025',
        android: 'https://play.google.com/store/apps/details?id=com.bird.ai.snap'
    },
    rock: {
        ios: 'https://apps.apple.com/us/app/rockaisnap-rock-identify/id6751223713',
        android: 'https://play.google.com/store/apps/details?id=com.rock.ai.snap'
    },
    mushroom: {
        ios: 'https://apps.apple.com/us/app/mushroom-identify/id123456789', // 待更新实际链接
        android: 'https://play.google.com/store/apps/details?id=com.mushroom.ai.snap'
    }
};

/**
 * 检测设备类型
 * @returns {string} 'ios' | 'android' | 'other'
 */
function detectDevice() {
    const userAgent = navigator.userAgent.toLowerCase();
    
    console.log('User Agent:', userAgent); // 调试信息
    
    // 检测iOS设备 - 更精确的检测
    if (/iphone|ipad|ipod/.test(userAgent)) {
        console.log('Detected iOS device');
        return 'ios';
    }
    
    // 检测Android设备
    if (/android/.test(userAgent)) {
        console.log('Detected Android device');
        return 'android';
    }
    
    // 检测Mac设备（可能需要iOS App Store）
    if (/macintosh|mac os x/.test(userAgent)) {
        console.log('Detected Mac device');
        return 'ios';
    }
    
    // 默认返回Android（大多数其他设备）
    console.log('Detected other device, defaulting to Android');
    return 'android';
}

/**
 * 智能下载函数 - 修复版本
 * @param {string} appType - 应用类型 ('bird', 'rock', 'mushroom')
 */
function smartDownload(appType) {
    const device = detectDevice();
    const links = APP_STORE_LINKS[appType];
    
    console.log('Smart download called:', { appType, device, links });
    
    if (!links) {
        console.error(`Unknown app type: ${appType}`);
        return;
    }
    
    const downloadUrl = links[device] || links.android;
    console.log('Download URL:', downloadUrl);
    
    // 对于iOS设备，使用多种方法尝试跳转
    if (device === 'ios') {
        // 方法1: 直接设置window.location (iOS Safari更兼容)
        try {
            window.location.href = downloadUrl;
            return;
        } catch (e) {
            console.log('Method 1 failed, trying method 2');
        }
        
        // 方法2: 使用window.open
        try {
            const newWindow = window.open(downloadUrl, '_blank');
            if (!newWindow) {
                // 如果被阻止，尝试方法3
                throw new Error('Popup blocked');
            }
            return;
        } catch (e) {
            console.log('Method 2 failed, trying method 3');
        }
        
        // 方法3: 创建临时链接并点击
        try {
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            return;
        } catch (e) {
            console.log('Method 3 failed, trying method 4');
        }
        
        // 方法4: 最后的备用方案
        alert(`Please visit: ${downloadUrl}`);
    } else {
        // Android设备使用原来的方法
        window.open(downloadUrl, '_blank');
    }
    
    // 可选：记录下载事件（用于分析）
    if (typeof gtag !== 'undefined') {
        gtag('event', 'download_click', {
            'app_name': appType,
            'platform': device,
            'url': downloadUrl
        });
    }
}

/**
 * 获取当前设备对应的下载URL
 * @param {string} appType - 应用类型
 * @returns {string} 下载URL
 */
function getDownloadUrl(appType) {
    const device = detectDevice();
    const links = APP_STORE_LINKS[appType];
    
    if (!links) {
        return '#';
    }
    
    return links[device] || links.android;
}

/**
 * 更新下载按钮的链接和文本 - 修复版本
 */
function updateDownloadButtons() {
    const device = detectDevice();
    const isIOS = device === 'ios';
    
    console.log('Updating download buttons for device:', device);
    
    // 查找所有下载按钮并更新
    document.querySelectorAll('[data-app-type]').forEach(button => {
        const appType = button.getAttribute('data-app-type');
        const links = APP_STORE_LINKS[appType];
        
        if (links) {
            // 更新链接
            const targetUrl = links[device] || links.android;
            button.href = targetUrl;
            
            console.log(`Updated button for ${appType}:`, targetUrl);
            
            // 移除原有的点击事件监听器
            button.removeEventListener('click', button._smartDownloadHandler);
            
            // 添加新的点击事件处理器
            button._smartDownloadHandler = function(e) {
                e.preventDefault();
                console.log('Button clicked for:', appType);
                smartDownload(appType);
                return false;
            };
            
            button.addEventListener('click', button._smartDownloadHandler);
            
            // 更新按钮文本（可选）
            if (isIOS && button.textContent && button.textContent.includes('Download')) {
                button.innerHTML = button.innerHTML.replace('Download Now', 'Download on App Store');
            }
        }
    });
    
    // 特殊处理：直接为iOS按钮添加正确的href
    document.querySelectorAll('.ios-download').forEach(button => {
        const appType = button.getAttribute('data-app-type');
        if (appType && APP_STORE_LINKS[appType]) {
            button.href = APP_STORE_LINKS[appType].ios;
            console.log(`Set iOS button href for ${appType}:`, button.href);
        }
    });
    
    // 特殊处理：直接为Android按钮添加正确的href
    document.querySelectorAll('.android-download').forEach(button => {
        const appType = button.getAttribute('data-app-type');
        if (appType && APP_STORE_LINKS[appType]) {
            button.href = APP_STORE_LINKS[appType].android;
            console.log(`Set Android button href for ${appType}:`, button.href);
        }
    });
}

/**
 * 创建双平台下载按钮组
 * @param {string} appType - 应用类型
 * @returns {HTMLElement} 按钮组元素
 */
function createDualDownloadButtons(appType) {
    const links = APP_STORE_LINKS[appType];
    if (!links) return null;
    
    const buttonGroup = document.createElement('div');
    buttonGroup.className = 'download-buttons-group';
    
    // iOS按钮
    const iosButton = document.createElement('a');
    iosButton.href = links.ios;
    iosButton.className = 'btn btn-download ios-download';
    iosButton.target = '_blank';
    iosButton.innerHTML = `
        <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download on App Store" style="height: 40px;">
    `;
    
    // Android按钮
    const androidButton = document.createElement('a');
    androidButton.href = links.android;
    androidButton.className = 'btn btn-download android-download';
    androidButton.target = '_blank';
    androidButton.innerHTML = `
        <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play" style="height: 40px;">
    `;
    
    buttonGroup.appendChild(iosButton);
    buttonGroup.appendChild(androidButton);
    
    return buttonGroup;
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('Smart download system initializing...');
    
    // 延迟执行以确保所有元素都已加载
    setTimeout(() => {
        updateDownloadButtons();
        
        // 如果需要显示当前设备类型（调试用）
        const device = detectDevice();
        console.log('Detected device:', device);
        
        // 为所有现有的下载按钮添加点击处理
        document.querySelectorAll('a[href*="apps.apple.com"], a[href*="play.google.com"]').forEach(link => {
            if (!link.hasAttribute('data-app-type')) {
                // 尝试从href推断应用类型
                if (link.href.includes('bird')) {
                    link.setAttribute('data-app-type', 'bird');
                } else if (link.href.includes('rock')) {
                    link.setAttribute('data-app-type', 'rock');
                }
            }
        });
        
        // 重新更新按钮
        updateDownloadButtons();
    }, 100);
});

// 导出函数供全局使用
window.smartDownload = smartDownload;
window.getDownloadUrl = getDownloadUrl;
window.createDualDownloadButtons = createDualDownloadButtons;
window.detectDevice = detectDevice; // 导出用于调试
