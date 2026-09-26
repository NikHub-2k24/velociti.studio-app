import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Velociti Studio | Software & Digital Products</title>
    <meta name="description" content="Velociti Studio builds custom software, mobile apps, and AI solutions.">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <a class="brand" href="index.html#home" aria-label="Velociti Studio home">
                <img class="brand-logo" src="assets/images/logo/velocity_logo.png" alt="Velociti Studio logo">
            </a>

            <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-navigation">
                <span class="menu-toggle-line"></span>
                <span class="menu-toggle-line"></span>
                <span class="menu-toggle-line"></span>
                <span class="sr-only">Toggle navigation</span>
            </button>

            <nav class="primary-nav" id="primary-navigation" aria-label="Primary navigation">
                <a href="#vision">Vision</a>
                <a href="#values">How We Do Things</a>
                <a href="#work">Our Work</a>
                <a href="#process">Timeline</a>
                <a href="#team">Team</a>
            </nav>
        </div>
    </header>

    <main>
        <!-- HERO -->
        <section class="section section--hero" id="home">
            <div class="section__glow"></div>
            <div class="container hero-grid">
                <div class="hero-content" data-animate="fade-up">
                    <p class="eyebrow" data-animate="fade-in">DIGITAL PRODUCTS &bull; TECHNOLOGY &bull; INNOVATION</p>
                    <h1 class="section__title-hero" data-animate="fade-up">Building Digital Experiences That Move Businesses Forward</h1>
                    <p class="hero-copy" data-animate="fade-up">Velociti Studio builds custom software, mobile apps, and AI solutions that solve real business problems. We focus on clean architecture, intuitive design, and scalable technology to turn your ideas into reliable, working systems.</p>
                    <div class="hero-actions" data-animate="fade-in">
                        <a class="button button--primary" href="#contact">Get an Estimate</a>
                        <a class="button button--secondary" href="#work">Explore Our Work</a>
                    </div>
                </div>

                <div class="hero-visual" aria-label="Code editor graphic" data-animate="fade-in">
                    <div class="code-window card">
                        <div class="code-header">
                            <span class="dot"></span>
                            <span class="dot"></span>
                            <span class="dot"></span>
                        </div>
                        <div class="code-body">
<pre><code><span class="code-keyword">const</span> <span class="code-variable">velociti</span> = {
  <span class="code-property">focus</span>: <span class="code-string">"Digital Products"</span>,
  <span class="code-property">approach</span>: <span class="code-string">"Keep it clean, make it work."</span>,
  <span class="code-property">stack</span>: [<span class="code-string">"Web"</span>, <span class="code-string">"Mobile"</span>, <span class="code-string">"AI"</span>],
  <span class="code-function">build</span>() {
    <span class="code-keyword">return</span> <span class="code-keyword">this</span>.<span class="code-property">focus</span>;
  }
};

