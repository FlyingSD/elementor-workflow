# Elementor Developer Resources Reference

**Purpose**: Authoritative sources for Elementor development and automation
**Last Updated**: 2025-11-29
**Source**: Fetched via r.jina from official Elementor documentation

---

## 🎯 Primary Documentation Hub

**Main Entry Point**: https://developers.elementor.com/

This is the official Elementor Developers Documentation Center - the most authoritative source for understanding Elementor's internal logic and programmatic interfaces.

**Key Feature**: The entire site is built with Elementor itself, demonstrating best practices and patterns.

---

## 📚 Key Documentation Sections

### 1. WP-CLI Commands (Automation Hub)

**URL**: https://developers.elementor.com/docs/cli/

**Purpose**: "The Gold Standard" for automation - allows managing Elementor without the UI.

**Available Commands**:

```bash
# Syntax
wp elementor <command> [--argument]
wp elementor-pro <command> [--argument]

# System & Database Management
wp elementor system-info              # Get system information
wp elementor update-db                # Update database schema
wp elementor flush-css                # Regenerate CSS files

# URL & Content
wp elementor replace-urls             # Replace URLs in database

# Library Operations
wp elementor library-sync             # Sync library
wp elementor library-connect          # Connect to library
wp elementor library-disconnect       # Disconnect from library
wp elementor library-import           # Import from library
wp elementor library-import-dir       # Import directory

# Kit Management
wp elementor kit-import               # Import design kit
wp elementor kit-export               # Export design kit

# Theme Builder
wp elementor clear-theme-builder-conditions  # Clear conditions

# Experiments
wp elementor experiment-status        # Check experiment status
wp elementor experiment-activate      # Activate experiment
wp elementor experiment-deactivate    # Deactivate experiment

# Licensing (PRO)
wp elementor-pro license-activate     # Activate license
wp elementor-pro license-deactivate   # Deactivate license
```

**Use Cases**:
- Bulk operations across multiple sites
- CI/CD pipeline integration
- Automated deployments
- Server-side cache management
- URL migrations after domain changes

**Help**: Use `wp help elementor <command>` for detailed parameters.

---

### 2. Hooks & Filters Reference

**URL**: https://developers.elementor.com/docs/hooks/

**Purpose**: Extensibility points for customizing Elementor behavior without modifying core files.

**Critical Hooks by Category**:

#### Page Save/Update Operations:
- **Save Editor Data** - Handles editor data persistence
- Allows interception of page save workflow
- Useful for validation, transformation, or logging

#### Widget Registration:
- **Widget Skins** - Customize widget appearance options
- Enables creation of widget variations
- Core component for extending functionality

#### CSS Generation:
- **Parse Element CSS** - Manages stylesheet processing
- Intercept and modify styling logic
- Critical for custom CSS injection (like our polyfill!)

#### Frontend Rendering:
- **Render Frontend Elements** - Controls element output on public site
- **Render Widget Content** - Handles widget display
- **Frontend Content** - Manages general frontend output
- **Print Widget Template** - Affects template rendering

**Hook Types Available**:
- ✅ **Filter hooks** - Return modified parameter values
- ✅ **Action hooks** - Execute custom code during specific events
- ✅ **PHP hooks** - Server-side logic
- ✅ **JavaScript hooks** - Client-side behavior
- ✅ **Frontend hooks** - Public-facing pages
- ✅ **Editor hooks** - Admin interface

**Philosophy**: "Manipulate functionality without modifying core files"

---

### 3. Widget Structure & Data

**URL**: https://developers.elementor.com/docs/widgets/

**Purpose**: Understanding how widgets are built and stored.

#### Widget Data Methods (PHP Class):

```php
class My_Widget extends \Elementor\Widget_Base {

    // 1. Unique identifier
    public function get_name() {
        return 'my-widget';
    }

    // 2. User-facing label
    public function get_title() {
        return 'My Widget';
    }

    // 3. Visual icon (FontAwesome or Elementor icons)
    public function get_icon() {
        return 'eicon-code';
    }

    // 4. Organizational category
    public function get_categories() {
        return ['general'];
    }

    // 5. Search keywords
    public function get_keywords() {
        return ['custom', 'widget'];
    }

    // 6. Optional help URL
    public function get_custom_help_url() {
        return 'https://example.com/help';
    }

    // 7. Optional upsale data
    public function get_upsale_data() {
        return [];
    }
}
```

#### Database Storage:

**Field**: `_elementor_data` (in `post_meta` table)
**Format**: Serialized JSON array

