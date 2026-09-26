import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Append Code Window CSS
code_css = """
/* CODE WINDOW */
.code-window {
    width: 90%;
    max-width: 500px;
    background: #0d101d;
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    overflow: hidden;
    text-align: left;
    z-index: 2;
}
.code-header {
    background: #15192b;
    padding: 12px 16px;
    display: flex;
    gap: 8px;
    border-bottom: 1px solid var(--border);
}
.code-header .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--text-secondary);
    opacity: 0.3;
}
.code-header .dot:nth-child(1) { background: #ff5f56; opacity: 1; }
.code-header .dot:nth-child(2) { background: #ffbd2e; opacity: 1; }
.code-header .dot:nth-child(3) { background: #27c93f; opacity: 1; }
.code-body {
    padding: 24px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9rem;
    line-height: 1.6;
    color: #e2e8f0;
}
.code-keyword { color: #ff641f; font-weight: bold; }
.code-variable { color: #61afef; }
.code-property { color: #e5c07b; }
.code-string { color: #98c379; }
.code-function { color: #c678dd; }
"""

# Redesign Timeline
timeline_css_old = r'/\* TIMELINE SECTION \*/.*?/\* CONTACT & CALENDAR SECTION \*/'
timeline_css_new = """/* TIMELINE SECTION */
.timeline-grid {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-top: 48px;
    max-width: 800px;
}
.timeline-step {
    display: grid;
    grid-template-columns: 80px 1fr;
    gap: 24px;
    position: relative;
    padding-bottom: 48px;
}
.timeline-step:last-child {
    padding-bottom: 0;
}
.timeline-step::before {
    content: '';
    position: absolute;
    top: 50px;
    left: 39px;
    bottom: -10px;
    width: 2px;
    background: var(--border);
}
.timeline-step:last-child::before {
    display: none;
}
.step-number {
    width: 50px;
    height: 50px;
    background: var(--bg-primary);
    border: 2px solid var(--accent);
    color: var(--accent);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1rem;
    z-index: 2;
    position: relative;
    margin: 0 auto;
}
.timeline-content {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 32px;
    transition: border-color 0.2s ease;
}
.timeline-step:hover .timeline-content {
    border-color: rgba(255, 255, 255, 0.2);
}
.timeline-content h3 {
    font-size: 1.25rem;
    margin-bottom: 8px;
    color: var(--text-primary);
}
.timeline-content p {
    color: var(--text-secondary);
    font-size: 1rem;
    line-height: 1.6;
}

/* CONTACT & CALENDAR SECTION */"""

css = re.sub(timeline_css_old, timeline_css_new, css, flags=re.DOTALL)

# Redesign Values (How We Do Things)
values_css_old = r'/\* VALUES SECTION \*/.*?/\* TIMELINE SECTION \*/'
values_css_new = """/* VALUES SECTION */
.values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 32px;
    margin-top: 48px;
}
.value-card {
    padding: 40px 32px;
    border-top: 2px solid var(--border-strong);
    background: linear-gradient(180deg, var(--bg-tertiary) 0%, transparent 100%);
    transition: transform 0.2s ease, border-color 0.2s ease;
}
.value-card:hover {
    border-top-color: var(--accent);
    transform: translateY(-2px);
}
.value-card h3 {
    font-size: 1.2rem;
    margin-bottom: 16px;
    color: var(--text-primary);
}
.value-card p {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
}

/* TIMELINE SECTION */"""

css = re.sub(values_css_old, values_css_new, css, flags=re.DOTALL)

if '/* CODE WINDOW */' in css:
    css = css[:css.find('/* CODE WINDOW */')] + code_css
else:
    css += code_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    num = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    return f'''<div class="timeline-step">
                        <span class="step-number">{num}</span>
                        <div class="timeline-content">
                            <h3>{title}</h3>
                            <p>{desc}</p>
                        </div>
                    </div>'''

html = re.sub(r'<div class="timeline-step">\s*<span class="step-number">(.*?)</span>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</div>', replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
