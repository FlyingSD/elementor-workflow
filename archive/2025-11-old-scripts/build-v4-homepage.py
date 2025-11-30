#!/usr/bin/env python3
"""
Build V4 Homepage Structure
Creates complete JSON structure for Homepage rebuild
"""

import json
import random
import string

def generate_id(length=7):
    """Generate random Elementor ID"""
    return ''.join(random.choices(string.hexdigits.lower()[:16], k=length))

# Build complete V4 structure
v4_structure = []

# =============================================================================
# SECTION 1: HERO (Yellow Gradient Background, 2 Columns)
# =============================================================================
hero_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "background_background": "gradient",
        "background_color": "#FEFCF5",
        "background_color_stop": {"unit": "%", "size": 0},
        "background_color_b": "#fff4d9",
        "background_color_b_stop": {"unit": "%", "size": 40},
        "background_gradient_type": "linear",
        "background_gradient_angle": {"unit": "deg", "size": 120},
        "padding": {
            "unit": "px",
            "top": "100",
            "right": "20",
            "bottom": "100",
            "left": "20",
            "isLinked": False
        },
        "min_height": {"unit": "px", "size": 650}
    },
    "elements": [
        # Column 1: Text Content (60%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 60,
                "_inline_size": 60,
                "content_position": "center"
            },
            "elements": [
                # H1 Heading
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "title": "Развийте математическите умения на вашето дете",
                        "header_size": "h1",
                        "align": "left",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "rem", "size": 3.25},
                        "typography_font_weight": "700",
                        "typography_line_height": {"unit": "em", "size": 1.15}
                    },
                    "elements": [],
                    "widgetType": "heading"
                },
                # Subtitle Text
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "editor": "<p>Ментална аритметика за деца от 5 до 12 години. Развиваме концентрация, логика и увереност чрез доказани методи в приятна и подкрепяща среда.</p>",
                        "align": "left",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "rem", "size": 1.25},
                        "typography_line_height": {"unit": "em", "size": 1.75}
                    },
                    "elements": [],
                    "widgetType": "text-editor"
                },
                # Primary Button
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "text": "Безплатен пробен урок",
                        "link": {"url": "#contact", "is_external": False, "nofollow": False},
                        "align": "left",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-primary)",
                        "border_radius": {
                            "unit": "px",
                            "top": "12",
                            "right": "12",
                            "bottom": "12",
                            "left": "12",
                            "isLinked": True
                        },
                        "button_padding": {
                            "unit": "px",
                            "top": "18",
                            "right": "40",
                            "bottom": "18",
                            "left": "40",
                            "isLinked": False
                        },
                        "button_box_shadow_box_shadow": {
                            "horizontal": 0,
                            "vertical": 6,
                            "blur": 20,
                            "spread": 0,
                            "color": "rgba(250, 186, 41, 0.35)"
                        },
                        "button_background_hover_color": "var(--e-global-color-secondary)",
                        "hover_animation": "grow"
                    },
                    "elements": [],
                    "widgetType": "button"
                },
                # Secondary Button
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "text": "Вижте програмите",
                        "link": {"url": "/programs/", "is_external": False, "nofollow": False},
                        "align": "left",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-accent)",
                        "border_radius": {
                            "unit": "px",
                            "top": "12",
                            "right": "12",
                            "bottom": "12",
                            "left": "12",
                            "isLinked": True
                        },
                        "button_padding": {
                            "unit": "px",
                            "top": "18",
                            "right": "40",
                            "bottom": "18",
                            "left": "40",
                            "isLinked": False
                        },
                        "button_box_shadow_box_shadow": {
                            "horizontal": 0,
                            "vertical": 6,
                            "blur": 20,
                            "spread": 0,
                            "color": "rgba(255, 140, 122, 0.35)"
                        },
                        "button_background_hover_color": "var(--e-global-color-secondary)"
                    },
                    "elements": [],
                    "widgetType": "button"
                }
            ],
            "isInner": False
        },
        # Column 2: Zhara Mascot Image (40%)
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 40,
                "_inline_size": 40,
                "content_position": "center"
            },
            "elements": [
                # Image Widget (Zhara mascot)
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "image": {
                            "url": "http://svetlinkielementor.local/wp-content/uploads/2025/11/Zhara-pointing-at-CTA.png",
                            "id": 129
                        },
                        "image_size": "full",
                        "align": "center",
                        "width": {"unit": "px", "size": 520},
                        "_box_shadow_box_shadow": {
                            "horizontal": 0,
                            "vertical": 15,
                            "blur": 40,
                            "spread": 0,
                            "color": "rgba(250, 186, 41, 0.25)"
                        }
                    },
                    "elements": [],
                    "widgetType": "image"
                }
            ],
            "isInner": False
        }
    ],
    "isInner": False
}

