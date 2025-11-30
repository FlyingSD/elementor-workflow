# Elementor AI Automation System - Complete Architecture Guide

**Version**: 7.0 (Knowledge System Complete)
**Last Updated**: 2025-11-30
**Purpose**: Comprehensive documentation of how the entire multi-agent system works

---

## 📖 What is This System?

This is a **multi-agent AI automation system** for building WordPress pages with Elementor. Instead of manually clicking in the Elementor editor, we use:

1. **Claude Code** (Main Coordinator) - Receives requests, delegates to specialists
2. **Specialized Agents** - Each with deep expertise in specific domains
3. **MCP Servers** - Tools for WordPress/Elementor automation
4. **SSOT Files** - Single Source of Truth documentation
5. **Knowledge Guides** - Technical expertise codified in markdown files

**Goal**: Build professional, accessible WordPress pages automatically with AI agents that have deep technical knowledge.

---

## 🏗️ System Architecture Overview

### The Complete Stack

```
┌─────────────────────────────────────────────────────┐
│                    USER (Denis)                      │
└─────────────────┬───────────────────────────────────┘
                  │ Request
                  ↓
┌─────────────────────────────────────────────────────┐
│         CLAUDE CODE (Main Coordinator)               │
│  - Reads SSOT/ACTIVE_STATE.md                       │
│  - Creates TodoWrite task lists                      │
│  - Delegates via Task tool                           │
│  - Tracks progress, reports results                  │
└─────────────────┬───────────────────────────────────┘
                  │ Task Tool (2-Hop Delegation)
                  ↓
┌─────────────────────────────────────────────────────┐
│              SPECIALIZED AGENTS                      │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  elementor-expert (🆕 2025-11-30)          │    │
│  │  - Reads: ELEMENTOR-API-TECHNICAL-GUIDE    │    │
│  │  - Reads: ELEMENTOR-STRUCTURE-ALIGNMENT    │    │
│  │  - Expert: MCP, API, JSON structure        │    │
│  │  - Use for: Technical implementation       │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  design-expert (🆕 2025-11-30)             │    │
│  │  - Reads: CORE-WEBSITE-BUILDING-RULES      │    │
│  │  - Expert: UX/UI, WCAG, Typography         │    │
│  │  - Use for: Design decisions, standards    │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  coder (General Implementation)             │    │
│  │  - Reads: STATIC_RULES.md (sections)       │    │
│  │  - Creates: Pages via MCP                   │    │
│  │  - Use for: General page building           │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  tester (Visual QA)                         │    │
│  │  - Uses: Playwright MCP                     │    │
│  │  - Creates: Screenshots                     │    │
│  │  - Use for: Visual verification             │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  stuck (Research)                           │    │
│  │  - Uses: Brave Search + R.JINA              │    │
│  │  - Sources: GitHub, docs, Stack Overflow    │    │
│  │  - Use for: Problem solving                 │    │
│  └────────────────────────────────────────────┘    │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │  designer (Legacy - being replaced)         │    │
│  │  - Use design-expert instead                │    │
│  └────────────────────────────────────────────┘    │
└─────────────────┬───────────────────────────────────┘
                  │ Uses tools
                  ↓
┌─────────────────────────────────────────────────────┐
│                 MCP SERVERS                          │
│                                                      │
│  wp-elementor-mcp (32 tools)                        │
│  ├─ create_page, update_page, get_pages             │
│  ├─ get_elementor_elements, update_elementor_widget │
│  ├─ backup_elementor_data, clear_elementor_cache    │
│  └─ create_elementor_section, add_widget_to_section │
│                                                      │
│  json-schema-validator (5 tools)                    │
│  └─ validate_json_schema (prevent broken JSON)      │
│                                                      │
│  brave-search (2 tools)                             │
│  └─ brave_web_search, brave_local_search            │
│                                                      │
│  playwright (20+ tools)                             │
│  └─ browser_navigate, browser_snapshot              │
└─────────────────┬───────────────────────────────────┘
                  │ Manipulates
                  ↓
┌─────────────────────────────────────────────────────┐
│         WORDPRESS / ELEMENTOR                        │
│  - Site: http://svetlinkielementor.local            │
│  - Theme: Hello Elementor 3.4.5                     │
│  - Pages: 21 (Home), 23 (About), 25 (Programs)...  │
│  - REST API: /wp-json/wp/v2/posts                   │
└─────────────────────────────────────────────────────┘
```

