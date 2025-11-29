# ACTIVE_STATE.md - Current Project State

**Document Type**: Live Project Status
**Last Updated**: 2025-11-29
**Purpose**: Track ONLY current state - page IDs, credentials, active configuration
**Read by**: All agents on-demand for current values

---

## 🔐 Credentials & Access

**WordPress**:
- Site URL: `http://svetlinkielementor.local`
- Admin User: `test`
- Admin Password: `S27q64rqoFhfTPDA30nBhNM5` (Application Password)
- REST API: `http://svetlinkielementor.local/wp-json/wp/v2/`

**MCP Servers**:
- WordPress/Elementor: `wp-elementor-mcp` (standard mode, 32 tools)
- Research: `brave-search` (web search engine)
- Config: `.mcp.json` in project root

**Research Tools**:
- Brave Search API: `BSALRthHC5TjPLZ-kA70Dk7YqhCfhmC` (web search)
- R.JINA API: `jina_700485007fde405aba61e94002ee4a10M3Ueq3DucEcT73UKdsVUbcvGWDPU` (content extraction)
- **Workflow**: Brave finds URLs → R.JINA extracts content
- **Sources**: Tier 1 (official docs, GitHub) + Tier 2 (WordPress.org, Stack Exchange, engineering blogs)

**Config File**:
- Location: `config.json` (project root)
- Contains: Brave API key, R.JINA API key, WordPress credentials, Global Colors, page IDs

---

## 📄 Current Pages (WordPress)

| Page ID | Title | Slug | Status | Purpose |
|---------|-------|------|--------|---------|
| 21 | Home | home-2 | publish | Homepage (6 sections built) |
| 23 | About | about | publish | About page |
| 25 | Programs | programs | publish | Programs listing |
| 27 | Contact | contact | publish | Contact form page |
| 29 | FAQ | faq | publish | FAQ/Questions |
| 31 | Blog | blog | publish | Blog listing |
| 33 | Privacy Policy | privacy-policy-2 | publish | Privacy page |
| 35 | Terms of Service | terms-of-service | publish | Terms page |

**Templates**:
- Header: Template ID **69** (`elementor-hf` post type)
- Footer: Template ID **73** (`elementor-hf` post type)

**Status**: Header/Footer templates exist but are EMPTY (awaiting content import)

---

## 🎨 Global Design System

### Global Colors (Elementor Site Settings)

| Variable | Hex | Name | Usage |
|----------|-----|------|-------|
| `var(--e-global-color-primary)` | `#FABA29` | Yellow/Gold | CTA buttons, accents |
| `var(--e-global-color-secondary)` | `#4F9F8B` | Teal/Green | Headings, links |
| `var(--e-global-color-text)` | `#2C2C2C` | Dark Gray | Body text |
| `var(--e-global-color-accent)` | `#FEFCF5` | Warm Cream | Backgrounds |

**Critical**: Polyfill active at `wp-content/themes/twentytwentyfive/inc/elementor-global-colors-polyfill.php`

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
**Theme**: Twenty Twenty-Five
**Plugin**: Header Footer Elementor (active)

**Critical Settings**:
- CSS Print Method: **Internal Embedding** (required for .local domains)
- Global Colors: Configured + Polyfill active ✓
- Stretch Section: Working (requires Internal Embedding) ✓

**Limitations (FREE)**:
- Must use Legacy Sections: `Section > Column > Widget` (NOT Containers - PRO only)
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
├── API.txt (WordPress password - deprecated, use config.json)
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
├── scripts/deprecated/ (7 old scripts archived)
├── screenshots/archive/ (reference screenshots archived)
├── backups/
│   ├── homepage-page-21-backup.json
│   ├── header-template-69-backup.json
│   └── footer-template-73-backup.json
└── rebuild-all-6-sections.py (WORKING rebuild script)
```

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

### Issue #4: Flexbox Containers Don't Work
**Status**: ⚠️ EXPECTED - PRO feature
**Solution**: Use Legacy Sections: `Section > Column > Widget`
**Reference**: TROUBLESHOOTING.md, STATIC_RULES.md#section-structure

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

**Templates Ready for Import**:
- `header-template.json` - Header content (manual import needed)
- `footer-template.json` - Footer content (manual import needed)

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| Pages Created | 8 |
| Homepage Sections | 6 (complete) |
| Global Colors | 4 (all working) |
| Widget Whitelist | 29 FREE widgets |
| MCP Tools Available | 32 (standard mode) |
| Documentation Size | ~3500+ lines (STATIC_RULES.md) |
| Backup Files | 3 (homepage, header, footer) |

---

## 🔄 Agent Quick Reference

**When agents need current values**:
1. **Page IDs**: Read this file → Current Pages section
2. **WordPress credentials**: Read this file → Credentials section OR config.json
3. **Global Colors**: Read this file → Global Design System section
4. **Widget whitelist**: Read STATIC_RULES.md#widget-whitelist
5. **JSON structure**: Read STATIC_RULES.md#json-data-schema
6. **Known issues**: Read TROUBLESHOOTING.md OR this file → Known Issues

**What NOT to do**:
- ❌ Don't read historical session logs (archived in SSOT/archive/sessions/)
- ❌ Don't read deprecated scripts (archived in scripts/deprecated/)
- ❌ Don't reference old screenshot folders (archived in screenshots/archive/)

---

## 📌 Next Immediate Actions

**Critical Path** (must be done in order):
1. Test agent delegation after architecture simplification (see commit 0ff70f0)
2. Continue Golden Triangle optimization (Phase 2-5 from OPTIMIZATION-MASTER-PLAN.md)
3. Import header/footer templates (header-template.json, footer-template.json)
4. Verify all pages working after optimization

**Post-Optimization**:
- Install JSON Schema MCP for validation (see OPTIMIZATION-MASTER-PLAN.md)
- Create Python validation scripts (validate_elementor_json.py, find_hardcoded_values.py)
- Resume page building with optimized workflow

---

**Document Version**: 1.0
**Created**: 2025-11-29
**Purpose**: Single source for current project state
**Update Policy**: Update only when values change (page IDs, credentials, new pages created, etc.)
