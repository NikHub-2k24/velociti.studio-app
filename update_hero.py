import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_hero_visual = '''<div class="hero-visual" aria-label="Code editor graphic">
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
                </div>'''

# Replace the hero visual div
html = re.sub(r'<div class="hero-visual" aria-label="Hero visual graphic">.*?</div>', new_hero_visual, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
