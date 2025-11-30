#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Footer Template (ID 86) with Dark Background and 4 Columns
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
footer_id = 86

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# =============================================================================
# FOOTER MAIN SECTION: 4-Column Layout with Dark Background
# =============================================================================
footer_main = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",  # Full-width
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#1a1a1a",
        "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False},
        "gap": "default"
    },
    "elements": [
        # Column 1: About + Social Media (25%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 25
            },
            "elements": [
                # Heading
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h4",
                        "title_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "22", "sizes": []},
                        "typography_font_weight": "700"
                    }
                },
                # Description text
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "Модерен образователен център за ментална аритметика. Развиваме потенциала на деца от 4 до 13 години в София.",
                        "text_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                },
                # Social Media Icons
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "social-icons",
                    "settings": {
                        "social_icon_list": [
                            {
                                "_id": generate_id(),
                                "social_icon": {"value": "fab fa-facebook", "library": "fa-brands"},
                                "link": {"url": "https://facebook.com/svetlinki", "is_external": True}
                            },
                            {
                                "_id": generate_id(),
                                "social_icon": {"value": "fab fa-instagram", "library": "fa-brands"},
                                "link": {"url": "https://instagram.com/svetlinki", "is_external": True}
                            }
                        ],
                        "icon_color": "#ffffff",
                        "icon_color_hover": "var(--e-global-color-accent)",  # Yellow
                        "icon_size": {"unit": "px", "size": "24", "sizes": []},
                        "icon_spacing": {"unit": "px", "size": "15", "sizes": []}
                    }
                }
            ]
        },
        # Column 2: Resources (25%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 25
            },
            "elements": [
                # Heading
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Ресурси",
                        "header_size": "h4",
                        "title_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                # List of links
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "icon-list",
                    "settings": {
                        "icon_list": [
                            {
                                "_id": generate_id(),
                                "text": "FAQ",
                                "link": {"url": "/faq/", "is_external": False}
                            },
                            {
                                "_id": generate_id(),
                                "text": "Блог",
                                "link": {"url": "/blog/", "is_external": False}
                            },
                            {
                                "_id": generate_id(),
                                "text": "Контакти",
                                "link": {"url": "/contact/", "is_external": False}
                            }
                        ],
                        "icon_list_icon": {"value": "", "library": ""},  # No icon
                        "text_color": "#ffffff",
                        "text_color_hover": "var(--e-global-color-accent)",  # Yellow
                        "text_typography_typography": "custom",
                        "text_typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "space_between": {"unit": "px", "size": "10", "sizes": []}
                    }
                }
            ]
        },
        # Column 3: Contact Info (25%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 25
            },
            "elements": [
                # Heading
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Свържете се с нас",
                        "header_size": "h4",
                        "title_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                # Contact info text
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p><strong>Адрес:</strong><br>София, ул. Оборище 1А, ет. 3</p><p><strong>Email:</strong><br>info@svetlinki.bg</p><p><strong>Телефон:</strong><br>+359 123 456 789</p>",
                        "text_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.8", "sizes": []}
                    }
                }
            ]
        },
        # Column 4: Empty or Additional Info (25%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 25
            },
            "elements": []
        }
    ]
}

# =============================================================================
# FOOTER BOTTOM BAR: Copyright and Links
# =============================================================================
footer_bottom = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#2a2a2a",
        "padding": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": True}
    },
    "elements": [
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": '<p style="text-align: center;">© 2025 Светлинки. Всички права запазени. | <a href="/privacy-policy/">Политика за поверителност</a> | <a href="/terms-of-service/">Общи условия</a></p>',
                        "text_color": "#ffffff",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "13", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# Wrap in array as required by Elementor
elementor_data = [footer_main, footer_bottom]

# Update the footer template
update_url = f"{base_url}/wp-json/wp/v2/elementor_library/{footer_id}"
payload = {
    "meta": {
        "_elementor_data": json.dumps(elementor_data)
    }
}

print(f"Updating Footer Template (ID {footer_id})...")
response = requests.post(update_url, auth=auth, json=payload)

if response.status_code in [200, 201]:
    print("SUCCESS! Footer template updated.")
    print(f"Status: {response.status_code}")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
