import random

# Professional Font Pairings
FONT_PAIRS = [
    {"heading": "'Playfair Display', serif", "body": "'Inter', sans-serif"},
    {"heading": "'Montserrat', sans-serif", "body": "'Open Sans', sans-serif"},
    {"heading": "'Outfit', sans-serif", "body": "'Roboto', sans-serif"},
    {"heading": "'Cormorant Garamond', serif", "body": "'Lato', sans-serif"},
    {"heading": "'Lora', serif", "body": "'Nunito', sans-serif"},
    {"heading": "'Bebas Neue', display", "body": "'Rubik', sans-serif"}
]

# Color Presets per Category
CATEGORY_PRESETS = {
    "salon": {
        "base_primary": "#E91E63", # Pink
        "styles": ["Luxe", "Modern", "Classic"]
    },
    "dermatologist": {
        "base_primary": "#007BFF", # Blue
        "styles": ["Clinical", "Soft", "Premium"]
    },
    "luxury-cafe": {
        "base_primary": "#6F4E37", # Brown
        "styles": ["Warm", "Minimal", "Gold"]
    },
    "boutique-hotel": {
        "base_primary": "#1A237E", # Navy
        "styles": ["Royal", "Contemporary", "Vintage"]
    },
    "yoga-studio": {
        "base_primary": "#673AB7", # Purple
        "styles": ["Zen", "Natural", "Airy"]
    }
}

def generate_brand_colors(category):
    preset = CATEGORY_PRESETS.get(category, {"base_primary": "#333333"})
    primary = preset["base_primary"]
    
    # Simple logic to vary the secondary color slightly
    # In a real scenario, we could use HSL to shift hue/lightness
    rand_val = random.randint(0, 100)
    if rand_val < 33:
        secondary = "#D4AF37" # Gold
        accent = "#212121"
    elif rand_val < 66:
        secondary = "#F8F9FA" # Light Gray
        accent = primary
    else:
        secondary = primary
        accent = "#FFFFFF"

    return {
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "text_dark": "#1A1A1A",
        "bg_light": "#FDFDFD"
    }

def get_random_theme(category):
    fonts = random.choice(FONT_PAIRS)
    colors = generate_brand_colors(category)
    style_name = random.choice(CATEGORY_PRESETS.get(category, {"styles": ["Standard"]})["styles"])
    
    return {
        "font_heading": fonts["heading"],
        "font_body": fonts["body"],
        "color_primary": colors["primary"],
        "color_secondary": colors["secondary"],
        "color_accent": colors["accent"],
        "color_text": colors["text_dark"],
        "color_bg": colors["bg_light"],
        "style_preset": style_name
    }

if __name__ == "__main__":
    print(get_random_theme("salon"))
