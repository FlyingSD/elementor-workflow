# WordPress Elementor MCP Solutions for Claude Code

## Executive Summary

This document outlines MCP (Model Context Protocol) server solutions that enable Claude Code to programmatically create WordPress pages with Elementor. These solutions ensure pages remain fully customizable by users and won't break on WordPress/Elementor updates.

**Last Updated:** November 28, 2025

---

## Top Recommendation: wp-elementor-mcp by alex-daiz

**GitHub Repository:** https://github.com/alex-daiz/wp-elementor-mcp
**NPM Package:** https://www.npmjs.com/package/wp-elementor-mcp

### Why This is the Best Solution

1. **Most Comprehensive** - Offers 20-34 tools across 4 configuration modes
2. **Fully Tested** - 100% schema validation, comprehensive test suite
3. **Production Ready** - Type-safe, thoroughly documented, actively maintained
4. **Scalable** - Start simple (Essential mode) and scale up to Advanced/Full modes
5. **NPM Package Available** - Easy to install via `npx wp-elementor-mcp`

### Key Features

- Create/update/delete pages and posts via WordPress REST API
- Build Elementor sections, containers, columns, and widgets programmatically
- Full CRUD operations on Elementor data structures
- Performance optimized with incremental updates
- Chunked data loading for large pages
- Smart caching system with automatic invalidation
- Works with both Elementor Free and Elementor Pro
- Content discovery with Elementor status indicators

### Configuration Modes

| Mode | Tools | Best For | Use Case |
|------|-------|----------|----------|
| **Essential** | 20 | Learning, basic tasks | Basic WordPress + Elementor operations |
| **Standard** | 32 | Most users (recommended) | Page building + element management |
| **Advanced** | 34 | Power users | Performance tools + advanced operations |
| **Full** | 34 | Pro workflows | Everything including Pro features |

---

## Installation & Setup Guide

### Step 1: Generate WordPress Application Password

1. Log into WordPress Admin Dashboard
2. Navigate to **Users → Profile**
3. Scroll to **Application Passwords** section
4. Enter name: "Claude Code MCP"
5. Click **Add New Application Password**
6. **Copy the generated password immediately** (format: `xxxx xxxx xxxx xxxx xxxx xxxx`)
   - You cannot view this password again after closing the window
   - Store it securely

### Step 2: Configure Claude Code MCP Settings

Edit your Claude Code configuration file:

**macOS Location:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows Location:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Configuration JSON:**

```json
{
  "mcpServers": {
    "elementor-wordpress": {
      "command": "npx",
      "args": ["wp-elementor-mcp"],
      "env": {
        "ELEMENTOR_MCP_MODE": "standard",
        "WORDPRESS_BASE_URL": "https://yoursite.com",
        "WORDPRESS_USERNAME": "your-username",
        "WORDPRESS_APPLICATION_PASSWORD": "xxxx xxxx xxxx xxxx xxxx xxxx"
      }
    }
  }
}
```

**Configuration Options:**

```javascript
// Mode Selection
ELEMENTOR_MCP_MODE: "essential"   // 20 tools - Basic operations
ELEMENTOR_MCP_MODE: "standard"    // 32 tools - Page building (default)
ELEMENTOR_MCP_MODE: "advanced"    // 34 tools - Performance tools
ELEMENTOR_MCP_MODE: "full"        // 34 tools - Pro features

// Quick Shortcuts
ELEMENTOR_MINIMAL_MODE: true      // Same as essential mode
ELEMENTOR_ENABLE_ALL: true        // Same as full mode

// Individual Feature Toggles (Optional)
ELEMENTOR_ENABLE_TEMPLATES: true
ELEMENTOR_ENABLE_PERFORMANCE: true
```

### Step 3: Set WordPress User Permissions

Ensure your WordPress user account has the following capabilities:

- ✅ Create/edit/delete posts
- ✅ Create/edit/delete pages
- ✅ Upload media files
- ✅ Access Elementor data
- ✅ REST API access (enabled by default in WordPress 5.6+)

### Step 4: Restart Claude Code

After updating the configuration file, restart Claude Code to load the MCP server.

---

## Available Tools by Mode

### Always Available (1 tool)
- `configure_wordpress` - Manual WordPress connection setup

### Essential Mode (+19 tools)

