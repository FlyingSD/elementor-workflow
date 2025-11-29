#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Header and Footer via Direct Database Update
Uses WordPress database directly since REST API doesn't support elementor-hf post type
"""

import mysql.connector
import json
import random
import sys
import codecs

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Database connection details (Local by Flywheel defaults)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'local'
}

header_id = 69
footer_id = 73

def generate_id():
    return ''.join(random.choices('0123456789abcdef', k=7))

print("="*60)
print("UPDATING HEADER AND FOOTER VIA DATABASE")
print("="*60)

# =============================================================================
# BUILD HEADER CONTENT
# =============================================================================
header_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {
            "unit": "px",
            "top": "20",
            "right": "20",
            "bottom": "20",
            "left": "20",
            "isLinked": False
        },
        "border_border": "solid",
        "border_width": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "2",
            "left": "0",
            "isLinked": False
        },
        "border_color": "var(--e-global-color-accent)"
    },
    "elements": [
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h3",
                        "title_color": "var(--e-global-color-secondary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "28", "sizes": []},
                        "typography_font_weight": "700"
                    }
                }
            ]
        },
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "ЗАПАЗИ СЕ СЕГА",
                        "link": {"url": "#contact"},
                        "align": "right",
                        "button_text_color": "#FFFFFF",
                        "background_color": "var(--e-global-color-primary)",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "16", "sizes": []},
                        "typography_font_weight": "600"
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# BUILD FOOTER CONTENT
# =============================================================================
footer_section = {
    "id": generate_id(),
    "elType": "section",
    "settings": {
        "stretch_section": "section-stretched",
        "layout": "boxed",
        "background_background": "classic",
        "background_color": "var(--e-global-color-secondary)",
        "padding": {
            "unit": "px",
            "top": "40",
            "right": "20",
            "bottom": "40",
            "left": "20",
            "isLinked": False
        }
    },
    "elements": [
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Светлинки",
                        "header_size": "h4",
                        "title_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "20", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>Ментална аритметика за деца</p><p>&copy; 2025 Светлинки. Всички права запазени.</p>",
                        "text_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                }
            ]
        },
        {
            "id": generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 50,
                "content_position": "center"
            },
            "elements": [
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Контакт",
                        "header_size": "h4",
                        "title_color": "#FFFFFF",
                        "align": "right",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "18", "sizes": []},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p>София, ул. Оборище 1А</p><p>Тел: +359 XXX XXX XXX</p>",
                        "text_color": "#FFFFFF",
                        "align": "right",
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": "14", "sizes": []},
                        "typography_line_height": {"unit": "em", "size": "1.6", "sizes": []}
                    }
                }
            ]
        }
    ]
}

# =============================================================================
# UPDATE DATABASE
# =============================================================================
try:
    print("\nConnecting to database...")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Update header
    print(f"\n[1/2] Updating header template (ID: {header_id})...")
    header_json = json.dumps([header_section], ensure_ascii=False)

    cursor.execute("""
        UPDATE wp_postmeta
        SET meta_value = %s
        WHERE post_id = %s AND meta_key = '_elementor_data'
    """, (header_json, header_id))

    if cursor.rowcount > 0:
        print("✓ Header updated in database")
    else:
        # Try to insert if not exists
        cursor.execute("""
            INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
            VALUES (%s, '_elementor_data', %s)
        """, (header_id, header_json))
        print("✓ Header inserted into database")

    # Update footer
    print(f"\n[2/2] Updating footer template (ID: {footer_id})...")
    footer_json = json.dumps([footer_section], ensure_ascii=False)

    cursor.execute("""
        UPDATE wp_postmeta
        SET meta_value = %s
        WHERE post_id = %s AND meta_key = '_elementor_data'
    """, (footer_json, footer_id))

    if cursor.rowcount > 0:
        print("✓ Footer updated in database")
    else:
        cursor.execute("""
            INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
            VALUES (%s, '_elementor_data', %s)
        """, (footer_id, footer_json))
        print("✓ Footer inserted into database")

    conn.commit()

    print("\n" + "="*60)
    print("SUCCESS! Header and footer updated in database.")
    print("="*60)
    print("\n⚠️  IMPORTANT NEXT STEPS:")
    print("1. Open each template in Elementor editor")
    print("2. Click 'Update' button to trigger processing hooks")
    print("3. Clear Elementor cache")
    print("\nHeader edit: http://svetlinkielementor.local/wp-admin/post.php?post=69&action=elementor")
    print("Footer edit: http://svetlinkielementor.local/wp-admin/post.php?post=73&action=elementor")

except mysql.connector.Error as err:
    print(f"\n✗ Database error: {err}")
    sys.exit(1)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")

print("="*60)
