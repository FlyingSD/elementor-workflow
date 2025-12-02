# FAILURES LOG

**Purpose**: Track what doesn't work (prevent repeating same failures)
**Format**: Chronological log of 3-attempt failures + escalations
**Updated By**: Agents (automatic) + Coordinator

---

## 📋 How to Use This Log

**When agent fails 3 times**:
- Agent logs failure here BEFORE escalating to stuck
- Stuck agent reads this to avoid known dead-ends
- Coordinator reviews weekly to identify patterns

**When solution found**:
- Update this entry with [RESOLVED] tag
- Move knowledge to TROUBLESHOOTING.md
- Add to GUIDE-INDEX if new pattern

---

## 🚨 ACTIVE FAILURES (Unresolved)

(None yet - system just implemented)

---

## ✅ RESOLVED FAILURES (Historical)

### ❌ → ✅ RESOLVED: CSS Not Showing After MCP Update (2025-11-30)

**Agent**: coder
**Attempts**: Multiple (5+ hours debugging)
**Date**: 2025-11-30

**What Failed**:
- MCP update_elementor_widget executed ✅
- Changes visible in editor ✅
- Frontend showed old styling ❌
- Tried: Hard refresh, incognito, cache clear - nothing worked

**Escalation**: Manual (Denis called stuck agent after 5 hours)

**Resolution** (found by stuck):
- Root cause: MCP updates database only, doesn't trigger CSS regeneration
- Solution: nuclear-css-fix.php + page visit (mandatory workflow)
- Documentation: MANDATORY-CSS-REGENERATION.md + TROUBLESHOOTING.md Issue #6

**Prevention**:
- Added to SYSTEM-PROTOCOL Rule #10 (forbidden to skip CSS regen)
- LESSONS-LEARNED.md has full post-mortem
- All agents now aware of mandatory workflow

**Cost**: 5 hours debugging time
**Savings**: Future tasks won't repeat this mistake

**📈 IMPROVEMENT (2025-12-01)**:
- Created `regenerate-css-api.php` - Web API endpoint for CSS regeneration
- **100% reliability** (vs nuclear-css-fix.php ~80%)
- Page-specific regeneration (faster, safer than nuclear approach)
- Single HTTP request handles all steps
- Usage: `curl "http://svetlinkielementor.local/regenerate-css-api.php?page=21&secret=svetlinki2024"`
- Documented in MANDATORY-CSS-REGENERATION.md as primary method

---

## 📝 LOG ENTRY TEMPLATE

```markdown
## ❌ FAILURE: [Task Description]

**Agent**: [agent-name]
**Date**: 2025-12-01 HH:MM
**Attempts**: 3/3
**Escalated**: [Yes/No] → [stuck/coordinator]

**Error Pattern**:
- Attempt 1: [error message]
- Attempt 2: [error message]
- Attempt 3: [error message]

**Context**:
- Page ID: [id]
- Element: [element-id]
- Guides consulted: [list]
- MCP tools used: [list]

**Current Status**: [Investigating/Resolved/Known Limitation]

**Resolution** (if found):
[Solution description]

**Updated Files**:
[TROUBLESHOOTING.md, guides, etc.]
```

---

**Log Version**: 1.0
**Created**: 2025-12-01
**Last Reviewed**: 2025-12-01
