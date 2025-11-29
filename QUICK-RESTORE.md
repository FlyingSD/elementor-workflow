# Quick Context Restore - Start Here After /clear or Restart

**Use this**: Copy and paste this entire file to Claude Code after restart or /clear command

---

## 🎯 Where We Are Now

**Project**: Svetlinki Elementor AI Automation (WordPress + Elementor FREE)
**Status**: Optimization Phase 3 & 5 Complete ✅ | Phase 4 Partial (50%)
**Last Commit**: `0fa1cf6` - Phase 3 & 5: Agent compression + script organization
**Date**: 2025-11-29

---

## 📁 Project Architecture (Golden Triangle)

### The 3 Active Files (Read These First):
1. **SSOT/ACTIVE_STATE.md** - Current state (credentials, page IDs, next action)
2. **SSOT/STATIC_RULES.md** - Rules that never change (widget list, JSON schema)
3. **SSOT/TROUBLESHOOTING.md** - 5 known issues with solutions

### Agent System (2-Hop Model):
```
User (Denis)
  ↓
Claude Code (coordinator) → reads .claude/CLAUDE.md
  ↓ Task tool
  ├─→ coder agent → .claude/agents/coder.md (MCP page creation)
  ├─→ designer agent → .claude/agents/designer.md (design review)
  ├─→ tester agent → .claude/agents/tester.md (Playwright screenshots)
  └─→ stuck agent → .claude/agents/stuck.md (Brave Search + R.JINA research)
```

### Key Directories:
```
C:\Users\denit\Local Sites\svetlinkielementor\
├── config.json (WordPress credentials, page IDs, Global Colors)
├── .mcp.json (wp-elementor-mcp + brave-search servers)
├── SSOT/ (Golden Triangle + archive/)
├── .claude/ (CLAUDE.md + agents/)
├── scripts/
│   ├── working/ (5 production scripts)
│   ├── templates/ (2 JSON templates)
│   └── deprecated/ (old scripts archived)
├── backups/ (3 backups: homepage, header, footer)
└── OPTIMIZATION-MASTER-PLAN.md (full optimization plan)
```

---

## 🚀 What's Completed (Phases 1-3, 5)

### ✅ Phase 1: Archive Everything (DONE - commit 94e6c61)
- 25 files + 4 folders archived (ZERO deletions)
- Session logs → SSOT/archive/sessions/
- Reference docs → SSOT/archive/reference/
- Deprecated scripts → scripts/deprecated/
- Screenshots → screenshots/archive/

### ✅ Phase 2: Golden Triangle (DONE - commit f7399e1)
- Created STATIC_RULES.md (3504 lines, merged 4 files)
- Created ACTIVE_STATE.md (current state only)
- Renamed ISSUES-AND-SOLUTIONS → TROUBLESHOOTING.md
- Updated SSOT/README.md
- 85% context reduction achieved

### ✅ Phase 3: Agent Compression (DONE - commit 0fa1cf6)
- CLAUDE.md: 485 → 302 lines (38% reduction)
- coder.md: 853 → 331 lines (61% reduction)
- designer.md: 576 → 290 lines (49.6% reduction)
- stuck.md: 641 → 449 lines (29.9% reduction)
- tester.md: 197 → 240 lines (standardized)
- **Total: 2752 → 1612 lines (41.4% reduction)**

### ✅ Phase 5: Script Organization (DONE - commit 0fa1cf6)
- Created scripts/working/ (5 scripts)
- Created scripts/templates/ (2 JSON templates)
- Created scripts/README.md
- All working scripts organized

### ⏳ Phase 4: Config Centralization (50% DONE)
- ✅ config.json created
- ✅ config.json in .gitignore
- ❌ config.example.json missing (needs template)
- ❌ API.txt still exists (should be deleted)

---

## 📊 Current System State

**WordPress**:
- Site: http://svetlinkielementor.local
- Auth: test / S27q64rqoFhfTPDA30nBhNM5
- Elementor: FREE version (not Pro)

**Pages**:
- Homepage: Page ID 21 (6 sections complete)
- Header Template: ID 69 (empty, awaiting import)
- Footer Template: ID 73 (empty, awaiting import)

