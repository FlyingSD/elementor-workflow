# Compress SSOT - Quick Reference

**Script**: `scripts/core/compress-ssot.js`
**Purpose**: Reduce SSOT file size by ~5-10% while preserving structure

---

## Quick Commands

```bash
# Preview compression (safe, no changes)
node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md --dry-run

# Compress single file
node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md

# Compress all SSOT files
node scripts/core/compress-ssot.js --all

# Get help
node scripts/core/compress-ssot.js --help
```

---

## What Gets Compressed

✅ Verbose phrases ("This is important because...")
✅ ASCII decorations (━━━, ───, ═══)
✅ Multiple blank lines (3+ → 2)
✅ Redundant examples (keeps first only)
✅ Label prefixes ("Note:", "Remember:")
✅ Verbose paragraphs (4+ sentences → bullets)

---

## What's Preserved

🔒 All `## ` headers (anchors!)
🔒 All code blocks
🔒 All tables
🔒 All links
🔒 All inline code
🔒 Already-formatted content

---

## Safety Features

🛡️ Automatic `.backup` file created
🛡️ Dated backup (e.g., `-backup-2025-12-01.md`)
🛡️ Anchor verification (aborts if broken)
🛡️ Dry run mode (preview before applying)

---

## Expected Results

| File | Savings |
|------|---------|
| STATIC_RULES.md | ~6% (229 lines) |
| ELEMENTOR-STRUCTURE-GUIDE.md | ~3.5% (36 lines) |
| CORE-WEBSITE-RULES.md | ~4.6% (39 lines) |
| ELEMENTOR-API-GUIDE.md | ~3.9% (28 lines) |
| **Total** | **5.4%** (332 lines) |

**Token savings**: ~10,000-15,000 per full SSOT load

---

## Quick Rollback

```bash
# Restore from latest backup
mv SSOT/STATIC_RULES.md.backup SSOT/STATIC_RULES.md

# Or from dated backup
mv SSOT/STATIC_RULES-backup-2025-12-01.md SSOT/STATIC_RULES.md

# Or from git
git checkout HEAD -- SSOT/STATIC_RULES.md
```

---

## Recommended Workflow

```bash
# 1. Dry run first (always!)
node scripts/core/compress-ssot.js --all --dry-run

# 2. Review output

# 3. Apply if good
node scripts/core/compress-ssot.js --all

# 4. Verify anchors work
node scripts/core/anchor-search.js "widget whitelist"

# 5. Commit
git add SSOT/*.md
git commit -m "Compress SSOT files (5.4% savings)"
```

---

## When to Use

**Compress after**:
- Adding 100+ lines to SSOT files
- Merging documents
- Adding verbose examples
- Quarterly cleanup

**Don't compress**:
- Small edits (<50 lines)
- Files already compressed recently
- While agents actively using files

---

**Full docs**: `scripts/core/README-compress-ssot.md`
**Created**: 2025-12-01
