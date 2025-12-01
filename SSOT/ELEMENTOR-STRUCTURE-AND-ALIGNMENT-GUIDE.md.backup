# Elementor Structure & Alignment Guide

**Purpose**: Practical rules for building proper layouts, card structures, and alignments
**Date**: 2025-11-30
**Status**: Production reference for page building
**Version**: 1.0

---

## Table of Contents

1. [Structure Fundamentals](#structure-fundamentals)
2. [Section Configuration](#section-configuration)
3. [Column Layout & Alignment](#column-layout--alignment)
4. [Card Structure Patterns](#card-structure-patterns)
5. [Text & Content Alignment](#text--content-alignment)
6. [Spacing System](#spacing-system)
7. [Common Patterns](#common-patterns)
8. [Troubleshooting Layouts](#troubleshooting-layouts)

---

## Structure Fundamentals

### Element Hierarchy

```
Section/Container (Full-width wrapper)
├── Column 1
│   ├── Widget 1
│   └── Widget 2
├── Column 2
│   ├── Widget 3
│   └── Widget 4
└── Column 3
    ├── Widget 5
    └── Widget 6
```

### Key Principles

1. **Sections** define horizontal sections of page
2. **Columns** create horizontal divisions within sections
3. **Widgets** are actual content elements (cannot contain other widgets)
4. **Styling applies at appropriate level**:
   - Page background → Section
   - Card background → Column
   - Content styling → Widget

### Element Capabilities

| Element | Can Style | Cannot Style |
|---------|-----------|--------------|
| **Section** | Background, border, padding, margin, height, column gaps | Individual column content |
| **Column** | Background, border, shadow, padding, margin, width, alignment | Widget-specific properties |
| **Widget** | Text, icon, button, typography | Container background (limited) |

**Critical Rule**: To create card-style layouts with backgrounds, borders, and shadows → **Style the COLUMN, not the widget!**

---

## Section Configuration

Source: `includes/elements/section.php`

### Layout Type

```json
{
  "layout": "boxed" | "full_width"
}
```

**boxed**: Centered container with max-width
**full_width**: Stretches edge-to-edge

**Best Practice**:
- Hero sections: `full_width`
- Content sections: `boxed` with 1140px content_width
- Footer: `full_width`

### Content Width

```json
{
  "layout": "boxed",
  "content_width": {"size": 1140, "unit": "px"}
}
```

**Common Widths**:
- Desktop standard: 1140px
- Wide layout: 1400px
- Narrow content: 960px

### Column Structure

```json
{
  "structure": "33.333" | "50" | "25" | "custom"
}
```

**Common Structures**:
- 3 equal columns: `"33.333"` + `"33.333"` + `"33.333"`
- 2 equal columns: `"50"` + `"50"`
- 4 equal columns: `"25"` + `"25"` + `"25"` + `"25"`
- 2/3 + 1/3: `"66.666"` + `"33.333"`

### Column Gap

```json
{
  "gap": "default" | "no" | "narrow" | "extended" | "wide" | "wider" | "custom",
  "gap_columns_custom": {"size": 40, "unit": "px"}
}
```

**Gap Values** (Elementor defaults):
- `no`: 0px
- `narrow`: 5px
- `default`: 10px
- `extended`: 15px
- `wide`: 20px
- `wider`: 30px
- `custom`: Your value

**For Cards**: Use `extended` (15px) or `custom` (30-40px) for visual separation

### Section Height

```json
{
  "height": "default" | "full" | "min-height",
  "custom_height": {"size": 600, "unit": "px"}
}
```

**Usage**:
- `full`: Full viewport height (hero sections)
- `min-height`: Minimum height with `custom_height`
- `default`: Height based on content

### Vertical Alignment (Section-Level)

```json
{
  "column_position": "stretch" | "top" | "middle" | "bottom"
}
```

**Visual Effect**:
```
┌─────────┬─────────┬─────────┐
│ Content │ Content │ Content │  top
├─────────┼─────────┼─────────┤
│         │ Content │         │  middle
├─────────┼─────────┼─────────┤
│         │         │ Content │  bottom
└─────────┴─────────┴─────────┘
```

### Stretch Section

```json
{
  "stretch_section": "yes" | ""
}
```

**Effect**: Makes section stretch to browser window edges (ignores container padding)

**Use Case**: Full-width backgrounds while keeping content boxed inside

---

## Column Layout & Alignment

Source: `includes/elements/column.php`

### Column Width

```json
{
  "_inline_size": 33  // Percentage
}
```

**Responsive Widths**:
```json
{
  "_inline_size": 33,           // Desktop (33%)
  "_inline_size_tablet": 50,    // Tablet (50%)
  "_inline_size_mobile": 100    // Mobile (100% - full width)
}
```

### Vertical Alignment (Content Position)

```json
{
  "content_position": "default" | "top" | "center" | "bottom" | "space-between" | "space-around" | "space-evenly"
}
```

**CSS Effect**:
- Applies `align-items` and `align-content` to `.elementor-widget-wrap`
- Controls vertical placement of widgets WITHIN the column

**Visual Examples**:
```
┌─────────┐
│ Widget  │  top
│ Widget  │
│         │
│         │
└─────────┘

┌─────────┐
│         │
│ Widget  │  center
│ Widget  │
│         │
└─────────┘

┌─────────┐
│ Widget  │  space-between
│         │
│ Widget  │
└─────────┘
```

**Best Practice**:
- Cards with equal heights: `center`
- Hero sections: `center`
- Form layouts: `top`
- Footer: `space-between`

### Horizontal Alignment

```json
{
  "align": "default" | "flex-start" | "center" | "flex-end" | "space-between" | "space-around" | "space-evenly"
}
```

**CSS Effect**:
- Applies `justify-content` to `.elementor-widget-wrap`
- Controls horizontal placement of widgets

**Visual Examples**:
```
┌────────────────────────┐
│ [Widget] [Widget]      │  flex-start (left)
└────────────────────────┘

┌────────────────────────┐
│    [Widget] [Widget]   │  center
└────────────────────────┘

┌────────────────────────┐
│ [Widget]      [Widget] │  space-between
└────────────────────────┘
```

**Best Practice**:
- Center aligned content: `center`
- Multiple buttons: `center` or `space-around`
- Icon + text layouts: `flex-start`

### Widget Spacing

```json
{
  "space_between_widgets": {"size": 20, "unit": "px"}
}
```

**Effect**: Gap between widgets stacked vertically in column

**Recommended Values**:
- Tight layout: 10-15px
- Standard: 20px
- Loose: 30-40px

### Padding & Margin

```json
{
  "padding": {
    "unit": "px",
    "top": "45",
    "right": "35",
    "bottom": "45",
    "left": "35",
    "isLinked": false
  },
  "margin": {
    "unit": "px",
    "top": "0",
    "right": "10",
    "bottom": "0",
    "left": "10",
    "isLinked": false
  }
}
```

**Padding** = Internal spacing (inside border)
**Margin** = External spacing (outside border)

**Card Padding Best Practice**:
```json
{
  "padding": {
    "top": "35",     // More vertical space
    "right": "30",   // Less horizontal space
    "bottom": "35",
    "left": "30",
    "isLinked": false
  }
}
```

**Column Margin for Gaps**:
```json
{
  "margin": {
    "right": "15",  // Half of desired gap (30px total between 2 columns)
    "left": "15",
    "isLinked": false
  }
}
```

---

## Card Structure Patterns

### Pattern 1: Icon-Box Card (3-Column Grid)

**Structure**:
```
Section (background, gap)
├── Column 1 (card styling)
│   └── Icon-Box Widget (content only)
├── Column 2 (card styling)
│   └── Icon-Box Widget (content only)
└── Column 3 (card styling)
    └── Icon-Box Widget (content only)
```

**Column Settings** (Card Container):
```json
{
  "_column_size": 33,
  "_inline_size_tablet": 50,
  "_inline_size_mobile": 100,

  // Card Background
  "background_background": "classic",
  "background_color": "#FFFFFF",

  // Card Border
  "border_border": "solid",
  "border_width": {
    "top": "5", "right": "0", "bottom": "0", "left": "0",
    "isLinked": false
  },
  "border_color": "#FABA29",
  "border_radius": {
    "top": "20", "right": "20", "bottom": "20", "left": "20",
    "isLinked": true
  },

  // Card Shadow
  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)"
  },

  // Internal Spacing
  "padding": {
    "top": "35", "right": "30", "bottom": "35", "left": "30"
  },

  // Alignment
  "content_position": "top",  // Widgets start at top
  "align": "center"           // Center horizontally
}
```

**Icon-Box Widget Settings** (Content Only):
```json
{
  // Icon Style
  "view": "stacked",
  "shape": "circle",
  "primary_color": "#FABA29",      // Circle background
  "secondary_color": "#FFFFFF",    // Icon color
  "icon_size": {"size": 38, "unit": "px"},
  "icon_space": {"size": 22, "unit": "px"},

  // Layout
  "position": "top",
  "text_align": "center",

  // Typography (title/description handled separately)
}
```

**Section Settings** (Container):
```json
{
  "layout": "boxed",
  "content_width": {"size": 1140, "unit": "px"},
  "gap": "custom",
  "gap_columns_custom": {"size": 30, "unit": "px"},
  "background_background": "classic",
  "background_color": "#FEFCF5"
}
```

### Pattern 2: Text Card (2-Column Grid)

**Structure**:
```
Section
├── Column 1 (card)
│   ├── Heading Widget
│   ├── Text Editor Widget
│   └── Button Widget
└── Column 2 (card)
    ├── Heading Widget
    ├── Text Editor Widget
    └── Button Widget
```

**Column Settings**:
```json
{
  "_column_size": 50,
  "_inline_size_mobile": 100,

  "background_background": "classic",
  "background_color": "#FFFFFF",

  "border_border": "solid",
  "border_width": {"top": "0", "right": "0", "bottom": "3", "left": "0"},
  "border_color": "#4F9F8B",

  "box_shadow": {
    "horizontal": 0,
    "vertical": 5,
    "blur": 20,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.08)"
  },

  "padding": {"top": "40", "right": "30", "bottom": "40", "left": "30"},

  "content_position": "top",
  "align": "flex-start",
  "space_between_widgets": {"size": 20, "unit": "px"}
}
```

### Pattern 3: Image + Text Card (Horizontal)

**Structure**:
```
Section
└── Column (card)
    ├── Image Widget
    ├── Heading Widget
    ├── Text Editor Widget
    └── Button Widget
```

**OR** (side-by-side):
```
Section
└── Outer Column (card)
    ├── Inner Column 40% (image)
    │   └── Image Widget
    └── Inner Column 60% (content)
        ├── Heading Widget
        ├── Text Editor Widget
        └── Button Widget
```

**Outer Column Settings**:
```json
{
  "_column_size": 100,

  "background_background": "classic",
  "background_color": "#FFFFFF",

  "border_radius": {"top": "15", "right": "15", "bottom": "15", "left": "15"},

  "box_shadow": {
    "horizontal": 0,
    "vertical": 8,
    "blur": 25,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.12)"
  },

  "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0"},

  // Use inner columns for layout
  "content_position": "stretch"
}
```

---

## Text & Content Alignment

### Widget-Level Text Alignment

**Heading Widget**:
```json
{
  "align": "left" | "center" | "right" | "justify"
}
```

**Text Editor Widget**:
```json
{
  "align": "left" | "center" | "right" | "justify"
}
```

**Icon-Box Widget**:
```json
{
  "text_align": "left" | "center" | "right",
  "content_vertical_alignment": "top" | "middle" | "bottom"  // When icon is left/right
}
```

**Button Widget**:
```json
{
  "align": "left" | "center" | "right" | "justify"
}
```

### Responsive Alignment

```json
{
  "align": "center",          // Desktop
  "align_tablet": "left",     // Tablet
  "align_mobile": "center"    // Mobile
}
```

**Best Practice**:
- Desktop cards: Center aligned
- Mobile cards: Left aligned (easier to read)
- CTAs: Always center aligned

---

## Spacing System

### Spacing Hierarchy

```
Section Padding (60-80px)
  ├── Column Margin (10-20px gaps)
  │   └── Column Padding (30-45px)
  │       └── Widget Spacing (15-25px)
  │           └── Widget Internal (10-15px)
```

### Recommended Values

**Section Padding** (Top/Bottom):
```json
{
  "padding": {
    "top": "80",
    "bottom": "80"
  }
}
```
- Hero: 100-120px
- Content: 60-80px
- Footer: 40-60px

**Column Padding** (Cards):
```json
{
  "padding": {
    "top": "35",
    "right": "30",
    "bottom": "35",
    "left": "30"
  }
}
```
- Small cards: 25-30px
- Medium cards: 35-40px
- Large cards: 45-50px

**Widget Spacing** (Between widgets in column):
```json
{
  "space_between_widgets": {"size": 20, "unit": "px"}
}
```
- Tight: 15px
- Normal: 20px
- Loose: 25-30px

**Column Gaps** (Between columns):
```json
{
  "gap_columns_custom": {"size": 30, "unit": "px"}
}
```
- Tight grid: 15-20px
- Normal grid: 30px
- Wide grid: 40-50px

### Responsive Spacing

**Pattern**: Reduce spacing on smaller screens

```json
{
  "padding": {
    "top": "45",
    "right": "35",
    "bottom": "45",
    "left": "35"
  },
  "padding_tablet": {
    "top": "35",
    "right": "25",
    "bottom": "35",
    "left": "25"
  },
  "padding_mobile": {
    "top": "25",
    "right": "20",
    "bottom": "25",
    "left": "20"
  }
}
```

---

## Common Patterns

### Pattern: 3-Column Benefits Cards

**Goal**: Equal-height cards with icons, centered content

**Section**:
```json
{
  "layout": "boxed",
  "gap": "custom",
  "gap_columns_custom": {"size": 30, "unit": "px"},
  "padding": {"top": "80", "bottom": "80"}
}
```

**Each Column** (33.333% width):
```json
{
  "_column_size": 33,
  "content_position": "top",
  "align": "center",
  "background_color": "#FFFFFF",
  "border_radius": {"top": "20", ...},
  "box_shadow": {...},
  "padding": {"top": "35", "right": "30", "bottom": "35", "left": "30"}
}
```

**Responsive**:
```json
{
  "_inline_size_tablet": 50,     // 2 columns on tablet
  "_inline_size_mobile": 100     // 1 column on mobile
}
```

### Pattern: Hero Section (Full-Width Gradient)

**Section**:
```json
{
  "layout": "full_width",
  "height": "full",
  "column_position": "middle",

  "background_background": "gradient",
  "background_gradient_type": "linear",
  "background_gradient_angle": {"size": 120, "unit": "deg"},
  "background_color": "#FEFCF5",
  "background_color_stop": {"size": 0, "unit": "%"},
  "background_color_b": "#ffe8b3",
  "background_color_b_stop": {"size": 100, "unit": "%"}
}
```

**Column** (2 columns: 50% text + 50% image):
```json
{
  "_column_size": 50,
  "content_position": "center",
  "align": "flex-start",
  "padding": {"top": "60", "right": "40", "bottom": "60", "left": "40"}
}
```

### Pattern: Programs Teaser Cards

**Section**:
```json
{
  "layout": "boxed",
  "content_width": {"size": 1140, "unit": "px"},
  "gap": "custom",
  "gap_columns_custom": {"size": 40, "unit": "px"}
}
```

**Columns** (3 equal):
```json
{
  "_column_size": 33,
  "content_position": "space-between",  // Spread widgets evenly
  "background_color": "#FFFFFF",
  "border_radius": {"top": "20", ...},
  "box_shadow": {...},
  "padding": {"top": "35", "right": "30", "bottom": "35", "left": "30"},
  "space_between_widgets": {"size": 20, "unit": "px"}
}
```

**Widgets**:
- Heading (title)
- Text Editor (description)
- Button (CTA)

### Pattern: Footer (Full-Width Background)

**Section**:
```json
{
  "layout": "full_width",
  "background_color": "#1D3234",
  "padding": {"top": "60", "bottom": "40"}
}
```

**Columns** (4 equal):
```json
{
  "_column_size": 25,
  "_inline_size_tablet": 50,
  "_inline_size_mobile": 100,
  "content_position": "top",
  "align": "flex-start"
}
```

---

## Troubleshooting Layouts

### Issue: Cards Not Equal Height

**Problem**: Columns have different content lengths, creating uneven heights

**Solution 1**: Use `column_position: "stretch"` at section level
```json
{
  "column_position": "stretch"  // Forces all columns to match tallest
}
```

**Solution 2**: Set minimum height on columns
```json
{
  "min_height": {"size": 400, "unit": "px"}
}
```

### Issue: Content Not Centered in Card

**Problem**: Widget content sticks to top/left of column

**Solution**: Use both vertical and horizontal alignment
```json
{
  "content_position": "center",  // Vertical
  "align": "center"              // Horizontal
}
```

**Widget**: Also center widget content
```json
{
  "text_align": "center"  // For icon-box, heading, text
}
```

### Issue: Cards Too Wide on Mobile

**Problem**: 3-column layout too cramped on mobile

**Solution**: Responsive column widths
```json
{
  "_column_size": 33,           // Desktop (3 columns)
  "_inline_size_tablet": 50,    // Tablet (2 columns)
  "_inline_size_mobile": 100    // Mobile (1 column)
}
```

### Issue: Gaps Too Small/Large

**Problem**: Cards touching or too far apart

**Solution 1**: Use section gap setting
```json
{
  "gap": "custom",
  "gap_columns_custom": {"size": 30, "unit": "px"}
}
```

**Solution 2**: Use column margins
```json
{
  "margin": {
    "right": "15",  // 30px total gap between columns
    "left": "15"
  }
}
```

### Issue: Column Not Showing Background

**Problem**: Applied background_color but not visible

**Check**:
1. `background_background` set to `"classic"`?
2. CSS regenerated? (see ELEMENTOR-API-TECHNICAL-GUIDE.md)
3. Column has content (height)?

**Solution**:
```json
{
  "background_background": "classic",  // ← Must set type!
  "background_color": "#FFFFFF"
}
```

### Issue: Icon-Box Card Shadow Not Showing

**Problem**: Applied box_shadow to widget instead of column

**Solution**: Apply to parent column
```json
// ❌ WRONG - Widget settings
{
  "_box_shadow_box_shadow": {...}  // Doesn't work on icon-box!
}

// ✅ CORRECT - Column settings
{
  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)"
  }
}
```

### Issue: Text Alignment Not Working

**Problem**: Text still left-aligned despite settings

**Check**:
1. Applied to widget, not column?
2. Widget has default alignment override?
3. CSS specificity issue?

**Solution**:
```json
// Widget level (heading, text-editor, button)
{
  "align": "center"
}

// Icon-box uses different property
{
  "text_align": "center"
}
```

### Issue: Column Position Not Taking Effect

**Problem**: Set `content_position: "center"` but widgets still at top

**Reasons**:
1. Column has no fixed height (height = content height)
2. Widget has margin pushing it
3. Section `column_position` conflicts

**Solution**:
```json
{
  // Give column minimum height
  "min_height": {"size": 300, "unit": "px"},

  // Then center works
  "content_position": "center"
}
```

---

## Quick Reference Cheat Sheet

### Section Quick Config
```json
{
  "layout": "boxed",
  "content_width": {"size": 1140, "unit": "px"},
  "gap": "custom",
  "gap_columns_custom": {"size": 30, "unit": "px"},
  "column_position": "stretch",
  "padding": {"top": "80", "bottom": "80"}
}
```

### Card Column Quick Config
```json
{
  "_column_size": 33,
  "_inline_size_tablet": 50,
  "_inline_size_mobile": 100,

  "background_background": "classic",
  "background_color": "#FFFFFF",

  "border_border": "solid",
  "border_width": {"top": "5", "right": "0", "bottom": "0", "left": "0"},
  "border_color": "#FABA29",
  "border_radius": {"top": "20", "right": "20", "bottom": "20", "left": "20"},

  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)"
  },

  "padding": {"top": "35", "right": "30", "bottom": "35", "left": "30"},

  "content_position": "top",
  "align": "center",
  "space_between_widgets": {"size": 20, "unit": "px"}
}
```

### Icon-Box Widget Quick Config
```json
{
  "view": "stacked",
  "shape": "circle",
  "primary_color": "#FABA29",
  "secondary_color": "#FFFFFF",
  "icon_size": {"size": 38, "unit": "px"},
  "icon_space": {"size": 22, "unit": "px"},
  "position": "top",
  "text_align": "center"
}
```

---

## Best Practices Summary

1. **Card Styling**: Always style the COLUMN, not the widget
2. **Equal Heights**: Use section `column_position: "stretch"`
3. **Spacing**: Use consistent spacing system (15/20/30/40px increments)
4. **Responsive**: Always define tablet/mobile breakpoints
5. **Alignment**: Combine section, column, and widget alignment for best control
6. **Gaps**: Use section gap OR column margins, not both
7. **Testing**: Always test on all 3 breakpoints (desktop/tablet/mobile)
8. **CSS Regeneration**: After API updates, regenerate CSS (see Technical Guide)

---

**Last Updated**: 2025-11-30
**Version**: 1.0
**Companion Guide**: ELEMENTOR-API-TECHNICAL-GUIDE.md
**Status**: Production Ready