**WordPress Operations:**
- `get_posts` - List all posts with pagination
- `get_post` - Get specific post details
- `create_post` - Create new post
- `update_post` - Update existing post
- `get_pages` - List all pages with pagination
- `create_page` - Create new page
- `update_page` - Update existing page
- `get_media` - List media library items
- `upload_media` - Upload media files
- `list_all_content` - Content discovery with Elementor status

**Basic Elementor:**
- `get_elementor_templates` - Get available templates
- `get_elementor_data` - Get page Elementor data
- `update_elementor_data` - Update page Elementor data
- `get_elementor_widget` - Get specific widget
- `update_elementor_widget` - Update specific widget
- `get_elementor_elements` - List all elements
- `update_elementor_section` - Update section settings
- `get_elementor_data_chunked` - Get data in chunks
- `backup_elementor_data` - Backup page data
- `clear_elementor_cache` - Clear Elementor cache

### Standard Mode (+12 tools)

**Section & Container Creation:**
- `create_elementor_section` - Create sections with columns
- `create_elementor_container` - Create Flexbox containers
- `add_column_to_section` - Add columns to sections
- `duplicate_section` - Clone sections with content

**Widget Management:**
- `add_widget_to_section` - Add widgets to containers
- `insert_widget_at_position` - Insert at specific positions
- `clone_widget` - Duplicate widgets
- `move_widget` - Move widgets between containers

**Element Operations:**
- `delete_elementor_element` - Remove elements safely
- `reorder_elements` - Change element order
- `copy_element_settings` - Copy settings between elements

**Page Analysis:**
- `get_page_structure` - Get simplified page overview

### Advanced Mode (+2 tools)

**Performance:**
- `clear_elementor_cache_by_page` - Page-specific cache clearing

**Advanced Operations:**
- `find_elements_by_type` - Search elements by type

### Full Mode (+0 new tools, enables Pro features)

Currently implemented as stubs - requires Elementor Pro integration:
- Template management capabilities
- Global color and font settings
- Custom field integration
- Revision and history features

---

## How It Works: Technical Deep Dive

### Elementor Data Storage Architecture

Elementor stores page layouts as JSON data in WordPress meta fields:

**Core Meta Fields:**

1. **`_elementor_data`** (text/longtext)
   - Main JSON structure containing all sections, columns, widgets
   - Hierarchical structure: Section → Column → Widget
   - Each element has unique ID, type, and settings
   - Example structure:
     ```json
     [
       {
         "id": "abc123",
         "elType": "section",
         "elements": [
           {
             "id": "def456",
             "elType": "column",
             "elements": [
               {
                 "id": "ghi789",
                 "elType": "widget",
                 "widgetType": "heading",
                 "settings": {
                   "title": "Welcome"
                 }
               }
             ]
           }
         ]
       }
     ]
     ```

2. **`_elementor_edit_mode`** (string)
   - Set to `"builder"` for Elementor-managed pages
   - Tells WordPress this page uses Elementor

3. **`_elementor_template_type`** (string)
   - Page type identifier
   - Common values: `"wp-page"`, `"wp-post"`, `"elementor_library"`

4. **`_elementor_version`** (string)
   - Elementor version used to create the page
   - Used for compatibility checks

5. **`_elementor_controls_usage`** (serialized array)
   - Tracks which widgets/controls are used
   - Used for performance optimization

### Why Pages Remain Customizable After Creation

1. **Standard WordPress Storage**
   - Uses native WordPress `wp_postmeta` table
   - No custom tables or proprietary storage
   - Fully compatible with WordPress backup/restore tools

2. **REST API Integration**
   - All operations use official WordPress REST API
   - Authentication via WordPress Application Passwords
   - Same API Elementor uses internally

3. **Native Elementor Format**
   - Creates data in Elementor's exact JSON format
   - No conversion or translation needed
   - Elementor editor reads and writes same structure

4. **No Lock-in**
   - Pages can be edited in Elementor editor immediately
   - All visual editing tools work normally
   - Users can modify, duplicate, or delete as usual

5. **Update-Safe**
   - Survives WordPress core updates
   - Survives Elementor plugin updates
   - No dependency on specific Elementor versions

### WordPress REST API Endpoints Used

The MCP server interacts with these endpoints:

