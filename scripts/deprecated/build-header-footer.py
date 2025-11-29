#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Header and Footer Templates
Injects content into empty Header Footer Elementor templates
"""

import requests
import json
import random
import sys
import codecs

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")

# Template IDs
header_id = 69
footer_id = 73

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

print("="*60)
print("BUILDING HEADER AND FOOTER TEMPLATES")
print("="*60)

# =============================================================================
# HEADER TEMPLATE
# =============================================================================
print("\n[1/2] Building Header...")

header_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",  # Full-width
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {
            "unit": "px",
            "top": "20",
            "right": "20",
            "bottom": "20",
            "left": "20",
            "isLinked": False
        },
        "border_border": "solid",
        "border_width": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "2",
            "left": "0",
            "isLinked": False
        },
        "border_color": "var(--e-global-color-accent)"  # Cream border bottom
    },
    "elements": [
        # Left column: Logo/Site name
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-secondary)",  # Teal
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "28", "sizes": []},
                        "typography_font_weight": "700"
                    }
                }
            ]
        },
        # Right column: CTA Button
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "ЗАПАЗИ СЕ СЕГА",
                        "link": {"url": "#contact"},
                        "align": "right",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-primary)",  # Yellow
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "typography_font_weight": "600",
                        "button_border_radius": {
                            "unit": "px",
                            "top": "4",
                            "right": "4",
                            "bottom": "4",
                            "left": "4",
                            "isLinked": True
                        }
                    }
                }
            ]
        }
    ]
}

# Save header using generic post meta update
print("Saving header template...")
# Try using wp/v2/posts endpoint with custom fields
header_response = requests.post(
    f"{base_url}/wp-json/wp/v2/posts/{header_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps([header_section], ensure_ascii=False)}}
)

if header_response.status_code == 200:
    print("✓ Header saved successfully!")
else:
    print(f"✗ Header save failed: {header_response.status_code}")
    print(header_response.text)

# =============================================================================
# FOOTER TEMPLATE
# =============================================================================
print("\n[2/2] Building Footer...")

footer_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",  # Full-width
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-secondary)",  # Teal background
        "padding": {
            "unit": "px",
            "top": "40",
            "right": "20",
            "bottom": "40",
            "left": "20",
            "isLinked": False
        }
    },
    "elements": [
        # Left column: Copyright and tagline
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h4",
                        "title_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "20", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Ментална аритметика за деца</p><p>&copy; 2025 Светлинки. Всички права запазени.</p>",
                        "text_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                }
            ]
        },
        # Right column: Contact info
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Контакт",
                        "header_size": "h4",
                        "title_color": "#FFFFFF",
                        "align": "right",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>София, ул. Оборище 1А</p><p>Тел: +359 XXX XXX XXX</p>",
                        "text_color": "#FFFFFF",
                        "align": "right",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# Save footer using generic post meta update
print("Saving footer template...")
footer_response = requests.post(
    f"{base_url}/wp-json/wp/v2/posts/{footer_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps([footer_section], ensure_ascii=False)}}
)

if footer_response.status_code == 200:
    print("✓ Footer saved successfully!")
else:
    print(f"✗ Footer save failed: {footer_response.status_code}")
    print(footer_response.text)

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "="*60)
print("SUMMARY")
print("="*60)

if header_response.status_code == 200 and footer_response.status_code == 200:
    print("\n✓ Both header and footer templates built successfully!")
    print("\nHeader content:")
    print("  - Site name: 'Светлинки'")
    print("  - CTA button: 'ЗАПАЗИ СЕ СЕГА' (links to #contact)")
    print("  - White background with cream bottom border")

    print("\nFooter content:")
    print("  - Site name and copyright")
    print("  - Contact information")
    print("  - Teal background with white text")

    print(f"\n⚠️  IMPORTANT: Clear Elementor cache!")
    print(f"   DELETE {base_url}/wp-json/elementor/v1/cache")

    print(f"\nView homepage: {base_url}/home-2/")
    print(f"Edit header: {base_url}/wp-admin/post.php?post={header_id}&action=elementor")
    print(f"Edit footer: {base_url}/wp-admin/post.php?post={footer_id}&action=elementor")
else:
    print("\n✗ Some templates failed to save. Check errors above.")

print("="*60)
