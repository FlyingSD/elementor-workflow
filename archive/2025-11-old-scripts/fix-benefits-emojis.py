#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Benefits Section Icons - Replace FontAwesome with Emojis
Page 21, Section 6bf56d6, Widgets: 13318db, 426c398, 137e434
"""

import requests
import json
import sys
from requests.auth import HTTPBasicAuth

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# WordPress credentials
WP_URL = "http://svetlinkielementor.local"
WP_USER = "test"
WP_PASS = "test"
PAGE_ID = 21

def get_page_data():
    """Fetch current page data from WordPress"""
    url = f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}"
    response = requests.get(url, auth=HTTPBasicAuth(WP_USER, WP_PASS))

    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    page_data = response.json()
    elementor_data_str = page_data.get('meta', {}).get('_elementor_data', '[]')

    if isinstance(elementor_data_str, str):
        elementor_data = json.loads(elementor_data_str) if elementor_data_str else []
    else:
        elementor_data = elementor_data_str

    return page_data, elementor_data

def update_page_data(elementor_data):
    """Update page data in WordPress"""
    url = f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}"

    payload = {
        'meta': {
            '_elementor_data': json.dumps(elementor_data, ensure_ascii=False)
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(WP_USER, WP_PASS),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to update page: {response.status_code} - {response.text}")

    return response.json()

def find_and_update_widgets(elementor_data):
    """Find Benefits section and update icon widgets"""
    updated = False

    for section in elementor_data:
        if section.get('id') == '6bf56d6':  # Benefits section
            print("✓ Found Benefits section (6bf56d6)")

            for column in section.get('elements', []):
                for widget in column.get('elements', []):
                    widget_id = widget.get('id')

                    # Card 1: Brain emoji
                    if widget_id == '13318db':
                        print(f"  → Updating widget {widget_id}: fas fa-brain → 🧠")
                        widget['settings']['selected_icon'] = {
                            'value': '🧠',
                            'library': ''
                        }
                        updated = True

                    # Card 2: Lightbulb emoji
                    elif widget_id == '426c398':
                        print(f"  → Updating widget {widget_id}: fas fa-lightbulb → 💡")
                        widget['settings']['selected_icon'] = {
                            'value': '💡',
                            'library': ''
                        }
                        updated = True

                    # Card 3: Star emoji (was missing icon)
                    elif widget_id == '137e434':
                        print(f"  → Adding icon to widget {widget_id}: ⭐")
                        widget['settings']['selected_icon'] = {
                            'value': '⭐',
                            'library': ''
                        }
                        updated = True

    return updated

def main():
    print("=" * 60)
    print("BENEFITS SECTION EMOJI FIX")
    print("=" * 60)
    print()

    print("1. Fetching current page data...")
    page_data, elementor_data = get_page_data()
    print(f"   ✓ Page '{page_data['title']['rendered']}' loaded")
    print(f"   ✓ {len(elementor_data)} sections found")
    print()

    print("2. Updating icon widgets...")
    updated = find_and_update_widgets(elementor_data)

    if not updated:
        print("   ✗ Benefits section or widgets not found!")
        return
    print()

    print("3. Saving updated data to WordPress...")
    result = update_page_data(elementor_data)
    print("   ✓ Page updated successfully!")
    print()

    print("=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print()
    print("CHANGES MADE:")
    print("- Card 1 (13318db): fas fa-brain → 🧠")
    print("- Card 2 (426c398): fas fa-lightbulb → 💡")
    print("- Card 3 (137e434): ADDED ⭐ (was missing)")
    print()
    print("NEXT STEPS:")
    print("1. Open page in Elementor editor")
    print("2. Click 'Update' button (required for REST API changes)")
    print("3. View page to verify emojis display correctly")
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"✗ ERROR: {e}")
        exit(1)
