#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild COMPLETE Homepage with ALL 6 Sections in Correct Order
Uses SECTIONS (not Containers) - Elementor FREE compatible
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 21

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# =============================================================================
# SECTION 1: HERO (Full-Width, Cream Background)
# =============================================================================
hero_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",  # Full-width
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
                # H1 Heading
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Развийте <strong>Математическите Умения</strong> на Вашето Дете",
                        "header_size": "h1",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",  # Teal
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "48", "sizes": []},
                        "typography_font_weight": "700",
                        "typography_line_height": {"unit": "em", "size": "1.2", "sizes": []}
                    }
                },
                # Subtitle
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Професионални обучения по математика за деца от 4 до 16 години</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "20", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                },
                # Counter 1: 500+ ученици
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "counter",
                    "settings": {
                        "starting_number": 0,
                        "ending_number": 500,
                        "suffix": "+",
                        "duration": 2000,
                        "title": "ученици",
                        "number_color": "var(--e-global-color-primary)",  # Yellow
                        "title_color": "var(--e-global-color-text)",
                        "align": "center"
                    }
                },
                # Counter 2: 8+ Години опит
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "counter",
                    "settings": {
                        "starting_number": 0,
                        "ending_number": 8,
                        "suffix": "+",
                        "duration": 2000,
                        "title": "Години опит",
                        "number_color": "var(--e-global-color-primary)",
                        "title_color": "var(--e-global-color-text)",
                        "align": "center"
                    }
                },
                # CTA Button
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "ЗАПАЗИ СЕ СЕГА",
                        "link": {"url": "#contact"},
                        "align": "center",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-primary)",  # Yellow
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 2: BENEFITS (3 Cards with Icon Boxes)
# =============================================================================
benefits_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": [
        # Heading column (full width)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [{
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": 'Защо да изберете "Светлинки"?',
                    "header_size": "h2",
                    "title_color": "var(--e-global-color-secondary)",
                    "align": "center"
                }
            }]
        }
    ]
}

# Add 3 benefit cards
benefit_cards = [
    {"title": "По-добра Концентрация", "description": "Нашите методи подобряват фокуса и вниманието към детайла.", "icon": "fas fa-brain"},
    {"title": "Логическо Мислене", "description": "Децата се научават да решават проблеми бързо и ефективно.", "icon": "fas fa-lightbulb"},
    {"title": "Отлична Памет", "description": "Визуалните техники стимулират фотографската памет.", "icon": "fas fa-memory"}
]

for card in benefit_cards:
    benefits_section["elements"].append({
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 33},
        "elements": [{
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "icon-box",
            "settings": {
                "title_text": card["title"],
                "description_text": card["description"],
                "selected_icon": {"value": card["icon"], "library": "fa-solid"},
                "icon_color": "var(--e-global-color-primary)",
                "title_color": "var(--e-global-color-secondary)",
                "description_color": "var(--e-global-color-text)",
                "position": "top",
                "content_vertical_alignment": "top"
            }
        }]
    })

# =============================================================================
# GET EXISTING SECTIONS 3-6 (Programs, Pricing, Testimonials, Contact)
# =============================================================================
print("Fetching existing sections from page...")
response = requests.get(f"{base_url}/wp-json/wp/v2/pages/{page_id}", auth=auth)
page_data = response.json()

elementor_data_str = page_data.get('meta', {}).get('_elementor_data', '[]')
if isinstance(elementor_data_str, str):
    existing_sections = json.loads(elementor_data_str) if elementor_data_str else []
else:
    existing_sections = elementor_data_str

print(f"Found {len(existing_sections)} existing sections (should be 4: Programs, Pricing, Testimonials, Contact)")

# =============================================================================
# ASSEMBLE ALL 6 SECTIONS IN CORRECT ORDER
# =============================================================================
all_sections = [
    hero_section,        # Section 1: Hero
    benefits_section,    # Section 2: Benefits (3 cards)
    *existing_sections   # Sections 3-6: Programs, Pricing, Testimonials, Contact
]

print(f"\nTotal sections to save: {len(all_sections)}")
print("Order:")
print("  1. Hero (full-width, cream bg)")
print("  2. Benefits (3 cards)")
print("  3. Programs (5 levels)")
print("  4. Pricing CTA")
print("  5. Testimonials (2 cards)")
print("  6. Contact")

# =============================================================================
# SAVE TO DATABASE
# =============================================================================
print("\nSaving to database...")
update_response = requests.post(
    f"{base_url}/wp-json/wp/v2/pages/{page_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps(all_sections, ensure_ascii=False)}}
)

if update_response.status_code == 200:
    print("\n✅ SUCCESS! All 6 sections saved to database!")
    print(f"\nView: {base_url}/home-2/")
    print(f"Edit: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
    print("\n⚠️  IMPORTANT: Open Elementor editor and click 'Update' to trigger hooks!")
    print("⚠️  THEN: Clear Elementor cache to see changes on frontend")
else:
    print(f"\n❌ ERROR: {update_response.status_code}")
    print(update_response.text)
