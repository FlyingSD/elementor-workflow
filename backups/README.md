# WordPress Pages Backup

**Created**: 2025-11-29 10:09
**Updated**: 2025-11-29 (added automated Pre-Flight Snapshot workflow)
**Purpose**: Static backups + automated Pre-Flight Snapshots before updates

---

## 🚨 PRE-FLIGHT SNAPSHOT (MANDATORY WORKFLOW)

**NEW (2025-11-29)**: Automated backup before EVERY page update!

### Why Pre-Flight Snapshot?

**Nightmare Scenario**:
1. Update page with new JSON
2. JSON is valid but accidentally empty/wrong
3. Page becomes white screen
4. No recent backup to restore from

**Solution**: Always create timestamped backup BEFORE update!

### Automated Backup Scripts

**Location**: Project root directory

#### 1. `backup-before-update.py` - Create Pre-Flight Snapshot

```bash
# Before updating page 21
python backup-before-update.py --page-id 21 --task "hero-fix"

# Result:
# ✅ Backup saved: backups/page_21_before_hero-fix_20251129_143052.json
```

**What it does**:
- Fetches current page data from WordPress REST API
- Validates structure (not empty, valid elTypes)
- Saves timestamped backup to `backups/` directory
- Returns success/failure status

**Filename format**:
```
backups/page_{page_id}_before_{task}_{timestamp}.json
```

#### 2. `restore-from-backup.py` - Emergency Rollback

```bash
# Restore from latest backup
python restore-from-backup.py --page-id 21 --latest

# OR restore from specific backup
python restore-from-backup.py --backup "backups/page_21_before_hero-fix_20251129_143052.json"
```

**What it does**:
- Loads backup JSON file
- POSTs to WordPress REST API to restore page
- Verifies restoration by fetching page again
- Confirms with user before overwriting

### When to Use Pre-Flight Snapshot

**MANDATORY before**:
- ✅ Updating existing page content (`update_elementor_page_data()`)
- ✅ Modifying page structure (`update_page()`)
- ✅ Experimenting with new sections/widgets
- ✅ ANY change to live pages

**NOT needed for**:
- ❌ Creating NEW pages (nothing to backup)
- ❌ Testing on draft pages (can delete and recreate)

### Benefits

- ⚡ **Fast recovery**: 10 seconds to rollback vs hours to rebuild
- 🛡️ **Safety net**: Try changes without fear
- 📊 **Audit trail**: See exactly what changed when
- 🔍 **Debugging**: Compare old vs new JSON side-by-side

---

## Static Backup Files (Initial Snapshots)

These are one-time backups created before major changes:

### Files Included:

### 1. `homepage-page-21-backup.json` (32KB)
**Page ID**: 21
**URL**: http://svetlinkielementor.local/home-2/
**Status**: Working - All 6 sections present

**Sections**:
1. Hero (cream background, counters, CTA)
2. Benefits (3 icon boxes)
3. Programs (5 program levels)
4. Pricing CTA
5. Testimonials (2 cards)
6. Contact

### 2. `header-template-69-backup.json` (124 bytes)
**Template ID**: 69
**Name**: "Main header"
**Type**: Header Footer Elementor template
**Status**: Empty (awaiting content import)
**Display Rule**: Entire Website

### 3. `footer-template-73-backup.json` (124 bytes)
**Template ID**: 73
**Name**: "Footer"
**Type**: Header Footer Elementor template
**Status**: Empty (awaiting content import)
**Display Rule**: Entire Website

---

## How to Restore:

### Homepage (Page 21):
```bash
curl -X POST "http://svetlinkielementor.local/wp-json/wp/v2/pages/21" \
  -u "test:S27q64rqoFhfTPDA30nBhNM5" \
  -H "Content-Type: application/json" \
  -d @homepage-page-21-backup.json
```

Then:
1. Open in Elementor editor
2. Click "Update" button
3. Clear Elementor cache

### Header Template (69):
Note: `elementor-hf` post type is not REST API accessible.
Must restore via Elementor editor UI import feature.

### Footer Template (73):
Same as header - manual import required.

---

## Additional Backups:

### GitHub Repository:
**URL**: https://github.com/FlyingSD/elementor-workflow
**Commit**: 5688791 "Backup before optimization (2025-11-29)"

Contains:
- All Python scripts
- All documentation (SSOT/)
- Configuration files (.claude/, .mcp.json)
- Templates (header-template.json, footer-template.json)

### Local Files:
**Location**: `C:\Users\denit\Local Sites\svetlinkielementor\`
**Git branch**: master
**Status**: Clean working directory (all files committed)

---

## System Configuration:

**WordPress Version**: 6.7.1
**Elementor Version**: Free (latest)
**PHP Version**: 8.2
**Local WP**: Active

**Elementor Settings**:
- CSS Print Method: Internal Embedding ✓
- Global Colors Polyfill: Active ✓
- Header Footer Elementor: Installed & Active ✓

**Global Colors**:
- Primary: #FABA29 (Yellow)
- Secondary: #4F9F8B (Teal)
- Accent: #FEFCF5 (Cream)
- Text: #2C2C2C (Dark gray)

---

## Notes:

1. Header/footer templates are empty but configured correctly
2. Ready-to-import content available in:
   - `header-template.json` (project root)
   - `footer-template.json` (project root)
3. All backups verified before optimization started
4. GitHub remote is up to date

---

**Backup Status**: ✅ COMPLETE
**Last Verified**: 2025-11-29 10:09
