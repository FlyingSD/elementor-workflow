# JSON Generation Tools Guide for Elementor Page Building

**Document Type**: Technical Reference & Integration Guide
**Date Created**: 2025-11-28
**Purpose**: Tools and strategies for generating Elementor JSON structures
**Research Source**: r.jina.ai web research (MCP servers, JSON tools)

---

## Table of Contents

1. [Overview](#overview)
2. [Recommended MCP Servers](#recommended-mcp-servers)
3. [JSON Schema Validator MCP](#json-schema-validator-mcp)
4. [JSON Manipulation MCP](#json-manipulation-mcp)
5. [Elementor JSON Structure Templates](#elementor-json-structure-templates)
6. [Workflow Integration](#workflow-integration)
7. [Usage Examples](#usage-examples)

---

## Overview

### The Challenge

Creating Elementor pages programmatically via MCP requires generating complex JSON structures:

```json
[
  {
    "id": "uuid",
    "elType": "section",
    "settings": { /* complex nested object */ },
    "elements": [ /* nested columns */ ]
  }
]
```

**Problems**:
- Manual JSON creation is error-prone
- Structure must be valid JSON Schema
- Elementor has specific required fields
- Deep nesting increases complexity
- Global Color/Font variables must be used correctly

### The Solution

Use specialized MCP servers to:
1. **Validate** JSON structure against schemas
2. **Generate** JSON from templates
3. **Manipulate** existing JSON structures
4. **Schema-validate** before sending to Elementor

---

## Recommended MCP Servers

### 1. JSON Schema Validator MCP ⭐ (BEST OPTION)

**Repository**: https://github.com/EienWolf/jsonshema_mcp
**Purpose**: Generate, validate, and manage JSON schemas
**Best For**: Creating Elementor JSON with validation

**Key Features**:
- ✅ Generate JSON schemas from example data
- ✅ Validate JSON against schemas
- ✅ Store schema collections
- ✅ Full JSON Schema Draft 2020-12 compliance
- ✅ Fallback to local file storage (no PostgreSQL required)

**Why This is Best for Svetlinki**:
- Can create Elementor JSON schema once, reuse for all pages
- Validates JSON before sending to WordPress
- Prevents malformed data from breaking pages
- Works offline with file storage

### 2. JSON Manipulation MCP (Alternative)

**Repository**: https://github.com/GongRzhe/JSON-MCP-Server
**Purpose**: Query and manipulate JSON via JSONPath
**Best For**: Modifying existing Elementor JSON

**Key Features**:
- ✅ JSONPath queries
- ✅ Filter, map, transform operations
- ✅ Array/object manipulation
- ✅ Aggregate functions

**Use Case for Svetlinki**:
- Extract sections from existing pages
- Modify widget settings in bulk
- Clone and transform page structures

### 3. Elementor JSON Generator (Web Tool)

**URL**: https://theresanaiforthat.com/@markwryte/elementor-json-generator/
**Purpose**: AI-powered Elementor JSON generation
**Best For**: Quick prototyping

**Limitations**:
- ❌ Not an MCP server (manual web tool)
- ❌ No Claude Code integration
- ❌ Must copy/paste output

**Use Case**:
- Generate initial structure ideas
- Quick validation of structure concepts
- Not recommended for production workflow

---

## JSON Schema Validator MCP

### Installation

#### Step 1: Install Server

```bash
# Clone repository
git clone https://github.com/EienWolf/jsonshema_mcp.git
cd jsonshema_mcp

# Install dependencies
pip install -r requirements.txt

# Test server
python mcp_server.py
```

#### Step 2: Configure Claude Code

**Windows** - Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "elementor-wordpress": {
      "command": "npx",
      "args": ["wp-elementor-mcp"],
      "env": {
        "ELEMENTOR_MCP_MODE": "standard",
        "WORDPRESS_BASE_URL": "http://svetlinkielementor.local",
        "WORDPRESS_USERNAME": "test",
        "WORDPRESS_APPLICATION_PASSWORD": "S27q 64rq oFhf TPDA 30nB hNM5"
      }
    },
    "json-schema-validator": {
      "command": "python",
      "args": ["C:\\Users\\denit\\path\\to\\jsonshema_mcp\\mcp_server.py"]
    }
  }
}
```

**Notes**:
- Replace path with actual location
- No PostgreSQL needed (uses local file storage)
- Restart Claude Code after configuration

### Available Tools

#### 1. `generate_schema` - Create Schema from Example

**Purpose**: Generate a JSON schema from example Elementor JSON.

**Usage**:
```javascript
// First, create example Elementor structure
const exampleSection = {
  "id": "abc123",
  "elType": "section",
  "settings": {
    "background_color": "var(--e-global-color-background)",
    "padding": {
      "unit": "px",
      "top": "64",
      "right": "20",
      "bottom": "64",
      "left": "20"
    }
  },
  "elements": []
};

// Generate schema
generate_schema({
  json_data: JSON.stringify(exampleSection),
  schema_name: "elementor_section",
  description: "Schema for Elementor section element"
});
```

**Output**: JSON schema that can validate future sections.

#### 2. `validate_json_schema` - Validate Before Sending

**Purpose**: Ensure JSON is valid before sending to WordPress.

**Usage**:
```javascript
// Validate section before creating page
validate_json_schema({
  json_data: JSON.stringify(newSection),
  schema: elementorSectionSchema
});

// If valid, proceed to create
if (validation.valid) {
  create_elementor_section({
    page_id: 21,
    settings: newSection.settings,
    columns: 1
  });
}
```

#### 3. `add_update_schema` - Store Reusable Schemas

**Purpose**: Save Elementor component schemas for reuse.

**Usage**:
```javascript
// Create schema collection
add_update_schema({
  collection: "elementor",
  schema_id: "section",
  schema: sectionSchema,
  description: "Elementor section structure"
});

add_update_schema({
  collection: "elementor",
  schema_id: "widget_heading",
  schema: headingWidgetSchema,
  description: "Heading widget structure"
});

add_update_schema({
  collection: "elementor",
  schema_id: "widget_icon_box",
  schema: iconBoxWidgetSchema,
  description: "Icon Box widget structure"
});
```

#### 4. `validate_json_from_collections` - Validate Against Stored Schema

**Purpose**: Quick validation using stored schemas.

**Usage**:
```javascript
// Validate new heading widget
validate_json_from_collections({
  json_data: JSON.stringify(newHeading),
  collection: "elementor",
  schema_id: "widget_heading"
});
```

#### 5. `list_schemas` - View Available Schemas

**Purpose**: List all stored schemas for reference.

**Usage**:
```javascript
list_schemas({
  collection: "elementor"
});
// Returns: ["section", "widget_heading", "widget_icon_box", ...]
```

---

## JSON Manipulation MCP

### Installation

```bash
# Install via npm (global)
npm install -g @gongrzhe/server-json-mcp

# Or run via npx
npx @gongrzhe/server-json-mcp
```

### Configure Claude Code

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "elementor-wordpress": { /* existing */ },
    "json-schema-validator": { /* existing */ },
    "json-manipulation": {
      "command": "npx",
      "args": ["@gongrzhe/server-json-mcp"]
    }
  }
}
```

### Use Cases for Elementor

#### Extract All Headings from a Page

```javascript
// Get page Elementor data
const pageData = await get_elementor_data({ page_id: 21 });

// Query all heading widgets
query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..elements[?(@.widgetType=='heading')]"
});
```

#### Find All Hardcoded Colors

```javascript
// Query for hex color values (should be replaced with Global Colors)
query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)]"
});
```

#### Clone Section and Modify Settings

```javascript
// Get specific section
const section = await query_json({
  path: "$.elements[0]"  // First section
});

// Modify background color
filter_json({
  json_data: JSON.stringify(section),
  path: "$.settings.background_color",
  operation: "set",
  value: "var(--e-global-color-background)"
});
```

---

## Elementor JSON Structure Templates

### Template 1: Basic Section with Single Column

```json
{
  "id": "{{ uuid() }}",
  "elType": "section",
  "settings": {
    "background_color": "var(--e-global-color-background)",
    "padding": {
      "unit": "px",
      "top": "64",
      "right": "20",
      "bottom": "64",
      "left": "20"
    }
  },
  "elements": [
    {
      "id": "{{ uuid() }}",
      "elType": "column",
      "settings": {
        "_column_size": 100
      },
      "elements": []
    }
  ]
}
```

**JSON Schema** (for validation):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "elType", "settings", "elements"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier"
    },
    "elType": {
      "type": "string",
      "enum": ["section"],
      "description": "Element type must be 'section'"
    },
    "settings": {
      "type": "object",
      "properties": {
        "background_color": {
          "type": "string",
          "pattern": "^var\\(--e-global-color-.*\\)$",
          "description": "Must use Global Color CSS variable"
        },
        "padding": {
          "type": "object",
          "properties": {
            "unit": { "type": "string", "enum": ["px", "rem", "%"] },
            "top": { "type": "string" },
            "right": { "type": "string" },
            "bottom": { "type": "string" },
            "left": { "type": "string" }
          }
        }
      }
    },
    "elements": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/column"
      }
    }
  },
  "definitions": {
    "column": {
      "type": "object",
      "required": ["id", "elType", "settings", "elements"],
      "properties": {
        "id": { "type": "string" },
        "elType": { "type": "string", "enum": ["column"] },
        "settings": {
          "type": "object",
          "properties": {
            "_column_size": {
              "type": "number",
              "minimum": 0,
              "maximum": 100
            }
          }
        },
        "elements": {
          "type": "array",
          "description": "Array of widgets"
        }
      }
    }
  }
}
```

### Template 2: Heading Widget

```json
{
  "id": "{{ uuid() }}",
  "elType": "widget",
  "widgetType": "heading",
  "settings": {
    "title": "{{ content }}",
    "header_size": "h1",
    "color": "var(--e-global-color-secondary)",
    "typography_typography": "custom",
    "typography_font_size": {
      "unit": "rem",
      "size": "2.75"
    },
    "typography_font_size_tablet": {
      "unit": "rem",
      "size": "2"
    },
    "typography_font_size_mobile": {
      "unit": "rem",
      "size": "1.5"
    }
  }
}
```

**JSON Schema**:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "elType", "widgetType", "settings"],
  "properties": {
    "id": { "type": "string" },
    "elType": {
      "type": "string",
      "enum": ["widget"]
    },
    "widgetType": {
      "type": "string",
      "enum": ["heading"]
    },
    "settings": {
      "type": "object",
      "required": ["title", "header_size"],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1,
          "description": "Heading text content"
        },
        "header_size": {
          "type": "string",
          "enum": ["h1", "h2", "h3", "h4", "h5", "h6"],
          "description": "HTML heading tag"
        },
        "color": {
          "type": "string",
          "pattern": "^var\\(--e-global-color-.*\\)$",
          "description": "Must use Global Color"
        },
        "typography_font_size": {
          "type": "object",
          "properties": {
            "unit": { "type": "string", "enum": ["rem", "px", "em"] },
            "size": { "type": ["string", "number"] }
          }
        }
      }
    }
  }
}
```

