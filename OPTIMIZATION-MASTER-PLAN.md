# Optimization Master Plan - Complete Discussion Archive

**Date**: 2025-11-29
**Session**: Pre-optimization planning
**Status**: Ready for implementation after user approval

---

## 🎯 ЦЯЛОСТНА ЦЕЛ

Преход от "Heavyweight" към "Modular" архитектура:
- ✅ Запазване на ЦЯЛАТА информация
- ✅ 85% context reduction (166 KB → 25 KB initial load)
- ✅ Активиране на правилен multi-agent workflow
- ✅ "Just-in-time" четене на документация

---

## 📊 ТЕКУЩО СЪСТОЯНИЕ (Before Optimization)

### Current Context Load: ~166 KB = ~40,000 tokens

```
Root Level:
├── 9 Python scripts (~80 KB)
│   ├── rebuild-all-6-sections.py ✅ WORKING
│   ├── rebuild-complete-homepage.py ✅ WORKING
│   ├── build-header-footer.py ❌ Failed (REST API)
│   ├── update-header-footer-db.py ❌ Failed (MySQL)
│   ├── build-all-sections.py ⚠️ DANGEROUS (overwrites)
│   └── 4x deprecated scripts 🗄️
├── 8 Documentation files (~120 KB)
├── 2 Templates (header/footer JSON)
└── API.txt (credentials)

.claude/ (132 KB):
├── CLAUDE.md (16 KB, 485 реда) ⚠️ TOO LONG
└── agents/
    ├── orchestrator.md (25 KB)
    ├── coder.md (30 KB)
    ├── designer.md (19 KB)
    ├── stuck.md (23 KB)
    └── tester.md (6 KB)

SSOT/ (352 KB) - 19 FILES:
├── Static Rules (4 files, 90 KB):
│   ├── ELEMENTOR-CORE-PRINCIPLES.md (24 KB)
│   ├── JSON-GENERATION-TOOLS-GUIDE.md (24 KB)
│   ├── ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md (25 KB)
│   └── MCP-PAGE-CREATION-CHECKLIST.md (19 KB)
├── State Tracking (2 files, 26 KB):
│   ├── 01-CURRENT-STATE.md (12 KB)
│   └── 02-PROGRESS-TRACKER.md (14 KB)
├── Troubleshooting (1 file, 21 KB):
│   └── ISSUES-AND-SOLUTIONS-GUIDE.md
├── Reference (4 files, 55 KB):
│   ├── ELEMENTOR-DEVELOPER-RESOURCES.md (15 KB)
│   ├── ELEMENTOR-FREE-COLOR-FIX-SOLUTION.md (11 KB)
│   ├── ELEMENTOR-REST-API-REFERENCE.md (15 KB)
│   └── EXISTING-PAGES-ANALYSIS.md (14 KB)
├── Session Logs (5 files, 85 KB):
│   ├── SESSION-2025-11-29-RECOVERY.md
│   ├── SESSION-FINAL-2025-11-29.md
│   ├── SESSION-SUMMARY-2025-11-28-EVENING.md
│   ├── SESSION-SUMMARY-2025-11-28.md
│   └── SESSION-SUMMARY-2025-11-29-COLOR-FIX.md
└── Meta (3 files):
    ├── README.md
    ├── 00-CONTEXT-RESTORE-PROMPT.md
    └── 03-DOCUMENTATION-RULES.md

Screenshots: ~10 MB (50+ files)
├── 2025-11-26-current-state/ (4.5 MB)
├── comparison/ (3.7 MB)
└── user-feedback/ (840 KB)

Backups: 42 KB (protected ✓)
```

---

## 🎯 TARGET СЪСТОЯНИЕ (After Optimization)

### New Context Load: ~7-25 KB = ~2,000-6,000 tokens
### SAVINGS: 85% context reduction

