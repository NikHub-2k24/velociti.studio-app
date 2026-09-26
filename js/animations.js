/**
 * animations.js — Velociti Studio
 * GSAP 3.12.5 + ScrollTrigger — hero entrance, scroll reveals, cursor follower, hover lift.
 * All animations are reduced-motion safe and GPU-accelerated.
 */

(function () {
  'use strict';

  // ── 0. Reduced-motion gate ─────────────────────────────────────────────────
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // ── 1. Register ScrollTrigger (after GSAP is loaded) ─────────────────────
  gsap.registerPlugin(ScrollTrigger);

  const EASE = 'power3.out';

  // ── 2. Hero entrance (staggered, once on load) ────────────────────────────
  const heroContent = document.querySelector('.hero-content');
  const heroVisual  = document.querySelector('.hero-visual');

  if (heroContent) {
    const items = [
      heroContent.querySelector('.eyebrow'),
      heroContent.querySelector('h1'),
      heroContent.querySelector('.hero-copy'),
      heroContent.querySelector('.hero-actions'),
    ].filter(Boolean);

    gsap.from(items, {
      opacity: 0,
      y: 28,
      duration: 0.65,
      ease: EASE,
      stagger: 0.13,
      clearProps: 'willChange',
    });
  }

  if (heroVisual) {
    gsap.from(heroVisual, {
      opacity: 0,
      y: 22,
      duration: 0.7,
      ease: EASE,
      delay: 0.35,
      clearProps: 'willChange',
    });
  }

  // ── 3. Helper: scroll-triggered reveal for a selector ─────────────────────
  function revealFrom(selector, triggerEl, vars = {}) {
    const els = gsap.utils.toArray(selector);
    if (!els.length) return;

    const {
      stagger = 0,
      y       = 22,
      duration= 0.7,
      start   = 'top 85%',
      delay   = 0,
    } = vars;

    gsap.from(els, {
      opacity : 0,
      y,
      duration,
      ease    : EASE,
      stagger,
      delay,
      clearProps: 'willChange',
      scrollTrigger: {
        trigger : triggerEl || els[0],
        start,
        once    : true,
      },
    });
  }

  // ── 4. Section heading reveals ─────────────────────────────────────────────
  document.querySelectorAll(
    '#vision   .section-header-left, #vision   .section-header-center,' +
    '#values   .section-header-left, #values   .section-header-center,' +
    '#work     .section-header-left, #work     .section-header-center,' +
    '#process  .section-header-left, #process  .section-header-center,' +
    '#team     .section-header-left, #team     .section-header-center,' +
    '#contact  .section-header-left, #contact  .section-header-center'
  ).forEach(header => {
    gsap.from(header, {
      opacity: 0,
      y: 20,
      duration: 0.7,
      ease: EASE,
      clearProps: 'willChange',
      scrollTrigger: { trigger: header, start: 'top 88%', once: true },
    });
  });

  // ── 5. Vision section body ─────────────────────────────────────────────────
  const visionSection = document.querySelector('#vision');
  if (visionSection) {
    revealFrom(
      '#vision .vision-body, #vision .lead-text, #vision .vision-stats',
      visionSection, { stagger: 0.1, y: 18 }
    );
  }

  // ── 6. "How We Do Things" bento cards (staggered) ─────────────────────────
  const bentoGrid = document.querySelector('.bento-values');
  if (bentoGrid) {
    revealFrom('.bento-values .bento-card', bentoGrid, { stagger: 0.09, y: 24 });
  }

  // ── 7. Featured Projects case-study blocks ────────────────────────────────
  const workSection = document.querySelector('#work');
  if (workSection) {
    revealFrom(
      '#work .cs-visual, #work .cs-info',
      workSection, { stagger: 0.1, y: 20, start: 'top 80%' }
    );
  }

  // ── 8. Project Timeline steps ─────────────────────────────────────────────
  const processSection = document.querySelector('#process');
  if (processSection) {
    revealFrom('.ht-step', processSection, { stagger: 0.1, y: 20, duration: 0.6 });
  }

  // ── 9. Team cards ─────────────────────────────────────────────────────────
  const teamSection = document.querySelector('#team');
  if (teamSection) {
    revealFrom('.team-card', teamSection, { stagger: 0.08, y: 24, duration: 0.6 });
  }

  // ── 10. CTA / Contact section ─────────────────────────────────────────────
  const contactSection = document.querySelector('#contact');
  if (contactSection) {
    revealFrom(
      '#contact .cta-content, #contact .cta-schedule',
      contactSection, { stagger: 0.12, y: 18 }
    );
  }

  // ── 11. Hover micro-interactions (lift + shadow) ───────────────────────────
  function addHoverLift(selector, liftY) {
    document.querySelectorAll(selector).forEach(el => {
      el.addEventListener('mouseenter', () =>
        gsap.to(el, { y: liftY, duration: 0.25, ease: 'power2.out',
          boxShadow: '0 16px 40px rgba(255,107,53,0.18)' })
      );
      el.addEventListener('mouseleave', () =>
        gsap.to(el, { y: 0, duration: 0.3, ease: 'power2.out',
          boxShadow: '0 0px 0px rgba(255,107,53,0)' })
      );
    });
  }

  addHoverLift('.bento-card', -5);
  addHoverLift('.team-card',  -5);
  addHoverLift('.case-study', -4);

  // ── 12. Cursor follower (desktop / hover-capable only) ────────────────────
  if (!window.matchMedia('(hover: none)').matches) {
    const dot = document.createElement('div');
    dot.id = 'cursor-follower';
    Object.assign(dot.style, {
      position      : 'fixed',
      top           : '0',
      left          : '0',
      width         : '10px',
      height        : '10px',
      borderRadius  : '50%',
      background    : 'rgba(255,107,53,0.55)',
      boxShadow     : '0 0 10px 4px rgba(255,107,53,0.22)',
      pointerEvents : 'none',
      zIndex        : '99999',
      opacity       : '0',
      willChange    : 'transform',
    });
    document.body.appendChild(dot);

    let mx = 0, my = 0, cx = 0, cy = 0;
    let live = false;

    window.addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
      if (!live) { dot.style.opacity = '1'; live = true; }
    });

    (function lerp() {
      cx += (mx - cx) * 0.12;
      cy += (my - cy) * 0.12;
      dot.style.transform = `translate(${cx - 5}px,${cy - 5}px)`;
      requestAnimationFrame(lerp);
    })();

    const BIG   = { width: '24px', height: '24px', opacity: '0.75' };
    const SMALL = { width: '10px', height: '10px', opacity: '1'    };

    document.querySelectorAll('a, button, .bento-card, .team-card, .case-study, .button, .time-btn').forEach(el => {
      el.addEventListener('mouseenter', () => Object.assign(dot.style, BIG));
      el.addEventListener('mouseleave', () => Object.assign(dot.style, SMALL));
    });

    document.addEventListener('mouseleave', () => { dot.style.opacity = '0'; });
    document.addEventListener('mouseenter', () => { if (live) dot.style.opacity = '1'; });
  }

})();
