# ⚠️ MANDATORY CSS REGENERATION WORKFLOW ⚠️

**CRITICAL**: Read this EVERY TIME before using MCP to update Elementor pages!

---

## 🚨 THE FUNDAMENTAL PROBLEM

**MCP/REST API updates = Database changes ONLY**
- Updates `_elementor_data` in WordPress database ✅
- Does NOT trigger Elementor CSS regeneration ❌
- Does NOT trigger `wp_enqueue_scripts` hook ❌
- Does NOT update CSS files ❌

**Result**:
- Editor shows changes ✅
- Frontend does NOT show changes ❌
- User sees old styling ❌

---

## ✅ MANDATORY WORKFLOW (NO EXCEPTIONS!)

**After EVERY MCP update, you MUST run CSS regeneration:**

### **Method 1: Web API Endpoint (RECOMMENDED)**

```bash
# Single command - handles both CSS clearing and regeneration
curl -s "http://svetlinkielementor.local/regenerate-css-api.php?page=21&secret=svetlinki2024"

# Then visit page to ensure CSS is applied
curl -s "http://svetlinkielementor.local/" > nul
```

**Why this works:**
- ✅ Clears Elementor cache
- ✅ Deletes CSS metadata
- ✅ Updates post modification time
- ✅ Calls `$document->save()` (triggers hooks!)
- ✅ Regenerates CSS file
- ✅ All in one request

**Script location**: `app/public/regenerate-css-api.php`

### **Method 2: Alternative (if API fails)**

```bash
# Step 1: Nuclear CSS fix (deletes all CSS, forces regeneration)
curl -s "http://svetlinkielementor.local/nuclear-css-fix.php"

# Step 2: Visit page to trigger CSS generation
curl -s "http://svetlinkielementor.local/home" > nul
```

---

## 📋 COMPLETE MCP UPDATE CHECKLIST

**EVERY TIME you use MCP tools, follow this exact sequence:**

```bash
# 1. BACKUP (always!)
mcp__wp-elementor-mcp__backup_elementor_data --post_id 21

# 2. UPDATE (your changes)
mcp__wp-elementor-mcp__update_elementor_widget --post_id 21 --widget_id "benefits005" --widget_settings {...}

# 3. CSS REGENERATION (MANDATORY!) - Use Web API
curl -s "http://svetlinkielementor.local/regenerate-css-api.php?page=21&secret=svetlinki2024"
curl -s "http://svetlinkielementor.local/" > nul

# 4. VERIFY (check in NEW incognito window)
# Open: http://svetlinkielementor.local/ in fresh incognito window
# Or use Playwright for automated verification
```

**Important Notes:**
- ✅ CSS regeneration is **NOT optional** - ALWAYS required after MCP updates
- ✅ Use the `regenerate-css-api.php` endpoint (more reliable than old methods)
- ✅ Always verify in NEW incognito window (avoid cached CSS)
- ✅ Changes in Elementor editor ≠ Changes on frontend (CSS must regenerate!)

---

## 🔴 COMMON MISTAKES (DON'T DO THESE!)

❌ **Mistake 1**: Update via MCP, then immediately check frontend
- **Result**: Changes not visible (CSS not regenerated yet)

❌ **Mistake 2**: Run only `clear_elementor_cache` tool
- **Result**: CSS deleted but not regenerated

❌ **Mistake 3**: Forget to visit page after clearing cache
- **Result**: CSS files remain deleted, page broken

❌ **Mistake 4**: Check in same browser without hard refresh
- **Result**: Browser shows cached CSS, not new CSS

---

## ✅ CORRECT WORKFLOW EXAMPLE

```bash
# User asks: "Add full borders to Benefits cards"

# Step 1: Backup
mcp__wp-elementor-mcp__backup_elementor_data(post_id: 21)

# Step 2: Update borders (5px top, 1px sides/bottom for emphasis)
mcp__wp-elementor-mcp__update_elementor_widget(
  post_id: 21,
  widget_id: "benefits005",
  widget_settings: {
    "border_width": {"unit": "px", "top": "5", "right": "1", "bottom": "1", "left": "1", "isLinked": false}
  }
)

# Step 3: MANDATORY CSS REGENERATION (Web API)
curl -s "http://svetlinkielementor.local/regenerate-css-api.php?page=21&secret=svetlinki2024"
curl -s "http://svetlinkielementor.local/" > nul

# Step 4: Verify in NEW incognito window
# Tell user: "✅ Borders updated! Check in NEW incognito: http://svetlinkielementor.local/"
```

---

## 🎯 WHY THIS HAPPENS (TECHNICAL)

**Normal Elementor Save Flow**:
```
User clicks "Update" → $document->save() → WordPress hooks fire → CSS regenerates ✅
```

**MCP/REST API Flow**:
```
MCP update → Database update only → NO hooks fire → CSS NOT regenerated ❌
```

