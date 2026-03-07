import os
from system.generators.layout_assembler import assemble_layout

def final_audit():
    sample_client = {
        "business_name": "Audit Biz",
        "category": "salon",
        "services": [{"service_title": "A", "service_description": "B", "service_image": "C"}],
        "reviews": [{"review_text": "Good", "reviewer_name": "User"}]
    }
    
    html, _ = assemble_layout("salon", "layout_1", sample_client)
    
    # 1. Check for AI signature (Prohibited)
    prohibited = ["Built by Antigravity", "by AI", "Crafted with Precision by AI"]
    for p in prohibited:
        if p in html:
            print(f"❌ FAIL: Prohibited string '{p}' found.")
            return

    # 2. Check for <main> wrapping
    if "<main>" not in html or "</main>" not in html:
        print("❌ FAIL: <main> tag missing.")
        return

    # 3. Check for mandatory order (Hero -> About -> Services)
    hero_pos = html.find('id="hero"')
    about_pos = html.find('id="about"')
    services_pos = html.find('id="services"')
    
    if hero_pos < about_pos < services_pos:
        print("✅ SUCCESS: Structure Audit Passed.")
    else:
        print("❌ FAIL: Structural sequence is incorrect.")

if __name__ == "__main__":
    final_audit()
