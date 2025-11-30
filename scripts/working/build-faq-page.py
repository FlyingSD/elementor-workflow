#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build FAQ Page (ID 29) - Svetlinki Elementor
Uses SECTIONS (not Containers) - Elementor FREE compatible
Uses Accordion widget for Q&A pairs
"""

import requests
import json
import random
import sys

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 29

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
                        "title": "Често задавани въпроси",
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
                        "editor": "<p>Намерете отговори на най-често срещаните въпроси</p>",
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
# SECTION 2: FAQ ACCORDION
# =============================================================================
faq_section = {
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
            "settings": {
                "_column_size": 100,
                "content_width": "full"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Въпроси и отговори",
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
                    "widgetType": "accordion",
                    "settings": {
                        "tabs": [
                            {
                                "_id": generate_id(),
                                "tab_title": "На каква възраст приемате деца?",
                                "tab_content": "<p>Приемаме деца от 3 до 12 години. Програмите са разделени на възрастови групи, за да осигурим най-подходящата среда за всяко дете.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Какво е включено в цената?",
                                "tab_content": "<p>Цената включва всички материали, оборудване и осигуровки. Не се изискват допълнителни такси освен ако не избирате допълнителни услуги като транспорт или разширена програма.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Имате ли програми за напреднали?",
                                "tab_content": "<p>Да, предлагаме 5 нива на обучение - от начинаещи до напреднали състезатели. Всяко дете се оценява индивидуално и се насочва към подходящото ниво.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Как се случва записването?",
                                "tab_content": "<p>Записването става онлайн чрез нашата форма или на място в офиса. След попълване на формата ще се свържем с вас за уточняване на детайли и насрочване на първа тренировка.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Какво оборудване е необходимо?",
                                "tab_content": "<p>За начинаещи предоставяме цялото необходимо оборудване. За напреднали препоръчваме собствено екипировка, като предлагаме отстъпки от партньорски магазини.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Има ли пробни тренировки?",
                                "tab_content": "<p>Да, предлагаме една безплатна пробна тренировка за всяко ново дете. Това позволява на детето да опита спорта преди да се ангажирате с абонамент.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Какви са изискванията за здравословно състояние?",
                                "tab_content": "<p>Изисква се медицинско свидетелство за допускане до спортни занимания. При хронични заболявания или специални нужди, моля консултирайте се с нас предварително.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Предлагате ли транспорт?",
                                "tab_content": "<p>Да, предлагаме транспорт от и до определени точки в София срещу допълнително заплащане. Вижте секцията \"Програми\" за подробности.</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Какво се случва при отсъствие?",
                                "tab_content": "<p>При планирано отсъствие можете да компенсирате часовете в друга група или да ги пренесете за следващия месец (при дългосрочни абонаменти).</p>"
                            },
                            {
                                "_id": generate_id(),
                                "tab_title": "Организирате ли лагери и състезания?",
                                "tab_content": "<p>Да, организираме летни и зимни лагери, както и участие в местни и национални състезания за напреднали нива.</p>"
                            }
                        ],
                        "title_color": "var(--e-global-color-text)",
                        "title_typography_typography": "custom",
                        "title_typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "title_typography_font_weight": "600",
                        "content_color": "var(--e-global-color-text)",
                        "content_typography_typography": "custom",
                        "content_typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
                        "border_color": "#E5E5E5",
                        "icon_color": "var(--e-global-color-primary)",  # Yellow for icon
                        "icon_active_color": "var(--e-global-color-secondary)",  # Teal when active
                        "space_between_items": {"unit": "px", "size": "15", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 3: CTA - Still Have Questions?
# =============================================================================
cta_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",  # Cream #FEFCF5
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
                        "title": "Не намерихте отговора?",
                        "header_size": "h3",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "32", "sizes": []},
                        "typography_font_weight": "700",
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Свържете се с нас директно и ще отговорим на всички ваши въпроси</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "Свържете се с нас",
                        "link": {"url": "/contact/", "is_external": "", "nofollow": ""},
                        "align": "center",
                        "button_type": "default",
                        "button_background_color": "var(--e-global-color-primary)",  # Yellow
                        "button_text_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600",
                        "button_border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
                        "button_padding": {"unit": "px", "top": "18", "right": "40", "bottom": "18", "left": "40", "isLinked": False}
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
    faq_section,
    cta_section
]

# =============================================================================
# SAVE TO JSON FILE FOR WP-CLI IMPORT
# =============================================================================
print("=" * 80)
print("Building FAQ Page (ID: 29)")
print("=" * 80)
print()

print(f"Number of sections: {len(elementor_data)}")
print(f"  - Hero section")
print(f"  - FAQ Accordion (10 Q&A pairs)")
print(f"  - CTA section")
print()

# Save JSON to file for PHP import
json_file = "faq-page-data.json"
try:
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(elementor_data, f, ensure_ascii=False, indent=2)
    print(f"JSON data saved to: {json_file}")
    print()
    print("Run the following command to import:")
    print("  wp eval-file scripts/working/import-faq-page.php")
    sys.exit(0)

except Exception as e:
    print(f"ERROR saving JSON: {str(e)}")
    sys.exit(1)