```
Root Level (cleaned):
├── config.json (NEW - centralized config)
├── scripts/
│   ├── working/
│   │   ├── rebuild-homepage.py
│   │   └── config-loader.py
│   ├── templates/
│   │   ├── header-template.json
│   │   └── footer-template.json
│   └── deprecated/ (archived, not deleted)
└── README-NEXT-STEPS.md (current)

.claude/ (41 KB - 66% reduction):
├── CLAUDE.md (5 KB, 150 реда) ✅ COMPRESSED
└── agents/ (all with "Reference Files" sections)
    ├── orchestrator.md (10 KB)
    ├── coder.md (8 KB)
    ├── designer.md (6 KB)
    ├── stuck.md (8 KB)
    └── tester.md (4 KB)

SSOT/ (Golden Triangle - 3 ACTIVE files):
├── STATIC_RULES.md (~90 KB)
│   ├── Section 1: Widget Whitelist
│   ├── Section 2: JSON Schema
│   ├── Section 3: Global Colors
│   ├── Section 4: Section Structure
│   ├── Section 5: MCP Checklist
│   └── [Read by section on demand]
├── ACTIVE_STATE.md (~15 KB)
│   ├── Current Setup (pages/IDs)
│   ├── Configuration (URLs/auth)
│   ├── Next Action
│   └── [Rewritten after each task]
├── TROUBLESHOOTING.md (21 KB)
│   └── [Read only when stuck]
├── README.md (updated navigation)
└── archive/
    ├── reference/
    │   ├── ELEMENTOR-DEVELOPER-RESOURCES.md
    │   ├── ELEMENTOR-FREE-COLOR-FIX-SOLUTION.md
    │   ├── ELEMENTOR-REST-API-REFERENCE.md
    │   └── EXISTING-PAGES-ANALYSIS.md
    ├── sessions/
    │   └── [All SESSION-*.md files]
    ├── deprecated-scripts/
    │   └── [Non-working scripts]
    └── deprecated-docs/
        └── [Old root documentation]

Screenshots/
└── archive/
    ├── 2025-11-26-current-state/
    ├── comparison/
    └── user-feedback/

Backups/ (unchanged, protected)
```

---

## 🔍 КЛЮЧОВИ ОТКРИТИЯ

### 1. Agent Architecture Misunderstanding (RESOLVED!)

**Грешно разбиране** (преди):
```
User → Claude (with all info loaded)
```

**Правилно разбиране** (сега):
```
User → Claude (CLAUDE.md - coordinator only)
    ↓ Task tool
    Orchestrator Agent (orchestrator.md - routes)
    ↓ Task tool
    ├─→ Coder (coder.md - writes code)
    ├─→ Tester (tester.md - tests)
    ├─→ Designer (designer.md - design)
    └─→ Stuck (stuck.md - research)
```

**Impact**:
- Agents НЕ се използват в момента
- Claude main прави всичко директно
- Context се пълни ненужно
- Multi-agent architecture съществува но не е активна

**Solution**:
- Compress CLAUDE.md с ясни "Delegate to agents" инструкции
- Update agents с "Reference Files" sections
- Test proper delegation flow

### 2. Duplicate Information (MAJOR ISSUE)

**Дублирани концепции**:
- Widget whitelist: в 3 места (ELEMENTOR-CORE-PRINCIPLES, coder.md, JSON-GENERATION)
- JSON structure: в 3 места
- Global Colors: в 4 места
- Current state: в 2 места (CURRENT-STATE, PROGRESS-TRACKER)

**Solution**: Single Source of Truth (SSOT) pattern
- Static info → STATIC_RULES.md (merged from 4 files)
- Dynamic info → ACTIVE_STATE.md (merged from 2 files)
- Agents → Reference these files, don't duplicate

### 3. Context Loading Pattern (INEFFICIENT)

**Current** (inefficient):
```python
# Every session start:
- Load CLAUDE.md (16 KB)
- Load ELEMENTOR-CORE-PRINCIPLES (24 KB)
- Load JSON-GENERATION-TOOLS (24 KB)
- Load CURRENT-STATE (12 KB)
- Load ISSUES-AND-SOLUTIONS (21 KB)
Total: 97 KB loaded ALWAYS

# When writing code:
- Already loaded everything above
- Plus: coder.md (30 KB)
Total: 127 KB
```

**Optimized** (efficient):
```python
# Session start:
- Load CLAUDE.md (5 KB) ✅
Total: 5 KB

# When writing code:
- Invoke orchestrator (10 KB) ✅
  - Invoke coder (8 KB) ✅
    - Read ACTIVE_STATE.md (2 KB) ✅
    - Read STATIC_RULES.md#widgets (5 KB only) ✅
    Total: 30 KB (52% savings)
```

---

## 📋 THE GOLDEN TRIANGLE

Само 3 файла се поддържат активно:

### 1. STATIC_RULES.md (~90 KB, sectioned)

**Purpose**: "The Constitution" - never changes