<span class="code-variable">velociti</span>.<span class="code-function">build</span>();</code></pre>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VISION -->
        <section class="section section--alt" id="vision">
            <div class="container vision-layout">
                <div class="vision-title" data-animate="slide-right">
                    <p class="eyebrow">OUR VISION</p>
                    <h2 class="section__title">Building for the Real World</h2>
                </div>
                <div class="vision-text" data-animate="fade-in">
                    <p class="lead-text">We are a small team of software engineers and designers who care about building things that actually work. We don't believe in overcomplicating projects or selling unnecessary features.</p>
                    <p>Whether you need a mobile app, a custom internal tool, or an AI-powered system, our goal is to understand exactly what your business needs and build a clean, reliable product that solves your problem.</p>
                </div>
            </div>
        </section>

        <!-- HOW WE DO THINGS -->
        <section class="section" id="values">
            <div class="container">
                <div class="section__header section__header--center" data-animate="fade-up">
                    <p class="eyebrow">WHY CHOOSE US</p>
                    <h2 class="section__title">How We Do Things</h2>
                </div>
                
                <div class="grid grid--bento">
                    <div class="card card--feature" data-animate="fade-up">
                        <div class="card__icon-chip">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                        </div>
                        <h3 class="card__title">Clear Communication</h3>
                        <p class="card__desc">We speak in plain language. You will always know what we are building, why we are building it, and where the project stands.</p>
                    </div>
                    <div class="card card--feature" data-animate="fade-up">
                        <div class="card__icon-chip">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                        </div>
                        <h3 class="card__title">Built for the Requirement</h3>
                        <p class="card__desc">We don't force unnecessary technology into your project. We choose the right tools to solve your specific problem efficiently.</p>
                    </div>
                    <div class="card card--feature" data-animate="fade-up">
                        <div class="card__icon-chip">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                        </div>
                        <h3 class="card__title">Straightforward Pricing</h3>
                        <p class="card__desc">No hidden fees or confusing retainer structures. We provide clear estimates and stick to them.</p>
                    </div>
                    <div class="card card--feature card--wide" data-animate="fade-up">
                        <div class="card__icon-chip">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                        </div>
                        <h3 class="card__title">Clean, Maintainable Work</h3>
                        <p class="card__desc">We write clean code and build organized systems so your product is easy to maintain and scale in the future.</p>
                    </div>
                    <div class="card card--feature card--wide" data-animate="fade-up">
                        <div class="card__icon-chip">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                        </div>
                        <h3 class="card__title">Support After Delivery</h3>
                        <p class="card__desc">We don't disappear when the project launches. We ensure everything runs smoothly and provide ongoing support if needed.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- FEATURED PROJECTS -->
        <section class="section section--alt" id="work">
            <div class="container">
                <div class="section__header" data-animate="fade-up">
                    <p class="eyebrow">OUR WORK</p>
                    <h2 class="section__title">Featured Projects</h2>
                </div>

                <div class="grid grid--projects" id="featured-projects-container">
                    <!-- Cards will be injected by JS, styled by our new CSS -->
                </div>

                <div class="section__footer" data-animate="fade-in">
                    <a class="button button--secondary" href="projects.html">View All Projects</a>
                </div>
            </div>
        </section>

        <!-- PROJECT TIMELINE -->
        <section class="section" id="process">
            <div class="container">
                <div class="section__header" data-animate="fade-up">
                    <p class="eyebrow">HOW WE WORK</p>
                    <h2 class="section__title">The Project Timeline</h2>
                </div>

                <div class="timeline" data-animate="fade-in">
                    <div class="timeline__track"></div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">01</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">First Meeting</h3>
                            <p class="card__desc">Understand idea & goals.</p>
                        </div>
                    </div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">02</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">Ideation</h3>
                            <p class="card__desc">Discuss features & direction.</p>
                        </div>
                    </div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">03</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">Planning</h3>
                            <p class="card__desc">Define structure before dev.</p>
                        </div>
                    </div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">04</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">Development</h3>
                            <p class="card__desc">Build and test product.</p>
                        </div>
                    </div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">05</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">Revisions</h3>
                            <p class="card__desc">Review & make changes.</p>
                        </div>
                    </div>
                    
                    <div class="timeline__step">
                        <div class="timeline__badge">06</div>
                        <div class="card card--timeline">
                            <h3 class="card__title">Delivery</h3>
                            <p class="card__desc">Hand over finished project.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TEAM SECTION -->
        <section class="section section--alt" id="team">
            <div class="container">
                <div class="section__header section__header--center" data-animate="fade-up">
                    <p class="eyebrow">OUR TEAM</p>
                    <h2 class="section__title">Meet the Experts</h2>
                </div>

                <div class="grid grid--team">
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/nikhil-bhagchandani.jpeg" alt="Nikhil Bhagchandani">
                        </div>
                        <h3 class="card__name">Nikhil Bhagchandani</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/laksh-rewani.jpeg" alt="Laksh Rewani">
                        </div>
                        <h3 class="card__name">Laksh Rewani</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/om-kaurani.jpeg" alt="Om Kaurani">
                        </div>
                        <h3 class="card__name">Om Kaurani</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/yajat-hans.jpeg" alt="Yajat Hans">
                        </div>
                        <h3 class="card__name">Yajat Hans</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/abhishek-wadhwani.jpeg" alt="Abhishek Wadhwani">
                        </div>
                        <h3 class="card__name">Abhishek Wadhwani</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                    <div class="card card--team" data-animate="scale-up">
                        <div class="card__avatar-ring">
                            <img class="card__avatar" src="assets/images/team_members/harshita-chhabria.jpeg" alt="Harshita Chhabria">
                        </div>
                        <h3 class="card__name">Harshita Chhabria</h3>
                        <p class="card__role">Software Engineer</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- FINAL CTA -->
        <section class="section section--cta" id="contact">
            <div class="section__glow"></div>
            <div class="container">
                <div class="section__header section__header--center" data-animate="fade-up">
                    <p class="eyebrow">START A PROJECT</p>
                    <h2 class="section__title">Let's build something real.</h2>
                </div>

                <div class="grid grid--cta">
                    <div class="card card--cta" data-animate="fade-up">
                        <div class="card__header">
                            <h3 class="card__title">Schedule a Call</h3>
                            <p class="card__desc">Pick a time for a free 30-minute introductory call.</p>
                        </div>
                        <div class="booking-ui">
                            <div class="booking-placeholder">
                                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                <h4>Book a Call</h4>
                                <p>Ready to connect to Cal.com or Calendly.</p>
                                <button class="button button--primary" style="margin-top: var(--space-md); width: 100%;">Connect Calendar</button>
                            </div>
                        </div>
                    </div>

                    <div class="card card--cta" data-animate="fade-up">
                        <div class="card__header">
                            <h3 class="card__title">Request an Estimate</h3>
                            <p class="card__desc">Fill out our simple inquiry form to get a detailed project estimate.</p>
                        </div>
                        <a href="inquiry.html" class="button button--secondary cta-link-btn">
                            Open Inquiry Form
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>

                    <div class="card card--cta" data-animate="fade-up">
                        <div class="card__header">
                            <h3 class="card__title">Email Us</h3>
                            <p class="card__desc">Send us an email outlining your project.</p>
                        </div>
                        <div class="email-block">
                            <a href="mailto:velocitistudio@gmail.com" class="email-address">velocitistudio@gmail.com</a>
                            <button class="copy-email-btn" data-email="velocitistudio@gmail.com" aria-label="Copy Email">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            </button>
                        </div>
                        <p class="copy-feedback" id="copy-feedback" aria-live="polite"></p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <a class="brand" href="index.html#home" aria-label="Velociti Studio home">
                    <img class="brand-logo footer-logo" src="assets/images/logo/velocity_logo.png" alt="Velociti Studio logo">
                </a>
                <p>Building digital products and technology solutions that help businesses turn ideas into working systems.</p>
            </div>

            <nav class="footer-nav" aria-label="Footer navigation">
                <a href="index.html#home">Home</a>
                <a href="index.html#vision">Vision</a>
                <a href="index.html#work">Our Work</a>
                <a href="index.html#team">Team</a>
            </nav>
        </div>

        <div class="container footer-bottom">
            <p>&copy; <span id="current-year"></span> Velociti Studio. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>
