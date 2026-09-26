import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

contact_css = """
/* CONTACT SECTION */
.contact-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
    gap: 32px;
}
.contact-actions {
    display: flex;
    flex-direction: column;
    gap: 32px;
}
.contact-card {
    padding: 48px;
    border: 1px solid var(--border);
    border-radius: 16px;
    background: var(--bg-tertiary);
    display: flex;
    flex-direction: column;
}
.contact-card h3 {
    font-size: 1.4rem;
    margin-bottom: 12px;
}
.contact-card p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-bottom: 32px;
    line-height: 1.6;
}
.primary-contact {
    background: linear-gradient(145deg, var(--bg-tertiary), var(--bg-secondary));
}
.booking-container {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 300px;
    background: var(--bg-primary);
    border: 1px dashed var(--border-strong);
    border-radius: 12px;
    padding: 32px;
    text-align: center;
}
.booking-placeholder h4 {
    font-size: 1.1rem;
    margin-bottom: 8px;
    color: var(--text-primary);
}
.booking-placeholder p {
    margin-bottom: 0;
    font-size: 0.9rem;
}
.email-actions {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: auto;
}
.email-actions .button {
    margin-top: 0;
}
.copy-feedback {
    margin-top: 16px;
    color: var(--accent);
    font-size: 0.85rem;
    font-weight: 600;
    min-height: 20px;
}
"""

css = re.sub(r'/\* CONTACT & CALENDAR SECTION \*/.*?(?=/\* TEAM LINKS \*/)', contact_css, css, flags=re.DOTALL)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