v4_structure.append(hero_section)

# =============================================================================
# SECTION 2: BLOG CAROUSEL (White Background)
# =============================================================================
blog_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {
            "unit": "px",
            "top": "90",
            "right": "20",
            "bottom": "90",
            "left": "20",
            "isLinked": False
        }
    },
    "elements": [
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                # Section Title
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "title": "От нашия блог",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "rem", "size": 2.5},
                        "typography_font_weight": "700",
                        "typography_line_height": {"unit": "em", "size": 1.3}
                    },
                    "elements": [],
                    "widgetType": "heading"
                },
                # Divider (Gradient Underline)
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "width": {"unit": "px", "size": 80},
                        "height": {"unit": "px", "size": 4},
                        "color": "var(--e-global-color-primary)",
                        "align": "center",
                        "gap": {"unit": "px", "size": 12}
                    },
                    "elements": [],
                    "widgetType": "divider"
                },
                # Image Carousel
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "carousel": [
                            {"id": "", "url": "http://svetlinkielementor.local/wp-content/uploads/2025/11/Zhara-pointing-at-CTA.png"}
                        ],
                        "slides_to_show": "1",
                        "slides_to_scroll": "1",
                        "navigation": "arrows",
                        "arrows": "yes",
                        "dots": "no",
                        "autoplay": "yes",
                        "autoplay_speed": 5000,
                        "infinite": "yes",
                        "speed": 500,
                        "arrows_color": "var(--e-global-color-primary)",
                        "arrows_size": {"unit": "px", "size": 55}
                    },
                    "elements": [],
                    "widgetType": "image-carousel"
                }
            ],
            "isInner": False
        }
    ],
    "isInner": False
}

v4_structure.append(blog_section)

# =============================================================================
# SECTION 3: BENEFITS (Cream Gradient Background, 3 Cards)
# =============================================================================
benefits_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "background_background": "gradient",
        "background_color": "#FEFCF5",
        "background_color_stop": {"unit": "%", "size": 0},
        "background_color_b": "#fff9e6",
        "background_color_b_stop": {"unit": "%", "size": 100},
        "background_gradient_type": "linear",
        "background_gradient_angle": {"unit": "deg", "size": 135},
        "padding": {
            "unit": "px",
            "top": "90",
            "right": "20",
            "bottom": "90",
            "left": "20",
            "isLinked": False
        }
    },
    "elements": [
        # Title Row
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "title": "Предимства на нашата програма",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "rem", "size": 2.5},
                        "typography_font_weight": "700"
                    },
                    "elements": [],
                    "widgetType": "heading"
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "width": {"unit": "px", "size": 80},
                        "height": {"unit": "px", "size": 4},
                        "color": "var(--e-global-color-primary)",
                        "align": "center",
                        "gap": {"unit": "px", "size": 12}
                    },
                    "elements": [],
                    "widgetType": "divider"
                }
            ],
            "isInner": False
        }
    ],
    "isInner": False
}

