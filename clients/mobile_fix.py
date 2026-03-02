import os

css_to_inject = """
/* --- UNIVERSAL MOBILE RESPONSIVENESS FIX --- */
@media (max-width: 768px) {
    /* Fix Navigation Position */
    nav {
        width: 100% !important;
        left: 0 !important;
        top: 0 !important;
        transform: none !important;
        border-radius: 0 !important;
        padding: 15px 20px !important;
        position: fixed !important;
        border: none !important;
        border-bottom: 1px solid var(--border, rgba(255,255,255,0.1)) !important;
        box-sizing: border-box !important;
    }
    .nav-links {
        top: 60px !important;
        border-radius: 0 0 20px 20px !important;
        width: 100% !important;
        left: 0 !important;
        box-sizing: border-box !important;
    }
    
    /* Aggressively scale down typography */
    h1 { font-size: 2.2rem !important; line-height: 1.2 !important; word-wrap: break-word !important; }
    h2, .section-title h2 { font-size: 1.8rem !important; line-height: 1.3 !important; }
    h3 { font-size: 1.5rem !important; line-height: 1.4 !important; }
    p { font-size: 0.95rem !important; line-height: 1.5 !important; }
    
    /* Fix Hero sizing and image cropping */
    .hero, header {
        min-height: 100vh !important;
        height: auto !important;
        background-attachment: scroll !important; /* fixes iOS bug */
        background-position: center center !important;
        background-size: cover !important;
        padding-top: 100px !important;
        padding-bottom: 60px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        box-sizing: border-box !important;
    }
    
    /* Fix sections and internal paddings */
    section {
        padding: 60px 20px !important;
        box-sizing: border-box !important;
        width: 100% !important;
    }
    
    /* Fix flex rows that should be columns on mobile */
    .grid, .features, .stats-grid, .footer-grid, .location-container, .contact-container, .services-grid, .portfolio-grid {
        gap: 20px !important;
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
    }

    .service-card, .portfolio-item, .stat-item, .contact-info, .contact-form, .review-box, .pricing-card {
        width: 100% !important;
        box-sizing: border-box !important;
        margin: 0 !important;
    }
    
    /* Prevent form outbounds */
    form {
        width: 100% !important;
        padding: 0 !important;
        box-sizing: border-box !important;
    }
    input, select, textarea {
        width: 100% !important;
        box-sizing: border-box !important;
    }
    .form-row {
        display: flex !important;
        flex-direction: column !important;
        gap: 15px !important;
    }
    
    /* Button formatting */
    .btn, .cta-btn, button {
        padding: 12px 24px !important;
        font-size: 1rem !important;
        width: 100% !important;
        text-align: center !important;
        box-sizing: border-box !important;
        margin-top: 10px !important;
        display: block !important;
    }
    
    /* Global fixes for horizontal scroll */
    html, body {
        max-width: 100vw !important;
        overflow-x: hidden !important;
    }
}
</style>
"""

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Binary read/write to avoid CRLF slicing corruption
            with open(filepath, 'rb') as f:
                content = f.read().decode('utf-8')
                
            if '/* --- UNIVERSAL MOBILE RESPONSIVENESS FIX --- */' in content:
                # We won't re-inject if it's already there
                continue
                
            parts = content.rsplit('</style>', 1)
            if len(parts) == 2:
                new_content = parts[0] + css_to_inject + parts[1]
                with open(filepath, 'wb') as f:
                    f.write(new_content.encode('utf-8'))
                count += 1
                
print(f"Applied Universal Mobile Overrides to {count} files.")
