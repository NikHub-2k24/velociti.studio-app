/**
 * animations.js — Velociti Studio
 * GSAP + ScrollTrigger entrance, scroll-reveal, cursor follower, and hover micro-interactions.
 * Tasteful, GPU-accelerated, and reduced-motion safe.
 */

(function () {
  'use strict';

  // ── 0. Reduced-motion gate ─────────────────────────────────────────────────
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion) {
    // Make everything immediately visible, no animations
    document.documentElement.style.setProperty('--anim-opacity', '1');
    return;
  }

  // ── 1. Register ScrollTrigger ─────────────────────────────────────────────
  gsap.registerPlugin(ScrollTrigger);

  // Shared ease
  const EASE_OUT = 'power2.out';
  const EASE_SMOOTH = 'power3.out';

  // ── 2. Hero entrance (staggered, runs once on load) ───────────────────────
  const heroEl = document.querySelector('.hero-content');
  if (heroEl) {
    const heroItems = [
      heroEl.querySelector('.eyebrow'),
      heroEl.querySelector('h1'),
      heroEl.querySelector('.hero-copy'),
      heroEl.querySelector('.hero-actions'),
    ].filter(Boolean);

    const codePanel = document.querySelector('.hero-visual');

    // Set initial state — hidden & shifted down
    gsap.set(heroItems, { opacity: 0, y: 28, willChange: 'transform, opacity' });
    if (codePanel) gsap.set(codePanel, { opacity: 0, y: 24, willChange: 'transform, opacity' });

    const tl = gsap.timeline({
      defaults: { ease: EASE_SMOOTH, duration: 0.65 },
      onComplete() {
        // Clean up will-change after animation
        gsap.set([...heroItems, codePanel].filter(Boolean), { willChange: 'auto' });
      }
    });

    tl.to(heroItems, {
      opacity: 1,
      y: 0,
      stagger: 0.13,
    });

    if (codePanel) {
      tl.to(codePanel, { opacity: 1, y: 0, duration: 0.6 }, '-=0.4');
    }
  }

  // ── 3. Scroll-triggered section reveals ───────────────────────────────────

  // Helper: fade + slide a set of elements in on scroll
  function revealOnScroll(selector, options = {}) {
    const els = gsap.utils.toArray(selector);
    if (!els.length) return;

    const {
      stagger = 0,
      y = 22,
      duration = 0.7,
      start = 'top 85%',
    } = options;

    gsap.set(els, { opacity: 0, y, willChange: 'transform, opacity' });

    ScrollTrigger.batch(els, {
      onEnter(batch) {
        gsap.to(batch, {
          opacity: 1,
          y: 0,
          stagger,
          duration,
          ease: EASE_SMOOTH,
          onComplete() {
            gsap.set(batch, { willChange: 'auto' });
          }
        });
      },
      once: true,
      start,
    });
  }

  // Section headings (eyebrow + h2 pairs)
  revealOnScroll('.section-header-left, .section-header-center', { y: 20, duration: 0.7 });

  // Vision section body text
  revealOnScroll('#vision .vision-body, #vision .vision-stats', { y: 18, duration: 0.65, stagger: 0.1 });

  // "How We Do Things" — 6 bento cards staggered
  revealOnScroll('.bento-values .bento-card', { stagger: 0.09, y: 24, duration: 0.65 });

  // Featured project slides / case study wrappers
  revealOnScroll('.case-study-list .cs-visual, .case-study-list .cs-info', { stagger: 0.1, y: 20 });

  // Project timeline nodes + content
  revealOnScroll('.ht-step', { stagger: 0.1, y: 20, duration: 0.6 });

  // Team cards
  revealOnScroll('.team-grid .team-card', { stagger: 0.08, y: 24, duration: 0.6 });

  // CTA section
  revealOnScroll('#contact .cta-content, #contact .cta-schedule', { stagger: 0.12, y: 18 });

  // ── 4. Hover micro-interactions (GSAP, GPU-accelerated) ───────────────────
  function addHoverLift(selector, liftY = -5) {
    document.querySelectorAll(selector).forEach(el => {
      el.addEventListener('mouseenter', () => {
        gsap.to(el, {
          y: liftY,
          duration: 0.25,
          ease: EASE_OUT,
          boxShadow: '0 16px 40px rgba(255, 107, 53, 0.18)',
        });
      });
      el.addEventListener('mouseleave', () => {
        gsap.to(el, {
          y: 0,
          duration: 0.3,
          ease: EASE_OUT,
          boxShadow: '0 0px 0px rgba(255,107,53,0)',
        });
      });
    });
  }

  addHoverLift('.bento-card', -5);
  addHoverLift('.team-card', -5);
  addHoverLift('.case-study', -4);

  // ── 5. Cursor follower (desktop only) ─────────────────────────────────────
  const isTouchDevice = window.matchMedia('(hover: none)').matches;

  if (!isTouchDevice) {
    // Create the follower element
    const follower = document.createElement('div');
    follower.id = 'cursor-follower';
    Object.assign(follower.style, {
      position: 'fixed',
      top: '0',
      left: '0',
      width: '10px',
      height: '10px',
      borderRadius: '50%',
      background: 'rgba(255, 107, 53, 0.55)',
      boxShadow: '0 0 10px 4px rgba(255, 107, 53, 0.25)',
      pointerEvents: 'none',
      zIndex: '99999',
      transform: 'translate(-50%, -50%)',
      willChange: 'transform',
      transition: 'width 0.2s, height 0.2s, opacity 0.2s, background 0.2s',
      opacity: '0',
    });
    document.body.appendChild(follower);

    // Lerp target
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let curX = mouseX;
    let curY = mouseY;
    const LERP = 0.12; // lag factor (lower = more lag)

    // Fade in follower on first move
    let started = false;
    window.addEventListener('mousemove', e => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (!started) {
        follower.style.opacity = '1';
        started = true;
      }
    });

    // RAF loop for smooth lerp
    function tick() {
      curX += (mouseX - curX) * LERP;
      curY += (mouseY - curY) * LERP;
      follower.style.transform = `translate(${curX - 5}px, ${curY - 5}px)`;
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);

    // Scale up on interactive elements
    const interactiveSelector = 'a, button, .bento-card, .team-card, .case-study, .time-btn, .button';
    document.querySelectorAll(interactiveSelector).forEach(el => {
      el.addEventListener('mouseenter', () => {
        follower.style.width = '24px';
        follower.style.height = '24px';
        follower.style.opacity = '0.75';
        follower.style.background = 'rgba(255, 107, 53, 0.4)';
      });
      el.addEventListener('mouseleave', () => {
        follower.style.width = '10px';
        follower.style.height = '10px';
        follower.style.opacity = '1';
        follower.style.background = 'rgba(255, 107, 53, 0.55)';
      });
    });

    // Hide when leaving window
    document.addEventListener('mouseleave', () => { follower.style.opacity = '0'; });
    document.addEventListener('mouseenter', () => { if (started) follower.style.opacity = '1'; });
  }

})();
