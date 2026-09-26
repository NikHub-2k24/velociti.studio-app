import os

# 1. Restore style.css from rewrite_css.py
os.system("python rewrite_css.py")

# 2. Restore script.js from rewrite_js.py
os.system("python rewrite_js.py")

# 3. Restore index.html by taking header/footer from projects.html and <main> from rewrite_html.py
with open('projects.html', 'r', encoding='utf-8') as f:
    proj_html = f.read()

header = proj_html[:proj_html.find('<main>')]
footer = proj_html[proj_html.find('</main>') + len('</main>'):]

# Extract new_main from rewrite_html.py
with open('rewrite_html.py', 'r', encoding='utf-8') as f:
    rewrite_code = f.read()

# rewrite_html.py contains `new_main = """<main>..."""`
# We can just execute it in a restricted namespace to get the string
namespace = {}
# We don't want to actually run the file overwrite in rewrite_html.py, we just want `new_main`.
# So we'll parse the string.
start_str = 'new_main = """<main>'
end_str = '    </main>"""'
if start_str in rewrite_code and end_str in rewrite_code:
    main_start = rewrite_code.find(start_str) + len('new_main = """')
    main_end = rewrite_code.find(end_str) + len('    </main>')
    new_main = rewrite_code[main_start:main_end]
else:
    # fallback
    main_start = rewrite_code.find('<main>')
    main_end = rewrite_code.find('</main>') + len('</main>')
    new_main = rewrite_code[main_start:main_end]

restored_index = header + new_main + footer

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(restored_index)

# 4. Re-patch subpages so projects.html and inquiry.html get the right CSS patches
os.system("python patch_subpages.py")
