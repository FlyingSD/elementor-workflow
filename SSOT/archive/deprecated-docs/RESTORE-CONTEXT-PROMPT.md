# RESTORE CONTEXT: Elementor AI Automation Project

## 🎯 Project Objective
Building a **wizard-v2 multi-agent system** to programmatically create WordPress pages using **Elementor** via **MCP (Model Context Protocol)**. The system automates page creation from reference screenshots while maintaining clean code principles and a Global Design System.

---

## 📁 Key File Locations

**Agent Configurations**:
- `.claude/CLAUDE.md` - Orchestrator directives (main entry point)
- `.claude/agents/orchestrator.md` - Task routing & delegation
- `.claude/agents/stuck.md` - Problem-solving & research
- `.claude/agents/coder.md` - MCP page creation
- `.claude/agents/designer.md` - Design system compliance
- `.claude/agents/tester.md` - Playwright visual testing
- `.claude/agents/qa.md` - 21 comprehensive tests
- `AGENT-CONFIGURATION-SUMMARY.md` - Complete agent documentation (7/7 agents)

**WordPress Site**:
- **URL**: http://svetlinkielementor.local
- **Admin**: http://svetlinkielementor.local/wp-admin (test/test)
- **MCP Config**: `C:\Users\denit\Local Sites\svetlinkielementor\.mcp.json`
- **Site Folder**: `C:\Users\denit\Local Sites\svetlinkielementor\`

**Reference Screenshots**:
- Location: `C:\Users\denit\Local Sites\svetlinkielementor\2025-11-26-current-state\`
- Contains: Current Kadence site screenshots for design reference

**SSOT (Single Source of Truth)**:
- `C:\Users\denit\Local Sites\svetlinki3\SSOT\svetlinkelementor-rebuild-guide.md`

---

## 🎨 Elementor Global Design System

**Global Colors** (configured in Elementor):
```css
Primary:    #6366f1 (Indigo)     → var(--e-global-color-primary)
Secondary:  #F5A623 (Orange)     → var(--e-global-color-secondary)
Text:       #2c2c2c (Dark Gray)  → var(--e-global-color-text)
Accent:     #FDB913 (Light Gold) → var(--e-global-color-accent)
Background: #fefcf5 (Warm White) → var(--e-global-color-background)
```

**Global Fonts Typography Scale**:
- H1: 2.75rem (44px) - clamp(2rem, 5vw, 2.75rem)
- H2: 1.9rem (30.4px) - clamp(1.5rem, 4vw, 1.9rem)
- H3: 1.4rem (22.4px) - clamp(1.2rem, 3vw, 1.4rem)
- Body: 1rem (16px)

**CRITICAL RULE**: NO hardcoded hex colors or font names - ONLY CSS variables!

---

## 🤖 Agent System Architecture

**Wizard-v2 Pattern**:
- **Orchestrator**: Routes tasks to specialized agents via Task tool
- **Agents work in isolation**: Each agent spawned via Task tool with specific prompt
- **NO direct agent-to-agent communication**: All coordination through Orchestrator
- **Context preservation**: Each agent receives complete context in spawn prompt

**Agent Roles**:
1. **Orchestrator** - Task routing, delegation, progress tracking
2. **Stuck** - Research via r.jina, problem-solving, escalation
3. **Coder** - MCP page creation, Elementor JSON generation
4. **Designer** - Design system compliance, visual consistency verification
5. **Tester** - Playwright screenshots, visual verification
6. **QA** - 21 comprehensive tests before deployment
7. **CLAUDE.md** - Main orchestration entry point

---

## 🔧 MCP Configuration

**MCP Server**: `wp-elementor-mcp` (npm package)
**Authentication**:
- Base URL: http://svetlinkielementor.local
- Username: test
- Password: S27q 64rq oFhf TPDA 30nB hNM5 (Application Password)

**Key MCP Tools Available**:
- `create_elementor_page` - Create new pages with Elementor content
- `update_elementor_page` - Modify existing pages
- `get_elementor_page_data` - Retrieve page JSON
- `list_elementor_pages` - List all pages

---

## 🔍 R.JINA Research API

**API Key**: `jina_700485007fde405aba61e94002ee4a10M3Ueq3DucEcT73UKdsVUbcvGWDPU`

**Usage Pattern**:
```bash
curl -H "Authorization: Bearer jina_700485007fde405aba61e94002ee4a10M3Ueq3DucEcT73UKdsVUbcvGWDPU" \
  "https://r.jina.ai/[URL]"
```

**Allowed Sources**:
- ✅ developers.elementor.com
- ✅ developer.wordpress.org
- ✅ GitHub repositories
- ❌ Random blogs/tutorials

---

## ⚠️ Core Principles

### No Fallback Principle
- **NEVER** create workarounds (e.g., `!important`, inline styles)
- **NEVER** guess solutions
- **ALWAYS** research via r.jina (official docs first)
- **ALWAYS** escalate to Stuck agent if uncertain

### Clean Code Standards
- ✅ Use Global Colors (CSS variables)
- ✅ Use Global Fonts (CSS variables)
- ✅ Minimal inline styles
- ✅ Semantic HTML structure
- ❌ NO hardcoded hex colors
- ❌ NO hardcoded font names
- ❌ NO `!important` CSS

---

## 📊 Current Progress

**Pages Created** (as of last session):
- ✅ Page 21: Home (ACTIVE at /) - 5 Elementor sections
- ✅ Page 23: About (/about/)
- ✅ Page 25: Programs (/programs/)
- ✅ Page 27: Contact (/contact/)
- ✅ Page 29: FAQ (/faq/)
- ✅ Page 31: Blog (/blog/)
- ✅ Page 33: Privacy Policy (/privacy-policy-2/)
- ✅ Page 35: Terms of Service (/terms-of-service/)

**Agent Configuration**: 7/7 core agents complete (100%)

**WordPress Front Page**: Page 21 set as homepage

---

## 🚀 Quick Start Commands

**Check current pages**:
```bash
curl -s -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/wp/v2/pages?_fields=id,title,slug,status&per_page=20&orderby=date&order=desc"
```

**Check WordPress settings**:
```bash
curl -s -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/wp/v2/settings" | python -m json.tool > C:\tmp\wp-settings.json
```

**Check recent file changes**:
```bash
dir "C:\Users\denit\Local Sites\svetlinkielementor\app\public\wp-content\uploads\elementor\css\" /O-D /T:W
```

---

## 📖 Typical Workflow

1. **User requests page creation** → Orchestrator routes to appropriate agents
2. **Designer analyzes reference screenshot** → Extracts design patterns
3. **Coder creates page via MCP** → Uses Global Design System
4. **Tester captures screenshots** → Verifies visual output
5. **QA runs 21 tests** → Ensures compliance before deployment
6. **Stuck handles blockers** → Researches solutions via r.jina

---

## 🎯 When You Resume

1. Read `AGENT-CONFIGURATION-SUMMARY.md` for complete agent docs
2. Check WordPress settings and recent pages
3. Review `.claude/CLAUDE.md` for orchestration directives
4. If blocked, spawn Stuck agent for research
5. Always use TodoWrite to track multi-step tasks

---

**Version**: Elementor v4.0 AI Automation
**Architecture**: Wizard-v2 Multi-Agent System
**Status**: PRODUCTION READY (7/7 agents configured)

---

## 🔑 Key Mantras

> "No hardcoded values, ever. Global Design System is law."

> "If uncertain, research. If research is unclear, escalate."

> "Agents work in isolation. Orchestrator coordinates. Context flows downward."

> "Clean code or no code. No fallbacks, no workarounds, no shortcuts."