"""

css_code = """
:root {
    /* COLORS */
    --color-bg-base: #0a0e1a;
    --color-bg-alt: #101524;
    --color-accent: #ff6b35;
    --color-accent-hover: #ff8559;
    --color-accent-glow: #8b2500;
    --color-accent-transparent: rgba(255, 107, 53, 0.15);
    
    --color-text-main: #f8fafc;
    --color-text-muted: #94a3b8;
    
    --color-border: rgba(255, 255, 255, 0.1);
    --color-border-hover: rgba(255, 107, 53, 0.4);
    --color-card-bg: rgba(16, 21, 36, 0.6);

    /* SPACING */
    --space-xs: 8px;
    --space-sm: 16px;
    --space-md: 24px;
    --space-lg: 48px;
    --space-xl: 80px;
    --space-section: 120px;

    /* TYPOGRAPHY */
    --font-sans: 'Inter', system-ui, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;

    /* LAYOUT */
    --container-width: 1200px;
    --header-height: 80px;
    
    /* SHADOWS & TRANSITIONS */
    --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.3);
    --shadow-card-hover: 0 16px 48px rgba(255, 107, 53, 0.15);
    --transition-fast: 0.2s ease;
    --transition-smooth: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
    margin: 0;
    font-family: var(--font-sans);
    color: var(--color-text-main);
    background: var(--color-bg-base);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