---

## 🧠 Knowledge Management System

### The Knowledge Pyramid

```
┌────────────────────────────────────────────────┐
│         UNIVERSAL KNOWLEDGE (2000+ lines)      │
│                                                │
│  1. ELEMENTOR-API-TECHNICAL-GUIDE.md           │
│     (~450 lines)                               │
│     - Elementor architecture                   │
│     - Save flow & CSS generation               │
│     - REST API integration                     │
│     - Property naming conventions              │
│     - Group controls structure                 │
│     READ BY: elementor-expert agent            │
│                                                │
│  2. ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md │
│     (~500 lines)                               │
│     - Element hierarchy                        │
│     - Section/Column/Widget capabilities       │
│     - Card structure patterns                  │
│     - Spacing & alignment                      │
│     READ BY: elementor-expert agent            │
│                                                │
│  3. CORE-WEBSITE-BUILDING-RULES.md             │
│     (~1100 lines)                              │
│     - Nielsen's Usability Heuristics           │
│     - WCAG Accessibility (POUR)                │
│     - Typography & spacing systems             │
│     - Color contrast & layout grids            │
│     READ BY: design-expert agent               │
└────────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────────┐
│       PROJECT-SPECIFIC KNOWLEDGE               │
│                                                │
│  4. STATIC_RULES.md                            │
│     (~90 KB - read by section)                 │
│     - Widget whitelist (40-50 FREE widgets)    │
│     - JSON schema & structure                  │
│     - Global Colors system                     │
│     - Section structure rules                  │
│     - MCP workflow checklist                   │
│     READ BY: All agents (specific sections)    │
│                                                │
│  5. ACTIVE_STATE.md                            │
│     (~15 KB - read entire)                     │
│     - Current page IDs                         │
│     - WordPress credentials                    │
│     - Global Colors values                     │
│     - Next actions                             │
│     UPDATED: After each task completion        │
│     READ BY: Main Coordinator on every request │
│                                                │
│  6. TROUBLESHOOTING.md                         │
│     (21 KB - read when stuck)                  │
│     - 5 known issues + solutions               │
│     - Global Colors (SOLVED)                   │
│     - Stretch section (SOLVED)                 │
│     - REST API CSS issue (WORKAROUND)          │
│     - Containers in FREE (CORRECTED)           │
│     READ BY: stuck agent, escalated issues     │
└────────────────────────────────────────────────┘
```

### Knowledge Flow Rules

**Main Coordinator (Claude)**:
- ✅ ALWAYS reads `ACTIVE_STATE.md` at start of request
- ✅ Points agents to specific SSOT sections (never duplicates)
- ❌ NEVER reads entire STATIC_RULES.md (too large)

**Specialized Agents**:
- ✅ Read assigned guides IMMEDIATELY on spawn (MANDATORY)
- ✅ Read project SSOT files on-demand (when needed)
- ✅ Escalate if information not in guides

**When Agent Spawns**:
```
elementor-expert spawns →
  1. Read ELEMENTOR-API-TECHNICAL-GUIDE.md (complete)
  2. Read ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md (complete)
  3. Read ACTIVE_STATE.md (Current Pages, Global Colors sections)
  4. (Optional) Read COLOR-AND-STYLE-VISION.md if design context needed

design-expert spawns →
  1. Read CORE-WEBSITE-BUILDING-RULES.md (complete)
  2. (Optional) Read COLOR-AND-STYLE-VISION.md for project colors
  3. (Optional) Read design-mockup-v4.html for approved design

coder spawns →
  1. Read STATIC_RULES.md#mcp-checklist
  2. Read ACTIVE_STATE.md (Current Pages, Credentials)
  3. Read specific STATIC_RULES sections as needed

stuck spawns →
  1. Read TROUBLESHOOTING.md first (known issues)
  2. If not found, use Brave Search + R.JINA
  3. Update TROUBLESHOOTING.md if new solution discovered
```

