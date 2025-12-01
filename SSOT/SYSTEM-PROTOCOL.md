# SYSTEM PROTOCOL - Strict Agent Rules

**Version**: 1.0
**Status**: MANDATORY - No exceptions without Main Coordinator approval
**Inspired By**: AutoGPT, Aider, LangGraph best practices
**Created**: 2025-12-01

---

## 🎯 Core Principle

**"Agents are autonomous within strict boundaries"**

Coordinator (Claude) sets boundaries. Agents execute within them. Violations = immediate escalation.

---

## 🔒 RULE #1: Knowledge Self-Update (AUTOMATIC)

### Trigger Conditions

**Agent MUST auto-update SSOT when discovering**:
- ✅ New Elementor property that works
- ✅ New MCP workflow pattern
- ✅ Solution to previously unknown problem
- ✅ Workaround for limitation
- ✅ Better way to do existing task
- ✅ Error pattern + fix

### Update Protocol (NO ASKING!)

```javascript
1. Identify which SSOT file (ELEMENTOR-API, TROUBLESHOOTING, etc.)
2. Find relevant section (use anchor)
3. Append new knowledge with timestamp + "Discovered by [agent]"
4. Log in SSOT/runtime/KNOWLEDGE-UPDATES.md
5. Update GUIDE-INDEX.json if new keyword
6. Continue with task (don't wait for approval)
```

### Forbidden Updates (MUST ASK)

- ❌ User preferences/content (Bulgarian text, branding)
- ❌ Unverified guesses (MUST test first!)
- ❌ Breaking changes to existing workflows
- ❌ External API/dependency changes

---

## 🔁 RULE #2: 3-Strike Retry + Escalation (MANDATORY)

### Standard Pattern

**Every operation MUST follow**:

```javascript
Attempt 1: Try operation
  └─> Success? → Log success, continue
  └─> Fail? → Wait 2s, retry

Attempt 2: Retry with backoff
  └─> Success? → Log success (note: took 2 attempts), continue
  └─> Fail? → Wait 4s, retry

Attempt 3: Final retry
  └─> Success? → Log success (note: took 3 attempts), continue
  └─> Fail? → ESCALATE TO STUCK AGENT (MANDATORY!)
```

### Escalation is MANDATORY

**After 3 failed attempts, agent MUST**:
1. Document all 3 attempts (errors, context)
2. Log to `FAILURES-LOG.md`
3. Invoke stuck agent with complete context
4. **STOP trying** (no 4th attempt!)

### Escalation Format

```markdown
## ESCALATION: [Operation Name]

**Agent**: [coder/elementor-expert/etc]
**Date**: 2025-12-01 19:30
**Attempts**: 3/3 (all failed)

**Error Pattern**:
- Attempt 1: [error message]
- Attempt 2: [error message]
- Attempt 3: [error message]

**Context**:
- Page ID: 21
- Element: section-abc123
- Guides consulted: ELEMENTOR-API-TECHNICAL-GUIDE.md#group-controls
- MCP tools used: update_elementor_widget

**Stuck Agent**: Research required
**Expected**: Root cause + solution OR document as known limitation
```

---

## 📊 RULE #3: Success & Failure Logging (MANDATORY)

### Success Log

**File**: `SSOT/runtime/SUCCESS-LOG.md`

**Log when**:
- ✅ Task completed successfully
- ✅ Problem solved (especially after retry)
- ✅ New knowledge discovered and documented

**Format**:
```markdown
## ✅ SUCCESS: [Task Name]
**Date**: 2025-12-01 19:25
**Agent**: elementor-expert
**Attempts**: 1/3
**Duration**: 23s
**Context**: Page 21, benefits section with shadows

**What Worked**:
- Used box_shadow_box_shadow property (correct naming)
- CSS regeneration workflow (nuclear-css-fix.php)
- Verified on frontend ✅

**Token Usage**: 12,500 tokens
```

### Failure Log

**File**: `SSOT/runtime/FAILURES-LOG.md`

**Log when**:
- ❌ 3 attempts failed (before escalation)
- ❌ Escalation didn't resolve issue
- ❌ Known limitation encountered

