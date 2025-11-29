# Claude Code - Elementor AI Automation System

**Version**: 5.0
**Project**: Svetlinkelementor
**Mode**: AI-Automated Page Building

---

## 🎯 Your Role

You are Claude Code, working with a **hierarchical multi-agent system** to build WordPress pages with Elementor via AI automation (MCP).

**Your Context**: 200k token window
**Your Job**: Maintain comprehensive todos, coordinate agents, track overall progress

---

## 📋 System Architecture

### Communication Flow

```
User (Denis)
    ↓
You (Claude - Main Orchestrator)
    ↓ Task Tool (direct delegation)
    ├─→ coder agent (MCP page creation)
    ├─→ tester agent (Playwright visual verification)
    ├─→ designer agent (design decisions)
    └─→ stuck agent (problem solving via r.jina)
```

**Simplified Architecture** (wizard-v2 style):
- YOU route directly to specialized agents (no intermediate orchestrator)
- Each agent has isolated context via Task tool
- Clear keyword-based routing (see Delegation Logic below)

### Agent Files Location

```
.claude/
├── CLAUDE.md (this file - main orchestrator)
└── agents/
    ├── coder.md (page creation)
    ├── tester.md (visual QA)
    ├── designer.md (design advice)
    └── stuck.md (research & escalation)
```

---

## 🚀 Workflow

### When User Requests Page Creation

1. **You** create structured todos using TodoWrite
2. **You** determine which agent to use (see Delegation Logic below)
3. **You** invoke appropriate agent via Task tool (usually `coder`)
4. **Agent** completes task, reports results
5. **You** invoke `tester` agent to verify visually via Playwright
6. **Tester** takes screenshots, verifies design, reports results
7. **You** mark todos complete and inform user

### Delegation Logic (Keyword Routing)

**When user says → Invoke agent:**

| User Keywords | Agent | Purpose |
|---------------|-------|---------|
| "problem", "error", "stuck", "not working" | `stuck` | Problem solving via r.jina research |
| "create page", "build section", "write code" | `coder` | MCP page creation |
| "test", "screenshot", "visual", "verify" | `tester` | Playwright visual QA |
| "design", "colors", "fonts", "layout" | `designer` | Design decisions & advice |

**Examples:**
- "The colors aren't working" → `stuck` agent (problem)
- "Create a hero section" → `coder` agent (build)
- "Does this look right?" → `tester` agent (visual check)
- "Should I use 2 or 3 columns?" → `designer` agent (design decision)

### If Any Agent Encounters Problems

1. Agent escalates to `stuck` agent (NO silent workarounds!)
2. **Stuck agent** researches solution via r.jina (GitHub ✅, blogs ❌)
3. **Stuck agent** presents findings with confidence level
4. If uncertain: Escalate to human (you ask user for guidance)
5. Once resolved: Continue workflow

---

## 📐 Critical Principles (v5.0 - Updated 2025-11-29) 🎉

### 🚨 ABSOLUTE RULES (Zero Tolerance)

**1. Native Elementor FREE Widgets ONLY**
- ❌ **FORBIDDEN**: HTML widget with custom code
- ❌ **FORBIDDEN**: Code widget with custom HTML/CSS
- ❌ **FORBIDDEN**: Shortcodes from third-party plugins (except approved form plugins)
- ❌ **FORBIDDEN**: Custom page builder blocks (Gutenberg/ACF/etc)
- ❌ **FORBIDDEN**: Custom CSS per element (PRO-only feature)
- ✅ **REQUIRED**: Use ONLY native Elementor FREE widgets
- ✅ **ALLOWED**: Elementor widget settings (padding, margin, colors, fonts)
- ✅ **ALLOWED**: Global Colors/Fonts via CSS variables (with polyfill)
- ✅ **EXCEPTION**: Theme-level PHP polyfills for FREE limitations (documented in SSOT)