---

## 🎯 How Coordination Works

### Standard Request Flow (Step-by-Step)

**Example**: User says "Create a 3-column benefits section with cards"

#### Step 1: Main Coordinator Receives Request
```
User Request → Claude Code
Claude reads ACTIVE_STATE.md to understand:
  - Current page ID (21)
  - Global Colors available
  - Current project state
```

#### Step 2: Create Task List (TodoWrite)
```javascript
TodoWrite({
  todos: [
    {content: "Backup page 21", status: "pending", activeForm: "Backing up page 21"},
    {content: "Create 3-column benefits section via elementor-expert", status: "pending", activeForm: "Creating benefits section"},
    {content: "Test visually via tester", status: "pending", activeForm: "Testing visually"},
    {content: "Fix any issues found", status: "pending", activeForm: "Fixing issues"}
  ]
})
```

#### Step 3: Delegate to Appropriate Agent
```javascript
// Mark first todo in_progress
TodoWrite({todos: [..., {content: "Backup page 21", status: "in_progress", ...}]})

// Run backup
Bash("python backup-before-update.py --page-id 21 --task 'create benefits section'")

// Mark complete, start next
TodoWrite({todos: [..., {content: "Backup page 21", status: "completed", ...}, {content: "Create 3-column benefits section", status: "in_progress", ...}]})

// Invoke specialist agent
Task({
  description: "Create 3-column benefits section",
  prompt: `Create a 3-column benefits section with icon-box cards on page 21.

  Requirements:
  - 3 columns with icon-box widgets
  - Card style: white background, top border (primary color), shadow
  - Equal height cards
  - Centered content
  - Responsive: 3 cols desktop, 2 tablet, 1 mobile
  - Use Global Colors from ACTIVE_STATE.md

  Technical:
  - Read ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md for card pattern
  - Style the COLUMN (not widget) for backgrounds/borders/shadows
  - Use 8-point spacing grid (30-40px column padding)
  - Follow MCP workflow (backup, get structure, update, clear cache)
  - Warn user about CSS regeneration (Issue #3)

  Page ID: 21
  Site: http://svetlinkielementor.local`,
  subagent_type: "general-purpose"
})
```

#### Step 4: Agent Works (Context Isolation)
```
elementor-expert agent spawns:
  1. Reads ELEMENTOR-API-TECHNICAL-GUIDE.md (knows property names, MCP workflow)
  2. Reads ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md (knows card pattern)
  3. Reads ACTIVE_STATE.md (gets page ID 21, Global Colors)
  4. Creates section using mcp__wp-elementor-mcp tools
  5. Returns report to Main Coordinator
```

#### Step 5: Main Coordinator Reports Back
```
TodoWrite({todos: [..., {content: "Create 3-column benefits section", status: "completed", ...}]})