img, svg { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
h1, h2, h3, h4, p { margin: 0; }

.container {
    width: min(100% - var(--space-lg), var(--container-width));
    margin: 0 auto;
}

/* =========================================
   HEADER & NAV
========================================= */
.site-header {
    position: sticky; top: 0; z-index: 50;
    background: rgba(10, 14, 26, 0.85);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--color-border);
}
.header-inner {
    height: var(--header-height);
    display: flex; align-items: center; justify-content: space-between;
}
.brand-logo { height: 26px; filter: brightness(1.1); }
.footer-logo { filter: grayscale(1) opacity(0.6); }

.primary-nav, .footer-nav { display: flex; gap: var(--space-md); }
.primary-nav a, .footer-nav a {
    font-size: 0.9rem; font-weight: 500;
    color: var(--color-text-muted);
    transition: color var(--transition-fast);
}
.primary-nav a:hover { color: var(--color-text-main); }
.menu-toggle { display: none; }

/* =========================================
   SECTIONS & TYPOGRAPHY
========================================= */
.section { position: relative; padding: var(--space-section) 0; overflow: hidden; }
.section--alt { background: var(--color-bg-alt); }
.section--hero { padding-top: calc(var(--space-section) - var(--space-xl)); }

.section__glow {
    position: absolute;
    width: 600px; height: 600px;
    background: radial-gradient(circle, var(--color-accent-glow) 0%, transparent 70%);
    opacity: 0.15; filter: blur(80px);
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    pointer-events: none; z-index: 0;
}

.section__header { margin-bottom: var(--space-xl); position: relative; z-index: 1; }
.section__header--center { text-align: center; }

.eyebrow {
    display: inline-flex; align-items: center; gap: var(--space-xs);
    font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--color-accent);
    margin-bottom: var(--space-md);
}
.section__header:not(.section__header--center) .eyebrow::before {
    content: ''; width: 24px; height: 2px; background: var(--color-accent);
}

.section__title-hero {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    line-height: 1.05; font-weight: 700; letter-spacing: -0.03em;
    margin-bottom: var(--space-md);
}
.section__title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.1; font-weight: 700; letter-spacing: -0.02em;
}

