from system.generators.layout_assembler import assemble_layout
import hashlib

def test_uniqueness():
    sample_client = {
        "business_name": "Test Salon",
        "category": "salon",
        "services": [{"service_title": "A", "service_description": "B", "service_image": "C"}],
        "reviews": [{"review_text": "Good", "reviewer_name": "User"}]
    }
    
    outputs = []
    for _ in range(5):
        html, theme = assemble_layout("salon", "layout_1", sample_client)
        outputs.append(html)
    
    # Check if all outputs are unique (at least some variation in colors/fonts)
    hashes = [hashlib.md5(o.encode()).hexdigest() for o in outputs]
    unique_count = len(set(hashes))
    
    print(f"Generated 5 variants. Unique variants: {unique_count}/5")
    if unique_count > 1:
        print("✅ SUCCESS: Uniqueness verified.")
    else:
        print("❌ FAILURE: All outputs were identical.")

if __name__ == "__main__":
    try:
        test_uniqueness()
    except Exception as e:
        print(f"Error during test: {e}")