**Elementor FREE Available Widgets** (29 total):
- Basic: Heading, Text Editor, Image, Video, Button, Divider, Spacer
- Media: Image Box, Icon, Icon Box, Image Carousel, Icon List
- Special: Counter, Progress Bar, Testimonial, Google Maps
- Interactive: Tabs, Accordion, Toggle, Social Icons, Alert, Rating
- Forms: NONE (use Contact Form 7 or WPForms plugin as shortcode)

**Elementor PRO Widgets NOT Available**:
- ❌ Call to Action widget (use Image Box + Button)
- ❌ Price List/Price Table (use styled Text Editor)
- ❌ Animated Headline (use Heading with CSS)
- ❌ Countdown Timer
- ❌ Elementor Forms (use CF7/WPForms)
- ❌ Posts/Portfolio widgets
- ❌ Advanced Carousels

**Why**: Client must be able to edit ALL content in Elementor UI. Custom HTML breaks this principle.

**2. Architecture: Legacy Sections (NOT Flexbox Containers)**
- ⚠️ **CRITICAL UPDATE**: Flexbox Containers are PRO-only!
- ✅ **MUST USE**: Legacy structure: Section > Column > Widget
- ❌ **DO NOT USE**: `elType: 'container'` (will fail in FREE)
- ✅ **STRUCTURE**: Section → Column → Widget (mandatory wrapper)
- ✅ **FULL-WIDTH**: Use `stretch_section: 'section-stretched'` setting
- ✅ **NESTING**: Avoid inner sections (performance cost)

**Example Correct Structure**:
```json
{
  "elType": "section",
  "settings": {
    "stretch_section": "section-stretched",
    "layout": "full_width"
  },
  "elements": [
    {
      "elType": "column",
      "settings": {"_column_size": 100},
      "elements": [/* widgets here */]
    }
  ]
}
```

**3. Design System Compliance (with Polyfill)**
- ✅ Use CSS variables: `var(--e-global-color-primary)` in JSON
- ✅ Global Colors defined:
  - Primary: #FABA29 (Yellow/Gold)
  - Secondary: #4F9F8B (Teal/Green)
  - Text: #2C2C2C (Dark Gray)
  - Accent: #FEFCF5 (Warm Cream)
- ✅ **POLYFILL REQUIRED**: `wp-content/themes/twentytwentyfive/inc/elementor-global-colors-polyfill.php`
- ✅ Loaded in `functions.php` (line 143)
- ✅ Use Global Fonts (system fonts in FREE)
- ❌ NO !important CSS
- ❌ NO hardcoded hex values in JSON

**4. CSS Print Method: Internal Embedding (Local Dev)**
- ✅ **REQUIRED FOR LOCAL**: Set to "Internal Embedding"
- ✅ **LOCATION**: WP Admin > Elementor > Settings > Performance
- ✅ **WHY**: Fixes caching issues on .local domains
- ✅ **EFFECT**: Embeds CSS in <head> instead of external files
- ⚠️ **PRODUCTION**: Change back to "External File" for performance

**5. Design Flexibility vs Fidelity**
- ✅ Overall style MUST remain consistent with reference
- ✅ Can adapt design to fit native Elementor FREE widgets
- ✅ Colors, spacing, typography MUST match design system
- ❌ Do NOT force exact pixel-perfect replica if widget doesn't support it
- ✅ Prioritize: Editability > Pixel-perfect accuracy
- ✅ Prioritize: Maintainability > Pixel-perfect accuracy

### No Fallback Principle

**From wizard-v2:**
- Agents MUST escalate problems, not work around them
- NO guessing or silent failures
- Stuck agent is mandatory escalation point
- Transparency over speed

### Research Protocol (R.JINA API)

**Stuck agent has access to r.jina for research:**

**API Access:**
- URL: `https://r.jina.ai/[target-url]`
- Auth: Bearer token (stored in config.json)
- Usage: Search official docs, GitHub repos, Stack Overflow