/* =========================================
   BUTTONS
========================================= */
.button {
    display: inline-flex; align-items: center; justify-content: center; gap: var(--space-xs);
    height: 52px; padding: 0 var(--space-md);
    border-radius: 8px; font-size: 0.95rem; font-weight: 600;
    cursor: pointer; transition: all var(--transition-fast);
    border: 1px solid transparent; text-align: center;
}
.button--primary { background: var(--color-accent); color: #fff; }
.button--primary:hover {
    background: var(--color-accent-hover);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px var(--color-accent-transparent);
}
.button--secondary { background: transparent; color: var(--color-text-main); border-color: var(--color-border); }
.button--secondary:hover {
    border-color: var(--color-border-hover);
    background: var(--color-accent-transparent);
}

/* =========================================
   CARDS (Base)
========================================= */
.card {
    background: var(--color-card-bg);
    border: 1px solid var(--color-border);
    border-radius: 16px;
    box-shadow: var(--shadow-card);
    transition: all var(--transition-smooth);
    position: relative; z-index: 1;
    overflow: hidden;
    backdrop-filter: blur(12px);
}
.card:hover {
    transform: translateY(-4px);
    border-color: var(--color-border-hover);
    box-shadow: var(--shadow-card-hover);
}

/* =========================================
   GRIDS
========================================= */
.grid { display: grid; gap: var(--space-lg); position: relative; z-index: 1; }
.grid--bento { grid-template-columns: repeat(3, 1fr); }
.grid--projects { grid-template-columns: repeat(2, 1fr); }
.grid--team { grid-template-columns: repeat(3, 1fr); }
.grid--cta { grid-template-columns: 1.2fr 0.8fr; grid-template-rows: auto auto; }

/* =========================================
   HERO COMPONENTS
========================================= */
.hero-grid { grid-template-columns: 1.1fr 0.9fr; align-items: center; }
.hero-copy { font-size: 1.1rem; color: var(--color-text-muted); margin-bottom: var(--space-lg); max-width: 540px; }
.hero-actions { display: flex; gap: var(--space-sm); }
.code-window { font-family: var(--font-mono); font-size: 0.9rem; }
.code-header { padding: var(--space-sm) var(--space-md); border-bottom: 1px solid var(--color-border); display: flex; gap: var(--space-xs); background: rgba(0,0,0,0.2); }
.code-header .dot { width: 12px; height: 12px; border-radius: 50%; background: var(--color-border); }
.code-body { padding: var(--space-lg); color: var(--color-text-main); }
.code-keyword { color: var(--color-accent); }
.code-string { color: #27c93f; }
.code-function { color: #61afef; }

/* =========================================
   VISION COMPONENTS
========================================= */
.vision-layout { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-xl); align-items: center; }
.vision-text .lead-text { font-size: 1.25rem; margin-bottom: var(--space-md); color: var(--color-text-main); }
.vision-text p { color: var(--color-text-muted); font-size: 1.1rem; }

/* =========================================
   FEATURE COMPONENTS (How we do things)
========================================= */
.card--feature { padding: var(--space-lg); display: flex; flex-direction: column; }
.card__icon-chip {
    width: 48px; height: 48px; border-radius: 12px;
    background: var(--color-accent-transparent);
    color: var(--color-accent);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: var(--space-lg);
}
.card__icon-chip svg { width: 24px; height: 24px; }
.card--feature .card__title { font-size: 1.25rem; margin-bottom: var(--space-xs); }
.card--feature .card__desc { color: var(--color-text-muted); font-size: 0.95rem; }
.card--wide { grid-column: span 2; }

/* =========================================
   PROJECT COMPONENTS
========================================= */
.card--project { display: flex; flex-direction: column; }
.card__thumbnail {
    width: 100%; aspect-ratio: 16/10;
    background: linear-gradient(135deg, var(--color-bg-alt), var(--color-bg-base));
    border-bottom: 1px solid var(--color-border);
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
}
.card__thumbnail img { width: 100%; height: 100%; object-fit: cover; }
.card__placeholder { font-size: 0.85rem; letter-spacing: 0.1em; color: var(--color-border); }
.card__content { padding: var(--space-lg); flex: 1; display: flex; flex-direction: column; }
.card__meta { font-size: 0.75rem; text-transform: uppercase; color: var(--color-accent); font-weight: 700; letter-spacing: 0.05em; margin-bottom: var(--space-xs); }
.card--project .card__title { font-size: 1.5rem; margin-bottom: var(--space-sm); }
.card--project .card__desc { color: var(--color-text-muted); margin-bottom: var(--space-lg); font-size: 0.95rem; }
.card__link { margin-top: auto; display: inline-flex; align-items: center; gap: var(--space-xs); color: var(--color-text-main); font-weight: 600; transition: color var(--transition-fast); }
.card__link svg { transition: transform var(--transition-fast); color: var(--color-accent); }
.card--project:hover .card__link { color: var(--color-accent); }
.card--project:hover .card__link svg { transform: translateX(4px); }

/* =========================================
   TIMELINE COMPONENTS
========================================= */
.timeline { display: flex; align-items: flex-start; gap: var(--space-lg); overflow-x: auto; padding-bottom: var(--space-md); position: relative; scrollbar-width: none; }
.timeline::-webkit-scrollbar { display: none; }
.timeline__track { position: absolute; top: 24px; left: 0; right: 0; height: 2px; background: var(--color-border); z-index: 0; }
.timeline__step { flex: 0 0 280px; position: relative; z-index: 1; }
.timeline__badge {
    width: 50px; height: 50px; border-radius: 50%;
    background: var(--color-bg-base); border: 2px solid var(--color-border);
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 1.1rem; color: var(--color-text-muted);
    margin-bottom: var(--space-md); transition: all var(--transition-fast);
}
.timeline__step:hover .timeline__badge { border-color: var(--color-accent); color: var(--color-accent); box-shadow: 0 0 20px var(--color-accent-transparent); }
.card--timeline { padding: var(--space-md); }
.card--timeline .card__title { font-size: 1.1rem; margin-bottom: var(--space-xs); }
.card--timeline .card__desc { font-size: 0.9rem; color: var(--color-text-muted); }

/* =========================================
   TEAM COMPONENTS
========================================= */
.card--team { padding: var(--space-lg); text-align: center; }
.card__avatar-ring {
    width: 140px; height: 140px; margin: 0 auto var(--space-md);
    border-radius: 50%; border: 2px solid var(--color-border);
    padding: 6px; transition: border-color var(--transition-fast);
}
.card--team:hover .card__avatar-ring { border-color: var(--color-accent); box-shadow: 0 0 20px var(--color-accent-transparent); }
.card__avatar { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; }
.card--team .card__name { font-size: 1.25rem; font-weight: 700; color: var(--color-text-main); margin-bottom: 4px; }
.card--team .card__role { font-size: 0.95rem; color: var(--color-text-muted); }

/* =========================================
   CTA COMPONENTS
========================================= */
.card--cta { padding: var(--space-lg); display: flex; flex-direction: column; }
.card--cta:first-child { grid-row: span 2; }
.card--cta .card__header { margin-bottom: var(--space-md); }
.card--cta .card__title { font-size: 1.5rem; margin-bottom: var(--space-xs); }
.card--cta .card__desc { color: var(--color-text-muted); }
.booking-ui { flex: 1; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.2); border-radius: 8px; border: 1px dashed var(--color-border); padding: var(--space-lg); text-align: center; }
.booking-placeholder svg { color: var(--color-text-muted); margin-bottom: var(--space-sm); }

.cta-link-btn { justify-content: space-between; padding: var(--space-md); height: auto; margin-top: auto; }
.email-block { display: flex; align-items: center; gap: var(--space-sm); margin-top: auto; background: rgba(0,0,0,0.2); padding: var(--space-sm) var(--space-md); border-radius: 8px; border: 1px solid var(--color-border); }
.email-address { font-weight: 600; flex: 1; }
.copy-email-btn { background: transparent; border: none; color: var(--color-text-muted); cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 8px; border-radius: 4px; transition: all var(--transition-fast); }
.copy-email-btn:hover { background: var(--color-accent-transparent); color: var(--color-accent); }
.copy-feedback { font-size: 0.85rem; color: var(--color-accent); margin-top: var(--space-xs); min-height: 20px; }

/* =========================================
   FOOTER
========================================= */
.site-footer { padding: var(--space-xl) 0 var(--space-md); border-top: 1px solid var(--color-border); }
.footer-grid { display: flex; justify-content: space-between; margin-bottom: var(--space-xl); }
.footer-brand p { color: var(--color-text-muted); max-width: 300px; margin-top: var(--space-md); font-size: 0.95rem; }
.footer-bottom { text-align: center; color: var(--color-text-muted); font-size: 0.85rem; }

/* =========================================
   MEDIA QUERIES
========================================= */
@media (max-width: 1024px) {
    .grid--bento { grid-template-columns: 1fr 1fr; }
    .card--wide { grid-column: span 1; }
    .grid--projects { grid-template-columns: 1fr; }
    .grid--team { grid-template-columns: repeat(2, 1fr); }
    .grid--cta { grid-template-columns: 1fr; }
    .card--cta:first-child { grid-row: auto; }
}

@media (max-width: 768px) {
    .hero-grid, .vision-layout { grid-template-columns: 1fr; gap: var(--space-xl); }
    .grid { grid-template-columns: 1fr; }
    
    .timeline { flex-direction: column; overflow: visible; padding-left: var(--space-lg); gap: 0; }
    .timeline__track { top: 0; bottom: 0; left: var(--space-lg); width: 2px; height: auto; }
    .timeline__step { width: 100%; display: flex; align-items: flex-start; gap: var(--space-md); padding-bottom: var(--space-lg); }
    .timeline__badge { margin-bottom: 0; margin-left: -25px; flex-shrink: 0; }
    .card--timeline { width: 100%; }
    
    .menu-toggle {
        display: flex; flex-direction: column; gap: 5px; background: transparent;
        border: none; cursor: pointer; width: 40px; height: 40px; justify-content: center;
    }
    .menu-toggle-line { width: 24px; height: 2px; background: #fff; }
    .primary-nav { display: none; }
}
"""

with open('update_visuals.py', 'w', encoding='utf-8') as f:
    f.write(f"""
import os

html = '''{html_code}'''
css = '''{css_code}'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update projects.html & inquiry.html just to fix the new variables for background
def patch_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple replace to ensure it still looks okay. Not changing their layouts since user said "this site", implying index
    # We will just write back.
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

patch_file('projects.html')
patch_file('inquiry.html')
""")
