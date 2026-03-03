---
description: Professional Web Design Standards and Guidelines
---

# Professional Web Design Standards

## 1. Website Width (Layout Container Size)
Professional websites are not full width; content should be constrained within a fixed container.
- **Mobile**: 100% (full width)
- **Tablet**: 90–95%
- **Laptop**: 1140px – 1200px
- **Desktop (large)**: 1200px – 1320px max
- **👉 Sweet spot**: 1200px container width. (Going wider makes content look stretched).

## 2. Breakpoints (Responsive Design Sizes)
Modern responsive websites typically use these breakpoints:
- **Small Mobile**: 320px – 480px
- **Large Mobile**: 481px – 768px
- **Tablet**: 769px – 1024px
- **Laptop**: 1025px – 1440px
- **Large Desktop**: 1441px+
*👉 90% of traffic comes from mobile. Always use mobile-first design.*

## 3. Hero Section (Top Banner)
**Desktop:**
- Height: 80vh – 100vh
- Padding: 80px top-bottom
- Headline size: 48px – 64px

**Mobile:**
- Height: auto (minimum 60vh)
- Padding: 40px
- Headline size: 28px – 36px
*👉 Keep the hero section clean and not overcrowded for a professional feel.*

## 4. Font Sizes (VERY IMPORTANT)
**Desktop:**
- H1: 48–64px
- H2: 32–40px
- H3: 24–28px
- Body text: 16–18px

**Mobile:**
- H1: 28–34px
- H2: 22–26px
- Body text: 15–16px
*⚠️ Never make body text smaller than 14px (it looks cheap).*

## 5. Section Spacing (Professional Look Secret)
Spacing is what makes a website look premium.
**Desktop:**
- Section padding: 80px – 120px

**Mobile:**
- Section padding: 50px – 70px
*👉 Too little spacing makes the website look crowded.*

## 6. Buttons Size
**Desktop:**
- Height: 45px – 55px
- Padding: 12px 24px

**Mobile:**
- Height: 48px minimum (thumb-friendly)
- *Full width recommended*

## 7. Images Size Guidelines
- **Hero Background**: 1920x1080 px (Full HD)
- **Card Images**: 600x400 px
- **Blog Thumbnails**: 1200x630 px (OG size)
- **Format**: Always use WebP format.
- **Size Limit**: Max 200–300KB per image.

## 8. Navbar Height
- **Desktop**: 70–90px
- **Mobile**: 60–70px
*👉 Sticky navbars are highly recommended in modern design.*

## 9. Cards Layout
**Desktop:**
- 3 cards per row
- Gap: 24–32px

**Tablet:**
- 2 cards per row

**Mobile:**
- 1 card per row

---

## 🧠 Golden Rule (Professional Standard)
Follow this core structure:
- **Max Width**: 1200px
- **Section Padding**: 100px
- **Body Font**: 16px
- **Consistent spacing scale (8px system)**: Use 8px, 16px, 24px, 32px, 40px, 48px, 64px. *Do not use random spacing.*

## 🚀 Bonus: What Makes a Website Look "Expensive"
- Lots of WHITE SPACE
- Fewer colors (strict palette)
- Big bold headlines
- Clean grid
- No tiny fonts
- No overcrowded sections

---

## 🥇 IMAGE OPTIMIZATION METHODS

### METHOD 1: HTML Responsive Images (Must Do)
Use `srcset` + `sizes` so only the required size downloads.
```html
<img 
  src="hero-1200.webp"
  srcset="
    hero-480.webp 480w,
    hero-800.webp 800w,
    hero-1200.webp 1200w,
    hero-1920.webp 1920w
  "
  sizes="(max-width: 768px) 100vw, 1200px"
  alt="Hero Image"
  loading="lazy"
/>
```

### METHOD 2: Modern Formats with `<picture>` (SaaS Level)
Provides fallbacks (AVIF -> WebP -> JPG).
```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" alt="Hero" loading="lazy">
</picture>
```

### METHOD 3: CSS Background Optimization
Using `image-set` or media queries for CSS backgrounds.
```css
/* Media query approach */
.hero {
  background-image: url("hero-1200.webp");
}
@media (max-width: 768px) {
  .hero {
    background-image: url("hero-480.webp");
  }
}
```

### METHOD 4: Backend Auto Optimization (Node.js)
Using `sharp` for resizing and WebP conversion.
```javascript
const sharp = require("sharp");
sharp("input.jpg")
  .resize(1200)
  .webp({ quality: 80 })
  .toFile("output.webp");
```

### 🧠 MUST ADD: Lazy Loading
- Use `loading="lazy"` for all non-critical images.
- Use `IntersectionObserver` for background images.
