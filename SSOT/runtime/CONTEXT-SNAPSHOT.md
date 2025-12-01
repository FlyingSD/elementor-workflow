# CONTEXT SNAPSHOT

**Last Updated**: 2025-12-01 19:08:24
**Purpose**: Session continuity - restore context after restart
**Auto-generated**: By update-snapshot.js

---

## 🎯 CURRENT WORKING STATE

**Active Pages**:
- Page 21: Home (/home-2/)
- Page 23: About (/about/)
- Page 25: Programs (/programs/)
- Page 27: Contact (/contact/)
- Page 29: FAQ (/faq/)
- Page 31: Blog (/blog/)
- Page 33: Privacy Policy (/privacy-policy-2/)
- Page 35: Terms of Service (/terms-of-service/)

**Last Session**: 2025-12-01

---

## 📋 NEXT ACTIONS

## 📌 Next Immediate Actions

**Completed (2025-11-29)**:
- ✅ Header/Footer templates built (ID 69, 73) with Theme Builder
- ✅ Navigation menu added to header (5 menu items: Home, About, Programs, Contact, Blog)
- ✅ Dark footer with 4 columns (brand, resources, contact, social icons)
- ✅ Programs page built (5 levels + pricing)
- ✅ About page built (mission + values + team)
- ✅ Contact page built (info + hours + form placeholder)
- ✅ FAQ page built (10 Q&A with accordion)
- ✅ All pages use Theme Builder templates (header/footer automatic)
- ✅ Theme switched to Hello Elementor (from Twenty Twenty-Five)
- ✅ Switched from Header Footer Elementor plugin to native Theme Builder

**Next Priority Tasks**:
1. **⭐ V4 STYLING IMPLEMENTATION** - Apply approved design to homepage (design-mockup-v4.html)
   - Hero section: Yellow gradient, two-column, mascot, coral underline
   - Benefits section: White cards with colored top borders
   - Programs section: 3 teaser cards (Levels, Promotions, FAQ)
   - Blog carousel: Single card with nav buttons
   - Use ELEMENTOR-API-WORKFLOW-GUIDE.md methodology
2. **Contact Page** - Add Contact Form 7 shortcode (form ID 43 exists)
3. **Contact Page** - Add Google Maps embed
4. **About Page** - Upload team member photos (replace icon placeholders)
5. **Programs Page** - Add program level images (5 images needed)

**Completed This Session (2025-11-29 Evening)**:
- ✅ Enabled Canvas template option on Footer template (ID 73) via PHP script
- ✅ Changed all pages (About, Programs, Contact, FAQ) to Canvas template
- ✅ Added complete header section to all pages with:
  * Logo "Светлинки" (left, teal, clickable to homepage)
  * Navigation menu (center, 5 links: Начало, За Нас, Програми, Контакти, FAQ)
  * CTA button "ЗАПАЗИ СЕ СЕГА" (right, golden yellow, links to /contact/)
- ✅ Cleared Elementor cache multiple times
- ✅ Created POST-LAUNCH-IMPROVEMENTS.md for future enhancements
- ✅ Documented why Nav Menu is HTML widget (Nav Menu widget is Elementor PRO only)
- ✅ **HEADERS AND FOOTERS NOW WORKING** - User opened pages in Elementor and clicked "Update", both header and footer now display on all pages!

**Completed This Session (2025-11-30 Evening)**:
- ✅ Created **ELEMENTOR-API-TECHNICAL-GUIDE.md** (SSOT/) - Complete technical reference:
  * Architecture overview (WordPress + Elementor plugin structure)
  * Complete save/update flow (document.php → CSS generation)
  * CSS generation system (post.php rendering pipeline)
  * REST API integration & MCP server workflow
  * Group controls deep dive (Background, Border, Shadow, Typography)
  * Property naming conventions & element-specific differences
  * Cache management (5 layers explained)
  * Troubleshooting guide (CSS visibility, shadows, gradients)
