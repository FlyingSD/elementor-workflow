# Elementor API Workflow Guide

**Purpose**: Complete guide for styling Elementor elements programmatically via API
**Date**: 2025-11-30
**Status**: Documentation of working methodology

---

## 🎯 Overview

This guide documents the complete workflow for styling Elementor widgets, columns, and sections using:
- **MCP (Model Context Protocol)** tools
- **WordPress REST API**
- **Elementor REST API**
- **Research tools** (Brave Search, R.JINA)

---

## 🛠️ Tools Stack

### 1. MCP - WordPress/Elementor Integration
**Tool**: `wp-elementor-mcp`
**Purpose**: Programmatic access to WordPress/Elementor via API

**Key Functions:**
```javascript
// Get element data
mcp__wp-elementor-mcp__get_elementor_widget(post_id, widget_id)

// Update element settings
mcp__wp-elementor-mcp__update_elementor_widget(post_id, widget_id, widget_settings)

// Get page structure
mcp__wp-elementor-mcp__get_elementor_elements(post_id, include_content)

// Clear cache
mcp__wp-elementor-mcp__clear_elementor_cache()
```

**What it does:**
- Reads/writes to WordPress database (`_elementor_data` post meta)
- Updates element settings as JSON
- Triggers Elementor cache clearing (though not always complete)

---

### 2. Brave Search
**Tool**: `mcp__brave-search__brave_web_search`
**Purpose**: Find documentation and source code

**Usage:**
```javascript
mcp__brave-search__brave_web_search({
  query: "site:github.com elementor icon-box.php widget controls",
  count: 10
})
```

**What to search for:**
- `site:github.com elementor [widget-name].php` - Source code
- `site:developers.elementor.com [widget] API` - Official docs
- `elementor [property-name] control settings` - Property documentation

---

### 3. R.JINA (Web Content Extractor)
**Tool**: `WebFetch` with R.JINA URLs
**Purpose**: Extract content from GitHub files and documentation

**Usage:**
```javascript
WebFetch({
  url: "https://r.jina.ai/https://raw.githubusercontent.com/elementor/elementor/main/includes/widgets/icon-box.php",
  prompt: "Extract all control names for background, border, shadow, padding"
})
```

**Why R.JINA:**
- GitHub's web UI doesn't show full files
- R.JINA extracts raw file content
- Can parse and analyze code structure

---

### 4. Playwright (Screenshots)
**Tool**: Node.js scripts with Playwright
**Purpose**: Visual verification of changes

**Script Location:** `scripts/working/take-screenshots-only.js`

**Usage:**
```bash
cd "C:\Users\denit\Local Sites\svetlinkielementor"
node scripts/working/take-screenshots-only.js
```

**What it does:**
- Takes desktop/tablet/mobile screenshots
- Captures individual sections
- Verifies styling applied correctly

---

### 5. Cache Clearing Scripts
**Tool**: PHP web endpoints
**Purpose**: Force Elementor CSS regeneration

**Script:** `regenerate-elementor-css.php`

**Access:** `http://svetlinkielementor.local/regenerate-elementor-css.php`

**What it does:**
```php
// Clear Elementor file cache
\Elementor\Plugin::instance()->files_manager->clear_cache();

// Regenerate CSS for specific page
$css_file = \Elementor\Core\Files\CSS\Post::create($page_id);
$css_file->delete();
$css_file->update();

// Clear WordPress caches
wp_cache_flush();
delete_transients();
```

---

## 🔬 Research Methodology

### Step 1: Identify Element Type
**Question:** "What type of element needs styling?"

**Process:**
1. Get element structure via MCP:
   ```javascript
   mcp__wp-elementor-mcp__get_elementor_elements(21, false)
   ```

2. Identify element types:
   - `section` - Full-width containers
   - `column` - Column elements inside sections
   - `widget` - Actual content widgets (icon-box, heading, button, etc.)

**Key Discovery:**
- **Widgets** (icon-box) DON'T have container styling controls
- **Columns** HAVE background/border/shadow controls
- Must style the PARENT COLUMN, not the widget itself

---

### Step 2: Find Source Code
**Question:** "What controls does this element type have?"

**Process:**
1. Search GitHub for element source:
   ```javascript
   mcp__brave-search__brave_web_search({
     query: "site:github.com elementor column.php controls"
   })
   ```

2. Extract source code via R.JINA:
   ```javascript
   WebFetch({
     url: "https://r.jina.ai/https://raw.githubusercontent.com/elementor/elementor/main/includes/elements/column.php",
     prompt: "Extract ALL control names for background, border, box-shadow, padding"
   })
   ```

