/**
 * animations.js — Velociti Studio
 * GSAP 3.12.5 + ScrollTrigger — hero entrance, scroll reveals, cursor follower, hover lift,
 * scrubbed timeline, word-by-word headings, hero parallax.
 * All animations are reduced-motion safe and GPU-accelerated.
 */

(function () {
  'use strict';

  // ── 0. Reduced-motion gate ─────────────────────────────────────────────────
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // ── 1. Register ScrollTrigger ─────────────────────────────────────────────
  gsap.registerPlugin(ScrollTrigger);

  const EASE = 'power3.out';
  const isMobile = () => window.innerWidth < 768;

  // ══════════════════════════════════════════════════════════════════════════
  // NEW ① — WORD-BY-WORD HEADING REVEALS
  // Wraps each word in a <span class="word">, animates them in on scroll.
  // ══════════════════════════════════════════════════════════════════════════
  function splitAndReveal(headingEl, trigger) {
    if (!headingEl) return;

    // Split into word spans preserving original text
    const words = headingEl.textContent.trim().split(/\s+/);
    headingEl.innerHTML = words
      .map(w => `<span class="word" style="display:inline-block;overflow:hidden;vertical-align:bottom">` +
                `<span class="word-inner" style="display:inline-block">${w}</span></span>`)
      .join(' ');

    const inners = headingEl.querySelectorAll('.word-inner');

    gsap.from(inners, {
      opacity   : 0,
      y         : 20,
      rotation  : 3,
      duration  : 0.55,
      ease      : EASE,
      stagger   : 0.04,
      clearProps: 'willChange',
      scrollTrigger: {
        trigger: trigger || headingEl,
        start  : 'top 88%',
        once   : true,
      },
    });
  }

  // Hero H1 — runs immediately (no scroll trigger needed, fires on load)
  const heroH1 = document.querySelector('.hero-content h1');
  if (heroH1) {
    const words = heroH1.textContent.trim().split(/\s+/);
    heroH1.innerHTML = words
      .map(w => `<span class="word" style="display:inline-block;overflow:hidden;vertical-align:bottom">` +
                `<span class="word-inner" style="display:inline-block">${w}</span></span>`)
      .join(' ');

    gsap.from(heroH1.querySelectorAll('.word-inner'), {
      opacity : 0,
      y       : 22,
      rotation: 3,
      duration: 0.55,
      ease    : EASE,
      stagger : 0.04,
      delay   : 0.12,   // fires just after the eyebrow fades in
      clearProps: 'willChange',
    });
  }

  // Section H2s — scroll-triggered word reveals
  [
    '#vision h2',
    '#values h2',
    '#work h2',
    '#process h2',
    '#team h2',
    '#contact h2',
  ].forEach(sel => {
    const el = document.querySelector(sel);
    if (el) splitAndReveal(el, el.closest('section'));
  });


  // ══════════════════════════════════════════════════════════════════════════
  // ── 2. Hero entrance (staggered, once on load) — unchanged ───────────────
  // ══════════════════════════════════════════════════════════════════════════
  const heroContent = document.querySelector('.hero-content');
  const heroVisual  = document.querySelector('.hero-visual');

  if (heroContent) {
    const items = [
      heroContent.querySelector('.eyebrow'),
      // h1 is handled by word-split above
      heroContent.querySelector('.hero-copy'),
      heroContent.querySelector('.hero-actions'),
    ].filter(Boolean);

    gsap.from(items, {
      opacity: 0,
      y      : 28,
      duration: 0.65,
      ease   : EASE,
      stagger: 0.13,
      clearProps: 'willChange',
    });
  }

  if (heroVisual) {
    gsap.from(heroVisual, {
      opacity : 0,
      y       : 22,
      duration: 0.7,
      ease    : EASE,
      delay   : 0.35,
      clearProps: 'willChange',
    });
  }


  // ══════════════════════════════════════════════════════════════════════════
  // NEW ③ — HERO PARALLAX (code panel moves slower than text on scroll)
  // ══════════════════════════════════════════════════════════════════════════
  if (heroVisual && heroContent) {
    const heroSection = document.querySelector('#home');
    if (heroSection) {
      // Text drifts upward slightly faster, panel drifts slower
      gsap.to(heroContent, {
        y: -30,
        ease: 'none',
        scrollTrigger: {
          trigger: heroSection,
          start  : 'top top',
          end    : 'bottom top',
          scrub  : true,
        },
      });
      gsap.to(heroVisual, {
        y: -10,   // 10-15% of the text movement → visible depth
        ease: 'none',
        scrollTrigger: {
          trigger: heroSection,
          start  : 'top top',
          end    : 'bottom top',
          scrub  : true,
        },
      });
    }
  }


  // ── 3. Helper: scroll-triggered reveal for a selector ─────────────────────
  function revealFrom(selector, triggerEl, vars = {}) {
    const els = gsap.utils.toArray(selector);
    if (!els.length) return;

    const {
      stagger  = 0,
      y        = 22,
      duration = 0.7,
      start    = 'top 85%',
      delay    = 0,
    } = vars;

    gsap.from(els, {
      opacity: 0,
      y,
      duration,
      ease   : EASE,
      stagger,
      delay,
      clearProps: 'willChange',
      scrollTrigger: {
        trigger: triggerEl || els[0],
        start,
        once   : true,
      },
    });
  }

  // ── 4. Section heading reveals (eyebrow only — H2 now done by word-split) ─
  document.querySelectorAll(
    '#vision .eyebrow, #values .eyebrow, #work .eyebrow,' +
    '#process .eyebrow, #team .eyebrow, #contact .eyebrow'
  ).forEach(el => {
    gsap.from(el, {
      opacity: 0,
      y      : 16,
      duration: 0.6,
      ease   : EASE,
      clearProps: 'willChange',
      scrollTrigger: { trigger: el, start: 'top 90%', once: true },
    });
  });

  // ── 5. Vision body ─────────────────────────────────────────────────────────
  const visionSection = document.querySelector('#vision');
  if (visionSection) {
    revealFrom(
      '#vision .vision-body, #vision .lead-text, #vision .vision-stats',
      visionSection, { stagger: 0.1, y: 18 }
    );
  }

  // ── 6. "How We Do Things" bento cards ────────────────────────────────────
  const bentoGrid = document.querySelector('.bento-values');
  if (bentoGrid) {
    revealFrom('.bento-values .bento-card', bentoGrid, { stagger: 0.09, y: 24 });
  }

  // ── 7. Featured Projects ──────────────────────────────────────────────────
  const workSection = document.querySelector('#work');
  if (workSection) {
    revealFrom(
      '#work .cs-visual, #work .cs-info',
      workSection, { stagger: 0.1, y: 20, start: 'top 80%' }
    );
  }


  // ══════════════════════════════════════════════════════════════════════════
  // NEW ② — SCRUBBED PROJECT TIMELINE (desktop only, mobile fallback)
  // ══════════════════════════════════════════════════════════════════════════
  const processSection = document.querySelector('#process');

  if (processSection) {
    if (isMobile()) {
      // ── Mobile fallback: simple staggered reveal ─────────────────────────
      revealFrom('.ht-step', processSection, { stagger: 0.1, y: 20, duration: 0.6 });

    } else {
      // ── Desktop: pinned, scrub-driven timeline ────────────────────────────
      const steps   = gsap.utils.toArray('.ht-step');
      const nodes   = gsap.utils.toArray('.ht-node');
      const contents= gsap.utils.toArray('.ht-content');
      const trackLine = document.querySelector('.ht-step::before'); // CSS pseudo — we'll use a real element

      // Inject a real animated fill line behind the pseudo-element track
      const timeline = document.querySelector('.horizontal-timeline');
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
        scaleX        : '0',
        zIndex        : '1',
      });
      if (timeline) {
        timeline.style.position = 'relative';
        timeline.insertBefore(fillLine, timeline.firstChild);
      }

      // Set initial state for all steps
      gsap.set(nodes,    { borderColor: 'var(--border)', color: 'var(--text-secondary)', scale: 1 });
      gsap.set(contents, { opacity: 0, y: 14 });

      // Master scrub timeline
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger  : processSection,
          start    : 'top top',
          // Give 150vh of scroll distance per step so scrubbing feels deliberate
          end      : `+=${steps.length * 160}`,
          pin      : true,
          scrub    : 1.2,
          anticipatePin: 1,
        },
      });

      // Animate fill line across full width (scrub-driven)
      tl.to(fillLine, { scaleX: 1, ease: 'none' }, 0);

      // Stagger each node highlight + content reveal, evenly spaced across the timeline
      const stepDuration = 1 / steps.length;
      steps.forEach((step, i) => {
        const t = i * stepDuration;

        // Node pulse + orange fill
        tl.to(nodes[i], {
          borderColor     : 'var(--accent)',
          color           : '#ffffff',
          backgroundColor : 'var(--accent)',
          scale           : 1.15,
          duration        : stepDuration * 0.4,
          ease            : 'power2.out',
        }, t);

        // Scale back to normal after brief pulse
        tl.to(nodes[i], {
          scale   : 1,
          duration: stepDuration * 0.3,
          ease    : 'power2.inOut',
        }, t + stepDuration * 0.4);

        // Content fade in
        tl.to(contents[i], {
          opacity : 1,
          y       : 0,
          duration: stepDuration * 0.5,
          ease    : 'power2.out',
        }, t + stepDuration * 0.15);
      });
    }
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


  // ── 11. Hover micro-interactions — unchanged ──────────────────────────────
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


  // ── 12. Cursor follower — unchanged ──────────────────────────────────────
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