**Content** (merged from 4 files):
```markdown
# Static Rules - Elementor Automation

## Navigation
1. [Widget Whitelist](#widget-whitelist) - 29 FREE widgets
2. [JSON Schema](#json-schema) - Structure reference
3. [Global Colors](#global-colors) - CSS variables
4. [Section Structure](#section-structure) - Section > Column > Widget
5. [MCP Checklist](#mcp-checklist) - Page creation workflow

---

## 1. Widget Whitelist
[Content from ELEMENTOR-CORE-PRINCIPLES.md]

## 2. JSON Schema
[Content from JSON-GENERATION-TOOLS-GUIDE.md + ELEMENTOR-DATA-SCHEMA]

## 3. Global Colors
[Content from ELEMENTOR-CORE-PRINCIPLES.md]

## 4. Section Structure
[Content from ELEMENTOR-CORE-PRINCIPLES.md]

## 5. MCP Checklist
[Content from MCP-PAGE-CREATION-CHECKLIST.md]
```

**Reading Pattern**:
- Agents read ONLY needed section
- Example: `READ STATIC_RULES.md#widget-whitelist` → 5 KB, not 90 KB

**Update Frequency**: Rare (only when Elementor updates)

---

### 2. ACTIVE_STATE.md (~15 KB)

**Purpose**: "The Pulse" - current state ONLY

**Content** (merged from 2 files):
```markdown
# Active State

## Current Setup
✅ Homepage: Page ID 21 (6 sections complete)
⚠️ Header: Template ID 69 (empty, awaiting import)
⚠️ Footer: Template ID 73 (empty, awaiting import)

## Configuration
- Base URL: http://svetlinkielementor.local
- Auth User: test
- Auth Pass: S27q64rqoFhfTPDA30nBhNM5

## Page IDs
| Page | ID | Status |
|------|----|----|
| Homepage | 21 | 6 sections ✓ |
| Header Template | 69 | Empty |
| Footer Template | 73 | Empty |

## Global Colors (Active)
| Name | Hex | CSS Variable |
|------|-----|--------------|
| Primary | #FABA29 | var(--e-global-color-primary) |
| Secondary | #4F9F8B | var(--e-global-color-secondary) |
| Accent | #FEFCF5 | var(--e-global-color-accent) |
| Text | #2C2C2C | var(--e-global-color-text) |

## Elementor Settings
✅ CSS Print Method: Internal Embedding
✅ Global Colors Polyfill: Active (twentytwentyfive theme)
✅ Header Footer Elementor: Installed

## Next Action
Import header-template.json and footer-template.json manually via Elementor editor

## Last Updated
2025-11-29 after Session 2 recovery
```

**Reading Pattern**:
- Read entire file (small, ~15 KB)
- Always current

**Update Frequency**: After every completed task

---

### 3. TROUBLESHOOTING.md (21 KB)

**Purpose**: "The Repair Manual" - read ONLY when stuck

**Content** (renamed from ISSUES-AND-SOLUTIONS-GUIDE.md):
```markdown
# Troubleshooting Guide

## Quick Reference Table
[5 known issues with symptoms → solutions]

## Issue #1: Global Colors Not Showing
[Full details]

## Issue #2: Stretch Section Not Working
[Full details]

## Issue #3: REST API Updates Not Applying
[Full details]

## Issue #4: Flexbox Containers Don't Work
[Full details]

## Issue #5: Header Footer Templates Not REST Accessible
[Full details]
```

**Reading Pattern**:
- Read ONLY when error occurs
- Search for specific issue

**Update Frequency**: When new issue discovered

---

## 🚀 IMPLEMENTATION PLAN

### Phase 1: Reference Files + Archive (30 minutes, LOW RISK)

#### Step 1.1: Add "Reference Files" to ALL agents
```markdown
# Add to end of each agent .md:

---

## Reference Files (Read On Demand)

**Current State**:
- READ SSOT/ACTIVE_STATE.md for:
  * Current page IDs (21, 69, 73)
  * Auth credentials (test / password)
  * Base URL (http://svetlinkielementor.local)
  * Global Colors (Primary, Secondary, Accent, Text)
  * Next action

**Static Rules**:
- READ SSOT/STATIC_RULES.md sections:
  * #widget-whitelist - 29 FREE widgets
  * #json-schema - JSON structure & examples
  * #global-colors - CSS variable system
  * #section-structure - Section > Column > Widget
  * #mcp-checklist - Page creation workflow

**Troubleshooting**:
- READ SSOT/TROUBLESHOOTING.md when stuck
- Search for error message or symptom

**DO NOT** load entire files. Read only needed sections.
```

