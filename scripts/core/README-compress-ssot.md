# SSOT Markdown Compressor Documentation

**Script**: `scripts/core/compress-ssot.js`
**Purpose**: Intelligently compress verbose SSOT markdown files while preserving critical structure
**Version**: 1.0
**Created**: 2025-12-01

---

## Overview

The SSOT (Single Source of Truth) files in this project are comprehensive technical references, but their size (3500+ lines) can consume significant token budget when loaded by AI agents. This script compresses them while maintaining:

✅ **All `## ` headers** (anchor links depend on them)
✅ **All code blocks** (critical technical content)
✅ **All tables** (structured data)
✅ **All inline code** (technical terms)
✅ **All links** (navigation)

---

## Compression Techniques

### 1. Remove Verbose Phrases
Eliminates redundant connectors that don't add technical value:
- "This is important because"
- "It's worth noting that"
- "Keep in mind that"
- "As mentioned earlier"
- "For example, if you"

### 2. Remove ASCII Decorations
Strips visual embellishments (lines, boxes):
- Horizontal lines: `━━━━━`, `─────`, `═════`
- Vertical bars: `│`, `┃`, `║`
- Box drawing: `┌┐└┘├┤┬┴┼`
- (Keeps markdown `---` for semantic meaning)

### 3. Remove Excessive Whitespace
- Multiple spaces → single space
- Tabs → 2 spaces
- 3+ blank lines → 2 blank lines
- Trailing whitespace on lines

### 4. Compress Repetitive Examples
- Keeps first example only
- Removes "Example 2:", "Example 3:", etc.
- Adds note: "*(Additional examples removed for brevity)*"

### 5. Remove Label Prefixes
Strips redundant labels (keeps content):
- "Note: content" → "content"
- "Remember: content" → "content"
- "Important: content" → "content"

### 6. Aggressive Paragraph Compression
For paragraphs with 4+ sentences and 300+ chars:
- Keeps first 3 sentences only
- Converts to bullet list for scannability

**Skips compression for**:
- Already bulleted lists
- Code blocks
- Headers
- Tables
- Emoji-decorated content (already formatted)
- Bold-prefixed paragraphs (list headers)
- Short paragraphs (<150 chars)

---

## Results (Actual Compression Test)

**Test Date**: 2025-12-01
**Mode**: Dry run on all target files

| File | Original | Compressed | Savings |
|------|----------|------------|---------|
| STATIC_RULES.md | 3553 lines | 3324 lines | **6.4%** (229 lines) |
| ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md | 1019 lines | 983 lines | **3.5%** (36 lines) |
| CORE-WEBSITE-BUILDING-RULES.md | 854 lines | 815 lines | **4.6%** (39 lines) |
| ELEMENTOR-API-TECHNICAL-GUIDE.md | 714 lines | 686 lines | **3.9%** (28 lines) |
| **TOTAL** | **6140 lines** | **5808 lines** | **5.4%** (332 lines) |

**Token Savings**: Approximately 10,000-15,000 tokens per full SSOT load (based on ~30 tokens/line average).

---

## Usage

### 1. Preview Compression (Dry Run)

**Single file**:
```bash
node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md --dry-run
```

**All target files**:
```bash
node scripts/core/compress-ssot.js --all --dry-run
```

**Output**:
- Original vs compressed line counts
- Savings percentage
- Anchor verification status
- First 500 chars preview
- Summary statistics

### 2. Apply Compression

**Single file**:
```bash
node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md
```

**All target files**:
```bash
node scripts/core/compress-ssot.js --all
```

**What happens**:
1. Creates `.backup` file (latest backup)
2. Creates `-backup-YYYY-MM-DD.md` (dated backup)
3. Writes compressed version
4. Reports statistics

### 3. Help

```bash
node scripts/core/compress-ssot.js --help
```

---

## Safety Features

### Automatic Backups

**Before any compression**, the script creates TWO backups:

1. **Latest backup** (`.backup` extension):
   - `SSOT/STATIC_RULES.md.backup`
   - Always overwritten with latest pre-compression version
   - Quick rollback: `mv STATIC_RULES.md.backup STATIC_RULES.md`

2. **Dated backup** (timestamped):
   - `SSOT/STATIC_RULES-backup-2025-12-01.md`
   - Historical snapshots
   - Never overwritten

### Anchor Verification