Report to user:
  "✅ Created 3-column benefits section with icon-box cards
   - Applied white backgrounds with top border (primary color)
   - Added shadow for depth
   - Cards are equal height and centered
   - Responsive across all breakpoints

   ⚠️  IMPORTANT: Open page in Elementor editor and click 'Update' to regenerate CSS (Issue #3)"
```

#### Step 6: Continue with Next Task
```
TodoWrite({todos: [..., {content: "Test visually via tester", status: "in_progress", ...}]})

Task({
  description: "Test benefits section",
  prompt: "Test page 21 at http://svetlinkielementor.local/home. Take desktop/tablet/mobile screenshots. Verify cards are equal height, shadows showing, responsive layout correct.",
  subagent_type: "general-purpose"
})
```

---

## 🔀 Decision Trees: When to Use Which Agent

### Decision Tree Diagram

```
User Request
    │
    ├─ Contains keywords: "error", "problem", "stuck", "not working"
    │  └─→ stuck agent (Research)
    │
    ├─ Contains keywords: "test", "screenshot", "verify", "check visually"
    │  └─→ tester agent (Visual QA)
    │
    ├─ Technical Elementor question:
    │  │
    │  ├─ "How to create...", "What's the JSON for...", "Why isn't X showing?"
    │  │  └─→ elementor-expert agent
    │  │
    │  ├─ "How to center...", "How to align...", "Card structure pattern?"
    │  │  └─→ elementor-expert agent
    │  │
    │  └─ "What property name for...", "MCP workflow for..."
    │     └─→ elementor-expert agent
    │
    ├─ Design decision question:
    │  │
    │  ├─ "Should I use 2 or 3 columns?", "What layout?"
    │  │  └─→ design-expert agent
    │  │
    │  ├─ "Is this accessible?", "Does this meet WCAG?"
    │  │  └─→ design-expert agent
    │  │
    │  ├─ "What font size?", "How much spacing?", "What contrast?"
    │  │  └─→ design-expert agent
    │  │
    │  └─ "Is this CTA clear?", "Is text scannable?"
    │     └─→ design-expert agent
    │
    └─ General page creation: "Create...", "Build...", "Add..."
       │
       ├─ Elementor-specific (sections, columns, widgets, styling)
       │  └─→ elementor-expert agent
       │
       └─ General page structure
          └─→ coder agent (may delegate to elementor-expert)
```

### Keyword Routing Table

| User Says... | Route To | Why |
|-------------|----------|-----|
| "Create 3-column card layout" | elementor-expert | Technical structure |
| "Why aren't shadows showing?" | elementor-expert | Issue #3 troubleshooting |
| "How to center column content?" | elementor-expert | Alignment configuration |
| "Add benefits section to page" | elementor-expert | MCP implementation |
| "What's the correct JSON for gradient?" | elementor-expert | Group controls |
| "Should I use 2 or 3 columns?" | design-expert | Layout decision |
| "Is this contrast accessible?" | design-expert | WCAG compliance |
| "What font size for headings?" | design-expert | Typography scale |
| "How much spacing between cards?" | design-expert | 8-point grid |
| "Is this CTA button text clear?" | design-expert | UX writing |
| "Check if mobile looks good" | tester | Visual QA |
| "Take screenshots of homepage" | tester | Playwright automation |
| "Error with MCP connection" | stuck | Research problem |
| "Global Colors not applying" | stuck | Known issue research |

---

## 🛠️ Technical Implementation Details

### MCP Workflow (Via elementor-expert)

**Standard Flow**:
```
1. Pre-Flight Backup (MANDATORY)
   python backup-before-update.py --page-id 21 --task "description"
   → Creates backup in backups/page-21-backup-YYYYMMDD-HHMMSS.json
   → 10-second rollback if something breaks

2. Get Current Structure
   mcp__wp-elementor-mcp__get_elementor_elements(21, false)
   → Returns flat list of all elements (sections, columns, widgets)
   → No content preview (include_content: false for speed)

3. Update Element
   mcp__wp-elementor-mcp__update_elementor_widget(21, element_id, settings)
   → Updates specific widget/column/section by ID
   → Saves to wp_postmeta table
   → Deletes old CSS files

4. Clear Cache
   mcp__wp-elementor-mcp__clear_elementor_cache()
   → Clears Elementor's internal cache
   → Does NOT regenerate CSS (Issue #3)

5. CRITICAL: CSS Regeneration
   → Tell user: "Open page in Elementor editor and click 'Update'"
   → OR run: curl http://site.local/regenerate-elementor-css.php
   → OR visit: Elementor > Tools > Regenerate Files & Data
```

### Element Hierarchy & Styling

**THE GOLDEN RULE**:
```
To create card-style layouts with backgrounds, borders, and shadows:
→ Style the COLUMN, not the widget!
```

**Why?**
- **Columns** have full styling capabilities (background, border, shadow, padding)
- **Widgets** have limited container styling (content-specific only)
- **Sections** control layout (gaps, height, stretch)

**Structure**:
```
Section/Container (top-level)
├── layout: "boxed" or "full_width"
├── content_width: {size: 1140, unit: "px"}
├── gap: "custom"
├── gap_columns_custom: {size: 30, unit: "px"}
└── column_position: "stretch" (equal height)
    │
    └── Column (layout division)
        ├── _column_size: 33 (desktop %)
        ├── _inline_size_tablet: 50
        ├── _inline_size_mobile: 100
        ├── background_background: "classic"
        ├── background_color: "#FFFFFF"
        ├── border_border: "solid"
        ├── border_width: {...}
        ├── box_shadow: {...}  ← CARD STYLING HERE
        └── padding: {...}
            │
            └── Widget (content element)
                ├── title: "Benefit Title"
                ├── description: "Text here"
                ├── icon: {...}
                └── settings: {...}  ← CONTENT ONLY
```

### Property Naming Conventions

**CRITICAL DIFFERENCE**:
```json
// COLUMNS use simple names
{
  "box_shadow": {
    "horizontal": 0,
    "vertical": 10,
    "blur": 35,
    "spread": 0,
    "color": "rgba(0, 0, 0, 0.1)"
  },
  "background_background": "classic",
  "border_border": "solid"
}

// WIDGETS use prefixed names (if supported at all)
{
  "_box_shadow_box_shadow": {...},
  "background_background": "classic"  // Limited support
}
```

**Responsive Pattern**:
```json
{
  "padding": {"top": "40", "right": "30", "bottom": "40", "left": "30"},  // Desktop
  "padding_tablet": {"top": "30", "right": "20", "bottom": "30", "left": "20"},
  "padding_mobile": {"top": "20", "right": "15", "bottom": "20", "left": "15"}
}
```

### Global Colors System

**How They Work**:
```json
{
  "background_color": "var(--e-global-color-primary)"  // References global color
}
```

**Available Colors** (from ACTIVE_STATE.md):
- `--e-global-color-primary`: `#FABA29` (Yellow/Gold)
- `--e-global-color-secondary`: `#4F9F8B` (Teal/Green)
- `--e-global-color-text`: `#1D3234` (Dark Teal)
- `--e-global-color-accent`: `#FF8C7A` (Coral)
- `--e-global-color-5`: `#FEFCF5` (Warm Cream)

**Polyfill Active**: Issue #1 solved - Global Colors now work via REST API

---

## ⚠️ Known Issues & Workarounds

### Issue #3: CSS Doesn't Regenerate Automatically (CRITICAL)

**THE PROBLEM**:
- REST API updates save to database ✅
- CSS files get deleted ✅
- CSS regeneration does NOT happen automatically ❌

**ROOT CAUSE** (from document.php source code):
```php
public function save($data) {
    // ... save data to database ...

    $css_file = Post_CSS::create($post_id);
    $css_file->delete();  // ← Only deletion!
    // NO ->update() call here!
}
```

**THE FIX**:
1. **User clicks "Update"** in Elementor editor (triggers regeneration)
2. **OR** run PHP script: `curl http://site.local/regenerate-elementor-css.php`
3. **OR** visit: Elementor > Tools > Regenerate Files & Data

**AGENT PROTOCOL**:
- elementor-expert MUST warn user about this after every MCP update
- Include in final report: "⚠️ IMPORTANT: Click 'Update' in Elementor editor"

---

### Issue #1: Global Colors Not Showing (SOLVED)

**Status**: ✅ SOLVED via polyfill

**Solution**:
- Polyfill script active in theme
- Global Colors work via REST API
- No action needed

---

### Issue #2: Stretch Section Not Full-Width (SOLVED)

**Status**: ✅ SOLVED via "Internal Embedding"

**Solution**:
- Set `stretch_section: "yes"` in section settings
- Elementor "Internal Embedding" feature handles full-width
- No CSS hacks needed

---

### Issue #4: Containers ARE Available in FREE (CORRECTED)

**Status**: ✅ CORRECTED understanding

**Truth**:
- Containers ARE available in Elementor FREE
- Can use Containers OR Legacy Sections (both work)
- Containers = modern flexbox system
- Legacy Sections = traditional row/column system

---

### Issue #5: Header/Footer Not REST Accessible (LIMITATION)

**Status**: ⚠️ LIMITATION (workaround exists)

**Problem**:
- Header/Footer templates use custom post type `elementor_library`
- Not exposed via standard REST API

**Workaround**:
- Manual import via Elementor editor
- OR use PHP scripts directly
- Headers/Footers already created and working for this project

---

## 🔧 Maintenance & Troubleshooting

### How to Update the System

**Adding New Knowledge**:
1. Research thoroughly (Brave + R.JINA)
2. Create/update guide in `SSOT/` directory
3. Update relevant agent file (`.claude/agents/*.md`) to read new guide
4. Update `CLAUDE.md` with new guide reference
5. Update `ACTIVE_STATE.md` with completion note
6. Update this file (SYSTEM-OVERVIEW.md) if architecture changes

**Adding New Agent**:
1. Create agent file: `.claude/agents/new-agent.md`
2. Define purpose, knowledge base, required reading
3. Add to `CLAUDE.md` Communication Flow diagram
4. Add to delegation logic table
5. Update this file with agent description
6. Test with sample request

**Updating SSOT Files**:
- `STATIC_RULES.md`: Update when widget list or JSON schema changes
- `ACTIVE_STATE.md`: Update after EVERY task completion
- `TROUBLESHOOTING.md`: Update when new issues discovered and solved
- Technical guides: Update when new Elementor features or patterns discovered

### Agent Troubleshooting

**Agent not using guide information**:
- Check: Does agent file have "MANDATORY" reading requirement?
- Check: Is guide path correct in agent instructions?
- Fix: Update agent file with explicit "DO NOT PROCEED without reading X"

**Agent making wrong decisions**:
- Check: Is decision tree in CLAUDE.md clear?
- Check: Are keywords mapped correctly?
- Fix: Update delegation logic table with better examples

**Agent escalating too much**:
- Check: Is information actually in guides?
- Fix: Add missing information to appropriate guide
- Fix: Update agent file to reference specific guide sections

**Agent duplicating SSOT content**:
- Check: Is Main Coordinator pointing to specific sections?
- Fix: Use pattern "Read STATIC_RULES.md#section-name" instead of copying

### MCP Server Issues

**MCP tools not showing (`mcp__` prefix missing)**:
- Check: Is `.mcp.json` configured correctly?
- Check: Are npm packages installed in MCP server directories?
- Fix: Run `npx @modelcontextprotocol/inspector list` to test
- Fix: Restart Claude Code

**wp-elementor-mcp connection failing**:
- Check: WordPress credentials in `config.json`
- Check: Site URL accessible (http://svetlinkielementor.local)
- Check: Application Password valid (not regular password)
- Fix: Regenerate Application Password in WordPress
- Fix: Update `config.json` with new credentials

**Brave Search rate limiting**:
- Check: Daily request limit reached
- Fix: Wait 24 hours OR use cached results
- Workaround: Use R.JINA with known URLs instead

---

## 📊 Performance & Best Practices

### Token Usage Optimization

**Main Coordinator**:
- ✅ Read ACTIVE_STATE.md (15 KB) - reasonable
- ✅ Read specific STATIC_RULES sections (pointed by coordinator)
- ❌ NEVER read entire STATIC_RULES.md (90 KB waste)

**Agents**:
- ✅ Read complete technical guides on spawn (MANDATORY for expertise)
- ✅ Read project SSOT sections on-demand
- ❌ Don't duplicate information already in guides

**Research**:
- ✅ Use Brave Search first (cheap)
- ✅ Use R.JINA for specific URLs (targeted extraction)
- ❌ Don't over-research - check guides first

### Quality Assurance

**Before Deploying Page Updates**:
1. ✅ Pre-flight backup created (`backup-before-update.py`)
2. ✅ Element structure correct (Section → Column → Widget)
3. ✅ Property names correct (check element type!)
4. ✅ Responsive settings applied (mobile/tablet/desktop)
5. ✅ Global Colors used (not hardcoded)
6. ✅ 8-point spacing grid followed
7. ✅ Cache cleared (`mcp__clear_elementor_cache`)
8. ✅ User warned about CSS regeneration (Issue #3)

**After Deploying**:
1. ✅ User clicks "Update" in Elementor editor
2. ✅ Visual test via tester agent (screenshots)
3. ✅ Responsive test (desktop/tablet/mobile)
4. ✅ Accessibility check (contrast, touch targets)
5. ✅ Update ACTIVE_STATE.md with changes

### Safety Protocols

**MANDATORY Pre-Flight Snapshot**:
```bash
python backup-before-update.py --page-id 21 --task "description"
```
- ✅ Creates timestamped backup in `backups/`
- ✅ 10-second rollback available if issue
- ✅ NO EXCEPTIONS - always backup first

**Research Source Hierarchy**:
```
Tier 1 (AUTHORITATIVE):
  - Official Elementor docs (developers.elementor.com)
  - GitHub (github.com/elementor/elementor)
  - Stack Overflow (stackoverflow.com)
  - W3C (w3.org)
  - Nielsen Norman Group (nngroup.com)

Tier 2 (TRUSTWORTHY):
  - WordPress.org forums
  - Smashing Magazine
  - CSS-Tricks
  - Web.dev

FORBIDDEN:
  - Medium (unreliable)
  - Random blogs
  - SEO content farms
```

**No Fallback Principle**:
- Agents escalate problems, don't work around
- If information not in guides → ask Main Coordinator
- If Main Coordinator doesn't know → delegate to stuck agent
- stuck agent researches → updates guides with findings

---

## 🎓 How to Use This System

### For New Users

1. **Read this file first** (you are here!)
2. **Read `.claude/CLAUDE.md`** (Main Coordinator instructions)
3. **Read `SSOT/ACTIVE_STATE.md`** (current project state)
4. **Understand the flow**: User → Coordinator → Agent → MCP → WordPress

### For Daily Work

**Pattern**:
```
1. User makes request
2. Main Coordinator reads ACTIVE_STATE.md
3. Main Coordinator creates TodoWrite task list
4. Main Coordinator delegates to appropriate agent via Task tool
5. Agent reads required guides (MANDATORY)
6. Agent completes task using MCP tools
7. Agent reports back to Main Coordinator
8. Main Coordinator updates TodoWrite (mark complete)
9. Main Coordinator reports to user
10. Main Coordinator updates ACTIVE_STATE.md
```

**Example User Requests**:

```
"Create a modern hero section with gradient background"
→ elementor-expert (technical implementation)

"Should the hero have 1 or 2 CTA buttons?"
→ design-expert (UX decision)

"Test if the homepage looks good on mobile"
→ tester (visual QA)

"Global Colors aren't showing up"
→ stuck (research - check TROUBLESHOOTING.md first)
```

### For System Maintenance

**Weekly**:
- Review ACTIVE_STATE.md for accuracy
- Check if any new issues need adding to TROUBLESHOOTING.md
- Verify MCP servers working (test with sample request)

**After Major Work**:
- Update ACTIVE_STATE.md with new page IDs, status
- Create session notes in `SSOT/archive/sessions/`
- Update technical guides if new patterns discovered

**When Adding Features**:
- Research thoroughly (Brave + R.JINA)
- Update appropriate guide in `SSOT/`
- Update agent files if new knowledge added
- Test with real request to verify agent understands

---

## 📚 Quick Reference

### Agent Spawn Checklist

**elementor-expert**:
- [ ] Read ELEMENTOR-API-TECHNICAL-GUIDE.md (complete)
- [ ] Read ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md (complete)
- [ ] Read ACTIVE_STATE.md (Current Pages, Global Colors)
- [ ] Ready to build with MCP

**design-expert**:
- [ ] Read CORE-WEBSITE-BUILDING-RULES.md (complete)
- [ ] (Optional) Read COLOR-AND-STYLE-VISION.md
- [ ] Ready to advise on UX/UI

**coder**:
- [ ] Read STATIC_RULES.md#mcp-checklist
- [ ] Read ACTIVE_STATE.md (Current Pages, Credentials)
- [ ] Ready to create pages

**tester**:
- [ ] Read ACTIVE_STATE.md (Current Pages, Site URL)
- [ ] Playwright MCP tools available
- [ ] Ready to test visually

**stuck**:
- [ ] Read TROUBLESHOOTING.md (check known issues first)
- [ ] Brave Search + R.JINA tools available
- [ ] Ready to research

### File Locations

```
.claude/
├── CLAUDE.md                      # Main Coordinator instructions
└── agents/
    ├── elementor-expert.md        # Elementor specialist
    ├── design-expert.md           # UX/UI specialist
    ├── coder.md                   # General implementation
    ├── tester.md                  # Visual QA
    ├── stuck.md                   # Research agent
    └── designer.md                # Legacy (use design-expert)

SSOT/
├── ELEMENTOR-API-TECHNICAL-GUIDE.md         # ~450 lines
├── ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md # ~500 lines
├── CORE-WEBSITE-BUILDING-RULES.md           # ~1100 lines
├── STATIC_RULES.md                          # ~90 KB
├── ACTIVE_STATE.md                          # ~15 KB (updated frequently)
└── TROUBLESHOOTING.md                       # 21 KB

SYSTEM-OVERVIEW.md              # This file - complete architecture
COLOR-AND-STYLE-VISION.md       # Project design system
config.json                     # WordPress credentials, MCP settings
.mcp.json                       # MCP server configuration
```

### Critical Commands

```bash
# Backup before update (MANDATORY)
python backup-before-update.py --page-id 21 --task "description"

# Regenerate CSS (Issue #3 workaround)
curl http://svetlinkielementor.local/regenerate-elementor-css.php

# Test MCP servers
npx @modelcontextprotocol/inspector list

# Check git status
git status

# Visual test
node scripts/working/take-screenshots-only.js
```

---

## ✅ System Health Checklist

**Green Light** (System Ready):
- [x] MCP servers loaded (mcp__ prefix visible in tools)
- [x] ACTIVE_STATE.md updated with current status
- [x] 3 technical guides created (API, Structure, Web Rules)
- [x] 2 specialized agents created (elementor-expert, design-expert)
- [x] Global Colors working (Issue #1 solved)
- [x] Pre-flight backup system active
- [x] Known issues documented in TROUBLESHOOTING.md

**Yellow Light** (Working with Limitations):
- [x] CSS regeneration manual (Issue #3 - user must click Update)
- [x] Header/Footer not REST accessible (Issue #5 - workaround exists)

**Red Light** (Action Needed):
- [ ] MCP servers not loading → Check `.mcp.json`, restart Claude
- [ ] Agents not reading guides → Update agent files with MANDATORY directive
- [ ] Tasks failing repeatedly → Check TROUBLESHOOTING.md, escalate to stuck agent

---

## 🎯 Key Takeaways

1. **This is a knowledge-driven system** - Agents must read guides to have expertise
2. **Coordination is key** - Main Coordinator delegates, doesn't do specialized work
3. **Context isolation works** - Each agent spawns fresh with Task tool, reads own guides
4. **Safety first** - Always backup before updates (pre-flight snapshot)
5. **CSS regeneration is manual** - Issue #3 is known, user must click Update
6. **SSOT is truth** - All information lives in SSOT files, no duplication
7. **Agents escalate** - No Fallback Principle - if stuck, escalate to Main Coordinator → stuck agent
8. **Visual testing matters** - Always verify with screenshots after changes
9. **8-point grid** - All spacing in multiples of 4px or 8px
10. **Style columns for cards** - Not widgets (most common mistake)

---

**Mantra**:
> "Read guides, delegate specialists, track with todos, backup first, verify visually."

**Version**: 7.0 (Knowledge System Complete)
**Last Updated**: 2025-11-30
**Maintained by**: Claude Code (Main Coordinator)

---

**If you're reading this and confused, start here**:
1. Read this file (SYSTEM-OVERVIEW.md) completely ← you are here
2. Read `.claude/CLAUDE.md` (Main Coordinator role)
3. Read `SSOT/ACTIVE_STATE.md` (current project state)
4. Make a request - watch the system work!

**Questions? Check**:
- TROUBLESHOOTING.md (known issues)
- Slack Main Coordinator: "How does X work?"
- Read relevant technical guide in SSOT/
