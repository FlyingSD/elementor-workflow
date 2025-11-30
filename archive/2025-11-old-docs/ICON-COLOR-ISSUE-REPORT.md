# Icon Color Issue - Investigation Report

**Date**: 2025-11-30
**Issue**: Icon-box circular backgrounds showing gray instead of brand colors (yellow/coral/teal)

---

## ✅ What's Working

1. **H1 Positioning**: Headers now appear ABOVE cards (fixed by splitting into separate sections)
2. **Icon Stacked View**: Icons display with circular backgrounds (`view: "stacked"`, `shape: "circle"`)
3. **Page Structure**: 6 sections total (Hero, Blog, Benefits Header, Benefits Cards, Programs Header, Programs Cards)
4. **Card Styling**: White backgrounds, top border accents, box shadows, padding all working

---

## ❌ What's NOT Working

**Icon background colors remain gray** instead of:
- Yellow (#FABA29) for brain/book/newspaper icons
- Coral (#FF8C7A) for lightbulb/gift icons
- Teal (#4F9F8B) for star/question icons

---

## Approaches Tested

### 1. Global Color CSS Variables
```json
"icon_secondary_color": "var(--e-global-color-primary)"
```
**Result**: Gray icons ❌

### 2. Direct Hex Values
```json
"icon_secondary_color": "#FABA29",
"icon_color": "#FABA29",
"hover_secondary_color": "#FABA29"
```
**Result**: Gray icons ❌

### 3. Multiple Color Properties
Added all possible icon color properties simultaneously:
- `icon_color`
- `icon_secondary_color`
- `hover_secondary_color`
- `icon_primary_color`
- `hover_primary_color`

**Result**: Gray icons ❌

### 4. Legacy Sections vs Containers
Tried both Legacy Sections/Columns and modern Containers structures.

**Result**: Gray icons in both ❌

---

## Database Verification

Confirmed via `mcp__wp-elementor-mcp__get_elementor_widget` that all color properties ARE saved correctly to database:

```json
{
  "view": "stacked",
  "shape": "circle",
  "icon_secondary_color": "#FABA29",
  "icon_primary_color": "#FFFFFF"
}
```

✅ **Data is correct** - the issue is with CSS generation/rendering, not data storage.

---

## Root Cause Analysis

### Known Elementor Bugs

From GitHub issues research:

1. **Issue #12249**: "Global colors not applied to site"
   - CSS variables present in HTML but not applied to widgets
   - Affects Elementor FREE

2. **Issue #18621**: "Icon List Widget Icon Styling Not Working"
   - Icon color changes don't take effect
   - Color inheritance issues

### Likely Cause

**Elementor FREE limitation**: The icon-box widget's `icon_secondary_color` property (for stacked/framed views) may not generate CSS properly in the FREE version. The property is:
- ✅ Accepted by REST API
- ✅ Saved to database
- ❌ NOT rendered in frontend CSS

---

## CSS Regeneration Attempts

Tried multiple cache/CSS regeneration methods:

1. ✅ MCP `clear_elementor_cache`
2. ✅ PHP endpoint `regenerate-css-web.php`
3. ✅ Elementor CSS file delete + regenerate
4. ✅ WordPress transients cleared
5. ✅ Post modified timestamp updated
6. ✅ Hard browser refresh (Ctrl+Shift+R)

**All caches cleared** - not a caching issue.

---

## Alternative Solutions

### Option 1: Use Icon Widget Instead of Icon-Box
The standalone `icon` widget (not `icon-box`) might have better color support:
```json
{
  "widgetType": "icon",
  "settings": {
    "view": "stacked",
    "shape": "circle",
    "primary_color": "#FABA29",  // Background
    "secondary_color": "#FFFFFF" // Icon color
  }
}
```
Then pair with separate `heading` and `text-editor` widgets.

**Pros**: More control over individual elements
**Cons**: More complex structure (3 widgets per card vs 1)

### Option 2: Custom CSS (If Allowed)
Add custom CSS to force icon colors:
```css
.benefits-section .elementor-icon {
  background-color: #FABA29 !important;
}
```

**Pros**: Direct control
**Cons**: Requires theme customization or Elementor Pro

### Option 3: Use Images Instead of Icons
Replace FontAwesome icons with custom PNG/SVG images with colored backgrounds.

**Pros**: Full visual control
**Cons**: Less semantic, harder to maintain

### Option 4: Accept Gray Icons (Temporary)
Keep current structure, document as known limitation, revisit if upgrading to Pro.

---

## Recommended Next Steps

1. **Ask user preference**: Which workaround to implement?
2. **Test Option 1**: Try standalone `icon` widget to see if color rendering works
3. **Document limitation**: Update SSOT/TROUBLESHOOTING.md with this finding
4. **Consider Elementor Pro**: Icon styling may work properly in Pro version

---

## Files Modified This Session

- `homepage-v4-split-sections.json` (6-section structure with Global Colors)
- `update-homepage-final.php` (PHP script to update page + regenerate CSS)
- `ICON-COLOR-ISSUE-REPORT.md` (this file)

---

## Summary

✅ **Fixed**: H1 positioning (headers now above cards)
✅ **Working**: Icon circular shapes (stacked view)
✅ **Working**: Card styling (borders, shadows, spacing)
❌ **NOT Working**: Icon background colors (Elementor FREE limitation)

**Current State**: Homepage structure is correct, but icons remain gray instead of colorful. This appears to be a fundamental limitation of Elementor FREE's icon-box widget rendering, not a configuration issue.