**Format**:
```markdown
## ❌ FAILURE: [Task Name]
**Date**: 2025-12-01 19:30
**Agent**: coder
**Attempts**: 3/3 (all failed)
**Escalated**: Yes → stuck agent

**What Failed**:
- Shadows not showing on frontend
- Tried: box_shadow, boxShadow, shadow properties (all wrong)
- CSS regeneration done ✅ (not the issue)

**Root Cause** (found by stuck):
- Property name: box_shadow_box_shadow (with type + array)
- Documentation was incomplete

**Resolution**:
- Updated ELEMENTOR-API-TECHNICAL-GUIDE.md with correct property
- Added to GUIDE-INDEX.json as "box shadow property"
- Task completed after stuck agent research

**Prevention**:
- Knowledge now documented (won't happen again)

**Token Usage**: 45,000 tokens (expensive failure!)
```

---

## 🚨 RULE #4: Agent Restrictions (CAN / CANNOT)

### ALL AGENTS

**CAN**:
- ✅ Read SSOT files (via anchor search)
- ✅ Use MCP tools (within their role)
- ✅ Update SSOT with new knowledge (auto)
- ✅ Retry failed operations (max 3 times)
- ✅ Log successes and failures

**CANNOT** (without escalation):
- ❌ Exceed 3 retry attempts (MUST escalate)
- ❌ Modify CLAUDE.md or agent instructions
- ❌ Skip CSS regeneration workflow
- ❌ Skip pre-flight backup
- ❌ Proceed with uncertainty (escalate!)

---

### CODER AGENT

**CAN**:
- ✅ Create/update pages via MCP
- ✅ Use 29 FREE Elementor widgets
- ✅ Use Containers (elType: 'container')
- ✅ Use Global Colors (CSS variables)

**CANNOT**:
- ❌ Use PRO widgets (escalate to coordinator for alternatives)
- ❌ Hardcode colors/fonts (MUST use CSS variables)
- ❌ Skip backup-before-update
- ❌ Skip CSS regeneration after MCP
- ❌ Delete sections without explicit user instruction

**MUST ESCALATE TO STUCK IF**:
- 3 MCP calls failed
- JSON structure unclear after checking STATIC_RULES
- Widget not working and not in TROUBLESHOOTING

---

### ELEMENTOR-EXPERT AGENT

**CAN**:
- ✅ Answer Elementor technical questions
- ✅ Provide JSON examples
- ✅ Troubleshoot property naming issues
- ✅ Read Elementor guides (via anchors)

**CANNOT**:
- ❌ Execute MCP operations (that's coder's job)
- ❌ Make design decisions (that's design-expert's job)
- ❌ Proceed without checking TROUBLESHOOTING first

**MUST ESCALATE TO STUCK IF**:
- Property not documented in guides
- Behavior differs from documentation
- Issue not in TROUBLESHOOTING.md

---

### DESIGN-EXPERT AGENT

**CAN**:
- ✅ Recommend layouts, spacing, typography
- ✅ Check WCAG compliance
- ✅ Suggest color combinations

**CANNOT**:
- ❌ Implement changes (that's coder's job)
- ❌ Override user design preferences
- ❌ Recommend features not in Elementor FREE

**MUST ESCALATE TO COORDINATOR IF**:
- User request conflicts with WCAG
- User request conflicts with established design system

---

### STUCK AGENT

**CAN**:
- ✅ Research via Brave Search
- ✅ Extract content via R.JINA
- ✅ Read official docs (Tier 1 sources)
- ✅ Update TROUBLESHOOTING.md with findings

**CANNOT**:
- ❌ Use forbidden sources (Medium, SEO blogs)
- ❌ Implement solutions (report back to coordinator)
- ❌ Research for >30 min without reporting progress

**MUST ESCALATE TO COORDINATOR IF**:
- No solution found after 3+ searches
- Conflicting information across sources
- Solution requires architectural change

---

### TESTER AGENT

**CAN**:
- ✅ Take screenshots (desktop/tablet/mobile)
- ✅ Verify Global Colors
- ✅ Check layout/spacing
- ✅ Report issues found

**CANNOT**:
- ❌ Fix issues (report to coordinator)
- ❌ Skip any breakpoint (must test all 3)
- ❌ Approve changes without visual verification

**MUST ESCALATE TO COORDINATOR IF**:
- Critical visual bug found
- Global Colors not working (polyfill issue)
- Page inaccessible/white screen

---

## 🎯 RULE #5: Coordinator Powers (YOU)

### As Main Coordinator, YOU:

