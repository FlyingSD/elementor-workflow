#!/usr/bin/env python3
"""Update homepage with v4 split sections structure."""

import json
import requests
from requests.auth import HTTPBasicAuth

# Configuration
SITE_URL = "http://svetlinkielementor.local"
USERNAME = "admin"
APP_PASSWORD = "MQmG 0uuZ ijPi 0w40 uZPo z6dy"
PAGE_ID = 21

# Read the JSON file
with open("homepage-v4-split-sections.json", "r", encoding="utf-8") as f:
    elementor_data = json.load(f)

# Prepare the request
url = f"{SITE_URL}/wp-json/wp/v2/pages/{PAGE_ID}"
headers = {
    "Content-Type": "application/json",
}
auth = HTTPBasicAuth(USERNAME, APP_PASSWORD)

# Update the page with Elementor data
data = {
    "meta": {
        "_elementor_data": json.dumps(elementor_data)
    }
}

print(f"Updating page {PAGE_ID} with {len(elementor_data)} sections...")
response = requests.post(url, headers=headers, auth=auth, json=data)

if response.status_code == 200:
    print("SUCCESS: Page updated successfully!")
    print(f"Sections: {len(elementor_data)}")
    print("\nNext steps:")
    print("1. Visit: http://svetlinkielementor.local/regenerate-css-web.php")
    print("2. Hard refresh browser (Ctrl+Shift+R)")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
