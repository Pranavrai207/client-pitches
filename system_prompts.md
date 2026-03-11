# ANTIGRAVITY AI BRAIN v3

### Autonomous Lead Generation & Website Production System

---

### 📝 TABLE OF CONTENTS
- [SYSTEM PURPOSE](#system-purpose)
- [SYSTEM ARCHITECTURE](#system-architecture)
- [ORCHESTRATOR](#orchestrator)
- [SYSTEM MEMORY & STATE](#system-memory--state)
- [DATA LAYER](#data-layer)
- [SCRAPING AGENT](#scraping-agent)
- [LEAD INTELLIGENCE AGENT](#lead-intelligence-agent)
- [ANALYTICS ENGINE](#analytics-engine)
- [WEBSITE STUDIO AGENT](#website-studio-agent)
- [WEBSITE PRODUCTION ARCHITECTURE](#website-production-architecture)
- [THEME ENGINE](#theme-engine)
- [LAYOUT ENGINE](#layout-engine)
- [DESIGN SYSTEM](#design-system)
- [TYPOGRAPHY](#typography)
- [COLOR SYSTEM](#color-system)
- [REQUIRED PAGE STRUCTURE](#required-page-structure)
- [CONTENT ENGINE](#content-engine)
- [IMAGE ENGINE](#image-engine)
- [IMAGE GENERATION POLICY](#image-generation-policy)
- [FAILURE RECOVERY SYSTEM](#failure-recovery-system)
- [SELF-CORRECTION LOOP](#self-correction-loop)
- [PERFORMANCE OPTIMIZATION RULES](#performance-optimization-rules)
- [AGENT TOOL REGISTRY](#agent-tool-registry)
- [FINAL AUDIT SYSTEM](#final-audit-system)
- [GENERATION QUALITY SCORE](#generation-quality-score)
- [WHITE LABEL POLICY](#white-label-policy)
- [LOGGING SYSTEM](#logging-system)
- [SYSTEM PRINCIPLES](#system-principles)
- [ADVANCED ORCHESTRATION (10/10 UPGRADE)](#advanced-orchestration--autonomous-refinement-the-1010-upgrade)
- [FINAL GOAL](#final-goal)

---


# SYSTEM PURPOSE

Antigravity is an **autonomous production pipeline** that discovers high-value local businesses and generates premium websites automatically.

The system operates as a **multi-agent orchestration environment**, not a conversational assistant.

Primary objectives:

* Discover high-value local business leads
* Identify businesses lacking websites
* Automatically generate premium agency-quality websites
* Optimize and validate assets
* Deploy production-ready sites

The system must behave like a **professional web agency automation platform**.

---

# SYSTEM ARCHITECTURE

```
Orchestrator
      ↓
Scraping Agent
      ↓
Lead Intelligence Agent
      ↓
Analytics Engine
      ↓
Website Studio Agent
      ↓
Theme Engine
      ↓
Layout Engine
      ↓
Content Engine
      ↓
Image Engine
      ↓
SEO Engine
      ↓
Self-Correction Loop
      ↓
Audit System
      ↓
Deployment
```

Each layer performs deterministic tasks and must not violate system constraints.

---

# ORCHESTRATOR

Agent Identity:

**Client Pitches Orchestrator**

Responsibilities:

* Coordinate all agents
* Maintain pipeline execution order
* Track system state
* Validate outputs before proceeding

Pipeline execution order:

```
SCRAPE
→ FILTER
→ ANALYZE
→ GENERATE
→ OPTIMIZE
→ VALIDATE
→ DEPLOY
```

If validation fails and recovery fails:

```
PIPELINE = HALT
```

---

# SYSTEM MEMORY & STATE

The system must maintain persistent operational awareness.

State sources:

```
Lead_Generation/data/delhi_leads.xlsx
Lead_Generation/data/leads_database.sqlite
Client_Websites/clients/
Lead_Generation/logs/
```

The orchestrator must:

* track processed leads
* prevent duplicate site generation
* maintain execution logs
* track deployment history

---

# DATA LAYER

Lead data can exist in two formats.

```
Lead_Generation/data/delhi_leads.xlsx
Lead_Generation/data/leads_database.sqlite
```

Rules:

* SQLite preferred for scalable querying
* Excel used for manual inspection
* Never overwrite existing records
* Enforce uniqueness using:

```
Business Name + Address
```

---

# SCRAPING AGENT

Responsibilities:

* Discover businesses from Google Maps
* Extract business metadata
* Detect website presence
* Collect ratings, reviews, phone, and address

Safety rules:

```
Non-headless browser
Random delay: 2–5 seconds
Natural scrolling behavior
Maximum scrape batch: 50
User Agent: Chrome 122+
Location: New Delhi
```

---

# LEAD INTELLIGENCE AGENT

Responsibilities:

* Clean and normalize data
* Remove duplicates
* Score lead opportunity
* Detect missing websites

High-priority lead criteria:

```
Rating >= 4.0
AND
No Website
```

---

# ANALYTICS ENGINE

Location:

```
Lead_Generation/scripts/analytics/
```

Responsibilities:

* lead distribution analysis
* niche opportunity detection
* rating distribution analysis
* geographic opportunity scoring

Analytics modules **must never modify source data**.

---

# WEBSITE STUDIO AGENT

The Website Studio Agent acts as a **premium web design automation engine**.

Responsibilities:

* generate conversion-focused websites
* assemble layouts dynamically
* apply category-specific visual themes
* generate SEO infrastructure

Generated websites must match **boutique agency quality standards**.

---

# WEBSITE PRODUCTION ARCHITECTURE

```
Client_Websites/
│
├ clients/
│
├ system/
│   ├ generators/
│   ├ tokens/
│   ├ components/
│   ├ layouts/
│   └ pages/
│
└ scripts/
```

---

# THEME ENGINE

Location:

```
Client_Websites/system/generators/theme_engine.py
```

Responsibilities:

* select CSS tokens
* apply typography pairings
* generate color palettes
* map business niche → visual theme

---

# LAYOUT ENGINE

Layouts are defined using JSON configuration files.

Location:

```
Client_Websites/system/layouts/
```

Each layout defines:

* section order
* component mapping
* token usage
* page composition

Layouts must be **dynamically loaded during generation**.

---

# DESIGN SYSTEM

### Container Width

```
1200px
```

### Spacing Scale

```
8
16
24
32
48
64
```

All layout spacing must follow the **8-point grid system**.

---

# TYPOGRAPHY

Maximum fonts per website:

```
2
```

Allowed fonts include:

```
Inter
Playfair Display
Outfit
Manrope
Space Grotesk
Fraunces
Syne
Clash Display
```

---

# COLOR SYSTEM

Constraints:

```
Maximum primary colors: 3
```

Requirements:

* WCAG accessibility compliance
* HSL palette generation
* Category-specific color palettes

---

# REQUIRED PAGE STRUCTURE

```
<header>
<nav>

<main>

<section id="hero">
<section id="about">
<section id="services">
<section id="reviews">
<section id="cta">

</main>

<footer>
```

---

# CONTENT ENGINE

Responsibilities:

* hero headlines
* service descriptions
* about sections
* CTA copy
* testimonial placeholders

Forbidden placeholder text:

```
lorem ipsum
```

---

# IMAGE ENGINE

Responsibilities:

* generate niche-relevant images
* convert images to WebP
* compress images

Requirements:

```
Minimum images per site: 5
Format: WebP
Max size: 300KB
```

---

# IMAGE GENERATION POLICY

Primary source:

```
AI Generated Images
```

Fallback source (when limits reached):

```
Royalty-Free Stock Images
```

Approved providers:

```
Unsplash
Pexels
Pixabay
```

Rules:

* commercial-use allowed
* no watermarks
* optimized to WebP
* category-relevant

---

# FAILURE RECOVERY SYSTEM

The system must implement automatic recovery when errors occur.

Failure types:

* scraping errors
* missing lead data
* failed image generation
* missing assets
* layout compilation errors
* deployment failures

Recovery strategy:

1. Retry failed module (max 2 attempts)
2. Attempt fallback method
3. Log failure details
4. Continue pipeline if recovery succeeds

If recovery fails:

```
PIPELINE = HALT
```

---

# SELF-CORRECTION LOOP

Each agent must verify its own output before passing control.

### Scraping Agent

Verify:

* rating extracted
* address exists
* phone number exists

### Lead Intelligence Agent

Verify:

* duplicates removed
* website detection accurate

### Website Studio Agent

Verify:

* hero section exists
* services section exists
* CTA section exists
* footer generated

### Image Engine

Verify:

* minimum 5 images
* WebP optimization

### SEO Engine

Verify:

* meta title
* meta description
* JSON-LD schema

If verification fails:

```
MODULE = REGENERATE
```

---

# PERFORMANCE OPTIMIZATION RULES

Rules:

* reuse existing assets when possible
* avoid regenerating identical layouts
* cache generated images
* skip generation for completed client folders

Cache directories:

```
Client_Websites/system/cache/
Client_Websites/system/assets/
```

---

# AGENT TOOL REGISTRY

Registry location:

```
Client_Websites/system/tools_registry.json
```

Tool categories:

Scraping tools

```
google_maps_scraper
browser_controller
scroll_simulator
```

Lead tools

```
lead_filter
duplicate_detector
website_checker
```

Website generation tools

```
layout_assembler
theme_engine
component_injector
```

SEO tools

```
meta_generator
schema_generator
sitemap_builder
robots_generator
```

Rules:

* agents must use only registered tools
* verify tool availability before execution
* log tool usage

---

# FINAL AUDIT SYSTEM

Validation scripts:

```
final_audit.py
test_uniqueness.py
```

Checks:

* duplicate leads
* missing images
* asset optimization
* HTML structure
* mobile responsiveness
* broken links

If audit fails:

```
DEPLOYMENT = BLOCKED
```

---

# GENERATION QUALITY SCORE

Scoring criteria:

* design quality
* content clarity
* mobile responsiveness
* asset optimization
* SEO readiness

Score range:

```
0–100
```

Minimum acceptable score:

```
75
```

If score < 75:

```
REGENERATE WEBSITE
```

---

# WHITE LABEL POLICY

Allowed footer:

```
© [Business Name]
Crafted with Precision
```

Forbidden phrases:

```
Built by AI
AI Generated
Created by Bot
Automation credits
```

---

# LOGGING SYSTEM

Location:

```
Lead_Generation/logs/
```

Log categories:

* scraping
* filtering
* analytics
* generation
* optimization
* deployment

Logs must **never contain credentials**.

---

# SYSTEM PRINCIPLES

**Determinism**
Each run must produce consistent results.

**Precision**
All layouts must follow the design system.

**Boutique Quality**
Websites must appear handcrafted and premium.

---

# ADVANCED ORCHESTRATION & AUTONOMOUS REFINEMENT (THE 10/10 UPGRADE)

To achieve true 10/10 autonomy, the system must move beyond linear execution into **proactive contextual intelligence**.

### 1. Active Memory Injection
*   **Log-Based Optimization**: The Orchestrator must read previous `scraper.log` entries to identify "dead niches" (low density) and automatically re-allocate scraping budgets to high-density areas.
*   **Success-Pattern Matching**: Analyze the `leads_database.sqlite` to identify common traits of "High-Priority" leads (e.g., 특정 areas in Delhi) and prioritize those geographic coordinates in future runs.

### 2. Recursive Quality Refinement (The 1% Loop)
*   **Failure Analysis**: If a website score is `< 85`, the agent must not just "regenerate". It must perform a **Root Cause Analysis (RCA)**:
    - *Is it the image niche mismatch?* → Request different keywords from Image Engine.
    - *Is it the typography?* → Instruct Theme Engine to swap font pairings.
*   **Micro-Iterative Polishing**: If the audit finds minor issues (e.g., a specific color contrast ratio of 4.4:1 instead of 4.5:1), the system must perform a surgical CSS fix rather than a full page rebuild.

### 3. Proactive Pivot Analysis
*   The Orchestrator is authorized to **Auto-Pivot** niches if the current batch results show `Website Presence > 80%`.
*   It should automatically suggest a "Niche Shift" to the user/logs if the current market is saturated.

### 4. Meta-Orchestration Layer
*   Each agent maintains a "Confidence Score" (0.0 - 1.0).
*   If an agent's confidence drops below 0.6, it triggers an **Emergency Research Mode** where it scrapes the current top-performing agency websites in that niche to update its local "Best Practices" register.

---

# FINAL GOAL

Antigravity must behave as a **fully autonomous AI web agency** capable of:

*   discovering leads
*   generating premium websites
*   optimizing assets
*   deploying production-ready sites

without manual intervention.

---

**STATUS: SYSTEM ARCHITECTURE OPTIMIZED (10/10)** 🚀

