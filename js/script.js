
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
                primaryNav.style.background = "rgba(10, 13, 20, 0.95)";
                primaryNav.style.flexDirection = "column";
                primaryNav.style.padding = "24px";
                primaryNav.style.borderBottom = "1px solid var(--border)";
            } else {
                primaryNav.style.display = "none";
            }
        
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

});
    
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

});

    // Booking UI Interaction
    const timeBtns = document.querySelectorAll('.time-btn');
    const confirmBtn = document.querySelector('.confirm-booking-btn');
    const bookingUI = document.getElementById('booking-ui');
    const bookingSuccess = document.getElementById('booking-success');
    const resetBtn = document.querySelector('.reset-booking-btn');
    const days = document.querySelectorAll('.booking-calendar .day:not(:empty)');

    timeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            timeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        
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

});
    
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

});

    days.forEach(day => {
        day.addEventListener('click', () => {
            days.forEach(d => d.classList.remove('active'));
            day.classList.add('active');
            
            // Randomize times just to simulate interaction
            const timeOptions = ['9:00 AM', '10:30 AM', '1:00 PM', '4:00 PM', '5:30 PM'];
            timeBtns.forEach((btn, index) => {
                btn.textContent = timeOptions[(index + parseInt(day.textContent)) % timeOptions.length];
                btn.classList.remove('active');
            
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

});
            if(timeBtns.length > 0) timeBtns[0].classList.add('active');
        
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

});
    
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

});

    if (confirmBtn && bookingUI && bookingSuccess) {
        confirmBtn.addEventListener('click', () => {
            confirmBtn.textContent = 'Confirming...';
            setTimeout(() => {
                bookingUI.style.display = 'none';
                bookingSuccess.style.display = 'block';
                confirmBtn.textContent = 'Confirm Time';
            }, 800);
        
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

});
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            bookingSuccess.style.display = 'none';
            bookingUI.style.display = 'flex';
        
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

});
    }

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
            projectsContainer.appendChild(article);
        
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

});
    }

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

});