```
GET    /wp-json/wp/v2/posts              # List posts
GET    /wp-json/wp/v2/posts/{id}         # Get post
POST   /wp-json/wp/v2/posts              # Create post
PUT    /wp-json/wp/v2/posts/{id}         # Update post
DELETE /wp-json/wp/v2/posts/{id}         # Delete post

GET    /wp-json/wp/v2/pages              # List pages
GET    /wp-json/wp/v2/pages/{id}         # Get page
POST   /wp-json/wp/v2/pages              # Create page
PUT    /wp-json/wp/v2/pages/{id}         # Update page
DELETE /wp-json/wp/v2/pages/{id}         # Delete page

GET    /wp-json/wp/v2/media              # List media
POST   /wp-json/wp/v2/media              # Upload media
```

**Authentication Method:**
```http
Authorization: Basic base64(username:application_password)
```

---

## Example Usage with Claude Code

Once configured, you can use natural language to create and manage WordPress/Elementor content:

### Example 1: Create Basic Page

**Prompt:**
```
Create a new WordPress page titled "About Us" with a professional layout
```

**What Claude Code Will Do:**
1. Use `create_page` tool to create the WordPress page
2. Set title and basic metadata
3. Set `_elementor_edit_mode` to "builder"
4. Return page ID and URL

### Example 2: Build Complex Elementor Layout

**Prompt:**
```
Create a new page called "Services" with Elementor. Add a hero section with a heading "Our Services" and a button "Get Started". Below that, add a 3-column section with icons and descriptions for our three main services.
```

**What Claude Code Will Do:**
1. Create the page using `create_page`
2. Use `create_elementor_section` to add hero section
3. Use `add_widget_to_section` to add heading widget
4. Configure heading widget settings
5. Add button widget with custom text
6. Create second section with 3 columns
7. Add icon widgets and text widgets to each column
8. Return complete page structure

### Example 3: Update Existing Content

**Prompt:**
```
On page ID 123, find all heading widgets and change their color to blue (#0066cc)
```

**What Claude Code Will Do:**
1. Use `get_elementor_elements` to list all elements
2. Use `find_elements_by_type` to filter heading widgets
3. For each heading, use `update_elementor_widget` to change color
4. Clear cache using `clear_elementor_cache_by_page`
5. Confirm updates completed

### Example 4: Performance-Optimized Update

**Prompt:**
```
Update only the call-to-action button text on page 67 to say "Start Your Free Trial" without loading the entire page
```

**What Claude Code Will Do:**
1. Use `get_elementor_elements` to find button widget ID
2. Use `update_elementor_widget` with specific widget ID
3. Perform incremental update (no full page load)
4. Return updated widget settings

---

## Alternative Solutions

### Option 2: aguaitech/Elementor-MCP (Simpler)

**GitHub:** https://github.com/aguaitech/Elementor-MCP
**NPM Package:** `elementor-mcp`
**Stars:** 18+ stars
**Status:** Actively maintained

**Best For:**
- Simpler use cases
- Getting started quickly
- Basic CRUD operations

**Features:**
- Basic WordPress page/post management
- Elementor data read/write operations
- Template support
- Environment-based configuration

**Installation:**

```json
{
  "mcpServers": {
    "Elementor MCP": {
      "command": "npx",
      "args": ["-y", "elementor-mcp"],
      "env": {
        "WP_URL": "https://url.of.target.website",
        "WP_APP_USER": "wordpress_username",
        "WP_APP_PASSWORD": "Appl icat ion_ Pass word"
      }
    }
  }
}
```

**Windows Installation:**

```json
{
  "mcpServers": {
    "Elementor MCP": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "elementor-mcp"],
      "env": {
        "WP_URL": "https://url.of.target.website",
        "WP_APP_USER": "wordpress_username",
        "WP_APP_PASSWORD": "Appl icat ion_ Pass word"
      }
    }
  }
}
```

### Option 3: blibbers/elementor-mcp (Multi-Site)

**GitHub:** https://github.com/blibbers/elementor-mcp

**Best For:**
- Managing multiple WordPress sites
- Multi-client agencies
- Site network management

**Features:**
- Multi-site configuration support
- 6 core tools (list_sites, list_pages, get_page, create_page, update_page, get_elementor_data)
- Environment-based site management
- REST API integration

**Available Tools:**
1. `list_sites` - List all configured WordPress sites
2. `list_pages` - List pages from a specific site
3. `get_page` - Get page details
4. `create_page` - Create new page with Elementor
5. `update_page` - Update existing page
6. `get_elementor_data` - Get Elementor-specific metadata

---

