import re

filepath = r"c:\Lead Generation\clients\reflections_cafe\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation
old_nav = """        nav {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 1200px;
            background: var(--glass);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            padding: 15px 30px;
            border-radius: 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }"""
new_nav = """        nav {
            position: fixed;
            top: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 1200px;
            background: var(--glass);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            padding: 20px 32px;
            border-radius: 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }"""
html = html.replace(old_nav, new_nav)

# 2. Update CTA Button
old_btn = """        .cta-btn {
            background: var(--primary);
            color: var(--bg);
            padding: 10px 24px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: 0.3s;
        }"""
new_btn = """        .cta-btn {
            background: var(--primary);
            color: var(--bg);
            padding: 12px 24px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            font-size: 16px;
            transition: 0.3s;
        }"""
html = html.replace(old_btn, new_btn)

# 3. Update Hero
old_hero = """        /* --- HERO SECTION --- */
        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('images/hero.png');
            background-size: cover;
            background-position: center;
            padding: 0 20px;
        }

        .hero h1 {
            font-size: clamp(3rem, 10vw, 6rem);
            margin-bottom: 20px;
            line-height: 1;
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 600px;
            margin-bottom: 40px;
        }"""
new_hero = """        /* --- HERO SECTION --- */
        .hero {
            height: 100vh;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-color: var(--bg);
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('images/hero.png');
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), -webkit-image-set(url('images/hero.png') 1x);
            background-size: cover;
            background-position: center;
            padding: 80px 20px;
        }

        .hero h1 {
            font-size: clamp(48px, 6vw, 64px);
            margin-bottom: 24px;
            line-height: 1.1;
        }

        .hero p {
            font-size: 18px;
            color: var(--text-muted);
            max-width: 600px;
            margin-bottom: 40px;
        }"""
html = html.replace(old_hero, new_hero)

# 4. Update Features
old_feat = """        /* --- FEATURES --- */
        .features {
            padding: 100px 5%;
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }

        .feature-card {
            background: var(--surface);
            padding: 40px;
            border-radius: 30px;
            border: 1px solid var(--border);
            transition: 0.4s;
            position: relative;
            overflow: hidden;
        }

        .feature-card:hover {
            background: #222;
            transform: translateY(-10px);
            border-color: var(--primary);
        }

        .feature-card h3 {
            font-size: 1.8rem;
            margin: 20px 0 15px;
        }

        .feature-card p {
            color: var(--text-muted);
        }"""
new_feat = """        /* --- FEATURES --- */
        .features {
            padding: 100px 20px;
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
        }

        .feature-card {
            background: var(--surface);
            padding: 40px;
            border-radius: 30px;
            border: 1px solid var(--border);
            transition: 0.4s;
            position: relative;
            overflow: hidden;
        }

        .feature-card:hover {
            background: #222;
            transform: translateY(-10px);
            border-color: var(--primary);
        }

        .feature-card h3 {
            font-size: 28px;
            margin: 24px 0 16px;
        }

        .feature-card p {
            font-size: 16px;
            color: var(--text-muted);
        }"""
html = html.replace(old_feat, new_feat)

# 5. Update Closing & Footer
old_close = """        /* --- CTA SECTION --- */
        .closing {
            padding: 150px 5%;
            text-align: center;
        }

        .closing h2 {
            font-size: 3.5rem;
            margin-bottom: 24px;
        }

        .closing p {
            color: var(--text-muted);
            margin-bottom: 40px;
        }

        footer {
            padding: 60px 5%;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            color: var(--text-muted);
            font-size: 0.8rem;
        }"""
new_close = """        /* --- CTA SECTION --- */
        .closing {
            padding: 120px 20px;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }

        .closing h2 {
            font-size: 40px;
            margin-bottom: 24px;
        }

        .closing p {
            font-size: 18px;
            color: var(--text-muted);
            margin-bottom: 40px;
        }

        footer {
            padding: 60px 20px;
            max-width: 1200px;
            margin: 0 auto;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            color: var(--text-muted);
            font-size: 16px;
        }"""
html = html.replace(old_close, new_close)

# 6. Inline HTML updates
html = html.replace('<div style="display: flex; gap: 20px;">', '<div style="display: flex; gap: 24px; justify-content: center; align-items: center; width: 100%; max-width: 600px; margin: 0 auto; flex-wrap: wrap;">')
html = html.replace('<a href="#" class="cta-btn" style="padding: 15px 40px;">View Menu</a>', '<a href="#" class="cta-btn" style="padding: 16px 32px; font-size: 18px; display: inline-block;">View Menu</a>')
html = html.replace('<a href="#"\n                style="color: #fff; text-decoration: none; padding: 15px; border: 1px solid var(--border); border-radius: 30px;">Our\n                Gallery</a>', '<a href="#"\n                style="color: #fff; text-decoration: none; padding: 16px 32px; border: 1px solid var(--border); border-radius: 30px; font-size: 18px; display: inline-block;">Our\n                Gallery</a>')

html = html.replace('<a href="#" class="cta-btn" style="padding: 20px 60px; font-size: 1.1rem;">Visit Us Today</a>', '<a href="#" class="cta-btn" style="padding: 16px 48px; font-size: 18px; display: inline-block;">Visit Us Today</a>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated successfully via exact string replacement.")