### Template 3: Icon Box Widget

```json
{
  "id": "{{ uuid() }}",
  "elType": "widget",
  "widgetType": "icon-box",
  "settings": {
    "icon": {
      "value": "fas fa-lightbulb",
      "library": "fa-solid"
    },
    "title_text": "{{ title }}",
    "description_text": "{{ description }}",
    "icon_color": "var(--e-global-color-accent)",
    "icon_size": {
      "unit": "px",
      "size": "48"
    },
    "title_color": "var(--e-global-color-secondary)",
    "description_color": "var(--e-global-color-text)"
  }
}
```

---

## Workflow Integration

### Recommended Workflow: Schema-First Approach

#### Phase 1: Create Schemas (One-Time Setup)

```javascript
// 1. Create example Elementor structures
const exampleSection = { /* ... */ };
const exampleHeading = { /* ... */ };
const exampleIconBox = { /* ... */ };

// 2. Generate schemas
generate_schema({
  json_data: JSON.stringify(exampleSection),
  schema_name: "section",
  description: "Elementor section"
});

generate_schema({
  json_data: JSON.stringify(exampleHeading),
  schema_name: "widget_heading",
  description: "Heading widget"
});

// 3. Store in collection
add_update_schema({
  collection: "elementor_svetlinki",
  schema_id: "section",
  schema: generatedSectionSchema
});
```

