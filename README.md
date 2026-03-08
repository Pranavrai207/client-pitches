# 🚀 Client Pitches — Premium Website Generator for Local Businesses
A modular, production-ready system that scrapes Google Maps for local business leads in Delhi, generates premium white-labeled websites, and deploys them to GitHub Pages — all from a single pipeline.

Live Portfolio: [pranavrai207.github.io/client-pitches](https://pranavrai207.github.io/client-pitches/clients/)

## 📁 Project Structure
| Folder/File | Purpose |
|-------------|---------|
| `main.py` | Central Orchestrator — run all commands from here |
| `scripts/` | Implementation logic (Scraper, Filter, Deploy, etc.) |
| `config/` | Central configuration (`config.py`) |
| `data/` | Lead databases (`.xlsx` files) |
| `logs/` | System operation logs (`scraper.log`) |
| `outputs/` | Generated reports and transient outputs |
| `clients/` | The Deal Hub — Premium HTML/CSS client websites |
| `system/` | Theme Engine — generators, tokens, components, layouts |
| `ai_memory/` | Design standards and pitch strategy documents |
| `final_audit.py` | Automated quality audit script |
| `requirements.txt` | Python dependencies |

## 🌐 Live Client Portfolio
All sites are deployed on GitHub Pages and accessible via live links.

### 💇 Salons & Beauty
| Client | Type | Rating | Live Link |
|--------|------|--------|-----------|
| Hairgenix Salon | Multi-page | ⭐ 4.5 | [View Site](https://pranavrai207.github.io/client-pitches/clients/hairgenix_salon/) |
| Images Unisex Saloon | Multi-page | ⭐ 4.2 | [View Site](https://pranavrai207.github.io/client-pitches/clients/images_unisex_saloon/) |
| In Style Hair Salon | Multi-page | ⭐ 4.4 | [View Site](https://pranavrai207.github.io/client-pitches/clients/in_style_hair_salon/) |
| J Salon | Multi-page | ⭐ 4.6 | [View Site](https://pranavrai207.github.io/client-pitches/clients/j_salon/) |
| Posh by Charms | Landing Page | ⭐ 4.7 | [View Site](https://pranavrai207.github.io/client-pitches/clients/posh_premium/) |
| Martina Wu | Landing Page | ⭐ 4.9 | [View Site](https://pranavrai207.github.io/client-pitches/clients/martina_wu/) |

### 🍽️ Restaurants & Cafes
| Client | Type | Rating | Live Link |
|--------|------|--------|-----------|
| Impresario | Multi-page | ⭐ 4.5 | [View Site](https://pranavrai207.github.io/client-pitches/clients/impresario/) |
| Mr. K Ramyun Cafe | Multi-page (4 pages) | ⭐ 4.3 | [View Site](https://pranavrai207.github.io/client-pitches/clients/mr_k_ramyun_cafe/) |
| The Golden Spoon | Landing Page | ⭐ 4.4 | [View Site](https://pranavrai207.github.io/client-pitches/clients/the-golden-spoon/) |
| Reflections Cafe | Landing Page | ⭐ 4.3 | [View Site](https://pranavrai207.github.io/client-pitches/clients/reflections_cafe/) |
| FoodCourt House Takeaway | Multi-page | ⭐ 4.1 | [View Site](https://pranavrai207.github.io/client-pitches/clients/foodcourt_house_takeway/) |
| 7Heaven Foods | Landing Page | ⭐ 4.0 | [View Site](https://pranavrai207.github.io/client-pitches/clients/7heaven_foods/) |
| ShellBeacon Cafe | Multi-page | ⭐ 4.3 | [View Site](https://pranavrai207.github.io/client-pitches/clients/shellbeacon_cafe/) |

### 💪 Fitness & Wellness
| Client | Type | Rating | Live Link |
|--------|------|--------|-----------|
| Real Steel Gym | Multi-page | ⭐ 4.6 | [View Site](https://pranavrai207.github.io/client-pitches/clients/real-steel-gym/) |
| Neon Genesis Fitness | Landing Page | ⭐ 4.5 | [View Site](https://pranavrai207.github.io/client-pitches/clients/neon-genesis-fitness/) |
| Yoga For World | Landing Page | ⭐ 4.8 | [View Site](https://pranavrai207.github.io/client-pitches/clients/yoga-for-world/) |
| Power Zone Gym | Landing Page | ⭐ 4.8 | [View Site](https://pranavrai207.github.io/client-pitches/clients/power_zone_gym/) |

### 🎭 Other
| Client | Type | Rating | Live Link |
|--------|------|--------|-----------|
| Dance with Shubham | Multi-page | ⭐ 4.7 | [View Site](https://pranavrai207.github.io/client-pitches/clients/dance-with-shubham/) |

## 🎨 Design System
Every client website is visually unique — no two sites look the same.

### Dynamic Theme Engine (`system/`)
| Component | Purpose |
|-----------|---------|
| `generators/theme_engine.py` | Randomized font pairings + color presets per category |
| `generators/layout_assembler.py`| Assembles HTML from components + layouts |
| `tokens/salon.css` | Design tokens for salon/beauty category |
| `tokens/premium-restaurant.css`| Design tokens for restaurant category |
| `components/` | Reusable section templates (hero, nav, footer, etc.) |
| `layouts/` | Page layout definitions for single & multi-page sites |

### What Makes Each Site Unique
- 🎨 **Custom Color Palettes** — No two clients share the same palette
- 🔤 **Unique Font Pairings** — Google Fonts combinations (Cormorant + Lato, Bebas Neue + Rubik, etc.)
- 🖼️ **AI-Generated Images** — Custom hero, service, and interior photos for each business
- 📐 **Category-Aware Layouts** — Salons get elegant serif styles, restaurants get bold food-first designs, gyms get high-energy aesthetics
- 📱 **Full Mobile Responsiveness** — Every site works perfectly on all screen sizes
- 🔍 **SEO Schema** — LocalBusiness / Restaurant / BeautySalon JSON-LD markup

## 🚀 Quick Setup

**Step 1 — Create a Virtual Environment**
```powershell
cd "C:\Lead Generation"
python -m venv venv
.\venv\Scripts\Activate.ps1

# If you see a permissions error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Step 2 — Install Dependencies**
```powershell
pip install -r requirements.txt
```

**Step 3 — Install Playwright Browser**
```powershell
playwright install chromium
```

## 🛠️ Usage

**Unified Pipeline (Recommended)**
```powershell
python main.py all
```

**Individual Commands**
```powershell
# Scrape specific niche
python main.py scrape --query "salons in Delhi" --max 40

# Filter results
python main.py filter

# Generate pitch
python main.py pitch --client "Bloom Salon"

# Optimize assets (Convert to WebP)
python main.py optimize --client "bloom_salon"

# Deploy to GitHub
python main.py deploy --client "bloom_salon"
```

**CLI Arguments**
| Argument | Short | Target | Description |
|----------|-------|--------|-------------|
| `--query` | `-q` | `scrape` | Search term for Google Maps |
| `--max` | `-m` | `scrape` | Max results per query |
| `--client` | `-c` | `pitch/deploy`| Client name or folder name |

## ⚙️ Configuration
```python
# config/config.py
SEARCH_QUERIES = [
    "cafes in Delhi",
    "restaurants in Delhi",
    "gyms in Delhi",
]

MAX_RESULTS = 50      # Leads per query
HEADLESS = False      # True = invisible browser
MIN_DELAY = 2.0       # Min delay between actions
MAX_DELAY = 5.0       # Max delay between actions
```

## 📊 Lead Database — `delhi_leads.xlsx`
| Column | Description |
|--------|-------------|
| Name | Business name |
| Rating | Star rating (e.g. 4.3) |
| Total Reviews | Number of reviews |
| Address | Street address |
| Phone | Contact number |
| Website | Website URL (or N/A) |
| Category | Business type |
| Maps URL | Direct Google Maps link |
| Priority | 🔥 High / 🟡 Medium / 🟢 Low |

**Lead Priority Logic**
| Priority | Condition | Why It Matters |
|----------|-----------|----------------|
| 🔥 High | No website listed | Perfect target for web design pitch |
| 🟡 Medium| Rating ≥ 4.0 with website | Open to premium upgrades |
| 🟢 Low | Website + rating < 4.0 | Already present online |

## 💎 Pitch Generation Protocol
1. **Lead Selection** — Use `python main.py filter` to identify high-priority targets
2. **Asset Creation** — Generate AI images, create client folder structure
3. **Theme Application** — Dynamic theme engine assigns unique fonts + colors
4. **UI Construction** — Build responsive HTML/CSS following `design_standards.md`
5. **Optimization** — Convert images to WebP for production performance
6. **Deployment** — Push to GitHub Pages for instant live links

## 🛡️ Anti-Detection Strategy
- Non-headless mode — real browser, not invisible
- Random delays (2–5s) between every action
- Gradual scrolling to simulate human behavior
- Realistic user-agent (Chrome 122, Windows 11)
- Geolocation set to New Delhi
- `navigator.webdriver` flag hidden

## 📈 Scale to Any City
```python
SEARCH_QUERIES = [
    "cafes in Mumbai",
    "restaurants in Bangalore",
    "gyms in Hyderabad",
]
OUTPUT_FILE = "india_leads.xlsx"
```

## ⚠️ Ethical Usage
- Intended for responsible, small-scale lead research only
- Keep MAX_RESULTS conservative (30–50 per run)
- Do not run in rapid succession
- Review Google Maps Terms of Service

## 🔧 Troubleshooting
| Issue | Fix |
|-------|-----|
| `playwright install fails` | Run PowerShell as Administrator |
| Script hangs on search | Increase timeout in `perform_search()` |
| 0 results collected | Check if Google changed their selectors |
| Excel not saving | `pip install openpyxl` |
| Activation error | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

Built with ❤️ using Playwright + Python + AI Image Generation
