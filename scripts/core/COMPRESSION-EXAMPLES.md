# Compression Examples - Before & After

**Script**: `compress-ssot.js`
**Purpose**: Show real compression transformations

---

## Example 1: Verbose Paragraphs

### BEFORE (10 lines, 523 chars)
```markdown
This is important because we need to ensure that all elements are properly 
aligned within the Elementor editor. It's worth noting that Elementor provides 
multiple alignment options for different use cases. Keep in mind that you 
should always test your alignments on mobile devices to ensure responsive 
behavior. One thing to remember is that responsive design is absolutely 
critical for modern websites. As mentioned earlier, proper alignment is 
the foundation of good web design.
```

### AFTER (3 lines, 267 chars)
```markdown
- We need to ensure that all elements are properly aligned within the Elementor editor.
- Elementor provides multiple alignment options for different use cases.
- You should always test your alignments on mobile devices to ensure responsive behavior.
```

**Savings**: 7 lines (70%), 256 chars (49%)

---

## Example 2: Redundant Examples

### BEFORE (15 lines)
```markdown
Example 1: Create a simple button
```javascript
{
  "widgetType": "button",
  "settings": {
    "text": "Click Me"
  }
}
```

Example 2: Create a heading widget
```javascript
{
  "widgetType": "heading",
  "settings": {
    "title": "Welcome"
  }
}
```

Example 3: Create an image widget
```javascript
{
  "widgetType": "image",
  "settings": {
    "url": "image.jpg"
  }
}
```
```

### AFTER (10 lines)
```markdown
Example 1: Create a simple button
```javascript
{
  "widgetType": "button",
  "settings": {
    "text": "Click Me"
  }
}
```

*(Additional examples removed for brevity)*
```

**Savings**: 5 lines (33%)

---

## Example 3: ASCII Decorations

### BEFORE (7 lines)
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Global Colors Configuration          │
│ Primary: #FABA29                      │
│ Secondary: #4F9F8B                    │
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### AFTER (3 lines)
```markdown
Global Colors Configuration
Primary: #FABA29
Secondary: #4F9F8B
```

**Savings**: 4 lines (57%)

---

## Example 4: Verbose Phrases

### BEFORE (1 line, 147 chars)
```markdown
This is important because you need to ensure that, as mentioned earlier, the Global Colors are properly configured before you start building pages.
```

### AFTER (1 line, 87 chars)
```markdown
You need to ensure that the Global Colors are properly configured before building pages.
```

**Savings**: 60 chars (41%)

---

## Example 5: Label Prefixes

### BEFORE (5 lines)
```markdown
Note: Always backup before updates
Remember: Test on staging first
Keep in mind: Mobile testing is critical
Important: Use Global Colors
For example: Primary color is #FABA29
```

### AFTER (5 lines)
```markdown
Always backup before updates
Test on staging first
Mobile testing is critical
Use Global Colors
Primary color is #FABA29
```

**Savings**: Same line count, but ~30% char reduction per line

---

## Example 6: Multiple Blank Lines

### BEFORE (10 lines)
```markdown
Section 1 content here


Section 2 content here



Section 3 content here
```

### AFTER (6 lines)
```markdown
Section 1 content here

Section 2 content here

Section 3 content here
```

**Savings**: 4 lines (40%)

---

## Example 7: Protected Content (NOT Compressed)

### Code Blocks (Preserved)
```markdown
### BEFORE & AFTER (Identical)
```javascript
function example() {
  // All whitespace preserved
  const config = {
    verbose:    true,
    spacing:    "preserved",
    comments:   "intact"
  };
  return config;
}
```
```

**Savings**: 0 (protected content)

---

## Example 8: Headers (NOT Compressed)

### BEFORE & AFTER (Identical)
```markdown
## Section Title (Anchor!)
### Subsection Title
#### Sub-subsection Title
```

**Savings**: 0 (anchors must be preserved)

---

## Example 9: Tables (NOT Compressed)

### BEFORE & AFTER (Identical)
```markdown
| Column 1        | Column 2        | Column 3        |
|-----------------|-----------------|-----------------|
| Data with lots  | More data here  | Even more data  |
| of   spacing    | preserved       | exactly         |
```

**Savings**: 0 (tables preserved)

---

## Real-World File Example

### STATIC_RULES.md

**BEFORE**: 3,553 lines
```markdown
# STATIC_RULES.md - Elementor Development Static Rules

This is important because this document serves as the single source of truth 
for all Elementor development rules and guidelines. It's worth noting that 
we've merged multiple documents into this comprehensive reference. Keep in 
mind that you should always read sections on-demand using anchor links rather 
than loading the entire file.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Core Principles                       │
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Structural Hierarchy

Note: Elementor offers two architecture options.

Remember: Use Flexbox Containers for all new pages.

Example 1: Container with 3 widgets
```json
{"elType": "container", "elements": [...]}
```

Example 2: Container with nested containers
```json
{"elType": "container", "elements": [{"elType": "container"}]}
```

Example 3: Empty container
```json
{"elType": "container", "elements": []}
```


Keep in mind: Containers are more performant than legacy sections.
```

**AFTER**: 3,324 lines
```markdown
# STATIC_RULES.md - Elementor Development Static Rules

- This document serves as the single source of truth for all Elementor development rules.
- We've merged multiple documents into this comprehensive reference.
- Always read sections on-demand using anchor links.

Core Principles

## Structural Hierarchy

Elementor offers two architecture options.

Use Flexbox Containers for all new pages.

Example 1: Container with 3 widgets
```json
{"elType": "container", "elements": [...]}
```

*(Additional examples removed for brevity)*

Containers are more performant than legacy sections.
```

**Savings**: 229 lines (6.4%)

---

## Summary Statistics

| Compression Type | Avg Savings |
|------------------|-------------|
| Verbose paragraphs | 40-70% |
| ASCII decorations | 50-60% |
| Redundant examples | 30-40% |
| Verbose phrases | 30-50% |
| Label prefixes | 20-30% |
| Multiple blank lines | 40% |
| **Overall** | **5-10%** |

---

## Protected Content (0% Compression)

- Code blocks: 30-40% of SSOT content
- Headers: 10-15% of SSOT content
- Tables: 10% of SSOT content
- Links: 5% of SSOT content

**Total protected**: ~55-70% of content

**Compressible content**: ~30-45%

**Realistic compression**: 5-10% of file size

---

**Script**: `scripts/core/compress-ssot.js`
**Created**: 2025-12-01
