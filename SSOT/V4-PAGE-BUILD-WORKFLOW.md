# V4 PAGE BUILD WORKFLOW

**Purpose**: Standard workflow for building/transforming pages with V4 styling
**Created**: 2025-12-02
**Status**: MANDATORY - Follow this sequence for all V4 page builds
**Proven On**: Programs page (ID: 25) - Complete success

---

## 🎯 THE WORKFLOW (4 STEPS)

### **Step 1: Consult Web Design Core Principles** 📚

**File**: `SSOT/CORE-WEBSITE-BUILDING-RULES.md`

**What to Look For**:
- Nielsen's 10 Usability Heuristics
- Visual hierarchy principles
- Material Design elevation levels (box shadows)
- WCAG accessibility standards (contrast ratios)
- Typography rules
- Spacing systems (8-point grid)

**Key Sections**:
```bash
# Use anchor search to find relevant sections
node scripts/core/anchor-search.js "visual hierarchy"
node scripts/core/anchor-search.js "box shadow"
node scripts/core/anchor-search.js "accessibility"
```

**Example Insights**:
- **Material Design Level 3**: `0 8px 20px rgba(0,0,0,0.12)` for primary cards
- **Contrast**: Minimum 4.5:1 for normal text
- **Spacing**: Use 8-point increments (8px, 16px, 24px, 32px, 40px)
- **Border Radius**: 12px for modern, friendly appearance

**Why This First?**:
- Establishes design principles before technical implementation
- Ensures accessibility and usability from the start
- Provides rationale for design decisions (not arbitrary)

---

### **Step 2: Check Elementor Widget & Settings Names** 🔧

**File**: `SSOT/ELEMENTOR-API-TECHNICAL-GUIDE.md`

**What to Look For**:
- Widget property names (exact spelling!)
- Group control structures (background, border, box_shadow, typography)
- Property naming conventions
- JSON structure requirements

**Key Sections**:
```bash
# Use anchor search for specific controls
node scripts/core/anchor-search.js "box shadow"
node scripts/core/anchor-search.js "border styling"
node scripts/core/anchor-search.js "background gradient"
```

**Critical Details**:

#### Box Shadow (Columns):
```json
{
  "box_shadow": {
    "horizontal": 0,
    "vertical": 8,
    "blur": 20,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.12)",
    "position": ""
  }
}
```

#### Border (All 4 Sides!):
```json
{
  "border_border": "solid",
  "border_width": {
    "unit": "px",
    "top": "5",
    "right": "1",
    "bottom": "1",
    "left": "1",
    "isLinked": false
  },
  "border_color": "var(--e-global-color-primary)"
}
```

#### Background Gradient:
```json
{
  "background_background": "gradient",
  "background_gradient_type": "linear",
  "background_gradient_angle": {"unit": "deg", "size": 120},
  "background_color": "#FEFCF5",
  "background_color_b": "#ffe8b3"
}
```

**Why This Second?**:
- Prevents syntax errors (wrong property names = failed updates)
- Ensures correct JSON structure
- Know which properties work on columns vs widgets vs sections

---

### **Step 3: Apply V4 HTML Design Reference** 🎨

**Files**:
- `design-mockup-v4.html` - Final approved homepage design
- `homepage-v4-full.png` - Screenshot of V4 styling
- `COLOR-AND-STYLE-VISION.md` - Complete V4 design system
- `SSOT/ACTIVE_STATE.md#global-design-system` - V4 colors, fonts, spacing

**What to Extract**:

#### Colors (V4 System):
```
Primary Yellow:   #FABA29 (var(--e-global-color-primary))
Secondary Teal:   #46b19d (var(--e-global-color-secondary))
Accent Coral:     #FF8C7A (var(--e-global-color-accent))
Text Dark Teal:   #1d3234 (var(--e-global-color-text))
Background Cream: #FEFCF5 (var(--e-global-color-5))
Background White: #FFFFFF
```

#### Typography Scale:
```
H1: 2.75rem (44px) - clamp(2rem, 5vw, 2.75rem)
H2: 1.9rem (30.4px) - clamp(1.5rem, 4vw, 1.9rem)
H3: 1.4rem (22.4px) - clamp(1.2rem, 3vw, 1.4rem)
Body: 1rem (16px)
Line Height: 1.7 (body), 1.2 (headings)
```