- ✅ Created **ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md** (SSOT/) - Practical layout guide:
  * Structure fundamentals (Section → Column → Widget hierarchy)
  * Section configuration (layout, gaps, height, alignment)
  * Column layout & alignment (vertical/horizontal, responsive widths)
  * Card structure patterns (3-column grids, icon-box cards, text cards)
  * Text & content alignment (widget-level controls)
  * Spacing system (recommended values, responsive scaling)
  * Common patterns (benefits cards, hero sections, footers)
  * Troubleshooting layouts (equal heights, centering, gaps)
- ✅ Created **CORE-WEBSITE-BUILDING-RULES.md** (SSOT/) - Universal web design principles:
  * Nielsen's 10 Usability Heuristics (system status, user control, consistency, error prevention)
  * 10 Principles of Effective Web Design (don't make users think, simplicity, whitespace)
  * WCAG Accessibility (POUR: Perceivable, Operable, Understandable, Robust)
  * Typography system (Material Design scale, line length 45-75 chars, line height 1.5)
  * 8-point spacing grid system (4px/8px increments, spacing hierarchy)
  * Color contrast rules (WCAG AA: 4.5:1 normal text, 3:1 large text)
  * Layout & grid systems (12-column grid, container widths, visual hierarchy)
  * Responsive design (mobile-first, breakpoints, touch targets 44px min)
  * Content/UX writing (scannable, active voice, 50-80 chars per line)
  * Navigation patterns, form best practices, performance (Core Web Vitals)
  * Before-launch checklist (content, design, accessibility, SEO, technical)
- ✅ Updated ACTIVE_STATE.md with references to all 3 new technical guides
- ✅ Research complete: Extracted from industry authorities (Nielsen Norman Group, W3C WCAG, Material Design, Smashing Magazine, Web.dev, USWDS)
- ✅ Created **elementor-expert agent** (.claude/agents/elementor-expert.md):
  * Specialized for Elementor API, MCP workflows, structure, alignment
  * MANDATORY reading: ELEMENTOR-API-TECHNICAL-GUIDE.md + ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md on spawn
  * Use for: Technical implementation, property names, MCP workflow, card patterns
- ✅ Created **design-expert agent** (.claude/agents/design-expert.md):
  * Specialized for UX/UI decisions, accessibility, web standards
  * MANDATORY reading: CORE-WEBSITE-BUILDING-RULES.md on spawn
  * Use for: Layout decisions, WCAG compliance, typography, spacing, color contrast
- ✅ Created **SYSTEM-OVERVIEW.md** (project root) - Complete architecture documentation:
  * Complete system architecture diagram (User → Coordinator → Agents → MCP → WordPress)
  * Knowledge management pyramid (3 universal guides + 3 project-specific SSOT files)
  * Decision trees (when to use which agent, keyword routing table)
  * MCP workflow, element hierarchy, property naming
  * Maintenance procedures, troubleshooting, best practices
  * 900+ lines comprehensive system documentation
- ✅ Updated **CLAUDE.md** (v7.0 - Knowledge System Complete):
  * Added "NEW TO THIS SYSTEM?" section pointing to SYSTEM-OVERVIEW.md
  * Updated Communication Flow diagram with elementor-expert and design-expert
  * Expanded Delegation Logic with detailed "When to use" examples
  * Updated Information Architecture listing 3 new technical guides
  * Updated Agent Files list with new agents

**Known Issues Resolved**:
- ✅ Footer now displaying (fixed after Elementor Update click - Issue #3 confirmed)
- ✅ Headers now displaying (fixed after Elementor Update click - Issue #3 confirmed)

**Technical Notes**:
- Navigation menu uses HTML widget (FREE workaround) instead of Nav Menu widget (PRO only) - see POST-LAUNCH-IMPROVEMENTS.md
- Issue #3 confirmed: REST API changes require manual Elementor "Update" click to activate

**Future**:
- Build Blog page (ID 31)
- Build Privacy Policy page (ID 33)
- Build Terms of Service page (ID 35)
- Test responsive design (mobile/tablet)
- Consider Elementor PRO upgrade (see POST-LAUNCH-IMPROVEMENTS.md)

---

**Document Version**: 1.7
**Created**: 2025-11-29
**Last Updated**: 2025-12-01 (Major cleanup & documentation session)
**Purpose**: Single source for current project state
**Update Policy**: Update only when values change (page IDs, credentials, new pages created, etc.)

**Session Note (2025-11-30)**:
✅ CLEANUP COMPLETE - 33 files archived to `archive/2025-11-old-*` folders:
- 11 completed documentation reports/session logs
- 3 design mockup iterations (v1-v3)
- 9 JSON data snapshots
- 10 deprecated Python/JavaScript scripts
✨ ROOT CLEANED - Only active files remain (V4 design docs, working scripts)
🎯 READY FOR V4 - Homepage styling implementation next using approved design-mockup-v4.html

**Session Note (2025-12-01 - Major Cleanup)**:
✅ **SSOT Enhanced with Research & Lessons**:
- Created `SSOT/LESSONS-LEARNED.md` - Post-mortem of 5-hour CSS regeneration debugging session
- Added GitHub research sources to `SSOT/TROUBLESHOOTING.md` Issue #6 (7 Elementor issues documented)
- Moved `ELEMENTOR-API-WORKFLOW-GUIDE.md` to SSOT/ (belongs with technical guides)

✅ **Project Root Cleaned**:
- Archived 3 reports to `archive/2025-11-30-session/reports/`:
  * CSS-REGENERATION-FINAL-REPORT.md
  * ELEMENTOR-CSS-REGENERATION-SOLUTION.md
  * HOMEPAGE-VISUAL-ANALYSIS-REPORT.md
- Archived templates to `archive/2025-11-30-session/templates/` (header, footer - 98+118 lines)
- Archived extracted-sections to `archive/2025-11-30-session/extracted-sections/` (benefits, blog, programs)
- Deleted screenshots/ directory (17MB stale screenshots - tester agent can regenerate fresh)
- Deleted temp files (backup_output.txt, backup_output2.txt, v4-for-mcp.txt, nul)

✅ **Scripts Organized**:
- Moved `force-css-regeneration.py` to scripts/working/
- Moved `take-elementor-editor-screenshot.js` to scripts/working/
- Updated `scripts/README.md` with all Playwright scripts (frontend vs editor distinction)
- **IMPORTANT**: Documented Denis's environment (changes show WITHOUT Update button)

✅ **Blog Files Cleanup**:
- 17 blog markdown files (Bulgarian) moved to `SSOT/archive/Blog/`

🎯 **File Structure Now**:
```
Root (CLEAN):
├── Design System: design-mockup-v4.html, COLOR-AND-STYLE-VISION.md, V4-COMPONENT-LIBRARY.md
├── System Docs: SYSTEM-OVERVIEW.md, README-NEXT-STEPS.md, ELEMENTOR-FREE-2024-2025.md
├── Config: config.json, .mcp.json
├── Safety: mcp-backup/ (wp-elementor-mcp safety backup)
└── Working: scripts/, SSOT/, backups/, archive/

SSOT/ (Enhanced):
├── Technical Guides (4): ELEMENTOR-API-*, ELEMENTOR-STRUCTURE-*, CORE-WEBSITE-*, ELEMENTOR-API-WORKFLOW-GUIDE
├── Project Docs (3): STATIC_RULES.md, ACTIVE_STATE.md, TROUBLESHOOTING.md
├── NEW: LESSONS-LEARNED.md (post-mortems of major issues)
└── NEW: MANDATORY-CSS-REGENERATION.md (critical workflow)
```

**Key Takeaway**: "Keep only what moves you forward" - Archived completed work, kept production-ready files, enhanced SSOT with lessons to prevent repeating 5-hour debugging sessions.


---

## 🚨 QUICK ACCESS

**Current Values**: Always read ACTIVE_STATE.md for:
- Page IDs → Current Pages section
- Global Colors → Global Design System section
- Credentials → Credentials & Access section

**Common Tasks**:
- Update page → Use anchor-search.js to find relevant guide sections
- Fix styling → Check TROUBLESHOOTING.md first
- CSS not showing → MANDATORY-CSS-REGENERATION.md workflow

---

## 💡 RESTORE PROTOCOL

**On restart, read this file FIRST** to understand:
- Where we left off
- What pages are active
- What's next to do

Then proceed with user's request.

---

**Snapshot Version**: 1.0
**Generated By**: scripts/core/update-snapshot.js
**Frequency**: After each major task completion
