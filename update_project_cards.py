import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

project_card_css = """
/* REFINED PROJECT CARDS */
.project-card {
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
}
.project-card:hover {
    border-color: transparent !important;
    transform: translateY(-4px) !important;
}
.project-card .card-image-placeholder {
    height: 340px;
    margin-bottom: 24px;
    border: 1px solid var(--border);
    transition: border-color 0.3s ease;
    border-radius: 12px;
}
.project-card:hover .card-image-placeholder {
    border-color: rgba(255, 255, 255, 0.3);
}
.project-card .card-body {
    padding: 0 !important;
}
.project-card .card-tag {
    color: var(--accent);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 12px;
    display: inline-block;
}
.project-card h3 {
    font-size: 1.5rem;
    margin-bottom: 8px;
    color: var(--text-primary);
}
.project-card .project-client {
    font-size: 1rem;
    color: var(--text-secondary);
}
.project-card .project-card-action {
    margin-top: 16px;
}
"""

if '/* REFINED PROJECT CARDS */' in css:
    css = re.sub(r'/\* REFINED PROJECT CARDS \*/.*?(?=\n\n)', project_card_css, css, flags=re.DOTALL)
else:
    # Append before media queries
    media_idx = css.find('@media (max-width: 1040px)')
    css = css[:media_idx] + project_card_css + "\n\n" + css[media_idx:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
