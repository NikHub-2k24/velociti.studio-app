import sys

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
                    <p class="hero-copy">Velociti Studio builds digital products and technology solutions that help businesses turn ideas into working systems. We combine product strategy, UX/UI, software engineering, AI, automation, and modern technologies to create solutions that are practical, scalable, and built for the real world.</p>
                    <a class="button button-primary" href="#contact">Get an Estimate</a>
                    <a class="button button-secondary" href="#work" style="margin-left: 12px;">Explore Our Work</a>
                </div>

                <div class="hero-visual" aria-label="Hero visual graphic">
                </div>
            </div>
        </section>

        <section class="section section-panel" id="vision">
            <div class="container split-section">
                <div class="section-heading">
                    <p class="eyebrow">OUR VISION</p>
                    <h2>Building for the Real World</h2>
                </div>
                <div class="section-copy">
                    <p>We are a small team of software engineers and designers who care about building things that actually work. We don't believe in overcomplicating projects or selling unnecessary features.</p>
                    <p>Whether you need a mobile app, a custom internal tool, or an AI-powered system, our goal is to understand exactly what your business needs and build a clean, reliable product that solves your problem.</p>
                </div>
            </div>
        </section>

        <section class="section" id="values">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">WHY CHOOSE US</p>
                    <h2>How We Do Things</h2>
                </div>
                
                <div class="values-grid">
                    <div class="value-card">
                        <h3>Clear Communication</h3>
                        <p>We speak in plain language. You will always know what we are building, why we are building it, and where the project stands.</p>
                    </div>
                    <div class="value-card">
                        <h3>Built for the Requirement</h3>
                        <p>We don't force unnecessary technology into your project. We choose the right tools to solve your specific problem efficiently.</p>
                    </div>
                    <div class="value-card">
                        <h3>Straightforward Pricing</h3>
                        <p>No hidden fees or confusing retainer structures. We provide clear estimates and stick to them.</p>
                    </div>
                    <div class="value-card">
                        <h3>Clean, Maintainable Work</h3>
                        <p>We write clean code and build organized systems so your product is easy to maintain and scale in the future.</p>
                    </div>
                    <div class="value-card">
                        <h3>Support After Delivery</h3>
                        <p>We don't disappear when the project launches. We ensure everything runs smoothly and provide ongoing support if needed.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section-panel" id="services">
            <div class="container split-section">
                <div class="section-heading">
                    <p class="eyebrow">WHAT WE BUILD</p>
                    <h2>Core Services</h2>
                </div>
                <div class="section-copy">
                    <div class="about-category-grid" aria-label="What Velociti Studio builds">
                        <article class="about-category-card">
                            <h3>Mobile Apps</h3>
                        </article>
                        <article class="about-category-card">
                            <h3>Desktop Apps</h3>
                        </article>
                        <article class="about-category-card">
                            <h3>Websites</h3>
                        </article>
                        <article class="about-category-card">
                            <h3>Custom Software</h3>
                        </article>
                        <article class="about-category-card about-category-card-wide">
                            <h3>AI & Automation</h3>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <section class="section" id="technologies">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">TECHNOLOGIES WE WORK WITH</p>
                    <h2>Our Tech Stack</h2>
                </div>

                <div class="technology-categories" aria-label="Technology categories"></div>
            </div>
        </section>

        <section class="section section-panel" id="work">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">OUR WORK</p>
                    <h2>Featured Projects</h2>
                </div>

                <div class="project-grid" data-project-list="featured" aria-label="Featured projects"></div>

                <div class="center-action">
                    <a class="button button-secondary" href="projects.html">See All Projects</a>
                </div>
            </div>
        </section>

        <section class="section" id="process">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">HOW WE WORK</p>
                    <h2>The Project Timeline</h2>
                </div>

                <div class="timeline-grid">
                    <div class="timeline-step">
                        <span class="step-number">01</span>
                        <h3>First Meeting</h3>
                        <p>We understand the idea, goals, and requirements.</p>
                    </div>
                    <div class="timeline-step">
                        <span class="step-number">02</span>
                        <h3>Ideation</h3>
                        <p>We discuss the approach, features, and overall direction.</p>
                    </div>
                    <div class="timeline-step">
                        <span class="step-number">03</span>
                        <h3>Design / Planning</h3>
                        <p>We define the structure and prepare the project before development.</p>
                    </div>
                    <div class="timeline-step">
                        <span class="step-number">04</span>
                        <h3>Development</h3>
                        <p>We build and test the actual product.</p>
                    </div>
                    <div class="timeline-step">
                        <span class="step-number">05</span>
                        <h3>Review & Revisions</h3>
                        <p>We review the result with the client and make the agreed revisions.</p>
                    </div>
                    <div class="timeline-step">
                        <span class="step-number">06</span>
                        <h3>Final Delivery</h3>
                        <p>We deliver the finished project and hand over everything required.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section-panel" id="achievements">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">ACHIEVEMENTS</p>
                    <h2>Awards & Recognition</h2>
                </div>

                <div class="achievement-grid" aria-label="Velociti Studio achievements"></div>
            </div>
        </section>

        <section class="section" id="team">
            <div class="container">
                <div class="section-header">
                    <p class="eyebrow">OUR TEAM</p>
                    <h2>Meet Our Team</h2>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
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
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                                </a>
                            </div>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <section class="section section-panel" id="contact">
            <div class="container">
                <div class="section-header" style="text-align: center; margin: 0 auto 56px;">
                    <p class="eyebrow">START A PROJECT</p>
                    <h2>Turning your vision into our mission.</h2>
                    <p class="section-description" style="margin: 16px auto 0; max-width: 600px; color: var(--text-secondary);">Reach out to us directly or schedule a meeting to discuss your idea.</p>
                </div>

                <div class="contact-split">
                    <div class="contact-card">
                        <h3 style="margin-bottom: 12px; font-size: 1.4rem;">Email Us</h3>
                        <p style="color: var(--text-secondary); margin-bottom: 32px;">Send us an email outlining your project, and we'll get back to you within 24 hours.</p>
                        
                        <div class="email-actions">
                            <a href="mailto:hello@velocitistudio.com" class="button button-primary" style="margin-top: 0;">Send Email</a>
                            <button class="button button-secondary copy-email-btn" data-email="hello@velocitistudio.com" style="margin-top: 0;">Copy Email</button>
                        </div>
                        <p class="copy-feedback" id="copy-feedback" aria-live="polite"></p>

                        <div style="margin-top: 40px; padding-top: 40px; border-top: 1px solid var(--border);">
                            <h3 style="margin-bottom: 12px; font-size: 1.4rem;">Request an Estimate</h3>
                            <p style="color: var(--text-secondary); margin-bottom: 24px;">Fill out our simple inquiry form to get a detailed project estimate.</p>
                            <a href="inquiry.html" class="button button-secondary" style="margin-top: 0;">Go to Inquiry Form</a>
                        </div>
                    </div>

                    <div class="contact-card">
                        <h3 style="margin-bottom: 12px; font-size: 1.4rem;">Schedule a Meeting</h3>
                        <p style="color: var(--text-secondary); margin-bottom: 32px;">Pick a time for a free 30-minute introductory call.</p>
                        
                        <div class="calendar-interface">
                            <div class="calendar-header">
                                <span style="font-weight: 600; font-size: 1.1rem;">October 2026</span>
                                <div style="display: flex; gap: 8px;">
                                    <button class="button button-secondary cal-nav-btn">&lt;</button>
                                    <button class="button button-secondary cal-nav-btn">&gt;</button>
                                </div>
                            </div>
                            <div class="calendar-days-header">
                                <span>Mo</span><span>Tu</span><span>We</span><span>Th</span><span>Fr</span>
                            </div>
                            <div class="calendar-days-grid">
                                <span></span><span></span>
                                <button class="cal-date">1</button>
                                <button class="cal-date active">2</button>
                                <button class="cal-date">3</button>
                            </div>
                            <div class="calendar-slots">
                                <button class="button button-secondary time-slot">10:00 AM</button>
                                <button class="button button-secondary time-slot active">11:30 AM</button>
                                <button class="button button-secondary time-slot">2:00 PM</button>
                            </div>
                            <button class="button button-primary" style="width: 100%; margin-top: 0;">Confirm Booking</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>"""

new_html = html[:start_idx] + new_main + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Updated index.html')
