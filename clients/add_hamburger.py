import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has hamburger menu toggle
    if 'id="mobile-menu"' in content or 'menu-toggle' in content:
        return

    # Check if there's a nav and nav-links
    if '<nav>' not in content and '<nav class=' not in content:
        return
    if 'nav-links' not in content:
        return

    # 1. Inject CSS for hamburger toggle before the 768px media query or somewhere safe in <style>
    css_injection = """
        /* Hamburger Menu */
        .menu-toggle {
            display: none;
            flex-direction: column;
            cursor: pointer;
            z-index: 1001;
        }

        .bar {
            width: 25px;
            height: 3px;
            background-color: var(--text-main, #fff); /* Fallback to white if var not defined */
            margin: 4px 0;
            transition: 0.4s;
            border-radius: 3px;
        }
"""
    
    # Try finding the media query for 768px to inject inside it
    mq_pattern = re.compile(r'@media\s*\(\s*max-width\s*:\s*768px\s*\)\s*\{', re.IGNORECASE)
    
    match = mq_pattern.search(content)
    if match:
        mq_start = match.start()
        # Insert general CSS right before the media query
        content = content[:mq_start] + css_injection + "\n        " + content[mq_start:]
        
        # Now find where .nav-links is hidden in the media query and replace it with the active state logic
        # Some padding diffs might exist, but we will just inject the required CSS inside the media query
        
        mq_injection = """
            .menu-toggle {
                display: flex;
            }

            .nav-links {
                display: none !important; /* Override standard hiding */
                flex-direction: column;
                position: absolute;
                top: 80px;
                left: 0;
                width: 100%;
                background: rgba(26, 26, 26, 0.95);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid var(--border, rgba(255,255,255,0.1));
                padding: 20px 0;
                text-align: center;
                gap: 15px;
            }

            .nav-links.active {
                display: flex !important;
            }
"""
        # Insert inside media query (right after the '{')
        new_mq_start = match.start() + len(css_injection) + 9 # account for injected css offset
        # Let's just find the media query again to be safe
        match2 = mq_pattern.search(content)
        if match2:
            insert_pos = match2.end()
            content = content[:insert_pos] + mq_injection + content[insert_pos:]

    # 2. Inject HTML for the hamburger icon inside <nav>
    # Find the logo div to inject after it, or just inject after <nav>
    nav_pattern = re.compile(r'(<nav[^>]*>.*?(?:<div[^>]*logo[^>]*>.*?</div>|<a[^>]*logo[^>]*>.*?</a>|<img[^>]*logo[^>]*>))', re.IGNORECASE | re.DOTALL)
    
    hamburger_html = """
        <div class="menu-toggle" id="mobile-menu">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </div>"""
    
    match3 = nav_pattern.search(content)
    if match3:
        insert_pos = match3.end()
        content = content[:insert_pos] + hamburger_html + content[insert_pos:]
    else:
        # Fallback: just insert after <nav>
        content = content.replace('<nav>', '<nav>' + hamburger_html, 1)

    # 3. Inject JS script before </body>
    js_injection = """
    <script>
        const mobileMenu = document.getElementById('mobile-menu');
        const navLinks = document.querySelector('.nav-links');

        if (mobileMenu && navLinks) {
            mobileMenu.addEventListener('click', () => {
                navLinks.classList.toggle('active');
            });
        }
    </script>
</body>"""
    content = content.replace('</body>', js_injection)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

import glob

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Skip reflections_cafe as we already did it manually
            if 'reflections_cafe' in filepath:
                continue
            try:
                process_file(filepath)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

