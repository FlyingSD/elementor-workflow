# Svetlinkelementor - Fresh Elementor Build Guide

**Project:** Recreate Svetlinki website using Elementor from scratch
**Approach:** New LocalWP site, fresh installation, visual recreation
**Goal:** Match colors & architecture using Elementor principles

**Created:** November 28, 2025
**Status:** Ready to Build

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Phase 1: LocalWP Setup](#phase-1-localwp-setup)
3. [Phase 2: Elementor Installation & Configuration](#phase-2-elementor-installation--configuration)
4. [Phase 3: Visual Design Recreation](#phase-3-visual-design-recreation)
5. [Phase 4: Claude Code MCP Integration](#phase-4-claude-code-mcp-integration)
6. [Design System Reference](#design-system-reference)
7. [Page-by-Page Recreation Guide](#page-by-page-recreation-guide)

---

## Project Overview

### What We're Building

**NEW Site:** `svetlinkelementor` (LocalWP)
**Technology:** WordPress + Elementor (fresh install)
**Goal:** Visually identical to svetlinki3, built with Elementor principles

### What We're NOT Doing

❌ Migrating existing files
❌ Using Kadence Theme
❌ Using Gutenberg blocks
❌ Copying HTML templates

### What We ARE Doing

✅ Fresh WordPress installation
✅ Elementor as primary page builder
✅ Recreate visual design using Elementor widgets
✅ Match colors, fonts, spacing, layout
✅ Build foundation for AI automation via MCP

### Benefits of This Approach

- 🎯 Clean slate - no legacy code
- 🎓 Learn Elementor properly
- 🧪 Safe testing environment
- 🤖 Perfect for MCP integration
- 🔄 Easy to iterate and improve

---

## Phase 1: LocalWP Setup

### Step 1: Create New Site in LocalWP

**Time:** 5 minutes

1. **Open LocalWP**
   ```
   Click the "+" button (Add New Site)
   ```

2. **Site Configuration**
   ```
   Site Name: svetlinkelementor
   Domain: svetlinkelementor.local

   Environment:
   - PHP Version: 8.2.x (Latest)
   - Web Server: nginx
   - Database: MySQL 8.0.x
   ```

3. **WordPress Setup**
   ```
   WordPress Username: admin
   WordPress Password: [secure password]
   WordPress Email: [your email]
   ```

4. **Start Site**
   ```
   Wait for LocalWP to provision the site
   Click "Admin" to open WordPress dashboard
   ```

### Step 2: Basic WordPress Configuration

**Time:** 5 minutes

1. **General Settings**
   ```
   WordPress Admin → Settings → General

   Site Title: Светлинки (Test)
   Tagline: Образователен център за ментална аритметика

   WordPress Address (URL): http://svetlinkelementor.local
   Site Address (URL): http://svetlinkelementor.local

   Site Language: Български
   Timezone: Sofia
   Date Format: d.m.Y
   ```

2. **Permalink Structure**
   ```
   Settings → Permalinks

   Select: Post name
   Custom Structure: /%postname%/

   Save Changes
   ```

3. **Delete Default Content**
   ```
   Posts → All Posts → Delete "Hello world!"
   Pages → All Pages → Delete "Sample Page"
   Comments → Delete default comment
   ```

### Step 3: Choose Theme

**Option A: Hello Elementor (Recommended)**
```
Appearance → Themes → Add New
Search: "Hello Elementor"
Install & Activate

Why: Minimal, lightweight, designed for Elementor
```

**Option B: Kadence Theme (If you want consistency)**
```
Appearance → Themes → Add New
Search: "Kadence"
Install & Activate

Why: Familiar, you already know it, fast
```

**Recommendation:** Use **Hello Elementor** for this fresh build. It's designed specifically for Elementor and has zero bloat.

---

## Phase 2: Elementor Installation & Configuration

### Step 1: Install Elementor

**Time:** 10 minutes

1. **Install Plugin**
   ```
   Plugins → Add New
   Search: "Elementor"
   Install: "Elementor Website Builder"
   Activate
   ```

2. **Choose Elementor Free or Pro**

   **Elementor Free** (Sufficient for most needs):
   - ✅ Drag & drop page builder
   - ✅ 40+ widgets
   - ✅ Responsive editing
   - ✅ Template library
   - ✅ Theme Builder (basic)

   **Elementor Pro** ($59/year - if needed later):
   - ✅ 100+ widgets
   - ✅ Advanced Theme Builder
   - ✅ Form Builder
   - ✅ Popup Builder
   - ✅ WooCommerce Builder
   - ✅ Dynamic Content

   **Decision:** Start with **Free**, upgrade to **Pro** only if you need advanced features.

3. **Elementor Setup Wizard**
   ```
   Skip the wizard - we'll configure manually
   ```

### Step 2: Configure Elementor Global Settings

**Time:** 15 minutes

#### A. Global Colors

```
Elementor → Site Settings → Global Colors
```

**Match Svetlinki3 Colors:**

```
Primary (#6366f1)
- Color: #6366f1
- Title: Primary (Indigo)
- Usage: Main CTA buttons, links

Secondary (#F5A623)
- Color: #F5A623
- Title: Svetlinki Orange (Brand)
- Usage: Headings, accents, highlights

Text (#2c2c2c)
- Color: #2c2c2c
- Title: Dark Text
- Usage: Body text, paragraphs

Accent (#FDB913)
- Color: #FDB913
- Title: Light Orange
- Usage: Hover states, secondary CTAs

Background (#fefcf5)
- Color: #fefcf5
- Title: Warm White
- Usage: Page backgrounds, sections

Muted (#6c757d)
- Color: #6c757d
- Title: Gray Text
- Usage: Meta information, subtle text
```

#### B. Global Fonts

```
Elementor → Site Settings → Global Fonts
```

**Typography System:**

```
Primary Heading Font:
- Font Family: System Default or Poppins (if matches original)
- Weight: 700 (Bold)
- Usage: H1, H2 headings

Secondary Heading Font:
- Font Family: System Default
- Weight: 600 (Semi-Bold)
- Usage: H3, H4 headings

Body Font:
- Font Family: System Default or Inter/Roboto
- Weight: 400 (Regular)
- Line Height: 1.7
- Usage: Paragraphs, content

Accent Font:
- Font Family: (Optional) Special font
- Weight: 500 (Medium)
- Usage: Buttons, special text
```

**Note:** Check original svetlinki3 fonts:
```css
/* From original CSS variables */
--global-heading-font-family: [check this]
--global-body-font-family: [check this]
```

#### C. Global Spacing

```
Elementor → Site Settings → Layout Settings
```

```
Content Width: 1200px
Page Padding:
- Top: 20px
- Right: 20px
- Bottom: 20px
- Left: 20px

Mobile Padding:
- Top: 15px
- Right: 15px
- Bottom: 15px
- Left: 15px
```

#### D. Lightbox Settings

```
Elementor → Settings → Lightbox
```

```
Enable: Yes
Background Color: rgba(0,0,0,0.9)
UI Color: #F5A623
UI Color Hover: #FDB913
```

#### E. Performance Settings

```
Elementor → Settings → Features
```

**Disable unused features for better performance:**

```
Flexbox Container: ✅ Enable (New, better)
Grid Container: ✅ Enable
Improved Asset Loading: ✅ Enable
Improved CSS Loading: ✅ Enable

Disable:
❌ Landing Pages
❌ Display Conditions (if not needed)
❌ History (if not needed)
```

### Step 3: Create Global Style Guide

**Time:** 10 minutes

Create a reusable style guide for consistency:

1. **Create Style Guide Page**
   ```
   Pages → Add New
   Title: "Style Guide (Internal)"
   Edit with Elementor
   ```

2. **Add Style Samples**

   **Section 1: Colors**
   - Add color swatches with hex codes
   - Test primary, secondary, text colors

   **Section 2: Typography**
   - H1 through H6 examples
   - Body text samples
   - Bold, italic, links

   **Section 3: Buttons**
   - Primary button style
   - Secondary button style
   - Outlined button style

   **Section 4: Spacing**
   - Standard section padding
   - Element spacing examples

3. **Save as Template**
   ```
   Save this page as "Svetlinki Style Guide"
   Use for reference when building pages
   ```

---

## Phase 3: Visual Design Recreation

### Current Svetlinki3 Architecture Analysis

Based on the politika-poveritelnost.html file we reviewed:

#### Visual Elements:

```
┌─────────────────────────────────┐
│  HEADER                         │
│  - Logo (likely)                │
│  - Navigation menu              │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  PAGE TITLE SECTION             │
│  - H1: Page Title               │
│  - Subtitle/date                │
│  - Horizontal divider           │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  CONTENT SECTIONS               │
│  - Max-width: 900px             │
│  - Centered content             │
│  - H2 section headings          │
│  - Paragraphs                   │
│  - Lists (ul, ol)               │
│  - Dividers between sections    │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  FOOTER                         │
│  - Copyright notice             │
│  - Links                        │
└─────────────────────────────────┘
```

#### CSS Styling Patterns:

```css
/* From politika-poveritelnost.html */

Container:
- max-width: 900px
- margin: 0 auto
- padding: 2rem 1rem
- background: #fefcf5

H1:
- font-size: clamp(2rem, 5vw, 2.75rem)
- color: #F5A623
- font-weight: 700

H2:
- font-size: clamp(1.5rem, 4vw, 1.9rem)
- margin-top: 2.5rem
- border-bottom: 3px solid #F5A623
- padding-bottom: 0.5rem

Paragraphs:
- margin-bottom: 1rem
- font-size: 1rem
- line-height: 1.7

Links:
- color: #F5A623
- text-decoration: underline
- hover: #FDB913

Dividers:
- border-top: 1px solid #e0e0e0
- margin: 2rem 0
```

### Recreation Strategy

We'll recreate pages using Elementor equivalents:

| Original HTML | Elementor Widget | Configuration |
|--------------|------------------|---------------|
| `<h1>` | Heading Widget | Tag: H1, Color: #F5A623, Size: 2.75rem |
| `<h2>` | Heading Widget | Tag: H2, Border-bottom: 3px #F5A623 |
| `<p>` | Text Editor Widget | Line-height: 1.7, Color: #2c2c2c |
| `<ul>, <ol>` | Text Editor Widget | HTML lists within editor |
| `<hr>` | Divider Widget | Color: #e0e0e0, Width: 1px |
| `.container` | Section | Max-width: 900px, Centered |
| Links | Text Editor Widget | Link color: #F5A623 |

---

## Phase 4: Claude Code MCP Integration

### Step 1: Generate Application Password

**Time:** 2 minutes

1. **Navigate to WordPress Profile**
   ```
   WordPress Admin → Users → Profile
   Scroll to bottom: "Application Passwords"
   ```

2. **Create New Application Password**
   ```
   Application Name: Claude Code MCP
   Click "Add New Application Password"

   IMPORTANT: Copy the password immediately!
   Format: xxxx xxxx xxxx xxxx xxxx xxxx
   ```

3. **Store Password Securely**
   ```
   Save to password manager or secure note
   You cannot view this password again!
   ```

### Step 2: Configure Claude Code MCP

**Time:** 5 minutes

1. **Locate Claude Code Config File**

   **Windows:**
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   C:\Users\[YourName]\AppData\Roaming\Claude\claude_desktop_config.json
   ```

   **macOS:**
   ```
   ~/Library/Application Support/Claude/claude_desktop_config.json
   ```

2. **Edit Configuration**

   Add this to your `claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "svetlinkelementor": {
         "command": "npx",
         "args": ["wp-elementor-mcp"],
         "env": {
           "ELEMENTOR_MCP_MODE": "standard",
           "WORDPRESS_BASE_URL": "http://svetlinkelementor.local",
           "WORDPRESS_USERNAME": "admin",
           "WORDPRESS_APPLICATION_PASSWORD": "xxxx xxxx xxxx xxxx xxxx xxxx"
         }
       }
     }
   }
   ```

3. **Restart Claude Code**

   Close and reopen Claude Code to load the new MCP server.

### Step 3: Test MCP Connection

**Time:** 5 minutes

1. **Test Basic Connection**

   In Claude Code, say:
   ```
   "List all pages on svetlinkelementor"
   ```

   Expected response:
   ```
   Tool: get_pages
   Result: [Empty list or default pages]
   ```

2. **Test Page Creation**

   In Claude Code, say:
   ```
   "Create a test page titled 'MCP Test Page' with a simple heading and paragraph"
   ```

   Expected result:
   ```
   Page created successfully with ID: X
   URL: http://svetlinkelementor.local/mcp-test-page/
   ```

3. **Verify in WordPress**
   ```
   WordPress Admin → Pages → All Pages
   Should see "MCP Test Page"
   Click "Edit with Elementor" to verify structure
   ```

### Step 4: Create First Real Page via MCP

**Time:** 10 minutes

Let's create a simple "About" page to test the full workflow:

**Prompt for Claude Code:**

```
Create a new page titled "За Нас" (About Us) on svetlinkelementor with the following structure:

- Hero section with:
  - Heading: "Образователен център Светлинки"
  - Color: #F5A623 (Svetlinki Orange)
  - Subtitle: "Развиваме умовете на бъдещето"
  - Background: #fefcf5

- Content section with 3 columns:
  - Column 1: Icon + Heading "10+ години опит"
  - Column 2: Icon + Heading "500+ деца"
  - Column 3: Icon + Heading "Доказани резултати"

- Text section with:
  - Heading: "Нашата мисия"
  - Paragraph explaining mental math education
  - Max-width: 900px, centered

Use global colors: Primary (#6366f1), Secondary (#F5A623), Text (#2c2c2c)
```

**Expected Outcome:**
- Page created in seconds
- Fully editable in Elementor
- Matches Svetlinki design system
- Ready for further customization

---

## Design System Reference

### Color Palette (From Svetlinki3)

```css
/* Primary Colors */
--primary-indigo: #6366f1;     /* Main brand color */
--secondary-orange: #F5A623;   /* Svetlinki orange */
--accent-orange: #FDB913;      /* Light orange */

/* Text Colors */
--text-dark: #2c2c2c;          /* Main text */
--text-muted: #6c757d;         /* Secondary text */
--text-light: #ffffff;         /* White text */

/* Background Colors */
--bg-white: #ffffff;           /* Pure white */
--bg-warm: #fefcf5;           /* Warm white */
--bg-light: #f8f9fa;          /* Light gray */

/* Border Colors */
--border-light: #e0e0e0;       /* Light borders */
--border-orange: #F5A623;      /* Orange borders */

/* State Colors */
--success: #28a745;            /* Green */
--warning: #ffc107;            /* Yellow */
--error: #dc3545;              /* Red */
--info: #17a2b8;               /* Blue */
```

### Typography Scale

```css
/* Headings */
H1: 2.75rem (44px) - Page titles
H2: 1.9rem (30.4px) - Section headings
H3: 1.4rem (22.4px) - Subsection headings
H4: 1.1rem (17.6px) - Minor headings
H5: 1rem (16px) - Small headings
H6: 0.875rem (14px) - Tiny headings

/* Body */
Body: 1rem (16px)
Small: 0.875rem (14px)
Tiny: 0.75rem (12px)

/* Line Heights */
Headings: 1.2
Body: 1.7
Tight: 1.4
Loose: 2.0
```

### Spacing System

```css
/* Margin/Padding Scale */
xs: 0.5rem (8px)
sm: 1rem (16px)
md: 1.5rem (24px)
lg: 2rem (32px)
xl: 2.5rem (40px)
2xl: 3rem (48px)
3xl: 4rem (64px)

/* Section Spacing */
Section Top: 2.5rem
Section Bottom: 2rem
Element Gap: 1rem
Column Gap: 1.5rem
```

### Border & Radius

```css
/* Border Width */
Thin: 1px
Medium: 2px
Thick: 3px

/* Border Radius */
None: 0
Small: 4px
Medium: 8px
Large: 12px
Round: 50%

/* Box Shadow */
Light: 0 2px 4px rgba(0,0,0,0.1)
Medium: 0 4px 8px rgba(0,0,0,0.15)
Heavy: 0 8px 16px rgba(0,0,0,0.2)
```

---

## Page-by-Page Recreation Guide

### 1. Home Page

**Structure:**

```
┌─────────────────────────────┐
│  Hero Section               │
│  - Main heading             │
│  - Subheading               │
│  - CTA button               │
│  - Hero image/illustration  │
└─────────────────────────────┘

┌─────────────────────────────┐
│  Features Section (3 cols)  │
│  - Icon + Heading + Text    │
│  - Icon + Heading + Text    │
│  - Icon + Heading + Text    │
└─────────────────────────────┘

┌─────────────────────────────┐
│  About Section              │
│  - Heading                  │
│  - Text content             │
│  - Image                    │
└─────────────────────────────┘

┌─────────────────────────────┐
│  CTA Section                │
│  - Heading                  │
│  - Button                   │
└─────────────────────────────┘
```

**Elementor Implementation:**

```
Section 1: Hero
├── Column 1 (50%)
│   ├── Heading Widget: "Образователен център Светлинки"
│   ├── Text Editor: Subheading
│   └── Button Widget: "Запиши се за пробен урок"
└── Column 2 (50%)
    └── Image Widget: Hero illustration

Section 2: Features
├── Column 1 (33%)
│   ├── Icon Widget
│   ├── Heading Widget
│   └── Text Editor
├── Column 2 (33%)
│   └── [Same structure]
└── Column 3 (33%)
    └── [Same structure]

Section 3: About
└── Column 1 (100%)
    ├── Heading Widget
    ├── Text Editor
    └── Image Widget

Section 4: CTA
└── Column 1 (100%)
    ├── Heading Widget
    └── Button Widget
```

**Claude Code Prompt:**

```
Create the home page for svetlinkelementor with:

Hero Section:
- Large heading: "Образователен център Светлинки"
- Subheading: "Развиваме умовете на бъдещето чрез ментална аритметика"
- CTA button: "Запиши се за безплатен пробен урок"
- Background color: #fefcf5
- Text color: #2c2c2c
- Button color: #F5A623

Features Section (3 columns):
Column 1:
- Icon: brain/mind icon
- Heading: "Ментална аритметика"
- Text: "Развиваме математическите способности..."

Column 2:
- Icon: target icon
- Heading: "Индивидуален подход"
- Text: "Всяко дете се развива в свой темп..."

Column 3:
- Icon: trophy icon
- Heading: "Доказани резултати"
- Text: "Над 500 деца са преминали нашите програми..."

Use global colors and centered layout (900px max-width)
```

### 2. Politika za Poveritelnost (Legal Page)

**Structure:**

```
┌─────────────────────────────┐
│  Title Section              │
│  - H1: Page title           │
│  - Last updated date        │
│  - Divider                  │
└─────────────────────────────┘

┌─────────────────────────────┐
│  Content Sections           │
│  - H2: Section heading      │
│  - Paragraphs               │
│  - Lists                    │
│  - Divider                  │
│  [Repeat for each section]  │
└─────────────────────────────┘

┌─────────────────────────────┐
│  Footer Info                │
│  - Copyright                │
└─────────────────────────────┘
```

**Elementor Implementation:**

```
Section: Title (Centered, 900px max-width)
└── Column 1 (100%)
    ├── Heading Widget (H1): "Политика за поверителност"
    │   └── Color: #F5A623
    ├── Text Editor: "<em>Последна актуализация: [date]</em>"
    │   └── Color: #6c757d
    └── Divider Widget
        └── Color: #e0e0e0

Section: Member 1 (Centered, 900px max-width)
└── Column 1 (100%)
    ├── Heading Widget (H2): "Член 1 - Общи положения"
    │   └── Border-bottom: 3px solid #F5A623
    ├── Text Editor: [paragraph content]
    │   └── Line-height: 1.7
    └── Divider Widget

[Repeat section for each "Член"]

Section: Footer (Centered)
└── Column 1 (100%)
    └── Text Editor: "© 2025 Svetlinki..."
        └── Text-align: center
        └── Color: #6c757d
```

**Claude Code Prompt:**

```
Create a legal page "Политика за поверителност" on svetlinkelementor with:

Title Section:
- H1: "Политика за поверителност" (color: #F5A623)
- Subtitle: "Последна актуализация: 28.11.2025" (italic, gray)
- Horizontal divider

Content structure (max-width: 900px, centered):

Section 1:
- H2: "Член 1 - Общи положения" (border-bottom: 3px #F5A623)
- Paragraph: [content about organization]
- Divider

Section 2:
- H2: "Член 2 - Идентификация на организацията"
- List of contact details
- Divider

[Continue for all 20 members/sections]

Footer:
- Copyright notice
- Centered, gray text

Styling:
- Background: #fefcf5
- Text color: #2c2c2c
- Links: #F5A623
- Font size: 1rem, line-height: 1.7
```

### 3. Contact Page

**Structure:**

```
┌─────────────────────────────┐
│  Header Section             │
│  - Heading                  │
│  - Subheading               │
└─────────────────────────────┘

┌─────────────────────────────┐
│  Two Column Section         │
│  - Contact Form (Left 60%)  │
│  - Contact Info (Right 40%) │
└─────────────────────────────┘

┌─────────────────────────────┐
│  Map Section                │
│  - Google Maps embed        │
└─────────────────────────────┘
```

**Elementor Implementation:**

```
Section: Header
└── Column 1 (100%)
    ├── Heading Widget: "Свържете се с нас"
    └── Text Editor: "Имате въпроси? Ще се радваме да отговорим!"

Section: Contact
├── Column 1 (60%)
│   └── Form Widget / HTML Widget with form
│       ├── Name field
│       ├── Email field
│       ├── Phone field
│       ├── Message field
│       └── Submit button
└── Column 2 (40%)
    ├── Heading Widget: "Контакти"
    ├── Icon List Widget:
    │   ├── Phone icon + number
    │   ├── Email icon + address
    │   └── Location icon + address
    └── Text Editor: Working hours

Section: Map
└── Column 1 (100%)
    └── Google Maps Widget or HTML embed
```

**Note:** For forms, you'll need either:
- Elementor Pro (has Form widget)
- Contact Form 7 plugin + Elementor integration
- HTML form with action to WordPress form handler

---

## Quick Reference: Elementor Widgets Cheat Sheet

### Essential Widgets

| Widget | Use Case | Key Settings |
|--------|----------|--------------|
| **Heading** | H1-H6 | HTML Tag, Color, Typography |
| **Text Editor** | Paragraphs, lists | Content, Color, Typography |
| **Image** | Photos, logos | Image URL, Size, Link |
| **Button** | CTAs, links | Text, Link, Colors, Size |
| **Divider** | Section breaks | Color, Width, Gap |
| **Spacer** | Vertical spacing | Height |
| **Icon** | Visual indicators | Icon, Size, Color |
| **Icon List** | Feature lists | Icons, Text, Color |

### Layout Widgets

| Widget | Use Case | Key Settings |
|--------|----------|--------------|
| **Section** | Major layout blocks | Columns, Background, Padding |
| **Column** | Content columns | Width, Background, Gap |
| **Inner Section** | Nested layouts | Similar to Section |

### Advanced Widgets (Elementor Pro)

| Widget | Use Case | Key Settings |
|--------|----------|--------------|
| **Form** | Contact forms | Fields, Actions, Styling |
| **Posts** | Blog listings | Post Type, Layout, Pagination |
| **Popup** | Modal windows | Trigger, Content, Animation |

---

## Build Workflow

### Recommended Order:

1. **Week 1: Foundation**
   - Day 1: LocalWP setup + Elementor installation
   - Day 2: Global colors & fonts configuration
   - Day 3: Style guide page creation
   - Day 4-5: Home page build

2. **Week 2: Core Pages**
   - Day 1-2: About page
   - Day 3-4: Services/Programs pages
   - Day 5: Contact page

3. **Week 3: Legal & Misc**
   - Day 1-2: Politika za Poveritelnost
   - Day 3-4: Obshti Usloviya
   - Day 5: FAQ or additional pages

4. **Week 4: Polish & MCP**
   - Day 1-2: Mobile responsiveness
   - Day 3: Claude Code MCP setup
   - Day 4-5: Testing & refinement

### Daily Building Routine:

```
Morning (2-3 hours):
1. Open svetlinkelementor in LocalWP
2. Choose page to build
3. Create page structure (sections/columns)
4. Add widgets and content

Afternoon (2-3 hours):
5. Style widgets (colors, fonts, spacing)
6. Test responsive design
7. Refine and adjust
8. Save and preview

Evening (Optional - 1 hour):
9. Test in Claude Code MCP
10. Document any issues
11. Plan next day's work
```

---

## Troubleshooting

### Common Issues

**1. Elementor Not Loading**
```
Solution: Clear browser cache, try incognito mode
Check: Chrome DevTools → Console for errors
```

**2. Styles Not Applying**
```
Solution: Elementor → Tools → Regenerate CSS
Check: Global colors/fonts are set correctly
```

**3. Responsive Issues**
```
Solution: Use Elementor responsive mode (desktop/tablet/mobile icons)
Set different values for each device
```

**4. MCP Connection Fails**
```
Solution: Check Application Password is correct
Verify WordPress URL matches: http://svetlinkelementor.local
Restart Claude Code after config changes
```

**5. Page Load Slow**
```
Solution: Disable unused Elementor features
Enable asset loading optimization
Minimize number of widgets
```

---

## Resources

### Learning Elementor

- **Elementor Academy:** https://elementor.com/academy/
- **YouTube:** "Elementor Tutorial for Beginners"
- **Documentation:** https://elementor.com/help/

### Design Inspiration

- Original Svetlinki3 site (reference for colors/layout)
- Elementor Template Library (built-in)
- Educational website templates

### Tools

- **LocalWP:** Local development environment
- **Claude Code:** AI-assisted page building via MCP
- **Browser DevTools:** Inspect original site for exact measurements

---

## Next Steps

### Ready to Start?

1. ✅ Create new LocalWP site "svetlinkelementor"
2. ✅ Install Elementor
3. ✅ Configure global colors and fonts
4. ✅ Build first test page
5. ✅ Set up Claude Code MCP
6. ✅ Start building pages systematically

### Questions Before You Begin?

- Which theme to use? (Recommend: Hello Elementor)
- Elementor Free or Pro? (Start with Free)
- Build order? (Home → About → Contact → Legal)
- MCP setup timing? (After first 2-3 pages built manually)

---

**Ready to build? Let's create svetlinkelementor!** 🚀

Once you've set up the LocalWP site and installed Elementor, come back and I'll help you build the first page step-by-step, or create it automatically via Claude Code MCP!

---

**Document Version:** 1.0
**Last Updated:** November 28, 2025
**Status:** Ready to Execute
**Location:** C:\Users\denit\Local Sites\svetlinki3\SSOT\