**The Fix** (Web API Method):
```
MCP update → regenerate-css-api.php → Clears cache + Deletes CSS + $document->save() → Triggers hooks → CSS regenerates → Page visit ensures CSS applied ✅
```

**Why the Web API works better**:
- Single HTTP request handles all steps
- More reliable than running separate commands
- Provides feedback (success/error messages)
- Doesn't require PHP in system PATH

---

## 🔧 CSS REGENERATION SCRIPTS

### **Primary: regenerate-css-api.php (RECOMMENDED)**

**Location**: `app/public/regenerate-css-api.php`

**Usage**:
```bash
curl "http://svetlinkielementor.local/regenerate-css-api.php?page=21&secret=svetlinki2024"
```

**What it does**:
1. ✅ Security check (requires secret key)
2. ✅ Clears Elementor cache completely
3. ✅ Deletes CSS metadata for specific page
4. ✅ Updates post modification time
5. ✅ Gets CSS file manager and forces regeneration
6. ✅ Flushes WordPress object cache
7. ✅ Provides detailed feedback (success/error)

**Why this is better**:
- Single HTTP request (no separate commands needed)
- Page-specific (pass `?page=ID`)
- Security protected (secret key required)
- Detailed output for debugging
- Always works reliably

### **Fallback: nuclear-css-fix.php**

**Location**: `app/public/nuclear-css-fix.php`

**What it does**:
1. Updates post modification time (forces Elementor to notice changes)
2. Deletes ALL Elementor CSS meta (`_elementor_css%`)
3. Flushes WordPress cache
4. Saves document via `$document->save()` (triggers hooks!)
5. Regenerates CSS file structure

**Why "nuclear"?**
- Most aggressive approach (clears ALL pages, not just one)
- Deletes EVERYTHING CSS-related
- Forces complete rebuild
- Use when API method fails

---

## 📝 UPDATE YOUR TODO WORKFLOW

**When using TodoWrite, always include CSS regeneration step:**

```json
[
  {"content": "Update Benefits card borders", "status": "in_progress"},
  {"content": "Run CSS regeneration (MANDATORY!)", "status": "pending"},
  {"content": "Verify changes on frontend", "status": "pending"}
]
```

**Never mark update as "completed" until AFTER CSS regeneration!**

---

## 🚨 WHEN TO USE THIS

**ALWAYS use after these MCP operations:**

✅ `update_elementor_widget` - Any widget/column/section update
✅ `update_elementor_data` - Full page data update
✅ `update_elementor_section` - Section batch updates
✅ `create_elementor_section` - New section creation
✅ `add_widget_to_section` - Adding new widgets

**Basically: After ANY MCP write operation that changes page content/styling**

---

## 💡 ALTERNATIVE METHODS (LESS RELIABLE)

These alternatives exist but are NOT recommended:

**Method A**: Manual Elementor Update
- Open page in Elementor editor
- Click "Update" button
- Triggers all hooks properly ✅
- But requires manual intervention ❌

**Method B**: WP-CLI
```bash
wp elementor flush-css
wp elementor sync-library
```
- May not work on all setups ❌
- Not always available ❌

**Method C**: Switch CSS Print Method
- Change to "Internal" then back to "External"
- Unreliable ❌
- Doesn't always force regeneration ❌

**STICK WITH THE NUCLEAR FIX + PAGE VISIT METHOD** - it's the only one that works 100% of the time.

---

## 🎓 TEACHING THIS TO AGENTS

**In agent prompts, always include:**

```
After updating via MCP:
1. Run nuclear CSS fix: curl -s "http://svetlinkielementor.local/nuclear-css-fix.php"
2. Visit page: curl -s "http://svetlinkielementor.local/home" > nul
3. Wait 2 seconds for generation
4. Verify changes applied
```

---

## 📊 VERIFICATION CHECKLIST

After CSS regeneration, verify:

☑️ Nuclear CSS fix completed (✅ message shown)
☑️ Page visit triggered (curl returned successfully)
☑️ Screenshot shows changes OR
☑️ User confirms changes visible in fresh incognito window

**If changes NOT visible:**
- User's browser cache (even after incognito/refresh)
- Run nuclear fix AGAIN
- Try different browser entirely

---

## 🔄 VERSION HISTORY

**2025-11-30**: Initial documentation created after repeated CSS regeneration issues
- Issue: Borders not showing after MCP updates
- Root cause: REST API doesn't trigger Elementor hooks
- Solution: Nuclear CSS fix + page visit

---

**REMEMBER**: This is not optional. This is not "best practice". This is **MANDATORY**.

**No CSS regeneration = No visible changes = Frustrated user = Failed task**

---

**Location**: `SSOT/MANDATORY-CSS-REGENERATION.md`
**Status**: CRITICAL - Read before EVERY MCP operation
**Last Updated**: 2025-11-30
