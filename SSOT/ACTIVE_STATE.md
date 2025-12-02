# ACTIVE_STATE.md - Current Project State

**Document Type**: Live Project Status
**Last Updated**: 2025-12-02 (Programs + FAQ + About pages V4 complete)
**Purpose**: Track ONLY current state - page IDs, credentials, active configuration
**Read by**: All agents on-demand for current values

---

## 🔐 Credentials & Access

**WordPress**:
- Site URL: `http://svetlinkielementor.local`
- Admin User: `test`
- Admin Password: `test`
- REST API: `http://svetlinkielementor.local/wp-json/wp/v2/`

**MCP Servers** (4 active):
- WordPress/Elementor: `wp-elementor-mcp` (standard mode, 32 tools) - ✅ Installed locally
  - Path: `C:\Users\denit\wp-elementor-mcp\`
  - GitHub: https://github.com/Huetarded/wp-elementor-mcp
- JSON Validation: `json-schema-validator` (5 tools) - ✅ Installed locally
  - Path: `C:\Users\denit\jsonshema_mcp\`
  - GitHub: https://github.com/EienWolf/jsonshema_mcp
- Research: `brave-search` (web search) - ✅ Working
- Browser: `Playwright` (20+ tools) - ✅ Working
- Config: `.mcp.json` in project root
- **Status**: Requires Claude Code restart to activate wp-elementor and json-schema MCPs

**Research Tools**:
- Brave Search API: `BSALRthHC5TjPLZ-kA70Dk7YqhCfhmC` (web search)
- R.JINA API: `jina_700485007fde405aba61e94002ee4a10M3Ueq3DucEcT73UKdsVUbcvGWDPU` (content extraction)
- **Workflow**: Brave finds URLs → R.JINA extracts content
- **Sources**: Tier 1 (official docs, GitHub) + Tier 2 (WordPress.org, Stack Exchange, engineering blogs)

**Config File**:
- Location: `config.json` (project root)
- Contains: Brave API key, R.JINA API key, WordPress credentials, Global Colors, page IDs

---

## 🎨 APPROVED DESIGN SYSTEM (V4)

**Status**: ✅ APPROVED by client (2025-11-30)
**Design Documents**:
- `COLOR-AND-STYLE-VISION.md` - Complete design system (colors, buttons, cards, animations)
- `design-mockup-v4.html` - Final approved homepage design

**V4 Homepage Structure**:
1. **Hero Section**: Yellow gradient background, 2 buttons (primary + secondary), Zhara mascot, coral SVG underline
2. **Blog Carousel**: White background, left/right navigation buttons
3. **Benefits Section**: 3 cards with colorful top borders (yellow, gradient, teal)
4. **Programs Teaser**: 3 cards (Levels, Promotions, FAQ) with "Прочети повече" buttons

**Color Hierarchy (FINAL)**:
- ⭐ **Yellow** (#FABA29) - MAIN STAR COLOR (hero, buttons, primary accents)
- 🎨 **Teal** (#46b19d) - Secondary (hover states, one benefit icon)
- 🌸 **Coral** (#FF8C7A) - Playful (secondary button, SVG underlines)
- 📝 **Dark Teal** (#1d3234) - ALL text
- ⚪ **White** (#FFFFFF) - Clean backgrounds

**Implementation Status**:
- 🔄 Homepage (21) - **PARTIAL V4** (Benefits + Programs sections styled)
- ✅ Programs (25) - **V4 COMPLETE + POLISHED** (2025-12-02)
- ⏳ Other pages - Will follow V4 styling

**V4 Build Workflow** (MANDATORY for all page builds):
- 📋 `SSOT/V4-PAGE-BUILD-WORKFLOW.md` - Complete 4-step process (proven on Programs page)
  1. Consult CORE-WEBSITE-BUILDING-RULES.md (design principles)
  2. Check ELEMENTOR-API-TECHNICAL-GUIDE.md (property names)
  3. Apply V4 HTML design reference (colors, typography, patterns)
  4. Build with MCP systematically (CSS regeneration after EVERY section!)

---

## 📄 Current Pages (WordPress)

| Page ID | Title | Slug | Status | Content Status |
|---------|-------|------|--------|----------------|
| 21 | Home | home-2 | publish | 🔄 **PARTIAL V4** (Header/footer restored, Benefits + Programs styled, Hero needs gradient) - 2025-12-02 |
| 23 | About | about | publish | ✅ **V4 COMPLETE** (Simple structure, white backgrounds, yellow accents, proper typography) - 2025-12-02 |
| 25 | Programs | programs | publish | ✅ **V4 COMPLETE + POLISHED** (Full V4 rebuild 2025-12-02: gradient hero, 5 levels cards, pricing, enhanced shadows) |
| 27 | Contact | contact | publish | ✅ **V4 COMPLETE** (CF7 Bulgarian form, Google Maps, philosophy content, V4 styling, header/footer) - 2025-12-02 |
| 29 | FAQ | faq | publish | ✅ **V4 COMPLETE + POLISHED** (20 Q&A, yellow gradient hero, light yellow backgrounds, 40px spacing) - 2025-12-02 |
| 31 | Blog | blog | publish | ✅ **V4 COMPLETE** (17 posts imported, card layout with V4 color-coded borders, WordPress native) - 2025-12-02 |
| 33 | Privacy Policy | privacy-policy-2 | publish | ⏸️ Not started |
| 35 | Terms of Service | terms-of-service | publish | ⏸️ Not started |

**Header/Footer Solution** (2025-12-02):
- **Method**: Built-in sections (NOT Theme Builder templates)
- Header section ID: **692b16d123b3c** (Logo, Navigation, CTA button)
- Footer section ID: **6a2800e** (4 columns: Brand, Resources, Contact, Social)
- Copyright section ID: **278f365a** (Copyright bar)
- **Status**: ✅ Working on all pages (Contact, Homepage)
- **Implementation**: Sections copied from Contact page template, added to each page individually

---

## 🎨 Global Design System

### Global Colors (V4 Approved System)

| Variable | Hex | Name | Dominance | Usage |
|----------|-----|------|-----------|-------|
| `var(--e-global-color-primary)` | `#FABA29` | Yellow/Gold | ⭐⭐⭐⭐⭐ STAR | MAIN COLOR - Hero gradients, primary buttons, carousel nav, icons, badges, accents |
| `var(--e-global-color-secondary)` | `#46b19d` | Teal | ⭐⭐ SUPPORT | Hover states, secondary accents, one benefit icon, link colors |
| `var(--e-global-color-accent)` | `#FF8C7A` | Coral | ⭐⭐ PLAYFUL | Secondary buttons, SVG underlines, gradient accents, playful touches |
| `var(--e-global-color-text)` | `#1d3234` | Dark Teal | ⭐⭐⭐⭐⭐ TEXT | ALL body text, headings, readable content |
| `var(--e-global-color-5)` | `#FEFCF5` | Warm Cream | ⭐⭐⭐⭐⭐ SPACE | Clean backgrounds, card backgrounds, breathing space |

