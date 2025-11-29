#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Container 1 (Hero Section) for Svetlinki Elementor Home Page
Uses WordPress REST API to create Flexbox Container with FREE Elementor widgets
"""

import requests
import json
import uuid
import sys
import io

# Force UTF-8 encoding for console output
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# WordPress Configuration
WORDPRESS_URL = "http://svetlinkielementor.local"
USERNAME = "test"
APP_PASSWORD = "S27q 64rq oFhf TPDA 30nB hNM5"
PAGE_ID = 21

def generate_element_id():
    """Generate unique Elementor element ID"""
    return str(uuid.uuid4()).replace('-', '')[:7]

def create_hero_container():
    """Create Hero Section using Flexbox Container with FREE widgets only"""

    # Main Hero Container (Flexbox)
    hero_container = {
        "id": generate_element_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "gap": {
                "unit": "px",
                "size": 30,
                "sizes": []
            },
            "padding": {
                "unit": "px",
                "top": "80",
                "right": "20",
                "bottom": "80",
                "left": "20",
                "isLinked": False
            },
            "background_background": "classic",
            "background_color": "var(--e-global-color-accent)"
        },
        "elements": []
    }

    # Widget 1: Heading (H1)
    heading_widget = {
        "id": generate_element_id(),
        "elType": "widget",
        "widgetType": "heading",
        "settings": {
            "title": "Развийте Математическите Умения на Вашето Дете",
            "header_size": "h1",
            "align": "center",
            "title_color": "var(--e-global-color-secondary)",
            "typography_typography": "custom",
            "typography_font_family": "var(--e-global-typography-primary-font-family)",
            "typography_font_size": {
                "unit": "px",
                "size": 48,
                "sizes": []
            },
            "typography_font_weight": "700",
            "typography_line_height": {
                "unit": "em",
                "size": 1.2,
                "sizes": []
            }
        }
    }

    # Widget 2: Text Editor
    text_widget = {
        "id": generate_element_id(),
        "elType": "widget",
        "widgetType": "text-editor",
        "settings": {
            "editor": "Професионални обучения по математика за деца от 4 до 16 години",
            "align": "center",
            "text_color": "var(--e-global-color-text)",
            "typography_typography": "custom",
            "typography_font_size": {
                "unit": "px",
                "size": 20,
                "sizes": []
            },
            "typography_line_height": {
                "unit": "em",
                "size": 1.6,
                "sizes": []
            }
        }
    }

    # Nested Container for Counters (Flexbox row)
    counters_container = {
        "id": generate_element_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "flex_direction": "row",
            "flex_justify_content": "center",
            "flex_align_items": "center",
            "gap": {
                "unit": "px",
                "size": 40,
                "sizes": []
            },
            "flex_wrap": "wrap"
        },
        "elements": []
    }

    # Widget 3: Counter #1 (500+ ученици)
    counter_1_widget = {
        "id": generate_element_id(),
        "elType": "widget",
        "widgetType": "counter",
        "settings": {
            "starting_number": 0,
            "ending_number": 500,
            "suffix": "+",
            "duration": 2000,
            "title": "ученици",
            "number_color": "var(--e-global-color-primary)",
            "title_color": "var(--e-global-color-text)",
            "typography_number_typography": "custom",
            "typography_number_font_size": {
                "unit": "px",
                "size": 48,
                "sizes": []
            },
            "typography_number_font_weight": "700",
            "typography_title_typography": "custom",
            "typography_title_font_size": {
                "unit": "px",
                "size": 16,
                "sizes": []
            }
        }
    }

    # Widget 4: Counter #2 (8+ Години)
    counter_2_widget = {
        "id": generate_element_id(),
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
            "typography_number_typography": "custom",
            "typography_number_font_size": {
                "unit": "px",
                "size": 48,
                "sizes": []
            },
            "typography_number_font_weight": "700",
            "typography_title_typography": "custom",
            "typography_title_font_size": {
                "unit": "px",
                "size": 16,
                "sizes": []
            }
        }
    }

    # Add counters to nested container
    counters_container["elements"].append(counter_1_widget)
    counters_container["elements"].append(counter_2_widget)

    # Widget 5: Button (CTA)
    button_widget = {
        "id": generate_element_id(),
        "elType": "widget",
        "widgetType": "button",
        "settings": {
            "text": "ЗАПАЗИ СЕ СЕГА",
            "link": {
                "url": "#contact",
                "is_external": "",
                "nofollow": "",
                "custom_attributes": ""
            },
            "align": "center",
            "button_type": "primary",
            "button_text_color": "var(--e-global-color-text)",
            "background_color": "var(--e-global-color-primary)",
            "typography_typography": "custom",
            "typography_font_size": {
                "unit": "px",
                "size": 18,
                "sizes": []
            },
            "typography_font_weight": "600",
            "button_padding": {
                "unit": "px",
                "top": "15",
                "right": "40",
                "bottom": "15",
                "left": "40",
                "isLinked": False
            },
            "border_radius": {
                "unit": "px",
                "top": "5",
                "right": "5",
                "bottom": "5",
                "left": "5",
                "isLinked": True
            }
        }
    }

    # Assemble the hero container with all widgets
    hero_container["elements"].append(heading_widget)
    hero_container["elements"].append(text_widget)
    hero_container["elements"].append(counters_container)
    hero_container["elements"].append(button_widget)

    return [hero_container]

def get_current_page_data():
    """Get current Elementor data for the page"""
    url = f"{WORDPRESS_URL}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit"

    response = requests.get(
        url,
        auth=(USERNAME, APP_PASSWORD.replace(' ', ''))
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error getting page data: {response.status_code}")
        print(response.text)
        return None

def update_page_with_hero_container():
    """Update page with new Hero Container"""

    # Get current page data first
    print("1. Fetching current page data...")
    current_data = get_current_page_data()

    if not current_data:
        return False

    print(f"   Page Title: {current_data.get('title', {}).get('rendered', 'N/A')}")

    # Check current Elementor data
    current_elementor = current_data.get('meta', {}).get('_elementor_data', '[]')
    if current_elementor:
        try:
            current_structure = json.loads(current_elementor) if isinstance(current_elementor, str) else current_elementor
            print(f"   Current structure: {len(current_structure)} top-level elements")
        except:
            print("   Current structure: Empty or invalid")

    # Create new Hero Container
    print("\n2. Creating Hero Container structure...")
    hero_data = create_hero_container()
    print(f"   Created container with {len(hero_data[0]['elements'])} direct children")
    print(f"   - Heading widget: H1")
    print(f"   - Text Editor widget")
    print(f"   - Nested container with 2 Counter widgets")
    print(f"   - Button widget")

    # Update page with new data
    print("\n3. Updating page via WordPress REST API...")
    url = f"{WORDPRESS_URL}/wp-json/wp/v2/pages/{PAGE_ID}"

    update_data = {
        "meta": {
            "_elementor_data": json.dumps(hero_data),
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "_elementor_version": "3.16.0"
        }
    }

    response = requests.post(
        url,
        auth=(USERNAME, APP_PASSWORD.replace(' ', '')),
        json=update_data,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code in [200, 201]:
        print(f"   ✅ Page updated successfully!")

        # Verify the update
        print("\n4. Verifying structure...")
        verify_data = get_current_page_data()
        if verify_data:
            new_elementor = verify_data.get('meta', {}).get('_elementor_data', '[]')
            try:
                new_structure = json.loads(new_elementor) if isinstance(new_elementor, str) else new_elementor
                print(f"   ✅ Verified: {len(new_structure)} top-level containers")

                if len(new_structure) > 0:
                    hero = new_structure[0]
                    print(f"   Container type: {hero.get('elType')}")
                    print(f"   Container ID: {hero.get('id')}")
                    print(f"   Direct children: {len(hero.get('elements', []))}")

                    # Count widgets
                    widget_count = 0
                    widget_types = []
                    for element in hero.get('elements', []):
                        if element.get('elType') == 'widget':
                            widget_count += 1
                            widget_types.append(element.get('widgetType'))
                        elif element.get('elType') == 'container':
                            # Count nested widgets
                            for nested in element.get('elements', []):
                                if nested.get('elType') == 'widget':
                                    widget_count += 1
                                    widget_types.append(nested.get('widgetType'))

                    print(f"   Total widgets: {widget_count}")
                    print(f"   Widget types: {', '.join(widget_types)}")
            except Exception as e:
                print(f"   Error parsing verification data: {e}")

        return True
    else:
        print(f"   ❌ Error updating page: {response.status_code}")
        print(f"   Response: {response.text}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Building Hero Container for Svetlinki Elementor Home Page")
    print("=" * 60)
    print(f"Target: Page ID {PAGE_ID} at {WORDPRESS_URL}")
    print("")

    success = update_page_with_hero_container()

    print("\n" + "=" * 60)
    if success:
        print("✅ HERO CONTAINER CREATED SUCCESSFULLY")
        print("=" * 60)
        print("\nNext Steps:")
        print("1. Open Elementor editor to view the hero section")
        print("2. All elements are editable in the Elementor UI")
        print("3. Global colors are applied via CSS variables")
        print(f"4. View page: {WORDPRESS_URL}/?page_id={PAGE_ID}")
    else:
        print("❌ FAILED TO CREATE HERO CONTAINER")
        print("=" * 60)
        print("\nPlease check the error messages above")