**Research Priority:**
1. **Official docs first** (developers.elementor.com, developer.wordpress.org)
2. **GitHub second** (working implementations, proven code)
3. **Stack Overflow third** (specific solutions with upvotes)
4. **NEVER**: Random blog posts, tutorials, opinion pieces

**Example Search Pattern:**
```bash
curl -H "Authorization: Bearer [token]" \
  "https://r.jina.ai/https://developers.elementor.com/docs/..."
```

**When to use r.jina:**
- Finding Elementor best practices
- Researching MCP tool capabilities
- Discovering proven automation patterns
- Verifying API methods and syntax

### Performance Budget

**Target Metrics** (Flexbox Containers):
- Containers: ≤10 per page
- Nested Containers: ≤3 levels
- Widgets: ≤30 per page
- Lighthouse Performance: 90+ (ideal: 95+)

**If budget exceeded:**
- Replace multiple primitive widgets with specialized widgets
- Use Icon Box instead of Icon + Heading + Text
- Use Call to Action instead of Image + Heading + Text + Button
- Use Carousel instead of multiple Image widgets

### Accessibility Requirements (WCAG 2.1 AA)

**MANDATORY:**
- ALT text on ALL images (descriptive, not "image1.jpg")
- Color contrast 4.5:1 minimum (normal text), 3:1 (large text)
- Keyboard navigation functional (Tab key works)
- Proper heading hierarchy (H1 → H2 → H3, no skips)
- ARIA labels for icon-only buttons
- Form labels (not just placeholders)

**Target**: Lighthouse Accessibility Score 90+

---

## 🛠️ MCP Tools Available

**Server**: `wp-elementor-mcp` (Standard Mode, 32 tools)
**Auth**: WordPress Application Password
**Base URL**: `http://svetlinkelementor.local`

### Key Tools

**Page Management:**
- `create_page` - Create WordPress page
- `update_page` - Update page
- `list_pages` - List all pages

**Elementor Structure:**
- `create_elementor_section` - Add section to page
- `create_elementor_column` - Add column to section
- `add_widget_to_section` - Add widget (heading, text, image, button, etc.)

**Global Design:**
- `update_elementor_global_colors` - Set color palette
- `update_elementor_global_fonts` - Set typography
- `get_elementor_page_data` - Retrieve page JSON
- `update_elementor_page_data` - Modify page structure

**Media:**
- `upload_media` - Upload images
- `list_media` - List uploaded media

---

## 📝 TodoWrite Usage

**CRITICAL**: Use TodoWrite for EVERY multi-step task

### When to Create Todos

- User requests page creation (3+ steps)
- Complex configuration tasks
- Multi-page projects
- After agent reports completion (mark done)

### Todo Format

```javascript
{
  content: "Create home page via MCP",
  activeForm: "Creating home page via MCP",
  status: "in_progress" // or "pending", "completed"
}
```

### Example Todo Flow

```
[1. Create home page structure via coder agent] - in_progress
[2. Test home page visually via tester agent] - pending
[3. Fix any visual issues found] - pending
[4. Deploy to production] - pending
```

**Mark completed IMMEDIATELY after each step** - don't batch!

---

## 🤖 Agent Invocation

### Using Task Tool

```javascript
// Invoke orchestrator to route task
Task({
  description: "Route page creation request",
  prompt: "User wants to create a home page with hero section, two-column content, and CTA. Route to appropriate agent.",
  subagent_type: "general-purpose"
});

// Invoke coder directly (if orchestrator determined this is correct)
Task({
  description: "Create home page via MCP",
  prompt: "Create home page with: 1) Hero section (H1 + text, Global colors), 2) Two-column section (image + text), 3) CTA section (button). Use MCP tools. Report page_id when done.",
  subagent_type: "general-purpose"
});

// Invoke tester after coder completes
Task({
  description: "Test home page visually",
  prompt: "Test page at http://svetlinkelementor.local/home. Take screenshots (desktop/tablet/mobile), verify Global Colors applied, check for console errors. Report findings.",
  subagent_type: "general-purpose"
});
```

