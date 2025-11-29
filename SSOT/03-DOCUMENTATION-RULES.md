# Documentation Rules & Standards

**Version**: 1.0
**Effective Date**: 2025-11-28
**Purpose**: Ensure consistent, complete, and useful documentation throughout the project

---

## 🎯 Core Documentation Principles

### 1. Always Document Before You Forget
Document immediately after:
- Creating new pages
- Making configuration changes
- Discovering issues/blockers
- Completing major tasks
- Finding solutions to problems

### 2. Future You Should Understand
Write as if explaining to someone with zero context:
- Include "why" not just "what"
- Add context for decisions
- Link to related documentation
- Provide examples where helpful

### 3. Keep It Current
Documentation that's out of date is worse than no documentation:
- Update Progress Tracker daily
- Update Current State after major milestones
- Version all significant changes
- Mark deprecated information clearly

---

## 📝 What to Document

### ALWAYS Document

#### Configuration Changes
- WordPress settings modifications
- Plugin installations/activations
- Theme customizations
- MCP configuration changes
- Elementor Global Colors/Fonts updates
- Database modifications

**Format**:
```markdown
**Change**: [What was changed]
**Date**: YYYY-MM-DD
**Reason**: [Why it was changed]
**Impact**: [What this affects]
**Rollback**: [How to undo if needed]
```

#### Pages Created/Modified
- Page ID, title, slug
- Number of Elementor sections
- Content source (reference screenshot, original content)
- Special features (forms, carousels, etc.)
- Known issues or TODOs
- Verification status (Designer/Tester/QA agent)

**Format**:
```markdown
**Page**: [Title] (ID: XX)
**Created**: YYYY-MM-DD
**Sections**: X sections (list section IDs)
**Reference**: [screenshot filename]
**Status**: ✅/🟡/❌
**Issues**: [Any known problems]
**Next**: [What needs to be done]
```

#### Issues & Blockers
- Clear problem description
- When it was discovered
- Impact on progress
- Attempted solutions
- Current status
- Who is responsible

**Format**:
```markdown
**Issue #X**: [Short title]
**Severity**: Critical/High/Medium/Low
**Discovered**: YYYY-MM-DD
**Description**: [Detailed explanation]
**Impact**: [What this blocks]
**Attempts**: [What's been tried]
**Status**: Open/In Progress/Resolved
**Owner**: [Agent or person]
```

#### Decisions Made
- What was decided
- Available options considered
- Reasoning for choice
- Trade-offs accepted
- Who made the decision

**Format**:
```markdown
**Decision**: [What was decided]
**Date**: YYYY-MM-DD
**Options Considered**:
- Option A: [pros/cons]
- Option B: [pros/cons]
**Chosen**: Option X
**Reasoning**: [Why this choice]
**Trade-offs**: [What we're accepting]
```

---

## 📁 File Naming Conventions

### SSOT Folder Structure
```
SSOT/
├── README.md                    # Folder overview
├── 01-CURRENT-STATE.md         # Current status
├── 02-PROGRESS-TRACKER.md      # Progress dashboard
├── 03-DOCUMENTATION-RULES.md   # This file
├── 04-MASTER-GUIDE.md          # Technical guide
├── 05-CHANGE-LOG.md            # Chronological changes
├── 06-ISSUES-LOG.md            # Issue tracking
└── 07-DECISIONS-LOG.md         # Decision record
```

### Naming Rules
- Use `##-DESCRIPTIVE-NAME.md` format
- All caps for main words
- Hyphens for spaces
- Numbers for ordering
- `.md` extension for markdown

---

## ✏️ Writing Style Guidelines

### Use Clear, Direct Language
❌ "It seems like the page might not be working correctly"
✅ "Page 27 returns 404 error when accessed via navigation menu"

### Include Specific Details
❌ "Some pages need images"
✅ "8/8 pages missing hero images: Home, About, Programs, Contact, FAQ, Blog, Privacy, Terms"

### Provide Context
❌ "Changed the setting"
✅ "Changed `show_on_front` from 'posts' to 'page' to display static homepage instead of blog posts"

### Use Status Indicators
- ✅ Complete/Working
- 🟡 Partial/In Progress
- ⚠️ Warning/Needs Attention
- ❌ Not Done/Broken

### Format for Readability
- Use headers (`##`, `###`) for sections
- Use bullet lists for items
- Use numbered lists for sequences
- Use tables for comparisons
- Use code blocks for technical content

---

## 🔄 Update Frequency

### Daily (When Work Is Done)
- Progress Tracker percentages
- Completed tasks marked
- New blockers added

### Weekly
- Current State review
- Change log summary
- Issues log triage

### After Major Milestones
- Current State full revision
- Progress Tracker recalculation
- Master Guide updates (if architecture changed)

### As Needed
- Documentation Rules (when standards change)
- Decisions Log (when decisions made)
- Issues Log (when issues discovered/resolved)

---

## 🧹 Maintenance Guidelines

### Keep Documents Clean
- Remove resolved issues (move to archive section)
- Update outdated information
- Delete duplicate content
- Consolidate related information

### Version Control
- Add version number at top of document
- Include "Last Updated" date
- Log significant changes in document
- Keep change history section

### Link Maintenance
- Verify links work
- Update file paths if structure changes
- Use relative paths where possible
- Check for broken links weekly

---

## 🚫 What NOT to Document

### Don't Document Trivial Changes
- Minor text edits
- Small CSS tweaks
- Experimental changes that were reverted
- Personal notes/scratch work

### Don't Document Obvious Things
- "WordPress is a CMS" (everyone knows this)
- "Save your work before closing" (basic practice)
- Standard WordPress features (well-documented elsewhere)

### Don't Duplicate External Docs
- Link to official Elementor docs instead
- Link to WordPress Codex instead
- Reference MCP docs instead of copying