**Structure** (based on our working examples):
```json
[
  {
    "id": "abc123",
    "elType": "section",
    "settings": {
      "stretch_section": "section-stretched",
      "background_color": "var(--e-global-color-accent)"
    },
    "elements": [
      {
        "id": "def456",
        "elType": "column",
        "settings": {
          "_column_size": 100
        },
        "elements": [
          {
            "id": "ghi789",
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
              "title": "Heading Text",
              "title_color": "var(--e-global-color-secondary)"
            }
          }
        ]
      }
    ]
  }
]
```

**elType Values**:
- `section` - Legacy section (Elementor FREE)
- `column` - Column wrapper inside section
- `widget` - Individual widget element
- `container` - Flexbox container (Elementor PRO only!)

**Key Properties**:
- `id` - Unique element identifier
- `elType` - Element type
- `settings` - Configuration object
- `elements` - Nested children array
- `widgetType` - Widget name (for elType: 'widget')

---

### 4. Widget Controls Reference

**URL**: https://developers.elementor.com/docs/widgets/widget-controls/

**Purpose**: API documentation for form controls and settings.

#### Available Control Types:

```php
// TEXT - Basic text input
$this->add_control(
    'title',
    [
        'type' => \Elementor\Controls_Manager::TEXT,
        'label' => 'Title',
        'placeholder' => 'Enter title',
        'default' => ''
    ]
);

// NUMBER - Numeric input
$this->add_control(
    'count',
    [
        'type' => \Elementor\Controls_Manager::NUMBER,
        'label' => 'Count',
        'min' => 0,
        'max' => 100,
        'step' => 1,
        'default' => 10
    ]
);

// SELECT - Dropdown
$this->add_control(
    'alignment',
    [
        'type' => \Elementor\Controls_Manager::SELECT,
        'label' => 'Alignment',
        'options' => [
            'left' => 'Left',
            'center' => 'Center',
            'right' => 'Right'
        ],
        'default' => 'left'
    ]
);

// CHOOSE - Icon-based choice
$this->add_control(
    'text_align',
    [
        'type' => \Elementor\Controls_Manager::CHOOSE,
        'label' => 'Text Align',
        'options' => [
            'left' => [
                'title' => 'Left',
                'icon' => 'eicon-text-align-left'
            ],
            'center' => [
                'title' => 'Center',
                'icon' => 'eicon-text-align-center'
            ]
        ]
    ]
);
```

#### Control Registration Pattern:

```php
protected function register_controls() {
    // Start section
    $this->start_controls_section(
        'content_section',
        [
            'label' => 'Content',
            'tab' => \Elementor\Controls_Manager::TAB_CONTENT
        ]
    );

    // Add controls
    $this->add_control('control_id', [...]);

    // End section
    $this->end_controls_section();
}
```

#### Control Categories:
- ✅ **Regular controls** - Single values
- ✅ **Responsive controls** - Device-specific variations
- ✅ **Group controls** - Bundled related settings (typography, dimensions)

**Storage**: Control values are saved in the `settings` object in JSON.

---

### 5. Scripts & Styles Management

**URL**: https://developers.elementor.com/docs/ (specific section TBD)

**Purpose**: Asset enqueuing and resource management.

**Key Concepts**:
- CSS Print Method settings (Internal Embedding vs External File)
- Script dependencies and loading order
- Style regeneration and caching

**Related to Our Fixes**:
- CSS Print Method = "Internal Embedding" solves caching on .local domains
- `wp elementor flush-css` regenerates all CSS files
- Polyfill injection via `wp_head` action hook

---

## 🐙 GitHub Repository

**URL**: https://github.com/elementor/elementor

**License**: Free and Open Source

**Key Directories**:
```
elementor/
├── core/           # Core framework and foundation logic
├── modules/        # Feature modules (likely widget location)
├── includes/       # Helper functions and utilities
├── assets/         # Frontend resources (CSS, JS, images)
├── app/            # Application-level code
├── packages/       # Reusable code packages
├── tests/          # Test suites
└── docs/           # Documentation
```

**Languages**:
- PHP: 38.5% (backend)
- JavaScript: 33.4% (frontend)
- TypeScript: 23.1% (modern frontend)

**Entry Point**: `elementor.php` (main plugin file)

**Configuration Files**:
- `composer.json` - PHP dependencies
- `package.json` - JavaScript/Node dependencies
- `tsconfig.json` - TypeScript configuration