# Add 3 columns for benefit cards
benefit_cards_data = [
    {
        "icon": "fas fa-brain",
        "title": "По-добра концентрация",
        "description": "Вашето дете ще научи да се фокусира върху задачи за по-дълго време и да игнорира разсейванията.",
        "border_color": "var(--e-global-color-primary)",
        "icon_bg": "var(--e-global-color-primary)"
    },
    {
        "icon": "fas fa-lightbulb",
        "title": "Логическо мислене",
        "description": "Развиваме способността за анализиране на проблеми и намиране на творчески решения.",
        "border_color": "var(--e-global-color-accent)",
        "icon_bg": "var(--e-global-color-accent)"
    },
    {
        "icon": "fas fa-star",
        "title": "Отлична памет",
        "description": "Чрез визуализация и повторение укрепваме паметта и способността за запаметяване.",
        "border_color": "var(--e-global-color-secondary)",
        "icon_bg": "var(--e-global-color-secondary)"
    }
]

for card_data in benefit_cards_data:
    benefits_section["elements"].append({
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 33, "_inline_size": 33},
        "elements": [
            {
                "id": generate_id(),
                "elType": "widget",
                "settings": {
                    "selected_icon": {"value": card_data["icon"], "library": "fa-solid"},
                    "title_text": card_data["title"],
                    "description_text": card_data["description"],
                    "position": "top",
                    "title_color": "var(--e-global-color-text)",
                    "description_color": "#5a6c6d",
                    "icon_primary_color": "#FFFFFF",
                    "icon_size": {"unit": "px", "size": 38},
                    "icon_space": {"unit": "px", "size": 22},
                    "icon_padding": {
                        "unit": "px",
                        "top": "18",
                        "right": "18",
                        "bottom": "18",
                        "left": "18",
                        "isLinked": True
                    },
                    "icon_border_radius": {
                        "unit": "%",
                        "top": "50",
                        "right": "50",
                        "bottom": "50",
                        "left": "50",
                        "isLinked": True
                    },
                    "icon_background_color": card_data["icon_bg"],
                    "border_border": "solid",
                    "border_width": {
                        "unit": "px",
                        "top": "5",
                        "right": "0",
                        "bottom": "0",
                        "left": "0",
                        "isLinked": False
                    },
                    "border_color": card_data["border_color"],
                    "border_radius": {
                        "unit": "px",
                        "top": "20",
                        "right": "20",
                        "bottom": "20",
                        "left": "20",
                        "isLinked": True
                    },
                    "background_background": "classic",
                    "background_color": "#FFFFFF",
                    "padding": {
                        "unit": "px",
                        "top": "45",
                        "right": "35",
                        "bottom": "45",
                        "left": "35",
                        "isLinked": False
                    },
                    "_box_shadow_box_shadow": {
                        "horizontal": 0,
                        "vertical": 10,
                        "blur": 35,
                        "spread": 0,
                        "color": "rgba(0, 0, 0, 0.1)"
                    }
                },
                "elements": [],
                "widgetType": "icon-box"
            }
        ],
        "isInner": False
    })

v4_structure.append(benefits_section)

# =============================================================================
# SECTION 4: PROGRAMS TEASER (White Background, 3 Cards)
# =============================================================================
programs_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {
            "unit": "px",
            "top": "90",
            "right": "20",
            "bottom": "90",
            "left": "20",
            "isLinked": False
        }
    },
    "elements": [
        # Title Row
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "title": "Нашите програми",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "rem", "size": 2.5},
                        "typography_font_weight": "700"
                    },
                    "elements": [],
                    "widgetType": "heading"
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "settings": {
                        "width": {"unit": "px", "size": 80},
                        "height": {"unit": "px", "size": 4},
                        "color": "var(--e-global-color-primary)",
                        "align": "center",
                        "gap": {"unit": "px", "size": 12}
                    },
                    "elements": [],
                    "widgetType": "divider"
                }
            ],
            "isInner": False
        }
    ],
    "isInner": False
}