## Comparison Matrix

| Feature | wp-elementor-mcp | aguaitech/Elementor-MCP | blibbers/elementor-mcp |
|---------|------------------|-------------------------|------------------------|
| **Total Tools** | 20-34 (configurable) | ~15 tools | 6 tools |
| **Configuration Modes** | 4 modes | Single mode | Single mode |
| **Multi-Site Support** | No | No | Yes |
| **Performance Tools** | Yes (Advanced mode) | Limited | No |
| **Test Coverage** | 100% validated | Good | Basic |
| **Documentation** | Comprehensive | Good | Good |
| **Active Development** | Very Active | Active | Moderate |
| **NPM Package** | Yes | Yes | No |
| **TypeScript** | Yes | No | No |
| **Elementor Pro Support** | Planned (Full mode) | No | No |
| **Best For** | Production use, complex builds | Quick start, learning | Multi-site management |

---

## Security Best Practices

### 1. Application Password Management

- ✅ Create unique application password for Claude Code
- ✅ Use descriptive name: "Claude Code MCP - [Date]"
- ✅ Rotate passwords every 90 days
- ✅ Revoke unused passwords immediately
- ✅ Never commit passwords to version control
- ❌ Don't use your regular WordPress password

### 2. WordPress Site Security

- ✅ Use HTTPS for all WordPress sites in production
- ✅ Keep WordPress core updated
- ✅ Keep Elementor plugin updated
- ✅ Use strong passwords for WordPress accounts
- ✅ Enable WordPress security plugins (e.g., Wordfence)
- ✅ Implement IP whitelisting for REST API if possible
- ✅ Monitor API usage logs regularly

### 3. User Permission Management

- ✅ Create dedicated user for API access
- ✅ Assign minimum required permissions
- ✅ Use "Editor" role instead of "Administrator" if possible
- ✅ Review user capabilities regularly
- ❌ Don't use shared accounts

### 4. Configuration File Security

- ✅ Set proper file permissions on config files
- ✅ Use environment variables when possible
- ✅ Exclude config files from backups if they contain passwords
- ✅ Use `.gitignore` to prevent config file commits

### 5. Network Security

- ✅ Use VPN for sensitive operations
- ✅ Implement rate limiting on WordPress REST API
- ✅ Monitor for unusual API traffic patterns
- ✅ Use Content Security Policy (CSP) headers
- ✅ Enable WordPress REST API authentication logs

### 6. Monitoring & Auditing

- ✅ Enable WordPress activity logs
- ✅ Monitor API call frequency and patterns
- ✅ Set up alerts for suspicious activity
- ✅ Regular security audits of API access
- ✅ Review Elementor data modifications periodically

---

## Troubleshooting Guide

### Issue 1: Connection Errors

**Symptoms:**
- "Connection refused"
- "Failed to connect to WordPress"
- Timeout errors

**Solutions:**

1. **Verify WordPress URL**
   ```bash
   curl https://yoursite.com/wp-json/wp/v2/posts
   ```
   Should return JSON response with post data

2. **Check REST API Status**
   - Visit: `https://yoursite.com/wp-json/`
   - Should see JSON with API routes
   - If 404, REST API may be disabled

3. **Test Application Password**
   ```bash
   curl -u "username:xxxx xxxx xxxx xxxx xxxx xxxx" \
     https://yoursite.com/wp-json/wp/v2/posts
   ```
   Should authenticate successfully

4. **Check Firewall Rules**
   - Verify server firewall allows REST API access
   - Check WordPress security plugins for REST API blocks
   - Whitelist your IP address if needed

### Issue 2: 404 Errors / "No Elementor Data Found"

**Symptoms:**
- "No Elementor data found for this page"
- 404 when accessing Elementor endpoints
- Empty data returned

**Solutions:**

1. **Verify Elementor is Installed**
   - Check WordPress Admin → Plugins
   - Ensure Elementor is activated
   - Update to latest version

2. **Check Page/Post Has Elementor Data**
   ```bash
   curl -u "username:password" \
     "https://yoursite.com/wp-json/wp/v2/pages/{id}?context=edit"
   ```
   Look for `meta._elementor_data` in response

3. **Use Content Discovery Tool**
   - Use `list_all_content` tool to see which pages have Elementor
   - Look for ✅ indicator for Elementor-enabled pages

4. **Verify Edit Context**
   - Ensure API calls include `?context=edit` parameter
   - This enables full meta field access

