#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Modern Hero Section - Two-Column Layout
Uses CONTAINERS (Flexbox) - Available in Elementor FREE

Design:
- Left Column (55%): Badge, Heading, Description, Buttons, Icon List
- Right Column (45%): Hero Image with styling
"""

import requests
import json
import random

# Configuration
base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 21

def generate_id():
    """Generate random 7-character hex ID for Elementor elements"""
    return ''.join(random.choices('0123456789abcdef', k=7))

# =============================================================================
# MODERN HERO SECTION - CONTAINER BASED (FLEXBOX)
# =============================================================================

# Main Container (Full Width with Gradient Background)
hero_section = {
    "id": generate_id(),
    "elType": "container",
    "settings": {
        # Layout
        "content_width": "full",
        "flex_direction": "row",
        "flex_wrap": "wrap",
        "flex_gap": {"unit": "px", "size": 60},
        "padding": {
            "unit": "px",
            "top": "80",
            "right": "20",
            "bottom": "80",
            "left": "20",
            "isLinked": False
        },
        # Background Gradient
        "background_background": "gradient",
        "background_gradient_type": "linear",
        "background_gradient_angle": {"unit": "deg", "size": 135},
        "background_gradient_color": "#FEFCF5",
        "background_gradient_color_stop": {"unit": "%", "size": 0},
        "background_gradient_color_b": "#FFF5E6",
        "background_gradient_color_b_stop": {"unit": "%", "size": 100},
    },
    "elements": [
        # Inner Container (Boxed, 1200px max)
        {
            "id": generate_id(),
            "elType": "container",
            "settings": {
                "content_width": "boxed",
                "width": {"unit": "px", "size": 1200},
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "flex_gap": {"unit": "px", "size": 60},
                "margin": {"unit": "px", "top": "0", "right": "auto", "bottom": "0", "left": "auto", "isLinked": False}
            },
            "elements": [
                # LEFT CONTAINER (55% width)
                {
                    "id": generate_id(),
                    "elType": "container",
                    "settings": {
                        "flex_basis": {"unit": "%", "size": 55},
                        "flex_direction": "column",
                        "flex_gap": {"unit": "px", "size": 30},
                        "justify_content": "center",
                        # Responsive
                        "flex_basis_mobile": {"unit": "%", "size": 100},
                    },
                    "elements": [
                        # Badge/Pill (Icon Box)
                        {
                            "id": generate_id(),
                            "elType": "widget",
                            "widgetType": "icon-box",
                            "settings": {
                                "view": "default",
                                "icon": {"value": "fas fa-check-circle", "library": "fa-solid"},
                                "title_text": "Доказана методика с над 500+ ученика",
                                "icon_color": "var(--e-global-color-accent)",  # Coral #FF8C7A
                                "title_color": "var(--e-global-color-secondary)",  # Teal #4F9F8B
                                "typography_typography": "custom",
                                "typography_font_size": {"unit": "px", "size": 14},
                                "typography_font_weight": "600",
                                "border_border": "solid",
                                "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
                                "border_color": "var(--e-global-color-accent)",
                                "border_radius": {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True},
                                "padding": {"unit": "px", "top": "12", "right": "24", "bottom": "12", "left": "24", "isLinked": False},
                                "background_background": "classic",
                                "background_color": "#FFFFFF"
                            }
                        },
                        # H1 Heading with Accent
                        {
                            "id": generate_id(),
                            "elType": "widget",
                            "widgetType": "heading",
                            "settings": {
                                "title": "Математика, Която <span style='color: var(--e-global-color-secondary);'>Вдъхновява</span> и Развива",
                                "header_size": "h1",
                                "align": "left",
                                "title_color": "var(--e-global-color-text)",  # Dark #1D3234
                                "typography_typography": "custom",
                                "typography_font_size": {"unit": "px", "size": 48},
                                "typography_font_weight": "700",
                                "typography_line_height": {"unit": "em", "size": 1.2},
                                # Responsive
                                "typography_font_size_mobile": {"unit": "px", "size": 32}
                            }
                        },
                        # Description Text
                        {
                            "id": generate_id(),
                            "elType": "widget",
                            "widgetType": "text-editor",
                            "settings": {
                                "editor": "<p>Индивидуален подход, интерактивни упражнения и доказани методи, които помагат на децата да разберат и обикнат математиката.</p>",
                                "align": "left",
                                "text_color": "var(--e-global-color-text)",
                                "typography_typography": "custom",
                                "typography_font_size": {"unit": "px", "size": 18},
                                "typography_line_height": {"unit": "em", "size": 1.6}
                            }
                        },
                        # Buttons Container (Flexbox)
                        {
                            "id": generate_id(),
                            "elType": "container",
                            "settings": {
                                "flex_direction": "row",
                                "flex_gap": {"unit": "px", "size": 20},
                                "flex_wrap": "wrap",
                                # Responsive
                                "flex_direction_mobile": "column"
                            },
                            "elements": [
                                # Primary Button (Yellow)
                                {
                                    "id": generate_id(),
                                    "elType": "widget",
                                    "widgetType": "button",
                                    "settings": {
                                        "text": "Запазете Първи Час",
                                        "link": {"url": "#contact"},
                                        "button_type": "success",
                                        "size": "md",
                                        "button_background_color": "var(--e-global-color-primary)",  # Yellow #FABA29
                                        "button_text_color": "#1D3234",
                                        "typography_typography": "custom",
                                        "typography_font_size": {"unit": "px", "size": 16},
                                        "typography_font_weight": "600",
                                        "button_border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                                        "button_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
                                        "button_box_shadow_box_shadow_type": "yes",
                                        "button_box_shadow_box_shadow": {
                                            "horizontal": 0,
                                            "vertical": 4,
                                            "blur": 12,
                                            "spread": 0,
                                            "color": "rgba(250, 186, 41, 0.3)"
                                        },
                                        # Hover
                                        "button_background_hover_color": "#E5A824",
                                        "hover_animation": "grow"
                                    }
                                },
                                # Secondary Button (Outline Teal)
                                {
                                    "id": generate_id(),
                                    "elType": "widget",
                                    "widgetType": "button",
                                    "settings": {
                                        "text": "Разгледайте Методиката",
                                        "link": {"url": "#about"},
                                        "button_type": "default",
                                        "size": "md",
                                        "button_text_color": "var(--e-global-color-secondary)",  # Teal #4F9F8B
                                        "typography_typography": "custom",
                                        "typography_font_size": {"unit": "px", "size": 16},
                                        "typography_font_weight": "600",
                                        "border_border": "solid",
                                        "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
                                        "border_color": "var(--e-global-color-secondary)",
                                        "button_border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                                        "button_padding": {"unit": "px", "top": "16", "right": "32", "bottom": "16", "left": "32", "isLinked": False},
                                        "background_background": "classic",
                                        "background_color": "transparent",
                                        # Hover
                                        "button_background_hover_color": "var(--e-global-color-secondary)",
                                        "button_hover_color": "#FFFFFF"
                                    }
                                }
                            ]
                        },
                        # Icon List (3 benefits)
                        {
                            "id": generate_id(),
                            "elType": "widget",
                            "widgetType": "icon-list",
                            "settings": {
                                "icon_list": [
                                    {
                                        "_id": generate_id(),
                                        "text": "Индивидуален подход към всяко дете",
                                        "icon": {"value": "fas fa-check", "library": "fa-solid"}
                                    },
                                    {
                                        "_id": generate_id(),
                                        "text": "Интерактивни упражнения и игри",
                                        "icon": {"value": "fas fa-check", "library": "fa-solid"}
                                    },
                                    {
                                        "_id": generate_id(),
                                        "text": "Доказани резултати и подобрени оценки",
                                        "icon": {"value": "fas fa-check", "library": "fa-solid"}
                                    }
                                ],
                                "icon_color": "var(--e-global-color-accent)",  # Coral #FF8C7A
                                "text_color": "var(--e-global-color-text)",
                                "text_typography_typography": "custom",
                                "text_typography_font_size": {"unit": "px", "size": 16},
                                "space_between": {"unit": "px", "size": 12}
                            }
                        }
                    ]
                },
                # RIGHT CONTAINER (45% width)
                {
                    "id": generate_id(),
                    "elType": "container",
                    "settings": {
                        "flex_basis": {"unit": "%", "size": 45},
                        "flex_direction": "column",
                        "justify_content": "center",
                        "align_items": "center",
                        # Responsive
                        "flex_basis_mobile": {"unit": "%", "size": 100},
                    },
                    "elements": [
                        # Hero Image
                        {
                            "id": generate_id(),
                            "elType": "widget",
                            "widgetType": "image",
                            "settings": {
                                "image": {"url": "https://picsum.photos/600/650"},
                                "image_size": "full",
                                "border_border": "solid",
                                "border_width": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                                "border_color": "#FFFFFF",
                                "border_radius": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": True},
                                "_box_shadow_box_shadow_type": "yes",
                                "_box_shadow_box_shadow": {
                                    "horizontal": 0,
                                    "vertical": 10,
                                    "blur": 40,
                                    "spread": 0,
                                    "color": "rgba(0, 0, 0, 0.1)"
                                },
                                "width": {"unit": "%", "size": 100}
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

# =============================================================================
# FETCH EXISTING PAGE DATA
# =============================================================================
print("=" * 80)
print("BUILDING MODERN HERO SECTION")
print("=" * 80)
print(f"Page ID: {page_id}")
print(f"Site: {base_url}")
print()

print("Fetching existing page data...")
response = requests.get(f"{base_url}/wp-json/wp/v2/pages/{page_id}", auth=auth)

if response.status_code != 200:
    print(f"❌ ERROR: Failed to fetch page data (Status {response.status_code})")
    print(response.text)
    exit(1)

page_data = response.json()
elementor_data_str = page_data.get('meta', {}).get('_elementor_data', '[]')

if isinstance(elementor_data_str, str):
    existing_sections = json.loads(elementor_data_str) if elementor_data_str else []
else:
    existing_sections = elementor_data_str

print(f"✅ Found {len(existing_sections)} existing sections")

# =============================================================================
# REPLACE FIRST SECTION WITH NEW HERO
# =============================================================================
if len(existing_sections) > 0:
    print(f"Replacing first section (was: {existing_sections[0].get('elType', 'unknown')})")
    new_sections = [hero_section] + existing_sections[1:]
else:
    print("No existing sections found, creating new hero as first section")
    new_sections = [hero_section]

print(f"\nTotal sections after update: {len(new_sections)}")
print("Structure:")
print("  1. Hero (NEW - Modern Two-Column Container)")
for i, section in enumerate(new_sections[1:], start=2):
    el_type = section.get('elType', 'unknown')
    print(f"  {i}. {el_type.capitalize()}")

# =============================================================================
# SAVE TO DATABASE
# =============================================================================
print("\n" + "=" * 80)
print("SAVING TO DATABASE...")
print("=" * 80)

update_response = requests.post(
    f"{base_url}/wp-json/wp/v2/pages/{page_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps(new_sections, ensure_ascii=False)}}
)

if update_response.status_code == 200:
    print("\n✅ SUCCESS! Modern hero section created!")
    print()
    print(f"View: {base_url}")
    print(f"Edit: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
    print()
    print("=" * 80)
    print("NEXT STEPS:")
    print("=" * 80)
    print("1. Open Elementor editor and click 'Update' to trigger hooks")
    print("2. Clear Elementor cache (Tools > Regenerate CSS)")
    print("3. View frontend to see the new hero section")
    print()
else:
    print(f"\n❌ ERROR: Failed to update page (Status {update_response.status_code})")
    print(response.text)
    exit(1)