#### Phase 2: Build Pages with Validation

```javascript
// 1. Construct page JSON
const newPage = {
  sections: [
    {
      id: generateUUID(),
      elType: "section",
      settings: {
        background_color: "var(--e-global-color-background)",
        padding: { unit: "px", top: "64", right: "20", bottom: "64", left: "20" }
      },
      elements: [
        {
          id: generateUUID(),
          elType: "column",
          settings: { _column_size: 100 },
          elements: [
            {
              id: generateUUID(),
              elType: "widget",
              widgetType: "heading",
              settings: {
                title: "Образователен център Светлинки",
                header_size: "h1",
                color: "var(--e-global-color-secondary)"
              }
            }
          ]
        }
      ]
    }
  ]
};

// 2. Validate each component
for (const section of newPage.sections) {
  const valid = await validate_json_from_collections({
    json_data: JSON.stringify(section),
    collection: "elementor_svetlinki",
    schema_id: "section"
  });

  if (!valid.is_valid) {
    console.error("Validation failed:", valid.errors);
    return;  // Stop if invalid
  }
}

// 3. If valid, create page
create_elementor_page({
  title: "За Нас",
  slug: "about",
  elementor_data: JSON.stringify(newPage.sections)
});
```

#### Phase 3: Audit Existing Pages