# Add 3 columns for program teaser cards
program_cards_data = [
    {
        "title": "5 нива на обучение",
        "description": "• Ниво 1: Основи с абакус\\n• Ниво 2: Ментална визуализация\\n• Ниво 3: Сложни операции\\n• Ниво 4: Майсторско ниво\\n• Ниво 5: Състезателна група",
        "button_text": "Прочети повече",
        "button_link": "/programs/",
        "border_color": "var(--e-global-color-primary)"
    },
    {
        "title": "Специални промоции",
        "description": "Безплатен пробен урок за всяко ново дете!\\n\\n10% отстъпка при записване на второ дете от семейството\\n\\n* Промоциите са валидни за нови записвания до края на месеца.",
        "button_text": "Прочети повече",
        "button_link": "/programs/#pricing",
        "border_color": "var(--e-global-color-accent)"
    },
    {
        "title": "Имате въпроси?",
        "description": "Отговорихме на най-честите въпроси на родителите:\\n\\n• Колко струва обучението?\\n• Колко деца има в група?\\n• Колко време трае програмата?\\n• Какви са резултатите?\\n\\n...и още 16 въпроса!",
        "button_text": "Прочети повече",
        "button_link": "/faq/",
        "border_color": "var(--e-global-color-secondary)"
    }
]

for card_data in program_cards_data:
    programs_section["elements"].append({
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 33, "_inline_size": 33},
        "elements": [
            # Icon Box (Card styling)
            {
                "id": generate_id(),
                "elType": "widget",
                "settings": {
                    "selected_icon": {"value": "fas fa-book", "library": "fa-solid"},
                    "title_text": card_data["title"],
                    "description_text": card_data["description"],
                    "position": "top",
                    "title_color": "var(--e-global-color-text)",
                    "description_color": "#5a6c6d",
                    "icon_primary_color": "var(--e-global-color-primary)",
                    "icon_size": {"unit": "px", "size": 52},
                    "border_border": "solid",
                    "border_width": {
                        "unit": "px",
                        "top": "5",
                        "right": "0",
                        "bottom": "0",
                        "left": "0",
                        "isLinked": False
                    },
                    "border_color": card_data["border_color"],
                    "border_radius": {
                        "unit": "px",
                        "top": "20",
                        "right": "20",
                        "bottom": "20",
                        "left": "20",
                        "isLinked": True
                    },
                    "background_background": "classic",
                    "background_color": "#FFFFFF",
                    "padding": {
                        "unit": "px",
                        "top": "45",
                        "right": "35",
                        "bottom": "45",
                        "left": "35",
                        "isLinked": False
                    },
                    "_box_shadow_box_shadow": {
                        "horizontal": 0,
                        "vertical": 10,
                        "blur": 35,
                        "spread": 0,
                        "color": "rgba(0, 0, 0, 0.1)"
                    }
                },
                "elements": [],
                "widgetType": "icon-box"
            },
            # Button below card
            {
                "id": generate_id(),
                "elType": "widget",
                "settings": {
                    "text": card_data["button_text"],
                    "link": {"url": card_data["button_link"], "is_external": False, "nofollow": False},
                    "align": "center",
                    "button_text_color": "#FFFFFF",
                    "background_color": "var(--e-global-color-accent)",
                    "border_radius": {
                        "unit": "px",
                        "top": "12",
                        "right": "12",
                        "bottom": "12",
                        "left": "12",
                        "isLinked": True
                    },
                    "button_padding": {
                        "unit": "px",
                        "top": "18",
                        "right": "40",
                        "bottom": "18",
                        "left": "40",
                        "isLinked": False
                    },
                    "button_background_hover_color": "var(--e-global-color-secondary)"
                },
                "elements": [],
                "widgetType": "button"
            }
        ],
        "isInner": False
    })

v4_structure.append(programs_section)

# Save to file
output_file = "v4-homepage-structure.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(v4_structure, f, indent=2, ensure_ascii=False)

print("SUCCESS: V4 Homepage structure built successfully!")
print(f"Saved to: {output_file}")
print(f"Total sections: {len(v4_structure)}")
print("Sections:")
for i, section in enumerate(v4_structure, 1):
    section_name = ["Hero", "Blog Carousel", "Benefits", "Programs Teaser"][i-1]
    widgets_count = sum(len(col.get("elements", [])) for col in section.get("elements", []))
    print(f"   {i}. {section_name} - {len(section.get('elements', []))} columns, {widgets_count} widgets")
