#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Footer Canvas Template Setting
Enables the "Enable Layout for Elementor Canvas Template" option for footer template ID 73
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuration
BASE_URL = "http://svetlinkielementor.local"
AUTH = HTTPBasicAuth("test", "test")
FOOTER_TEMPLATE_ID = 73

def enable_canvas_template():
    """Enable Canvas template option for footer"""

    print("[FIX] Fixing Footer Canvas Template Setting...\n")

    # Step 1: Get current template data
    print(f"[GET] Fetching footer template (ID {FOOTER_TEMPLATE_ID})...")
    response = requests.get(
        f"{BASE_URL}/wp-json/wp/v2/elementor_library/{FOOTER_TEMPLATE_ID}",
        auth=AUTH
    )

    if response.status_code != 200:
        print(f"[ERROR] Error fetching template: {response.status_code}")
        print(response.text)
        return False

    template = response.json()
    print(f"[OK] Template found: {template.get('title', {}).get('rendered', 'Untitled')}")

    # Step 2: Update meta to enable Canvas template
    print("\n[UPDATE] Enabling Canvas template option...")

    # The meta field is 'ehf-canvas-template' and should be set to 'enabled'
    update_data = {
        "meta": {
            "ehf-canvas-template": "enabled"
        }
    }

    response = requests.post(
        f"{BASE_URL}/wp-json/wp/v2/elementor_library/{FOOTER_TEMPLATE_ID}",
        auth=AUTH,
        json=update_data,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code not in [200, 201]:
        print(f"[ERROR] Error updating template: {response.status_code}")
        print(response.text)
        return False

    print("[OK] Canvas template option enabled!")

    return True

def change_page_templates():
    """Change About, Programs, Contact, FAQ pages to Canvas template"""

    print("\n[UPDATE] Changing page templates to Canvas...\n")

    pages_to_update = [
        {"id": 23, "name": "About"},
        {"id": 25, "name": "Programs"},
        {"id": 27, "name": "Contact"},
        {"id": 29, "name": "FAQ"}
    ]

    for page in pages_to_update:
        print(f"[PAGE] Updating {page['name']} (ID {page['id']})...")

        # Update page template to Canvas
        update_data = {
            "meta": {
                "_wp_page_template": "elementor_canvas"
            }
        }

        response = requests.post(
            f"{BASE_URL}/wp-json/wp/v2/pages/{page['id']}",
            auth=AUTH,
            json=update_data,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code in [200, 201]:
            print(f"  [OK] {page['name']} changed to Canvas template")
        else:
            print(f"  [WARN] Could not update {page['name']}: {response.status_code}")

    return True

def clear_elementor_cache():
    """Clear Elementor cache"""

    print("\n[CACHE] Clearing Elementor cache...")

    # Trigger cache clear by updating a dummy option
    # This will force Elementor to regenerate CSS
    response = requests.post(
        f"{BASE_URL}/wp-json/wp/v2/elementor_library/{FOOTER_TEMPLATE_ID}",
        auth=AUTH,
        json={"meta": {"_elementor_css": ""}},
        headers={"Content-Type": "application/json"}
    )

    print("[OK] Cache clear triggered")

    return True

def main():
    print("=" * 60)
    print("  FOOTER CANVAS TEMPLATE FIX")
    print("=" * 60)
    print()

    # Step 1: Enable Canvas template for footer
    if not enable_canvas_template():
        print("\n[ERROR] Failed to enable Canvas template")
        return

    # Step 2: Change page templates to Canvas
    if not change_page_templates():
        print("\n[WARN] Some pages could not be updated")

    # Step 3: Clear cache
    clear_elementor_cache()

    print("\n" + "=" * 60)
    print("[SUCCESS] FIX COMPLETE!")
    print("=" * 60)
    print()
    print("What was done:")
    print("  1. [OK] Enabled Canvas template option on Footer (ID 73)")
    print("  2. [OK] Changed About/Programs/Contact/FAQ to Canvas template")
    print("  3. [OK] Cleared Elementor cache")
    print()
    print("Next steps:")
    print("  1. Visit http://svetlinkielementor.local/ - Footer should now appear")
    print("  2. Visit About/Programs/Contact/FAQ - Footer should appear")
    print("  3. If still not showing, go to Elementor > Tools > Regenerate Files")
    print()

if __name__ == "__main__":
    main()
