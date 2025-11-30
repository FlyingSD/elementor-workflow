# 🔄 POST-COMPACT CONTEXT RESTORATION - Svetlinki Project

**Created**: 2025-11-30
**Purpose**: COMPLETE context restoration after /compact command
**Status**: PRODUCTION READY - Read this FIRST!
**Progress**: 75% Complete

---

## ⚡ INSTANT RESTORATION (Read in Order)

### **Step 1: Core Identity** (30 seconds)
- **Project**: Educational center website (Mental Arithmetic for kids 5-12, Sofia, Bulgaria)
- **Philosophy**: "Every child has their own light (светлинка)"
- **Site**: http://svetlinkielementor.local
- **Tech**: WordPress 6.7.1 + Elementor FREE + Hello Elementor theme
- **Auth**: test / S27q64rqoFhfTPDA30nBhNM5

### **Step 2: Critical Constraints** (1 minute)
```
❌ NO Flexbox Containers (elType: 'container') - PRO ONLY!
✅ MUST USE: Section > Column > Widget (Legacy Sections)
✅ Global Colors via PHP polyfill (outputs CSS vars in <head>)
✅ CSS Print Method: Internal Embedding (fixes .local caching)
✅ 29 FREE widgets only (no Call to Action, Forms, Posts)
```

### **Step 3: What's Done** (30 seconds)
- ✅ Homepage (Page 21) - 6 sections complete + headers/footers
- ✅ About (23), Programs (25), FAQ (29) - Complete
- ✅ Contact (27) - Built but needs CF7 + Google Maps
- ✅ Blog content - 17 posts written (SSOT/Blog/) ready to publish
- ⏳ Blog page (31), Privacy (33), Terms (35) - Not built

### **Step 4: File Structure** (30 seconds)
```
SSOT/
├── ACTIVE_STATE.md          ← Current page IDs, credentials, colors
├── STATIC_RULES.md          ← Widget list, JSON schema (read by section)
├── TROUBLESHOOTING.md       ← 5 known issues + solutions
└── Blog/*.md                ← 17 posts ready (Bulgarian)

.claude/agents/
├── coder.md                 ← MCP page builder
├── designer.md              ← Design compliance enforcer
├── tester.md                ← Playwright screenshots
└── stuck.md                 ← Research (Brave + WebFetch)
```

### **Step 5: Agent System** (30 seconds)
```
Invoke via Task tool:
- "create/build" → coder agent (MCP tools)
- "design/colors" → designer agent (Global Colors)
- "test/screenshot" → tester agent (Playwright)
- "problem/stuck" → stuck agent (research)
```

### **Step 6: Next Priority** (10 seconds)
1. Fix Contact page (CF7 + maps + template)
2. Build Blog page (content ready!)
3. Fix homepage layouts (Benefits + Programs cramped)

**DONE! You're restored. Continue working.**

---

## 📊 DETAILED STATUS (If Needed)

### **Pages Completed:**
| ID | Page | Status | Notes |
|----|------|--------|-------|
| 21 | Homepage | ✅ Complete | 6 sections, headers/footers working |
| 23 | About | ✅ Complete | 4 sections, team placeholders |
| 25 | Programs | ✅ Complete | 5 levels + pricing |
| 27 | Contact | 🟡 Partial | Needs CF7 form + Google Maps |
| 29 | FAQ | ✅ Complete | 10 Q&A accordion |
| 31 | Blog | ❌ Not built | Content ready (17 posts) |
| 33 | Privacy | ❌ Not built | - |
| 35 | Terms | ❌ Not built | - |

### **Headers/Footers:**
- ✅ Header (Template 69): Logo + 5-item nav + CTA button
- ✅ Footer (Template 73): 4 columns, dark teal background
- ✅ Working on ALL pages via native Theme Builder

---

## 🎨 GLOBAL DESIGN SYSTEM

### **Colors (via PHP Polyfill):**
```css
--e-global-color-primary:   #FABA29  /* Yellow/Gold */
--e-global-color-secondary: #4F9F8B  /* Teal/Green */
--e-global-color-accent:    #FEFCF5  /* Warm Cream */
--e-global-color-text:      #2C2C2C  /* Dark Gray */
```

**Polyfill Location**: `wp-content/themes/twentytwentyfive/inc/elementor-global-colors-polyfill.php`

