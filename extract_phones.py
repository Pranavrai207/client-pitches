import pandas as pd
import os

def find_phones():
    clean_leads_path = r'c:\Users\conta\Client-pitches\client-pitches\data\delhi_leads_clean.xlsx'
    master_path = r'c:\Users\conta\Client-pitches\client-pitches\Client_Pitches_Master.xlsx'
    
    targets = [
        'Amba Traders', 'Ambica', 'Bloom Salon', 'Dance with Shubham', 
        'Fitness Zone', 'Gopal Sindhi', 'Images Unisex', 'Impresario', 
        'J Salon', 'Neon Genesis', 'Posh by Charms', 'Reflections Cafe', 
        'Saviour Physio', 'Golden Spoon'
    ]
    
    results = {}
    
    if os.path.exists(clean_leads_path):
        df1 = pd.read_excel(clean_leads_path)
        for t in targets:
            match = df1[df1['Name'].str.contains(t, case=False, na=False)]
            if not match.empty:
                results[t] = match.iloc[0]['Phone']
                
    if os.path.exists(master_path):
        df2 = pd.read_excel(master_path)
        # Check column names for master df
        name_col = 'Client Name' if 'Client Name' in df2.columns else 'Name'
        phone_col = 'Phone' if 'Phone' in df2.columns else 'Phone Number'
        
        for t in targets:
            if t not in results or pd.isna(results[t]):
                match = df2[df2[name_col].str.contains(t, case=False, na=False)]
                if not match.empty:
                    results[t] = match.iloc[0][phone_col]

    print("--- FINAL CONTACTS ---")
    for t, phone in results.items():
        print(f"{t}: {phone}")

if __name__ == '__main__':
    find_phones()
