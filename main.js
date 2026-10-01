const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuBtn && mobileMenu) {
    const setMenuOpen = (open) => {
        mobileMenu.hidden = !open;
        mobileMenuBtn.setAttribute('aria-expanded', String(open));
        mobileMenuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };

    mobileMenuBtn.addEventListener('click', () => {
        setMenuOpen(mobileMenu.hidden);
    });

    // Close mobile menu when clicking a link or pressing Escape
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => setMenuOpen(false));
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !mobileMenu.hidden) {
            setMenuOpen(false);
            mobileMenuBtn.focus();
        }
    });
}

// Typing animation (decorative; the same phrases are shown statically when motion is reduced)
const typingText = document.getElementById('typing-text');

if (typingText) {
    const phrases = JSON.parse(typingText.dataset.phrases);

    if (reduceMotion) {
        typingText.textContent = phrases.join(' · ');
    } else {
        typingText.classList.add('typing-cursor');
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        const typeEffect = () => {
            const currentPhrase = phrases[phraseIndex];

            if (isDeleting) {
                charIndex--;
            } else {
                charIndex++;
            }
            typingText.textContent = currentPhrase.substring(0, charIndex);

            let delay = isDeleting ? 50 : 100;
            if (!isDeleting && charIndex === currentPhrase.length) {
                isDeleting = true;
                delay = 2000;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
            }

            setTimeout(typeEffect, delay);
        };

        typeEffect();
    }
}

// Fade sections in as they scroll into view
const fadeSections = document.querySelectorAll('.section-fade');

if (reduceMotion || !('IntersectionObserver' in window)) {
    fadeSections.forEach(section => section.classList.add('visible'));
} else {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0,
        rootMargin: '0px 0px -100px 0px'
    });

    fadeSections.forEach(section => observer.observe(section));
}
