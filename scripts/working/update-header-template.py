#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Header Template (ID 69) with Navigation Menu
3-column layout: Logo | Navigation | CTA Button
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
header_id = 85

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# =============================================================================
# HEADER SECTION: 3-Column Layout
# =============================================================================
header_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",  # Full-width
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": False},
        "gap": "narrow"
    },
    "elements": [
        # Column 1: Logo (33%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 33,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h2",
                        "align": "left",
                        "title_color": "var(--e-global-color-primary)",  # Teal
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "28", "sizes": []},
                        "typography_font_weight": "700"
                    }
                }
            ]
        },
        # Column 2: Navigation Menu (34%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 34,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "nav-menu",
                    "settings": {
                        "layout": "horizontal",
                        "align_items": "center",
                        "pointer": "underline",
                        "menu": "5",  # Menu ID created earlier
                        "menu_typography_typography": "custom",
                        "menu_typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "menu_typography_font_weight": "500",
                        "text_color": "#333333",
                        "text_hover_color": "var(--e-global-color-primary)"
                    }
                }
            ]
        },
        # Column 3: CTA Button (33%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 33,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "ЗАПАЗИ СЕ СЕГА",
                        "link": {"url": "/contact/", "is_external": False, "nofollow": False},
                        "align": "right",
                        "size": "md",
                        "button_text_color": "#000000",
                        "background_color": "var(--e-global-color-accent)",  # Yellow
                        "button_background_hover_color": "#E0A820",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "typography_font_weight": "600",
                        "border_radius": {"unit": "px", "top": "5", "right": "5", "bottom": "5", "left": "5", "isLinked": True},
                        "button_padding": {"unit": "px", "top": "15", "right": "30", "bottom": "15", "left": "30", "isLinked": False}
                    }
                }
            ]
        }
    ]
}

# Wrap in array as required by Elementor
elementor_data = [header_section]

# Update the header template
update_url = f"{base_url}/wp-json/wp/v2/elementor_library/{header_id}"
payload = {
    "meta": {
        "_elementor_data": json.dumps(elementor_data)
    }
}

print(f"Updating Header Template (ID {header_id})...")
response = requests.post(update_url, auth=auth, json=payload)

if response.status_code in [200, 201]:
    print("SUCCESS! Header template updated.")
    print(f"Status: {response.status_code}")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