**Global Colors** (CSS variables):
- Primary: #FABA29 (Yellow/Gold)
- Secondary: #4F9F8B (Teal/Green)
- Accent: #FEFCF5 (Warm Cream)
- Text: #2C2C2C (Dark Gray)

**Critical Settings**:
- CSS Print Method: Internal Embedding ✓
- Global Colors Polyfill: Active (PHP polyfill in theme) ✓
- Stretch Sections: Working (1920px edge-to-edge) ✓

**5 Known Issues** (see TROUBLESHOOTING.md):
1. Global Colors not showing → SOLVED (polyfill)
2. Stretch section 645px → SOLVED (Internal Embedding)
3. REST API updates don't apply → WORKAROUND (click "Update" in editor)
4. Containers don't work → EXPECTED (use Legacy Sections in FREE)
5. Header/Footer not REST accessible → LIMITATION (manual import)

---

## 🔧 MCP Servers Configured

1. **wp-elementor-mcp** (32 tools, standard mode):
   - WordPress page management
   - Elementor structure creation
   - Global Colors/Fonts
   - Media uploads

2. **brave-search** (web search):
   - For stuck agent research
   - Two-step: Brave finds URLs → R.JINA extracts content

**Research Protocol** (Stuck Agent):
- Tier 1 sources: developers.elementor.com, developer.wordpress.org, github.com, stackoverflow.com
- Tier 2 sources: wordpress.org/support, kinsta.com/blog, css-tricks.com, reddit.com/r/elementor
- Forbidden: medium.com, SEO blogs, w3schools, YouTube

---

## 🎯 Next Immediate Actions

1. **Finish Phase 4** (5 minutes):
   - Create config.example.json
   - Delete API.txt
   - Git commit

2. **Test System** (after restart):
   - Verify Brave Search MCP loaded
   - Test agent delegation (call coder agent)
   - Verify Golden Triangle file access

3. **Import Header/Footer**:
   - Use scripts/templates/header-template.json
   - Use scripts/templates/footer-template.json
   - Manual import via Elementor editor (REST API not accessible)

---

## 🚨 Critical Safety Rules

### Pre-Flight Snapshot (MANDATORY):
**Before EVERY page update:**
```bash
python scripts/working/backup-before-update.py --page-id 21 --task "description"
```

**If update fails:**
```bash
python scripts/working/restore-from-backup.py --page-id 21 --latest
```

**Why**: Prevents white screen disasters. 10-second rollback vs hours to rebuild.

### No Fallback Principle (All Agents):
1. ❌ DO NOT guess solutions
2. ❌ DO NOT create silent workarounds
3. ✅ RESEARCH proper solutions (Brave + R.JINA)
4. ✅ ESCALATE to human if uncertain

---

## 📚 Quick Navigation

**Need current page IDs?** → Read SSOT/ACTIVE_STATE.md

**Need widget list?** → Read SSOT/STATIC_RULES.md#widget-whitelist

**Need JSON structure?** → Read SSOT/STATIC_RULES.md#json-schema

**Encountering error?** → Read SSOT/TROUBLESHOOTING.md

**Full optimization plan?** → Read OPTIMIZATION-MASTER-PLAN.md

**Script documentation?** → Read scripts/README.md

**Backup workflow?** → Read backups/README.md

---

## 💾 Git Status

**Branch**: master
**Remote**: https://github.com/FlyingSD/elementor-workflow.git
**Last Commit**: 0fa1cf6 - Phase 3 & 5 complete
**All changes**: Committed and pushed ✓

---

## ✅ You're Ready!

Claude Code is now optimized and ready for:
- AI-automated page building via MCP
- Multi-agent delegation (coder, designer, tester, stuck)
- Research via Brave Search + R.JINA
- Safe updates with Pre-Flight Snapshots

**Start working** by reading SSOT/ACTIVE_STATE.md for current state!

---

**File**: QUICK-RESTORE.md
**Purpose**: Fast context restore after /clear or restart
**Usage**: Copy and paste entire file to Claude Code
**Last Updated**: 2025-11-29