#### Card Pattern:
```
- White background (#FFFFFF)
- Colored top border: 5px thick + 1px sides/bottom
- Border colors rotate: Yellow → Coral → Teal
- Border radius: 12px
- Box shadow: 0 8px 20px rgba(0,0,0,0.12)
- Padding: 40px (primary cards) or 32px (secondary)
- Spacing: 15px column margins = 30px gaps
```

#### Hero Pattern:
```
- Background: Yellow gradient (120deg, #FEFCF5 → #ffe8b3)
- Layout: 2 columns (text + image/mascot)
- Heading: H1, dark teal, left-aligned
- Button: Primary yellow (#FABA29), 8px radius
```

**Why This Third?**:
- Translates visual design into technical specifications
- Ensures consistency with approved V4 design
- Provides exact values (colors, sizes, spacing)

---

### **Step 4: Build with MCP Using That Knowledge** 🚀

**Approach**: Combine Steps 1-3 knowledge and build systematically

#### Pre-Build:
```bash
# 1. Backup existing page
mcp__wp-elementor-mcp__backup_elementor_data(post_id: X, backup_name: "before-v4-transform")

# 2. Extract existing content (if rebuilding)
node scripts/working/extract-[page]-content.js

# 3. Take "before" screenshot
npx playwright screenshot http://svetlinkielementor.local/[page]/ [page]-before.png --full-page
```

#### Build Process:

**For Each Section**:
1. **Create section** with V4 background (gradient or white)
2. **Add columns** with proper spacing (15px margins)
3. **Add widgets** (heading, text, icon-box, button, etc.)
4. **Apply styling**:
   - Global colors (var(--e-global-color-*))
   - V4 typography scale (rem units)
   - Borders (5px top + 1px sides, all 4 sides!)
   - Box shadows (Material Design Level 3)
   - Border radius (12px)
   - Padding (40px or 32px)
5. **Regenerate CSS** (MANDATORY!):
   ```bash
   curl -s "http://svetlinkielementor.local/regenerate-css-api.php?page=X&secret=svetlinki2024"
   curl -s "http://svetlinkielementor.local/[page]/" > nul
   ```
6. **Verify section** on frontend before moving to next

**Build Order** (Recommended):
1. Hero section (establishes tone)
2. Introduction/content sections
3. Main content (cards, features, etc.)
4. CTA sections
5. Pricing/tables (if applicable)
6. Footer content sections

#### Post-Build:
```bash
# 1. Final CSS regeneration
curl -s "http://svetlinkielementor.local/regenerate-css-api.php?page=X&secret=svetlinki2024"

# 2. Take "after" screenshot
npx playwright screenshot http://svetlinkielementor.local/[page]/ [page]-after.png --full-page

# 3. Verify in NEW incognito window
# Open: http://svetlinkielementor.local/[page]/ in fresh browser

# 4. Update SSOT files:
# - ACTIVE_STATE.md (page status)
# - SUCCESS-LOG.md (document success)
# - KNOWLEDGE-UPDATES.md (any new patterns discovered)
# - CONTEXT-SNAPSHOT.md (next session context)
```

**Why This Fourth?**:
- Systematic approach prevents missing steps
- CSS regeneration after EVERY section ensures changes visible
- Verification at each step catches issues early
- Documentation ensures future sessions understand what was done

---

## 🎯 COMPLETE WORKFLOW CHECKLIST

Use this for every V4 page build:

### Pre-Build Phase:
- [ ] Read `CORE-WEBSITE-BUILDING-RULES.md` (Step 1) - Design principles
- [ ] Read `ELEMENTOR-API-TECHNICAL-GUIDE.md` (Step 2) - Property names
- [ ] Review `ACTIVE_STATE.md#global-design-system` (Step 3) - V4 colors/fonts
- [ ] Review V4 HTML reference or screenshots (Step 3) - Visual patterns
- [ ] Create MCP backup of existing page
- [ ] Extract existing content (if rebuilding)
- [ ] Take "before" screenshot

