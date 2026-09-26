import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('<main>')
end_idx = html.find('</main>') + len('</main>')

new_main = """<main>
        <section class="hero section" id="home">
            <div class="container hero-grid">
                <div class="hero-content">
                    <p class="eyebrow">DIGITAL PRODUCTS • TECHNOLOGY • INNOVATION</p>
                    <h1>Building Digital Experiences That Move Businesses Forward</h1>
                    <p class="hero-copy">Velociti Studio builds custom software, mobile apps, and AI solutions that solve real business problems. We focus on clean architecture, intuitive design, and scalable technology to turn your ideas into reliable, working systems.</p>
                    <div class="hero-actions">
                        <a class="button button-primary" href="#contact">Get an Estimate</a>
                        <a class="button button-secondary" href="#work">Explore Our Work</a>
                    </div>
                </div>

                <div class="hero-visual" aria-label="Code editor graphic">
                    <div class="code-window">
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

        <!-- VISION (Asymmetric Layout) -->
        <section class="section section-darker" id="vision">
            <div class="container vision-layout">
                <div class="vision-title">
                    <p class="eyebrow">OUR VISION</p>
                    <h2>Building for the Real World</h2>
                </div>
                <div class="vision-text">
                    <p class="lead-text">We are a small team of software engineers and designers who care about building things that actually work. We don't believe in overcomplicating projects or selling unnecessary features.</p>
                    <p>Whether you need a mobile app, a custom internal tool, or an AI-powered system, our goal is to understand exactly what your business needs and build a clean, reliable product that solves your problem.</p>
                </div>
            </div>
        </section>

        <!-- HOW WE DO THINGS (Numbered Grid) -->
        <section class="section" id="values">
            <div class="container">
                <div class="section-header-center">
                    <p class="eyebrow">WHY CHOOSE US</p>
                    <h2>How We Do Things</h2>
                </div>
                
                <div class="bento-values">
                    <div class="bento-card">
                        <span class="bento-num">01</span>
                        <h3>Clear Communication</h3>
                        <p>We speak in plain language. You will always know what we are building, why we are building it, and where the project stands.</p>
                    </div>
                    <div class="bento-card">
                        <span class="bento-num">02</span>
                        <h3>Built for the Requirement</h3>
                        <p>We don't force unnecessary technology into your project. We choose the right tools to solve your specific problem efficiently.</p>
                    </div>
                    <div class="bento-card">
                        <span class="bento-num">03</span>
                        <h3>Straightforward Pricing</h3>
                        <p>No hidden fees or confusing retainer structures. We provide clear estimates and stick to them.</p>
                    </div>
                    <div class="bento-card bento-wide">
                        <span class="bento-num">04</span>
                        <h3>Clean, Maintainable Work</h3>
                        <p>We write clean code and build organized systems so your product is easy to maintain and scale in the future.</p>
                    </div>
                    <div class="bento-card bento-wide">
                        <span class="bento-num">05</span>
                        <h3>Support After Delivery</h3>
                        <p>We don't disappear when the project launches. We ensure everything runs smoothly and provide ongoing support if needed.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- FEATURED PROJECTS (Premium Case Studies) -->
        <section class="section section-darker" id="work">
            <div class="container">
                <div class="section-header-left">
                    <p class="eyebrow">OUR WORK</p>
                    <h2>Featured Projects</h2>
                </div>

                <div class="case-study-list" id="featured-projects-container">
                    <!-- Projects injected via JS, but we'll style the containers in CSS -->
                </div>

                <div class="center-action" style="margin-top: 64px;">
                    <a class="button button-secondary" href="projects.html">View All Projects</a>
                </div>
            </div>
        </section>

        <!-- PROJECT TIMELINE (Horizontal Process) -->
        <section class="section" id="process">
            <div class="container">
                <div class="section-header-left">
                    <p class="eyebrow">HOW WE WORK</p>
                    <h2>The Project Timeline</h2>
                </div>

                <div class="horizontal-timeline">
                    <div class="timeline-track"></div>
                    <div class="ht-step">
                        <div class="ht-node">01</div>
                        <div class="ht-content">
                            <h3>First Meeting</h3>
                            <p>Understand idea & goals.</p>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">02</div>
                        <div class="ht-content">
                            <h3>Ideation</h3>
                            <p>Discuss features & direction.</p>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">03</div>
                        <div class="ht-content">
                            <h3>Planning</h3>
                            <p>Define structure before dev.</p>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">04</div>
                        <div class="ht-content">
                            <h3>Development</h3>
                            <p>Build and test product.</p>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">05</div>
                        <div class="ht-content">
                            <h3>Revisions</h3>
                            <p>Review & make changes.</p>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">06</div>
                        <div class="ht-content">
                            <h3>Delivery</h3>
                            <p>Hand over finished project.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TEAM SECTION -->
        <section class="section section-darker" id="team">
            <div class="container">
                <div class="section-header-center">
                    <p class="eyebrow">OUR TEAM</p>
                    <h2>Meet the Experts</h2>
                </div>

                <div class="team-grid">
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/nikhil-bhagchandani.jpeg" alt="Nikhil Bhagchandani">
                        </div>
                        <div class="card-body">
                            <h3>Nikhil Bhagchandani</h3>
                            <div class="team-links">
                                <a href="https://github.com/NikHub-2k24/" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/laksh-rewani.jpeg" alt="Laksh Rewani">
                        </div>
                        <div class="card-body">
                            <h3>Laksh Rewani</h3>
                            <div class="team-links">
                                <a href="https://github.com/Lakshrewani26" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/om-kaurani.jpeg" alt="Om Kaurani">
                        </div>
                        <div class="card-body">
                            <h3>Om Kaurani</h3>
                            <div class="team-links">
                                <a href="https://github.com/Om-Kaurani" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/yajat-hans.jpeg" alt="Yajat Hans">
                        </div>
                        <div class="card-body">
                            <h3>Yajat Hans</h3>
                            <div class="team-links">
                                <a href="https://github.com/Y-Hans/" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/abhishek-wadhwani.jpeg" alt="Abhishek Wadhwani">
                        </div>
                        <div class="card-body">
                            <h3>Abhishek Wadhwani</h3>
                            <div class="team-links">
                                <a href="https://github.com/abhishekwadhwani2007" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                    <article class="team-card">
                        <div class="profile-placeholder has-profile-image">
                            <img class="profile-image" src="assets/images/team_members/harshita-chhabria.jpeg" alt="Harshita Chhabria">
                        </div>
                        <div class="card-body">
                            <h3>Harshita Chhabria</h3>
                            <div class="team-links">
                                <a href="https://github.com/harshitachhabria18" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="GitHub">
                                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- FINAL CTA -->
        <section class="section" id="contact">
            <div class="container">
                <div class="section-header-center" style="margin-bottom: 64px;">
                    <p class="eyebrow">START A PROJECT</p>
                    <h2>Let's build something real.</h2>
                </div>

                <div class="cta-grid">
                    <!-- Schedule a Call -->
                    <div class="cta-card cta-schedule">
                        <div class="cta-header">
                            <h3>Schedule a Call</h3>
                            <p>Pick a time for a free 30-minute introductory call.</p>
                        </div>
                        <div class="booking-ui" id="booking-ui">
                            <div class="booking-sidebar">
                                <div class="booking-month">October 2026</div>
                                <div class="booking-calendar">
                                    <div class="day-name">Mo</div><div class="day-name">Tu</div><div class="day-name">We</div><div class="day-name">Th</div><div class="day-name">Fr</div>
                                    <div class="day"></div><div class="day"></div><div class="day active">1</div><div class="day">2</div><div class="day">3</div>
                                    <div class="day">6</div><div class="day">7</div><div class="day">8</div><div class="day">9</div><div class="day">10</div>
                                </div>
                            </div>
                            <div class="booking-main">
                                <div class="booking-date-title">Thursday, Oct 1</div>
                                <div class="time-slots">
                                    <button class="time-btn">10:00 AM</button>
                                    <button class="time-btn active">11:30 AM</button>
                                    <button class="time-btn">2:00 PM</button>
                                    <button class="time-btn">3:30 PM</button>
                                </div>
                                <button class="button button-primary confirm-booking-btn">Confirm Time</button>
                            </div>
                        </div>
                        <div class="booking-success" id="booking-success" style="display: none;">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="margin-bottom: 16px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            <h4>Call Scheduled</h4>
                            <p>We've sent a calendar invite to your email.</p>
                            <button class="button button-secondary reset-booking-btn" style="margin-top: 16px;">Book Another Call</button>
                        </div>
                    </div>

                    <!-- Estimate -->
                    <div class="cta-card cta-estimate">
                        <div class="cta-header">
                            <h3>Request an Estimate</h3>
                            <p>Fill out our simple inquiry form to get a detailed project estimate.</p>
                        </div>
                        <a href="inquiry.html" class="cta-large-btn">
                            <span>Open Inquiry Form</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>

                    <!-- Email -->
                    <div class="cta-card cta-email">
                        <div class="cta-header">
                            <h3>Email Us</h3>
                            <p>Send us an email outlining your project.</p>
                        </div>
                        <div class="email-block">
                            <a href="mailto:velocitistudio@gmail.com" class="email-address">velocitistudio@gmail.com</a>
                            <button class="copy-icon-btn copy-email-btn" data-email="velocitistudio@gmail.com" aria-label="Copy Email">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            </button>
                        </div>
                        <p class="copy-feedback" id="copy-feedback" aria-live="polite"></p>
                    </div>
                </div>
            </div>
        </section>
    </main>"""

new_html = html[:start_idx] + new_main + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
