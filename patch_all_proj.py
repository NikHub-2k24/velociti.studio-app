with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

all_proj = """
    const allProjectsContainer = document.querySelector('[data-project-list="all"]');
    if (allProjectsContainer) {
        allProjectsContainer.className = 'grid grid--projects';
        for(let i=0; i<4; i++) {
            const article = document.createElement('article');
            article.className = 'card card--project';
            article.innerHTML = '<div class="card__thumbnail"><span class="card__placeholder">PREVIEW</span></div><div class="card__content"><span class="card__meta">Archive</span><h3 class="card__title">Archived Project 0' + (i+1) + '</h3><p class="card__desc">Historical project entry demonstrating our long-term engineering capabilities.</p><a href="#" class="card__link">View Work <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a></div>';
            allProjectsContainer.appendChild(article);
        }
    }
"""

if "allProjectsContainer" not in js:
    js = js.replace('});', all_proj + '\n});')
    with open('js/script.js', 'w', encoding='utf-8') as f:
        f.write(js)
