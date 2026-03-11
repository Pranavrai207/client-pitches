# 🧠 AI Brain: System Prompts & Strategy

This file is the single Source of Truth for the Lead Generation and Website Building system.

---

## 🎨 Professional Web Design Standards (10/10)

These guidelines ensure all generated websites meet premium, high-conversion standards.

### Core Directives
1.  **Enforce** a maximum container width of **1200px**.
2.  **Apply** the **8px spacing scale** rigorously (8, 16, 24, 32, 48, 64px).
3.  **Optimize** all assets to **WebP** format.
4.  **Verify** accessibility (WCAG compliant colors) and **mobile-first** responsiveness.

### Visual Constraints
- Maximum **3 primary colors**.
- Maximum **2 font families**.
- No gradients unless brand-required.
- No inline CSS or unused classes.

### Structural Skeleton (Non-Negotiable)
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

---

## 📈 Pitch Protocol: Rapid Client Website Generation

This workflow defines the exact steps for generating a high-end landing page in 10–20 minutes.

### 1. Project Intake
Collect: Business Name, Category, Rating, Total Reviews, Address, Phone, Primary Services, USP.

### 2. Folder Structure
All projects must live in: `Client_Websites/clients/[folder_name]/`

### 3. Asset Rules
- Use `generate_image` for 5+ high-quality images.
- Physical verification of files via `list_dir` is mandatory.
- Images must be WebP and optimized under 300KB.

### 4. Mobile Responsiveness
- Navbar: Fixed at top, `white-space: nowrap` on logo/buttons.
- H1: max 2.2rem (mobile), H2: max 1.8rem (mobile).
- `overflow-x: hidden` globally.
- Never mix `.container` and styled box classes.

### 5. SEO & White-Labeling
- Include JSON-LD LocalBusiness schema.
- Semantic HTML only.
- **NO AI SIGNATURES** (e.g., "Built by AI" is forbidden).
- Footer only: Business copyright or "Crafted with Precision".

---

## 🤖 System Philosophy
The system removes ambiguity and enforces structure to ensure near one-run execution success.
