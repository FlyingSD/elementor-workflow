import requests
import json
import random

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 21

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

# Get current Elementor data
print("Getting current page Elementor data...")
response = requests.get(f"{base_url}/wp-json/wp/v2/pages/{page_id}", auth=auth)
page_data = response.json()

elementor_data_str = page_data.get('meta', {}).get('_elementor_data', '[]')

if isinstance(elementor_data_str, str):
    current_sections = json.loads(elementor_data_str) if elementor_data_str else []
else:
    current_sections = elementor_data_str

print(f"Current sections: {len(current_sections)}")

# Build ALL remaining sections
new_sections = []

# Section 3: Programs (5 levels)
programs_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": [{
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
                    "header_size": "h2",
                    "title_color": "var(--e-global-color-secondary)",
                    "align": "center"
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": "От първите стъпки до състезателно майсторство",
                    "text_color": "var(--e-global-color-text)",
                    "align": "center"
                }
            }
        ]
    }]
}

# Add 5 program level cards
programs = [
    ("Ниво 1: Начална Група", "5-7 години", "Тук изграждаме любов към числата."),
    ("Ниво 2: Средна Група", "8-10 години", "Основата е здрава, сега надграждаме."),
    ("Ниво 3: Напреднала Група", "11+ години", "Тук ученикът започва да се отличава."),
    ("Ниво 4: Майсторска Група", "Напреднали", "Превръщаме фокуса в лазер."),
    ("Ниво 5: Състезателна Група", "Шампиони", "Нивото на шампионите.")
]

for title, age, desc in programs:
    programs_section["elements"].append({
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 20},
        "elements": [{
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": f"<h3>{title}</h3><p><strong>{age}</strong></p><p>{desc}</p>",
                "text_color": "var(--e-global-color-text)"
            }
        }]
    })

new_sections.append(programs_section)

# Section 4: Pricing CTA
pricing_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": [{
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 100},
        "elements": [
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": "Нека поговорим за цените",
                    "header_size": "h2",
                    "title_color": "var(--e-global-color-secondary)"
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": "Знаем, че това е важен въпрос. Затова сме напълно прозрачни.",
                    "text_color": "var(--e-global-color-text)"
                }
            },
            {
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "button",
                "settings": {
                    "text": "Разгледайте нашите цени",
                    "link": {"url": "/programs"},
                    "background_color": "var(--e-global-color-secondary)",
                    "button_text_color": "#FFFFFF"
                }
            }
        ]
    }]
}

new_sections.append(pricing_section)

# Section 5: Testimonials
testimonials_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-accent)",
        "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}
    },
    "elements": [{
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 100},
        "elements": [{
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Какво казват родителите",
                "header_size": "h2",
                "title_color": "var(--e-global-color-secondary)",
                "align": "center"
            }
        }]
    }]
}

# Add 2 testimonials
testimonials = [
    ("Анна Василева", "Майка на Виктор", "Синът ми не просто подобри успеха си по математика."),
    ("Петър Георгиев", "Баща на Мария", "Първо бях скептичен, но резултатите са видими.")
]

for name, role, quote in testimonials:
    testimonials_section["elements"].append({
        "id": generate_id(),
        "elType": "column",
        "settings": {"_column_size": 50},
        "elements": [{
            "id": generate_id(),
            "elType": "widget",
            "widgetType": "testimonial",
            "settings": {
                "testimonial_content": quote,
                "testimonial_name": name,
                "testimonial_job": role
            }
        }]
    })

new_sections.append(testimonials_section)

# Section 6: Contact
contact_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
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
            "elements": [{
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": "Свържете се с нас",
                    "header_size": "h2",
                    "title_color": "var(--e-global-color-secondary)",
                    "align": "center"
                }
            }]
        },
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 50},
            "elements": [{
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": "<h3>Адрес</h3><p>София, ул. Оборище 1А</p>",
                    "text_color": "var(--e-global-color-text)"
                }
            }]
        },
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {"_column_size": 50},
            "elements": [{
                "id": generate_id(),
                "elType": "widget",
                "widgetType": "shortcode",
                "settings": {
                    "shortcode": "[contact-form-7]"
                }
            }]
        }
    ]
}

new_sections.append(contact_section)

# Append all new sections
current_sections.extend(new_sections)

print(f"\nTotal sections after addition: {len(current_sections)}")
print(f"Added {len(new_sections)} new sections")

# Update page
update_response = requests.post(
    f"{base_url}/wp-json/wp/v2/pages/{page_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps(current_sections, ensure_ascii=False)}}
)

if update_response.status_code == 200:
    print("\n[SUCCESS] All sections added!")
    print(f"\nView: {base_url}/home-2/")
    print(f"Edit: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
else:
    print(f"\n[ERROR] Update failed: {update_response.status_code}")
