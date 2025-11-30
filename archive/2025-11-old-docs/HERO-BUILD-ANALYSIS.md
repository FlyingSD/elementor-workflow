# Hero Section Build Analysis

**Purpose**: Document how the Hero section was built and apply same principles to Blog/Benefits/Programs sections.

---

## Current Hero Structure (Working ✅)

### High-Level Architecture

```
Hero Section (e0fc723) - Legacy Section
├── Column 1 (7f4b890) - 60% width
│   ├── Heading Widget (H1)
│   ├── Text Editor Widget (description)
│   ├── Button Widget (primary CTA)
│   └── Button Widget (secondary CTA)
└── Column 2 (1f4634d) - 40% width
    └── Image Widget (Zhara character)
```

**Note**: Hero currently uses LEGACY SECTION/COLUMN structure (`elType: "section"`, `elType: "column"`).

For new sections, we'll use **CONTAINERS** (`elType: "container"`) - modern Flexbox approach.

---

## Key Styling Principles (Apply to All Sections)

### 1. Section-Level Styling

**Located**: On the section/container element itself

```json
{
  "stretch_section": "section-stretched",  // Full-width
  "background_background": "gradient",     // Or "classic" for solid
  "background_color": "#FEFCF5",          // Global Color 5
  "background_color_b": "#fff4d9",        // Gradient end
  "background_gradient_angle": {
    "unit": "deg",
    "size": 120
  },
  "padding": {
    "unit": "px",
    "top": "100",
    "right": "20",
    "bottom": "100",
    "left": "20"
  },
  "min_height": {
    "unit": "px",
    "size": 650
  }
}
```

**Principle**:
- Use `stretch_section` for full-width
- Apply background (solid or gradient) at section level
- Generous padding (80-100px top/bottom, 20px sides)
- Set min-height for hero sections

### 2. Column/Container Content Positioning

**Located**: On column/container settings

```json
{
  "_column_size": 60,           // Percentage width
  "_inline_size": 60,           // Explicit inline size
  "content_position": "center"  // Vertical centering
}
```

**Principle**:
- Use percentage-based widths for responsive layout
- Center content vertically with `content_position`
- For two-column: 60/40 split works well for hero

### 3. Widget-Level Styling (Typography & Colors)

**Located**: On individual widget settings

**Heading Example**:
```json
{
  "title": "Развийте математическите умения на вашето дете",
  "header_size": "h1",
  "align": "left",
  "title_color": "var(--e-global-color-text)",  // ✅ Global Color
  "typography_typography": "custom",
  "typography_font_size": {
    "unit": "rem",
    "size": 3.25  // Large hero heading
  },
  "typography_font_weight": "700",
  "typography_line_height": {
    "unit": "em",
    "size": 1.15
  }
}
```

**Text Editor Example**:
```json
{
  "editor": "<p>Ментална аритметика за деца...</p>",
  "text_color": "var(--e-global-color-text)",  // ✅ Global Color
  "typography_font_size": {
    "unit": "rem",
    "size": 1.25  // Readable body text
  },
  "typography_line_height": {
    "unit": "em",
    "size": 1.75  // Generous line spacing
  }
}
```

**Button Example**:
```json
{
  "text": "Безплатен пробен урок",
  "button_text_color": "#FFFFFF",
  "background_color": "var(--e-global-color-primary)",  // ✅ Global Color
  "border_radius": {
    "unit": "px",
    "top": "12",
    "right": "12",
    "bottom": "12",
    "left": "12"
  },
  "button_padding": {
    "unit": "px",
    "top": "18",
    "right": "40",
    "bottom": "18",
    "left": "40"
  },
  "button_box_shadow_box_shadow": {
    "horizontal": 0,
    "vertical": 6,
    "blur": 20,
    "spread": 0,
    "color": "rgba(250, 186, 41, 0.35)"  // Glow effect
  },
  "button_background_hover_color": "var(--e-global-color-secondary)",
  "hover_animation": "grow"
}
```

**Principle**:
- ALWAYS use Global Colors via CSS variables (`var(--e-global-color-primary)`)
- Use `rem` for font sizes (scalable)
- Use `em` for line-height (relative to font size)
- Add box shadows for depth
- Add hover states for interactivity

---

## Global Colors Reference

```css
--e-global-color-primary: #FABA29   (Yellow/Gold)
--e-global-color-secondary: #4F9F8B (Teal/Green)
--e-global-color-text: #1D3234      (Dark Teal)
--e-global-color-accent: #FF8C7A    (Coral)
--e-global-color-5: #FEFCF5         (Warm Cream)
```

---

## Translating to Container-Based Approach

### Legacy Section/Column → Modern Container

**Old (Legacy Section/Column)**:
```json
{
  "elType": "section",
  "elements": [
    {
      "elType": "column",
      "_column_size": 60,
      "elements": [/* widgets */]
    },
    {
      "elType": "column",
      "_column_size": 40,
      "elements": [/* widgets */]
    }
  ]
}
```

