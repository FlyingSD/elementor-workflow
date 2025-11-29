#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild ALL 6 Homepage Sections - Complete Recovery
Uses SECTIONS (not Containers) - Elementor FREE compatible
"""

import requests
import json
import random
import sys
import codecs

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
page_id = 21

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

print("="*60)
print("REBUILDING ALL 6 HOMEPAGE SECTIONS")
print("="*60)

# SECTION 1: HERO
hero_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
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
            {"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Развийте <strong>Математическите Умения</strong> на Вашето Дете", "header_size": "h1", "align": "center", "title_color": "var(--e-global-color-secondary)"}},
            {"id": generate_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p>Професионални обучения по математика за деца от 4 до 16 години</p>", "align": "center", "text_color": "var(--e-global-color-text)"}},
            {"id": generate_id(), "elType": "widget", "widgetType": "counter", "settings": {"starting_number": 0, "ending_number": 500, "suffix": "+", "title": "ученици", "number_color": "var(--e-global-color-primary)", "title_color": "var(--e-global-color-text)", "align": "center"}},
            {"id": generate_id(), "elType": "widget", "widgetType": "counter", "settings": {"starting_number": 0, "ending_number": 8, "suffix": "+", "title": "Години опит", "number_color": "var(--e-global-color-primary)", "title_color": "var(--e-global-color-text)", "align": "center"}},
            {"id": generate_id(), "elType": "widget", "widgetType": "button", "settings": {"text": "ЗАПАЗИ СЕ СЕГА", "link": {"url": "#contact"}, "align": "center", "button_text_color": "#FFFFFF", "background_color": "var(--e-global-color-primary)"}}
        ]
    }]
}

# SECTION 2: BENEFITS
benefits_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {"layout": "boxed", "background_background": "classic", "background_color": "#FFFFFF", "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}},
    "elements": [{"id": generate_id(), "elType": "column", "settings": {"_column_size": 100}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Защо да изберете \"Светлинки\"?", "header_size": "h2", "title_color": "var(--e-global-color-secondary)", "align": "center"}}]}]
}
for card in [{"title": "По-добра Концентрация", "desc": "Нашите методи подобряват фокуса и вниманието към детайла.", "icon": "fas fa-brain"}, {"title": "Логическо Мислене", "desc": "Децата се научават да решават проблеми бързо и ефективно.", "icon": "fas fa-lightbulb"}, {"title": "Отлична Памет", "desc": "Визуалните техники стимулират фотографската памет.", "icon": "fas fa-memory"}]:
    benefits_section["elements"].append({"id": generate_id(), "elType": "column", "settings": {"_column_size": 33}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "icon-box", "settings": {"title_text": card["title"], "description_text": card["desc"], "selected_icon": {"value": card["icon"], "library": "fa-solid"}, "icon_color": "var(--e-global-color-primary)", "title_color": "var(--e-global-color-secondary)", "description_color": "var(--e-global-color-text)", "position": "top"}}]})

# SECTION 3: PROGRAMS (5 levels)
programs_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {"layout": "boxed", "background_background": "classic", "background_color": "var(--e-global-color-accent)", "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}},
    "elements": [{"id": generate_id(), "elType": "column", "settings": {"_column_size": 100}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Нашата 5-степенна програма", "header_size": "h2", "title_color": "var(--e-global-color-secondary)", "align": "center"}}, {"id": generate_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "От първите стъпки до състезателно майсторство", "text_color": "var(--e-global-color-text)", "align": "center"}}]}]
}
for level in [("Ниво 1: Начална Група", "5-7 години", "Тук изграждаме любов към числата."), ("Ниво 2: Средна Група", "8-10 години", "Основата е здрава, сега надграждаме."), ("Ниво 3: Напреднала Група", "11+ години", "Тук ученикът започва да се отличава."), ("Ниво 4: Майсторска Група", "Напреднали", "Превръщаме фокуса в лазер."), ("Ниво 5: Състезателна Група", "Шампиони", "Нивото на шампионите.")]:
    programs_section["elements"].append({"id": generate_id(), "elType": "column", "settings": {"_column_size": 20}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f"<h3>{level[0]}</h3><p><strong>{level[1]}</strong></p><p>{level[2]}</p>", "text_color": "var(--e-global-color-text)"}}]})

# SECTION 4: PRICING CTA
pricing_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {"layout": "boxed", "background_background": "classic", "background_color": "#FFFFFF", "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}},
    "elements": [{"id": generate_id(), "elType": "column", "settings": {"_column_size": 100}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Нека поговорим за цените", "header_size": "h2", "title_color": "var(--e-global-color-secondary)"}}, {"id": generate_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "Знаем, че това е важен въпрос. Затова сме напълно прозрачни.", "text_color": "var(--e-global-color-text)"}}, {"id": generate_id(), "elType": "widget", "widgetType": "button", "settings": {"text": "Разгледайте нашите цени", "link": {"url": "/programs"}, "background_color": "var(--e-global-color-secondary)", "button_text_color": "#FFFFFF"}}]}]
}

# SECTION 5: TESTIMONIALS
testimonials_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {"layout": "boxed", "background_background": "classic", "background_color": "var(--e-global-color-accent)", "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}},
    "elements": [{"id": generate_id(), "elType": "column", "settings": {"_column_size": 100}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Какво казват родителите", "header_size": "h2", "title_color": "var(--e-global-color-secondary)", "align": "center"}}]}]
}
for testimonial in [("Анна Василева", "Майка на Виктор", "Синът ми не просто подобри успеха си по математика."), ("Петър Георгиев", "Баща на Мария", "Първо бях скептичен, но резултатите са видими.")]:
    testimonials_section["elements"].append({"id": generate_id(), "elType": "column", "settings": {"_column_size": 50}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "testimonial", "settings": {"testimonial_content": testimonial[2], "testimonial_name": testimonial[0], "testimonial_job": testimonial[1]}}]})

# SECTION 6: CONTACT
contact_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {"layout": "boxed", "background_background": "classic", "background_color": "#FFFFFF", "padding": {"unit": "px", "top": "80", "right": "20", "bottom": "80", "left": "20", "isLinked": False}},
    "elements": [
        {"id": generate_id(), "elType": "column", "settings": {"_column_size": 100}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Свържете се с нас", "header_size": "h2", "title_color": "var(--e-global-color-secondary)", "align": "center"}}]},
        {"id": generate_id(), "elType": "column", "settings": {"_column_size": 50}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<h3>Адрес</h3><p>София, ул. Оборище 1А</p>", "text_color": "var(--e-global-color-text)"}}]},
        {"id": generate_id(), "elType": "column", "settings": {"_column_size": 50}, "elements": [{"id": generate_id(), "elType": "widget", "widgetType": "shortcode", "settings": {"shortcode": "[contact-form-7]"}}]}
    ]
}

# ASSEMBLE ALL 6 SECTIONS
all_sections = [hero_section, benefits_section, programs_section, pricing_section, testimonials_section, contact_section]

print(f"\nTotal sections: {len(all_sections)}")
print("1. Hero (full-width cream)")
print("2. Benefits (3 icon boxes)")
print("3. Programs (5 levels)")
print("4. Pricing CTA")
print("5. Testimonials (2 cards)")
print("6. Contact")

# SAVE
print("\nSaving to database...")
response = requests.post(f"{base_url}/wp-json/wp/v2/pages/{page_id}", auth=auth, json={"meta": {"_elementor_data": json.dumps(all_sections, ensure_ascii=False)}})

if response.status_code == 200:
    print("\n[SUCCESS] All 6 sections saved!")
    print(f"\nView: {base_url}/home-2/")
    print(f"Edit: {base_url}/wp-admin/post.php?post={page_id}&action=elementor")
    print("\nNEXT: Open Elementor editor and click Update!")
else:
    print(f"\n[ERROR] {response.status_code}")
    print(response.text)
