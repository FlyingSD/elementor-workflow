# MCP Server Configuration for Svetlinki Project

**Last Updated**: 2025-11-30
**Status**: PRODUCTION READY

---

## 📦 INSTALLED MCP SERVERS

### 1. **wp-elementor-mcp** (WordPress/Elementor Automation)

**Purpose**: Create and manage WordPress pages with Elementor programmatically

**GitHub**: https://github.com/Huetarded/wp-elementor-mcp
**NPM**: Not published (use local installation)
**Local Path**: `C:\Users\denit\wp-elementor-mcp\`

**Configuration**:
```json
{
  "wp-elementor-mcp": {
    "command": "node",
    "args": ["C:\\Users\\denit\\wp-elementor-mcp\\dist\\index.js"],
    "env": {
      "ELEMENTOR_MCP_MODE": "standard",
      "WORDPRESS_BASE_URL": "http://svetlinkielementor.local",
      "WORDPRESS_USERNAME": "test",
      "WORDPRESS_APPLICATION_PASSWORD": "S27q64rqoFhfTPDA30nBhNM5"
    }
  }
}
```

**Mode**: Standard (32 tools available)

**Available Tools**:
- `create_elementor_section` - Create sections with columns
- `add_widget_to_section` - Add widgets to containers
- `get_elementor_data` - Get page Elementor data
- `update_elementor_data` - Update page Elementor data
- `clear_elementor_cache_by_page` - Clear page-specific cache
- `create_page` - Create new WordPress page
- `update_page` - Update existing page
- `get_pages` - List all pages
- `upload_media` - Upload images/files
- Plus 23 more...

**Status**: ✅ Installed locally and configured (needs Claude Code restart)

**Installation**: Cloned from GitHub and built locally at `C:\Users\denit\wp-elementor-mcp\`

---

### 2. **brave-search** (Web Research)

**Purpose**: Search the web for documentation and solutions

**Configuration**:
```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "BSALRthHC5TjPLZ-kA70Dk7YqhCfhmC"
    }
  }
}
```

**Status**: ✅ Working (used by stuck agent)

**Usage**: Research Elementor issues, find documentation, Stack Overflow answers

---

### 3. **json-schema-validator** (JSON Validation) 🆕

**Purpose**: Validate Elementor JSON structures before deployment

**GitHub**: https://github.com/EienWolf/jsonshema_mcp

**Installation Location**: `C:\Users\denit\jsonshema_mcp\`

**Configuration**:
```json
{
  "json-schema-validator": {
    "command": "python",
    "args": ["C:\\Users\\denit\\jsonshema_mcp\\mcp_server.py"]
  }
}
```

**Available Tools**:
- `generate_schema` - Create JSON schema from example data
- `validate_json_schema` - Validate JSON against schema
- `add_update_schema` - Store reusable schemas
- `validate_json_from_collections` - Validate using stored schemas
- `list_schemas` - List available schemas

**Status**: ✅ Installed and configured (needs Claude Code restart)

**Use Cases**:
1. Validate Elementor JSON before sending to WordPress
2. Prevent malformed data from breaking pages
3. Create reusable component schemas (sections, widgets)
4. Audit existing pages for structure issues

---

### 4. **Playwright** (Browser Automation)

**Purpose**: Take screenshots, test pages visually

**Status**: ✅ Working (used by tester agent)

**Available Tools**:
- `browser_navigate` - Navigate to URL
- `browser_snapshot` - Take accessibility snapshot
- `browser_take_screenshot` - Capture screenshots
- `browser_click` - Click elements
- Plus 15 more...

---

## 🔧 CONFIGURATION FILE LOCATION

**Windows**:
```
C:\Users\denit\Local Sites\svetlinkielementor\.mcp.json
```

**Full Configuration**:
```json
{
  "mcpServers": {
    "wp-elementor-mcp": {
      "command": "npx",
      "args": ["wp-elementor-mcp"],
      "env": {
        "ELEMENTOR_MCP_MODE": "standard",
        "WORDPRESS_BASE_URL": "http://svetlinkielementor.local",
        "WORDPRESS_USERNAME": "test",
        "WORDPRESS_APPLICATION_PASSWORD": "S27q64rqoFhfTPDA30nBhNM5"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "BSALRthHC5TjPLZ-kA70Dk7YqhCfhmC"
      }
    },
    "json-schema-validator": {
      "command": "python",
      "args": ["C:\\Users\\denit\\jsonshema_mcp\\mcp_server.py"]
    }
  }
}
```

---

## 🚀 ACTIVATION INSTRUCTIONS

After modifying `.mcp.json`:

1. **Save the file**
2. **Restart Claude Code completely** (close and reopen)
3. **Wait 10-15 seconds** for MCP servers to initialize
4. **Check available tools** (tools will appear with `mcp__` prefix)

---

## 🔍 TROUBLESHOOTING

### Issue: wp-elementor-mcp tools not appearing

**Symptoms**: No `mcp__wp-elementor__*` tools available

**Possible Causes**:
1. Package not installed globally
2. Claude Code not restarted after config change
3. MCP server startup error

**Solutions**:
```bash
# Try installing globally
npm install -g wp-elementor-mcp

