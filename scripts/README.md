# Scripts Directory

**Organization**: Phase 5 - Script Organization Complete
**Date**: 2025-11-29

---

## 📁 Directory Structure

```
scripts/
├── working/          Production-ready scripts (USE THESE)
├── templates/        JSON templates for manual import
└── deprecated/       Old/non-working scripts (DO NOT USE)
```

---

## ✅ working/ - Production Scripts

### Safety Scripts (MANDATORY)

**backup-before-update.py**
- **Purpose**: Pre-Flight Snapshot before page updates
- **Usage**: `python scripts/working/backup-before-update.py --page-id 21 --task "hero-fix"`
- **Output**: `backups/page_21_before_hero-fix_TIMESTAMP.json`
- **When**: BEFORE every `update_elementor_page_data()` call
- **See**: `backups/README.md` for full workflow

**restore-from-backup.py**
- **Purpose**: Emergency rollback from backup
- **Usage**: `python scripts/working/restore-from-backup.py --page-id 21 --latest`
- **When**: If page update goes wrong (white screen, broken layout)
- **Speed**: 10-second rollback vs hours to rebuild

### Homepage Rebuild Scripts

**rebuild-all-6-sections.py**
- **Purpose**: Rebuild homepage (all 6 sections)
- **Usage**: `python scripts/working/rebuild-all-6-sections.py`
- **Sections**: Hero, Benefits, Programs, Pricing CTA, Testimonials, Contact
- **Status**: ✅ WORKING (tested 2025-11-29)

**rebuild-complete-homepage.py**
- **Purpose**: Alternative homepage rebuild approach
- **Usage**: `python scripts/working/rebuild-complete-homepage.py`
- **Status**: ✅ WORKING (alternative implementation)

### Page Building Scripts

**build-modern-hero.py**
- **Purpose**: Build hero section only
- **Usage**: `python scripts/working/build-modern-hero.py`
- **When**: Hero section needs update

**build-about-page.py**
- **Purpose**: Build About page (ID 23)
- **Usage**: `python scripts/working/build-about-page.py`

**build-programs-page.py**
- **Purpose**: Build Programs page (ID 25)
- **Usage**: `python scripts/working/build-programs-page.py`

**build-contact-page.py**
- **Purpose**: Build Contact page (ID 27)
- **Usage**: `python scripts/working/build-contact-page.py`

**build-faq-page.py**
- **Purpose**: Build FAQ page (ID 29)
- **Usage**: `python scripts/working/build-faq-page.py`

### Header/Footer Management

**update-header-template.py**
- **Purpose**: Update header template (ID 69)
- **Usage**: `python scripts/working/update-header-template.py`

**update-header-simple.py**
- **Purpose**: Simplified header update
- **Usage**: `python scripts/working/update-header-simple.py`

**update-footer-template.py**
- **Purpose**: Update footer template (ID 73)
- **Usage**: `python scripts/working/update-footer-template.py`

**add-header-footer-to-homepage.py**
- **Purpose**: Add header/footer sections to homepage
- **Usage**: `python scripts/working/add-header-footer-to-homepage.py`

### CSS Regeneration & Testing

**force-css-regeneration.py**
- **Purpose**: Force Elementor CSS regeneration (diagnostic tool)
- **Usage**: `python scripts/working/force-css-regeneration.py 21`
- **When**: Testing CSS generation, debugging visibility issues
- **Note**: For MCP workflow, use nuclear-css-fix.php instead

**⚠️ MANDATORY MCP Workflow (2025-12-01)**:

After EVERY MCP update, run these 2 commands:

```bash
# Step 1: Nuclear CSS fix
curl -s "http://svetlinkielementor.local/nuclear-css-fix.php"

# Step 2: Visit page to trigger regeneration
curl -s "http://svetlinkielementor.local/home" > nul
```

