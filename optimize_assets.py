import os
import sys
from PIL import Image

if len(sys.argv) < 2:
    print("Usage: python optimize_assets.py <directory>")
    sys.exit(1)

target_dir = sys.argv[1]

if not os.path.exists(target_dir):
    print(f"Directory {target_dir} does not exist.")
    sys.exit(1)

sizes = [480, 800, 1200, 1920]

# Find all PNGs in the directory
images = [f for f in os.listdir(target_dir) if f.endswith('.png')]

for filename in images:
    path = os.path.join(target_dir, filename)
    name = os.path.splitext(filename)[0]
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            # Create base version
            img.save(os.path.join(target_dir, f"{name}.webp"), "WEBP", quality=80)
            
            for size in sizes:
                # Calculate new height maintaining aspect ratio
                ratio = size / float(img.width)
                new_height = int((float(img.height) * float(ratio)))
                resized_img = img.resize((size, new_height), Image.Resampling.LANCZOS)
                output_path = os.path.join(target_dir, f"{name}-{size}.webp")
                resized_img.save(output_path, "WEBP", quality=80)
                print(f"Saved {output_path}")
                
    except Exception as e:
        print(f"Error processing {filename}: {e}")
