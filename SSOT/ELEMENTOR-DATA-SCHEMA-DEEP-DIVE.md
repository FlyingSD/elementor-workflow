# Elementor Data Schema Deep Dive (Reverse Engineering Level)

**Purpose**: Complete technical schema for direct Elementor database manipulation
**Level**: Reverse Engineering / "DNA Level"
**Source**: Elementor GitHub repository source code analysis via r.jina
**Last Updated**: 2025-11-29
**For**: AI automation (Claude Code) - building pages without visual interface

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