# Or use REST API directly (current workaround)
# Works fine via coder agent
```

### Issue: json-schema-validator not loading

**Symptoms**: No `mcp__json-schema__*` tools after restart

**Solutions**:
1. Check Python installation: `python --version` (need 3.8+)
2. Verify dependencies: `cd C:\Users\denit\jsonshema_mcp && python -m pip list`
3. Test server manually: `python C:\Users\denit\jsonshema_mcp\mcp_server.py`
4. Check Claude Code logs for MCP errors

---

## 📚 USAGE EXAMPLES

### Example 1: Validate Elementor Section JSON

```javascript
// Create section structure
const heroSection = {
  id: "hero-123",
  elType: "section",
  settings: {
    background_color: "var(--e-global-color-accent)",
    padding: { unit: "px", top: "80", right: "20", bottom: "80", left: "20" }
  },
  elements: [
    {
      id: "col-456",
      elType: "column",
      settings: { _column_size: 100 },
      elements: []
    }
  ]
};

// Validate before sending to WordPress
const validation = await validate_json_schema({
  json_data: JSON.stringify(heroSection),
  schema: elementorSectionSchema
});

if (validation.is_valid) {
  // Safe to create page
  create_elementor_section({
    page_id: 21,
    settings: heroSection.settings,
    columns: 1
  });
} else {
  console.error("Invalid JSON:", validation.errors);
}
```

### Example 2: Research via Brave Search

```javascript
// Find Elementor documentation
brave_search({
  query: "site:developers.elementor.com global colors"
});

// Find solutions on Stack Overflow
brave_search({
  query: "site:stackoverflow.com elementor rest api create section"
});
```

### Example 3: Take Page Screenshot

```javascript
// Navigate and screenshot
await browser_navigate({
  url: "http://svetlinkielementor.local"
});

await browser_take_screenshot({
  filename: "homepage-current.png",
  fullPage: true
});
```

---

## 🎯 RECOMMENDED WORKFLOW

### Phase 1: Planning
1. Design page structure (sections, widgets)
2. Create JSON schemas for components (one-time setup)

### Phase 2: Building
1. Construct Elementor JSON
2. **Validate with json-schema-validator** ← Prevents errors!
3. Send to WordPress via wp-elementor-mcp or REST API
4. Clear Elementor cache

### Phase 3: Testing
1. Screenshot via Playwright
2. Visual verification
3. Fix issues if found

### Phase 4: Deployment
1. Final validation
2. Publish page
3. Test on live site

---

## 📖 REFERENCE DOCUMENTATION

**Detailed guides in archive**:
- `SSOT/archive/merged-sources/JSON-GENERATION-TOOLS-GUIDE.md` - Complete JSON MCP guide
- `SSOT/archive/deprecated-docs/elementor-mcp-solution.md` - wp-elementor-mcp documentation
- `SSOT/archive/merged-sources/MCP-PAGE-CREATION-CHECKLIST.md` - Workflow checklist

---

## ✅ NEXT STEPS

1. **Restart Claude Code** to load json-schema-validator
2. **Create Elementor component schemas**:
   - Section schema
   - Column schema
   - Widget schemas (heading, text-editor, button, icon-box, etc.)
3. **Test validation workflow** on existing pages
4. **Integrate into coder agent workflow**

---

**Version**: 1.0
**Status**: Production Ready
**Last Updated**: 2025-11-30