```javascript
// 1. Get existing page
const pageData = await get_elementor_data({ page_id: 21 });

// 2. Validate entire page structure
const validation = await validate_json_from_collections({
  json_data: JSON.stringify(pageData),
  collection: "elementor_svetlinki",
  schema_id: "page"
});

// 3. Find hardcoded colors
const hardcodedColors = await query_json({
  url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
  path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)]"
});

// 4. Generate optimization report
console.log("Validation:", validation.is_valid ? "PASS" : "FAIL");
console.log("Hardcoded colors found:", hardcodedColors.length);
```

---

## Usage Examples

### Example 1: Create Home Page Hero Section

```javascript
// Define hero structure
const heroSection = {
  id: "hero-" + Date.now(),
  elType: "section",
  settings: {
    background_color: "var(--e-global-color-background)",
    padding: {
      unit: "px",
      top: "80",
      right: "20",
      bottom: "80",
      left: "20"
    }
  },
  elements: [
    {
      id: "hero-col-" + Date.now(),
      elType: "column",
      settings: { _column_size: 100 },
      elements: [
        {
          id: "hero-heading-" + Date.now(),
          elType: "widget",
          widgetType: "heading",
          settings: {
            title: "Образователен център Светлинки",
            header_size: "h1",
            color: "var(--e-global-color-secondary)",
            typography_font_size: { unit: "rem", size: "2.75" }
          }
        },
        {
          id: "hero-text-" + Date.now(),
          elType: "widget",
          widgetType: "text-editor",
          settings: {
            editor: "<p>Развиваме умовете на бъдещето чрез ментална аритметика</p>",
            text_color: "var(--e-global-color-text)"
          }
        },
        {
          id: "hero-button-" + Date.now(),
          elType: "widget",
          widgetType: "button",
          settings: {
            text: "Запиши се за пробен урок",
            button_type: "primary",
            background_color: "var(--e-global-color-secondary)",
            hover_background_color: "var(--e-global-color-accent)"
          }
        }
      ]
    }
  ]
};

// Validate
const isValid = await validate_json_from_collections({
  json_data: JSON.stringify(heroSection),
  collection: "elementor_svetlinki",
  schema_id: "section"
});

if (isValid.is_valid) {
  // Create page with hero
  create_elementor_page({
    title: "Home",
    slug: "home",
    elementor_data: JSON.stringify([heroSection])
  });
}
```

### Example 2: Audit and Fix Hardcoded Colors

```javascript
// 1. Get all pages
const pages = await get_pages({ per_page: 100 });

// 2. For each page, find hardcoded colors
for (const page of pages) {
  const pageData = await get_elementor_data({ page_id: page.id });

  // Find hardcoded colors
  const violations = await query_json({
    url: "data:application/json," + encodeURIComponent(JSON.stringify(pageData)),
    path: "$..settings[?(@.color =~ /#[0-9A-Fa-f]{6}/)].color"
  });

  if (violations.length > 0) {
    console.log(`Page ${page.id} (${page.title}): ${violations.length} hardcoded colors found`);
    console.log("Violations:", violations);

    // Map hex colors to Global Colors
    const colorMap = {
      "#6366f1": "var(--e-global-color-primary)",
      "#F5A623": "var(--e-global-color-secondary)",
      "#2c2c2c": "var(--e-global-color-text)",
      "#FDB913": "var(--e-global-color-accent)",
      "#fefcf5": "var(--e-global-color-background)"
    };

    // Fix automatically (requires iteration through widgets)
    // ... implementation details
  }
}
```

