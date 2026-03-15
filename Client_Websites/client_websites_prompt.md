# WEBSITE STUDIO SYSTEM PROMPT
## Premium Web Design & Production Engine

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

# FAILURE RECOVERY SYSTEM (WEBSITE)

The system must implement automatic recovery when errors occur.

Failure types:

* failed image generation
* missing assets
* layout compilation errors
* deployment failures

Recovery strategy:

1. Retry failed module (max 2 attempts)
2. Attempt fallback method
3. Log failure details
4. Continue pipeline if recovery succeeds

---

# SELF-CORRECTION LOOP (WEBSITE)

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

---

# FINAL AUDIT SYSTEM

Validation scripts:

```
final_audit.py
test_uniqueness.py
```

Checks:

* missing images
* asset optimization
* HTML structure
* mobile responsiveness
* broken links

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

# WORKFLOW: RAPID CLIENT PITCH GENERATION (EXECUTION PROTOCOL)

> [!IMPORTANT]
> **MASTER TRUTH**: The logic in this document is derived from [rapid_client_pitch.json](file:///c:/Lead%20Generation/.agent/workflows/brain/rapid_client_pitch.json). For AI execution, the JSON file is the absolute authority.

This workflow defines the exact steps required to generate a high-end, SEO-optimized, white-labeled landing page in 10–20 minutes.

All output must strictly comply with `design_standards.md` without deviation.

## 1. Project Intake (Structured Input Required)

Before generation begins, collect:
- Business Name
- Category
- Rating
- Number of Reviews
- Address
- Phone
- Primary Service(s)
- Unique Selling Proposition (if available)

No build begins without this data.

## 2. Mandatory Folder Structure (Pre-Build Setup)

All projects must follow this structure:

```
/clients/folder_name/
  index.html
  /assets/
     /images/
     /css/
     /js/
```

No alternative structure allowed.

### Deployment & Presentation
- **MANDATORY PRE-DEPLOY SYNC**: Always run `git pull origin main` BEFORE deploying to prevent push rejections from diverged branches.
- Use `deploy.py [folder_name]` for deployment.
- **MANDATORY URL STRUCTURE**: All live links MUST follow this exact format:
  `https://pranavrai207.github.io/client-pitches/clients/[folder_name]/`
- Do NOT omit the `/clients/` segment, or the link will fail.
- Always verify the live link physically before presenting to the user.

## 3. Asset Generation & Optimization

   - Use the `generate_image` tool to create at least 5 high-quality (8k, photorealistic) WebP images (Hero, About, and at least 3 Service cards).
   - **MANDATORY PHYSICAL VERIFICATION**: After copying images to the `clients/<client_folder>/assets/images` directory, you MUST run `list_dir` to physically confirm the files exist. Do NOT assume success from the console output.
   - Run the optimization script: `python optimize_assets.py "clients/<client_folder>/assets/images"`.
   - **MANDATORY CHECK**: You must verify that the script successfully generated the `.webp` versions inside the client's specific image folder before proceeding.

## 4. Visual Asset Generation (Strict Rules)

All generated images must:
- Match business category
- Align with discovered brand tone
- Be exported in WebP format
- Be under 300KB per image
- Be generated in multiple sizes: 480px, 800px, 1200px, 1920px
- Be implemented using `srcset`
- Use `loading="lazy"` for all non-critical images

## 5. Custom UI Construction (Deterministic Rules)

All layout must strictly follow `design_standards.md`.

**Visual Constraints:**
- Maximum 3 primary colors
- Maximum 2 font families
- No gradients unless brand-required
- No inline CSS
- No unused classes
- No unnecessary libraries

**Structural Constraint (Non-Negotiable Layout Skeleton):**
```html
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
Order must remain consistent.

## 6. Strict Mobile Responsiveness Enforcement

Mobile-first design is mandatory.

**Requirements:**
- Max width: 768px target
- Navbar: 100% width, Fixed at top. Add `white-space: nowrap` to logo and buttons to prevent awkward wrapping.
- H1 max size: 2.2rem (mobile)
- H2 max size: 1.8rem (mobile)
- All grids must stack vertically (`flex-direction: column`)
- `box-sizing: border-box` enforced globally
- **NO HORIZONTAL SCROLL**: Ensure `overflow-x: hidden` is on html/body.
- **MIXING RULE**: Never mix `.container` and styled box classes on the same element. Wrap the box inside the container.

## 7. Professional SEO Injection

Must include:
- JSON-LD LocalBusiness schema
- Semantic HTML (header, nav, main, section, footer)
- Optimized meta description
- Open Graph tags
- Proper alt attributes
- Title tag under 60 characters
- Meta description under 160 characters

## 8. White-Label Enforcement (Critical)

Strictly prohibited:
- "Built by Antigravity"
- Any AI signature (e.g., "by AI", "Crafted with Precision by AI")
- Any developer/generator branding

Footer must contain only:
- Business copyright OR "Crafted with Precision"

## 9. Pre-Output Self-Audit (Mandatory Before Final Output)

Before deployment, internally verify:
- [ ] Max container width 1200px?
- [ ] 8px spacing scale followed?
- [ ] All images WebP?
- [ ] 5 unique images present?
- [ ] Physical directory verification (list_dir) passed?
- [ ] No AI signature? (MUST NOT CONTAIN "by AI")
- [ ] URL contains `/clients/` path?
- [ ] No horizontal scroll on mobile?

If any condition fails, correct before finalizing. This step is mandatory.
