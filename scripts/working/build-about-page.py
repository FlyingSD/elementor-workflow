#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build About Page (ID 23) - Svetlinki Elementor
Uses SECTIONS (not Containers) - Elementor FREE compatible
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 23

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
        "background_color": "var(--e-global-color-accent)",  # Cream
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
                        "title": "За нашия екип",
                        "header_size": "h1",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
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
                        "editor": "<p>Запознайте се с екипа, който прави образованието забавно и ефективно</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "20", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 2: MISSION
# =============================================================================
mission_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
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
                        "title": "Нашата Мисия",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "30", "sizes": []},
                        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "30", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Ние вярваме, че всяко дете притежава гений, който чака да бъде отключен. Нашата мисия е да предоставим инструментите и увереността, от които децата се нуждаят, за да успеят, чрез доказаните методи на менталната аритметика.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>С повече от 10 години опит, нашите сертифицирани преподаватели са посветени на създаването на подкрепяща и забавна учебна среда.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "divider",
                    "settings": {
                        "color": "var(--e-global-color-primary)",
                        "weight": {"unit": "px", "size": "3", "sizes": []},
                        "width": {"unit": "%", "size": "50", "sizes": []},
                        "gap": {"unit": "px", "size": "30", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<blockquote style=\"font-style: italic; font-size: 22px; text-align: center; border-left: 4px solid var(--e-global-color-primary); padding-left: 20px; margin: 30px auto; max-width: 700px;\">\"Умът не е съд, който трябва да бъде запълнен, а огън, който трябва да бъде запален.\"</blockquote>",
                        "text_color": "var(--e-global-color-text)"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 3: VALUES (4 Icon Boxes)
# =============================================================================
values_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": []
}

# Add heading in full-width column first
heading_column = {
    "id": generate_id(),
    "elType": "column",
    "settings": {"_column_size": 100},
    "elements": [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Нашите Ценности",
                "header_size": "h2",
                "align": "center",
                "title_color": "var(--e-global-color-secondary)",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": "30", "sizes": []},
                "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
            }
        }
    ]
}
values_section["elements"].append(heading_column)

# Values data
values = [
    {
        "icon": "fas fa-clock",
        "title": "Търпение",
        "description": "Всяко дете учи със собствен темп."
    },
    {
        "icon": "fas fa-smile",
        "title": "Позитивизъм",
        "description": "Ученето трябва да бъде радост, а не задължение."
    },
    {
        "icon": "fas fa-star",
        "title": "Професионализъм",
        "description": "Винаги се стремим към най-високите стандарти."
    },
    {
        "icon": "fas fa-user",
        "title": "Индивидуален подход",
        "description": "Всяко дете е уникално и заслужава персонализирано внимание."
    }
]

# Create 4 columns for values
for value in values:
    column = {
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 25},
        "elements": [
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "icon-box",
                "settings": {
                    "selected_icon": {"value": value["icon"], "library": "fa-solid"},
                    "icon_color": "var(--e-global-color-primary)",
                    "icon_size": {"unit": "px", "size": "50", "sizes": []},
                    "title_text": value["title"],
                    "title_color": "var(--e-global-color-text)",
                    "description_text": value["description"],
                    "description_color": "var(--e-global-color-text)",
                    "position": "top",
                    "content_vertical_alignment": "top"
                }
            }
        ]
    }
    values_section["elements"].append(column)

# =============================================================================
# SECTION 4: TEAM (2 Members)
# =============================================================================
team_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": []
}

# Add heading in full-width column first
team_heading_column = {
    "id": generate_id(),
    "elType": "column",
    "settings": {"_column_size": 100},
    "elements": [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Нашият Екип",
                "header_size": "h2",
                "align": "center",
                "title_color": "var(--e-global-color-secondary)",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": "30", "sizes": []},
                "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "40", "left": "0", "isLinked": False}
            }
        }
    ]
}
team_section["elements"].append(team_heading_column)

# Team members data
team_members = [
    {
        "name": "Деница Илчева - Дени",
        "title": "Сертифициран инструктор по ментална аритметика",
        "bio": "Математическа гимназия – Плевен. С дългогодишен опит в работата с деца, Деница е водещ учител в детска градина, където обучава деца от 4 до 5 годишна възраст чрез иновативни методи, развиващи логическото мислене, концентрацията и увереността."
    },
    {
        "name": "Симона Ефремова - Мони",
        "title": "Сертифициран инструктор по ментална аритметика",
        "bio": "Създател на платформата ZadaZnam - образователна платформа за ранно детско развитие. Учителски опит като преподавател в детска градина на възрастова група от 5 до 6 годишни деца."
    }
]

# Create 2 columns for team members
for member in team_members:
    column = {
        "id": generate_id(),
        "elType": "column",
        "settings": {
            "_column_size": 50,
            "background_background": "classic",
            "background_color": "var(--e-global-color-accent)",
            "padding": {"unit": "px", "top": "40", "right": "40", "bottom": "40", "left": "40", "isLinked": True},
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
            "border_color": "#E0E0E0"
        },
        "elements": [
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "icon-box",
                "settings": {
                    "selected_icon": {"value": "fas fa-user-circle", "library": "fa-solid"},
                    "icon_color": "var(--e-global-color-primary)",
                    "icon_size": {"unit": "px", "size": "80", "sizes": []},
                    "title_text": member["name"],
                    "title_color": "var(--e-global-color-secondary)",
                    "description_text": f"<p><strong>{member['title']}</strong></p>",
                    "description_color": "var(--e-global-color-text)",
                    "position": "top",
                    "content_vertical_alignment": "top"
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p>{member['bio']}</p>",
                    "text_color": "var(--e-global-color-text)",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                    "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                }
            }
        ]
    }
    team_section["elements"].append(column)

# =============================================================================
# BUILD PAGE STRUCTURE
# =============================================================================
page_data = [
    hero_section,
    mission_section,
    values_section,
    team_section
]

# Update page via WordPress REST API
elementor_data_string = json.dumps(page_data)

response = requests.post(
    f"{base_url}/wp-json/wp/v2/pages/{page_id}",
    auth=auth,
    json={
        "meta": {
            "_elementor_data": elementor_data_string,
            "_elementor_edit_mode": "builder"
        }
    }
)

if response.status_code == 200:
    print("SUCCESS: About page built successfully!")
    print(f"Edit URL: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
    print(f"View URL: {base_url}/?page_id={page_id}")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
