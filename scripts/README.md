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

### Utility Scripts

**merge-static-rules.py**
- **Purpose**: Merge 4 SSOT files into STATIC_RULES.md
- **Usage**: `python scripts/working/merge-static-rules.py`
- **Used for**: Phase 2 optimization (Golden Triangle creation)
- **Note**: One-time use script (completed)

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
