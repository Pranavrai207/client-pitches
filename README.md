# 🗺️ Delhi Local Business Lead Generation Scraper

A **modular, production-ready** Python automation tool that scrapes Google Maps for local business leads in Delhi and exports them to a formatted Excel file.

---

## 📦 Project Files

| File | Purpose |
|------|---------|
| `scraper.py` | Main automation script (all 6 modular functions) |
| `config.py` | Central configuration — queries, delays, output settings |
| `requirements.txt` | Python dependencies |
| `delhi_leads.xlsx` | Output file (generated after run) |
| `scraper.log` | Log file (generated after run) |

---

## 🚀 Quick Setup

### Step 1 — Create a Virtual Environment

```powershell
# Navigate to the project folder
cd "C:\Lead Generation"

# Create a virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# If you see a permissions error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 2 — Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 3 — Install Playwright Browser

```powershell
playwright install chromium
```

---

## ▶️ Running the Scraper

### Default Run (uses `config.py` settings)
```powershell
python scraper.py
```

### Custom Query via CLI
```powershell
# Scrape restaurants, collect 40 results
python scraper.py --query "restaurants in Delhi" --max 40

# Short form
python scraper.py -q "gyms in Delhi" -m 30

# Custom output file
python scraper.py -q "salons in Delhi" -m 35 -o "salon_leads.xlsx"
```

### CLI Arguments

| Argument | Short | Default | Description |
|----------|-------|---------|-------------|
| `--query` | `-q` | From `config.py` | Search term for Google Maps |
| `--max` | `-m` | `50` | Max results to collect |
| `--output` | `-o` | `delhi_leads.xlsx` | Output Excel filename |

---

## ⚙️ Customising `config.py`

```python
# Add more search targets
SEARCH_QUERIES = [
    "cafes in Delhi",
    "restaurants in Delhi",
    "gyms in Delhi",
]

MAX_RESULTS = 50      # How many leads to collect per query
HEADLESS = False      # True = invisible browser (less human-like)
MIN_DELAY = 2.0       # Min seconds between actions
MAX_DELAY = 5.0       # Max seconds between actions
```

---

## 📊 Output — `delhi_leads.xlsx`

Each row is one unique business with these columns:

| Column | Description |
|--------|-------------|
| **Name** | Business name |
| **Rating** | Star rating (e.g. 4.3) |
| **Total Reviews** | Number of reviews |
| **Address** | Street address |
| **Phone** | Contact number |
| **Website** | Website URL (or N/A) |
| **Category** | Business type (e.g. Café) |
| **Maps URL** | Direct Google Maps link |
| **Priority** | 🔥 High / 🟡 Medium / 🟢 Low |

### 🎯 Lead Priority Logic

| Priority | Condition | Why It Matters |
|----------|-----------|---------------|
| 🔥 **High** | No website listed | Perfect target for web design / digital marketing |
| 🟡 **Medium** | Rating ≥ 4.0 with website | Established business, open to extra services |
| 🟢 **Low** | Website + rating < 4.0 | Already present online |

---

## 🛡️ Anti-Detection Strategy

- **Non-headless mode** — real browser, not invisible
- **Random delays** (2–5 seconds) between every action
- **Gradual scrolling** to simulate human reading pace
- **Realistic user-agent** string (Chrome 122, Windows 11)
- **Geolocation set to New Delhi** for local results
- **`navigator.webdriver` flag hidden** via init script

---

## 📈 Scaling to Other Cities

Simply update `config.py`:
```python
SEARCH_QUERIES = [
    "cafes in Mumbai",
    "restaurants in Bangalore",
    "gyms in Hyderabad",
]
OUTPUT_FILE = "india_leads.xlsx"
```

---

## ⚠️ Ethical Usage

- This tool is intended for **responsible, small-scale lead research only**.
- Keep `MAX_RESULTS` conservative (30–50 per run).
- Do not run in rapid succession — respect platform rate limits.
- Review [Google Maps Terms of Service](https://maps.google.com/help/terms_maps/) before use.

---

## 🔧 Troubleshooting

| Issue | Fix |
|-------|-----|
| `playwright install` fails | Run PowerShell as Administrator |
| Script hangs on search | Increase timeout in `perform_search()` |
| 0 results collected | Check if Google changed their selectors; inspect the page manually |
| Excel not saving | Ensure `openpyxl` is installed: `pip install openpyxl` |
| Activation error | Run: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

*Built with ❤️ using Playwright + pandas + openpyxl*