**Important Note (Denis's Environment - 2025-12-01)**:
- Changes show WITHOUT manual Update button ✅
- nuclear-css-fix.php + page visit is SUFFICIENT
- Issue #3 workaround (click Update in editor) NOT needed
- See `SSOT/MANDATORY-CSS-REGENERATION.md` for full documentation

### Playwright Testing Scripts

**take-screenshots-only.js**
- **Purpose**: Take FRONTEND screenshots ONLY (homepage)
- **Usage**: `node scripts/working/take-screenshots-only.js`
- **Output**: Desktop (1920x1080), Tablet (768x1024), Mobile (375x812)
- **When**: Visual QA of homepage frontend

**take-elementor-editor-screenshot.js**
- **Purpose**: Take EDITOR screenshots ONLY (Elementor backend)
- **Usage**: `node scripts/working/take-elementor-editor-screenshot.js`
- **Output**: Full editor view + Update button area
- **When**: Debugging editor issues, documenting editor state

**click-update-and-screenshot.js**
- **Purpose**: Automate Issue #3 workaround (login → editor → click Update)
- **Usage**: `node scripts/working/click-update-and-screenshot.js`
- **When**: REST API changes not showing (may not be needed in Denis's environment)

**Best Practice**: Run BOTH screenshot scripts for complete visual QA:
```bash
# Frontend screenshots
node scripts/working/take-screenshots-only.js

# Editor screenshots
node scripts/working/take-elementor-editor-screenshot.js
```

**Note**: Playwright scripts separated to avoid confusion:
- Frontend vs Editor screenshots are different views
- Run appropriate script based on what you need to verify

### Utility Scripts

**merge-static-rules.py**
- **Purpose**: Merge 4 SSOT files into STATIC_RULES.md
- **Usage**: `python scripts/working/merge-static-rules.py`
- **Used for**: Phase 2 optimization (Golden Triangle creation)
- **Note**: One-time use script (completed)

**emergency-restore.py**
- **Purpose**: Quick restore without prompts
- **Usage**: `python scripts/working/emergency-restore.py --backup "path/to/backup.json"`
- **When**: Critical failure, need immediate restore

**import-faq-page.php**
- **Purpose**: Import FAQ page via PHP (WordPress context)
- **Usage**: `php scripts/working/import-faq-page.php`
- **When**: REST API import fails

---

## 📄 templates/ - JSON Templates

**header-template.json**
- **Content**: Header structure (site name + CTA button)
- **Template ID**: 69 (from ACTIVE_STATE.md)
- **Import**: Manual via Elementor editor UI
  1. WP Admin → Elementor → Tools → Template Library
  2. Import template from file
  3. Assign to "Entire Website" display rule

**footer-template.json**
- **Content**: Footer structure (copyright + contact info)
- **Template ID**: 73 (from ACTIVE_STATE.md)
- **Import**: Same as header (manual)

**Why manual?**
- `elementor-hf` post type NOT REST API accessible
- REST API attempts will fail
- See `SSOT/TROUBLESHOOTING.md` Issue #5

---

## 🗄️ deprecated/ - Old Scripts (DO NOT USE)

**Location**: `scripts/deprecated/`

**Files**:
- `build_hero_container.py` - Container approach (doesn't work in FREE)
- `export_hero_structure.py` - Old export utility
- `verify_hero_structure.py` - Old verification
- `build-section-2-benefits.py` - Partial section builder
- `build-header-footer.py` - Failed (REST API not accessible)
- `update-header-footer-db.py` - Failed (MySQL connection)

**DANGEROUS**:
- `scripts/deprecated/DANGEROUS/build-all-sections.py`
  - ⚠️ Overwrites existing sections without backup
  - See `scripts/deprecated/DANGEROUS/README.md` for warnings

**Why archived?**
- Reference for learning what NOT to do
- Historical context
- "Disk is cheap, knowledge is expensive"

---

## 🚀 Quick Start

### Before Updating a Page (MANDATORY):
```bash
# 1. Create Pre-Flight Snapshot
python scripts/working/backup-before-update.py --page-id 21 --task "description"

# 2. Make your changes via MCP or Python

# 3. If something goes wrong:
python scripts/working/restore-from-backup.py --page-id 21 --latest
```

### Rebuild Homepage:
```bash
python scripts/working/rebuild-all-6-sections.py
```

### Import Header/Footer:
```
1. Open Elementor → Tools → Template Library
2. Click "Import Template"
3. Select scripts/templates/header-template.json
4. Assign to "Entire Website" → Header
5. Repeat for footer-template.json
```

---

## 📊 Configuration

**All scripts read from**: `config.json` (project root)

**Config contains**:
- WordPress credentials (base_url, username, password)
- Page IDs (homepage: 21, header: 69, footer: 73)
- Global Colors (Primary, Secondary, Accent, Text)
- Brave Search API key
- R.JINA API key

**Example** (from config.json):
```json
{
  "wordpress": {
    "base_url": "http://svetlinkielementor.local",
    "auth": {
      "user": "test",
      "password": "S27q64rqoFhfTPDA30nBhNM5"
    }
  }
}
```

---

## 🔒 Security

**Sensitive files**:
- `config.json` - Contains credentials (NOT in git)
- `.gitignore` - Protects config.json

**Backup strategy**:
- Pre-Flight Snapshots: Local (`backups/` directory)
- Static backups: Git (`backups/` committed)
- Full project: GitHub (`elementor-workflow` repo)

---

## 📚 Documentation

**For detailed workflows**, see:
- `backups/README.md` - Pre-Flight Snapshot workflow
- `SSOT/STATIC_RULES.md#mcp-checklist` - MCP page creation
- `SSOT/TROUBLESHOOTING.md` - Known issues & solutions
- `.claude/agents/coder.md` - Safety rules & workflows

---

**Created**: 2025-11-29 (Phase 5)
**Purpose**: Organized script directory with clear separation
**Philosophy**: working/ for production, deprecated/ for history, templates/ for manual imports
