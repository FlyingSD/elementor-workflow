# Elementor Global Colors Setup Guide

**Site**: http://svetlinkielementor.local
**Date**: 2025-11-28

---

## 🎨 Colors To Configure

Based on your Svetlinki design system, configure these Global Colors in Elementor:

### Color Palette:

| Color Name | Hex Code | Usage | Elementor Slot |
|------------|----------|-------|----------------|
| **Primary** | `#6366f1` | CTA buttons, links, main brand color | Color 1 (Primary) |
| **Secondary** | `#F5A623` | Headings, accents, Svetlinki Orange | Color 2 (Secondary) |
| **Text** | `#2c2c2c` | Body text, paragraphs, dark text | Color 3 (Text) |
| **Accent** | `#FDB913` | Hover states, secondary CTAs, highlights | Color 4 (Accent) |
| **Background** | `#fefcf5` | Page backgrounds, sections, warm white | Color 5 (Background) |

---

## 📋 Setup Steps

### 1. Access Elementor Theme Builder

1. Go to: `http://svetlinkielementor.local/wp-admin`
2. Login with: `test` / `test`
3. Navigate to: **Elementor → Theme Builder**

### 2. Open Site Settings

1. Click the hamburger menu (☰) top left
2. Click **Site Settings**
3. Navigate to **Global Colors**

### 3. Configure Each Color

**Color 1 - Primary (#6366f1)**
- Click on Color 1
- Enter hex: `#6366f1`
- Rename to: "Primary" or "Indigo"
- Usage: CTA buttons, links

**Color 2 - Secondary (#F5A623)**
- Click on Color 2
- Enter hex: `#F5A623`
- Rename to: "Secondary" or "Svetlinki Orange"
- Usage: Headings, accents

**Color 3 - Text (#2c2c2c)**
- Click on Color 3
- Enter hex: `#2c2c2c`
- Rename to: "Text" or "Dark Gray"
- Usage: Body text, paragraphs

**Color 4 - Accent (#FDB913)**
- Click on Color 4
- Enter hex: `#FDB913`
- Rename to: "Accent" or "Light Orange"
- Usage: Hover states, highlights

**Color 5 - Background (#fefcf5)**
- Click on Color 5 (or add new if needed)
- Enter hex: `#fefcf5`
- Rename to: "Background" or "Warm White"
- Usage: Page backgrounds

### 4. Save

- Click **Update** at the bottom
- Close Site Settings panel

---

## ✅ Verification

After setup, verify Global Colors are working:

1. Create a test page with Elementor
2. Add a Heading widget
3. Click on text color → Should see your Global Colors available
4. Select "Primary" → Text should turn indigo (#6366f1)

---

## 🔤 Global Fonts (Optional - Future Setup)

Typography scale to configure later:
- **Primary**: System font stack (default for now)
- **Secondary**: For headings
- **Body**: 1rem (16px), line-height 1.7
- **H1**: 2.75rem (44px), line-height 1.2
- **H2**: 1.9rem (30.4px), line-height 1.2
- **H3**: 1.4rem (22.4px), line-height 1.2

---

## 🚀 After Setup

Once Global Colors are configured:
1. Return to Claude Code
2. Confirm colors are set up
3. We can begin creating pages with agents
4. All widgets will use Global Colors (no hardcoded values)

---

**Reference**: Based on `svetlinkelementor-rebuild-guide.md` design system
**Status**: Ready for manual setup
