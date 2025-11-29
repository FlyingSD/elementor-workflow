#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export Hero Container structure to JSON file
"""

import requests
import json
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

def export_structure():
    """Export page structure to JSON"""
    url = f"{WORDPRESS_URL}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit"

    response = requests.get(
        url,
        auth=(USERNAME, APP_PASSWORD.replace(' ', ''))
    )

    if response.status_code == 200:
        data = response.json()
        elementor_data = data.get('meta', {}).get('_elementor_data', '[]')

        if elementor_data:
            structure = json.loads(elementor_data) if isinstance(elementor_data, str) else elementor_data

            # Save to file
            output_file = "hero_container_structure.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(structure, f, indent=2, ensure_ascii=False)

            print(f"✅ Structure exported to: {output_file}")
            print(f"\nFile size: {len(json.dumps(structure, indent=2))} bytes")
            print(f"Containers: {len(structure)}")

            # Count widgets
            total_widgets = 0
            for container in structure:
                for element in container.get('elements', []):
                    if element.get('elType') == 'widget':
                        total_widgets += 1
                    elif element.get('elType') == 'container':
                        for nested in element.get('elements', []):
                            if nested.get('elType') == 'widget':
                                total_widgets += 1

            print(f"Widgets: {total_widgets}")

        else:
            print("No Elementor data found!")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    export_structure()
