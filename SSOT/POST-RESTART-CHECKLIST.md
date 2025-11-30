# 🔄 POST-RESTART CHECKLIST - Immediate Actions After Claude Code Restart

**Created**: 2025-11-30
**Purpose**: Get back on track immediately after restarting Claude Code
**Status**: READY TO USE
**Estimated Time**: 5-10 minutes

---

## ⚡ STEP 1: VERIFY MCP TOOLS LOADED (2 minutes)

### **Expected New Tools** (37 total):

#### **wp-elementor-mcp** (32 tools expected):
```bash
# Check for these tool prefixes:
mcp__wp-elementor__create_page
mcp__wp-elementor__update_page
mcp__wp-elementor__get_pages
mcp__wp-elementor__create_elementor_section
mcp__wp-elementor__add_widget_to_section
mcp__wp-elementor__get_elementor_data
mcp__wp-elementor__update_elementor_data
mcp__wp-elementor__clear_elementor_cache_by_page
mcp__wp-elementor__upload_media
# Plus 23 more...
```

#### **json-schema-validator** (5 tools expected):
```bash
mcp__json-schema__generate_schema
mcp__json-schema__validate_json_schema
mcp__json-schema__add_update_schema
mcp__json-schema__validate_json_from_collections
mcp__json-schema__list_schemas
```

#### **Already Working**:
- ✅ `mcp__playwright__*` tools (20+ browser automation tools)
- ✅ Brave Search (via brave-search MCP)

### **Verification Actions**:
1. Check tool list for `mcp__wp-elementor__*` prefix
2. Check tool list for `mcp__json-schema__*` prefix
3. If NOT present → Restart Claude Code again and wait 15 seconds
4. If still not working → Check `.mcp.json` configuration

---

## 📊 STEP 2: CURRENT PROJECT STATUS (1 minute read)

### **What's Done**:
- ✅ Homepage (Page 21): 6 sections complete, headers/footers working
- ✅ About (23), Programs (25), FAQ (29): Complete
- ✅ Contact (27): Built but needs CF7 form + Google Maps
- ✅ Blog content: 17 posts written (SSOT/Blog/) ready to publish
- ✅ Global Colors: Updated with Coral #FF8C7A, background #FEFCF5
- ✅ Containers: NOW AVAILABLE in FREE (documentation corrected)
- ✅ MCP Servers: 4 configured (wp-elementor, json-schema, brave, playwright)

### **What's Pending**:
- ⏳ Hero Section: Needs IMPROVEMENT (not rebuild!) - use modern design as inspiration
- ⏳ Blog page (31): Not built yet
- ⏳ Privacy (33), Terms (35): Not built
- ⏳ Contact page: Add CF7 form + Google Maps

### **Critical Context**:
- **Recent Issue**: Coder agent deleted homepage content when told "use as reference"
- **Lesson Learned**: "Use as reference" = INSPIRATION for styling, NOT replacement
- **Rule Added**: CRITICAL RULE in all agent files (improvements vs replacements)

---

## 🎯 STEP 3: IMMEDIATE PRIORITY TASKS

### **Priority 1: Test MCP Tools** (5 minutes)
```bash
# Test wp-elementor-mcp connection
# Use any wp-elementor tool to verify WordPress connection
# Expected: Successfully connects to http://svetlinkielementor.local

# Test json-schema-validator
# Use generate_schema or list_schemas to verify Python server running
# Expected: Tool responds without errors
```

### **Priority 2: Hero Section Design Improvements** (CAREFUL!)
**User Request**: Improve hero section using React component as INSPIRATION

**What User Wants**:
- Modern gradient background (like reference)
- Two-column layout (like reference)
- Badge/pill accent element (like reference)
- Dual CTA buttons (like reference)

**What User DOESN'T Want**:
- ❌ Delete existing content
- ❌ Rebuild from scratch
- ❌ Remove Bulgarian text
- ❌ Remove counters
- ❌ Remove existing CTAs

**CRITICAL RULE**:
> "Use as reference" = INSPIRATION for styling/layout
> "Rebuild entirely" = FULL REPLACEMENT
> **IF UNCLEAR → ASK USER FIRST!**

**Safe Approach**:
1. Read current homepage hero section (Page 21, Section 0)
2. Design improvements that ENHANCE existing content
3. Ask user for approval before implementing
4. **MANDATORY**: Run Pre-Flight Snapshot before ANY changes

### **Priority 3: Build Blog Page** (When ready)
- 17 posts already written in SSOT/Blog/
- Content is in Bulgarian
- Ready to publish and display

---

## 🚨 SAFETY REMINDERS (READ BEFORE WORKING!)

### **Pre-Flight Snapshot** (MANDATORY):
```bash
# BEFORE ANY PAGE UPDATE:
python backup-before-update.py --page-id 21 --task "hero-improvements"

# IF SOMETHING BREAKS:
python restore-from-backup.py --page-id 21 --latest
```

### **CRITICAL RULE #1: Improvements vs Replacements**

**WHEN USER PROVIDES REFERENCE/INSPIRATION:**

✅ **DO - IMPROVE EXISTING**:
- Use reference for **styling ideas** (colors, layouts, spacing)
- Use reference for **design patterns** (two-column, gradients, etc.)
- **KEEP ALL existing content/information**
- **ENHANCE** what's already there
- Add new elements **alongside** existing ones

❌ **DON'T - REPLACE EVERYTHING**:
- ❌ NEVER delete all existing sections
- ❌ NEVER rebuild from scratch unless explicitly told
- ❌ NEVER remove existing content/widgets
- ❌ NEVER assume "reference" means "replace everything"