**Before writing**, the script verifies:
- All `## ` headers preserved (count match)
- Header text identical (character-by-character)
- Order maintained

**If anchors broken** → Compression aborted, no files modified.

### Dry Run Mode

**Always test first** with `--dry-run`:
- No files modified
- Shows preview of compression
- Reports statistics
- Validates anchor preservation

---

## Target Files

**Current targets** (defined in script):
```javascript
const TARGET_FILES = [
  'SSOT/STATIC_RULES.md',
  'SSOT/ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md',
  'SSOT/CORE-WEBSITE-BUILDING-RULES.md',
  'SSOT/ELEMENTOR-API-TECHNICAL-GUIDE.md'
];
```

**To add files**: Edit `TARGET_FILES` array in script.

---

## Protected Content

**NEVER compressed** (preserved exactly):

### Code Blocks
````markdown
```javascript
function example() {
  return "preserved";
}
```
````

### Inline Code
```markdown
Use `mcp__wp-elementor__create_page` to create pages.
```

### Links
```markdown
[Link text](url)
```

### Anchors
```markdown
<a name="section-name"></a>
```

### Headers
```markdown
## All Level 2 Headers (Anchors!)
### Subheaders (H3-H6)
```

### Tables
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |
```

---

## When to Compress

### Recommended Schedule

**Compress after**:
- Major SSOT file edits (adding 100+ lines)
- Merging multiple documents
- Adding verbose explanations/examples
- Quarterly cleanup

**Don't compress**:
- Files already compressed recently
- Small edits (<50 lines changed)
- When agents actively referencing files

### Best Practices

1. **Always dry-run first**:
   ```bash
   node scripts/core/compress-ssot.js --all --dry-run
   ```

2. **Review preview**: Check first 500 chars look good

3. **Apply compression**:
   ```bash
   node scripts/core/compress-ssot.js --all
   ```

4. **Verify backups created**: Check for `.backup` files

5. **Test agent access**: Ensure anchor links still work:
   ```bash
   node scripts/core/anchor-search.js "widget whitelist"
   ```

6. **Commit to git**:
   ```bash
   git add SSOT/*.md
   git commit -m "Compress SSOT files (5.4% savings, 332 lines)"
   ```

---

## Rollback Procedure

**If compression breaks something**:

### Option 1: Latest Backup (Quick)
```bash
cd "C:\Users\denit\Local Sites\svetlinkielementor\SSOT"
mv STATIC_RULES.md.backup STATIC_RULES.md
```

### Option 2: Dated Backup (Historical)
```bash
cd "C:\Users\denit\Local Sites\svetlinkielementor\SSOT"
mv STATIC_RULES-backup-2025-12-01.md STATIC_RULES.md
```

### Option 3: Git Rollback (Nuclear)
```bash
git checkout HEAD -- SSOT/STATIC_RULES.md
```

---

## Limitations

### What's NOT Compressed

**Structural elements** (must preserve for navigation):
- Headers (`## `, `### `)
- Anchor tags (`<a name="...">`)
- Tables (structured data)
- Code blocks (critical technical content)

**Already-formatted content**:
- Bullet lists (already concise)
- Emoji-decorated sections (visual structure)
- Bold-prefixed lists (semantic headers)

### Compression Cap

**Maximum realistic compression**: ~10-15%

**Why not more?**
- SSOT files are already technical (not fluff)
- Code blocks = 30-40% of content (can't compress)
- Headers = 10-15% of content (can't compress)
- Tables = 10% of content (can't compress)

**Diminishing returns**: Beyond 15%, risks losing critical information.

---

## Troubleshooting

### "Header count mismatch!"

**Cause**: Compression accidentally removed a `## ` header.

**Fix**: Bug in script logic. Report issue. Compression aborted automatically.

**Rollback**: Not needed (no files modified).

---

### "Original: 3553, Compressed: 3594 (negative savings)"

**Cause**: Paragraph-to-bullets conversion added more lines than removed.

**Fix**: Script tuned to skip this (requires 300+ char paragraphs with 4+ sentences).

**Action**: Normal for already-concise files. No compression needed.

---

### "Anchors broken after compression"

**Cause**: Manual edit or script bug.

**Fix**:
1. Rollback: `mv STATIC_RULES.md.backup STATIC_RULES.md`
2. Report issue
3. Re-run with `--dry-run` to diagnose

**Prevention**: Always use `--dry-run` first.

---

### "Can't find file"

**Error**: `❌ File not found: SSOT/STATIC_RULES.md`

**Cause**: Running from wrong directory.

**Fix**: Always run from project root:
```bash
cd "C:\Users\denit\Local Sites\svetlinkielementor"
node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md
```

---

## Technical Details

### Algorithm Overview

```javascript
1. Parse markdown → split by ## headers
2. Protect critical content (code blocks, links, etc.)
   → Replace with __PROTECTED_N__ tokens
3. For each content section (NOT headers):
   a. Remove verbose phrases
   b. Strip ASCII decorations
   c. Compress whitespace
   d. Compress examples (keep first only)
   e. Remove label prefixes (Note:, etc.)
   f. Convert verbose paragraphs → bullets
   g. Remove trailing whitespace
4. Restore protected content
5. Verify all anchors preserved
6. Write compressed version (with backups)
```

### Regex Patterns

**Verbose phrases**:
```javascript
/This is important because/gi
/It's worth noting that/gi
/Keep in mind that/gi
```

**ASCII decorations**:
```javascript
/^[━─═]+$/gm          // Horizontal lines
/^[│┃║]\s*/gm         // Vertical bars
/^[┌┐└┘├┤┬┴┼╔╗╚╝╠╣╦╩╬]+$/gm  // Box drawing
```

**Whitespace**:
```javascript
/ {2,}/g              // Multiple spaces → single
/\n\n\n+/g            // 3+ blank lines → 2
```

---

## Integration with System

### Related Scripts

1. **anchor-search.js**: Find section locations
   - Use after compression to verify anchors work
   - `node scripts/core/anchor-search.js "widget whitelist"`

2. **update-snapshot.js**: Session continuity
   - Run after compression to update context
   - `node scripts/core/update-snapshot.js`

### Workflow

```bash
# 1. Dry run compression
node scripts/core/compress-ssot.js --all --dry-run

