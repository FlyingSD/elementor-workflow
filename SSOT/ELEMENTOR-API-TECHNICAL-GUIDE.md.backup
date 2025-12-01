# Elementor API Technical Deep Dive

**Purpose**: Complete technical reference for Elementor WordPress API internals
**Date**: 2025-11-30
**Status**: Production reference documentation
**Version**: 1.0

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Data Flow & Save Mechanism](#data-flow--save-mechanism)
3. [CSS Generation System](#css-generation-system)
4. [REST API Integration](#rest-api-integration)
5. [Group Controls Deep Dive](#group-controls-deep-dive)
6. [Property Naming Conventions](#property-naming-conventions)
7. [Cache Management](#cache-management)
8. [Troubleshooting](#troubleshooting)

---

## Architecture Overview

### Core Components

```
WordPress
├── wp_postmeta table
│   ├── _elementor_data (JSON structure)
│   ├── _elementor_css (generated CSS)
│   └── _elementor_edit_mode (boolean)
│
├── Elementor Plugin
│   ├── Core
│   │   ├── Files Manager (CSS generation)
│   │   ├── Documents (save/update logic)
│   │   └── Elements Manager (element instantiation)
│   │
│   ├── Includes
│   │   ├── Elements (Section, Column, Container)
│   │   ├── Widgets (40-50 FREE widgets)
│   │   └── Controls (input types)
│   │
│   └── Controls
│       ├── Simple (text, color, number)
│       └── Group (background, border, shadow)
│
└── REST API
    ├── /wp-json/wp/v2/posts
    ├── /wp-json/wp/v2/pages
    └── /wp-json/wp/v2/media
```

### Element Hierarchy

```
Document (Post/Page)
└── Section/Container (top-level)
    └── Column (layout division)
        └── Widget (content element)
            └── Settings (JSON object)
```

---

## Data Flow & Save Mechanism

### Complete Save Flow

Source: `core/base/document.php` - `save()` method

```
User Change (via Editor or API)
    ↓
save($data)
    ├── 1. Set locale: LC_NUMERIC = 'C'
    ├── 2. Apply filter: 'elementor/document/save/data'
    ├── 3. Permission check: is_editable_by_current_user()
    ├── 4. Set is_saving(true)
    │
    ├── 5. Sanitize data (if no unfiltered_html capability)
    │   └── wp_kses_post() on all values
    │
    ├── 6. Save Settings
    │   ├── save_settings($data['settings'])
    │   ├── → Settings Manager updates options
    │   └── → update_meta() called internally
    │
    ├── 7. Save Elements
    │   ├── save_elements($data['elements'])
    │   ├── → get_elements_raw_data() transforms editor data
    │   └── → update_metadata('post', $post_id, '_elementor_data', $json)
    │
    ├── 8. CSS Deletion (Force Regeneration)
    │   ├── Post_CSS::create($post_id)
    │   └── →delete() removes cached CSS files
    │
    ├── 9. Cache Clearing
    │   ├── delete_cache() removes element cache
    │   └── Clears rendered HTML/scripts/styles
    │
    ├── 10. Post-Save Hooks
    │   ├── do_action('elementor/document/before_save')
    │   ├── do_action('elementor/document/after_save')
    │   └── do_action('elementor/editor/after_save')
    │
    └── 11. Complete
        ├── set_is_saving(false)
        ├── Restore locale
        └── Return true
```

### Why CSS Doesn't Show Immediately

**Critical Discovery**: CSS is DELETED, not regenerated during save.

```php
// From document.php save() flow
$css_file = Post_CSS::create($post_id);
$css_file->delete();  // ← Only deletion happens!
// NO ->update() call here!
```

**CSS Regeneration Happens**:
1. On next frontend page load (lazy generation)
2. When user clicks "Update" in Elementor editor
3. When running "Regenerate Files & Data" in Elementor > Tools

**Implication for API Updates**:
- REST API updates save to database ✅
- CSS files get deleted ✅
- CSS regeneration does NOT happen automatically ❌
- Manual trigger required (see Troubleshooting section)

---

## CSS Generation System

### Generation Flow

Source: `core/files/css/post.php` - `render_css()` method

```
render_css()
    ↓
1. Retrieve Data
   ├── get_data() → Document elements
   └── Elements Manager instantiates each element
    ↓
2. Phase 1: Global Styles
   ├── render_element_global_styles()
   ├── → Check Kit Manager (custom colors/typography enabled?)
   ├── → Build global_controls array with defaults
   └── → add_control_rules() applies kit-level CSS
    ↓
3. Phase 2: Element Styles
   ├── render_element_styles()
   ├── → Pass control definitions + element settings
   ├── → Replace placeholders: {{ID}}, {{WRAPPER}}, {{VALUE}}
   └── → add_controls_stack_style_rules() generates CSS
    ↓
4. Responsive Handling
   ├── Process active breakpoints (desktop, tablet, mobile)
   ├── Generate media queries
   └── Apply responsive-specific values
    ↓
5. Output
   ├── Compile all CSS rules
   ├── Minify (if enabled)
   └── Write to /uploads/elementor/css/post-{ID}.css
```

### CSS Selector Structure

**Wrapper Pattern**:
```css
/* Section */
.elementor-element.elementor-element-{ID}

/* Column populated area */
.elementor-element.elementor-element-{ID} > .elementor-element-populated

/* Widget wrapper */
.elementor-element.elementor-element-{ID} .elementor-widget-wrap

/* Widget container */
.elementor-element.elementor-element-{ID} .elementor-widget-container
```

### Placeholder Replacement

```javascript
// Template
"{{WRAPPER}} > .elementor-element-populated {
  box-shadow: {{HORIZONTAL}}px {{VERTICAL}}px {{BLUR}}px {{SPREAD}}px {{COLOR}};
}"

// Replaced (for column ID "abc123")
".elementor-element.elementor-element-abc123 > .elementor-element-populated {
  box-shadow: 0px 10px 35px 0px rgba(0, 0, 0, 0.1);
}"
```

---

## REST API Integration

### WordPress Standard Endpoints

Elementor uses standard WordPress REST API with custom meta fields:

```bash
# Get post with Elementor data
GET /wp-json/wp/v2/posts/{id}?context=edit

# Update post
POST /wp-json/wp/v2/posts/{id}
Headers:
  Authorization: Basic {base64(username:app_password)}
  Content-Type: application/json

Body:
{
  "meta": {
    "_elementor_data": "[{...}]",  // JSON-encoded string!
    "_elementor_edit_mode": "builder"
  }
}
```

### Authentication

**Application Password** (WordPress 5.6+):
1. User Profile > Application Passwords
2. Create new password (auto-generated)
3. Use in Basic Auth header
4. Format: `Authorization: Basic base64(username:password)`

### MCP Integration (wp-elementor-mcp)

Our MCP server (`wp-elementor-mcp v1.6.1`) wraps WordPress REST API:

```
MCP Tool Call
    ↓
mcp__wp-elementor-mcp__update_elementor_widget(post_id, widget_id, settings)
    ↓
1. Fetch current data
   GET /wp-json/wp/v2/posts/{post_id}?context=edit
    ↓
2. Parse _elementor_data JSON
   elements = JSON.parse(meta._elementor_data)
    ↓
3. Find target element by ID
   element = findDeep(elements, widget_id)
    ↓
4. Merge settings
   element.settings = {...element.settings, ...new_settings}
    ↓
5. Update post
   POST /wp-json/wp/v2/posts/{post_id}
   body: {meta: {_elementor_data: JSON.stringify(elements)}}
    ↓
6. Database updated ✅
   CSS NOT regenerated ❌
```

### Critical Limitation

**REST API updates DO NOT trigger CSS regeneration!**

Workaround options:
1. Manual: Click "Update" in Elementor editor
2. Script: Run `Elementor\Plugin::instance()->files_manager->clear_cache()`
3. Tool: Visit Elementor > Tools > Regenerate Files & Data

---

## Group Controls Deep Dive

### Background Control

**Control Name**: `background_background` (type selector)

**Structure**:
```json
{
  "background_background": "classic" | "gradient" | "video" | "slideshow",

  // Classic (solid color)
  "background_color": "#FFFFFF",
  "background_image": {"url": "...", "id": 123},
  "background_position": "center center",
  "background_attachment": "scroll",
  "background_repeat": "no-repeat",
  "background_size": "cover",

  // Gradient
  "background_gradient_type": "linear" | "radial",
  "background_gradient_angle": {"size": 180, "unit": "deg"},
  "background_gradient_position": "center center",
  "background_color": "#FABA29",      // Color A
  "background_color_b": "#FF8C7A",    // Color B
  "background_color_stop": {"size": 0, "unit": "%"},
  "background_color_b_stop": {"size": 100, "unit": "%"}
}
```

**CSS Output**:
```css
/* Classic */
background-color: #FFFFFF;
background-image: url("...");
background-position: center center;

/* Gradient */
background-image: linear-gradient(
  180deg,
  #FABA29 0%,
  #FF8C7A 100%
);
```

### Box Shadow Control

Source: `includes/controls/groups/box-shadow.php`

**Control Name**: `box_shadow` (for columns) or `_box_shadow_box_shadow` (for widgets)

**Structure**:
```json
{
  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)",
    "position": "" | "inset"
  }
}
```

**CSS Output Template**:
```css
box-shadow: {{HORIZONTAL}}px {{VERTICAL}}px {{BLUR}}px {{SPREAD}}px {{COLOR}} {{POSITION}};

/* Example */
box-shadow: 0px 10px 35px 0px rgba(0, 0, 0, 0.1);
```

**Critical Property Name Difference**:
- **Columns**: `box_shadow` (simple name)
- **Widgets**: `_box_shadow_box_shadow` (prefixed)
- **Sections**: `box_shadow` (simple name)

### Border Control

Source: `includes/controls/groups/border.php`

**Structure**:
```json
{
  "border_border": "solid" | "dashed" | "dotted" | "double" | "none",
  "border_width": {
    "unit": "px",
    "top": "5",
    "right": "0",
    "bottom": "0",
    "left": "0",
    "isLinked": false
  },
  "border_color": "#FABA29",
  "border_radius": {
    "unit": "px",
    "top": "20",
    "right": "20",
    "bottom": "20",
    "left": "20",
    "isLinked": true
  }
}
```

**CSS Output**:
```css
border-style: solid;
border-width: 5px 0px 0px 0px;
border-color: #FABA29;
border-radius: 20px 20px 20px 20px;
```

### Typography Control

**Structure**:
```json
{
  "typography_typography": "custom",
  "typography_font_family": "Roboto",
  "typography_font_size": {"size": 16, "unit": "px"},
  "typography_font_weight": "400",
  "typography_text_transform": "none",
  "typography_font_style": "normal",
  "typography_line_height": {"size": 1.5, "unit": "em"},
  "typography_letter_spacing": {"size": 0, "unit": "px"}
}
```

---

## Property Naming Conventions

### Naming Patterns

**Group Control Pattern**:
```
{control_name}_{property}
```

Examples:
- `background_color` (background control → color property)
- `border_width` (border control → width property)
- `box_shadow` (box shadow control → direct name)
- `typography_font_size` (typography control → font_size property)

### Element-Specific Differences

**Column Properties** (from `includes/elements/column.php`):
```json
{
  "content_position": "top" | "center" | "bottom" | "space-between" | "space-around" | "space-evenly",
  "align": "flex-start" | "center" | "flex-end" | "space-between" | "space-around" | "space-evenly",
  "_inline_size": 33,  // Column width percentage
  "space_between_widgets": {"size": 20, "unit": "px"},
  "margin": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px"},
  "padding": {"top": "10", "right": "10", "bottom": "10", "left": "10", "unit": "px"},
  "background_background": "classic",
  "background_color": "#FFFFFF",
  "border_border": "solid",
  "border_width": {...},
  "box_shadow": {...}  // ← Simple name for columns!
}
```

**Section Properties** (from `includes/elements/section.php`):
```json
{
  "layout": "boxed" | "full_width",
  "content_width": {"size": 1140, "unit": "px"},
  "gap": "default" | "no" | "narrow" | "extended" | "wide" | "wider" | "custom",
  "gap_columns_custom": {"size": 20, "unit": "px"},
  "height": "default" | "full" | "min-height",
  "column_position": "stretch" | "top" | "middle" | "bottom",
  "content_position": "top" | "middle" | "bottom" | "space-between" | "space-around" | "space-evenly",
  "stretch_section": "yes" | "",
  "background_background": "gradient",
  "background_gradient_type": "linear",
  "background_gradient_angle": {"size": 120, "unit": "deg"}
}
```

**Widget Properties** (example: `includes/widgets/icon-box.php`):
```json
{
  "view": "default" | "stacked" | "framed",
  "shape": "circle" | "square",
  "primary_color": "#FABA29",     // Icon background (stacked view)
  "secondary_color": "#FFFFFF",   // Icon color (stacked view)
  "icon_size": {"size": 38, "unit": "px"},
  "icon_space": {"size": 22, "unit": "px"},
  "position": "top" | "left" | "right",
  "text_align": "left" | "center" | "right",
  "content_vertical_alignment": "top" | "middle" | "bottom",
  "_box_shadow_box_shadow": {...}  // ← Prefixed for widgets!
}
```

### Responsive Properties

**Pattern**: `{property}_{breakpoint}`

```json
{
  "content_position": "center",          // Desktop
  "content_position_tablet": "top",      // Tablet (768px)
  "content_position_mobile": "bottom"    // Mobile (480px)
}
```

**Available Breakpoints**:
- Desktop: (default, no suffix)
- Tablet: `_tablet`
- Mobile: `_mobile`

---

## Cache Management

### Cache Layers

**1. Elementor CSS Cache**
- Location: `/wp-content/uploads/elementor/css/`
- Files: `post-{ID}.css`, `post-{ID}-{timestamp}.css`
- Cleared by: `\Elementor\Plugin::instance()->files_manager->clear_cache()`

**2. WordPress Object Cache**
- Memory-based (Redis, Memcached, or transient API)
- Cleared by: `wp_cache_flush()`

**3. WordPress Transients**
- Database: `wp_options` table (`_transient_*`)
- Cleared by: `DELETE FROM wp_options WHERE option_name LIKE '_transient_%'`

**4. Elementor Document Cache**
- Element instances, rendered HTML
- Cleared by: `$document->delete_cache()`

**5. Browser Cache**
- User's browser cached CSS/JS/images
- Cleared by: Hard refresh (Ctrl+Shift+R)

### Complete Cache Clear Flow

```php
// 1. Clear WordPress caches
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");
wp_cache_flush();

// 2. Clear Elementor cache
if (did_action('elementor/loaded')) {
    \Elementor\Plugin::instance()->files_manager->clear_cache();
}

// 3. Delete CSS files manually
$upload_dir = wp_upload_dir();
$elementor_css_dir = $upload_dir['basedir'] . '/elementor/css/';
$files = glob($elementor_css_dir . 'post-{ID}*.css');
foreach ($files as $file) {
    unlink($file);
}

// 4. Force CSS regeneration
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css_file->delete();
$css_file->update();  // ← This regenerates!

// 5. Update post timestamp (bust cache)
wp_update_post([
    'ID' => $post_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
]);
```

---

## Troubleshooting

### Issue: REST API Changes Not Visible

**Symptoms**:
- MCP update returns success
- Database shows correct values
- Frontend shows old styling

**Root Cause**: CSS not regenerated after REST API update

**Solutions**:

**Option 1: Manual Editor Update**
1. Open page in Elementor editor
2. Click "Update" button
3. CSS regenerates automatically

**Option 2: PHP Script**
```php
require_once('wp-load.php');
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css_file->delete();
$css_file->update();
```

**Option 3: Elementor Tools**
1. WordPress Admin > Elementor > Tools
2. Click "Regenerate Files & Data"
3. Regenerates CSS for all pages

**Option 4: Change CSS Print Method**
1. WordPress Admin > Elementor > Settings > Advanced
2. CSS Print Method: Toggle between "Internal Embedding" and "External File"
3. Save changes
4. Toggle back and save again
5. Forces complete CSS rebuild

### Issue: Box Shadow Not Showing

**Check**:
1. Property name correct? (`box_shadow` for columns, `_box_shadow_box_shadow` for widgets)
2. Applied to correct element? (columns have shadows, widgets don't)
3. CSS regenerated? (see above)
4. Browser DevTools: Is CSS rule present?

**Debug**:
```php
// Check if property saved
$data = get_post_meta($post_id, '_elementor_data', true);
$elements = json_decode($data, true);
// Find element and check settings['box_shadow']

// Check generated CSS
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css = $css_file->get_content();
echo $css; // Search for "box-shadow"
```

### Issue: Background Gradient Not Showing

**Check**:
1. `background_background` set to `"gradient"`
2. `background_gradient_type` specified (`"linear"` or `"radial"`)
3. Both color stops defined
4. CSS regenerated

**Correct Structure**:
```json
{
  "background_background": "gradient",
  "background_gradient_type": "linear",
  "background_gradient_angle": {"size": 120, "unit": "deg"},
  "background_color": "#FEFCF5",
  "background_color_stop": {"size": 0, "unit": "%"},
  "background_color_b": "#ffe8b3",
  "background_color_b_stop": {"size": 100, "unit": "%"}
}
```

### Issue: Column Alignment Not Working

**Check**:
1. Using correct property names:
   - Vertical: `content_position`
   - Horizontal: `align`
2. Applied to column, not widget
3. Column has height to align within
4. Not conflicting with widget-level alignment

**Example**:
```json
{
  "_column_size": 33,
  "content_position": "center",  // Vertical center
  "align": "center"              // Horizontal center
}
```

---

## Reference Resources

### Source Code Locations

**GitHub Repository**: https://github.com/elementor/elementor

**Key Files**:
- `core/base/document.php` - Save mechanism
- `core/files/css/post.php` - CSS generation
- `core/files/manager.php` - Cache management
- `includes/elements/column.php` - Column controls
- `includes/elements/section.php` - Section controls
- `includes/widgets/*.php` - Widget definitions
- `includes/controls/groups/*.php` - Group controls

### Official Documentation

- Elementor Developer Docs: https://developers.elementor.com/docs/
- WordPress REST API: https://developer.wordpress.org/rest-api/
- Application Passwords: https://make.wordpress.org/core/2020/11/05/application-passwords/

### MCP Server

- wp-elementor-mcp: https://github.com/alex-daiz/wp-elementor-mcp
- Local installation: `C:\Users\denit\wp-elementor-mcp`
- Version: 1.6.1

---

## Quick Reference Commands

```bash
# MCP update element
mcp__wp-elementor-mcp__update_elementor_widget(post_id, element_id, {settings})

# Clear cache via curl
curl http://site.local/nuclear-cache-clear.php

# Get element structure
mcp__wp-elementor-mcp__get_elementor_elements(post_id, false)

# Get element data
mcp__wp-elementor-mcp__get_elementor_widget(post_id, element_id)

# Backup before changes
mcp__wp-elementor-mcp__backup_elementor_data({post_id})
```

---

**Last Updated**: 2025-11-30
**Version**: 1.0
**Maintainer**: Claude Code AI System
**Status**: Production Ready