---

## 🔍 When to Escalate to Stuck Agent

Automatically escalate when:
- MCP tools fail or return errors
- Page doesn't look correct after creation
- Global Colors/Fonts not applying
- Uncertain how to proceed
- Any agent reports being blocked

**Never guess or work around issues** - escalate!

---

## 🎯 Task Priorities

**Priority framework for project planning:**

### P1 - CRITICAL (Must Have Now)
□ Global Colors configured (no hardcoded colors)
□ Global Fonts configured (no hardcoded fonts)
□ MCP connection working
□ Basic page creation via AI functional
□ No !important CSS in codebase
□ CSS Print Method = Internal Embedding (for .local dev)

### P2 - HIGH (Should Have)
□ Reusable templates created
□ Minimal custom CSS (scoped and documented)
□ Visual testing with Playwright after each page
□ Responsive design verified (mobile/tablet/desktop)
□ No inline styles (use Global settings)

### P3 - MEDIUM (Nice to Have)
□ Performance optimization (Lighthouse 90+)
□ Accessibility enhancements (WCAG 2.1 AA)
□ Advanced animations and interactions

### P4 - LOW (Post-Launch)
□ SEO configuration (RankMath, meta tags)
□ Advanced interactions (hover effects, parallax)
□ Code documentation and comments
□ Production deployment optimization

**Note**: Focus on P1-P2 during initial build. P3-P4 come after site is functional.

---

## 📊 Progress Reporting

**ALWAYS show user clear progress:**

```
🔄 CURRENT PROGRESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Task: Create Home Page
👤 Agent: Coder Agent (via MCP)
⚡ Status: 🔄 In Progress
➡️  Next: Tester Agent (visual verification)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎨 Design System Reference

**Global Color Palette** (from SSOT/svetlinkelementor-rebuild-guide.md):
- Primary: #6366f1 (Indigo - CTA buttons, links)
- Secondary: #F5A623 (Svetlinki Orange - headings, accents)
- Text: #2c2c2c (Dark text - body content)
- Accent: #FDB913 (Light Orange - hover states)
- Background: #fefcf5 (Warm White - page backgrounds)

**Typography Scale:**
- H1: 2.75rem (44px) - clamp(2rem, 5vw, 2.75rem)
- H2: 1.9rem (30.4px) - clamp(1.5rem, 4vw, 1.9rem)
- H3: 1.4rem (22.4px) - clamp(1.2rem, 3vw, 1.4rem)
- Body: 1rem (16px)
- Line-height: 1.7 (body), 1.2 (headings)

---

## 📁 Documentation Location

**SSOT Folder** (Single Source of Truth):
```
C:\Users\denit\Local Sites\svetlinki3\SSOT\
├── elementor-mcp-solution.md (MCP setup guide)
├── svetlinkelementor-rebuild-guide.md (Design system & build guide)
└── kadence-to-elementor-migration-strategy.md (Migration analysis)
```

**Agent Configuration:**
```
C:\Users\denit\Local Sites\svetlinki3\New folder\
├── .claude\
│   ├── CLAUDE.md (this file)
│   └── agents\
│       ├── orchestrator.md
│       ├── coder.md
│       ├── tester.md
│       └── stuck.md
└── AGENT-CONFIGURATION-SUMMARY.md (setup summary)
```

---

## ⚡ Quick Start Checklist

When starting a new page creation task:

1. ☐ Create todos with TodoWrite
2. ☐ Invoke orchestrator agent to determine routing
3. ☐ Invoke coder agent with specific page requirements
4. ☐ Monitor coder agent progress (page_id returned)
5. ☐ Invoke tester agent for visual verification
6. ☐ If issues found → invoke stuck agent
7. ☐ Mark todos complete as you go
8. ☐ Report final result to user with URLs

---

## 🎓 Example Complete Workflow

```
User: "Create a home page with hero section"

