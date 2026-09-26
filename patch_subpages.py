import re

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

all_projects_js = """
    // Render All Projects on projects.html
    const allProjectsContainer = document.querySelector('[data-project-list="all"]');
    if (allProjectsContainer) {
        allProjectsContainer.className = "case-study-list";
        
        const allProjects = [
            {
                title: "Fintech Dashboard API",
                client: "Nexus Financial",
                category: "Web & API",
                description: "A secure, high-performance financial dashboard handling real-time transaction processing and analytics for enterprise clients.",
                link: "#"
            },
            {
                title: "Logistics Optimization Engine",
                client: "CargoStream",
                category: "AI & Automation",
                description: "Machine learning powered route optimization system that reduced delivery delays by 34% and automated driver dispatching.",
                link: "#"
            },
            {
                title: "HealthTrack Mobile App",
                client: "Vitality Inc",
                category: "Mobile",
                description: "Cross-platform mobile application for patient health tracking and remote monitoring integrated with wearable devices.",
                link: "#"
            },
            {
                title: "E-Commerce Microservices",
                client: "RetailGlobal",
                category: "Cloud",
                description: "Migrated a legacy monolith to a scalable microservices architecture, handling 10k+ concurrent users during peak sales.",
                link: "#"
            }
        ];

        allProjects.forEach(project => {
            const article = document.createElement("article");
            article.className = "case-study";

            article.innerHTML = `
                <div class="cs-visual">
                    <span class="cs-visual-placeholder">PROJECT PREVIEW</span>
                </div>
                <div class="cs-content">
                    <div class="cs-meta">
                        <span class="cs-tag">${project.category}</span>
                    </div>
                    <h3 class="cs-title">${project.title}</h3>
                    <p class="cs-desc">${project.description}</p>
                    <a href="${project.link}" class="cs-link">
                        Read Case Study
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>
            `;
            allProjectsContainer.appendChild(article);
        });
    }
"""

js = js.replace('});', all_projects_js + '\n});')

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update inquiry.html CSS
with open('inquiry.html', 'r', encoding='utf-8') as f:
    inq = f.read()

inq_css = """
        .inquiry-page-section {
            min-height: calc(100vh - 200px);
            display: flex;
            align-items: center;
        }
        .inquiry-form-container {
            max-width: 600px;
            margin: 0 auto;
            background: var(--bg-secondary);
            padding: 48px;
            border-radius: 20px;
            border: 1px solid var(--border);
        }
        .form-group { margin-bottom: 24px; }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-secondary);
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 16px;
            background: var(--bg-tertiary);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-primary);
            font-family: inherit;
            font-size: 1rem;
            transition: border-color 0.2s ease;
        }
        .form-group input:focus, .form-group textarea:focus {
            outline: none;
            border-color: var(--accent);
        }
        .form-group textarea { resize: vertical; min-height: 120px; }
        .form-actions { margin-top: 32px; }
"""

inq = re.sub(r'<style>.*?</style>', f'<style>{inq_css}</style>', inq, flags=re.DOTALL)
inq = inq.replace('section-header', 'section-header-center')
inq = inq.replace('class="section inquiry-page-section"', 'class="section inquiry-page-section section-darker"')

with open('inquiry.html', 'w', encoding='utf-8') as f:
    f.write(inq)


# Update projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    proj = f.read()

proj = proj.replace('section-header', 'section-header-center')
proj = proj.replace('class="section projects-page-section"', 'class="section section-darker"')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(proj)
