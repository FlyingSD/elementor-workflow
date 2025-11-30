#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Programs Page (ID 25) - Svetlinki Elementor
Uses SECTIONS (not Containers) - Elementor FREE compatible
"""

import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 25

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
                        "title": "Нашата 5-степенна програма",
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
                        "editor": "<p>От начинаещи до състезатели - всяко дете започва от Ниво 1</p>",
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
# SECTION 2: PHILOSOPHY (Yellow Box)
# =============================================================================
philosophy_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-primary)",  # Yellow
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
                        "title": "Открийте потенциала",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "30", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>\"Трябва ли да започнем от Ниво 1?\" Това е въпрос, който чуваме всеки ден. Отговорът е категорично \"Да\". Това е нашата философия - всяко дете започва от основите, без значение от възрастта. Защото здравата основа е всичко.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 3: PROGRAM CARDS (5 Levels)
# =============================================================================
programs_section = {
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

# Program data
programs = [
    {
        "title": "Ниво 1: Начална Група",
        "description": "Тук изграждаме любов към числата. Превръщаме \"Не искам\" в \"Искам още!\" чрез игра и забавление.",
        "duration": "12 месеца",
        "frequency": "1 път седмично (60 мин)",
        "group_size": "До 8 деца",
        "price": "160 лв."
    },
    {
        "title": "Ниво 2: Средна Група",
        "description": "Основата е здрава, сега надграждаме. Умножението и делението се превръщат в интересно предизвикателство.",
        "duration": "18 месеца",
        "frequency": "1 път седмично (75 мин)",
        "group_size": "До 10 деца",
        "price": "160 лв."
    },
    {
        "title": "Ниво 3: Напреднала Група",
        "description": "Тук ученикът започва да се отличава. Уменията се задълбочават и подготвяме желаещите за първи състезания.",
        "duration": "24 месеца",
        "frequency": "1 път седмично (90 мин)",
        "group_size": "До 12 деца",
        "price": "160 лв."
    },
    {
        "title": "Ниво 4: Майсторска Група",
        "description": "Това е нивото за задълбочен анализ. Превръщаме фокуса в лазер. Дроби, проценти – всичко идва на мястото си.",
        "duration": "24 месеца",
        "frequency": "1 път седмично (90 мин)",
        "group_size": "До 12 деца",
        "price": "160 лв."
    },
    {
        "title": "Ниво 5: Състезателна Група",
        "description": "Нивото на шампионите. Тук развиваме състезателен дух, бързина на мисълта и увереност.",
        "duration": "24 месеца",
        "frequency": "1 път седмично (90 мин)",
        "group_size": "До 12 деца",
        "price": "160 лв."
    }
]

# Create program cards - 2 cards per row
for i in range(0, len(programs), 2):
    row_columns = []

    # First card
    program = programs[i]
    card_elements = [
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": program["title"],
                "header_size": "h3",
                "title_color": "var(--e-global-color-secondary)",
                "typography_typography": "custom",
                "typography_font_size": {"unit": "px", "size": "22", "sizes": []}
            }
        },
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": f"<p>{program['description']}</p>",
                "text_color": "var(--e-global-color-text)"
            }
        },
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "divider",
            "settings": {}
        },
        {
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": f"<p><strong>Продължителност:</strong> {program['duration']}<br><strong>Занятия:</strong> {program['frequency']}<br><strong>Група:</strong> {program['group_size']}<br><strong>Цена:</strong> {program['price']}</p>",
                "text_color": "var(--e-global-color-text)"
            }
        }
    ]

    first_column = {
        "id": generate_id(),
        "elType": "column",
        "settings": {
            "_column_size": 50,
            "background_background": "classic",
            "background_color": "var(--e-global-color-accent)",
            "padding": {"unit": "px", "top": "30", "right": "30", "bottom": "30", "left": "30", "isLinked": True},
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
            "border_color": "#E0E0E0"
        },
        "elements": card_elements
    }
    row_columns.append(first_column)

    # Second card (if exists)
    if i + 1 < len(programs):
        program = programs[i + 1]
        card_elements = [
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": program["title"],
                    "header_size": "h3",
                    "title_color": "var(--e-global-color-secondary)",
                    "typography_typography": "custom",
                    "typography_font_size": {"unit": "px", "size": "22", "sizes": []}
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p>{program['description']}</p>",
                    "text_color": "var(--e-global-color-text)"
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "divider",
                "settings": {}
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p><strong>Продължителност:</strong> {program['duration']}<br><strong>Занятия:</strong> {program['frequency']}<br><strong>Група:</strong> {program['group_size']}<br><strong>Цена:</strong> {program['price']}</p>",
                    "text_color": "var(--e-global-color-text)"
                }
            }
        ]

        second_column = {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "background_background": "classic",
                "background_color": "var(--e-global-color-accent)",
                "padding": {"unit": "px", "top": "30", "right": "30", "bottom": "30", "left": "30", "isLinked": True},
                "border_border": "solid",
                "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                "border_color": "#E0E0E0"
            },
            "elements": card_elements
        }
        row_columns.append(second_column)

    programs_section["elements"].extend(row_columns)

# =============================================================================
# SECTION 4: CTA (Yellow Background)
# =============================================================================
cta_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-primary)",  # Yellow
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
                        "title": "Вярвате ли, че Вашето дете може повече?",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "30", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Вие не търсите просто курс по математика. Вие търсите начин да отключите потенциала на детето си. И ние знаем как да го направим.</p>",
                        "align": "center",
                        "text_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "Запишете се за безплатен пробен урок",
                        "link": {"url": "#contact", "is_external": "", "nofollow": ""},
                        "align": "center",
                        "button_type": "default",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-secondary)",
                        "button_background_hover_color": "var(--e-global-color-text)",
                        "border_radius": {"unit": "px", "top": "5", "right": "5", "bottom": "5", "left": "5", "isLinked": True},
                        "button_padding": {"unit": "px", "top": "15", "right": "30", "bottom": "15", "left": "30", "isLinked": False}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 5: PRICING TABLES
# =============================================================================
pricing_section = {
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
                        "title": "Нашата Радикална Прозрачност: Цени и Отстъпки",
                        "header_size": "h2",
                        "align": "center",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "30", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Основни планове",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "24", "sizes": []},
                        "margin": {"unit": "px", "top": "40", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": """<table style="width:100%; border-collapse: collapse;">