**KEY DISTINCTION**:
- "Use this as reference" = **INSPIRATION for styling**
- "Rebuild this entirely" = **FULL REPLACEMENT**

**IF UNCLEAR → ASK USER FIRST!**

**Example**:
- User shows React hero code → Use for styling ideas (gradient, layout)
- KEEP existing Bulgarian text, counters, CTA buttons
- IMPROVE styling/layout, DON'T delete everything

---

## 🔧 TECHNICAL QUICK REFERENCE

### **WordPress Access**:
- Site URL: `http://svetlinkielementor.local`
- Admin User: `test`
- Admin Password: `test`
- REST API: `http://svetlinkielementor.local/wp-json/wp/v2/`
- Application Password: `S27q64rqoFhfTPDA30nBhNM5`

### **Global Colors** (5 colors):
```css
--e-global-color-primary:   #FABA29  /* Yellow/Gold */
--e-global-color-secondary: #4F9F8B  /* Teal/Green */
--e-global-color-text:      #1D3234  /* Dark Teal */
--e-global-color-accent:    #FF8C7A  /* Coral - NEW */
--e-global-color-5:         #FEFCF5  /* Warm Cream - Site Background */
```

### **Elementor FREE Capabilities**:
```javascript
// ✅ Containers ARE AVAILABLE in FREE (verified 2025-11-30)
{"elType": "container"}  // Modern, recommended

// ✅ Legacy Sections still supported
{"elType": "section"}  // Section > Column > Widget
```

### **Page IDs**:
- Homepage: 21
- About: 23
- Programs: 25
- Contact: 27
- FAQ: 29
- Blog: 31
- Privacy: 33
- Terms: 35

### **Template IDs**:
- Header: 69
- Footer: 73

---

## 📂 KEY FILES TO READ (If Needed)

**Essential Context**:
1. `SSOT/00-POST-COMPACT-RESTORATION.md` - Complete project context (read first!)
2. `SSOT/ACTIVE_STATE.md` - Current page IDs, credentials, colors
3. `SSOT/MCP-CONFIGURATION.md` - MCP server documentation
4. `SSOT/STATIC_RULES.md` - Elementor FREE constraints, widget whitelist
5. `SSOT/TROUBLESHOOTING.md` - Known issues and solutions

**Agent Files**:
- `.claude/CLAUDE.md` - Main coordinator instructions
- `.claude/agents/coder.md` - MCP page builder
- `.claude/agents/designer.md` - Design compliance enforcer
- `.claude/agents/tester.md` - Playwright screenshots
- `.claude/agents/stuck.md` - Research agent

---

## ✅ VERIFICATION CHECKLIST

After restart, verify:
- [ ] wp-elementor-mcp tools loaded (32 tools with `mcp__wp-elementor__*` prefix)
- [ ] json-schema-validator tools loaded (5 tools with `mcp__json-schema__*` prefix)
- [ ] Playwright tools still working (20+ tools with `mcp__playwright__*` prefix)
- [ ] Brave Search still working
- [ ] Total tools: 55+ available
- [ ] WordPress connection: Test with wp-elementor tool
- [ ] JSON validator: Test with list_schemas or generate_schema
- [ ] Read CRITICAL RULE in .claude/CLAUDE.md (improvements vs replacements)
- [ ] Know Pre-Flight Snapshot workflow (backup-before-update.py)
- [ ] Understand current hero section status (needs improvement, not rebuild)

---

## 🎯 NEXT ACTIONS (In Order)

1. **Verify MCP Tools** (2 min) - Check for 37 new tools
2. **Test MCP Connections** (5 min) - WordPress + JSON validator
3. **Read Hero Section** (2 min) - Understand current state (Page 21, Section 0)
4. **Plan Hero Improvements** (5 min) - Design enhancements ONLY (no deletions)
5. **Ask User for Approval** (REQUIRED) - Show plan before implementing
6. **Pre-Flight Snapshot** (30 sec) - Backup before ANY changes
7. **Implement Improvements** (10 min) - Enhance styling/layout
8. **Test and Screenshot** (5 min) - Verify improvements worked

---

## 🚨 RED FLAGS - STOP AND ASK USER IF:

- You're about to delete existing sections/widgets
- You're about to rebuild a page from scratch
- User says "use as reference" but you're planning full replacement
- You're unsure if task is improvement or replacement
- Pre-Flight Snapshot fails or backup doesn't exist
- MCP tools are not loading after restart
- JSON validation fails on Elementor structure

**When in doubt → ASK USER FIRST!**

---

## 📞 QUICK HELP

**If MCP tools not loading**:
1. Check `.mcp.json` configuration exists
2. Verify paths: `C:\Users\denit\wp-elementor-mcp\dist\index.js`
3. Verify paths: `C:\Users\denit\jsonshema_mcp\mcp_server.py`
4. Restart Claude Code again (wait 15 seconds)
5. Check Claude Code logs for MCP startup errors

**If stuck on Elementor issues**:
1. Read `SSOT/TROUBLESHOOTING.md` (5 known issues documented)
2. Check `SSOT/STATIC_RULES.md` for widget constraints
3. Delegate to stuck agent for research (Task tool with subagent_type="stuck")

**If unsure about design approach**:
1. Delegate to designer agent for specifications
2. Ask user for clarification
3. Show plan before implementing

---

**✅ CHECKLIST COMPLETE! You're ready to continue working.**

**Version**: 1.0
**Created**: 2025-11-30
**Last Updated**: 2025-11-30
**Next Review**: After Claude Code restart