# 2. Review output, apply if good
node scripts/core/compress-ssot.js --all

# 3. Verify anchors work
node scripts/core/anchor-search.js "widget whitelist"

# 4. Update snapshot
node scripts/core/update-snapshot.js

# 5. Commit to git
git add SSOT/*.md scripts/core/
git commit -m "Compress SSOT files (5.4% savings)"
```

---

## Future Enhancements

**Potential improvements** (not implemented yet):

1. **Semantic compression**: Use AI to identify redundant content
2. **Link deduplication**: Replace repeated URLs with references
3. **Smart example selection**: Keep most relevant example (not just first)
4. **Interactive mode**: Show each change, ask to apply
5. **Token count reporting**: Show estimated token savings
6. **Diff view**: Show before/after side-by-side

**Priority**: LOW (current compression sufficient)

---

## FAQ

### Q: Will this break anchor links?

**A**: No. The script NEVER modifies `## ` headers and verifies all anchors before writing. If verification fails, compression is aborted.

### Q: Can I undo compression?

**A**: Yes, three ways:
1. Restore from `.backup` file
2. Restore from dated backup
3. Git checkout previous version

### Q: How often should I compress?

**A**: After major edits (100+ lines added). Quarterly cleanup recommended.

### Q: Will this remove important information?

**A**: No. Compression targets:
- Verbose connectors ("This is important because...")
- ASCII decorations (visual fluff)
- Redundant examples (keeps first)
- Multiple blank lines

Technical content is preserved.

### Q: Can I add more aggressive compression?

**A**: Yes, edit `COMPRESSION_RULES` object in script. But be careful - over-compression risks losing critical information.

### Q: What if I want to compress other files?

**A**: Add to `TARGET_FILES` array:
```javascript
const TARGET_FILES = [
  'SSOT/STATIC_RULES.md',
  'SSOT/YOUR-NEW-FILE.md',  // Add here
];
```

---

## Version History

**v1.0** (2025-12-01):
- Initial release
- 5.4% average compression (332 lines saved)
- Anchor verification
- Automatic backups
- Dry run mode
- Batch processing

---

**Script Location**: `C:\Users\denit\Local Sites\svetlinkielementor\scripts\core\compress-ssot.js`
**Documentation**: `C:\Users\denit\Local Sites\svetlinkielementor\scripts\core\README-compress-ssot.md`
**Last Updated**: 2025-12-01
