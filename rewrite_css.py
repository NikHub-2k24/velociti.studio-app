import re

css = """
:root {
    --bg-primary: #0a0d14;
    --bg-secondary: #111520;
    --bg-tertiary: #1a1f2e;
    --accent: #ff641f;
    --accent-hover: #ff7b3f;
    --accent-soft: rgba(255, 100, 31, 0.1);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --border: rgba(255, 255, 255, 0.08);
    --border-strong: rgba(255, 100, 31, 0.3);
    --container: 1200px;
    --header-height: 80px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
:target { scroll-margin-top: calc(var(--header-height) + 20px); }

body {
    margin: 0;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: var(--text-primary);
    background: var(--bg-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
h1, h2, h3, h4, p { margin: 0; }

.container {
    width: min(100% - 48px, var(--container));
    margin: 0 auto;
}

/* =========================================
   HEADER & LOGO
========================================= */
.site-header {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(10, 13, 20, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
}

.header-inner {
    height: var(--header-height);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.brand {
    display: flex;
    align-items: center;
}

/* LOGO REWORK */
.brand-logo {
    height: 24px;
    width: auto;
    object-fit: contain;
    filter: brightness(1.2) drop-shadow(0 0 12px rgba(255,255,255,0.1));
}

.primary-nav, .footer-nav {
    display: flex;
    gap: 32px;
}
.primary-nav a, .footer-nav a {
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text-secondary);
    transition: color 0.2s;
}
.primary-nav a:hover { color: var(--text-primary); }

.menu-toggle { display: none; }

/* =========================================
   TYPOGRAPHY & SECTIONS
========================================= */
.section { padding: 120px 0; }
.section-darker { background: var(--bg-secondary); border-block: 1px solid var(--border); }

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
}
.eyebrow::before {
    content: '';
    width: 24px;
    height: 2px;
    background: var(--accent);
}

h1 {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    line-height: 1.05;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 24px;
}
h2 {
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.1;
    font-weight: 700;
    letter-spacing: -0.02em;
}
h3 {
    font-size: 1.5rem;
    line-height: 1.3;
    font-weight: 600;
}

.section-header-left, .section-header-center { margin-bottom: 64px; }
.section-header-center { text-align: center; }
.section-header-center .eyebrow { justify-content: center; }
.section-header-center .eyebrow::before { display: none; }

.lead-text {
    font-size: 1.25rem;
    color: var(--text-primary);
    margin-bottom: 16px;
}

/* =========================================
   BUTTONS
========================================= */
.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 52px;
    padding: 0 28px;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    border: 1px solid transparent;
}
.button-primary {
    background: var(--accent);
    color: #fff;
}
.button-primary:hover {
    background: var(--accent-hover);
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(255, 100, 31, 0.2);
}
.button-secondary {
    background: transparent;
    color: var(--text-primary);
    border-color: var(--border);
}
.button-secondary:hover {
    border-color: var(--text-secondary);
    background: rgba(255,255,255,0.03);
}

/* =========================================
   HERO
========================================= */
.hero {
    padding: 80px 0 120px;
}
.hero-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 64px;
    align-items: center;
}
.hero-copy {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 40px;
    max-width: 540px;
}
.hero-actions {
    display: flex;
    gap: 16px;
}

.code-window {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 30px 60px rgba(0,0,0,0.5);
}
.code-header {
    background: var(--bg-tertiary);
    padding: 16px;
    display: flex;
    gap: 8px;
    border-bottom: 1px solid var(--border);
}
.code-header .dot {
    width: 12px; height: 12px; border-radius: 50%;
    background: var(--border);
}
.code-header .dot:nth-child(1) { background: #ff5f56; }
.code-header .dot:nth-child(2) { background: #ffbd2e; }
.code-header .dot:nth-child(3) { background: #27c93f; }
.code-body {
    padding: 32px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.9rem;
    line-height: 1.7;
}
.code-keyword { color: #ff641f; }
.code-variable { color: #e2e8f0; }
.code-property { color: #94a3b8; }
.code-string { color: #27c93f; }
.code-function { color: #61afef; }

/* =========================================
   VISION
========================================= */
.vision-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
}
.vision-text p {
    color: var(--text-secondary);
    font-size: 1.1rem;
    margin-bottom: 24px;
}

/* =========================================
   HOW WE DO THINGS (BENTO GRID)
========================================= */
.bento-values {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: minmax(280px, auto);
    gap: 24px;
}
.bento-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    transition: border-color 0.3s;
}
.bento-card:hover {
    border-color: var(--border-strong);
}
.bento-num {
    font-size: 3rem;
    font-weight: 700;
    color: var(--accent-soft);
    margin-bottom: auto;
    line-height: 1;
}
.bento-card h3 {
    margin-top: 32px;
    margin-bottom: 12px;
}
.bento-card p {
    color: var(--text-secondary);
    font-size: 0.95rem;
}
.bento-wide {
    grid-column: span 2;
}

/* =========================================
   PROJECT TIMELINE
========================================= */
.horizontal-timeline {
    display: flex;
    gap: 32px;
    overflow-x: auto;
    padding-bottom: 40px;
    scrollbar-width: none; /* Firefox */
}
.horizontal-timeline::-webkit-scrollbar { display: none; }
.ht-step {
    flex: 0 0 280px;
    position: relative;
    padding-top: 60px;
}
.ht-step::before {
    content: '';
    position: absolute;
    top: 24px;
    left: 0;
    right: -32px;
    height: 2px;
    background: var(--border);
}
.ht-step:last-child::before { right: 0; }
.ht-node {
    position: absolute;
    top: 0;
    left: 0;
    width: 50px;
    height: 50px;
    background: var(--bg-primary);
    border: 2px solid var(--border);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: var(--text-secondary);
    z-index: 2;
    transition: all 0.3s;
}
.ht-step:hover .ht-node {
    border-color: var(--accent);
    color: var(--accent);
}
.ht-content h3 { margin-bottom: 8px; }
.ht-content p { color: var(--text-secondary); }

/* =========================================
   FEATURED PROJECTS (CASE STUDIES)
========================================= */
.case-study-list {
    display: flex;
    flex-direction: column;
    gap: 120px;
}
.case-study {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 64px;
    align-items: center;
}
.case-study:nth-child(even) {
    grid-template-columns: 0.8fr 1.2fr;
}
.case-study:nth-child(even) .cs-visual {
    order: 2;
}
.cs-visual {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid var(--border);
    background: var(--bg-tertiary);
    aspect-ratio: 4/3;
    display: flex;
    align-items: center;
    justify-content: center;
}
.cs-visual-placeholder {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-secondary);
    letter-spacing: 0.1em;
}
.cs-meta {
    display: flex;
    gap: 12px;
    margin-bottom: 24px;
}
.cs-tag {
    padding: 6px 14px;
    border-radius: 100px;
    border: 1px solid var(--border);
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.cs-title {
    font-size: 2.5rem;
    margin-bottom: 16px;
}
.cs-desc {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin-bottom: 32px;
}
.cs-link {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-weight: 600;
    color: var(--accent);
}
.cs-link svg {
    transition: transform 0.2s;
}
.cs-link:hover svg {
    transform: translateX(4px);
}

/* =========================================
   TEAM
========================================= */
.team-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
}
.team-card {
    text-align: center;
}
.team-card .profile-placeholder {
    width: 180px;
    height: 180px;
    margin: 0 auto 24px;
    border-radius: 50%;
    overflow: hidden;
    border: 1px solid var(--border);
    background: var(--bg-tertiary);
}
.team-card h3 {
    font-size: 1.25rem;
    margin-bottom: 12px;
}
.team-links {
    display: flex;
    justify-content: center;
}
.team-card .social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--bg-tertiary);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-secondary);
    transition: all 0.2s;
}
.team-card .social-icon:hover {
    background: var(--accent);
    color: #fff;
}
.team-card .social-icon svg { width: 20px; height: 20px; }

/* =========================================
   FINAL CTA
========================================= */
.cta-grid {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    grid-template-rows: auto auto;
    gap: 24px;
}
.cta-schedule {
    grid-row: span 2;
}
.cta-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 48px;
    display: flex;
    flex-direction: column;
}
.cta-header h3 { font-size: 1.8rem; margin-bottom: 12px; }
.cta-header p { color: var(--text-secondary); margin-bottom: 32px; }

/* Booking UI */
.booking-ui {
    display: flex;
    gap: 32px;
    background: var(--bg-primary);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin-top: auto;
}
.booking-sidebar { width: 220px; }
.booking-month { font-weight: 600; margin-bottom: 16px; }
.booking-calendar {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    text-align: center;
}
.day-name { font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 8px; }
.day {
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.2s;
}
.day:hover:not(:empty) { background: var(--bg-tertiary); }
.day.active { background: var(--accent); color: #fff; font-weight: 600; }
.booking-main { flex: 1; border-left: 1px solid var(--border); padding-left: 32px; }
.booking-date-title { font-weight: 600; margin-bottom: 16px; }
.time-slots { display: grid; gap: 12px; margin-bottom: 24px; }
.time-btn {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 12px;
    border-radius: 8px;
    cursor: pointer;
    font-family: inherit;
    font-weight: 500;
    transition: all 0.2s;
}
.time-btn:hover { border-color: var(--border-strong); }
.time-btn.active { background: rgba(255, 100, 31, 0.1); border-color: var(--accent); color: var(--accent); }
.confirm-booking-btn { width: 100%; height: 44px; }

.cta-large-btn {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--bg-primary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 32px;
    font-size: 1.25rem;
    font-weight: 600;
    transition: border-color 0.2s;
    margin-top: auto;
}
.cta-large-btn:hover { border-color: var(--text-secondary); }
.email-block {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: auto;
}
.email-address {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--accent);
}
.copy-icon-btn {
    background: var(--bg-primary);
    border: 1px solid var(--border);
    color: var(--text-primary);
    width: 44px;
    height: 44px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.2s;
}
.copy-icon-btn:hover { background: var(--bg-tertiary); }

/* =========================================
   FOOTER
========================================= */
.site-footer {
    padding: 64px 0 32px;
    border-top: 1px solid var(--border);
}
.footer-grid {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 64px;
}
.footer-brand p {
    color: var(--text-secondary);
    max-width: 300px;
    margin-top: 24px;
}
.footer-social { display: flex; gap: 16px; }
.footer-social a {
    color: var(--text-secondary);
}
.footer-social a:hover { color: var(--text-primary); }
.footer-bottom {
    text-align: center;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* =========================================
   MEDIA QUERIES
========================================= */
@media (max-width: 1024px) {
    .bento-values { grid-template-columns: 1fr 1fr; }
    .bento-wide { grid-column: span 1; }
    .vision-layout { grid-template-columns: 1fr; gap: 32px; }
    .cta-grid { grid-template-columns: 1fr; }
    .cta-schedule { grid-row: auto; }
}

@media (max-width: 768px) {
    .hero-grid { grid-template-columns: 1fr; gap: 48px; }
    .case-study, .case-study:nth-child(even) {
        grid-template-columns: 1fr;
        gap: 32px;
    }
    .case-study:nth-child(even) .cs-visual { order: 0; }
    
    .horizontal-timeline {
        flex-direction: column;
        overflow-x: visible;
        padding-left: 24px;
        gap: 0;
    }
    .ht-step {
        flex: auto;
        padding-top: 0;
        padding-bottom: 48px;
        padding-left: 48px;
    }
    .ht-step::before {
        top: 24px;
        bottom: 0;
        left: -1px;
        width: 2px;
        height: auto;
    }
    .ht-node {
        top: 0;
        left: -25px;
    }
    
    .team-grid { grid-template-columns: 1fr; }
    .booking-ui { flex-direction: column; }
    .booking-main { border-left: none; padding-left: 0; border-top: 1px solid var(--border); padding-top: 32px; }
    
    .menu-toggle {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 5px;
        width: 44px; height: 44px;
        background: transparent;
        border: none;
        cursor: pointer;
    }
    .menu-toggle span {
        width: 24px; height: 2px; background: #fff;
    }
    .primary-nav {
        display: none;
    }
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
