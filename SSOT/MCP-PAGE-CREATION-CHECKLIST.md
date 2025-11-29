# MCP Page Creation Checklist & Workflow

**Document Type**: Operational Checklist
**Date Created**: 2025-11-28
**Purpose**: Step-by-step guide for creating optimized Elementor pages via MCP
**Reference**: ELEMENTOR-CORE-PRINCIPLES.md

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