You: [Creates todos via TodoWrite]
1. Create home page structure via coder agent
2. Test page visually with Playwright via tester agent
3. Fix any issues found

You: [Analyzes keywords: "create" → coder agent]

You: [Invokes coder via Task tool]
Task → "Create home page with hero section (H1 + text + CTA button).
       Use Global Colors. Report page_id when done."

Coder: "Page created. ID: 123. URL: /home"

You: [Marks todo #1 complete, invokes tester]
Task → "Test page at http://svetlinkelementor.local/home.
       Take screenshots (desktop/tablet/mobile), verify Global Colors."

Tester: "✅ All tests pass. Screenshots attached. No console errors."

You: [Marks todo #2 complete]

You → User: "✅ Home page created and tested successfully!
📄 URL: http://svetlinkelementor.local/home
🎨 Elementor Editor: http://svetlinkelementor.local/wp-admin/post.php?post=123&action=elementor"
```

---

## 🔧 Known Issues & Critical Solutions (Added 2025-11-29)

### Issue #1: Global Colors Not Showing (White Background)
**Symptom**: Colors appear as defaults despite correct JSON
**Cause**: Elementor FREE doesn't output Global Colors as CSS variables
**Solution**: PHP polyfill already created at `wp-content/themes/twentytwentyfive/inc/elementor-global-colors-polyfill.php`
**Status**: ✅ SOLVED - Polyfill active

### Issue #2: Stretch Section Not Working (Section Not Full-Width)
**Symptom**: Section shows 645px instead of 1920px despite `stretch_section: 'section-stretched'`
**Cause**: CSS Print Method = External File causes caching on .local domains
**Solution**: Change to "Internal Embedding" at WP Admin > Elementor > Settings > Performance
**Status**: ✅ SOLVED - Setting configured

### Issue #3: REST API Updates Not Applying
**Symptom**: JSON updates to `_elementor_data` don't appear on frontend
**Cause**: REST API bypasses Elementor's save hooks
**Solution**: After REST API update, open page in Elementor editor and click "Update"
**Status**: ⚠️ WORKAROUND - Manual step required

### Issue #4: Flexbox Containers Don't Work
**Symptom**: `elType: 'container'` renders incorrectly
**Cause**: Containers are Elementor PRO feature only
**Solution**: Use legacy structure: Section > Column > Widget
**Status**: ✅ DOCUMENTED - Use Sections

### Issue #5: Header Footer Elementor Templates Not REST API Accessible
**Symptom**: Cannot update header/footer templates via REST API
**Cause**: Custom post type `elementor-hf` not registered with REST API
**Solution**: Create JSON export files and import manually in Elementor editor
**Status**: ⚠️ WORKAROUND - Manual import required

**FULL REFERENCE**: See `SSOT/ISSUES-AND-SOLUTIONS-GUIDE.md` for complete troubleshooting

---

## 🚨 Remember

1. **Context Isolation**: Agents receive fresh context via Task tool
2. **No Fallback Principle**: Escalate problems, don't work around
3. **TodoWrite**: Use for every multi-step task
4. **Mark Complete**: Immediately after each step
5. **Visual Testing**: Always test after page creation
6. **Clean Code**: Enforce Global Colors/Fonts, no hardcoding
7. **Report Progress**: Keep user informed with clear status

---

## 📞 Escalation Path

```
Coder Agent encounters issue
    ↓
Escalates to Stuck Agent
    ↓
Stuck Agent researches via r.jina
    ↓
    ├─→ Solution found → Continue workflow
    └─→ Uncertain → You ask user for guidance
```

---

**Mantra**:
> "Coordinate agents, track todos, enforce clean code principles, escalate uncertainty."

**Location**: `.claude/CLAUDE.md`
**Last Updated**: 2025-11-29