5. **Check Meta Field Permissions**
   - User must have `edit_posts` capability
   - Meta fields must be registered for REST API

**See Full Troubleshooting Guide:**
https://github.com/alex-daiz/wp-elementor-mcp/blob/main/TROUBLESHOOTING.md

### Issue 3: Authentication Failures

**Symptoms:**
- "Unauthorized" or 401 errors
- "Invalid credentials"
- "Forbidden" or 403 errors

**Solutions:**

1. **Regenerate Application Password**
   - Delete old application password
   - Create new one
   - Update configuration immediately

2. **Verify Username Format**
   - Use WordPress username (not email)
   - Username is case-sensitive
   - No spaces in username

3. **Check Application Password Format**
   - Keep spaces in password: `xxxx xxxx xxxx xxxx`
   - Some clients require no spaces: `xxxxxxxxxxxxxxxx`
   - Try both formats

4. **Verify User Permissions**
   ```php
   // Check user capabilities
   $user = get_user_by('login', 'username');
   if ($user->has_cap('edit_posts')) {
       echo 'Has permission';
   }
   ```

### Issue 4: Too Many/Too Few Tools

**Symptoms:**
- Expected 32 tools but seeing 20
- Tool count doesn't match mode
- Missing specific tools

**Solutions:**

1. **Check Configuration Mode**
   ```bash
   npm run test:config
   ```
   Displays current mode and tool count

2. **Verify Environment Variables**
   - Check `ELEMENTOR_MCP_MODE` is set correctly
   - Ensure no typos in mode name
   - Try different mode explicitly

3. **Start with Essential Mode**
   ```json
   "env": {
     "ELEMENTOR_MINIMAL_MODE": "true"
   }
   ```
   Reduces to 20 core tools

4. **Clear NPM Cache**
   ```bash
   npm cache clean --force
   npx clear-npx-cache
   npx wp-elementor-mcp
   ```

### Issue 5: Performance Issues / Timeouts

**Symptoms:**
- Slow response times
- Timeout errors
- High memory usage

**Solutions:**

1. **Use Essential or Standard Mode**
   - Reduces tool count and overhead
   - Standard mode (32 tools) is recommended balance

2. **Enable Incremental Updates**
   - Use `update_elementor_widget` for single widget changes
   - Avoid `update_elementor_data` for small changes
   - Use chunked loading for large pages

3. **Clear Cache Regularly**
   - Use `clear_elementor_cache` tool
   - Clear WordPress object cache
   - Clear Elementor CSS cache

4. **Monitor Tool Usage**
   ```bash
   npm run test:comprehensive
   ```
   Shows performance metrics for each tool

5. **Optimize WordPress**
   - Enable caching plugin (WP Rocket, W3 Total Cache)
   - Optimize database tables
   - Increase PHP memory limit
   - Use PHP 8.0+ for better performance

---

## Migration Guide

### From Previous MCP Implementations

If you're currently using a different WordPress MCP solution:

**Step 1: Backup Current Configuration**
```bash
# macOS
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup

# Windows
copy %APPDATA%\Claude\claude_desktop_config.json ^
     %APPDATA%\Claude\claude_desktop_config.json.backup
```

**Step 2: Test New Server**
```bash
npx wp-elementor-mcp
```

**Step 3: Update Configuration**
Replace old server config with new one (see Installation section)

**Step 4: Verify Tools**
```bash
npm run test:config
```

### Recommended Upgrade Path

1. **Start with Essential Mode**
   - 20 tools for basic operations
   - Familiarize yourself with core features
   - Test on development site first

2. **Upgrade to Standard Mode**
   - Add page building capabilities
   - Learn section and widget creation
   - Practice with sample layouts

3. **Try Advanced Mode**
   - Include performance tools
   - Use incremental updates
   - Optimize workflows

4. **Use Full Mode** (Optional)
   - Only with Elementor Pro license
   - Enable template features
   - Advanced integrations

---

## Programmatic Approach (Alternative to MCP)

If you prefer direct code implementation without MCP:

### Using WordPress REST API Directly