**Example Output:**
```php
// From column.php
$this->add_control(
    'background_background',
    ['label' => 'Background Type', 'type' => Controls_Manager::CHOOSE]
);

$this->add_control(
    'box_shadow',  // ← KEY: Different from widget property name!
    ['label' => 'Box Shadow', 'type' => Controls_Manager::BOX_SHADOW]
);
```

---

### Step 3: Understand Property Names
**Question:** "What exact JSON property names should I use?"

**Critical Discovery:**
- Property names DIFFER between element types!
- Columns: `box_shadow`
- Widgets: `_box_shadow_box_shadow`

**Property Structure:**
```json
{
  "background_background": "classic",
  "background_color": "#FFFFFF",
  "border_border": "solid",
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
  },
  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)"
  },
  "padding": {
    "unit": "px",
    "top": "45",
    "right": "35",
    "bottom": "45",
    "left": "35",
    "isLinked": false
  }
}
```

---

### Step 4: Test with One Element
**Question:** "Does this work?"

**Process:**
1. Get current element data:
   ```javascript
   mcp__wp-elementor-mcp__get_elementor_widget(21, "benefits005")
   ```

2. Apply ONE property to test:
   ```javascript
   mcp__wp-elementor-mcp__update_elementor_widget(21, "benefits005", {
     "_column_size": 33,
     "background_background": "classic",
     "background_color": "#FFFFFF"
   })
   ```

3. Clear cache and verify:
   ```bash
   curl http://svetlinkielementor.local/regenerate-elementor-css.php
   ```

4. Take screenshot to verify

**If it works:** Apply to all elements
**If it doesn't:** Research why (wrong property name, wrong element type, etc.)

---

## 🔄 Complete Workflow Example

### Scenario: Style icon-box cards with white backgrounds and colored borders

#### Phase 1: Research
```javascript
// 1. Find element IDs
mcp__wp-elementor-mcp__get_elementor_elements(21, false)
// Result: benefits005, benefits007, benefits009 (columns)
//         benefits006, benefits008, benefits010 (icon-box widgets inside)

// 2. Search for column controls
mcp__brave-search__brave_web_search({
  query: "site:github.com elementor column.php background border"
})

// 3. Extract source code
WebFetch({
  url: "https://r.jina.ai/https://raw.githubusercontent.com/elementor/elementor/main/includes/elements/column.php",
  prompt: "Extract background, border, box-shadow control names"
})
// Result: Found property names - box_shadow (not _box_shadow_box_shadow!)
```

#### Phase 2: Apply
```javascript
// 4. Update first column to test
mcp__wp-elementor-mcp__update_elementor_widget(21, "benefits005", {
  "_column_size": 33,
  "background_background": "classic",
  "background_color": "#FFFFFF",
  "border_border": "solid",
  "border_width": {"unit": "px", "top": "5", "right": "0", "bottom": "0", "left": "0"},
  "border_color": "#FABA29",
  "border_radius": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20"},
  "box_shadow": {"horizontal": 0, "vertical": 10, "blur": 35, "spread": 0, "color": "rgba(0, 0, 0, 0.1)"},
  "padding": {"unit": "px", "top": "45", "right": "35", "bottom": "45", "left": "35"}
})

// 5. Clear cache
curl http://svetlinkielementor.local/regenerate-elementor-css.php
```

#### Phase 3: Verify
```bash
# 6. Take screenshot
cd "C:\Users\denit\Local Sites\svetlinkielementor"
node scripts/working/take-screenshots-only.js

# 7. Check screenshot
# If success: Apply to all other columns (benefits007, benefits009, programs005, programs008, programs011)
# If fail: Debug - check property names, element type, cache clearing
```

---

## ❌ Common Pitfalls

### 1. Wrong Element Type
**Problem:** Applied styling to widget instead of column
**Solution:** Style the parent column, not the widget

### 2. Wrong Property Name
**Problem:** Used `_box_shadow_box_shadow` on column
**Solution:** Columns use `box_shadow`, widgets use `_box_shadow_box_shadow`

### 3. Incomplete Cache Clearing
**Problem:** Changes saved but don't appear on frontend
**Solution:**
- Use nuclear cache clear script
- Run Elementor's regenerate files in admin
- Hard refresh browser (Ctrl+Shift+R)

### 4. Icon Colors Not Showing
**Problem:** Used `icon_primary_color` instead of `primary_color`
**Solution:** Icon-box widgets use:
- `primary_color` (background in stacked view)
- `secondary_color` (icon color in stacked view)
- NOT `icon_primary_color` or `icon_secondary_color`

