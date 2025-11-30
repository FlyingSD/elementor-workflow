import json
import requests

# Read backup
with open('backups/page_21_before_hero-redesign_20251130_094711.json', 'r', encoding='utf-8') as f:
    backup = json.load(f)

# Restore via REST API
response = requests.post(
    'http://svetlinkielementor.local/wp-json/wp/v2/pages/21',
    json={'meta': {'_elementor_data': backup['meta']['_elementor_data']}},
    auth=('test', 'test')
)

if response.status_code in [200, 201]:
    print("HOMEPAGE RESTORED SUCCESSFULLY!")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)