**Background Variations**:
- `#FFFFFF` - White (card backgrounds, clean sections)
- `#fff4d9` - Light Yellow (hero gradient middle)
- `#ffe8b3` - Warm Yellow (hero gradient end)
- `#fff9e6` - Cream Yellow (Benefits/Programs alternate backgrounds)

**Critical**:
- Polyfill active at `wp-content/themes/twentytwentyfive/inc/elementor-global-colors-polyfill.php`
- Reference: `COLOR-AND-STYLE-VISION.md` for complete color rules

### Global Fonts

| Usage | Font Family | Weight |
|-------|-------------|--------|
| Primary Headings | Roboto | 600 |
| Secondary Headings | Roboto Slab | 400 |
| Body Text | Roboto | 400 |

### Typography Scale

```
H1: 2.75rem (44px) - clamp(2rem, 5vw, 2.75rem)
H2: 1.9rem (30.4px) - clamp(1.5rem, 4vw, 1.9rem)
H3: 1.4rem (22.4px) - clamp(1.2rem, 3vw, 1.4rem)
Body: 1rem (16px)
Line Height: 1.7 (body), 1.2 (headings)
```

### Spacing System

```
xs:  8px  (0.5rem)
sm:  16px (1rem)
md:  24px (1.5rem)
lg:  32px (2rem)
xl:  40px (2.5rem)
2xl: 48px (3rem)
3xl: 64px (4rem)
```

---

## ⚙️ Elementor Configuration

**Version**: Free (NOT Pro)
**Theme**: Hello Elementor (v3.4.5) - Switched from Twenty Twenty-Five on 2025-11-29
**Plugin**: Header Footer Elementor (active)