### **Typography:**
- H1: 2.75rem (clamp(2rem, 5vw, 2.75rem))
- H2: 1.9rem (clamp(1.5rem, 4vw, 1.9rem))
- H3: 1.4rem (clamp(1.2rem, 3vw, 1.4rem))
- Body: 1rem, line-height: 1.7

### **Fonts:**
- Headings: Roboto (600)
- Secondary: Roboto Slab (400)
- Body: Roboto (400)

---

## 🏗️ TECHNICAL ARCHITECTURE

### **CRITICAL: Elementor FREE Structure**
```javascript
// ✅ CORRECT (Legacy Sections):
{
  elType: 'section',  // NOT 'container'!
  settings: {
    stretch_section: 'section-stretched',  // Full-width
    layout: 'full_width',
    background_color: 'var(--e-global-color-accent)'
  },
  elements: [{
    elType: 'column',  // Mandatory wrapper
    settings: { _column_size: 100 },
    elements: [
      { elType: 'widget', widgetType: 'heading', settings: {...} }
    ]
  }]
}
```

### **Widget Property Names (NOT INTUITIVE!):**
```javascript
Heading:      { title_color: "..." }      // NOT color!
Text Editor:  { text_color: "..." }       // NOT color!
Button:       { button_text_color: "..." } // NOT text_color!
Counter:      { number_color: "...", title_color: "..." }
```

### **29 FREE Widgets:**
Basic: Heading, Text Editor, Image, Video, Button, Divider, Spacer
Media: Image Box, Icon, Icon Box, Image Carousel, Icon List
Special: Counter, Progress Bar, Testimonial, Tabs, Accordion, Toggle, Social Icons, Alert, Rating, Google Maps

### **NOT Available (PRO only):**
❌ Call to Action, Forms, Posts, Advanced Carousels
✅ Flexbox Containers (Available in FREE - documentation corrected 2025-11-30)

---

## 🔌 MCP & AGENTS

### **4 MCP Servers Active:**
1. **wp-elementor-mcp** (Standard Mode - 32 tools) ✅
   - Location: `C:\Users\denit\wp-elementor-mcp\`
   - Tools: `create_page`, `update_page`, `create_elementor_section`
   - `add_widget_to_section`, `upload_media`, `clear_elementor_cache_by_page`
   - GitHub: https://github.com/Huetarded/wp-elementor-mcp

2. **json-schema-validator** (5 tools) 🆕
   - Location: `C:\Users\denit\jsonshema_mcp\`
   - Tools: `generate_schema`, `validate_json_schema`, `add_update_schema`
   - Purpose: Validate Elementor JSON before deployment
   - GitHub: https://github.com/EienWolf/jsonshema_mcp

3. **brave-search** (Web research) ✅
   - Used by stuck agent for problem solving

4. **Playwright** (Browser automation - 20+ tools) ✅
   - Tools: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`
   - Used by tester agent for visual QA

### **4 Agents:**
- **coder**: MCP page builder, Pre-Flight Snapshot workflow
- **designer**: Global Colors/Fonts enforcer, design compliance
- **tester**: Playwright screenshots, 21-point checklist
- **stuck**: Problem solver via Brave Search + WebFetch

---

## ⚠️ KNOWN ISSUES (5 Documented)

### **Issue #1: Global Colors Not Showing** ✅ SOLVED
- **Solution**: PHP polyfill active
- **File**: `twentytwentyfive/inc/elementor-global-colors-polyfill.php`

### **Issue #2: Stretch Section Not Working** ✅ SOLVED
- **Solution**: CSS Print Method = "Internal Embedding"
- **Path**: Elementor → Settings → Performance

### **Issue #3: REST API Updates Don't Apply** ⚠️ WORKAROUND
- **Solution**: Open page in Elementor editor, click "Update"
- **Reason**: REST API bypasses Elementor hooks

### **Issue #4: Containers ARE Available in FREE** ✅ CORRECTED (2025-11-30)
- **Previous Misconception**: Containers thought to be PRO-only
- **Actual**: Flexbox/Grid Containers work in Elementor FREE
- **Solution**: Use Containers OR Legacy Sections (both work!)

### **Issue #5: Header/Footer Not REST Accessible** ✅ RESOLVED
- **Old Issue**: `elementor-hf` post type not REST enabled
- **New Solution**: Using native Theme Builder (works perfectly!)

**Full details**: `SSOT/TROUBLESHOOTING.md`

---

## 📝 BLOG CONTENT (17 Posts Ready!)

**Location**: `SSOT/Blog/*.md`
**Language**: Bulgarian
**Tone**: Honest, conversational ("Без Захаросване")

