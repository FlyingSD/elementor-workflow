# 🎨 Svetlinki - Color & Style Vision

**Date**: 2025-11-30
**Status**: ✅ APPROVED
**Version**: Final
**Based On**: design-mockup-v3.html

---

## 🌈 COLOR PALETTE (Priority Order)

### **Primary Colors:**

| Color | Hex | Usage | Dominance |
|-------|-----|-------|-----------|
| **Yellow** | `#FABA29` | MAIN COLOR - Hero gradients, primary buttons, carousel nav, icons, badges, accents | ⭐⭐⭐⭐⭐ STAR |
| **Dark Teal** | `#1d3234` | ALL body text, headings, readable content | ⭐⭐⭐⭐⭐ TEXT |
| **White** | `#FFFFFF` | Clean backgrounds, card backgrounds, breathing space | ⭐⭐⭐⭐⭐ SPACE |

### **Secondary Colors:**

| Color | Hex | Usage | Dominance |
|-------|-----|-------|-----------|
| **Teal** | `#46b19d` | Hover states, secondary accents, one benefit icon, link colors | ⭐⭐ SUPPORT |
| **Coral** | `#FF8C7A` | Secondary buttons, SVG underlines, gradient accents, playful touches | ⭐⭐ PLAYFUL |

### **Background Variations:**

| Color | Hex | Usage |
|-------|-----|-------|
| **Warm Cream** | `#FEFCF5` | Alternate section backgrounds, card backgrounds |
| **Light Yellow** | `#fff4d9` | Hero gradient middle |
| **Warm Yellow** | `#ffe8b3` | Hero gradient end |
| **Cream Yellow** | `#fff9e6` | Benefits/Programs alternate backgrounds |

---

## 🎨 COLOR USAGE RULES

### **DO:**
✅ Use `#FABA29` (yellow) as the dominant color
✅ Use `#1d3234` (dark teal) for ALL text
✅ Use `#FFFFFF` (white) for clean backgrounds
✅ Use `#46b19d` (teal) ONLY for hover states and small accents
✅ Use `#FF8C7A` (coral) ONLY for subtle playful touches
✅ Use gradients with yellow as base (yellow → coral, yellow → teal)

### **DON'T:**
❌ DON'T make teal dominant (it's secondary!)
❌ DON'T use green instead of teal
❌ DON'T use harsh backgrounds (keep white/cream)
❌ DON'T add new colors without approval

---

## 🔘 BUTTON STYLES

### **Primary Button** (Main CTA - "Безплатен пробен урок")
```css
Background: #FABA29 (yellow)
Hover: #46b19d (teal)
Text: #FFFFFF (white)
Border-radius: 12px (slightly rounded)
Padding: 18px 40px
Shadow: 0 6px 20px rgba(250, 186, 41, 0.35)
Transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1)
Hover effect: translateY(-3px) + shadow increase + ripple
```

### **Secondary Button** ("Вижте програмите", "Прочети повече")
```css
Background: #FF8C7A (coral)
Hover: #46b19d (teal)
Text: #FFFFFF (white)
Border-radius: 12px
Padding: 18px 40px
Shadow: 0 6px 20px rgba(255, 140, 122, 0.35)
Transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1)
Hover effect: translateY(-3px) + shadow increase + ripple
```

---

## 📐 CARD STYLES

### **Standard Cards** (Benefits, Programs, Blog)

```css
Background: #FFFFFF (white)
Border-radius: 20px (well rounded)
Padding: 45px 35px (generous)
Box-shadow: 0 10px 35px rgba(0, 0, 0, 0.1) (deep shadow)
Border-top: 5px solid [varies by card]
Transition: all 0.35s ease

Hover effect:
  - translateY(-12px) scale(1.02)
  - box-shadow: 0 20px 50px rgba(250, 186, 41, 0.2)
  - NO border changes on hover (simple lift)
```

### **Card Top Borders** (Colorful variety)
- Card 1: `#FABA29` (yellow)
- Card 2: `linear-gradient(90deg, #FABA29, #FF8C7A)` (yellow → coral)
- Card 3: `#46b19d` (teal)

---

## 🎭 ICON STYLES

### **Benefit Icons** (Circular with gradients)
```css
Width/Height: 75px
Border-radius: 50% (perfect circle)
Background: linear-gradient(135deg, #FABA29, #f5a500) (yellow)
OR: linear-gradient(135deg, #FF8C7A, #ff7059) (coral)
OR: linear-gradient(135deg, #46b19d, #3d8a7a) (teal)
Box-shadow: 0 6px 20px rgba(250, 186, 41, 0.3)
Font-size: 38px (emoji)

Hover effect:
  - transform: scale(1.15) rotate(5deg)
```

### **Program Number Badges**
```css
Width/Height: 50px
Border-radius: 50%
Background: linear-gradient(135deg, #FABA29, #FF8C7A)
Color: #FFFFFF
Font-size: 22px
Font-weight: 700
Box-shadow: 0 4px 15px rgba(250, 186, 41, 0.35)
```

---

## 🌊 HERO SECTION

### **Background Gradient**
```css
background: linear-gradient(120deg, #FEFCF5 0%, #fff4d9 40%, #ffe8b3 100%);
```

### **Radial Glows** (Playful floating orbs)
```css
/* Yellow glow - top right */
radial-gradient(circle, rgba(250, 186, 41, 0.3) 0%, transparent 70%)
Position: top -50%, right -10%
Size: 600px × 600px

/* Coral glow - bottom left */
radial-gradient(circle, rgba(255, 140, 122, 0.15) 0%, transparent 70%)
Position: bottom -30%, left -5%
Size: 500px × 500px
```