**Use Cases**:
- Understanding internal implementation
- Finding undocumented features
- Debugging complex issues
- Studying best practices

---

## 🔧 Developer Edition

**URL**: https://github.com/elementor/elementor-developer-edition

**Purpose**: Development-focused version with additional tooling.

---

## 📖 Help Center (User Documentation)

**URL**: https://elementor.com/help/

**Sitemap**: https://elementor.com/help/sitemap/ (for Claude to crawl)

**Purpose**: User-facing documentation explaining UI features and workflows.

**Use Cases**:
- Understanding "what this button does"
- Learning UI layout logic (like Full Width issues)
- User-facing feature explanations

**Note**: This is for UI understanding, not programmatic interfaces.

---

## 🎯 Strategy for Claude Code Usage

### For System/Config Tasks:
✅ **Use**: WP-CLI documentation
✅ **Approach**: Terminal commands for setup and configuration
✅ **Example**: `wp elementor flush-css` after changes

### For Debugging Issues:
✅ **Use**: Developer Docs + GitHub Issues
✅ **Approach**: Research error messages and implementation details
✅ **Example**: Finding why Global Colors don't output (led to polyfill solution)

### For Content Creation:
✅ **Use**: Widget structure docs + JSON format understanding
✅ **Approach**: Construct `_elementor_data` JSON or use templates
✅ **Example**: Building Hero section with correct JSON structure

### For Hook Implementation:
✅ **Use**: Hooks reference + GitHub code examples
✅ **Approach**: Find appropriate action/filter, study parameters
✅ **Example**: `wp_head` hook for polyfill injection

---

## 🚨 Critical Learnings (from 2025-11-29 Session)

### What the Docs DON'T Tell You:

1. **Global Colors in FREE don't output CSS variables**
   - Not mentioned in FREE vs PRO comparison
   - Discovered through debugging
   - Solution: PHP polyfill via `wp_head` hook

2. **CSS Print Method affects stretch sections on local domains**
   - Mentioned in settings, but not the .local caching issue
   - "Internal Embedding" required for local development

3. **REST API bypasses Elementor hooks**
   - Not documented in API docs
   - Manual "Update" click required after REST API changes

4. **Flexbox Containers are PRO-only**
   - Mentioned but not emphasized in comparisons
   - Must use Legacy Sections in FREE

5. **Widget property names are specific, not generic**
   - Not in a centralized reference
   - `title_color` not `color`, `button_text_color` not `text_color`
   - Must inspect widget code or test empirically

---

## 📋 Recommended Reading Order (for Claude)

When starting new Elementor development work:

1. **First**: https://developers.elementor.com/ (Overview)
2. **Second**: Widget Structure docs (understand data format)
3. **Third**: Hooks reference (for customizations)
4. **Fourth**: WP-CLI commands (for automation)
5. **As Needed**: GitHub repo (for implementation details)
6. **Last Resort**: Help Center (user perspective)

---

## 🔗 Quick Reference Links

| Resource | URL | Use Case |
|----------|-----|----------|
| Developer Hub | https://developers.elementor.com/ | Main entry point |
| WP-CLI | https://developers.elementor.com/docs/cli/ | Automation commands |
| Hooks | https://developers.elementor.com/docs/hooks/ | Extensibility |
| Widgets | https://developers.elementor.com/docs/widgets/ | Widget development |
| Controls | https://developers.elementor.com/docs/widgets/widget-controls/ | Form controls |
| GitHub | https://github.com/elementor/elementor | Source code |
| Help Center | https://elementor.com/help/ | User docs |
| Help Sitemap | https://elementor.com/help/sitemap/ | Crawlable help index |

---

## 💡 Tips for r.jina Research

When using r.jina to fetch Elementor docs:

✅ **Prioritize**: Official developers.elementor.com over blog posts
✅ **Check**: GitHub issues for undocumented behaviors
✅ **Verify**: Help Center for UI-related questions
✅ **Cross-reference**: Multiple sources for critical information
✅ **Test**: Always validate findings empirically (docs can be outdated)

❌ **Avoid**: Random blog tutorials (often outdated or incomplete)
❌ **Avoid**: Marketing content (lacks technical depth)
❌ **Avoid**: Tutorial mills (may contain inaccurate information)

---

**Version**: 1.0
**Created**: 2025-11-29
**Maintained by**: Claude Code
**Purpose**: Authoritative reference for Elementor development and automation

**Note**: This document is a curated summary. Always consult the live documentation at developers.elementor.com for the most up-to-date information.
