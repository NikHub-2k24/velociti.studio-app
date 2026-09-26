js_code = """
document.addEventListener("DOMContentLoaded", () => {
    // Current Year
    const yearEl = document.getElementById("current-year");
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Mobile Menu Toggle
    const menuToggle = document.querySelector(".menu-toggle");
    const primaryNav = document.getElementById("primary-navigation");

    if (menuToggle && primaryNav) {
        menuToggle.addEventListener("click", () => {
            const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
            menuToggle.setAttribute("aria-expanded", !isExpanded);
            
            if (!isExpanded) {
                primaryNav.style.display = "flex";
                primaryNav.style.position = "absolute";
                primaryNav.style.top = "var(--header-height)";
                primaryNav.style.left = "0";
                primaryNav.style.right = "0";
                primaryNav.style.background = "var(--color-bg-base)";
                primaryNav.style.flexDirection = "column";
                primaryNav.style.padding = "var(--space-md)";
                primaryNav.style.borderBottom = "1px solid var(--color-border)";
            } else {
                primaryNav.style.display = "none";
            }
        });
    }

    // Copy Email Functionality
    const copyBtns = document.querySelectorAll('.copy-email-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', async () => {
            const email = btn.getAttribute('data-email');
            const feedbackEl = document.getElementById('copy-feedback');
            
            if (email) {
                try {
                    await navigator.clipboard.writeText(email);
                    if (feedbackEl) {
                        feedbackEl.textContent = 'Email copied to clipboard!';
                        setTimeout(() => {
                            feedbackEl.textContent = '';
                        }, 3000);
                    }
                } catch (err) {
                    console.error('Failed to copy email:', err);
                }
            }
        });
    });

    // Render Projects
    const projectsContainer = document.getElementById("featured-projects-container");
    if (projectsContainer) {
        const featuredProjects = [
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
            }
        ];

        featuredProjects.forEach(project => {
            const article = document.createElement("article");
            article.className = "card card--project";
            article.setAttribute("data-animate", "fade-up");

            article.innerHTML = `
                <div class="card__thumbnail">
                    <span class="card__placeholder">PROJECT PREVIEW</span>
                </div>
                <div class="card__content">
                    <span class="card__meta">${project.category}</span>
                    <h3 class="card__title">${project.title}</h3>
                    <p class="card__desc">${project.description}</p>
                    <a href="${project.link}" class="card__link">
                        View Work
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>
            `;
            projectsContainer.appendChild(article);
        });
    }
});
"""

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js_code)
