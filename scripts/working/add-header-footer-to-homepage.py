#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Header (ID 85) and Footer (ID 86) to Homepage (ID 21)
Prepends header and appends footer to existing homepage sections
"""

import requests
import json

base_url = "http://svetlinkielementor.local"
auth = ("test", "S27q64rqoFhfTPDA30nBhNM5")
homepage_id = 21
header_id = 85
footer_id = 86

print("Fetching header template...")
header_response = requests.get(
    f"{base_url}/wp-json/wp/v2/elementor_library/{header_id}?context=edit",
    auth=auth
)
header_json = header_response.json()
header_data = json.loads(header_json['meta']['_elementor_data'])
print(f"[OK] Header loaded: {len(header_data)} sections")

print("Fetching footer template...")
footer_response = requests.get(
    f"{base_url}/wp-json/wp/v2/elementor_library/{footer_id}?context=edit",
    auth=auth
)
footer_json = footer_response.json()
footer_data = json.loads(footer_json['meta']['_elementor_data'])
print(f"[OK] Footer loaded: {len(footer_data)} sections")

print("Fetching current homepage...")
homepage_response = requests.get(
    f"{base_url}/wp-json/wp/v2/pages/{homepage_id}?context=edit",
    auth=auth
)
homepage_json = homepage_response.json()
homepage_elementor_data = homepage_json['meta'].get('_elementor_data', '[]')

if homepage_elementor_data:
    current_sections = json.loads(homepage_elementor_data)
else:
    current_sections = []

print(f"[OK] Homepage loaded: {len(current_sections)} existing sections")

# Combine: header + existing sections + footer
new_page_structure = header_data + current_sections + footer_data

print(f"\nNew page structure: {len(new_page_structure)} total sections")
print("  - Header sections: 1")
print(f"  - Body sections: {len(current_sections)}")
print(f"  - Footer sections: {len(footer_data)}")

# Update homepage
print("\nUpdating homepage...")
update_response = requests.post(
    f"{base_url}/wp-json/wp/v2/pages/{homepage_id}",
    auth=auth,
    json={"meta": {"_elementor_data": json.dumps(new_page_structure, ensure_ascii=False)}}
)

if update_response.status_code == 200:
    print("\n[SUCCESS] Header and Footer added to homepage!")
    print(f"\nView homepage: {base_url}/")
    print(f"Edit in Elementor: {base_url}/wp-admin/post.php?post={homepage_id}&action=elementor")
else:
    print(f"\n[ERROR] {update_response.status_code}")
    print(update_response.text[:500])