### Example 3: Clone and Modify Section

```javascript
// 1. Get existing section from About page
const aboutData = await get_elementor_data({ page_id: 23 });
const missionSection = aboutData.elements[1];  // Second section

// 2. Clone structure
const clonedSection = JSON.parse(JSON.stringify(missionSection));

// 3. Modify IDs (make unique)
clonedSection.id = "cloned-" + Date.now();
clonedSection.elements.forEach(col => {
  col.id = "cloned-col-" + Date.now();
  col.elements.forEach(widget => {
    widget.id = "cloned-widget-" + Date.now();
  });
});

// 4. Modify content
if (clonedSection.elements[0].elements[0].widgetType === "heading") {
  clonedSection.elements[0].elements[0].settings.title = "Нашата визия";
}

// 5. Validate
const valid = await validate_json_from_collections({
  json_data: JSON.stringify(clonedSection),
  collection: "elementor_svetlinki",
  schema_id: "section"
});

// 6. Add to another page
if (valid.is_valid) {
  // Get current page data
  const programsData = await get_elementor_data({ page_id: 25 });
  programsData.elements.push(clonedSection);

  // Update page
  update_elementor_data({
    page_id: 25,
    elementor_data: JSON.stringify(programsData.elements)
  });
}
```

---

## Best Practices

### 1. Always Validate Before Creating

```javascript
// ✅ GOOD
const valid = await validate_json_schema({ json_data, schema });
if (valid.is_valid) {
  create_elementor_page({ ... });
}

// ❌ BAD
create_elementor_page({ ... });  // No validation
```

### 2. Use Schema Collections for Organization

```javascript
// Organize by component type
add_update_schema({ collection: "elementor_sections", schema_id: "hero" });
add_update_schema({ collection: "elementor_sections", schema_id: "features" });
add_update_schema({ collection: "elementor_widgets", schema_id: "heading" });
add_update_schema({ collection: "elementor_widgets", schema_id: "icon_box" });
```

### 3. Store Reusable Templates

```javascript
// Create library of validated templates
const templates = {
  hero_section: await generate_schema({ ... }),
  features_section: await generate_schema({ ... }),
  cta_section: await generate_schema({ ... })
};

// Save to file for reuse
fs.writeFileSync("elementor-templates.json", JSON.stringify(templates));
```

### 4. Automate Validation in CI/CD

```python
# Python script for automated validation
import json

def validate_all_pages():
    pages = [21, 23, 25, 27, 29, 31, 33, 35]
    results = []

    for page_id in pages:
        page_data = get_elementor_data(page_id)
        validation = validate_json_from_collections(
            json_data=json.dumps(page_data),
            collection="elementor_svetlinki",
            schema_id="page"
        )
        results.append({
            "page_id": page_id,
            "valid": validation.is_valid,
            "errors": validation.errors
        })

    return results

# Run before deployment
results = validate_all_pages()
if not all(r["valid"] for r in results):
    print("Validation failed! Cannot deploy.")
    exit(1)
```

---

## Summary

### Key Takeaways

1. **Use JSON Schema Validator MCP** for:
   - Generating schemas from examples
   - Validating JSON before creating pages
   - Storing reusable component schemas

2. **Use JSON Manipulation MCP** for:
   - Querying existing page structures
   - Finding hardcoded values (colors, fonts)
   - Bulk modifications

3. **Schema-First Workflow**:
   - Create schemas once (one-time setup)
   - Validate every JSON structure before use
   - Store templates for common components

4. **Benefits**:
   - ✅ Prevents malformed JSON
   - ✅ Catches Global Color/Font violations early
   - ✅ Ensures consistency across all pages
   - ✅ Enables automated auditing
   - ✅ Reduces debugging time

### Next Steps

1. **Install JSON Schema Validator MCP** (priority)
2. **Create Elementor component schemas** (section, column, widgets)
3. **Validate existing pages** (find issues)
4. **Build new pages with validation** (prevent issues)

---

**Document Version**: 1.0
**Last Updated**: 2025-11-28
**Research Method**: r.jina.ai web search and repository analysis
**Status**: Production Ready - Recommended for Implementation