### **Typography**
```css
H1:
  Font-size: clamp(2.25rem, 5vw, 3.25rem)
  Color: #1d3234
  Font-weight: 700
  Line-height: 1.15

Subtitle:
  Font-size: clamp(1.05rem, 2.5vw, 1.25rem)
  Color: #1d3234
  Opacity: 0.9
  Line-height: 1.75
```

---

## ✨ CREATIVE ELEMENTS

### **1. Coral SVG Underline** (Subtle accent)
```css
Position: absolute, bottom -5px
Width: 100%
Height: 12px
Opacity: 0.7
Stroke: #FF8C7A (coral)
Stroke-width: 4px
```

### **2. Section Title Underlines**
```css
Position: absolute, bottom -12px
Width: 80px
Height: 4px
Background: linear-gradient(90deg, #FABA29, #FF8C7A)
Border-radius: 2px
```

### **3. Ripple Effect on Buttons**
```css
Before pseudo-element:
  Width/Height: 0 → 300px (on hover)
  Background: rgba(255, 255, 255, 0.3)
  Border-radius: 50%
  Transition: 0.6s
```

### **4. Hover Animations**
- Cards: `translateY(-12px) scale(1.02)`
- Icons: `scale(1.15) rotate(5deg)`
- Buttons: `translateY(-3px)`
- Carousel nav: `scale(1.15) rotate(5deg)`

---

## 📱 RESPONSIVE BREAKPOINTS

### **Desktop** (1200px+)
- Hero: 2 columns (text left, mascot right)
- Benefits: 3 columns
- Programs: 3 columns
- Max-width: 1200px

### **Tablet** (768px - 1200px)
- Hero: 1 column (stacked)
- Benefits: 2 columns
- Programs: 2 columns

### **Mobile** (<768px)
- Hero: 1 column, centered text
- Benefits: 1 column
- Programs: 1 column
- Padding reduced: 70px → 40px

---

## 🎯 ANIMATION TIMING

```css
Standard transition: all 0.35s ease
Button transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1)
Ripple transition: width/height 0.6s
Hover lift: transform 0.35s ease
```

---

## 📝 TYPOGRAPHY

### **Font Families**
```css
font-family: 'Segoe UI', 'Roboto', 'Open Sans', sans-serif;
```

### **Font Weights**
- Body text: 400 (regular)
- Emphasis: 600 (semi-bold)
- Headings: 700 (bold)

### **Line Heights**
- Body text: 1.7 - 1.75
- Headings: 1.15 - 1.3

### **Font Sizes (Clamp for responsiveness)**
```css
H1: clamp(2.25rem, 5vw, 3.25rem)
H2: clamp(1.85rem, 4vw, 2.5rem)
H3: clamp(1.4rem, 3vw, 1.65rem)
Body: clamp(1rem, 2vw, 1.05rem)
```

---

## 🎨 SECTION BACKGROUNDS

### **Pattern:**
Alternate between white and warm backgrounds

```
Hero: Yellow gradient (#FEFCF5 → #fff4d9 → #ffe8b3)
Blog Carousel: White (#FFFFFF)
Benefits: Warm cream gradient (#FEFCF5 → #fff9e6)
Programs: White (#FFFFFF)
```

---

## 💡 DESIGN PHILOSOPHY

### **Brand Personality:**
- **Joyful**: Yellow dominates, creates positive mood
- **Professional**: Clean white backgrounds, readable text
- **Confidence-inspiring**: Bold typography, clear hierarchy
- **Playful**: Subtle animations, coral accents, rounded corners
- **Modern**: Gradients, shadows, smooth transitions

### **Target Audience:**
- **Primary**: Parents (mothers) aged 30-45
- **Tone**: Empathetic expert (warm + credible)
- **Goal**: Inspire hope and confidence

### **Selling:**
- NOT selling "math tutoring"
- Selling HOPE to worried parents
- Transformation story (from fear to confidence)

---

## ✅ IMPLEMENTATION CHECKLIST

When building in Elementor:

- [ ] Use Global Colors feature (map hex codes)
- [ ] Sans-serif fonts (Roboto, Open Sans, Segoe UI)
- [ ] Border-radius: 12px (buttons), 20px (cards), 50% (icons)
- [ ] Deep shadows: `0 10px 35px rgba(0, 0, 0, 0.1)`
- [ ] Hover effects: translateY + scale + shadow increase
- [ ] All text: `#1d3234` (dark teal)
- [ ] Primary buttons: `#FABA29` → `#46b19d` hover
- [ ] Secondary buttons: `#FF8C7A` → `#46b19d` hover
- [ ] Card top borders: 5px solid (varied colors)
- [ ] Generous padding: 45px inside cards, 90px sections
- [ ] Mobile: Reduce padding to 40px, stack columns
- [ ] NO mascot hover effects (static images)

---

## 🔗 REFERENCE FILES

- **HTML Mockup**: `design-mockup-v3.html`
- **Final Mockup**: `design-mockup-v4.html` (with Programs teaser)
- **This Document**: `COLOR-AND-STYLE-VISION.md`

---

**Status**: ✅ APPROVED by client (2025-11-30)
**Ready for**: Elementor implementation via coder agent
**Color System**: Yellow STAR, teal secondary, coral playful, dark teal text, white space
