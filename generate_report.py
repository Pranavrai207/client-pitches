import os
import re
import json
from openpyxl import Workbook

def extract_data(html_content, folder_name):
    data = {
        "Name": folder_name.replace('_', ' ').title(),
        "Category": "N/A",
        "Rating": "N/A",
        "Reviews": "N/A",
        "Address": "N/A",
        "Phone": "N/A",
        "Live URL": f"https://pranavrai207.github.io/client-pitches/clients/{folder_name}/"
    }
    
    # Try to find JSON-LD
    json_ld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html_content, re.DOTALL)
    if json_ld_match:
        try:
            js = json.loads(json_ld_match.group(1).strip())
            data["Name"] = js.get("name", data["Name"])
            data["Category"] = js.get("@type", "N/A")
            if js.get("@type") == "Restaurant":
                data["Category"] = js.get("servesCuisine", "Restaurant")
            
            data["Phone"] = js.get("telephone", "N/A")
            
            addr = js.get("address", {})
            if isinstance(addr, dict):
                data["Address"] = f"{addr.get('streetAddress', '')}, {addr.get('addressLocality', '')}".strip(", ")
            
            rating = js.get("aggregateRating", {})
            if isinstance(rating, dict):
                data["Rating"] = rating.get("ratingValue", "N/A")
                data["Reviews"] = rating.get("reviewCount", "N/A")
        except:
            pass
            
    return data

def main():
    clients_dir = r"c:\Lead Generation\clients"
    report_data = []
    
    if not os.path.exists(clients_dir):
        print(f"Directory {clients_dir} not found.")
        return

    for folder in os.listdir(clients_dir):
        folder_path = os.path.join(clients_dir, folder)
        if os.path.isdir(folder_path):
            index_path = os.path.join(folder_path, "index.html")
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    report_data.append(extract_data(content, folder))

    # Create Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Client Websites Report"
    
    headers = ["Name", "Category", "Rating", "Reviews", "Address", "Phone", "Live URL"]
    ws.append(headers)
    
    for row in report_data:
        ws.append([row[h] for h in headers])
        
    output_file = r"c:\Lead Generation\client_websites_report.xlsx"
    wb.save(output_file)
    print(f"SUCCESS: Report saved to {output_file}")

if __name__ == "__main__":
    main()
