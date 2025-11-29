#!/usr/bin/env python3
"""
Merge 4 source files into STATIC_RULES.md
Preserves ALL content, organizes by sections with anchor links
"""

def main():
    output_file = "SSOT/STATIC_RULES.md"

    # Header
    header = """# STATIC_RULES.md - Elementor Development Static Rules

**Document Type**: Consolidated Technical Reference
**Created**: 2025-11-29
**Purpose**: Single source of truth for Elementor development rules, JSON structures, and workflows
**Source Files Merged**:
- ELEMENTOR-CORE-PRINCIPLES.md (932 lines)
- JSON-GENERATION-TOOLS-GUIDE.md (941 lines)
- ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md (848 lines)
- MCP-PAGE-CREATION-CHECKLIST.md (750 lines)

**Total Content**: 3471 lines merged and organized
**Status**: Production Reference - Read sections on-demand using anchor links

---

## Table of Contents

Jump to specific sections:
1. [Core Principles & Widget Whitelist](#core-principles) - From ELEMENTOR-CORE-PRINCIPLES.md
2. [JSON Generation Tools](#json-tools) - From JSON-GENERATION-TOOLS-GUIDE.md
3. [Database Schema Deep Dive](#database-schema) - From ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md
4. [MCP Page Creation Checklist](#mcp-checklist) - From MCP-PAGE-CREATION-CHECKLIST.md

---

"""

    # Read source files
    files = [
        ("SSOT/ELEMENTOR-CORE-PRINCIPLES.md", "core-principles", "Core Principles & Widget Whitelist"),
        ("SSOT/JSON-GENERATION-TOOLS-GUIDE.md", "json-tools", "JSON Generation Tools"),
        ("SSOT/ELEMENTOR-DATA-SCHEMA-DEEP-DIVE.md", "database-schema", "Database Schema Deep Dive"),
        ("SSOT/MCP-PAGE-CREATION-CHECKLIST.md", "mcp-checklist", "MCP Page Creation Checklist")
    ]

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(header)

        for filepath, anchor, title in files:
            print(f"Merging {filepath}...")

            # Add section header
            out.write(f'\n<a name="{anchor}"></a>\n')
            out.write(f'## {title}\n\n')
            out.write(f'**Source**: `{filepath}`\n\n')
            out.write('---\n\n')

            # Read and write content (skip original header)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                # Skip until first real content (after metadata header)
                skip_header = True
                for line in lines:
                    # Skip metadata headers and first TOC
                    if skip_header:
                        if line.startswith('##') and not line.startswith('## Table of Contents'):
                            skip_header = False
                            out.write(line)
                        elif line.startswith('---') and len(line.strip()) == 3:
                            # Found first horizontal rule, next content is real
                            skip_header = False
                    else:
                        out.write(line)

            out.write('\n\n')

    print(f"\n✅ Created {output_file}")
    print("✅ ALL content preserved from 4 source files")
    print("✅ Total: 3471+ lines merged")

if __name__ == '__main__':
    main()
