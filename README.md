# 🗺️ Delhi Local Business Lead Generation Scraper

A **modular, production-ready** Python automation tool that scrapes Google Maps for local business leads in Delhi and exports them to a formatted Excel file.

---

| Folder/File | Purpose |
|------|---------|
| `main.py` | **Central Orchestrator** (Run all commands from here) |
| `scripts/` | Implementation logic (Scraper, Filter, Deploy, etc.) |
| `config/` | Central configuration (`config.py`) |
| `data/` | Lead databases (`.xlsx` files) |
| `logs/` | System operation logs (`scraper.log`) |
| `outputs/` | Generated reports and transient outputs |
| `clients/` | **The Deal Hub** (Premium HTML/CSS pitches) |
| `ai_memory/` | Design standards and pitch strategy documents |
| `requirements.txt` | Python dependencies |

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

### Unified Pipeline (Recommended)
```powershell
# Scrape + Filter + Organize (The 10/10 way)
python main.py all
```

### Individual Commands via Orchestrator
```powershell
# Scrape specific niche
python main.py scrape --query "salons in Delhi" --max 40

# Filter results
python main.py filter

# Generate pitch
python main.py pitch --client "Bloom Salon"

# Optimize assets
python main.py optimize --client "bloom_salon"

# Deploy to GitHub
python main.py deploy --client "bloom_salon"
```

### CLI Arguments (`main.py`)

| Argument | Short | Target | Description |
|----------|-------|--------|-------------|
| `--query` | `-q` | `scrape` | Search term for Google Maps |
| `--max` | `-m` | `scrape` | Max results per query |
| `--client` | `-c` | `pitch/deploy` | Client name or folder name |

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

## 💎 Premium Pitch Generation Protocol (10/10 Quality)

To maintain a premium standard for high-ticket clients, follow this manual-crafting workflow:

### 1. Lead Selection
Use `python filter_leads.py` to identify high-priority targets. Focus on businesses with high ratings but no digital presence.

### 2. Bespoke Asset Creation
- Create client folder: `clients/[business-slug]/assets/images/`.
- Generate custom AI/Stock images tailored to the business's niche and vibe.
- **Optimize**: Run `python optimize_assets.py "clients/[business-slug]/assets/images"` to ensure 10/10 loading speed (WebP).

### 3. UI/UX Construction
- Develop `index.html` and `styles.css` following `design_standards.md`.
- Ensure unique typography pairings and premium color palettes for every client.
- Implement LocalBusiness JSON-LD for SEO.

### 4. Deployment & Audit
- **Deploy**: Run `python deploy.py [business-slug]`.
- **Verify**: Audit the mobile responsiveness and layout alignment on all devices.

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