### Build Phase:
- [ ] Build section by section (don't rush all at once!)
- [ ] Use Global Colors (var(--e-global-color-*)) - NOT hex codes
- [ ] Apply V4 typography scale (rem units)
- [ ] Set borders with all 4 sides (top, right, bottom, left)
- [ ] Apply Material Design shadows (0 8px 20px rgba(0,0,0,0.12))
- [ ] Use 12px border radius for modern cards
- [ ] Set proper padding (40px primary, 32px secondary)
- [ ] Use column margins for spacing (15px left/right = 30px gaps)
- [ ] **Regenerate CSS after EVERY section** (MANDATORY!)
- [ ] Verify each section on frontend before moving to next

### Post-Build Phase:
- [ ] Final CSS regeneration for entire page
- [ ] Take "after" screenshot (full page)
- [ ] Verify in NEW incognito window (avoid cached CSS)
- [ ] Compare before/after screenshots
- [ ] Update ACTIVE_STATE.md (page status → V4 COMPLETE)
- [ ] Log success in SUCCESS-LOG.md
- [ ] Document any new patterns in KNOWLEDGE-UPDATES.md
- [ ] Update CONTEXT-SNAPSHOT.md for next session

---

## 📚 QUICK REFERENCE FILES

**Design Principles**:
- `SSOT/CORE-WEBSITE-BUILDING-RULES.md` - Nielsen, Material Design, WCAG

**Technical Reference**:
- `SSOT/ELEMENTOR-API-TECHNICAL-GUIDE.md` - Widget properties, JSON structure
- `SSOT/LESSONS-LEARNED.md` - Border pattern (Lesson #2), Spacing (Lesson #3)

**V4 Design System**:
- `SSOT/ACTIVE_STATE.md#global-design-system` - Colors, fonts, spacing
- `COLOR-AND-STYLE-VISION.md` - Complete V4 vision
- `design-mockup-v4.html` - Approved homepage design
- `homepage-v4-full.png` - V4 visual reference

**Workflow & Patterns**:
- `SSOT/MANDATORY-CSS-REGENERATION.md` - CSS regeneration (CRITICAL!)
- `SSOT/runtime/KNOWLEDGE-UPDATES.md` - Material Design shadows, border radius, padding

**Tools**:
- `scripts/core/anchor-search.js` - Find specific guide sections
- `regenerate-css-api.php` - CSS regeneration endpoint (100% reliable)
- Playwright - Screenshots for verification

---

## ✅ PROVEN SUCCESS

**Programs Page (ID: 25) - 2025-12-02**:
- Followed this exact workflow
- Result: Complete V4 transformation + professional polish
- Time: ~3 hours (2 hours build + 45 minutes polish)
- CSS regeneration: 100% success rate
- Frontend: Matches V4 design perfectly

**Key Success Factors**:
1. ✅ Consulted design principles FIRST (not afterthought)
2. ✅ Used correct property names (no trial-and-error)
3. ✅ Applied V4 design system consistently
4. ✅ Built systematically, verified each section
5. ✅ CSS regeneration after EVERY section (mandatory!)
6. ✅ Documented everything for future sessions

---

## 🚨 COMMON MISTAKES TO AVOID

**❌ Mistake 1**: Skip design principles, jump straight to building
- **Result**: Inconsistent design, poor accessibility, arbitrary decisions
- **Fix**: Always read CORE-WEBSITE-BUILDING-RULES.md first

**❌ Mistake 2**: Guess property names or use wrong syntax
- **Result**: MCP updates fail, wasted time debugging
- **Fix**: Always check ELEMENTOR-API-TECHNICAL-GUIDE.md for exact names

**❌ Mistake 3**: Use hex colors directly instead of Global Colors
- **Result**: Can't update colors site-wide, breaks design system
- **Fix**: Always use `var(--e-global-color-*)` variables

**❌ Mistake 4**: Forget to specify all 4 border sides
- **Result**: Only top border shows, sides/bottom missing
- **Fix**: Always specify top, right, bottom, left explicitly

**❌ Mistake 5**: Skip CSS regeneration or forget after some sections
- **Result**: Changes not visible on frontend, confusion ensues
- **Fix**: Regenerate CSS after EVERY section (mandatory!)

**❌ Mistake 6**: Verify in same browser window (cached CSS)
- **Result**: See old cached styles, think changes didn't work
- **Fix**: Always verify in NEW incognito window

---

## 🎓 FOR FUTURE AGENTS

**When you're asked to build/transform a page with V4 styling**:

1. **Read this file first** - Understand the complete workflow
2. **Follow the 4 steps IN ORDER** - Don't skip or rearrange
3. **Use the checklist** - Ensures nothing is forgotten
4. **Document your work** - Update SSOT files for next session
5. **If stuck**: Read LESSONS-LEARNED.md for solutions to known issues

**This workflow is PROVEN**. Programs page took ~3 hours following this process. Without this workflow, it would have taken 8-10 hours of trial and error.

**Trust the process. Follow the steps. Document the results.**

---

**Version**: 1.0
**Last Updated**: 2025-12-02
**Status**: MANDATORY for all V4 page builds
**Proven Success**: Programs page (ID: 25)