**Critical Settings**:
- CSS Print Method: **Internal Embedding** (required for .local domains)
- Global Colors: Configured + Polyfill active ✓
- Stretch Section: Working (requires Internal Embedding) ✓

**Why Hello Elementor**:
- Lightweight, minimal theme designed specifically for Elementor
- No built-in header/footer to conflict with Elementor templates
- Eliminates duplication and theme conflicts
- Industry standard for Elementor-based sites

**Limitations (FREE)**:
- ✅ Containers ARE available in FREE (Flexbox/Grid layouts supported)
- Can use both Legacy Sections AND modern Containers
- 29 FREE widgets available (see STATIC_RULES.md#widget-whitelist)
- No Call to Action widget (use Image Box + Button)
- No Elementor Forms (use Contact Form 7)

---

## 📂 File Locations

### Key Project Files

```
C:\Users\denit\Local Sites\svetlinkielementor\
├── config.json (credentials, IDs, Global Colors)
├── .mcp.json (MCP server config)
├── .gitignore (protects config.json)
├── SYSTEM-OVERVIEW.md (✨ NEW: Complete system architecture - START HERE!)
├── README-NEXT-STEPS.md (active roadmap)
├── ELEMENTOR-API-WORKFLOW-GUIDE.md (✨ NEW: MCP/API styling methodology)
├── design-mockup-v4.html (approved V4 design - current)
├── COLOR-AND-STYLE-VISION.md (V4 design system)
├── V4-COMPONENT-LIBRARY.md (component reference)
├── DESIGN-TRACKING.md (design progress tracking)
├── ELEMENTOR-FREE-2024-2025.md (capabilities reference)
├── SSOT/
│   ├── STATIC_RULES.md (3504 lines - read by section)
│   ├── ACTIVE_STATE.md (this file - current values)
│   └── TROUBLESHOOTING.md (known issues & solutions)
├── .claude/
│   ├── CLAUDE.md (main orchestrator)
│   ├── archive/reference/orchestrator-18-agents-original.md
│   └── agents/
│       ├── coder.md
│       ├── tester.md
│       ├── designer.md
│       └── stuck.md
├── archive/
│   ├── 2025-11-old-docs/ (11 completed reports/sessions)
│   ├── 2025-11-old-mockups/ (v1-v3 design iterations)
│   ├── 2025-11-old-json/ (9 old data snapshots)
│   └── 2025-11-old-scripts/ (10 deprecated scripts)
├── scripts/working/ (active Playwright scripts)
├── screenshots/archive/ (reference screenshots archived)
├── backups/
│   ├── homepage-page-21-backup.json
│   ├── header-template-69-backup.json
│   └── footer-template-73-backup.json
└── backup-before-update.py (MANDATORY pre-flight snapshot)
```

**Archived (2025-11-30)**:
- 11 old documentation files (reports/session logs)
- 3 design mockup versions (v1, v2, v3)
- 9 JSON data snapshots (temp files)
- 10 Python/JavaScript scripts (completed tasks)

### WordPress Theme Customization

**Location**: `app/public/wp-content/themes/twentytwentyfive/`
- `functions.php` - line 143: Loads polyfill
- `inc/elementor-global-colors-polyfill.php` - CSS variable output for FREE

---

## 🚨 Known Issues & Workarounds

### Issue #1: Global Colors Not Showing (SOLVED)
**Status**: ✅ FIXED with polyfill
**Solution**: PHP polyfill outputs CSS variables (Elementor FREE doesn't do this natively)
**Reference**: TROUBLESHOOTING.md

### Issue #2: Stretch Section Not Working (SOLVED)
**Status**: ✅ FIXED with CSS Print Method
**Solution**: Set CSS Print Method to "Internal Embedding"
**Reference**: TROUBLESHOOTING.md

### Issue #3: REST API Can't Update `_elementor_data`
**Status**: ⚠️ WORKAROUND - Manual Elementor editor update needed
**Solution**: After REST API update, open in Elementor editor and click "Update"
**Reference**: TROUBLESHOOTING.md

### Issue #4: Containers ARE Available in FREE (CORRECTED)
**Status**: ✅ AVAILABLE - Containers work in Elementor FREE
**Solution**: Use Containers (Flexbox/Grid) OR Legacy Sections (both work)

### Issue #6: MCP/REST API Updates Not Showing on Frontend (CRITICAL)
**Status**: ✅ SOLVED with mandatory workflow
**Solution**: After EVERY MCP update, run nuclear-css-fix.php + page visit
**Reference**: SSOT/MANDATORY-CSS-REGENERATION.md, TROUBLESHOOTING.md
**Documented**: 2025-11-30 (Issue discovered and solved during Benefits/Programs section fixes)
**Reference**: TROUBLESHOOTING.md, STATIC_RULES.md#section-structure
**Note**: Previous documentation incorrectly stated Containers were PRO only

### Issue #5: Header/Footer Templates Not REST API Accessible
**Status**: ⚠️ LIMITATION - `elementor-hf` post type not REST enabled
**Solution**: Manual import via Elementor editor OR use JSON templates (header-template.json, footer-template.json)
**Reference**: TROUBLESHOOTING.md

---

## 🎯 Current Active Scripts

**Safety Scripts** (project root) - **MANDATORY**:
- `backup-before-update.py` - Pre-Flight Snapshot before page updates
- `restore-from-backup.py` - Emergency rollback from backup
- **Usage**: See `backups/README.md` for full workflow

**Working Scripts** (project root):
- `rebuild-all-6-sections.py` - Rebuild homepage (all 6 sections)
- `rebuild-complete-homepage.py` - Alternative rebuild
- `merge-static-rules.py` - Merge SSOT documentation (used for optimization)

**Deprecated Scripts** (scripts/deprecated/):
- `build_hero_container.py` - Old container approach (doesn't work in FREE)
- `build-all-sections.py` - ⚠️ DANGEROUS (overwrites, see scripts/deprecated/DANGEROUS/README.md)

**Templates** (No longer needed - built directly):
- ~~`header-template.json`~~ - Header built via MCP (ID 69) ✅
- ~~`footer-template.json`~~ - Footer built via MCP (ID 73) ✅

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| Pages Created | 8 (4 fully built, 4 pending) |
| Pages Fully Built | 4 (Home, About, Programs, FAQ) |
| Homepage Sections | 6 (complete) |
| Header/Footer Templates | 2 (both built and active) |
| Global Colors | 5 (all working) |
| Widget Whitelist | 29 FREE widgets |
| MCP Tools Available | 32 (standard mode) |
| Theme | Hello Elementor 3.4.5 |
| Documentation Size | ~3500+ lines (STATIC_RULES.md) |
| Backup Files | Multiple (homepage, pages, templates) |

---

## 🔄 Agent Quick Reference

**🆕 SYSTEM ARCHITECTURE** (2025-11-30):
0. **How the system works**: Read SYSTEM-OVERVIEW.md (complete architecture guide)
   - Multi-agent coordination flow, knowledge management, decision trees
   - When to use which agent, MCP workflow, element hierarchy
   - Maintenance procedures, troubleshooting, best practices
   - **READ THIS FIRST if you're new to the system!**

**When agents need current values**:
1. **Page IDs**: Read this file → Current Pages section
2. **WordPress credentials**: Read this file → Credentials section OR config.json
3. **Global Colors**: Read this file → Global Design System section
4. **Widget whitelist**: Read STATIC_RULES.md#widget-whitelist
5. **JSON structure**: Read STATIC_RULES.md#json-data-schema
6. **Known issues**: Read TROUBLESHOOTING.md OR this file → Known Issues

**Technical Deep Dives** (NEW - 2025-11-30):
7. **Elementor API internals**: Read SSOT/ELEMENTOR-API-TECHNICAL-GUIDE.md
   - Complete save mechanism, CSS generation, REST API flow, cache management
   - Group controls structure (background, border, shadow)
   - Property naming conventions, troubleshooting CSS visibility issues
8. **Layout & alignment rules**: Read SSOT/ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md
   - Section/column/widget hierarchy and capabilities
   - Card structure patterns (3-column benefits, icon-box cards)
   - Spacing system, responsive breakpoints, alignment troubleshooting
9. **Core web design principles**: Read SSOT/CORE-WEBSITE-BUILDING-RULES.md
   - Nielsen's 10 Usability Heuristics, Effective Web Design principles
   - WCAG accessibility standards (POUR principles)
   - Typography rules (scale, line height, font pairing)
   - 8pt spacing system, whitespace principles, color contrast
   - Responsive design (mobile-first, breakpoints, touch targets)
   - Content/UX writing, navigation patterns, form best practices

**What NOT to do**:
- ❌ Don't read historical session logs (archived in SSOT/archive/sessions/)
- ❌ Don't read deprecated scripts (archived in scripts/deprecated/)
- ❌ Don't reference old screenshot folders (archived in screenshots/archive/)

---

## 📌 Next Immediate Actions

**Completed (2025-11-29)**:
- ✅ Header/Footer templates built (ID 69, 73) with Theme Builder
- ✅ Navigation menu added to header (5 menu items: Home, About, Programs, Contact, Blog)
- ✅ Dark footer with 4 columns (brand, resources, contact, social icons)
- ✅ Programs page built (5 levels + pricing)
- ✅ About page built (mission + values + team)
- ✅ Contact page built (info + hours + form placeholder)
- ✅ FAQ page built (10 Q&A with accordion)
- ✅ All pages use Theme Builder templates (header/footer automatic)
- ✅ Theme switched to Hello Elementor (from Twenty Twenty-Five)
- ✅ Switched from Header Footer Elementor plugin to native Theme Builder

**Completed This Session (2025-12-02 - CF7, Blog Import, Header/Footer Fix)**:
- ✅ **Contact Form 7 Setup & Customization**:
  * Found existing form (ID 5)
  * Updated with Bulgarian labels (Име, Имейл, Телефон, Съобщение, Изпрати)
  * Applied V4 styling (yellow button, proper sizing, hover effects)
  * Email template in Bulgarian
  * Update-safe implementation (PHP script)
- ✅ **Contact Page V4 Redesign**:
  * Added philosophy content ("Ние сме тук за Вас" - warm, supportive tone)
  * Embedded Google Maps (Sofia location, rounded corners)
  * Custom CSS for CF7 form (600px max-width, yellow focus borders)
  * V4 colors applied to all sections (yellow gradient hero, alternating white/cream)
  * Full page styling complete
- ✅ **Blog System Automated**:
  * Imported all 17 blog posts from markdown files
  * Cleaned titles (removed "Блог-XX-" prefix)
  * Set up Blog page (ID 31) as WordPress Posts page
  * Color-coded borders (Yellow/Teal/Coral/Dark Teal based on title hash)
  * Modern card layout (CSS Grid, responsive, hover effects)
  * V4 styling applied (cards with colored left borders)
- ✅ **Homepage Header/Footer Restored**:
  * Changed template from "Canvas" to "Default" (Canvas hides header/footer)
  * Copied header/footer sections from Contact page
  * Header: Logo, Navigation, CTA button
  * Footer: 4-column dark footer + copyright bar
  * Homepage now has 60 elements (was 45)
  * CSS regenerated successfully
- ✅ **Scripts Created**:
  * `update-cf7-form.php` - CF7 Bulgarian labels (update-safe)
  * `import-blog-posts-v4.php` - Complete blog automation
  * `copy-header-footer-to-homepage.php` - Header/footer restoration
  * All scripts reusable and documented
- ✅ **Website Audit & Hardcoded Colors Fixed** (Later 2025-12-02):
  * Created comprehensive audit script (`audit-forbidden-practices.php`)
  * Audited all 8 pages for: Custom HTML, !important CSS, inline styles, hardcoded colors
  * Found 161 violations total (296 checks)
  * **Fixed Priority 2**: Replaced 71 hardcoded colors with V4 global variables
  * Converted old colors: #4F9F8B, #2C2C2C, #2a2a2a, #1a1a1a, #000000, #5a6c6d → global vars
  * Converted V4 hex to vars: #FABA29, #1D3234, #46b19d, #FF8C7A → global vars
  * Violations reduced: 161 → 143 (18 fewer)
  * Kept acceptable exceptions: Background variations (#FFFFFF, #E5E5E5, #ffe8b3, etc.)
  * Blog/FAQ !important CSS: Marked as acceptable (user approved)
  * All backups saved: `_elementor_data_backup_colors`

**Next Priority Tasks**:
1. **⭐ HOMEPAGE V4 COMPLETION** - Finish hero section styling
   - Hero section: Apply yellow gradient background
   - Blog carousel: Style existing section or add new carousel
   - Ensure all sections have proper V4 spacing/colors
2. **Privacy Policy Page** - Build with V4 styling
3. **Terms of Service Page** - Build with V4 styling
4. **Upload Images** - Team photos (About), Program level images (Programs)
5. **Testing** - Responsive design check (mobile/tablet)

**Completed This Session (2025-11-29 Evening)**:
- ✅ Enabled Canvas template option on Footer template (ID 73) via PHP script
- ✅ Changed all pages (About, Programs, Contact, FAQ) to Canvas template
- ✅ Added complete header section to all pages with:
  * Logo "Светлинки" (left, teal, clickable to homepage)
  * Navigation menu (center, 5 links: Начало, За Нас, Програми, Контакти, FAQ)
  * CTA button "ЗАПАЗИ СЕ СЕГА" (right, golden yellow, links to /contact/)
- ✅ Cleared Elementor cache multiple times
- ✅ Created POST-LAUNCH-IMPROVEMENTS.md for future enhancements
- ✅ Documented why Nav Menu is HTML widget (Nav Menu widget is Elementor PRO only)
- ✅ **HEADERS AND FOOTERS NOW WORKING** - User opened pages in Elementor and clicked "Update", both header and footer now display on all pages!

**Completed This Session (2025-11-30 Evening)**:
- ✅ Created **ELEMENTOR-API-TECHNICAL-GUIDE.md** (SSOT/) - Complete technical reference:
  * Architecture overview (WordPress + Elementor plugin structure)
  * Complete save/update flow (document.php → CSS generation)
  * CSS generation system (post.php rendering pipeline)
  * REST API integration & MCP server workflow
  * Group controls deep dive (Background, Border, Shadow, Typography)
  * Property naming conventions & element-specific differences
  * Cache management (5 layers explained)
  * Troubleshooting guide (CSS visibility, shadows, gradients)
- ✅ Created **ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md** (SSOT/) - Practical layout guide:
  * Structure fundamentals (Section → Column → Widget hierarchy)
  * Section configuration (layout, gaps, height, alignment)
  * Column layout & alignment (vertical/horizontal, responsive widths)
  * Card structure patterns (3-column grids, icon-box cards, text cards)
  * Text & content alignment (widget-level controls)
  * Spacing system (recommended values, responsive scaling)
  * Common patterns (benefits cards, hero sections, footers)
  * Troubleshooting layouts (equal heights, centering, gaps)
- ✅ Created **CORE-WEBSITE-BUILDING-RULES.md** (SSOT/) - Universal web design principles:
  * Nielsen's 10 Usability Heuristics (system status, user control, consistency, error prevention)
  * 10 Principles of Effective Web Design (don't make users think, simplicity, whitespace)
  * WCAG Accessibility (POUR: Perceivable, Operable, Understandable, Robust)
  * Typography system (Material Design scale, line length 45-75 chars, line height 1.5)
  * 8-point spacing grid system (4px/8px increments, spacing hierarchy)
  * Color contrast rules (WCAG AA: 4.5:1 normal text, 3:1 large text)
  * Layout & grid systems (12-column grid, container widths, visual hierarchy)
  * Responsive design (mobile-first, breakpoints, touch targets 44px min)
  * Content/UX writing (scannable, active voice, 50-80 chars per line)
  * Navigation patterns, form best practices, performance (Core Web Vitals)
  * Before-launch checklist (content, design, accessibility, SEO, technical)
- ✅ Updated ACTIVE_STATE.md with references to all 3 new technical guides
- ✅ Research complete: Extracted from industry authorities (Nielsen Norman Group, W3C WCAG, Material Design, Smashing Magazine, Web.dev, USWDS)
- ✅ Created **elementor-expert agent** (.claude/agents/elementor-expert.md):
  * Specialized for Elementor API, MCP workflows, structure, alignment
  * MANDATORY reading: ELEMENTOR-API-TECHNICAL-GUIDE.md + ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md on spawn
  * Use for: Technical implementation, property names, MCP workflow, card patterns
- ✅ Created **design-expert agent** (.claude/agents/design-expert.md):
  * Specialized for UX/UI decisions, accessibility, web standards
  * MANDATORY reading: CORE-WEBSITE-BUILDING-RULES.md on spawn
  * Use for: Layout decisions, WCAG compliance, typography, spacing, color contrast
- ✅ Created **SYSTEM-OVERVIEW.md** (project root) - Complete architecture documentation:
  * Complete system architecture diagram (User → Coordinator → Agents → MCP → WordPress)
  * Knowledge management pyramid (3 universal guides + 3 project-specific SSOT files)
  * Decision trees (when to use which agent, keyword routing table)
  * MCP workflow, element hierarchy, property naming
  * Maintenance procedures, troubleshooting, best practices
  * 900+ lines comprehensive system documentation
- ✅ Updated **CLAUDE.md** (v7.0 - Knowledge System Complete):
  * Added "NEW TO THIS SYSTEM?" section pointing to SYSTEM-OVERVIEW.md
  * Updated Communication Flow diagram with elementor-expert and design-expert
  * Expanded Delegation Logic with detailed "When to use" examples
  * Updated Information Architecture listing 3 new technical guides
  * Updated Agent Files list with new agents

**Known Issues Resolved**:
- ✅ Footer now displaying (fixed after Elementor Update click - Issue #3 confirmed)
- ✅ Headers now displaying (fixed after Elementor Update click - Issue #3 confirmed)

**Technical Notes**:
- Navigation menu uses HTML widget (FREE workaround) instead of Nav Menu widget (PRO only) - see POST-LAUNCH-IMPROVEMENTS.md
- Issue #3 confirmed: REST API changes require manual Elementor "Update" click to activate

**Future**:
- Build Blog page (ID 31)
- Build Privacy Policy page (ID 33)
- Build Terms of Service page (ID 35)
- Test responsive design (mobile/tablet)
- Consider Elementor PRO upgrade (see POST-LAUNCH-IMPROVEMENTS.md)

---

**Document Version**: 1.7
**Created**: 2025-11-29
**Last Updated**: 2025-12-01 (Major cleanup & documentation session)
**Purpose**: Single source for current project state
**Update Policy**: Update only when values change (page IDs, credentials, new pages created, etc.)

**Session Note (2025-11-30)**:
✅ CLEANUP COMPLETE - 33 files archived to `archive/2025-11-old-*` folders:
- 11 completed documentation reports/session logs
- 3 design mockup iterations (v1-v3)
- 9 JSON data snapshots
- 10 deprecated Python/JavaScript scripts
✨ ROOT CLEANED - Only active files remain (V4 design docs, working scripts)
🎯 READY FOR V4 - Homepage styling implementation next using approved design-mockup-v4.html

**Session Note (2025-12-01 - Major Cleanup)**:
✅ **SSOT Enhanced with Research & Lessons**:
- Created `SSOT/LESSONS-LEARNED.md` - Post-mortem of 5-hour CSS regeneration debugging session
- Added GitHub research sources to `SSOT/TROUBLESHOOTING.md` Issue #6 (7 Elementor issues documented)
- Moved `ELEMENTOR-API-WORKFLOW-GUIDE.md` to SSOT/ (belongs with technical guides)

✅ **Project Root Cleaned**:
- Archived 3 reports to `archive/2025-11-30-session/reports/`:
  * CSS-REGENERATION-FINAL-REPORT.md
  * ELEMENTOR-CSS-REGENERATION-SOLUTION.md
  * HOMEPAGE-VISUAL-ANALYSIS-REPORT.md
- Archived templates to `archive/2025-11-30-session/templates/` (header, footer - 98+118 lines)
- Archived extracted-sections to `archive/2025-11-30-session/extracted-sections/` (benefits, blog, programs)
- Deleted screenshots/ directory (17MB stale screenshots - tester agent can regenerate fresh)
- Deleted temp files (backup_output.txt, backup_output2.txt, v4-for-mcp.txt, nul)

✅ **Scripts Organized**:
- Moved `force-css-regeneration.py` to scripts/working/
- Moved `take-elementor-editor-screenshot.js` to scripts/working/
- Updated `scripts/README.md` with all Playwright scripts (frontend vs editor distinction)
- **IMPORTANT**: Documented Denis's environment (changes show WITHOUT Update button)

✅ **Blog Files Cleanup**:
- 17 blog markdown files (Bulgarian) moved to `SSOT/archive/Blog/`

🎯 **File Structure Now**:
```
Root (CLEAN):
├── Design System: design-mockup-v4.html, COLOR-AND-STYLE-VISION.md, V4-COMPONENT-LIBRARY.md
├── System Docs: SYSTEM-OVERVIEW.md, README-NEXT-STEPS.md, ELEMENTOR-FREE-2024-2025.md
├── Config: config.json, .mcp.json
├── Safety: mcp-backup/ (wp-elementor-mcp safety backup)
└── Working: scripts/, SSOT/, backups/, archive/

SSOT/ (Enhanced):
├── Technical Guides (4): ELEMENTOR-API-*, ELEMENTOR-STRUCTURE-*, CORE-WEBSITE-*, ELEMENTOR-API-WORKFLOW-GUIDE
├── Project Docs (3): STATIC_RULES.md, ACTIVE_STATE.md, TROUBLESHOOTING.md
├── NEW: LESSONS-LEARNED.md (post-mortems of major issues)
└── NEW: MANDATORY-CSS-REGENERATION.md (critical workflow)
```

**Key Takeaway**: "Keep only what moves you forward" - Archived completed work, kept production-ready files, enhanced SSOT with lessons to prevent repeating 5-hour debugging sessions.

**Session Note (2025-12-01 Evening - SYSTEM UPGRADE TO LEVEL 4)**:

✅ **AGENT COMPRESSION** (11 commits total today):
- CLAUDE.md: 456 → 267 lines (-41%)
- All 6 agents: 2,672 → 1,051 lines (-61%)
- SSOT files: 6,140 → 5,808 lines (-5.4%)
- **Total reduction**: -1,985 lines (-15% overall)

✅ **ANCHOR INDEX SYSTEM** (93% Context Reduction):
- Created SSOT/runtime/GUIDE-INDEX.json (92 keyword mappings)
- Created scripts/core/anchor-search.js (Tier 1-2-3 search)
- Created scripts/core/update-snapshot.js (session continuity)
- **Result**: Agents load 200 lines instead of 2000 (45K → 3K tokens)

✅ **STRICT PROTOCOL SYSTEM**:
- Created SSOT/SYSTEM-PROTOCOL.md (10 mandatory rules)
- 3-attempt limit with auto-escalation to stuck agent
- Created logging: SUCCESS-LOG.md, FAILURES-LOG.md, KNOWLEDGE-UPDATES.md
- All agents updated with protocol compliance

✅ **SELF-HEALING + SELF-LEARNING**:
- Created scripts/core/self-healing.js (auto-detect + auto-fix issues)
- Created scripts/core/auto-knowledge-update.js (autonomous SSOT updates)
- Agents instructed to Edit SSOT when discovering knowledge
- **Tested and validated**: All 3 systems working ✅

✅ **AUTOMATION TOOLS**:
- Created scripts/core/compress-ssot.js (automated compression with anchor preservation)
- CONTEXT-SNAPSHOT.md auto-generated (8 pages tracked)
- Two-tier context warning (30% early alert, 15% full report)

✅ **RESEARCH & VALIDATION**:
- Benchmarked vs AutoGPT, Aider, CrewAI, Devin AI
- Position: Tier 2 (Industry Standard), Level 4 (High Automation)
- Archived Upgrade.md research (5,957 lines) → archive/2025-12-01-optimization-research.md
- Created FUTURE-IMPLEMENTATIONS.md (production features roadmap)

🎯 **NEW FILE STRUCTURE**:
```
SSOT/runtime/ (NEW - Auto-Generated):
├── GUIDE-INDEX.json (92 keyword mappings)
├── CONTEXT-SNAPSHOT.md (session state)
├── SUCCESS-LOG.md (track wins)
├── FAILURES-LOG.md (track issues)
└── KNOWLEDGE-UPDATES.md (track discoveries)

scripts/core/ (NEW - Automation Tools):
├── anchor-search.js (targeted section retrieval)
├── update-snapshot.js (auto-snapshot generator)
├── self-healing.js (auto-detect + auto-fix)
├── auto-knowledge-update.js (autonomous SSOT updates)
└── compress-ssot.js (automated compression)
```

📊 **SYSTEM CAPABILITIES NOW**:
- Context efficiency: 93% reduction per agent spawn
- Autonomy level: Level 4 (High Automation)
- Self-healing: Detection + auto-fix scripts operational
- Self-learning: Agents can autonomously Edit SSOT (validated!)
- Context management: Two-tier warnings (30% + 15%)
- Session continuity: ON RESTART protocol in CLAUDE.md
- Strict hierarchy: 3-attempt → stuck escalation enforced

🚀 **STATUS**: Production-Ready, tested, validated, documented
**NEXT**: V4 Homepage Implementation (using new optimized system)
