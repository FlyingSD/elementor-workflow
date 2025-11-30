#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Header Template (ID 85) with Simple Navigation using HTML Widget
Since nav-menu is Elementor Pro only, we'll use HTML widget for navigation
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
header_id = 85

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# Navigation HTML with styled links
nav_html = '''
<nav style="display: flex; justify-content: center; align-items: center; gap: 30px; height: 100%;">
    <a href="/" style="color: #333333; text-decoration: none; font-size: 16px; font-weight: 500; transition: color 0.3s;">Начало</a>
    <a href="/about/" style="color: #333333; text-decoration: none; font-size: 16px; font-weight: 500; transition: color 0.3s;">За Нас</a>
    <a href="/programs/" style="color: #333333; text-decoration: none; font-size: 16px; font-weight: 500; transition: color 0.3s;">Програми</a>
    <a href="/contact/" style="color: #333333; text-decoration: none; font-size: 16px; font-weight: 500; transition: color 0.3s;">Контакти</a>
    <a href="/blog/" style="color: #333333; text-decoration: none; font-size: 16px; font-weight: 500; transition: color 0.3s;">Блог</a>
</nav>
'''

# Header Section with 3 columns
header_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
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
                        "title_color": "#4F9F8B",  # Teal color
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "28", "sizes": []},
                        "typography_font_weight": "700"
                    }
                }
            ]
        },
        # Column 2: Navigation Menu (34%) - Using HTML widget
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
                    "widgetType": "html",
                    "settings": {
                        "html": nav_html
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
                        "background_color": "#FABA29",  # Yellow
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

# Wrap in array
elementor_data = [header_section]

# Update the header template
update_url = f"{base_url}/wp-json/wp/v2/elementor_library/{header_id}"
payload = {
    "meta": {
        "_elementor_data": json.dumps(elementor_data)
    }
}

print(f"Updating Header Template (ID {header_id}) with simple HTML navigation...")
response = requests.post(update_url, auth=auth, json=payload)

if response.status_code in [200, 201]:
    print("[SUCCESS] Header template updated with HTML navigation!")
    print(f"Status: {response.status_code}")
else:
    print(f"[ERROR] {response.status_code}")
    print(response.text[:500])