**New (Container with Nested Containers)**:
```json
{
  "elType": "container",
  "settings": {
    "content_width": "full",
    "flex_direction": "row",
    "flex_wrap": "wrap",
    "flex_gap": {"column": "30", "row": "30", "unit": "px"}
  },
  "elements": [
    {
      "elType": "container",
      "settings": {
        "flex_basis": "60",  // 60% width
        "flex_grow": "1"
      },
      "elements": [/* widgets */]
    },
    {
      "elType": "container",
      "settings": {
        "flex_basis": "40",  // 40% width
        "flex_grow": "1"
      },
      "elements": [/* widgets */]
    }
  ]
}
```

**Key Differences**:
- Use `content_width: "full"` instead of `stretch_section`
- Use `flex_direction: "row"` for horizontal layout
- Use `flex_basis` instead of `_column_size`
- Use `flex_gap` for spacing between items

---

## Section-Specific Applications

### Blog Section (Single Column, Centered)

**Structure**:
```
Container (full-width, white background)
└── Container (centered content)
    ├── Heading Widget ("От нашия блог")
    ├── Divider Widget (80px yellow line)
    └── Icon-Box Widget (blog card with newspaper icon)
```

**Styling Focus**:
- White background (`#FFFFFF`)
- Centered heading (2.5rem, bold)
- Icon-box with top border accent (5px yellow)
- Icon in circular background (newspaper icon, yellow circle)

### Benefits Section (3-Column Grid)

**Structure**:
```
Container (full-width, white background)
├── Container (centered header)
│   ├── Heading Widget
│   └── Divider Widget
└── Container (3-column grid)
    ├── Container (column 1)
    │   └── Icon-Box Widget (brain icon, yellow circle)
    ├── Container (column 2)
    │   └── Icon-Box Widget (lightbulb icon, coral circle)
    └── Container (column 3)
        └── Icon-Box Widget (star icon, teal circle)
```

**Styling Focus**:
- Each card has top border matching icon color
- Icons use FontAwesome (NOT emojis): `fas fa-brain`, `fas fa-lightbulb`, `fas fa-star`
- Icon styling on widget settings (NOT column):
  ```json
  {
    "icon_padding": {"unit": "px", "top": "18", ...},
    "icon_border_radius": {"unit": "%", "top": "50", ...},
    "icon_background_color": "var(--e-global-color-primary)"
  }
  ```

### Programs Section (3-Column Grid with Buttons)

**Structure**:
```
Container (full-width, white background)
├── Container (centered header)
│   ├── Heading Widget
│   └── Divider Widget
└── Container (3-column grid)
    ├── Container (column 1)
    │   ├── Icon-Box Widget (book icon, yellow)
    │   └── Button Widget
    ├── Container (column 2)
    │   ├── Icon-Box Widget (gift icon, coral)
    │   └── Button Widget
    └── Container (column 3)
        ├── Icon-Box Widget (question-circle icon, teal)
        └── Button Widget
```

**Styling Focus**:
- Icons: `fas fa-book`, `fas fa-gift`, `fas fa-question-circle`
- Each card has border color matching icon background
- Buttons below each card ("Прочети повече")

---

## Common Pitfalls to Avoid

1. ❌ **DON'T** apply icon styling at column level - apply at widget level
2. ❌ **DON'T** use emojis - use FontAwesome icons only
3. ❌ **DON'T** use hardcoded colors - use Global Colors (`var(--e-global-color-*)`)
4. ❌ **DON'T** forget box shadows - they add depth
5. ❌ **DON'T** nest containers unnecessarily - keep flat structure where possible
6. ✅ **DO** use generous padding (40-45px on cards)
7. ✅ **DO** use border-radius (20px for cards, 12px for buttons)
8. ✅ **DO** match border colors to icon background colors

---

## MCP Implementation Checklist

When using `mcp__wp-elementor-mcp__create_elementor_section`:

1. Create main container with full-width settings
2. Add nested containers for layout (if multi-column)
3. Add widgets to containers with full styling
4. Use `icon_padding`, `icon_border_radius`, `icon_background_color` for circular icons
5. Use `border_border`, `border_width`, `border_color` for top accent borders
6. Add box shadows for depth
7. Use Global Colors for all colors
8. Test on frontend and regenerate CSS if needed

---

## Summary: Core Principles

1. **Full-Width Stretch**: Use `content_width: "full"` on main container
2. **Global Colors Always**: Never hardcode brand colors
3. **Widget-Level Icon Styling**: Apply icon styling on widget, not parent
4. **Generous Spacing**: 80-100px section padding, 40-45px card padding
5. **Visual Hierarchy**: Headings (2.5rem) → Dividers (80px × 4px) → Content
6. **Depth via Shadows**: All cards have subtle box shadows
7. **Border Accents**: Top borders (5px) matching icon colors
8. **FontAwesome Only**: NO emojis (they cause rendering issues)

---

**Created**: 2025-11-30
**Purpose**: Guide for rebuilding Blog/Benefits/Programs sections with Container approach