**Files to update**:
- .claude/CLAUDE.md
- .claude/agents/orchestrator.md
- .claude/agents/coder.md
- .claude/agents/designer.md
- .claude/agents/stuck.md
- .claude/agents/tester.md

**Git commit**: "Phase 1.1: Add Reference Files sections to all agents"

---

#### Step 1.2: Create archive structure
```bash
mkdir -p SSOT/archive/reference
mkdir -p SSOT/archive/sessions
mkdir -p SSOT/archive/deprecated-docs
mkdir -p scripts/deprecated
mkdir -p screenshots/archive
```

**Git commit**: "Phase 1.2: Create archive directory structure"

---

#### Step 1.3: Move session logs to archive
```bash
mv SSOT/SESSION-*.md SSOT/archive/sessions/
```

**Files moved**:
- SESSION-2025-11-29-RECOVERY.md
- SESSION-FINAL-2025-11-29.md
- SESSION-SUMMARY-2025-11-28-EVENING.md
- SESSION-SUMMARY-2025-11-28.md
- SESSION-SUMMARY-2025-11-29-COLOR-FIX.md

**Git commit**: "Phase 1.3: Archive session logs (5 files)"

---

#### Step 1.4: Move reference docs to archive
```bash
mv SSOT/ELEMENTOR-DEVELOPER-RESOURCES.md SSOT/archive/reference/
mv SSOT/ELEMENTOR-FREE-COLOR-FIX-SOLUTION.md SSOT/archive/reference/
mv SSOT/ELEMENTOR-REST-API-REFERENCE.md SSOT/archive/reference/
mv SSOT/EXISTING-PAGES-ANALYSIS.md SSOT/archive/reference/
```

**Git commit**: "Phase 1.4: Archive reference documentation (4 files)"

---

#### Step 1.5: Move deprecated scripts
```bash
mkdir -p scripts/deprecated
mv build_hero_container.py scripts/deprecated/
mv export_hero_structure.py scripts/deprecated/
mv verify_hero_structure.py scripts/deprecated/
mv build-section-2-benefits.py scripts/deprecated/
mv build-header-footer.py scripts/deprecated/ # Failed - REST API
mv update-header-footer-db.py scripts/deprecated/ # Failed - MySQL

# DANGEROUS script - explicit warning
mkdir -p scripts/deprecated/DANGEROUS
mv build-all-sections.py scripts/deprecated/DANGEROUS/
echo "⚠️ DO NOT USE - Overwrites existing sections" > scripts/deprecated/DANGEROUS/README.md
```

**Git commit**: "Phase 1.5: Archive deprecated scripts (7 files, 1 DANGEROUS)"

---

#### Step 1.6: Move old root documentation
```bash
mkdir -p SSOT/archive/deprecated-docs
mv DESIGNER-BLOG-ANALYSIS.md SSOT/archive/deprecated-docs/
mv svetlinkelementor-rebuild-guide.md SSOT/archive/deprecated-docs/
mv ELEMENTOR-GLOBAL-COLORS-SETUP.md SSOT/archive/deprecated-docs/ # Duplicate
mv RESTORE-CONTEXT-PROMPT.md SSOT/archive/deprecated-docs/
mv HERO_CONTAINER_REPORT.md SSOT/archive/deprecated-docs/
mv HERO_VISUAL_STRUCTURE.txt SSOT/archive/deprecated-docs/
mv QUICK-RESTORE-COMMAND.txt SSOT/archive/deprecated-docs/
mv elementor-mcp-solution.md SSOT/archive/deprecated-docs/
mv hero_container_structure.json SSOT/archive/deprecated-docs/
```

**Git commit**: "Phase 1.6: Archive old root documentation (9 files)"

---

#### Step 1.7: Archive screenshots
```bash
mkdir -p screenshots/archive
mv 2025-11-26-current-state screenshots/archive/
mv 2025-11-26-comparison screenshots/archive/
mv comparison screenshots/archive/
mv user-feedback screenshots/archive/
```

**Git commit**: "Phase 1.7: Archive screenshots (~10 MB, 4 folders)"

---

