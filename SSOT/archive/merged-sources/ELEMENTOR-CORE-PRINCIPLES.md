# Elementor Core Principles & Best Practices

**Document Type**: Technical Reference
**Date Created**: 2025-11-28
**Source**: Official Elementor documentation via r.jina research
**Purpose**: Guide for building Svetlinki Elementor pages programmatically via MCP

---

## Table of Contents

1. [Structural Hierarchy](#structural-hierarchy)
2. [Performance Optimization](#performance-optimization)
3. [Widget Selection Strategy](#widget-selection-strategy)
4. [Design System Implementation](#design-system-implementation)
5. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
6. [Responsive Design](#responsive-design)
7. [JSON Data Structure](#json-data-structure)
8. [Programmatic Building Guidelines](#programmatic-building-guidelines)

---

## Structural Hierarchy

### Modern Architecture: Flexbox Containers (RECOMMENDED)

Elementor now offers **Flexbox Containers** as the modern, performance-optimized approach to page building.

**Two Architecture Options**:

#### Option A: Flexbox Containers (Modern - USING THIS) ⭐
```
Page
└── Container (flexbox-based layout)
    └── Widget (direct children, no columns needed)
        └── Nested Container (optional, for complex layouts)
```

**Benefits**:
- ✅ **Better Performance**: Fewer DOM elements (no column wrappers)
- ✅ **More Flexible**: Full CSS Flexbox/Grid control
- ✅ **Cleaner HTML**: Direct container → widget structure
- ✅ **Responsive by Default**: Built-in flex wrapping

#### Option B: Traditional Sections (Legacy)
```
Page
└── Section (largest building block)
    └── Column (segments within sections)
        └── Widget (individual elements)
```

**We use Flexbox Containers for all new pages.**

---

### Container Best Practices

**Key Principle**: Each container should serve a **distinct content purpose**.

✅ **DO**:
- Create containers for major content divisions (Hero, Features, Testimonials, CTA)
- Use direct widget children (no unnecessary nesting)
- Keep container count minimal (6-10 containers for most pages)
- Leverage flexbox direction (row/column), justify, align properties

❌ **DON'T**:
- Create containers just for spacing control (use padding/margin on widgets)
- Over-nest containers (max 2 levels deep)
- Duplicate containers for responsive design (use responsive settings)

**Example: Optimal Home Page Structure (Containers)**:
```
Container 1: Hero (direction: column, full-width)
  └── Heading widget
  └── Text Editor widget
  └── Button widget

Container 2: Features (direction: row, flex-wrap)
  └── Icon Box widget
  └── Icon Box widget
  └── Icon Box widget

Container 3: About (direction: row, 2 nested containers)
  └── Container (text content)
  └── Container (image)

Container 4: Testimonials (direction: column)
  └── Testimonial Carousel widget

Container 5: CTA (direction: column, centered)
  └── Heading widget
  └── Button widget
```

### Container Layout Properties

**Flexbox Direction**:
- `row`: Horizontal layout (side-by-side widgets)
- `column`: Vertical layout (stacked widgets)
- `row-reverse` / `column-reverse`: Reverse order

**Justify Content** (main axis alignment):
- `flex-start`: Align to start
- `center`: Center alignment
- `space-between`: Spread with space between
- `space-around`: Spread with space around

**Align Items** (cross axis alignment):
- `flex-start`: Align to top/left
- `center`: Center alignment
- `flex-end`: Align to bottom/right
- `stretch`: Fill container

**Wrapping**:
- `nowrap`: Single line (default)
- `wrap`: Allow wrapping to multiple lines (essential for responsive grids)

---

## Performance Optimization

### Minimize DOM Elements

**Critical Rule**: Reduce containers and widgets to the absolute minimum needed.

**Real-World Example (Traditional Sections)**:
```
BEFORE (Poor Performance):
- 9 sections
- 31 columns
- 5 inner sections
- 44 widgets
- Lighthouse Score: 73/100

AFTER (Optimized with Sections):
- 6 sections
- 7 columns
- 0 inner sections
- 16 widgets
- Lighthouse Score: 98/100

AFTER (Optimized with Containers) ⭐:
- 6 containers
- 0 columns needed
- 0 nested containers (or max 3 for complex layouts)
- 16 widgets
- Lighthouse Score: 98/100
- BONUS: Even fewer DOM nodes than sections
```

**Performance Budget (Flexbox Containers)**:
```
✅ Target Metrics:
- Containers: ≤10
- Nested Containers: ≤3 (only for complex layouts)
- Widgets: ≤30
- Lighthouse Performance: 90+ (ideal: 95+)

❌ Warning Signs:
- >15 containers = too many content divisions
- >5 nested containers = over-nesting
- >40 widgets = replace with specialized widgets
```

### Optimization Strategies

1. **Replace Multiple Widgets with Single Specialized Widgets**:
   ```
   ❌ Image + Heading + Text + Button = 4 widgets
   ✅ Call to Action widget = 1 widget

   ❌ Icon + Heading + Text = 3 widgets
   ✅ Icon Box widget = 1 widget

   ❌ Multiple Image widgets in columns = 6+ widgets
   ✅ Image Carousel widget = 1 widget
   ```

2. **🚨 CRITICAL: Native Elementor FREE Widgets ONLY**:

   **FORBIDDEN (Zero Tolerance)**:
   - ❌ HTML widget with custom code
   - ❌ Code widget with custom HTML/CSS
   - ❌ Shortcodes from third-party plugins
   - ❌ Custom Gutenberg/ACF blocks
   - ❌ Any custom-coded elements

   **REQUIRED (Client-Editable)**:
   - ✅ Native Elementor FREE widgets ONLY
   - ✅ Widget settings panel for styling
   - ✅ Global Colors/Fonts (CSS variables)

   **Elementor FREE Available Widgets**:
   ```
   BASIC WIDGETS:
   - Heading            (H1-H6 titles)
   - Text Editor        (WYSIWYG content)
   - Image             (Single images)
   - Video             (YouTube/Vimeo embed)
   - Button            (Call-to-action buttons)
   - Divider           (Horizontal lines)
   - Spacer            (Vertical spacing)

   MEDIA WIDGETS:
   - Image Box         (Image + heading + text)
   - Icon              (Font Awesome icons)
   - Icon Box          (Icon + heading + text) ⭐ MOST USEFUL
   - Image Carousel    (Multiple images slider)
   - Icon List         (Bulleted list with icons)

   SPECIAL WIDGETS:
   - Google Maps       (Embedded map)
   - Counter           (Animated numbers) ⭐ FOR STATS
   - Progress Bar      (Skill bars)
   - Testimonial       (Quote + author)
   - Tabs              (Tabbed content)
   - Accordion         (Collapsible sections)
   - Toggle            (Show/hide content)
   - Social Icons      (Social media links)
   - Alert             (Notice boxes)
   - Rating            (Star ratings)
   ```

   **Elementor PRO Widgets NOT Available**:
   - ❌ Call to Action (use Image Box + Button instead)
   - ❌ Price List/Table (use Text Editor + styling)
   - ❌ Animated Headline (use Heading + CSS)
   - ❌ Countdown Timer
   - ❌ Forms (use Contact Form 7 shortcode)
   - ❌ Posts/Portfolio widgets
   - ❌ Advanced Carousels

   **Why This Rule**:
   - Client MUST edit ALL content in Elementor UI
   - Custom HTML breaks visual editing
   - Maintenance requires developer for text changes
   - Security vulnerabilities
   - Performance issues
   - Breaks responsive controls

   **Design Adaptation Strategy**:
   - If design needs unavailable widget: Use closest FREE widget
   - Example: No "Call to Action" widget → Use Image Box + Button
   - Prioritize: Maintainability > Pixel-perfect accuracy
   - Overall style > Exact layout replica

3. **Image Optimization & Loading Strategy**:
   - Set image dimensions inside the widget (prevents layout shift)
   - Add ALT text for accessibility and SEO (MANDATORY)
   - Use appropriate image sizes:
     - Hero images: <150KB (optimized JPG/WebP)
     - Feature images: <50KB
     - Icons: Use icon fonts or SVG
   - **Lazy Loading** (ENABLE):
     - Enable lazy loading for below-fold images
     - Keep hero/above-fold images without lazy load
     - Enable lazy loading for videos and Lottie animations
   - **Responsive Images**:
     - Use Elementor's built-in responsive image system
     - Provide mobile-specific images when needed

4. **Font and Color Consistency**:
   - Limit to 2 font families maximum
   - Use Global Fonts and Global Colors exclusively
   - Never hardcode hex colors or font names

### Performance Testing Workflow

```bash
# 1. Open page in Incognito Mode
# 2. Open Chrome DevTools (F12)
# 3. Run Lighthouse audit
# 4. Target scores:
#    - Performance: 90+ (ideal: 95+)
#    - Accessibility: 90+
#    - Best Practices: 90+
#    - SEO: 90+
```

---

## Accessibility Best Practices

### WCAG 2.1 AA Compliance (MANDATORY)

Elementor pages must be accessible to all users, including those with disabilities.

#### 1. **Images & Alt Text**
```
✅ ALWAYS:
- Add descriptive ALT text to all images
- Use empty ALT="" for decorative images
- Describe the content/purpose, not "image of"

❌ NEVER:
- Leave ALT text empty for content images
- Use generic text like "image1.jpg"
- Repeat the same ALT text multiple times
```

#### 2. **Color Contrast**
```
✅ REQUIRED Ratios:
- Normal text (body): 4.5:1 minimum
- Large text (18pt+ or 14pt+ bold): 3:1 minimum
- Interactive elements (buttons, links): 3:1 minimum

Our Colors (Verified):
- Primary (#FABA29) on Text (#2C2C2C): ✅ Pass
- Secondary (#4F9F8B) on Accent (#FEFCF5): ✅ Pass
- Text (#2C2C2C) on Accent (#FEFCF5): ✅ Pass
```

#### 3. **Keyboard Navigation**
```
✅ ENSURE:
- All interactive elements reachable via Tab key
- Visible focus indicators (outline/ring)
- Logical tab order (top to bottom, left to right)
- Skip-to-content link for screen readers

❌ AVOID:
- tabindex values >0 (breaks natural order)
- Removing focus outlines with CSS
- Keyboard traps (modal/dropdown issues)
```

#### 4. **Semantic HTML & ARIA**
```
✅ USE:
- Proper heading hierarchy (H1 → H2 → H3, no skips)
- ARIA labels for icon-only buttons
- aria-label for screen reader context
- <nav>, <main>, <aside> landmarks (Elementor auto-generates)

EXAMPLE:
<button aria-label="Close menu">
  <i class="fa fa-times"></i>
</button>
```

#### 5. **Form Accessibility**
```
✅ REQUIRED:
- <label> for every <input>
- Error messages associated with fields (aria-describedby)
- Required fields marked (aria-required="true")
- Clear focus states on inputs

EXAMPLE (Elementor Forms):
- Enable "Required" setting
- Add field labels (not just placeholders)
- Use validation messages
```

#### 6. **Motion & Animations**
```
✅ RESPECT prefers-reduced-motion:
- Provide option to disable animations
- Use CSS: @media (prefers-reduced-motion: reduce)
- Keep essential animations subtle

❌ AVOID:
- Autoplay videos with sound
- Flashing content (seizure risk)
- Parallax effects without alternatives
```

### Accessibility Testing Tools

```bash
# 1. Lighthouse Accessibility Audit (Chrome DevTools)
# 2. axe DevTools Extension (browser extension)
# 3. WAVE Extension (webaim.org/wave/)
# 4. Keyboard-only navigation test (unplug mouse!)
# 5. Screen reader test (NVDA on Windows, VoiceOver on Mac)
```

**Target**: Lighthouse Accessibility Score 90+ (ideally 100)

---

## Widget Selection Strategy

### Decision Tree: Choosing the Right Widget

**For Text + Image Combinations**:
- **Hero Section**: Heading + Text Editor + Button + Image widgets
- **Icon with Description**: Icon Box widget (NOT separate icon + text)
- **Image with Caption**: Image Box widget
- **Logo Display**: Site Logo widget (NOT image widget)

**For Structured Content**:
- **Multiple Similar Items**: Use Carousel or Grid containers
- **Testimonials**: Testimonial Carousel widget or Icon Box in columns
- **FAQ**: Accordion widget or Toggle widget
- **Contact Info**: Icon List widget (NOT separate icon + text widgets)

**For Call-to-Actions**:
- **Simple Button**: Button widget
- **CTA with Text + Button**: Call to Action widget
- **Form + Button**: Form widget

### Header & Footer Specifics

**Header Structure** (Maximum 2 columns):
```
Column 1 (40%): Site Logo widget
Column 2 (60%): Nav Menu widget (Inline positioning)
```

**Footer Structure** (Maximum 4 columns):
```
Column 1: Text Editor (About/Copyright)
Column 2: Icon List (Contact Info)
Column 3: Icon List (Quick Links)
Column 4: Icon List (Social Media)
```

---

## Design System Implementation

### Global Colors (CRITICAL)

**Rule**: NEVER hardcode hex colors. ALWAYS use Global Colors.

**Setup in Elementor**:
```
Site Settings → Global Colors

Primary:    #FABA29 (Yellow/Gold)  → var(--e-global-color-primary)
Secondary:  #4F9F8B (Teal/Green)   → var(--e-global-color-secondary)
Text:       #2C2C2C (Dark Gray)    → var(--e-global-color-text)
Accent:     #FEFCF5 (Warm Cream)   → var(--e-global-color-accent)
```

**Usage in MCP/JSON**:
```json
{
  "settings": {
    "color": "var(--e-global-color-secondary)",
    "background_color": "var(--e-global-color-background)"
  }
}
```

### Global Fonts

**Rule**: Limit to 2 font families site-wide.

**Setup in Elementor**:
```
Site Settings → Global Fonts

Primary Heading Font:   [Font Family], Weight: 700
Secondary Heading Font: [Font Family], Weight: 600
Body Font:             [Font Family], Weight: 400
```

**Typography Scale** (Svetlinki):
```
H1: 2.75rem (44px) - clamp(2rem, 5vw, 2.75rem)
H2: 1.9rem (30.4px) - clamp(1.5rem, 4vw, 1.9rem)
H3: 1.4rem (22.4px) - clamp(1.2rem, 3vw, 1.4rem)
H4: 1.1rem (17.6px)
Body: 1rem (16px)
Line Height: 1.7 (body text)
```

### Spacing System

**Rule**: Use consistent padding and margin values.

**Spacing Scale**:
```
xs:  8px  (0.5rem)
sm:  16px (1rem)
md:  24px (1.5rem)
lg:  32px (2rem)
xl:  40px (2.5rem)
2xl: 48px (3rem)
3xl: 64px (4rem)
```

**Section Padding** (typical):
```
Desktop: Top: 64px, Bottom: 64px, Left: 20px, Right: 20px
Tablet:  Top: 48px, Bottom: 48px, Left: 15px, Right: 15px
Mobile:  Top: 32px, Bottom: 32px, Left: 15px, Right: 15px
```

---

## Common Mistakes to Avoid

### 1. Over-Nesting Sections

❌ **WRONG**:
```
Section
  └── Inner Section
       └── Inner Section
            └── Column
                 └── Widget
```

✅ **RIGHT**:
```
Section
  └── Column
       └── Widget
```

**Impact**: Each unnecessary nesting level adds ~50-100 DOM elements.

### 2. Using Empty Columns for Spacing

❌ **WRONG**:
```
Section (3 columns)
  Column 1: Empty (for spacing)
  Column 2: Content
  Column 3: Empty (for spacing)
```

✅ **RIGHT**:
```
Section (1 column)
  Column 1: Content (with padding left/right)
```

### 3. Duplicating Sections for Mobile

❌ **WRONG**:
```
Section: Desktop Hero (hidden on mobile)
Section: Mobile Hero (hidden on desktop)
```

✅ **RIGHT**:
```
Section: Hero (responsive with custom widths)
  Settings: Hide on Tablet/Mobile (specific elements only)
```

### 4. Hardcoding Colors

❌ **WRONG**:
```json
{
  "settings": {
    "color": "#F5A623"
  }
}
```

✅ **RIGHT**:
```json
{
  "settings": {
    "color": "var(--e-global-color-secondary)"
  }
}
```

### 5. Not Setting Image Dimensions

❌ **WRONG**:
```json
{
  "widgetType": "image",
  "settings": {
    "image": { "url": "..." }
  }
}
```

✅ **RIGHT**:
```json
{
  "widgetType": "image",
  "settings": {
    "image": { "url": "..." },
    "width": { "unit": "px", "size": 600 },
    "height": { "unit": "px", "size": 400 }
  }
}
```

**Benefit**: Prevents layout shift, improves Core Web Vitals.

### 6. Using Too Many Fonts

❌ **WRONG**:
```
H1: Poppins Bold
H2: Montserrat Semi-Bold
H3: Open Sans Regular
Body: Roboto Regular
Buttons: Lato Medium
```

✅ **RIGHT**:
```
Headings: Poppins (various weights)
Body: Inter (400, 600)
```

---

## Responsive Design

### Key Principles

1. **Design Mobile-First**:
   - Start with mobile layout
   - Enhance for tablet and desktop
   - Use percentage-based widths

2. **Custom Breakpoints**:
   ```
   Desktop: 1200px+
   Tablet:  768px - 1199px
   Mobile:  0px - 767px
   ```

3. **Responsive Settings Per Widget**:
   - Font size: Use `clamp()` or responsive units
   - Padding/Margin: Set different values for each breakpoint
   - Hide/Show: Use device visibility settings

4. **Column Behavior**:
   ```
   Desktop: 3 columns (33% each)
   Tablet:  2 columns (50% each)
   Mobile:  1 column (100%)
   ```

### Testing Workflow

```
1. Edit page in Elementor
2. Toggle between Desktop/Tablet/Mobile views (bottom toolbar)
3. Adjust settings per device
4. Preview in actual devices or browser DevTools
5. Test with real content (not Lorem Ipsum)
```

---

## JSON Data Structure

### Element Hierarchy

Every Elementor page is stored as JSON in WordPress post meta (`_elementor_data`):

```json
[
  {
    "id": "abc123",
    "elType": "section",
    "settings": {
      "background_color": "var(--e-global-color-background)",
      "padding": {
        "unit": "px",
        "top": "64",
        "right": "20",
        "bottom": "64",
        "left": "20"
      }
    },
    "elements": [
      {
        "id": "def456",
        "elType": "column",
        "settings": {
          "_column_size": 100
        },
        "elements": [
          {
            "id": "ghi789",
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
              "title": "Welcome",
              "header_size": "h1",
              "color": "var(--e-global-color-secondary)"
            }
          }
        ]
      }
    ]
  }
]
```

### Required Fields

**Section**:
- `id`: Unique identifier (use `uuid()` or `wp_generate_uuid4()`)
- `elType`: "section"
- `settings`: Object with section settings
- `elements`: Array of column objects

**Column**:
- `id`: Unique identifier
- `elType`: "column"
- `settings`: Object with `_column_size` (percentage)
- `elements`: Array of widget objects

**Widget**:
- `id`: Unique identifier
- `elType`: "widget"
- `widgetType`: Widget type (e.g., "heading", "text-editor", "button")
- `settings`: Object with widget-specific settings

### Meta Fields

When creating pages via MCP, set these meta fields:

```json
{
  "_elementor_edit_mode": "builder",
  "_elementor_template_type": "wp-page",
  "_elementor_version": "3.16.0",
  "_elementor_data": "[JSON array]"
}
```

---

## Programmatic Building Guidelines

### MCP Workflow for Svetlinki

**Phase 1: Structure Creation**
```
1. Create page with create_elementor_page
2. Add sections with create_elementor_section
3. Add columns with add_column_to_section
4. Add widgets with add_widget_to_section
```

**Phase 2: Content Population**
```
5. Update widget settings with update_elementor_widget
6. Add images (upload_media first, then reference ID)
7. Configure responsive settings
```

**Phase 3: Optimization**
```
8. Clear cache with clear_elementor_cache
9. Verify with get_page_structure
10. Test performance with Lighthouse
```

### Design System Checklist

Before creating any page, verify:

- [ ] Global Colors configured in Elementor
- [ ] Global Fonts configured
- [ ] Typography scale documented
- [ ] Spacing system defined
- [ ] Reference screenshots available
- [ ] Content written in Bulgarian
- [ ] Image assets prepared

### Page Creation Checklist

For each page:

- [ ] Minimal sections (aim for 6-10)
- [ ] Mostly single-column layout
- [ ] Global Colors used (no hardcoded hex)
- [ ] Global Fonts used
- [ ] Image dimensions set
- [ ] ALT text added to images
- [ ] Responsive settings configured
- [ ] Performance tested (Lighthouse 90+)
- [ ] Visual verification against reference screenshot
- [ ] Designer agent review completed
- [ ] Tester agent screenshot captured
- [ ] QA agent 21-test suite passed

---

## Quick Reference: Widget Selection

| Use Case | Widget | Alternative (Avoid) |
|----------|--------|---------------------|
| Heading | Heading | Text Editor with `<h1>` |
| Paragraph | Text Editor | Multiple Heading widgets |
| Image with Caption | Image Box | Image + Text Editor |
| Icon + Text | Icon Box | Icon + Heading + Text |
| Button | Button | Text Editor with link |
| CTA with Text | Call to Action | Multiple widgets |
| Contact Info | Icon List | Multiple Icon + Text |
| Testimonial | Testimonial | Image + Text + Heading |
| FAQ | Accordion | Multiple Heading + Text |
| Gallery | Gallery | Multiple Image widgets |
| Logo | Site Logo | Image widget |
| Navigation | Nav Menu | Text Editor with links |
| Form | Form | Third-party plugin |
| Divider | Divider | Empty sections |
| Spacer | Spacer | Empty columns |

---

## Key Mantras for Svetlinki Build

> **"Minimize DOM elements. Every section, column, and widget adds weight."**

> **"Global Colors and Global Fonts only. No exceptions."**

> **"Use specialized widgets. Don't build with primitives."**

> **"Single columns by default. Only add columns when content requires side-by-side layout."**

> **"Performance first. Beauty without speed is failure."**

> **"Responsive by design, not by duplication."**

---

## Performance Targets

### Lighthouse Scores (Minimum)

```
Performance:       90+ (Target: 95+)
Accessibility:     90+
Best Practices:    90+
SEO:              90+
```

### DOM Element Budget

```
Per Page Maximum:
- Sections:        10
- Columns:         15
- Inner Sections:   0 (avoid completely)
- Widgets:        30
```

### Image Budget

```
Hero Image:        150KB max
Feature Images:     50KB max
Icons:             10KB max (or use icon fonts)
Total Page Weight: 1.5MB max
```

---

## Verification Process

### Designer Agent Review

After creating each page, run:

```
Designer agent should verify:
1. Global Colors used correctly (no hardcoded hex)
2. Global Fonts applied consistently
3. Typography scale followed
4. Spacing system adhered to
5. Visual match to reference screenshot
6. No unnecessary sections/columns
7. Optimal widget selection
8. Responsive design working
```

### Tester Agent Verification

```
Tester agent should capture:
1. Desktop screenshot (1920x1080)
2. Tablet screenshot (768px)
3. Mobile screenshot (375px)
4. Compare to reference screenshots
5. Identify visual discrepancies
6. Report performance metrics
```

### QA Agent 21-Test Suite

```
QA agent should test:
1. Global Colors compliance
2. Global Fonts compliance
3. Performance score (Lighthouse)
4. Accessibility (WCAG AA)
5. Responsive breakpoints
6. Image optimization
7. Form functionality (if applicable)
8. Navigation working
9. Links working
10. SEO metadata present
... [21 total tests]
```

---

## References

**Official Documentation**:
- Elementor Developers: https://developers.elementor.com/
- Elementor GitHub: https://github.com/elementor/elementor
- Elementor Help Center: https://elementor.com/help/

**Research Sources**:
- Layout Optimization Best Practices (via r.jina)
- Essential Addons Best Practices (via r.jina)
- Elementor GitHub Architecture (via r.jina)

**Project-Specific**:
- Svetlinki Global Colors: ELEMENTOR-GLOBAL-COLORS-SETUP.md
- Agent Configuration: AGENT-CONFIGURATION-SUMMARY.md
- Context Restoration: RESTORE-CONTEXT-PROMPT.md

---

**Document Version**: 1.0
**Last Updated**: 2025-11-28
**Maintained by**: Claude (via r.jina research)
**Status**: Production Reference