---

## 🎯 Icon-Box Widget Specific Guide

### Icon Colors (Stacked View)
```json
{
  "view": "stacked",
  "shape": "circle",
  "primary_color": "#FABA29",      // Circle background
  "secondary_color": "#FFFFFF",     // Icon color
  "hover_primary_color": "#FABA29",
  "hover_secondary_color": "#FFFFFF",
  "icon_size": {"unit": "px", "size": 38},
  "icon_space": {"unit": "px", "size": 22}
}
```

### Card Styling (Apply to COLUMN, not widget)
```json
{
  "background_background": "classic",
  "background_color": "#FFFFFF",
  "border_border": "solid",
  "border_width": {"unit": "px", "top": "5", "right": "0", "bottom": "0", "left": "0"},
  "border_color": "#FABA29",
  "border_radius": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20"},
  "box_shadow": {"horizontal": 0, "vertical": 10, "blur": 35, "spread": 0, "color": "rgba(0, 0, 0, 0.1)"},
  "padding": {"unit": "px", "top": "45", "right": "35", "bottom": "45", "left": "35"}
}
```

---

## 🔍 How to Research ANY Elementor Element

### Universal Research Process:

1. **Find element type:**
   ```javascript
   mcp__wp-elementor-mcp__get_elementor_elements(post_id, false)
   ```

2. **Search for source code:**
   ```
   Brave Search: "site:github.com elementor [element-type].php"
   ```

3. **Extract source code:**
   ```javascript
   WebFetch("https://r.jina.ai/[github-raw-url]",
     "Extract control names for [desired-property]")
   ```

4. **Identify property names:**
   - Look for `$this->add_control('property_name', ...)`
   - Look for `$this->add_group_control(Group_Control_Background::get_type(), ...)`
   - Note the EXACT property name (including underscores)

5. **Test with one element:**
   ```javascript
   mcp__wp-elementor-mcp__update_elementor_widget(post_id, element_id, {
     "property_name": "value"
   })
   ```

6. **Clear cache and verify:**
   ```bash
   curl http://site.local/regenerate-elementor-css.php
   node scripts/working/take-screenshots-only.js
   ```

7. **If success:** Apply to all similar elements
   **If fail:** Debug and iterate

---

## 📚 Reference Resources

### Elementor Source Code Locations:
- Widgets: `elementor/includes/widgets/[widget-name].php`
- Elements: `elementor/includes/elements/[element-type].php`
- Column: `elementor/includes/elements/column.php`
- Section: `elementor/includes/elements/section.php`

### Key Documentation:
- Elementor Controls: https://developers.elementor.com/docs/editor-controls/
- Elementor REST API: GitHub elementor/includes/widgets/ (source code)
- Group Controls: https://developers.elementor.com/docs/editor-controls/group-control-types/

### Research URLs:
- GitHub search: `site:github.com elementor [term]`
- Raw files: `https://raw.githubusercontent.com/elementor/elementor/main/[path]`
- R.JINA: `https://r.jina.ai/[url]`

---

## ✅ Verification Checklist

After applying styling:

- [ ] MCP update returned success
- [ ] Cache cleared via script
- [ ] Screenshot taken
- [ ] Visual verification passed
- [ ] Properties saved in database (check via get_elementor_widget)
- [ ] CSS generated correctly (check browser DevTools)
- [ ] Changes visible on frontend (hard refresh)

---

## 🎓 Key Learnings

1. **Always research element type first** - Don't assume widgets have all styling controls
2. **Property names matter** - One character difference breaks everything
3. **Cache clearing is critical** - Changes won't appear without it
4. **Test incrementally** - Apply one property, verify, then continue
5. **Screenshot everything** - Visual verification is essential
6. **Document as you go** - Save property names and patterns for reuse

---

## 🚀 Quick Reference Commands

```bash
# Get element structure
mcp__wp-elementor-mcp__get_elementor_elements(21, false)

# Get element data
mcp__wp-elementor-mcp__get_elementor_widget(21, "element_id")

# Update element
mcp__wp-elementor-mcp__update_elementor_widget(21, "element_id", {...})

# Clear cache
curl http://svetlinkielementor.local/regenerate-elementor-css.php

# Take screenshots
node scripts/working/take-screenshots-only.js

# Search GitHub
mcp__brave-search__brave_web_search({query: "site:github.com elementor [term]"})

# Extract source
WebFetch({url: "https://r.jina.ai/[github-url]", prompt: "Extract [info]"})
```

---

**Last Updated**: 2025-11-30
**Version**: 1.0
**Status**: Complete methodology documentation