#### Step 1.8: Test that archives are accessible
```bash
# Verify files exist
ls SSOT/archive/reference/
ls SSOT/archive/sessions/
ls scripts/deprecated/
ls screenshots/archive/

# Test read access
cat SSOT/archive/reference/ELEMENTOR-DEVELOPER-RESOURCES.md | head -20
```

**Git commit**: "Phase 1.8: Verify archive accessibility"

---

**Phase 1 Complete**: ~30 minutes, archive done, nothing deleted

---

### Phase 2: Create Golden Triangle Files (45 minutes, MEDIUM RISK)

#### Step 2.1: Create STATIC_RULES.md
```bash
# Merge 4 files into one
cat > SSOT/STATIC_RULES.md << 'EOF'
# Static Rules - Elementor Automation

**Purpose**: The Constitution - rules that never change
**Read Pattern**: By section on demand (#widget-whitelist, #json-schema, etc.)
**Update Frequency**: Rare (only when Elementor updates)

---

## Table of Contents
1. [Widget Whitelist](#widget-whitelist) - 29 FREE widgets
2. [JSON Schema](#json-schema) - Structure & examples
3. [Global Colors](#global-colors) - CSS variables
4. [Section Structure](#section-structure) - Section > Column > Widget
5. [Widget Properties](#widget-properties) - Property names
6. [MCP Checklist](#mcp-checklist) - Page creation workflow

---

[Content merged from:]
- ELEMENTOR-CORE-PRINCIPLES.md (Sections 1, 3, 4)
- JSON-GENERATION-TOOLS-GUIDE.md (Section 2)
- ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md (Section 2 details)
- MCP-PAGE-CREATION-CHECKLIST.md (Section 6)
EOF
```

**Manual work required**: Copy/paste content with proper headers

**Git commit**: "Phase 2.1: Create STATIC_RULES.md (merged from 4 files)"

---

#### Step 2.2: Create ACTIVE_STATE.md
```markdown
# Active State

[Content from 01-CURRENT-STATE.md + 02-PROGRESS-TRACKER.md]
[Keep ONLY current information, remove history]
```

**Git commit**: "Phase 2.2: Create ACTIVE_STATE.md (current state only)"

---

#### Step 2.3: Rename ISSUES-AND-SOLUTIONS-GUIDE.md
```bash
mv SSOT/ISSUES-AND-SOLUTIONS-GUIDE.md SSOT/TROUBLESHOOTING.md
```

**Git commit**: "Phase 2.3: Rename to TROUBLESHOOTING.md"

---

#### Step 2.4: Update SSOT/README.md
```markdown
# SSOT - Single Source of Truth

## Active Files (Read These)
- **STATIC_RULES.md** - Rules that never change (read by section)
- **ACTIVE_STATE.md** - Current state (read entire file)
- **TROUBLESHOOTING.md** - Error solutions (read when stuck)

## Archive (Reference When Needed)
- **archive/reference/** - Elementor docs, API guides
- **archive/sessions/** - Session history logs
- **archive/deprecated-docs/** - Old documentation

## Navigation Quick Reference
- Current page IDs → ACTIVE_STATE.md
- Widget list → STATIC_RULES.md#widget-whitelist
- JSON structure → STATIC_RULES.md#json-schema
- Error solutions → TROUBLESHOOTING.md
```

**Git commit**: "Phase 2.4: Update SSOT/README.md with new structure"

---

#### Step 2.5: Archive old state files
```bash
mv SSOT/01-CURRENT-STATE.md SSOT/archive/deprecated-docs/
mv SSOT/02-PROGRESS-TRACKER.md SSOT/archive/deprecated-docs/
mv SSOT/ELEMENTOR-CORE-PRINCIPLES.md SSOT/archive/deprecated-docs/
mv SSOT/JSON-GENERATION-TOOLS-GUIDE.md SSOT/archive/deprecated-docs/
mv SSOT/ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md SSOT/archive/deprecated-docs/
mv SSOT/MCP-PAGE-CREATION-CHECKLIST.md SSOT/archive/deprecated-docs/
```

**Git commit**: "Phase 2.5: Archive source files (merged into STATIC_RULES/ACTIVE_STATE)"

---

**Phase 2 Complete**: Golden Triangle created, old files archived

---

### Phase 3: Compress Agents (30 minutes, MEDIUM RISK)