<thead>
<tr style="background-color: var(--e-global-color-primary);">
<th style="padding:15px; border:1px solid #ddd;">Услуга</th>
<th style="padding:15px; border:1px solid #ddd;">План</th>
<th style="padding:15px; border:1px solid #ddd;">Цена</th>
<th style="padding:15px; border:1px solid #ddd;">Детайли</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Обучение в група</td>
<td style="padding:15px; border:1px solid #ddd;">План "Гъвкав"</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>160 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">4 посещения в месеца</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Индивидуално обучение</td>
<td style="padding:15px; border:1px solid #ddd;">План "Гъвкав"</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>220 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">4 индивидуални посещения</td>
</tr>
</tbody>
</table>""",
                        "text_color": "var(--e-global-color-text)"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "План \"Ангажиран\" (Ниво 2-5)",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "24", "sizes": []},
                        "margin": {"unit": "px", "top": "40", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": """<table style="width:100%; border-collapse: collapse;">
<thead>
<tr style="background-color: var(--e-global-color-secondary); color: white;">
<th style="padding:15px; border:1px solid #ddd;">Ниво</th>
<th style="padding:15px; border:1px solid #ddd;">Стандартна цена</th>
<th style="padding:15px; border:1px solid #ddd;">Цена "Ангажиран"</th>
<th style="padding:15px; border:1px solid #ddd;">Спестявате</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Ниво 2 (16 урока / 4 мес.)</td>
<td style="padding:15px; border:1px solid #ddd;">640 лв.</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>580 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd; color: green;">60 лв.</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Ниво 3 (16 урока / 4 мес.)</td>
<td style="padding:15px; border:1px solid #ddd;">640 лв.</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>580 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd; color: green;">60 лв.</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Ниво 4 (16 урока / 4 мес.)</td>
<td style="padding:15px; border:1px solid #ddd;">640 лв.</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>580 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd; color: green;">60 лв.</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Ниво 5 (16 урока / 4 мес.)</td>
<td style="padding:15px; border:1px solid #ddd;">640 лв.</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>580 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd; color: green;">60 лв.</td>
</tr>
</tbody>
</table>""",
                        "text_color": "var(--e-global-color-text)"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Други услуги",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-text)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "24", "sizes": []},
                        "margin": {"unit": "px", "top": "40", "right": "0", "bottom": "20", "left": "0", "isLinked": False}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": """<table style="width:100%; border-collapse: collapse;">
<thead>
<tr style="background-color: var(--e-global-color-primary);">
<th style="padding:15px; border:1px solid #ddd;">Услуга</th>
<th style="padding:15px; border:1px solid #ddd;">Цена</th>
<th style="padding:15px; border:1px solid #ddd;">Детайли</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Пробен урок</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>0 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">Напълно безплатен</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Единичен урок (в група)</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>50 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">За наваксване</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Единичен урок (индивидуален)</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>70 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">За наваксване</td>
</tr>
<tr>
<td style="padding:15px; border:1px solid #ddd;">Стартов учебен комплект</td>
<td style="padding:15px; border:1px solid #ddd;"><strong>40 лв.</strong></td>
<td style="padding:15px; border:1px solid #ddd;">Еднократно. Включва Абакус</td>
</tr>
</tbody>
</table>""",
                        "text_color": "var(--e-global-color-text)"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# SECTION 6: DISCOUNTS
# =============================================================================
discounts_section = {
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
        # Column 1: Текущи отстъпки
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 50},
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Текущи отстъпки",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "24", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "icon-box",
                    "settings": {
                        "selected_icon": {"value": "fas fa-users", "library": "fa-solid"},
                        "icon_color": "var(--e-global-color-primary)",
                        "title_text": "Семейна отстъпка",
                        "title_color": "var(--e-global-color-text)",
                        "description_text": "20% за 2 деца, 30% за 3+ деца от едно семейство"
                    }
                }
            ]
        },
        # Column 2: Еднократни бонуси
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 50},
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Еднократни бонуси",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "24", "sizes": []}
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "icon-box",
                    "settings": {
                        "selected_icon": {"value": "fas fa-gift", "library": "fa-solid"},
                        "icon_color": "var(--e-global-color-primary)",
                        "title_text": "Доведи приятел",
                        "title_color": "var(--e-global-color-text)",
                        "description_text": "50 лв. бонус за Вас и за приятеля Ви"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# BUILD PAGE STRUCTURE
# =============================================================================
page_data = [
    hero_section,
    philosophy_section,
    programs_section,
    cta_section,
    pricing_section,
    discounts_section
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
    print("SUCCESS: Programs page built successfully!")
    print(f"Edit URL: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
    print(f"View URL: {base_url}/?page_id={page_id}")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
