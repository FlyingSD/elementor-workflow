#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Contact Page (ID 27) - Svetlinki Elementor
Uses SECTIONS (not Containers) - Elementor FREE compatible
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 27

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# =============================================================================
# SECTION 1: HERO
# =============================================================================
hero_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",  # Cream #FEFCF5
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
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
                    "widgetType": "heading",
                    "settings": {
                        "title": "Контакти",
                        "header_size": "h1",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",  # Teal #4F9F8B
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "44", "sizes": []},
                        "typography_font_weight": "700"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Свържете се с нас</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",  # Dark Gray #2C2C2C
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "20", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 2: CONTACT INFORMATION
# =============================================================================
contact_info_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
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
                    "widgetType": "heading",
                    "settings": {
                        "title": "Информация за контакт",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "36", "sizes": []},
                        "typography_font_weight": "700",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
                    }
                }
            ]
        }
    ]
}

# Three columns for contact details
contact_info_section["elements"].append({
    "id": generate_id(),
    "elType": "column",
    "settings": {"_column_size": 33, "_inline_size": 33.333},
    "elements": [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "icon-box",
            "settings": {
                "icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"},
                "title_text": "Адрес",
                "description_text": "София, ул. Примерна 123",
                "title_color": "var(--e-global-color-secondary)",
                "description_color": "var(--e-global-color-text)",
                "icon_color": "var(--e-global-color-primary)",  # Yellow #FABA29
                "icon_size": {"unit": "px", "size": "40", "sizes": []},
                "position": "top",
                "content_vertical_alignment": "top",
                "title_typography_typography": "custom",
                "title_typography_font_size": {"unit": "px", "size": "22", "sizes": []},
                "title_typography_font_weight": "600",
                "description_typography_typography": "custom",
                "description_typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                "text_align": "center"
            }
        }
    ]
})

contact_info_section["elements"].append({
    "id": generate_id(),
    "elType": "column",
    "settings": {"_column_size": 33, "_inline_size": 33.333},
    "elements": [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "icon-box",
            "settings": {
                "icon": {"value": "fas fa-phone-alt", "library": "fa-solid"},
                "title_text": "Телефон",
                "description_text": "+359 123 456 789",
                "title_color": "var(--e-global-color-secondary)",
                "description_color": "var(--e-global-color-text)",
                "icon_color": "var(--e-global-color-primary)",
                "icon_size": {"unit": "px", "size": "40", "sizes": []},
                "position": "top",
                "content_vertical_alignment": "top",
                "title_typography_typography": "custom",
                "title_typography_font_size": {"unit": "px", "size": "22", "sizes": []},
                "title_typography_font_weight": "600",
                "description_typography_typography": "custom",
                "description_typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                "text_align": "center"
            }
        }
    ]
})

contact_info_section["elements"].append({
    "id": generate_id(),
    "elType": "column",
    "settings": {"_column_size": 33, "_inline_size": 33.333},
    "elements": [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "icon-box",
            "settings": {
                "icon": {"value": "fas fa-envelope", "library": "fa-solid"},
                "title_text": "Имейл",
                "description_text": "info@svetlinki.bg",
                "title_color": "var(--e-global-color-secondary)",
                "description_color": "var(--e-global-color-text)",
                "icon_color": "var(--e-global-color-primary)",
                "icon_size": {"unit": "px", "size": "40", "sizes": []},
                "position": "top",
                "content_vertical_alignment": "top",
                "title_typography_typography": "custom",
                "title_typography_font_size": {"unit": "px", "size": "22", "sizes": []},
                "title_typography_font_weight": "600",
                "description_typography_typography": "custom",
                "description_typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                "text_align": "center"
            }
        }
    ]
})

# =============================================================================
# SECTION 3: WORKING HOURS
# =============================================================================
working_hours_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",
        "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
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
                    "widgetType": "heading",
                    "settings": {
                        "title": "Работно време",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "36", "sizes": []},
                        "typography_font_weight": "700",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p><strong>Понеделник - Петък:</strong> 09:00 - 18:00</p><p><strong>Събота:</strong> 10:00 - 14:00</p><p><strong>Неделя:</strong> Почивен ден</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.8", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 4: CONTACT FORM
# =============================================================================
contact_form_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
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
                    "widgetType": "heading",
                    "settings": {
                        "title": "Изпратете ни съобщение",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "36", "sizes": []},
                        "typography_font_weight": "700",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Попълнете формата по-долу и ние ще се свържем с вас възможно най-скоро.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "divider",
                    "settings": {
                        "color": "var(--e-global-color-primary)",
                        "weight": {"unit": "px", "size": "2", "sizes": []},
                        "width": {"unit": "%", "size": "50", "sizes": []},
                        "align": "center",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<div style='background: #f9f9f9; padding: 40px; border-radius: 8px; border: 2px dashed #FABA29; text-align: center;'><p style='font-size: 18px; color: #2C2C2C; margin: 0;'><strong>Contact Form 7 shortcode will be configured here</strong></p><p style='margin: 10px 0 0 0; color: #666;'>Form integration pending</p></div>",
                        "text_color": "var(--e-global-color-text)"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 5: MAP PLACEHOLDER
# =============================================================================
map_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",
        "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
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
                    "widgetType": "heading",
                    "settings": {
                        "title": "Намерете ни",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "36", "sizes": []},
                        "typography_font_weight": "700",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Интерактивна карта с локацията ще бъде добавена тук. Можете да използвате Google Maps widget от Elementor или да добавите iframe код за вградена карта.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "16", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "divider",
                    "settings": {
                        "color": "var(--e-global-color-primary)",
                        "weight": {"unit": "px", "size": "2", "sizes": []},
                        "width": {"unit": "%", "size": "30", "sizes": []},
                        "align": "center",
                        "margin": {"unit": "px", "top": "20", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# COMBINE ALL SECTIONS
# =============================================================================
elementor_data = [
    hero_section,
    contact_info_section,
    working_hours_section,
    contact_form_section,
    map_section
]

# =============================================================================
# UPDATE THE PAGE
# =============================================================================
def update_page():
    print("=" * 80)
    print("Building Contact Page (ID 27)")
    print("=" * 80)
    print(f"\nSections to create: {len(elementor_data)}")
    print("\n1. Hero Section - Контакти")
    print("2. Contact Information Section - 3 Icon Boxes (Address, Phone, Email)")
    print("3. Working Hours Section")
    print("4. Contact Form Section - Placeholder")
    print("5. Map Section - Placeholder")
    print("\n" + "=" * 80)

    # Prepare the data
    elementor_json = json.dumps(elementor_data)

    # Update post meta via REST API
    url = f"{base_url}/wp-json/wp/v2/pages/{page_id}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "meta": {
            "_elementor_data": elementor_json,
            "_elementor_edit_mode": "builder",
            "_elementor_page_settings": {
                "page_title": "",
                "page_layout": "elementor_full_width"
            }
        }
    }

    print("\nSending data to WordPress...")
    response = requests.post(url, auth=auth, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ SUCCESS! Contact page built successfully!")
        print(f"\nView page: {base_url}/contact/")
        print(f"Edit in Elementor: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
        print("\n" + "=" * 80)
        print("NEXT STEPS:")
        print("1. Clear Elementor cache")
        print("2. View the page to verify layout")
        print("3. Configure Contact Form 7 and replace placeholder")
        print("4. Add Google Maps widget or embed code")
        print("=" * 80)
    else:
        print(f"❌ ERROR: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_page()