```php
// Create page with Elementor data
$page_data = [
    'title' => 'My New Page',
    'status' => 'publish',
    'content' => '', // Empty content for Elementor pages
    'meta' => [
        '_elementor_edit_mode' => 'builder',
        '_elementor_template_type' => 'wp-page',
        '_elementor_version' => '3.16.0',
        '_elementor_data' => json_encode([
            [
                'id' => wp_generate_uuid4(),
                'elType' => 'section',
                'settings' => [],
                'elements' => [
                    [
                        'id' => wp_generate_uuid4(),
                        'elType' => 'column',
                        'settings' => ['_column_size' => 100],
                        'elements' => [
                            [
                                'id' => wp_generate_uuid4(),
                                'elType' => 'widget',
                                'widgetType' => 'heading',
                                'settings' => [
                                    'title' => 'Welcome to My Site',
                                    'header_size' => 'h1'
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ])
    ]
];

// Using WordPress REST API
$response = wp_remote_post('https://yoursite.com/wp-json/wp/v2/pages', [
    'headers' => [
        'Authorization' => 'Basic ' . base64_encode('username:app_password'),
        'Content-Type' => 'application/json'
    ],
    'body' => json_encode($page_data)
]);
```

### Using Python

```python
import requests
import json
import uuid

def create_elementor_page(base_url, username, app_password, title):
    endpoint = f"{base_url}/wp-json/wp/v2/pages"

    # Create Elementor data structure
    elementor_data = [
        {
            'id': str(uuid.uuid4()),
            'elType': 'section',
            'settings': {},
            'elements': [
                {
                    'id': str(uuid.uuid4()),
                    'elType': 'column',
                    'settings': {'_column_size': 100},
                    'elements': [
                        {
                            'id': str(uuid.uuid4()),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': 'Welcome',
                                'header_size': 'h1'
                            }
                        }
                    ]
                }
            ]
        }
    ]

    # Page data
    page_data = {
        'title': title,
        'status': 'publish',
        'content': '',
        'meta': {
            '_elementor_edit_mode': 'builder',
            '_elementor_template_type': 'wp-page',
            '_elementor_data': json.dumps(elementor_data)
        }
    }

    # Send request
    response = requests.post(
        endpoint,
        auth=(username, app_password),
        json=page_data
    )

    return response.json()

# Usage
result = create_elementor_page(
    'https://yoursite.com',
    'username',
    'xxxx xxxx xxxx xxxx',
    'My New Page'
)
print(f"Page created with ID: {result['id']}")
```

### Using JavaScript/Node.js

```javascript
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

async function createElementorPage(baseUrl, username, appPassword, title) {
    const endpoint = `${baseUrl}/wp-json/wp/v2/pages`;

    // Create Elementor data structure
    const elementorData = [
        {
            id: uuidv4(),
            elType: 'section',
            settings: {},
            elements: [
                {
                    id: uuidv4(),
                    elType: 'column',
                    settings: { _column_size: 100 },
                    elements: [
                        {
                            id: uuidv4(),
                            elType: 'widget',
                            widgetType: 'heading',
                            settings: {
                                title: 'Welcome',
                                header_size: 'h1'
                            }
                        }
                    ]
                }
            ]
        }
    ];

    // Page data
    const pageData = {
        title: title,
        status: 'publish',
        content: '',
        meta: {
            _elementor_edit_mode: 'builder',
            _elementor_template_type: 'wp-page',
            _elementor_data: JSON.stringify(elementorData)
        }
    };

    // Send request
    const response = await axios.post(endpoint, pageData, {
        auth: {
            username: username,
            password: appPassword
        }
    });

    return response.data;
}

// Usage
createElementorPage(
    'https://yoursite.com',
    'username',
    'xxxx xxxx xxxx xxxx',
    'My New Page'
).then(result => {
    console.log(`Page created with ID: ${result.id}`);
});
```

---

## Additional Resources

### MCP Protocol & Marketplaces

- **Official MCP Specification:** https://spec.modelcontextprotocol.io/
- **MCP Servers Repository:** https://github.com/modelcontextprotocol/servers
- **Cline MCP Marketplace:** https://github.com/cline/mcp-marketplace
- **Awesome MCP Servers:** https://github.com/wong2/awesome-mcp-servers

### WordPress Development

- **WordPress REST API Handbook:** https://developer.wordpress.org/rest-api/
- **WordPress REST API Reference:** https://developer.wordpress.org/rest-api/reference/
- **Application Passwords Guide:** https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/

### Elementor Development

- **Elementor Developers Documentation:** https://developers.elementor.com/
- **Elementor GitHub Repository:** https://github.com/elementor/elementor
- **Elementor Community Forum:** https://github.com/elementor/elementor/discussions

