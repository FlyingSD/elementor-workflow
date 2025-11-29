# STATIC_RULES.md - Elementor Development Static Rules

**Document Type**: Consolidated Technical Reference
**Created**: 2025-11-29
**Purpose**: Single source of truth for Elementor development rules, JSON structures, and workflows
**Source Files Merged**:
- ELEMENTOR-CORE-PRINCIPLES.md (932 lines)
- JSON-GENERATION-TOOLS-GUIDE.md (941 lines)
- ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md (848 lines)
- MCP-PAGE-CREATION-CHECKLIST.md (750 lines)

**Total Content**: 3471 lines merged and organized
**Status**: Production Reference - Read sections on-demand using anchor links

---

## Table of Contents

Jump to specific sections:
1. [Core Principles & Widget Whitelist](#core-principles) - From ELEMENTOR-CORE-PRINCIPLES.md
2. [JSON Generation Tools](#json-tools) - From JSON-GENERATION-TOOLS-GUIDE.md
3. [Database Schema Deep Dive](#database-schema) - From ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md
4. [MCP Page Creation Checklist](#mcp-checklist) - From MCP-PAGE-CREATION-CHECKLIST.md

---


<a name="core-principles"></a>
## Core Principles & Widget Whitelist

**Source**: `SSOT/ELEMENTOR-CORE-PRINCIPLES.md`

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



<a name="json-tools"></a>
## JSON Generation Tools

**Source**: `SSOT/JSON-GENERATION-TOOLS-GUIDE.md`

---


## Table of Contents

1. [Overview](#overview)
2. [Recommended MCP Servers](#recommended-mcp-servers)
3. [JSON Schema Validator MCP](#json-schema-validator-mcp)
4. [JSON Manipulation MCP](#json-manipulation-mcp)
5. [Elementor JSON Structure Templates](#elementor-json-structure-templates)
6. [Workflow Integration](#workflow-integration)
7. [Usage Examples](#usage-examples)

---

## Overview

### The Challenge

Creating Elementor pages programmatically via MCP requires generating complex JSON structures:

```json
[
  {
    "id": "uuid",
    "elType": "section",
    "settings": { /* complex nested object */ },
    "elements": [ /* nested columns */ ]
  }
]
```

**Problems**:
- Manual JSON creation is error-prone
- Structure must be valid JSON Schema
- Elementor has specific required fields
- Deep nesting increases complexity
- Global Color/Font variables must be used correctly

### The Solution

Use specialized MCP servers to:
1. **Validate** JSON structure against schemas
2. **Generate** JSON from templates
3. **Manipulate** existing JSON structures
4. **Schema-validate** before sending to Elementor

---

## Recommended MCP Servers

### 1. JSON Schema Validator MCP ⭐ (BEST OPTION)

**Repository**: https://github.com/EienWolf/jsonshema_mcp
**Purpose**: Generate, validate, and manage JSON schemas
**Best For**: Creating Elementor JSON with validation

**Key Features**:
- ✅ Generate JSON schemas from example data
- ✅ Validate JSON against schemas
- ✅ Store schema collections
- ✅ Full JSON Schema Draft 2020-12 compliance
- ✅ Fallback to local file storage (no PostgreSQL required)

**Why This is Best for Svetlinki**:
- Can create Elementor JSON schema once, reuse for all pages
- Validates JSON before sending to WordPress
- Prevents malformed data from breaking pages
- Works offline with file storage

### 2. JSON Manipulation MCP (Alternative)

**Repository**: https://github.com/GongRzhe/JSON-MCP-Server
**Purpose**: Query and manipulate JSON via JSONPath
**Best For**: Modifying existing Elementor JSON

**Key Features**:
- ✅ JSONPath queries
- ✅ Filter, map, transform operations
- ✅ Array/object manipulation
- ✅ Aggregate functions

**Use Case for Svetlinki**:
- Extract sections from existing pages
- Modify widget settings in bulk
- Clone and transform page structures

### 3. Elementor JSON Generator (Web Tool)

**URL**: https://theresanaiforthat.com/@markwryte/elementor-json-generator/
**Purpose**: AI-powered Elementor JSON generation
**Best For**: Quick prototyping

**Limitations**:
- ❌ Not an MCP server (manual web tool)
- ❌ No Claude Code integration
- ❌ Must copy/paste output

**Use Case**:
- Generate initial structure ideas
- Quick validation of structure concepts
- Not recommended for production workflow

---

## JSON Schema Validator MCP

### Installation

#### Step 1: Install Server

```bash
# Clone repository
git clone https://github.com/EienWolf/jsonshema_mcp.git
cd jsonshema_mcp

# Install dependencies
pip install -r requirements.txt

# Test server
python mcp_server.py
```

#### Step 2: Configure Claude Code

**Windows** - Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "elementor-wordpress": {
      "command": "npx",
      "args": ["wp-elementor-mcp"],
      "env": {
        "ELEMENTOR_MCP_MODE": "standard",
        "WORDPRESS_BASE_URL": "http://svetlinkielementor.local",
        "WORDPRESS_USERNAME": "test",
        "WORDPRESS_APPLICATION_PASSWORD": "S27q 64rq oFhf TPDA 30nB hNM5"
      }
    },
    "json-schema-validator": {
      "command": "python",
      "args": ["C:\\Users\\denit\\path\\to\\jsonshema_mcp\\mcp_server.py"]
    }
  }
}
```

**Notes**:
- Replace path with actual location
- No PostgreSQL needed (uses local file storage)
- Restart Claude Code after configuration

### Available Tools

#### 1. `generate_schema` - Create Schema from Example

**Purpose**: Generate a JSON schema from example Elementor JSON.

**Usage**:
```javascript
// First, create example Elementor structure
const exampleSection = {
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
  "elements": []
};

// Generate schema
generate_schema({
  json_data: JSON.stringify(exampleSection),
  schema_name: "elementor_section",
  description: "Schema for Elementor section element"
});
```

**Output**: JSON schema that can validate future sections.

#### 2. `validate_json_schema` - Validate Before Sending

**Purpose**: Ensure JSON is valid before sending to WordPress.

**Usage**:
```javascript
// Validate section before creating page
validate_json_schema({
  json_data: JSON.stringify(newSection),
  schema: elementorSectionSchema
});

// If valid, proceed to create
if (validation.valid) {
  create_elementor_section({
    page_id: 21,
    settings: newSection.settings,
    columns: 1
  });
}
```

#### 3. `add_update_schema` - Store Reusable Schemas

**Purpose**: Save Elementor component schemas for reuse.

**Usage**:
```javascript
// Create schema collection
add_update_schema({
  collection: "elementor",
  schema_id: "section",
  schema: sectionSchema,
  description: "Elementor section structure"
});

add_update_schema({
  collection: "elementor",
  schema_id: "widget_heading",
  schema: headingWidgetSchema,
  description: "Heading widget structure"
});

add_update_schema({
  collection: "elementor",
  schema_id: "widget_icon_box",
  schema: iconBoxWidgetSchema,
  description: "Icon Box widget structure"
});
```

#### 4. `validate_json_from_collections` - Validate Against Stored Schema

**Purpose**: Quick validation using stored schemas.

**Usage**:
```javascript
// Validate new heading widget
validate_json_from_collections({
  json_data: JSON.stringify(newHeading),
  collection: "elementor",
  schema_id: "widget_heading"
});
```

#### 5. `list_schemas` - View Available Schemas

**Purpose**: List all stored schemas for reference.

**Usage**:
```javascript
list_schemas({
  collection: "elementor"
});
// Returns: ["section", "widget_heading", "widget_icon_box", ...]
```

---

## JSON Manipulation MCP

### Installation

```bash
# Install via npm (global)
npm install -g @gongrzhe/server-json-mcp

# Or run via npx
npx @gongrzhe/server-json-mcp
```

### Configure Claude Code

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "elementor-wordpress": { /* existing */ },
    "json-schema-validator": { /* existing */ },
    "json-manipulation": {
      "command": "npx",
      "args": ["@gongrzhe/server-json-mcp"]
    }
  }
}
```

### Use Cases for Elementor

#### Extract All Headings from a Page

```javascript
// Get page Elementor data
const pageData = await get_elementor_data({ page_id: 21 });

// Query all heading widgets
query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..elements[?(@.widgetType=='heading')]"
});
```

#### Find All Hardcoded Colors

```javascript
// Query for hex color values (should be replaced with Global Colors)
query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)]"
});
```

#### Clone Section and Modify Settings

```javascript
// Get specific section
const section = await query_json({
  path: "$.elements[0]"  // First section
});

// Modify background color
filter_json({
  json_data: JSON.stringify(section),
  path: "$.settings.background_color",
  operation: "set",
  value: "var(--e-global-color-background)"
});
```

---

## Elementor JSON Structure Templates

### Template 1: Basic Section with Single Column

```json
{
  "id": "{{ uuid() }}",
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
      "id": "{{ uuid() }}",
      "elType": "column",
      "settings": {
        "_column_size": 100
      },
      "elements": []
    }
  ]
}
```

**JSON Schema** (for validation):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "elType", "settings", "elements"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier"
    },
    "elType": {
      "type": "string",
      "enum": ["section"],
      "description": "Element type must be 'section'"
    },
    "settings": {
      "type": "object",
      "properties": {
        "background_color": {
          "type": "string",
          "pattern": "^var\\(--e-global-color-.*\\)$",
          "description": "Must use Global Color CSS variable"
        },
        "padding": {
          "type": "object",
          "properties": {
            "unit": { "type": "string", "enum": ["px", "rem", "%"] },
            "top": { "type": "string" },
            "right": { "type": "string" },
            "bottom": { "type": "string" },
            "left": { "type": "string" }
          }
        }
      }
    },
    "elements": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/column"
      }
    }
  },
  "definitions": {
    "column": {
      "type": "object",
      "required": ["id", "elType", "settings", "elements"],
      "properties": {
        "id": { "type": "string" },
        "elType": { "type": "string", "enum": ["column"] },
        "settings": {
          "type": "object",
          "properties": {
            "_column_size": {
              "type": "number",
              "minimum": 0,
              "maximum": 100
            }
          }
        },
        "elements": {
          "type": "array",
          "description": "Array of widgets"
        }
      }
    }
  }
}
```

### Template 2: Heading Widget

```json
{
  "id": "{{ uuid() }}",
  "elType": "widget",
  "widgetType": "heading",
  "settings": {
    "title": "{{ content }}",
    "header_size": "h1",
    "color": "var(--e-global-color-secondary)",
    "typography_typography": "custom",
    "typography_font_size": {
      "unit": "rem",
      "size": "2.75"
    },
    "typography_font_size_tablet": {
      "unit": "rem",
      "size": "2"
    },
    "typography_font_size_mobile": {
      "unit": "rem",
      "size": "1.5"
    }
  }
}
```

**JSON Schema**:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "elType", "widgetType", "settings"],
  "properties": {
    "id": { "type": "string" },
    "elType": {
      "type": "string",
      "enum": ["widget"]
    },
    "widgetType": {
      "type": "string",
      "enum": ["heading"]
    },
    "settings": {
      "type": "object",
      "required": ["title", "header_size"],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1,
          "description": "Heading text content"
        },
        "header_size": {
          "type": "string",
          "enum": ["h1", "h2", "h3", "h4", "h5", "h6"],
          "description": "HTML heading tag"
        },
        "color": {
          "type": "string",
          "pattern": "^var\\(--e-global-color-.*\\)$",
          "description": "Must use Global Color"
        },
        "typography_font_size": {
          "type": "object",
          "properties": {
            "unit": { "type": "string", "enum": ["rem", "px", "em"] },
            "size": { "type": ["string", "number"] }
          }
        }
      }
    }
  }
}
```

### Template 3: Icon Box Widget

```json
{
  "id": "{{ uuid() }}",
  "elType": "widget",
  "widgetType": "icon-box",
  "settings": {
    "icon": {
      "value": "fas fa-lightbulb",
      "library": "fa-solid"
    },
    "title_text": "{{ title }}",
    "description_text": "{{ description }}",
    "icon_color": "var(--e-global-color-accent)",
    "icon_size": {
      "unit": "px",
      "size": "48"
    },
    "title_color": "var(--e-global-color-secondary)",
    "description_color": "var(--e-global-color-text)"
  }
}
```

---

## Workflow Integration

### Recommended Workflow: Schema-First Approach

#### Phase 1: Create Schemas (One-Time Setup)

```javascript
// 1. Create example Elementor structures
const exampleSection = { /* ... */ };
const exampleHeading = { /* ... */ };
const exampleIconBox = { /* ... */ };

// 2. Generate schemas
generate_schema({
  json_data: JSON.stringify(exampleSection),
  schema_name: "section",
  description: "Elementor section"
});

generate_schema({
  json_data: JSON.stringify(exampleHeading),
  schema_name: "widget_heading",
  description: "Heading widget"
});

// 3. Store in collection
add_update_schema({
  collection: "elementor_svetlinki",
  schema_id: "section",
  schema: generatedSectionSchema
});
```

#### Phase 2: Build Pages with Validation

```javascript
// 1. Construct page JSON
const newPage = {
  sections: [
    {
      id: generateUUID(),
      elType: "section",
      settings: {
        background_color: "var(--e-global-color-background)",
        padding: { unit: "px", top: "64", right: "20", bottom: "64", left: "20" }
      },
      elements: [
        {
          id: generateUUID(),
          elType: "column",
          settings: { _column_size: 100 },
          elements: [
            {
              id: generateUUID(),
              elType: "widget",
              widgetType: "heading",
              settings: {
                title: "Образователен център Светлинки",
                header_size: "h1",
                color: "var(--e-global-color-secondary)"
              }
            }
          ]
        }
      ]
    }
  ]
};

// 2. Validate each component
for (const section of newPage.sections) {
  const valid = await validate_json_from_collections({
    json_data: JSON.stringify(section),
    collection: "elementor_svetlinki",
    schema_id: "section"
  });

  if (!valid.is_valid) {
    console.error("Validation failed:", valid.errors);
    return;  // Stop if invalid
  }
}

// 3. If valid, create page
create_elementor_page({
  title: "За Нас",
  slug: "about",
  elementor_data: JSON.stringify(newPage.sections)
});
```

#### Phase 3: Audit Existing Pages

```javascript
// 1. Get existing page
const pageData = await get_elementor_data({ page_id: 21 });

// 2. Validate entire page structure
const validation = await validate_json_from_collections({
  json_data: JSON.stringify(pageData),
  collection: "elementor_svetlinki",
  schema_id: "page"
});

// 3. Find hardcoded colors
const hardcodedColors = await query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)]"
});

// 4. Generate optimization report
console.log("Validation:", validation.is_valid ? "PASS" : "FAIL");
console.log("Hardcoded colors found:", hardcodedColors.length);
```

---

## Usage Examples

### Example 1: Create Home Page Hero Section

```javascript
// Define hero structure
const heroSection = {
  id: "hero-" + Date.now(),
  elType: "section",
  settings: {
    background_color: "var(--e-global-color-background)",
    padding: {
      unit: "px",
      top: "80",
      right: "20",
      bottom: "80",
      left: "20"
    }
  },
  elements: [
    {
      id: "hero-col-" + Date.now(),
      elType: "column",
      settings: { _column_size: 100 },
      elements: [
        {
          id: "hero-heading-" + Date.now(),
          elType: "widget",
          widgetType: "heading",
          settings: {
            title: "Образователен център Светлинки",
            header_size: "h1",
            color: "var(--e-global-color-secondary)",
            typography_font_size: { unit: "rem", size: "2.75" }
          }
        },
        {
          id: "hero-text-" + Date.now(),
          elType: "widget",
          widgetType: "text-editor",
          settings: {
            editor: "<p>Развиваме умовете на бъдещето чрез ментална аритметика</p>",
            text_color: "var(--e-global-color-text)"
          }
        },
        {
          id: "hero-button-" + Date.now(),
          elType: "widget",
          widgetType: "button",
          settings: {
            text: "Запиши се за пробен урок",
            button_type: "primary",
            background_color: "var(--e-global-color-secondary)",
            hover_background_color: "var(--e-global-color-accent)"
          }
        }
      ]
    }
  ]
};

// Validate
const isValid = await validate_json_from_collections({
  json_data: JSON.stringify(heroSection),
  collection: "elementor_svetlinki",
  schema_id: "section"
});

if (isValid.is_valid) {
  // Create page with hero
  create_elementor_page({
    title: "Home",
    slug: "home",
    elementor_data: JSON.stringify([heroSection])
  });
}
```

### Example 2: Audit and Fix Hardcoded Colors

```javascript
// 1. Get all pages
const pages = await get_pages({ per_page: 100 });

// 2. For each page, find hardcoded colors
for (const page of pages) {
  const pageData = await get_elementor_data({ page_id: page.id });

  // Find hardcoded colors
  const violations = await query_json({
    url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
    path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)].color"
  });

  if (violations.length > 0) {
    console.log(`Page ${page.id} (${page.title}): ${violations.length} hardcoded colors found`);
    console.log("Violations:", violations);

    // Map hex colors to Global Colors
    const colorMap = {
      "#6366f1": "var(--e-global-color-primary)",
      "#F5A623": "var(--e-global-color-secondary)",
      "#2c2c2c": "var(--e-global-color-text)",
      "#FDB913": "var(--e-global-color-accent)",
      "#fefcf5": "var(--e-global-color-background)"
    };

    // Fix automatically (requires iteration through widgets)
    // ... implementation details
  }
}
```

### Example 3: Clone and Modify Section

```javascript
// 1. Get existing section from About page
const aboutData = await get_elementor_data({ page_id: 23 });
const missionSection = aboutData.elements[1];  // Second section

// 2. Clone structure
const clonedSection = JSON.parse(JSON.stringify(missionSection));

// 3. Modify IDs (make unique)
clonedSection.id = "cloned-" + Date.now();
clonedSection.elements.forEach(col => {
  col.id = "cloned-col-" + Date.now();
  col.elements.forEach(widget => {
    widget.id = "cloned-widget-" + Date.now();
  });
});

// 4. Modify content
if (clonedSection.elements[0].elements[0].widgetType === "heading") {
  clonedSection.elements[0].elements[0].settings.title = "Нашата визия";
}

// 5. Validate
const valid = await validate_json_from_collections({
  json_data: JSON.stringify(clonedSection),
  collection: "elementor_svetlinki",
  schema_id: "section"
});

// 6. Add to another page
if (valid.is_valid) {
  // Get current page data
  const programsData = await get_elementor_data({ page_id: 25 });
  programsData.elements.push(clonedSection);

  // Update page
  update_elementor_data({
    page_id: 25,
    elementor_data: JSON.stringify(programsData.elements)
  });
}
```

---

## Best Practices

### 1. Always Validate Before Creating

```javascript
// ✅ GOOD
const valid = await validate_json_schema({ json_data, schema });
if (valid.is_valid) {
  create_elementor_page({ ... });
}

// ❌ BAD
create_elementor_page({ ... });  // No validation
```

### 2. Use Schema Collections for Organization

```javascript
// Organize by component type
add_update_schema({ collection: "elementor_sections", schema_id: "hero" });
add_update_schema({ collection: "elementor_sections", schema_id: "features" });
add_update_schema({ collection: "elementor_widgets", schema_id: "heading" });
add_update_schema({ collection: "elementor_widgets", schema_id: "icon_box" });
```

### 3. Store Reusable Templates

```javascript
// Create library of validated templates
const templates = {
  hero_section: await generate_schema({ ... }),
  features_section: await generate_schema({ ... }),
  cta_section: await generate_schema({ ... })
};

// Save to file for reuse
fs.writeFileSync("elementor-templates.json", JSON.stringify(templates));
```

### 4. Automate Validation in CI/CD

```python
# Python script for automated validation
import json

def validate_all_pages():
    pages = [21, 23, 25, 27, 29, 31, 33, 35]
    results = []

    for page_id in pages:
        page_data = get_elementor_data(page_id)
        validation = validate_json_from_collections(
            json_data=json.dumps(page_data),
            collection="elementor_svetlinki",
            schema_id="page"
        )
        results.append({
            "page_id": page_id,
            "valid": validation.is_valid,
            "errors": validation.errors
        })

    return results

# Run before deployment
results = validate_all_pages()
if not all(r["valid"] for r in results):
    print("Validation failed! Cannot deploy.")
    exit(1)
```

---

## Summary

### Key Takeaways

1. **Use JSON Schema Validator MCP** for:
   - Generating schemas from examples
   - Validating JSON before creating pages
   - Storing reusable component schemas

2. **Use JSON Manipulation MCP** for:
   - Querying existing page structures
   - Finding hardcoded values (colors, fonts)
   - Bulk modifications

3. **Schema-First Workflow**:
   - Create schemas once (one-time setup)
   - Validate every JSON structure before use
   - Store templates for common components

4. **Benefits**:
   - ✅ Prevents malformed JSON
   - ✅ Catches Global Color/Font violations early
   - ✅ Ensures consistency across all pages
   - ✅ Enables automated auditing
   - ✅ Reduces debugging time

### Next Steps

1. **Install JSON Schema Validator MCP** (priority)
2. **Create Elementor component schemas** (section, column, widgets)
3. **Validate existing pages** (find issues)
4. **Build new pages with validation** (prevent issues)

---

**Document Version**: 1.0
**Last Updated**: 2025-11-28
**Research Method**: r.jina.ai web search and repository analysis
**Status**: Production Ready - Recommended for Implementation



<a name="database-schema"></a>
## Database Schema Deep Dive

**Source**: `SSOT/ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md`

---


## 🧬 The DNA of Elementor: JSON Structure

### Core Concept

**Elementor does NOT save HTML. It saves JSON.**

When you open a page, Elementor reads the JSON and generates HTML dynamically.
If Claude understands this JSON, it can generate entire pages without opening the editor.

---

## 📍 Database Storage Locations

### Table: `wp_postmeta`

| Meta Key | Purpose | Format | Required |
|----------|---------|--------|----------|
| `_elementor_data` | **Main builder content** (page structure) | JSON string (slash-escaped) | ✅ Yes |
| `_elementor_page_settings` | **Page configuration** (template, title visibility) | Serialized PHP array | ⚠️ Conditional |
| `_elementor_edit_mode` | **Builder flag** (marks post as Elementor-built) | String: `"builder"` | ✅ Yes |
| `_elementor_version` | Elementor version used | String: `"3.x.x"` | ✅ Yes |
| `_elementor_template_type` | Template type identifier | String | ⚠️ For templates |
| `_elementor_element_cache` | Cached element data | Serialized | 🔄 Auto-managed |

---

## 🏗️ The Hierarchical Structure

### Schema: Section > Column > Widget

**Elementor FREE uses Legacy Sections** (NOT Flexbox Containers - those are PRO only!)

```
Page
└── Section (elType: "section")
    └── Column (elType: "column") [MANDATORY wrapper]
        └── Widget (elType: "widget")
            ├── Heading
            ├── Text Editor
            ├── Button
            ├── Counter
            └── [29 FREE widgets total]
```

---

## 📐 Complete JSON Schema

### Basic Structure Template

```json
[
  {
    "id": "abc123",
    "elType": "section",
    "settings": {
      "stretch_section": "section-stretched",
      "layout": "full_width",
      "gap": "no",
      "height": "min-height",
      "custom_height": {
        "unit": "vh",
        "size": 85,
        "sizes": []
      },
      "column_position": "middle",
      "content_position": "",
      "html_tag": "section",
      "background_background": "classic",
      "background_color": "var(--e-global-color-accent)",
      "padding": {
        "unit": "px",
        "top": 120,
        "right": 40,
        "bottom": 120,
        "left": 40,
        "isLinked": false
      }
    },
    "elements": [
      {
        "id": "def456",
        "elType": "column",
        "settings": {
          "_column_size": 100,
          "_inline_size": null,
          "content_position": ""
        },
        "elements": [
          {
            "id": "ghi789",
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
              "title": "Развийте Математическите Умения на Вашето Дете",
              "header_size": "h1",
              "title_color": "var(--e-global-color-secondary)",
              "align": "center",
              "typography_typography": "custom",
              "typography_font_size": {
                "unit": "px",
                "size": 48,
                "sizes": []
              },
              "typography_font_weight": "700"
            }
          }
        ]
      }
    ]
  }
]
```

---

## 🔑 Critical Properties Explained

### Section Properties (elType: "section")

| Property | Type | Values | Default | Purpose |
|----------|------|--------|---------|---------|
| `stretch_section` | string | `""` or `"section-stretched"` | `""` | **Full-width edge-to-edge** (1920px viewport) |
| `layout` | string | `"boxed"` or `"full_width"` | `"boxed"` | Content width constraint |
| `gap` | string | `"default"`, `"no"`, `"narrow"`, `"extended"`, `"wide"`, `"wider"`, `"custom"` | `"default"` | Column spacing |
| `height` | string | `"default"`, `"full"`, `"min-height"` | `"default"` | Section height mode |
| `custom_height` | object | `{unit, size, sizes}` | - | Height value when `height: "min-height"` |
| `column_position` | string | `"top"`, `"middle"`, `"bottom"`, `"stretch"` | `"middle"` | Vertical column alignment |
| `content_position` | string | Flexbox values | `""` | Content vertical alignment |
| `html_tag` | string | `"div"`, `"header"`, `"footer"`, `"main"`, `"article"`, `"section"`, `"aside"`, `"nav"` | `"section"` | Semantic HTML element |
| `background_background` | string | `"classic"`, `"gradient"`, `"video"`, `"slideshow"` | - | Background type |
| `background_color` | string | CSS color or `var(--e-global-color-*)` | - | Background color |
| `padding` | object | `{unit, top, right, bottom, left, isLinked}` | `{}` | Section padding |
| `margin` | object | `{unit, top, right, bottom, left, isLinked}` | `{}` | Section margin |

### Column Properties (elType: "column")

| Property | Type | Values | Default | Purpose |
|----------|------|--------|---------|---------|
| `_column_size` | number | 0-100 | 100 | Column width percentage (generates CSS class `elementor-col-{value}`) |
| `_inline_size` | number/null | 2-98 or null | null | Responsive width override (`width: {{VALUE}}%`) |
| `content_position` | string | `"top"`, `"center"`, `"bottom"` | `""` | Content vertical alignment |

### Widget Properties (elType: "widget")

| Property | Type | Required | Purpose |
|----------|------|----------|---------|
| `widgetType` | string | ✅ Yes | Widget identifier (e.g., `"heading"`, `"text-editor"`, `"button"`) |
| `settings` | object | ✅ Yes | Widget-specific configuration |

---

## 🎨 Widget-Specific Settings (Property Names)

### Heading Widget (`widgetType: "heading"`)

```json
{
  "title": "Heading Text",
  "header_size": "h1",
  "title_color": "var(--e-global-color-secondary)",
  "align": "center",
  "typography_typography": "custom",
  "typography_font_size": {"unit": "px", "size": 48, "sizes": []},
  "typography_font_weight": "700",
  "typography_line_height": {"unit": "em", "size": 1.2, "sizes": []}
}
```

**Critical**: Property is `title_color` NOT `color`!

### Text Editor Widget (`widgetType: "text-editor"`)

```json
{
  "editor": "<p>HTML content here</p>",
  "text_color": "var(--e-global-color-text)",
  "align": "center",
  "typography_typography": "custom",
  "typography_font_size": {"unit": "px", "size": 16, "sizes": []},
  "typography_line_height": {"unit": "em", "size": 1.7, "sizes": []}
}
```

**Critical**: Property is `text_color` NOT `color`!

### Button Widget (`widgetType: "button"`)

```json
{
  "text": "Button Text",
  "button_type": "success",
  "link": {"url": "/contact", "is_external": false, "nofollow": false},
  "button_text_color": "#FFFFFF",
  "background_color": "var(--e-global-color-primary)",
  "border_radius": {"unit": "px", "size": 8, "sizes": []},
  "padding": {"unit": "px", "top": 15, "right": 30, "bottom": 15, "left": 30, "isLinked": false},
  "align": "center"
}
```

**Critical**: Property is `button_text_color` NOT `text_color` or `color`!

### Counter Widget (`widgetType: "counter"`)

```json
{
  "starting_number": 0,
  "ending_number": 500,
  "duration": 2000,
  "thousand_separator": "",
  "thousand_separator_char": ",",
  "title": "Ученици",
  "number_color": "var(--e-global-color-primary)",
  "title_color": "var(--e-global-color-secondary)",
  "number_size": {"unit": "px", "size": 48, "sizes": []},
  "title_size": {"unit": "px", "size": 16, "sizes": []}
}
```

**Critical**: `number_color` and `title_color` are separate properties!

### Image Widget (`widgetType: "image"`)

```json
{
  "image": {"url": "path/to/image.jpg", "id": 123},
  "image_size": "full",
  "caption": "Image caption",
  "align": "center",
  "width": {"unit": "%", "size": 100, "sizes": []},
  "link": {"url": "", "is_external": false}
}
```

---

## 💾 Database Serialization

### How JSON is Stored

**Source**: `includes/db.php`

```php
// Storage (BEFORE saving to database)
$json_string = json_encode($elementor_data);
$slashed_json = wp_slash($json_string);  // ⚠️ CRITICAL: Adds backslashes
update_post_meta($post_id, '_elementor_data', $slashed_json);

// Retrieval (AFTER reading from database)
$slashed_json = get_post_meta($post_id, '_elementor_data', true);
$json_string = wp_unslash($slashed_json);  // Remove backslashes
$elementor_data = json_decode($json_string, true);
```

**Why Slashing?**: WordPress escapes special characters for database security.

**Quote from source**: *"The elementor JSON needs slashes before saving."*

---

## 🔧 Page Settings Structure

### Meta Key: `_elementor_page_settings`

**Storage Format**: Serialized PHP array

**Critical Settings**:

```php
[
    'template' => 'elementor_header_footer',  // ⚠️ This is "Elementor Full Width"
    'hide_title' => 'yes',                    // Hides default page title
    'page_layout' => '',                      // Empty for default, or custom layout
    'status' => 'publish'                     // Publication status
]
```

### Template Options

| Value | UI Label | Effect |
|-------|----------|--------|
| `""` (empty) | Default | Shows header/footer, content in theme container |
| `"elementor_canvas"` | Canvas | **Removes** header/footer, full blank page |
| `"elementor_header_footer"` | Elementor Full Width | **Keeps** header/footer, content edge-to-edge |

**Critical**: `elementor_header_footer` ≠ Full-width sections!
- `template: elementor_header_footer` → Removes theme container
- `stretch_section: 'section-stretched'` → Makes section 1920px wide

**You need BOTH for true full-width design!**

---

## 🚀 Programmatic Page Creation (PHP)

### Complete Example: Create Page with Elementor

```php
<?php
// Step 1: Create WordPress post
$post_id = wp_insert_post([
    'post_title' => 'Home',
    'post_status' => 'publish',
    'post_type' => 'page'
]);

// Step 2: Mark as Elementor page
update_post_meta($post_id, '_elementor_edit_mode', 'builder');

// Step 3: Set Elementor version
update_post_meta($post_id, '_elementor_version', '3.18.0');

// Step 4: Configure page settings
update_post_meta($post_id, '_elementor_page_settings', [
    'template' => 'elementor_header_footer',  // Full-width template
    'hide_title' => 'yes'                     // Hide default title
]);

// Step 5: Build page structure
$elementor_data = [
    [
        'id' => uniqid(),
        'elType' => 'section',
        'settings' => [
            'stretch_section' => 'section-stretched',  // Edge-to-edge
            'layout' => 'full_width',
            'background_color' => 'var(--e-global-color-accent)',
            'padding' => [
                'unit' => 'px',
                'top' => 120,
                'right' => 40,
                'bottom' => 120,
                'left' => 40,
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => uniqid(),
                'elType' => 'column',
                'settings' => ['_column_size' => 100],
                'elements' => [
                    [
                        'id' => uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Welcome to Svetlinki',
                            'header_size' => 'h1',
                            'title_color' => 'var(--e-global-color-secondary)',
                            'align' => 'center'
                        ]
                    ]
                ]
            ]
        ]
    ]
];

// Step 6: Save with proper escaping
$json_string = json_encode($elementor_data);
$slashed_json = wp_slash($json_string);
update_post_meta($post_id, '_elementor_data', $slashed_json);

// Step 7: Clear Elementor cache
\Elementor\Plugin::$instance->files_manager->clear_cache();

echo "Page created: ID $post_id\n";
```

---

## 🔄 Cache Management

### PHP Method (Programmatic)

```php
// Clear all Elementor CSS cache
\Elementor\Plugin::$instance->files_manager->clear_cache();
```

### WP-CLI Method (Terminal)

```bash
# Regenerate all Elementor CSS files
wp elementor flush-css

# After database changes, always flush cache!
```

**When to Clear Cache**:
- ✅ After updating `_elementor_data` via REST API or direct DB
- ✅ After changing Global Colors/Fonts
- ✅ After modifying page settings
- ✅ When changes don't appear on frontend

---

## 🎯 CSS Class Reference (for "Blind" Styling)

### Unchangeable Elementor Classes

```css
/* Section wrapper */
.elementor-section {
  /* Always present on sections */
}

.elementor-section-stretched {
  /* Added when stretch_section: 'section-stretched' */
  /* JavaScript stretches to 1920px */
}

/* Content container inside section */
.elementor-container {
  /* This is the 645px box that needed fixing! */
  /* With stretch, becomes full-width */
}

/* Column wrapper */
.elementor-column {
  /* Base column class */
}

.elementor-col-100 {
  /* Full-width column (_column_size: 100) */
}

.elementor-col-50 {
  /* Half-width column (_column_size: 50) */
}

/* Widget wrapper */
.elementor-widget {
  /* Base widget class */
}

.elementor-widget-heading {
  /* Heading widget specifically */
}

.elementor-widget-text-editor {
  /* Text editor widget specifically */
}

.elementor-widget-button {
  /* Button widget specifically */
}

/* Inner wrappers */
.elementor-widget-wrap {
  /* Column inner wrapper */
}

.elementor-element-populated {
  /* Column with content */
}
```

---

## 📋 System Prompt for Claude (AI Automation Context)

```
You are acting as an Elementor Automation Engineer. Use the following internal logic:

**Content Storage**:
- Data stored in wp_postmeta table
- Key _elementor_data: Contains layout JSON (Sections > Columns > Widgets)
- Key _elementor_edit_mode: Must be set to 'builder'
- Key _elementor_version: Elementor version used

**Data Format**:
- JSON structure: Array of sections, each with nested columns and widgets
- Each element has: id (unique), elType, settings, elements (children array)
- JSON must be wp_slash()'ed before database storage
- JSON must be wp_unslash()'ed after database retrieval

**Page Attributes**:
To fix layout issues programmatically, modify _elementor_page_settings meta key:
- Set 'template' => 'elementor_header_footer' for Full Width (keeps header/footer)
- Set 'template' => 'elementor_canvas' for Canvas (removes header/footer)
- Set 'hide_title' => 'yes' to remove default page title

**Full-Width Sections**:
- Use stretch_section: 'section-stretched' in section settings
- Use layout: 'full_width' for content width
- Requires CSS Print Method = "Internal Embedding" on .local domains

**Widget Property Names** (CRITICAL):
- Heading: title_color (NOT color)
- Text Editor: text_color (NOT color)
- Button: button_text_color (NOT color or text_color)
- Counter: number_color and title_color (separate)

**Cache Clearing**:
Use wp elementor flush-css via CLI or:
\Elementor\Plugin::$instance->files_manager->clear_cache() via PHP
when layout changes don't appear.

**Architecture** (Elementor FREE):
- MUST use Legacy Sections: Section > Column > Widget
- DO NOT use Containers (elType: 'container' - PRO only!)
- Column is MANDATORY wrapper inside section
```

---

## ✅ Validation Checklist

Before saving Elementor data, verify:

- ☐ Every section has at least one column
- ☐ Every column has `_column_size` property
- ☐ Every widget has `widgetType` property
- ☐ All IDs are unique (use `uniqid()` in PHP or UUID in JavaScript)
- ☐ Settings objects exist (can be empty `{}`)
- ☐ Nested elements use `elements` array (not `children`)
- ☐ Colors use CSS variables: `var(--e-global-color-*)`
- ☐ JSON is properly escaped with `wp_slash()` before save
- ☐ `_elementor_edit_mode` set to `'builder'`
- ☐ Cache cleared after changes

---

## 🚨 Common Pitfalls

### 1. Wrong Property Names
```json
// ❌ WRONG
{"color": "#000000"}

// ✅ CORRECT (depends on widget)
{"title_color": "#000000"}       // Heading widget
{"text_color": "#000000"}        // Text Editor widget
{"button_text_color": "#000000"} // Button widget
```

### 2. Missing Column Wrapper
```json
// ❌ WRONG (widget directly in section)
{
  "elType": "section",
  "elements": [
    {"elType": "widget", "widgetType": "heading"}
  ]
}

// ✅ CORRECT (widget in column in section)
{
  "elType": "section",
  "elements": [
    {
      "elType": "column",
      "settings": {"_column_size": 100},
      "elements": [
        {"elType": "widget", "widgetType": "heading"}
      ]
    }
  ]
}
```

### 3. Using Containers (PRO Feature)
```json
// ❌ WRONG (FREE version)
{"elType": "container"}

// ✅ CORRECT (FREE version)
{"elType": "section"}
```

### 4. Not Clearing Cache
```php
// ❌ WRONG
update_post_meta($post_id, '_elementor_data', $data);
// Changes not visible!

// ✅ CORRECT
update_post_meta($post_id, '_elementor_data', $data);
\Elementor\Plugin::$instance->files_manager->clear_cache();
// Now visible!
```

### 5. Forgetting wp_slash()
```php
// ❌ WRONG (may corrupt quotes/backslashes)
update_post_meta($post_id, '_elementor_data', json_encode($data));

// ✅ CORRECT
update_post_meta($post_id, '_elementor_data', wp_slash(json_encode($data)));
```

---

## 📋 STRICT WHITELIST: Elementor FREE Widgets Only

### ⚠️ CRITICAL: Widget Type Validation

**Rule**: When generating `widgetType` for Elementor JSON, you are **STRICTLY LIMITED** to Elementor FREE widgets.

**DO NOT use PRO widgets** - they will cause render failures!

### ✅ ALLOWED widgetType VALUES (FREE Version)

#### 1. Basics (Basic Elements)

| widgetType | Name | Use Case |
|------------|------|----------|
| `heading` | Heading | H1-H6 headings |
| `image` | Image | Single image display |
| `text-editor` | Text Editor | Rich text content (HTML) |
| `video` | Video | YouTube/Vimeo/Self-hosted video |
| `button` | Button | Call-to-action buttons |
| `divider` | Divider | Horizontal separator line |
| `spacer` | Spacer | Vertical empty space |
| `google_maps` | Google Maps | Embedded map |
| `icon` | Icon | Single icon display |

#### 2. General (Composite Widgets)

| widgetType | Name | Use Case |
|------------|------|----------|
| `image-box` | Image Box | Image + Heading + Text (card-style) |
| `icon-box` | Icon Box | Icon + Heading + Text (services/features) |
| `star-rating` | Star Rating | Rating display (1-5 stars) |
| `image-carousel` | Image Carousel | Rotating image slider |
| `image-gallery` | Image Gallery | Multi-image grid gallery |
| `icon-list` | Icon List | List with icons (checklists, features) |
| `counter` | Counter | Animated number counter (e.g., "500+ Students") |
| `progress` | Progress Bar | Percentage progress bar |
| `testimonial` | Testimonial | Client review/testimonial |
| `tabs` | Tabs | Tabbed content sections |
| `accordion` | Accordion | Collapsible FAQ panels |
| `toggle` | Toggle | Like accordion, all can be open |
| `social-icons` | Social Icons | Social media icon links |
| `alert` | Alert | Colored message box |
| `audio` | Audio | Audio player |
| `shortcode` | Shortcode | WordPress shortcode embedder |
| `html` | HTML | Custom HTML/JS code |
| `menu-anchor` | Menu Anchor | Scroll anchor point |
| `sidebar` | Sidebar | Theme sidebar insertion |
| `read-more` | Read More | "Read More" button for archives |

**Total FREE Widgets**: 29

---

### ❌ FORBIDDEN widgetType VALUES (PRO Only)

These will **FAIL** in Elementor FREE:

| widgetType | Name | Why Forbidden |
|------------|------|---------------|
| `form` | Elementor Forms | PRO feature |
| `login` | Login Form | PRO feature |
| `nav-menu` | Navigation Menu | PRO feature |
| `slides` | Slides | PRO feature |
| `animated-headline` | Animated Headline | PRO feature |
| `price-list` | Price List | PRO feature |
| `price-table` | Price Table | PRO feature |
| `flip-box` | Flip Box | PRO feature |
| `call-to-action` | Call to Action | PRO feature |
| `media-carousel` | Media Carousel | PRO feature |
| `posts` | Posts | PRO feature |
| `portfolio` | Portfolio | PRO feature |
| `gallery` | Gallery (PRO version) | PRO feature |

**If a PRO feature is needed**: Simulate using `html` widget or combine `image-box`/`icon-box` with custom CSS.

---

### 🔒 System Prompt for Claude (Widget Enforcement)

```
STRICT RULE: ELEMENTOR FREE WIDGETS ONLY

When generating the widgetType for the Elementor JSON structure, you are strictly limited to the ELEMENTOR FREE version.

DO NOT use Pro widgets (e.g., form, login, nav-menu, slides, animated-headline, price-list, flip-box, call-to-action, media-carousel, posts, portfolio).

Using these will cause the render to FAIL.

ALLOWED widgetType VALUES:

Basics: heading, image, text-editor, video, button, divider, spacer, google_maps, icon

General: image-box, icon-box, star-rating, image-carousel, image-gallery, icon-list, counter, progress, testimonial, tabs, accordion, toggle, social-icons, alert, audio, shortcode, html, menu-anchor, sidebar, read-more

If a requested feature requires a Pro widget:
- Simulate using `html` widget with custom code
- OR combine image-box/icon-box with CSS styling
- OR use Contact Form 7 plugin for forms (via shortcode widget)

NEVER hallucinate Pro widgets or unknown widget types!
```

---

## 🏗️ Architecture Note: Containers vs Sections

### Legacy Structure (Elementor FREE - Default)

```
elType: "section"
  └── elType: "column"
      └── elType: "widget"
```

**Used when**: Elementor FREE version, backward compatibility

**Characteristics**:
- Column is **MANDATORY** wrapper
- Section has layout constraints (boxed/full_width)
- Requires `_column_size` property
- Uses CSS float/grid layout

**Example**:
```json
{
  "elType": "section",
  "elements": [
    {
      "elType": "column",
      "settings": {"_column_size": 100},
      "elements": [
        {"elType": "widget", "widgetType": "heading"}
      ]
    }
  ]
}
```

---

### Modern Structure (Flexbox Containers - PRO Feature!)

```
elType: "container"
  └── elType: "widget"
```

**Used when**: Elementor PRO, Flexbox experiment enabled

**Characteristics**:
- No column wrapper needed
- Direct widget placement in container
- Flexbox-based layout (flex-direction, justify-content, align-items)
- More flexible and modern

**Example**:
```json
{
  "elType": "container",
  "settings": {
    "flex_direction": "column",
    "flex_gap": {"size": 20, "unit": "px"}
  },
  "elements": [
    {"elType": "widget", "widgetType": "heading"},
    {"elType": "widget", "widgetType": "text-editor"}
  ]
}
```

**⚠️ CRITICAL**: For our Svetlinki project using Elementor FREE, we **MUST use Legacy Sections**!

**Reason**: Flexbox Containers are Elementor PRO feature only. Using `elType: "container"` in FREE will fail!

---

### How to Determine Which to Use

**Check Elementor Version**:
```php
// In WordPress
$elementor_version = get_option('elementor_version');
$is_pro = defined('ELEMENTOR_PRO_VERSION');

if ($is_pro && version_compare($elementor_version, '3.12', '>=')) {
    // Can use Containers
} else {
    // Must use Sections
}
```

**For Svetlinki Project**: ✅ Use Legacy Sections (Section > Column > Widget)

---

### Container Settings (PRO Only - For Reference)

If you ever upgrade to PRO, here are container settings:

```json
{
  "elType": "container",
  "settings": {
    "content_width": "full",
    "flex_direction": "column",
    "flex_wrap": "wrap",
    "flex_gap": {"size": 20, "unit": "px"},
    "justify_content": "center",
    "align_items": "center",
    "padding": {
      "unit": "px",
      "top": 60,
      "right": 40,
      "bottom": 60,
      "left": 40,
      "isLinked": false
    }
  }
}
```

---

## 📖 References

**Source Files Analyzed**:
- `includes/db.php` - Database manager
- `core/base/document.php` - Document base class
- `includes/elements/section.php` - Section element
- `includes/elements/column.php` - Column element
- `includes/base/widget-base.php` - Widget base class

**GitHub Repository**: https://github.com/elementor/elementor

---

**Version**: 1.0
**Created**: 2025-11-29
**Purpose**: Enable Claude Code to manipulate Elementor pages at the "DNA level" without UI
**Audience**: AI automation systems, advanced developers

**This is 1000% clean - verified from source code!** ✅



<a name="mcp-checklist"></a>
## MCP Page Creation Checklist

**Source**: `SSOT/MCP-PAGE-CREATION-CHECKLIST.md`

---


## Pre-Creation Phase

### 1. Design System Verification ✅

Before creating ANY page, verify these are configured:

- [ ] **Global Colors configured** in Elementor Site Settings
  - Primary: #FABA29 (Yellow/Gold)
  - Secondary: #4F9F8B (Teal/Green)
  - Text: #2C2C2C (Dark Gray)
  - Accent: #FEFCF5 (Warm Cream)

- [ ] **Global Fonts configured** in Elementor Site Settings
  - Primary Heading Font
  - Secondary Heading Font
  - Body Font

- [ ] **Typography Scale documented**
  - H1: 2.75rem, H2: 1.9rem, H3: 1.4rem
  - Body: 1rem, Line Height: 1.7

- [ ] **Spacing System defined**
  - Section padding values
  - Widget margin/padding scale

### 2. Content Preparation 📝

- [ ] **Content written** in Bulgarian
- [ ] **Reference screenshot** available (check `2025-11-26-current-state/`)
- [ ] **Page structure planned** (sections mapped out)
- [ ] **Images prepared** and uploaded to media library
  - Hero image optimized (<150KB)
  - Feature images optimized (<50KB)
  - ALT text prepared for all images

### 3. MCP Connection Verification 🔌

```bash
# Test MCP connection
curl -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/wp/v2/pages?per_page=1"
```

- [ ] MCP server responding
- [ ] Authentication working
- [ ] WordPress REST API accessible

---

## Page Creation Phase

### Step 1: Create Base Page Structure 🏗️

**MCP Tool**: `create_elementor_page` or `create_page`

**Checklist**:
- [ ] Page title in Bulgarian
- [ ] Slug set (lowercase, hyphens)
- [ ] Status: `draft` (until complete)
- [ ] Meta fields set:
  ```json
  {
    "_elementor_edit_mode": "builder",
    "_elementor_template_type": "wp-page",
    "_elementor_version": "3.16.0"
  }
  ```

**Example Command**:
```javascript
// Via MCP
create_page({
  title: "За Нас",
  slug: "about",
  status: "draft",
  meta: {
    "_elementor_edit_mode": "builder",
    "_elementor_template_type": "wp-page"
  }
})
```

### Step 2: Plan Section Structure 📐

**CRITICAL**: Apply minimalism principle from ELEMENTOR-CORE-PRINCIPLES.md

**Target Budget**:
- Sections: 6-10 maximum
- Columns: 15 maximum
- Inner Sections: 0 (avoid completely)
- Widgets: 30 maximum

**Section Planning Template**:
```
Page: [Page Name]
Target Section Count: [6-10]

Section 1: [Purpose] - [# Columns]
  └── Widget count: [estimate]

Section 2: [Purpose] - [# Columns]
  └── Widget count: [estimate]

... continue for all sections

TOTAL: [#] sections, [#] columns, [#] widgets
✅ Under budget? Yes/No
```

### Step 3: Create Sections 🎯

**MCP Tool**: `create_elementor_section`

**For Each Section**:

- [ ] **Section background** set (use Global Colors)
  ```json
  {
    "background_color": "var(--e-global-color-background)"
  }
  ```

- [ ] **Section padding** configured
  ```json
  {
    "padding": {
      "unit": "px",
      "top": "64",
      "right": "20",
      "bottom": "64",
      "left": "20"
    }
  }
  ```

- [ ] **Column count** justified
  - 1 column: Default (80% of sections)
  - 2 columns: Text + image, split content
  - 3 columns: Feature grids only
  - 4 columns: Special cases only

- [ ] **Column sizes** set (percentage)
  ```json
  {
    "_column_size": 50  // For 2-column: 50/50
  }
  ```

**Example**:
```javascript
create_elementor_section({
  page_id: 21,
  settings: {
    background_color: "var(--e-global-color-background)",
    padding: {
      unit: "px",
      top: "64",
      right: "20",
      bottom: "64",
      left: "20"
    }
  },
  columns: 1
})
```

### Step 4: Add Widgets 🧩

**MCP Tool**: `add_widget_to_section`

**Widget Selection Decision Tree**:

1. **Is it text + image + button?**
   - ✅ Use: Call to Action widget
   - ❌ Don't use: Separate Heading + Text + Button + Image

2. **Is it icon + heading + text?**
   - ✅ Use: Icon Box widget
   - ❌ Don't use: Separate Icon + Heading + Text

3. **Is it just a heading?**
   - ✅ Use: Heading widget
   - ❌ Don't use: Text Editor with `<h1>`

4. **Is it paragraph text?**
   - ✅ Use: Text Editor widget
   - ❌ Don't use: Multiple Heading widgets

5. **Is it a list of items with icons?**
   - ✅ Use: Icon List widget
   - ❌ Don't use: Multiple Icon + Text widgets

6. **Is it multiple images?**
   - ✅ Use: Gallery or Image Carousel widget
   - ❌ Don't use: Multiple Image widgets in columns

**For Each Widget**:

- [ ] **Widget type** selected from decision tree
- [ ] **Global Colors** used (never hardcoded hex)
  ```json
  {
    "color": "var(--e-global-color-secondary)"
  }
  ```

- [ ] **Typography** follows scale
  ```json
  {
    "header_size": "h1",  // or h2, h3, etc.
    "typography_typography": "custom",
    "typography_font_size": {
      "unit": "rem",
      "size": "2.75"
    }
  }
  ```

- [ ] **Image dimensions** set (if applicable)
  ```json
  {
    "image": { "url": "...", "id": 123 },
    "width": { "unit": "px", "size": 600 },
    "height": { "unit": "px", "size": 400 }
  }
  ```

- [ ] **ALT text** added (if image widget)
  ```json
  {
    "image": { "url": "...", "alt": "Описание на изображението" }
  }
  ```

**Example**:
```javascript
add_widget_to_section({
  page_id: 21,
  section_id: "abc123",
  column_index: 0,
  widget_type: "heading",
  settings: {
    "title": "Образователен център Светлинки",
    "header_size": "h1",
    "color": "var(--e-global-color-secondary)",
    "typography_font_size": {
      "unit": "rem",
      "size": "2.75"
    }
  }
})
```

### Step 5: Configure Responsive Settings 📱

**MCP Tool**: `update_elementor_widget`

**For Each Widget**:

- [ ] **Desktop settings** configured (default)
- [ ] **Tablet settings** configured (768px-1199px)
  ```json
  {
    "typography_font_size_tablet": {
      "unit": "rem",
      "size": "2"
    }
  }
  ```

- [ ] **Mobile settings** configured (0-767px)
  ```json
  {
    "typography_font_size_mobile": {
      "unit": "rem",
      "size": "1.5"
    }
  }
  ```

- [ ] **Hide on devices** (if needed)
  ```json
  {
    "hide_desktop": "",  // Show
    "hide_tablet": "yes", // Hide
    "hide_mobile": "yes"  // Hide
  }
  ```

**Section Padding - Responsive Example**:
```json
{
  "padding": {
    "unit": "px",
    "top": "64",
    "right": "20",
    "bottom": "64",
    "left": "20"
  },
  "padding_tablet": {
    "unit": "px",
    "top": "48",
    "right": "15",
    "bottom": "48",
    "left": "15"
  },
  "padding_mobile": {
    "unit": "px",
    "top": "32",
    "right": "15",
    "bottom": "32",
    "left": "15"
  }
}
```

---

## Verification Phase

### Step 6: Technical Verification ✅

**MCP Tool**: `get_page_structure`

- [ ] **Page structure retrieved** successfully
- [ ] **Section count** within budget (≤10)
- [ ] **Column count** within budget (≤15)
- [ ] **Widget count** within budget (≤30)
- [ ] **No inner sections** (should be 0)

**Example**:
```javascript
get_page_structure({ page_id: 21 })
// Review output for element counts
```

### Step 7: Clear Cache 🗑️

**MCP Tool**: `clear_elementor_cache_by_page`

- [ ] **Elementor CSS cache cleared**
- [ ] **WordPress object cache cleared** (if applicable)

```javascript
clear_elementor_cache_by_page({ page_id: 21 })
```

### Step 8: Designer Agent Review 🎨

**Agent**: Designer

**Verification Checklist**:
- [ ] **Global Colors compliance**
  - No hardcoded hex values (`#6366f1` → `var(--e-global-color-primary)`)
  - All colors use CSS variables

- [ ] **Global Fonts compliance**
  - No hardcoded font names
  - Typography scale followed

- [ ] **Visual match to reference screenshot**
  - Layout matches
  - Spacing consistent
  - Colors accurate

- [ ] **Responsive design working**
  - Desktop view correct
  - Tablet view correct
  - Mobile view correct

**Command**:
```bash
# Spawn Designer agent via Task tool
Task: "Review page ID 21 (Home) for Global Design System compliance and visual match to reference screenshot at 2025-11-26-current-state/homepage.png"
```

### Step 9: Tester Agent Verification 📸

**Agent**: Tester (Playwright)

**Capture Screenshots**:
- [ ] **Desktop screenshot** (1920x1080)
- [ ] **Tablet screenshot** (768px)
- [ ] **Mobile screenshot** (375px)
- [ ] **Compare to reference screenshots**
- [ ] **Document discrepancies**

**Command**:
```bash
# Spawn Tester agent via Task tool
Task: "Capture screenshots of page at http://svetlinkielementor.local/about/ at desktop (1920x1080), tablet (768px), and mobile (375px). Compare to reference screenshot at 2025-11-26-current-state/about.png"
```

### Step 10: Performance Testing 🚀

**Tool**: Chrome DevTools Lighthouse

**Manual Steps**:
```
1. Open page in Chrome Incognito
2. F12 → Lighthouse tab
3. Select: Performance, Accessibility, Best Practices, SEO
4. Run audit
```

**Target Scores**:
- [ ] **Performance**: 90+ (ideal: 95+)
- [ ] **Accessibility**: 90+
- [ ] **Best Practices**: 90+
- [ ] **SEO**: 90+

**If scores below target**:
- Review DOM element count (aim to reduce)
- Check image optimization (compress further)
- Review CSS/JS loading (eliminate unused)
- Check font loading (limit to 2 families)

### Step 11: QA Agent 21-Test Suite ✅

**Agent**: QA

**Test Categories**:
- [ ] Global Colors compliance (no hardcoded hex)
- [ ] Global Fonts compliance
- [ ] Performance score (Lighthouse 90+)
- [ ] Accessibility (WCAG AA)
- [ ] Responsive breakpoints working
- [ ] Image optimization verified
- [ ] Form functionality (if applicable)
- [ ] Navigation working
- [ ] Internal links working
- [ ] External links working (open in new tab)
- [ ] SEO metadata present (title, description)
- [ ] Open Graph tags present
- [ ] Schema markup present (if applicable)
- [ ] Page load time (<3 seconds)
- [ ] No JavaScript errors in console
- [ ] No CSS errors
- [ ] Cross-browser compatibility (Chrome, Firefox, Safari)
- [ ] Mobile usability
- [ ] Content accuracy (Bulgarian text correct)
- [ ] Visual consistency with design system
- [ ] No broken images

**Command**:
```bash
# Spawn QA agent via Task tool
Task: "Run comprehensive 21-test suite on page ID 21 (Home) at http://svetlinkielementor.local/. Report pass/fail for each test category."
```

---

## Publication Phase

### Step 12: Final Review 👀

**Human Review** (User):
- [ ] Content reviewed for accuracy
- [ ] Images display correctly
- [ ] Links work as expected
- [ ] No typos in Bulgarian text
- [ ] Page meets business requirements

### Step 13: Publish Page 🚀

**MCP Tool**: `update_page`

```javascript
update_page({
  page_id: 21,
  status: "publish"
})
```

- [ ] Status changed from `draft` to `publish`
- [ ] Page URL confirmed
- [ ] Page accessible on frontend

### Step 14: Documentation 📋

**Update Progress Tracker**:
- [ ] Mark page as complete in `02-PROGRESS-TRACKER.md`
- [ ] Update page completion percentage
- [ ] Document any issues or optimizations
- [ ] Add notes for future reference

**Example Entry**:
```markdown
| Page | Status | Sections | Widgets | Lighthouse | Notes |
|------|--------|----------|---------|------------|-------|
| Home | ✅ Complete | 5 | 18 | 96/100 | Optimized from original design |
```

---

## Post-Creation Optimization

### Optional: Further Optimization 🔧

If Lighthouse score < 95:

- [ ] **Reduce sections** (combine related content)
- [ ] **Reduce widgets** (use specialized widgets)
- [ ] **Optimize images** (compress further, use WebP)
- [ ] **Remove unused CSS** (Elementor settings)
- [ ] **Enable lazy loading** (videos, images below fold)
- [ ] **Minify CSS/JS** (Elementor performance settings)

### Optional: Accessibility Audit ♿

- [ ] **Keyboard navigation** working
- [ ] **Screen reader** friendly (test with NVDA/JAWS)
- [ ] **Color contrast** meets WCAG AA (4.5:1 for text)
- [ ] **Alt text** present on all images
- [ ] **Form labels** present (if forms exist)
- [ ] **ARIA labels** added where needed

---

## Quick Reference: MCP Tools

| Phase | Tool | Purpose |
|-------|------|---------|
| Create | `create_page` | Create WordPress page |
| Create | `create_elementor_page` | Create page with Elementor data |
| Structure | `create_elementor_section` | Add section to page |
| Structure | `add_column_to_section` | Add column to section |
| Content | `add_widget_to_section` | Add widget to column |
| Content | `update_elementor_widget` | Modify widget settings |
| Media | `upload_media` | Upload image to media library |
| Media | `get_media` | List media library items |
| Verify | `get_page_structure` | Get page element hierarchy |
| Verify | `get_elementor_data` | Get full Elementor JSON |
| Cache | `clear_elementor_cache` | Clear global cache |
| Cache | `clear_elementor_cache_by_page` | Clear page-specific cache |
| List | `get_pages` | List all pages |
| Update | `update_page` | Update page status/meta |

---

## Troubleshooting

### Issue: Page Not Displaying Correctly

**Checklist**:
- [ ] Clear Elementor cache
- [ ] Clear browser cache (Ctrl+Shift+Delete)
- [ ] Regenerate Elementor CSS (Elementor → Tools → Regenerate CSS)
- [ ] Check WordPress permalink structure (Settings → Permalinks → Save)
- [ ] Verify Elementor edit mode is set (`_elementor_edit_mode: builder`)

### Issue: Global Colors Not Applying

**Checklist**:
- [ ] Verify Global Colors configured in Elementor Site Settings
- [ ] Check CSS variable syntax: `var(--e-global-color-primary)`
- [ ] Clear Elementor cache
- [ ] Regenerate CSS files
- [ ] Check for hardcoded hex values (find/replace)

### Issue: Performance Score Low

**Checklist**:
- [ ] Count DOM elements (aim for <30 widgets)
- [ ] Optimize images (compress, resize, use WebP)
- [ ] Remove unused widgets
- [ ] Combine sections where possible
- [ ] Use specialized widgets instead of combinations
- [ ] Enable Improved Asset Loading (Elementor → Settings → Features)

### Issue: MCP Connection Fails

**Checklist**:
- [ ] Test WordPress REST API manually (curl command)
- [ ] Verify Application Password correct
- [ ] Check WordPress URL matches: `http://svetlinkielementor.local`
- [ ] Restart Claude Code
- [ ] Check Local site is running in LocalWP

---

## Example: Complete Page Creation Flow

### Scenario: Create "About" Page

**1. Pre-Creation**:
```bash
# Verify Global Colors configured
# Reference screenshot: 2025-11-26-current-state/about.png
# Content prepared in Bulgarian
# Images uploaded to media library
```

**2. Create Base Page**:
```javascript
create_page({
  title: "За Нас",
  slug: "about",
  status: "draft",
  meta: {
    "_elementor_edit_mode": "builder",
    "_elementor_template_type": "wp-page"
  }
})
// Returns: { id: 23 }
```

**3. Plan Structure**:
```
Section 1: Hero (1 column) - 3 widgets
  - Heading (H1)
  - Text Editor (intro)
  - Image

Section 2: Mission (2 columns) - 2 widgets
  - Column 1: Text Editor (mission statement)
  - Column 2: Image

Section 3: Values (1 column) - 1 widget
  - Icon Box (3 values in single widget)

TOTAL: 3 sections, 4 columns, 6 widgets ✅ Under budget
```

**4. Create Sections**:
```javascript
// Section 1: Hero
create_elementor_section({
  page_id: 23,
  settings: {
    background_color: "var(--e-global-color-background)",
    padding: { unit: "px", top: "64", right: "20", bottom: "64", left: "20" }
  },
  columns: 1
})
// Returns: { section_id: "abc123" }

// Section 2: Mission
create_elementor_section({
  page_id: 23,
  settings: { background_color: "var(--e-global-color-background)" },
  columns: 2
})
// Returns: { section_id: "def456" }

// Section 3: Values
create_elementor_section({
  page_id: 23,
  settings: { background_color: "var(--e-global-color-background)" },
  columns: 1
})
// Returns: { section_id: "ghi789" }
```

**5. Add Widgets**:
```javascript
// Section 1 widgets
add_widget_to_section({
  page_id: 23,
  section_id: "abc123",
  column_index: 0,
  widget_type: "heading",
  settings: {
    title: "За Нас",
    header_size: "h1",
    color: "var(--e-global-color-secondary)"
  }
})

add_widget_to_section({
  page_id: 23,
  section_id: "abc123",
  column_index: 0,
  widget_type: "text-editor",
  settings: {
    editor: "<p>Образователен център Светлинки...</p>"
  }
})

// ... continue for all widgets
```

**6. Configure Responsive**:
```javascript
update_elementor_widget({
  page_id: 23,
  widget_id: "widget123",
  settings: {
    typography_font_size_tablet: { unit: "rem", size: "2" },
    typography_font_size_mobile: { unit: "rem", size: "1.5" }
  }
})
```

**7. Verify & Test**:
```javascript
// Get structure
get_page_structure({ page_id: 23 })

// Clear cache
clear_elementor_cache_by_page({ page_id: 23 })

// Spawn Designer agent
// Spawn Tester agent
// Run Lighthouse audit
// Spawn QA agent
```

**8. Publish**:
```javascript
update_page({
  page_id: 23,
  status: "publish"
})
```

**9. Document**:
```markdown
✅ About page complete - 3 sections, 6 widgets, Lighthouse 94/100
```

---

## Summary: Key Success Factors

1. ✅ **Plan before creating** (section structure, widget count)
2. ✅ **Minimize elements** (6-10 sections, <30 widgets)
3. ✅ **Use Global Colors exclusively** (no hardcoded hex)
4. ✅ **Use specialized widgets** (don't combine primitives)
5. ✅ **Set image dimensions** (prevents layout shift)
6. ✅ **Configure responsive settings** (don't duplicate sections)
7. ✅ **Test thoroughly** (Designer, Tester, QA agents)
8. ✅ **Target Lighthouse 90+** (performance first)
9. ✅ **Document completion** (update progress tracker)

---

**Document Version**: 1.0
**Last Updated**: 2025-11-28
**Reference**: ELEMENTOR-CORE-PRINCIPLES.md
**Status**: Production Workflow Guide