**Key Posts:**
- Блог-01: Трансформацията (What mental arithmetic really is)
- Блог-13: FAQ (20 honest parent questions)
- Блог-17: Философията на Светлинки (Core philosophy)

All 17 posts written and ready to publish on Blog page (31).

---

## 🚨 SAFETY RULES (MANDATORY!)

### **CRITICAL RULE #1: IMPROVEMENTS vs REPLACEMENTS**

**WHEN USER PROVIDES REFERENCE/INSPIRATION:**

✅ **DO - IMPROVE EXISTING**:
- Use reference for **styling ideas** (colors, layouts, spacing)
- Use reference for **design patterns** (two-column, gradients, etc.)
- **KEEP ALL existing content/information**
- **ENHANCE** what's already there
- Add new elements **alongside** existing ones

❌ **DON'T - REPLACE EVERYTHING**:
- ❌ NEVER delete all existing sections
- ❌ NEVER rebuild from scratch unless explicitly told
- ❌ NEVER remove existing content/widgets
- ❌ NEVER assume "reference" means "replace everything"

**KEY DISTINCTION**:
- "Use this as reference" = **INSPIRATION for styling**
- "Rebuild this entirely" = **FULL REPLACEMENT**

**IF UNCLEAR → ASK USER FIRST!**

**Example**:
- User shows React hero code → Use for styling ideas (gradient, layout)
- KEEP existing Bulgarian text, counters, CTA buttons
- IMPROVE styling/layout, DON'T delete everything

---

### **CRITICAL RULE #2: Pre-Flight Snapshot Before EVERY Update:**
```bash
# 1. Backup FIRST:
python backup-before-update.py --page-id 21 --task "description"

# 2. Make changes via MCP

# 3. If breaks:
python restore-from-backup.py --page-id 21 --latest
```

**Why**: 10-second rollback vs hours to rebuild
**Docs**: `backups/README.md`, `.claude/agents/coder.md`

---

## 🎯 NEXT PRIORITIES (Phase 1: Critical)

### **P1 - Critical (Before Launch):**
1. ✅ Fix Contact page (add CF7 form + Google Maps)
2. ✅ Fix Contact template (remove blog metadata "By test")
3. ✅ Fix homepage Benefits section (3 cards cramped)
4. ✅ Fix homepage Programs section (5 cards narrow)

### **P2 - High Priority:**
5. ✅ Build Blog page (17 posts ready!)
6. ✅ Fix Title Case (Bulgarian capitalization)
7. ✅ Add team photos to About page
8. ✅ Add program level images

### **P3 - Medium Priority:**
9. ✅ Build Privacy Policy page
10. ✅ Build Terms of Service page
11. ✅ Test responsive design
12. ✅ Optimize images

---

## 💡 QUICK PROBLEM SOLVING

**If stuck:**
1. Check `SSOT/TROUBLESHOOTING.md` (5 known issues)
2. Check `SSOT/STATIC_RULES.md` (by section)
3. Check `SSOT/ACTIVE_STATE.md` (current state)
4. Delegate to stuck agent for research

**Common Issues:**
- Colors not showing? → Check polyfill in browser DevTools
- Section not full-width? → Check CSS Print Method
- REST API not working? → Click "Update" in Elementor editor
- Containers failing? → Use Legacy Sections

---

## ✅ RESTORATION CHECKLIST

After reading this, you should know:
- [ ] Project purpose (educational center, mental arithmetic, Sofia)
- [ ] Current status (75% done, 4 pages complete, blog content ready)
- [ ] Elementor FREE constraints (Legacy Sections, 29 widgets, NO Containers)
- [ ] Agent system (4 agents via Task tool)
- [ ] MCP configuration (3 servers: wp-elementor, brave-search, playwright)
- [ ] Global Colors (4 colors via PHP polyfill)
- [ ] Widget property names (title_color, text_color, button_text_color)
- [ ] Known issues (5 documented with solutions)
- [ ] File structure (SSOT/, .claude/agents/, Blog/)
- [ ] Next priorities (Contact, Blog, layout fixes)
- [ ] Safety rules (Pre-Flight Snapshot)
- [ ] Blog content ready (17 posts)

**✅ RESTORATION COMPLETE! Continue working on design improvements.**

---

**Version**: 2.0 (Enhanced)
**Last Updated**: 2025-11-30
**Maintainer**: Claude Code Main Coordinator