### Related WordPress MCP Projects

- **WordPress MCP Adapter:** https://github.com/WordPress/mcp-adapter
- **Automattic WordPress MCP:** https://github.com/Automattic/wordpress-mcp
- **WordPress MCP Server:** https://github.com/stefans71/wordpress-mcp-server

---

## Frequently Asked Questions (FAQ)

### Q: Will pages created via MCP break when WordPress/Elementor updates?

**A:** No. The MCP servers use standard WordPress REST API and store data in Elementor's native format. Pages created programmatically are identical to pages created manually in Elementor editor.

### Q: Can users edit pages after they're created by Claude Code?

**A:** Yes. Pages remain fully editable in Elementor's visual editor. Users can modify, duplicate, or delete content without any issues.

### Q: Do I need Elementor Pro?

**A:** No. All solutions work with free Elementor. Elementor Pro features are optional and only available in "Full" mode of wp-elementor-mcp.

### Q: Can I use this with custom post types?

**A:** Yes. The REST API approach works with any post type that supports the REST API and Elementor.

### Q: Is this safe for production sites?

**A:** Yes, with proper security measures:
- Use HTTPS
- Rotate application passwords regularly
- Monitor API usage
- Keep WordPress and Elementor updated

### Q: How do I handle media/images?

**A:** Use the `upload_media` tool to upload images first, then reference the media ID in widget settings.

### Q: Can I import/export entire page layouts?

**A:** Yes. Export Elementor data as JSON, store it, and import to other pages using `update_elementor_data`.

### Q: What's the performance impact?

**A:** Minimal. MCP servers use WordPress REST API which is optimized for performance. Use incremental updates and caching for best performance.

### Q: Can I manage multiple WordPress sites?

**A:** Yes. Configure multiple MCP server instances with different site credentials, or use blibbers/elementor-mcp which has built-in multi-site support.

### Q: What if I need custom Elementor widgets?

**A:** Custom widgets work if they're registered with Elementor. The MCP server treats them like standard widgets - just use the widget type name in the data structure.

---

## Support & Community

### Getting Help

1. **GitHub Issues:**
   - wp-elementor-mcp: https://github.com/alex-daiz/wp-elementor-mcp/issues
   - aguaitech/Elementor-MCP: https://github.com/aguaitech/Elementor-MCP/issues

2. **Documentation:**
   - Full configuration guide included with each package
   - Troubleshooting guides in repository READMEs

3. **Community:**
   - MCP Discord servers
   - WordPress support forums
   - Elementor community forums

### Contributing

Contributions are welcome! Check each repository's contribution guidelines:
- Fork the repository
- Create a feature branch
- Add tests for new features
- Update documentation
- Submit a pull request

---

## Changelog & Version History

### v1.6.1 (wp-elementor-mcp)
- Enhanced error handling with informative messages
- New `list_all_content` tool for content discovery
- Improved debugging with console logging
- Better WordPress integration with `context: 'edit'`
- Comprehensive test suite added

### v1.5.0 (wp-elementor-mcp)
- Added configuration modes (Essential, Standard, Advanced, Full)
- Performance optimizations
- Modular tool loading
- Enhanced documentation

---

## License

All mentioned MCP servers are open source:
- **wp-elementor-mcp:** MIT License
- **aguaitech/Elementor-MCP:** MIT License
- **blibbers/elementor-mcp:** MIT License

---

## Conclusion

The MCP server approach provides a robust, production-ready solution for programmatically creating WordPress pages with Elementor through Claude Code. The wp-elementor-mcp package by alex-daiz is the most comprehensive option with excellent documentation, testing, and scalability.

**Recommended Setup for Production:**
- Use wp-elementor-mcp in Standard mode (32 tools)
- Generate dedicated application password
- Enable HTTPS on WordPress site
- Monitor API usage regularly
- Keep WordPress and Elementor updated

**Quick Start for Testing:**
- Use aguaitech/Elementor-MCP for simpler setup
- Test on development/staging site first
- Start with Essential mode
- Scale up as needed

Both approaches ensure pages remain fully editable by users and won't break on updates.

---

**Document Version:** 1.0
**Last Updated:** November 28, 2025
**Author:** Research compiled for Svetlinki3 project
**Location:** C:\Users\denit\Local Sites\svetlinki3\SSOT\
