import os
import json

try:
    from system.generators.theme_engine import get_random_theme
except ImportError:
    from theme_engine import get_random_theme

def generate_style_block(theme):
    return f"""
    <style>
        :root {{
            --primary: {theme['color_primary']};
            --secondary: {theme['color_secondary']};
            --accent: {theme['color_accent']};
            --text-dark: {theme['color_text']};
            --bg-light: {theme['color_bg']};
            --font-heading: {theme['font_heading']};
            --font-body: {theme['font_body']};
        }}
        
        body {{
            font-family: var(--font-body);
            background: var(--bg-light);
            color: var(--text-dark);
        }}
        h1, h2, h3, h4 {{ font-family: var(--font-heading); }}
    </style>
    """

def load_component(name):
    base_path = "system/components"
    # Search in components and sub_templates
    search_paths = [base_path, os.path.join(base_path, "sub_templates")]
    
    for path in search_paths:
        for root, dirs, files in os.walk(path):
            filename = f"{name}.html"
            if filename in files:
                with open(os.path.join(root, filename), "r") as f:
                    return f.read()
    return f"<!-- Component {name} not found -->"

def inject_list(template_name, data_list):
    template = load_component(template_name)
    result = ""
    for item in data_list:
        item_html = template
        for key, value in item.items():
            item_html = item_html.replace("{{" + key + "}}", str(value))
        result += item_html + "\n"
    return result

def assemble_layout(category, layout_id, client_data):
    # Load layout definitions
    layout_file = f"system/layouts/{category}-layouts.json"
    with open(layout_file, "r") as f:
        layouts = json.load(f)
    
    components_to_use = layouts[layout_id]
    
    # 1. Generate Dynamic Theme
    theme = get_random_theme(category)
    
    # 2. Handle List Injections (Services, Reviews)
    if "services" in client_data:
        client_data["services_items"] = inject_list("service-item", client_data["services"])
    if "reviews" in client_data:
        client_data["review_items"] = inject_list("review-item", client_data["reviews"])

    full_html = generate_style_block(theme) + "\n"
    
    in_main = False
    for comp_name in components_to_use:
        content = load_component(comp_name)
        
        # Determine if we should be inside <main>
        is_header_footer = any(x in comp_name for x in ["navbar", "footer"])
        
        if not is_header_footer and not in_main:
            full_html += "<main>\n"
            in_main = True
        elif is_header_footer and in_main:
            full_html += "</main>\n"
            in_main = False

        # Inject client data + theme tokens
        all_data = {**client_data, **theme}
        for key, value in all_data.items():
            placeholder = "{{" + key + "}}"
            content = content.replace(placeholder, str(value))
            
        full_html += content + "\n"
    
    if in_main:
        full_html += "</main>\n"
        
    return full_html, theme

# Example usage
if __name__ == "__main__":
    sample_client = {
        "business_name": "Geeta's Luxe Salon",
        "business_phone": "+91 98765 43210",
        "cta_text_nav": "Book Now",
        "hero_headline": "Redefine Your Beauty",
        "hero_subheadline": "Luxury hair and skin care treatments in the heart of Delhi.",
        "hero_image_webp": "assets/images/hero.webp",
        "hero_image_fallback": "assets/images/hero.jpg",
        "cta_text_hero_primary": "Schedule Now",
        "cta_text_hero_secondary": "Visit Us",
        "google_maps_link": "https://maps.google.com",
        "about_headline": "Experience True Luxury",
        "about_description_1": "Geeta's Luxe Salon offers world-class beauty services.",
        "about_description_2": "Our stylists are trained by international experts.",
        "cta_text_about": "Learn More",
        "about_image_webp": "assets/images/about.webp",
        "about_image_fallback": "assets/images/about.jpg",
        "services_headline": "Our Premium Services",
        "services_subheadline": "We provide a wide range of services for your needs.",
        "services": [
            {"service_title": "Hair cut", "service_description": "Customized haircuts for everyone.", "service_image": "assets/images/service1.webp"},
            {"service_title": "Facial", "service_description": "Relaxing facial treatments.", "service_image": "assets/images/service2.webp"}
        ],
        "reviews": [
            {"review_text": "Amazing service!", "reviewer_name": "Priyanka"},
            {"review_text": "Highly recommended.", "reviewer_name": "Rahul"}
        ],
        "cta_headline": "Ready for a Change?",
        "cta_subheadline": "Join our 1000+ happy clients.",
        "cta_button_text": "Get Started"
    }
    
    # Simple test run
    # result = assemble_layout("salon", "layout_1", sample_client)
    # print(result[:500]) # Print first 500 chars
    print("Assembler logic initialized.")
