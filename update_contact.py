import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_contact = """<section class="section section-panel" id="contact">
            <div class="container">
                <div class="section-header" style="text-align: center; margin: 0 auto 64px;">
                    <p class="eyebrow">START A PROJECT</p>
                    <h2>Turning your vision into our mission.</h2>
                    <p class="section-description" style="margin: 16px auto 0; max-width: 600px; color: var(--text-secondary);">Reach out to us directly or schedule a meeting to discuss your idea.</p>
                </div>

                <div class="contact-grid">
                    <div class="contact-card primary-contact">
                        <h3>Schedule a Meeting</h3>
                        <p>Pick a time for a free 30-minute introductory call.</p>
                        
                        <!-- Cal.com / Calendly Ready Embed Container -->
                        <div class="booking-container">
                            <div class="booking-placeholder">
                                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 16px; color: var(--accent);"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                                <h4>Book a Call</h4>
                                <p>Ready to connect to Cal.com or Calendly.</p>
                                <button class="button button-primary" style="margin-top: 24px; width: 100%;">Connect Calendar</button>
                            </div>
                        </div>
                    </div>

                    <div class="contact-actions">
                        <div class="contact-card">
                            <h3>Email Us</h3>
                            <p>Send us an email outlining your project, and we'll get back to you within 24 hours.</p>
                            
                            <div class="email-actions">
                                <a href="mailto:velocitistudio@gmail.com" class="button button-primary">Send Email</a>
                                <button class="button button-secondary copy-email-btn" data-email="velocitistudio@gmail.com">Copy Email</button>
                            </div>
                            <p class="copy-feedback" id="copy-feedback" aria-live="polite"></p>
                        </div>

                        <div class="contact-card">
                            <h3>Request an Estimate</h3>
                            <p>Fill out our simple inquiry form to get a detailed project estimate.</p>
                            <a href="inquiry.html" class="button button-secondary" style="margin-top: 16px;">Go to Inquiry Form</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Replace the contact section
html = re.sub(r'<section class="section section-panel" id="contact">.*?</section>', new_contact, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