#### Step 3.1: Compress CLAUDE.md
```markdown
# Claude Code - Elementor AI Automation System

**Version**: 6.0 (Optimized)
**Your Role**: Main Orchestrator (Coordinator ONLY)
**Context**: 200k token window

---

## 🎯 Your Role

You are the MAIN ORCHESTRATOR.

**Your job**:
- Receive user requests
- Track overall progress (TodoWrite)
- **Delegate to orchestrator agent** (via Task tool)
- Report results to user

**NOT your job**:
- ❌ Don't write Python code yourself
- ❌ Don't debug code yourself
- ❌ Don't research docs yourself
- ❌ Don't test with Playwright yourself

**Rule**: Let agents do specialized work. You coordinate.

---

## 📋 Workflow

1. **User Request** → Read SSOT/ACTIVE_STATE.md (current state)
2. **TodoWrite** → Create task list if multi-step
3. **Task Tool** → Invoke orchestrator agent with instructions
4. **Orchestrator** → Routes to specialist (coder/tester/designer/stuck)
5. **Result** → Report back to user, update ACTIVE_STATE.md

---

## 🔧 Known Issues (Quick Reference)

Read SSOT/TROUBLESHOOTING.md for full details.

1. **Issue #1**: Global Colors not showing → Polyfill active
2. **Issue #2**: Stretch section not full-width → Internal Embedding
3. **Issue #3**: REST API updates don't apply → Click "Update" in editor
4. **Issue #4**: Containers don't work → Use Legacy Sections
5. **Issue #5**: elementor-hf not REST accessible → Manual import

---

## 📚 Reference Files

ALL detailed information is in SSOT/:

- **Current state** → SSOT/ACTIVE_STATE.md
- **Static rules** → SSOT/STATIC_RULES.md (by section)
- **Troubleshooting** → SSOT/TROUBLESHOOTING.md

**DO NOT** load entire files. Point agents to specific sections.

---

## 🎓 Agent Delegation Rules

When user wants:
- **Code written** → Invoke orchestrator → "User needs Python script for..."
- **Bug fixed** → Invoke orchestrator → "User reports error..."
- **Design decision** → Invoke orchestrator → "User wants design advice..."
- **Research** → Invoke orchestrator → "User needs info about..."

Orchestrator will route to: coder/tester/designer/stuck

---

**Location**: `.claude/CLAUDE.md`
**Last Updated**: 2025-11-29 (Optimization Phase 3)
```

**Lines**: 485 → 150 (70% reduction)

**Git commit**: "Phase 3.1: Compress CLAUDE.md (485 → 150 lines)"

---

#### Step 3.2-3.6: Compress agent files

Similar compression for:
- orchestrator.md (25 KB → 10 KB)
- coder.md (30 KB → 8 KB)
- designer.md (19 KB → 6 KB)
- stuck.md (23 KB → 8 KB)
- tester.md (6 KB → 4 KB)

**Pattern**: Keep role/principles, remove duplicated content, point to SSOT

**Git commits**: One per agent

---

**Phase 3 Complete**: All agents compressed

---

### Phase 4: Create config.json (15 minutes, LOW RISK)

#### Step 4.1: Create config.json
```json
{
  "wordpress": {
    "base_url": "http://svetlinkielementor.local",
    "auth": {
      "user": "test",
      "password": "S27q64rqoFhfTPDA30nBhNM5"
    }
  },
  "elementor": {
    "pages": {
      "homepage": 21,
      "header_template": 69,
      "footer_template": 73
    },
    "settings": {
      "css_print_method": "internal",
      "global_colors_polyfill": true
    }
  },
  "global_colors": {
    "primary": {"hex": "#FABA29", "css_var": "var(--e-global-color-primary)"},
    "secondary": {"hex": "#4F9F8B", "css_var": "var(--e-global-color-secondary)"},
    "accent": {"hex": "#FEFCF5", "css_var": "var(--e-global-color-accent)"},
    "text": {"hex": "#2C2C2C", "css_var": "var(--e-global-color-text)"}
  }
}
```

**Git commit**: "Phase 4.1: Create config.json (centralized configuration)"

---

#### Step 4.2: Update .gitignore
```
# Add to .gitignore:
config.json
```

**Git commit**: "Phase 4.2: Add config.json to .gitignore (sensitive)"

---

#### Step 4.3: Create config.example.json
```json
{
  "wordpress": {
    "base_url": "http://your-site.local",
    "auth": {
      "user": "your-username",
      "password": "your-app-password"
    }
  },
  ...
}
```

**Git commit**: "Phase 4.3: Add config.example.json (template)"

---

#### Step 4.4: Delete API.txt
```bash
rm API.txt
```