---

## ✅ Documentation Checklist

Before finishing any work session:

```markdown
[ ] Progress Tracker updated with completed tasks
[ ] New issues added to Current State → Critical Issues
[ ] Any configuration changes documented
[ ] Pages created/modified logged with details
[ ] Decisions made recorded with reasoning
[ ] Change Log updated with session summary
[ ] Next actions identified and prioritized
[ ] All documents have current "Last Updated" date
```

---

## 📊 Document Templates

### Issue Template
```markdown
## Issue #XXX: [Short Title]

**Severity**: Critical/High/Medium/Low
**Discovered**: YYYY-MM-DD HH:MM
**Reporter**: [Name/Agent]
**Affects**: [Pages/Features impacted]

### Description
[Detailed explanation of the problem]

### Steps to Reproduce
1. [Step one]
2. [Step two]
3. [Observed result]

### Expected Behavior
[What should happen]

### Current Workaround
[Temporary solution if any]

### Proposed Solution
[How to fix permanently]

### Status Updates
- YYYY-MM-DD: [Update]
- YYYY-MM-DD: [Update]
```

### Page Documentation Template
```markdown
## Page: [Title] (ID: XX)

**Created**: YYYY-MM-DD
**Slug**: /page-slug/
**Status**: ✅/🟡/❌
**Reference**: screenshot-name.png

### Structure
- Section 1: [section_id] - [Purpose]
- Section 2: [section_id] - [Purpose]
- Section 3: [section_id] - [Purpose]

### Content Source
[Where content came from - reference screenshot, original, translated, etc.]

### Widgets Used
- Heading (x2)
- Text Editor (x3)
- Button (x1)
- Image (x0) ← MISSING

### Design Compliance
- [ ] Uses Global Colors
- [ ] Uses Global Fonts
- [ ] Matches reference screenshot
- [ ] Responsive design verified
- [ ] Accessibility checked

### Known Issues
1. [Issue description]
2. [Issue description]

### Next Steps
1. [What needs to be done]
2. [What needs to be done]

### Verification Log
- [ ] Designer Agent review
- [ ] Tester Agent screenshots
- [ ] QA Agent 21-test suite
- [ ] Manual review
```

---

## 🎓 Examples of Good Documentation

### Example 1: Configuration Change
```markdown
**Change**: Configured WordPress to display static homepage
**Date**: 2025-11-28
**Settings Modified**:
- `show_on_front`: "posts" → "page"
- `page_on_front`: 0 → 21
**Reason**: Page 21 (Home) was created but not visible at root URL
**Impact**: Homepage now displays at http://svetlinkielementor.local/
**Command Used**:
curl -X POST -u "test:..." "http://svetlinkielementor.local/wp-json/wp/v2/settings" \
  -H "Content-Type: application/json" \
  -d '{"show_on_front":"page","page_on_front":21}'
**Rollback**: Set `show_on_front` to "posts" and `page_on_front` to 0
```

### Example 2: Issue Discovered
```markdown
## Issue #001: Media Library Empty - No Images

**Severity**: CRITICAL
**Discovered**: 2025-11-28 14:30
**Reporter**: Claude (during site audit)
**Affects**: All pages (0% visual completion)

### Description
WordPress media library contains zero files. All pages are missing:
- Hero images
- Testimonial photos
- Program illustrations
- Team member photos
- Icons/logos

### Impact
- Pages look incomplete
- Does not match reference screenshots
- Unprofessional appearance
- Blocks ~30% of remaining work

### Root Cause
Previous chat created text content but did not migrate images from Kadence site.

### Proposed Solution
1. Access Kadence site media library
2. Download all images (organize by category)
3. Upload to Elementor site media library
4. Update all pages with appropriate images
5. Verify against reference screenshots

### Status
- 2025-11-28: Discovered during audit
- 2025-11-28: Documented in Current State
- 2025-11-28: Added to Phase 3 tasks (high priority)
- NEXT: Execute image extraction and upload
```

---

## 🚨 Consequences of Poor Documentation

### What Happens When Documentation Fails

1. **Context Loss**: After /compact, you lose all knowledge of what was done
2. **Duplicate Work**: Re-doing work that was already completed
3. **Breaking Changes**: Modifying something without knowing why it was done
4. **Issue Recurrence**: Fixing same bug twice because fix wasn't documented
5. **Knowledge Silos**: Only one person knows how something works
6. **Slow Onboarding**: New team members can't get up to speed
7. **Project Delays**: Time wasted recreating understanding

### This Project Learned The Hard Way

**Previous Chat Session**:
- Created 8 pages ✅
- Configured MCP ✅
- Set up agents ✅
- **DOCUMENTED: NOTHING** ❌

**Result**:
- Had to audit entire site to understand what was done
- Discovered critical gaps (no images, no forms, no QA)
- Created this documentation system to prevent recurrence

---

## 💡 Documentation Tips

1. **Document as you go** - Don't wait until the end
2. **Use screenshots** - A picture is worth 1000 words
3. **Include commands** - Exact commands used (for reproduction)
4. **Link related docs** - Connect related information
5. **Update existing docs** - Don't create duplicate documents
6. **Be specific** - "Page 21" not "the homepage"
7. **Timestamp everything** - When was this true?
8. **Own your docs** - Sign your work with name/agent
9. **Review periodically** - Check docs are still accurate
10. **Ask "why"** - Future you will thank you

---

**Remember**:

> "Documentation is a love letter to your future self."
>
> "Code tells you how, documentation tells you why."
>
> "If it's not documented, it didn't happen."

---

**Version**: 1.0
**Created**: 2025-11-28
**Last Updated**: 2025-11-28
**Maintained by**: All contributors (human and AI)
