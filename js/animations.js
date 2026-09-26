/**
 * animations.js — Velociti Studio
 * GSAP 3.12.5 + ScrollTrigger — hero entrance, scroll reveals, cursor follower, hover lift,
 * scrubbed timeline, word-by-word headings, hero parallax,
 * magnetic buttons, 3D card tilt, clip-path image reveal.
 * All animations are reduced-motion safe and GPU-accelerated.
 */

(function () {
  'use strict';

  // ── 0. Reduced-motion gate ─────────────────────────────────────────────────
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // ── 1. Register ScrollTrigger ─────────────────────────────────────────────
  gsap.registerPlugin(ScrollTrigger);

  const EASE    = 'power3.out';
  const EASE_S  = 'sine.inOut';
  const isMobile = () => window.innerWidth < 768;
  const isTouch  = window.matchMedia('(hover: none)').matches;


  // ══════════════════════════════════════════════════════════════════════════
  // ① WORD-BY-WORD HEADING REVEALS  (pacing bumped: duration 0.55 → 0.82)
  // ══════════════════════════════════════════════════════════════════════════
  function splitAndReveal(headingEl, trigger) {
    if (!headingEl) return;
    const words = headingEl.textContent.trim().split(/\s+/);
    headingEl.innerHTML = words
      .map(w => `<span class="word"><span class="word-inner">${w}</span></span>`)
      .join(' ');

    const inners = headingEl.querySelectorAll('.word-inner');

    gsap.from(inners, {
      opacity   : 0,
      y         : 24,
      rotation  : 4,
      duration  : 0.82,         // was 0.55
      ease      : EASE_S,       // smoother than power3
      stagger   : 0.045,        // was 0.04
      clearProps: 'willChange',
      scrollTrigger: {
        trigger: trigger || headingEl,
        start  : 'top 88%',
        once   : true,
      },
    });
  }

  // Hero H1 word-split (on load, no scroll trigger)
  const heroH1 = document.querySelector('.hero-content h1');
  if (heroH1) {
    const words = heroH1.textContent.trim().split(/\s+/);
    heroH1.innerHTML = words
      .map(w => `<span class="word"><span class="word-inner">${w}</span></span>`)
      .join(' ');

    gsap.from(heroH1.querySelectorAll('.word-inner'), {
      opacity   : 0,
      y         : 26,
      rotation  : 4,
      duration  : 0.82,         // was 0.55
      ease      : EASE_S,
      stagger   : 0.05,
      delay     : 0.15,         // after eyebrow
      clearProps: 'willChange',
    });
  }

  // Section H2s
  ['#vision h2', '#values h2', '#work h2', '#process h2', '#team h2', '#contact h2']
    .forEach(sel => {
      const el = document.querySelector(sel);
      if (el) splitAndReveal(el, el.closest('section'));
    });


  // ══════════════════════════════════════════════════════════════════════════
  // ② HERO ENTRANCE  (duration 0.65 → 0.95, stagger 0.13 → 0.18)
  // ══════════════════════════════════════════════════════════════════════════
  const heroContent = document.querySelector('.hero-content');
  const heroVisual  = document.querySelector('.hero-visual');

  if (heroContent) {
    const items = [
      heroContent.querySelector('.eyebrow'),
      heroContent.querySelector('.hero-copy'),
      heroContent.querySelector('.hero-actions'),
    ].filter(Boolean);

    gsap.from(items, {
      opacity   : 0,
      y         : 32,
      duration  : 0.95,         // was 0.65
      ease      : EASE_S,
      stagger   : 0.18,         // was 0.13
      clearProps: 'willChange',
    });
  }

  if (heroVisual) {
    gsap.from(heroVisual, {
      opacity   : 0,
      y         : 26,
      duration  : 1.0,          // was 0.7
      ease      : EASE_S,
      delay     : 0.42,         // was 0.35
      clearProps: 'willChange',
    });
  }


  // ══════════════════════════════════════════════════════════════════════════
  // ③ HERO PARALLAX — pacing unchanged (scrub-linked, not time-based)
  // ══════════════════════════════════════════════════════════════════════════
  if (heroVisual && heroContent) {
    const heroSection = document.querySelector('#home');
    if (heroSection) {
      gsap.to(heroContent, {
        y: -30, ease: 'none',
        scrollTrigger: { trigger: heroSection, start: 'top top', end: 'bottom top', scrub: true },
      });
      gsap.to(heroVisual, {
        y: -10, ease: 'none',
        scrollTrigger: { trigger: heroSection, start: 'top top', end: 'bottom top', scrub: true },
      });
    }
  }


  // ── Helper: scroll-triggered fade+slide reveal  (duration bumped ~50%) ───
  function revealFrom(selector, triggerEl, vars = {}) {
    const els = gsap.utils.toArray(selector);
    if (!els.length) return;

    const {
      stagger  = 0,
      y        = 26,            // was 22
      duration = 1.05,          // was 0.7
      start    = 'top 85%',
      delay    = 0,
    } = vars;

    gsap.from(els, {
      opacity   : 0,
      y,
      duration,
      ease      : EASE_S,       // smoother
      stagger,
      delay,
      clearProps: 'willChange',
      scrollTrigger: { trigger: triggerEl || els[0], start, once: true },
    });
  }

  // ── Eyebrow reveals ───────────────────────────────────────────────────────
  document.querySelectorAll(
    '#vision .eyebrow, #values .eyebrow, #work .eyebrow,' +
    '#process .eyebrow, #team .eyebrow, #contact .eyebrow'
  ).forEach(el => {
    gsap.from(el, {
      opacity   : 0,
      y         : 18,
      duration  : 0.9,          // was 0.6
      ease      : EASE_S,
      clearProps: 'willChange',
      scrollTrigger: { trigger: el, start: 'top 90%', once: true },
    });
  });

  // ── Vision body ───────────────────────────────────────────────────────────
  const visionSection = document.querySelector('#vision');
  if (visionSection) {
    revealFrom('#vision .vision-body, #vision .lead-text, #vision .vision-stats',
      visionSection, { stagger: 0.12, y: 22 });
  }

  // ── "How We Do Things" bento cards ───────────────────────────────────────
  const bentoGrid = document.querySelector('.bento-values');
  if (bentoGrid) {
    revealFrom('.bento-values .bento-card', bentoGrid, { stagger: 0.1, y: 28 });
  }


  // ══════════════════════════════════════════════════════════════════════════
  // NEW A③ — CLIP-PATH WIPE for project images (left→right)
  // Replaces the old simple fade for cs-visual containers
  // ══════════════════════════════════════════════════════════════════════════
  const workSection = document.querySelector('#work');
  if (workSection) {
    // Use setTimeout(0) so script.js's dynamic card injection is complete
    setTimeout(() => {
      gsap.utils.toArray('#work .cs-visual').forEach(el => {
        gsap.from(el, {
          clipPath  : 'inset(0 100% 0 0)',
          duration  : 1.3,
          ease      : 'power3.inOut',
          clearProps: 'clipPath,willChange',
          scrollTrigger: { trigger: el, start: 'top 82%', once: true },
        });
      });
      revealFrom('#work .case-study .cs-content',
        workSection, { stagger: 0.12, y: 22, start: 'top 80%' });
      ScrollTrigger.refresh();
    }, 0);
  }



  // ══════════════════════════════════════════════════════════════════════════
  // SCRUBBED PROJECT TIMELINE — end value increased for more scroll distance
  // (steps.length * 160 → steps.length * 260)
  // ══════════════════════════════════════════════════════════════════════════
  const processSection = document.querySelector('#process');
  if (processSection) {
    if (isMobile()) {
      revealFrom('.ht-step', processSection, { stagger: 0.12, y: 22, duration: 0.9 });
    } else {
      const steps    = gsap.utils.toArray('.ht-step');
      const nodes    = gsap.utils.toArray('.ht-node');
      const contents = gsap.utils.toArray('.ht-content');
      const htLine   = document.querySelector('.horizontal-timeline');

      // Inject animated fill line
      const fillLine = document.createElement('div');
      fillLine.className = 'ht-fill-line';
      Object.assign(fillLine.style, {
        position      : 'absolute',
        top           : '24px',
        left          : '0',
        height        : '2px',
        width         : '100%',
        background    : 'var(--accent)',
        transformOrigin: 'left center',
        zIndex        : '1',
        pointerEvents : 'none',
      });
      gsap.set(fillLine, { scaleX: 0 });

      if (htLine) {
        htLine.style.position = 'relative';
        htLine.insertBefore(fillLine, htLine.firstChild);
      }

      gsap.set(nodes,    { borderColor: 'var(--border)', color: 'var(--text-secondary)', scale: 1 });
      gsap.set(contents, { opacity: 0, y: 16 });

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger      : processSection,
          start        : 'top top',
          end          : `+=${steps.length * 260}`,   // was 160 — more scroll distance
          pin          : true,
          scrub        : 1.5,                          // slightly more lag = smoother
          anticipatePin: 1,
        },
      });

      tl.to(fillLine, { scaleX: 1, ease: 'none' }, 0);

      const stepDuration = 1 / steps.length;
      steps.forEach((step, i) => {
        const t = i * stepDuration;
        tl.to(nodes[i], {
          borderColor     : 'var(--accent)',
          color           : '#ffffff',
          backgroundColor : 'var(--accent)',
          scale           : 1.15,
          duration        : stepDuration * 0.4,
          ease            : 'power2.out',
        }, t);
        tl.to(nodes[i], {
          scale   : 1,
          duration: stepDuration * 0.3,
          ease    : 'power2.inOut',
        }, t + stepDuration * 0.4);
        tl.to(contents[i], {
          opacity : 1,
          y       : 0,
          duration: stepDuration * 0.5,
          ease    : 'power2.out',
        }, t + stepDuration * 0.15);
      });
    }
  }

  // ── Team cards ────────────────────────────────────────────────────────────
  const teamSection = document.querySelector('#team');
  if (teamSection) {
    revealFrom('.team-card', teamSection, { stagger: 0.1, y: 28, duration: 0.9 });
  }

  // ── CTA / Contact ─────────────────────────────────────────────────────────
  const contactSection = document.querySelector('#contact');
  if (contactSection) {
    revealFrom('#contact .cta-content, #contact .cta-schedule',
      contactSection, { stagger: 0.14, y: 22 });
  }


  // ══════════════════════════════════════════════════════════════════════════
  // NEW A① — MAGNETIC BUTTONS  (snap stays fast per spec — duration 0.25/0.4)
  // ══════════════════════════════════════════════════════════════════════════
  if (!isTouch) {
    const MAGNETIC_SELECTORS = [
      '.button-primary',
      '.nav-estimate',
      '.confirm-booking-btn',
      '.cs-link',
    ];

    document.querySelectorAll(MAGNETIC_SELECTORS.join(', ')).forEach(btn => {
      const RANGE = 55;
      const PULL  = 5;   // max px shift

      btn.addEventListener('mousemove', e => {
        const rect = btn.getBoundingClientRect();
        const cx   = rect.left + rect.width  / 2;
        const cy   = rect.top  + rect.height / 2;
        const dx   = e.clientX - cx;
        const dy   = e.clientY - cy;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < RANGE) {
          // Linear map: cursor at edge = 0 shift, cursor at button center = PULL shift
          const t  = 1 - dist / RANGE;   // 0..1
          const shiftX = (dx / RANGE) * PULL;   // proportional, max ±PULL px
          const shiftY = (dy / RANGE) * PULL;
          gsap.to(btn, {
            x        : shiftX * t,
            y        : shiftY * t,
            duration : 0.25,
            ease     : 'power2.out',
            overwrite: true,
          });
        }
      });

      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.4, ease: 'elastic.out(1, 0.5)', overwrite: true });
      });
    });
  }


  // ══════════════════════════════════════════════════════════════════════════
  // NEW A② — 3D CARD TILT  (desktop only, max ±6°)
  // ══════════════════════════════════════════════════════════════════════════
  if (!isTouch) {
    const TILT_SELECTORS = ['.bento-card', '.team-card', '.case-study'];
    const MAX_TILT = 6;  // degrees

    document.querySelectorAll(TILT_SELECTORS.join(', ')).forEach(card => {
      card.style.transformStyle = 'preserve-3d';
      card.style.willChange     = 'transform';

      card.addEventListener('mousemove', e => {
        const rect  = card.getBoundingClientRect();
        const cx    = rect.left + rect.width  / 2;
        const cy    = rect.top  + rect.height / 2;
        const rx    = ((e.clientY - cy) / (rect.height / 2)) * -MAX_TILT;
        const ry    = ((e.clientX - cx) / (rect.width  / 2)) *  MAX_TILT;

        gsap.to(card, {
          rotateX     : rx,
          rotateY     : ry,
          duration    : 0.3,
          ease        : 'power2.out',
          transformPerspective: 800,
          overwrite   : true,
        });
      });

      card.addEventListener('mouseleave', () => {
        gsap.to(card, {
          rotateX: 0, rotateY: 0,
          duration: 0.55,
          ease    : 'power3.out',
          overwrite: true,
          onComplete() { card.style.willChange = 'auto'; },
        });
      });

      card.addEventListener('mouseenter', () => {
        card.style.willChange = 'transform';
      });
    });
  }


  // ── Hover lift — unchanged (fast, UI feedback) ────────────────────────────
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


  // ── Cursor follower — unchanged ───────────────────────────────────────────
  if (!isTouch) {
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

    let mx = 0, my = 0, cx = 0, cy = 0, live = false;

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