**Git commit**: "Phase 4.4: Remove API.txt (migrated to config.json)"

---

**Phase 4 Complete**: Configuration centralized

---

### Phase 5: Organize Working Scripts (15 minutes, LOW RISK)

#### Step 5.1: Create scripts structure
```bash
mkdir -p scripts/working
mkdir -p scripts/templates
```

#### Step 5.2: Move working scripts
```bash
mv rebuild-all-6-sections.py scripts/working/rebuild-homepage.py
mv rebuild-complete-homepage.py scripts/working/rebuild-homepage-alt.py
```

#### Step 5.3: Move templates
```bash
mv header-template.json scripts/templates/
mv footer-template.json scripts/templates/
```

#### Step 5.4: Create scripts/README.md
```markdown
# Scripts Directory

## working/
Production-ready scripts that work.

- **rebuild-homepage.py** - Main homepage rebuild (all 6 sections)
- **rebuild-homepage-alt.py** - Alternative rebuild approach

## templates/
JSON templates ready for import.

- **header-template.json** - Header content (site name + CTA)
- **footer-template.json** - Footer content (copyright + contact)

## deprecated/
Old/non-working scripts. DO NOT USE without review.

## Usage
```bash
# Rebuild homepage
python scripts/working/rebuild-homepage.py

# Import templates
# Use Elementor editor UI (REST API not available for elementor-hf)
```
```

**Git commits**:
- "Phase 5.1-5.3: Organize scripts into working/templates/deprecated"
- "Phase 5.4: Add scripts/README.md"

---

**Phase 5 Complete**: Scripts organized

---

## ✅ VERIFICATION CHECKLIST

After all phases complete:

### Context Reduction Test
```python
# Before:
Initial load: CLAUDE.md (16 KB) + agents (123 KB) + SSOT (352 KB)
= ~500 KB total context available

# After:
Initial load: CLAUDE.md (5 KB)
On demand: orchestrator (10 KB) + coder (8 KB) + ACTIVE_STATE (2 KB) + STATIC_RULES section (5 KB)
= ~30 KB total context loaded

Savings: 94% reduction!
```

### File Access Test
```bash
# Can we still access archived files?
cat SSOT/archive/sessions/SESSION-2025-11-29-RECOVERY.md
cat SSOT/archive/reference/ELEMENTOR-DEVELOPER-RESOURCES.md
cat scripts/deprecated/build_hero_container.py

# All should work ✓
```

### Agent Delegation Test
```
User: "Build a simple section with one heading widget"
└─→ Claude reads CLAUDE.md (5 KB)
    └─→ Invokes orchestrator via Task tool
        └─→ Orchestrator reads orchestrator.md (10 KB)
            └─→ Invokes coder via Task tool
                └─→ Coder reads coder.md (8 KB)
                └─→ Coder reads ACTIVE_STATE.md (2 KB)
                └─→ Coder reads STATIC_RULES.md#json-schema (5 KB)
                └─→ Coder writes script
                └─→ Returns to orchestrator
        └─→ Orchestrator returns to Claude
    └─→ Claude reports to user

Total context: 30 KB (vs 127 KB before)
Savings: 76%
```

### Information Preservation Test
```bash
# Can we still find everything?

# Widget list
grep "heading" SSOT/STATIC_RULES.md  # Should find widget

# Color fix solution
cat SSOT/archive/reference/ELEMENTOR-FREE-COLOR-FIX-SOLUTION.md  # Should exist

# Session history
ls SSOT/archive/sessions/  # Should list all 5 sessions

# Old scripts
ls scripts/deprecated/  # Should list 7 files

# All info preserved ✓
```

---

## 🚨 ROLLBACK PLAN

If something breaks:

### Full Rollback (Nuclear Option)
```bash
git reset --hard 91d21ed  # Backup commit before optimization
git push -f origin master  # Force push (ONLY if solo developer)
```

### Partial Rollback (Phase-by-Phase)
```bash
# Rollback Phase 5 only
git revert <phase-5-commit-hash>

# Rollback Phase 4 only
git revert <phase-4-commit-hash>

# etc.
```

### Manual File Restore
```bash
# Restore specific file from backup commit
git checkout 91d21ed -- path/to/file.md
```

---

## 📊 METRICS TO TRACK

After optimization, measure:

1. **Context Load**:
   - Before: ~166 KB initial load
   - After: ~7 KB initial load
   - Target: 85%+ reduction ✓

