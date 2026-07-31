/* ==========================================================================
   MushroomAiSnap — 文章页交互
   Loading 遮罩 / 阅读进度 / 顶栏 / 回到顶部 / 分享
   ========================================================================== */
(function () {
    'use strict';

    var doc = document;
    var body = doc.body;

    /* ----------------------------------------------------------------------
       Loading：DOM 就绪后预载 hero，最长 MAX_WAIT 兜底
       ---------------------------------------------------------------------- */
    var MAX_WAIT = 3200;
    var MIN_SHOW = 420;
    var started = Date.now();
    var settled = false;

    function revealPage() {
        if (settled) { return; }
        settled = true;

        var wait = Math.max(0, MIN_SHOW - (Date.now() - started));

        setTimeout(function () {
            var loader = doc.getElementById('m-loader');
            if (loader) {
                loader.classList.add('is-done');
                setTimeout(function () {
                    if (loader.parentNode) { loader.parentNode.removeChild(loader); }
                }, 500);
            }
            body.classList.remove('is-loading');
            body.classList.add('is-ready');
            update();
        }, wait);
    }

    function waitForHero() {
        var hero = doc.querySelector('.hero-image');
        if (!hero) { return revealPage(); }

        var bg = window.getComputedStyle(hero).backgroundImage || '';
        var match = bg.match(/url\((['"]?)(.*?)\1\)/);

        if (!match || !match[2]) { return revealPage(); }

        var img = new Image();
        img.onload = revealPage;
        img.onerror = revealPage;
        img.src = match[2];

        if (img.complete) { revealPage(); }
    }

    setTimeout(revealPage, MAX_WAIT);

    if (doc.readyState === 'loading') {
        doc.addEventListener('DOMContentLoaded', waitForHero, { once: true });
    } else {
        waitForHero();
    }

    /* ----------------------------------------------------------------------
       滚动：阅读进度 / 顶栏 / 回到顶部
       ---------------------------------------------------------------------- */
    var fill = doc.querySelector('.m-progress__fill');
    var topbar = doc.querySelector('.m-topbar');
    var toTop = doc.querySelector('.m-totop');
    var ticking = false;

    function update() {
        var scrolled = window.pageYOffset || doc.documentElement.scrollTop;
        var max = doc.documentElement.scrollHeight - window.innerHeight;

        if (fill) {
            var pct = max > 0 ? (scrolled / max) * 100 : 0;
            fill.style.width = Math.min(Math.max(pct, 0), 100) + '%';
        }

        var passedHero = scrolled > 260;
        if (topbar) { topbar.classList.toggle('is-visible', passedHero); }
        if (toTop) { toTop.classList.toggle('is-visible', scrolled > 640); }

        ticking = false;
    }

    function onScroll() {
        if (!ticking) {
            ticking = true;
            window.requestAnimationFrame(update);
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });

    if (toTop) {
        toTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    var share = doc.querySelector('.m-topbar__share');
    if (share) {
        share.addEventListener('click', function () {
            var data = {
                title: doc.title.replace(/\s*-\s*MushroomAiSnap\s*$/, ''),
                url: window.location.href
            };

            if (navigator.share) {
                navigator.share(data).catch(function () { /* 用户取消 */ });
            } else if (navigator.clipboard) {
                navigator.clipboard.writeText(data.url).then(function () {
                    var prev = share.textContent;
                    share.textContent = '✓';
                    setTimeout(function () { share.textContent = prev; }, 1600);
                }).catch(function () { /* 权限拒绝 */ });
            }
        });
    }
})();
