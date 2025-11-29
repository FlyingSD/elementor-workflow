import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 21

def generate_id():
    """Generate random 7-character hex ID like Elementor does"""
    return ''.join(random.choices('0123456789abcdef', k=7))

# Section 2: Benefits (3 cards)
section_benefits = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "",  # Not stretched, boxed content
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {
            "unit": "px",
            "top": 80,
            "right": 20,
            "bottom": 80,
            "left": 20,
            "isLinked": False
        },
        "gap": "default"
    },
    "elements": [
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 100,
                "_inline_size": None
            },
            "elements": [
                # Heading H2
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Защо да изберете \"Светлинки\"?",
                        "header_size": "h2",
                        "title_color": "var(--e-global-color-secondary)",
                        "align": "center",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                        "typography_line_height": {"unit": "em", "size": 1.2, "sizes": []}
                    }
                }
            ]
        }
    ]
}

# Add 3 benefit cards as separate columns
benefit_cards = [
    {
        "title": "По-добра Концентрация",
        "description": "Нашите методи подобряват фокуса и вниманието към детайла.",
        "icon": "fas fa-brain"
    },
    {
        "title": "Логическо Мислене",
        "description": "Децата се научават да решават проблеми бързо и ефективно.",
        "icon": "fas fa-lightbulb"
    },
    {
        "title": "Отлична Памет",
        "description": "Визуалните техники стимулират фотографската памет.",
        "icon": "fas fa-memory"
    }
]

# Create 3-column row for cards
for card in benefit_cards:
    column = {
        "id": generate_id(),
        "elType": "column",
        "settings": {
            "_column_size": 33,  # 33% width for 3 columns
            "_inline_size": None
        },
        "elements": [
            # Icon Box widget
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "icon-box",
                "settings": {
                    "title_text": card["title"],
                    "description_text": card["description"],
                    "selected_icon": {"value": card["icon"], "library": "fa-solid"},
                    "icon_color": "var(--e-global-color-primary)",
                    "icon_size": {"unit": "px", "size": 48, "sizes": []},
                    "title_color": "var(--e-global-color-secondary)",
                    "description_color": "var(--e-global-color-text)",
                    "content_vertical_alignment": "top",
                    "position": "top",
                    "title_size": "h3"
                }
            }
        ]
    }
    section_benefits["elements"].append(column)

print("Building Section 2: Benefits (3 cards)...")
print(json.dumps(section_benefits, indent=2, ensure_ascii=False))
print("\n" + "="*60)
print("Section JSON structure created!")
print("Next: Get current page data and append this section")