2. **Agent Usage**:
   - Before: 0 Task tool calls per session
   - After: Should see Task tool calls to orchestrator
   - Target: Proper delegation ✓

3. **File Count** (SSOT active):
   - Before: 19 files
   - After: 3 files (+ archive)
   - Target: Golden Triangle ✓

4. **Performance**:
   - Session start time (measure with timestamps)
   - Time to first meaningful response
   - Compact frequency (should be less)

5. **Information Accessibility**:
   - Can agents find widget list? ✓
   - Can we access session history? ✓
   - Can we restore old scripts? ✓

---

## 🎯 SUCCESS CRITERIA

Optimization is successful if:

1. ✅ Context reduction ≥ 80%
2. ✅ ALL information still accessible (nothing lost)
3. ✅ Agent delegation works (orchestrator → specialists)
4. ✅ Agents can find references (READ commands work)
5. ✅ Build tasks complete successfully
6. ✅ Can rollback if needed (git history intact)
7. ✅ User approves new structure

---

## 📋 USER APPROVAL NEEDED

Before starting implementation:

### Questions for User:

1. **Screenshots**: Archive all or keep latest?
   - Recommendation: Archive all (10 MB freed)

2. **Deprecated scripts**: Archive or delete?
   - Recommendation: Archive (keep for reference)
   - Exception: `build-all-sections.py` → Mark DANGEROUS

3. **Session logs**: Archive all?
   - Recommendation: Yes (history preserved but not in hot path)

4. **Phase order**: All at once or phase-by-phase with tests?
   - Recommendation: Phase-by-phase with git commits
   - Test after Phase 2 (Golden Triangle) before Phase 3 (Compress)

5. **Agent compression**: Aggressive (67% reduction) or conservative (30%)?
   - Recommendation: Aggressive (we can rollback if needed)

6. **MySQL MCP**: Try to set up during optimization?
   - Recommendation: Separate task (not part of file optimization)

7. **Docs MCP**: Try to set up during optimization?
   - Recommendation: Separate task (test Golden Triangle first)

---

## 🚀 READY TO START?

### Pre-Implementation Checklist:
- [x] Full backup in GitHub (commit 91d21ed, a666232) ✓
- [x] Complete inventory done (COMPLETE-INVENTORY.md) ✓
- [x] Optimization plan documented (this file) ✓
- [x] User understands multi-agent architecture ✓
- [x] User understands Golden Triangle concept ✓
- [ ] User approves plan
- [ ] User answers approval questions above
- [ ] Begin Phase 1

---

## 📞 POST-OPTIMIZATION TODO

After successful optimization:

1. **Test agent delegation** with simple task:
   - "Build a section with one heading widget"
   - Verify: Task tool used → orchestrator → coder
   - Verify: Context load stays low

2. **Test reference reading**:
   - Agent needs widget list
   - Verify: Reads STATIC_RULES.md#widget-whitelist
   - Verify: Doesn't load entire 90 KB file

3. **Update ACTIVE_STATE.md** after first task:
   - Verify: Easy to update
   - Verify: Stays slim (~15 KB max)

4. **Measure context savings**:
   - Check token usage before compact
   - Compare to pre-optimization sessions

5. **Document lessons learned**:
   - What worked well?
   - What needs adjustment?
   - Add to SSOT/archive/sessions/

---

**Created**: 2025-11-29
**Purpose**: Complete optimization discussion archive before compact
**Status**: Awaiting user approval to begin implementation
**Next Step**: User reviews and approves plan

**Git Backup**: All discussion captured in this file, committed before any changes

---

## 🎓 KEY LEARNINGS (For Future Reference)

### 1. Multi-Agent Architecture
- User → Claude (coordinator) → Orchestrator → Specialists
- NOT: User → Claude (does everything)

### 2. Context Management
- Load only what you need, when you need it
- Point to files, don't duplicate content
- Section-based reading (#anchor links)

### 3. SSOT Pattern
- One canonical source per concept
- Everything else points to it
- Update once, reflects everywhere

### 4. Archive vs Delete
- Archive everything (disk is cheap, knowledge is expensive)
- Clear folder structure (archive/reference, archive/sessions)
- Keep history accessible but out of hot path

### 5. Git as Safety Net
- Commit every phase
- Descriptive commit messages
- Easy rollback if needed

---

**END OF OPTIMIZATION MASTER PLAN**