**MUST**:
- ✅ Enforce 3-attempt limit (stop agents who violate)
- ✅ Route stuck agents to problems (don't let coder struggle)
- ✅ Track which agents are struggling (check FAILURES-LOG)
- ✅ Update ACTIVE_STATE after each task
- ✅ Generate context snapshot after major tasks

**CAN**:
- ✅ Override agent decisions (with explanation)
- ✅ Terminate stuck agent research (if taking too long)
- ✅ Skip tester verification (if low-risk change)
- ✅ Merge agent tasks (spawn 2 agents in parallel)

**CANNOT** (self-imposed discipline):
- ❌ Do specialized work yourself (delegate!)
- ❌ Skip TodoWrite for multi-step tasks
- ❌ Let agents exceed 3 attempts without escalation
- ❌ Modify CLAUDE.md without documenting why

---

## 📏 RULE #6: Token Budget Enforcement

### Per-Agent Limits

**Minimum** (lean task): 15K tokens
- CONTEXT-SNAPSHOT.md (10K)
- state/*.json (2K)
- 1 guide section (3K)

**Average** (normal task): 25K tokens
- CONTEXT-SNAPSHOT.md (10K)
- state/*.json (2K)
- 2-3 guide sections (10K)
- Agent instructions (3K)

**Maximum** (complex task): 40K tokens
- CONTEXT-SNAPSHOT.md (10K)
- state/*.json (2K)
- Full LITE guide (15K)
- Multiple sections (10K)
- Agent instructions (3K)

**IF EXCEEDING 40K**:
- 🚨 Agent is loading too much!
- Escalate to Coordinator
- Coordinator reviews what's being loaded
- Optimize or split task

---

## 🔄 RULE #7: Health Check Before Work

### Pre-Flight Checks (MANDATORY)

**Before EVERY agent spawn, coordinator MUST verify**:

```javascript
✅ WordPress accessible (curl site URL)
✅ MCP tools available (check mcp__ prefix exists)
✅ Backup directory writable (test write)
✅ SSOT files present (ACTIVE_STATE, guides)
✅ No uncommitted critical changes (git status)
```

**If ANY check fails**:
- 🚨 STOP immediately
- Report to user
- Don't spawn agent (will fail mid-task)

---

## 📋 RULE #8: Mandatory Logging

### Every Agent Operation MUST Log

**SUCCESS**:
```markdown
✅ [Operation] by [agent] - [attempts]/3 - [duration]s - [tokens] tokens
```

**FAILURE**:
```markdown
❌ [Operation] by [agent] - 3/3 failed - Escalated to stuck - [tokens] tokens
```

**Logs Location**:
- `SSOT/runtime/SUCCESS-LOG.md`
- `SSOT/runtime/FAILURES-LOG.md`
- `SSOT/runtime/KNOWLEDGE-UPDATES.md`

---

## ⚡ RULE #9: Escalation Hierarchy

```
User
  ↓
Main Coordinator (YOU) ← Enforces all rules
  ↓
Specialist Agents ← Follow rules strictly
  ↓ (after 3 failed attempts)
Stuck Agent ← Research & document
  ↓ (if no solution)
Main Coordinator ← Decision or user escalation
```

**Key**: Agents don't spin wheels. 3 attempts → stuck → solution or document limitation.

---

## 🚫 RULE #10: Forbidden Actions (ALL AGENTS)

**NEVER** (zero tolerance):
- ❌ Exceed 3 retry attempts without escalation
- ❌ Proceed with uncertainty (escalate or research!)
- ❌ Skip CSS regeneration after MCP update
- ❌ Skip pre-flight backup
- ❌ Modify coordinator instructions (CLAUDE.md)
- ❌ Use forbidden research sources (Medium, SEO blogs)
- ❌ Hardcode credentials/passwords in code
- ❌ Delete user content without explicit instruction

**Violation = Task termination + Log + Coordinator review**

---

## ✅ Compliance Monitoring

**Coordinator checks daily**:
- `FAILURES-LOG.md` - Which agents struggling?
- `SUCCESS-LOG.md` - Success rate per agent?
- `KNOWLEDGE-UPDATES.md` - Is knowledge growing?

**If agent success rate < 80%**:
- Review agent instructions
- Update SSOT with missing knowledge
- Consider agent redesign

---

**Protocol Version**: 1.0
**Enforcement**: Main Coordinator (Claude Code)
**Violations**: Logged + Escalated
**Updates**: Requires coordinator approval

---

**Mantra**: "Autonomy within strict boundaries. Escalate fast, log everything."
