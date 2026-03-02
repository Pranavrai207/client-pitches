import os

old_css = """    /* Button formatting */
    .btn, .cta-btn, button {
        padding: 12px 24px !important;
        font-size: 1rem !important;
        width: 100% !important;
        text-align: center !important;
        box-sizing: border-box !important;
        margin-top: 10px !important;
        display: block !important;
    }"""

new_css = """    /* Button formatting - Fixed from massive size */
    .btn, .cta-btn, button {
        padding: 14px 28px !important;
        font-size: 16px !important;
        width: auto !important;
        max-width: 100% !important;
        text-align: center !important;
        box-sizing: border-box !important;
        margin-top: 10px !important;
        display: inline-block !important;
        min-height: 48px !important; /* Thumb-friendly mobile standard */
        border-radius: 50px !important; /* Premium feel */
    }"""

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8')
                
            if old_css in content:
                content = content.replace(old_css, new_css)
                with open(filepath, 'wb') as f:
                    f.write(content.encode('utf-8'))
                count += 1
                
print(f"Fixed buttons in {count} files.")
