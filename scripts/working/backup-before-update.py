#!/usr/bin/env python3
"""
Pre-Flight Snapshot - Backup page before update

MANDATORY SAFETY PROTOCOL:
Before EVERY update to a WordPress page via MCP or REST API,
this script creates a timestamped backup of the current state.

Usage:
    python backup-before-update.py --page-id 21 --task "hero-fix"
    python backup-before-update.py --page-id 23 --task "about-update"

Result:
    backups/page_{page_id}_before_{task}_{timestamp}.json

Exit codes:
    0 - Success (backup created)
    1 - Failure (see error message)
"""

import json
import os
import sys
import argparse
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

# Load config
CONFIG_FILE = "config.json"

def load_config():
    """Load WordPress credentials from config.json"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"❌ ERROR: {CONFIG_FILE} not found!")
        print(f"   Expected location: {os.path.abspath(CONFIG_FILE)}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON in {CONFIG_FILE}")
        print(f"   {e}")
        sys.exit(1)

def get_page_data(page_id, config):
    """
    Fetch current page data from WordPress REST API

    Returns: JSON string (as stored in _elementor_data meta field)
    """
    base_url = config['wordpress']['base_url']
    username = config['wordpress']['auth']['user']
    password = config['wordpress']['auth']['password']

    # WordPress REST API endpoint for page meta
    url = f"{base_url}/wp-json/wp/v2/pages/{page_id}"

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password),
            timeout=10
        )
        response.raise_for_status()

        page = response.json()

        # Get _elementor_data from meta
        if 'meta' in page and '_elementor_data' in page['meta']:
            elementor_data = page['meta']['_elementor_data']

            # Parse if string (WordPress stores as slash-escaped JSON string)
            if isinstance(elementor_data, str):
                try:
                    elementor_data = json.loads(elementor_data)
                except json.JSONDecodeError:
                    # Already a string, return as-is
                    pass

            return elementor_data
        else:
            print(f"⚠️  WARNING: Page {page_id} has no _elementor_data meta field")
            print(f"   This might be a non-Elementor page")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Failed to fetch page {page_id}")
        print(f"   {e}")
        return None

def validate_page_data(data):
    """
    Validate that page data is not empty and has valid structure

    Returns: (is_valid, error_message)
    """
    if not data:
        return False, "Page data is empty or None"

    if isinstance(data, str):
        if len(data) == 0:
            return False, "Page data is empty string"
        # Try to parse if string
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return False, "Page data is not valid JSON"

    if isinstance(data, list):
        if len(data) == 0:
            return False, "Page data is empty array (no sections)"

        # Check first element has elType
        if 'elType' not in data[0]:
            return False, "First element missing 'elType' field"

    return True, ""

def save_backup(page_id, task, data):
    """
    Save backup to backups/ directory with timestamp

    Returns: (success, backup_path)
    """
    # Ensure backups directory exists
    os.makedirs('backups', exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Generate filename
    filename = f"page_{page_id}_before_{task}_{timestamp}.json"
    filepath = os.path.join('backups', filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True, filepath
    except Exception as e:
        print(f"❌ ERROR: Failed to write backup file")
        print(f"   {e}")
        return False, None

def main():
    parser = argparse.ArgumentParser(
        description='Pre-Flight Snapshot - Backup page before update'
    )
    parser.add_argument(
        '--page-id',
        type=int,
        required=True,
        help='WordPress page ID (e.g., 21 for homepage)'
    )
    parser.add_argument(
        '--task',
        type=str,
        required=True,
        help='Task description (e.g., "hero-fix", "about-update")'
    )

    args = parser.parse_args()

    print("=" * 80)
    print("🚨 PRE-FLIGHT SNAPSHOT - MANDATORY SAFETY BACKUP")
    print("=" * 80)
    print(f"Page ID: {args.page_id}")
    print(f"Task: {args.task}")
    print()

    # Load config
    print("📋 Loading configuration...")
    config = load_config()
    print(f"✅ Config loaded: {config['wordpress']['base_url']}")
    print()

    # Fetch current page data
    print(f"📡 Fetching current state of page {args.page_id}...")
    data = get_page_data(args.page_id, config)

    if data is None:
        print("❌ FAILED: Could not fetch page data")
        sys.exit(1)

    print(f"✅ Page data fetched successfully")
    print()

    # Validate data
    print("🔍 Validating page data...")
    is_valid, error_msg = validate_page_data(data)

    if not is_valid:
        print(f"❌ VALIDATION FAILED: {error_msg}")
        print(f"⚠️  Backup will still be created, but data may be corrupted")
    else:
        print(f"✅ Validation passed")

    # Count sections/widgets for info
    if isinstance(data, list):
        num_sections = len(data)
        num_widgets = sum(
            len(section.get('elements', [{}])[0].get('elements', []))
            for section in data
            if section.get('elType') == 'section'
        )
        print(f"   Sections: {num_sections}, Widgets: ~{num_widgets}")
    print()

    # Save backup
    print("💾 Saving backup...")
    success, backup_path = save_backup(args.page_id, args.task, data)

    if not success:
        print("❌ FAILED: Could not save backup")
        sys.exit(1)

    print(f"✅ Backup saved successfully!")
    print()
    print("=" * 80)
    print(f"📁 BACKUP LOCATION:")
    print(f"   {os.path.abspath(backup_path)}")
    print("=" * 80)
    print()
    print("✅ PRE-FLIGHT SNAPSHOT COMPLETE")
    print("   You can now safely proceed with your update.")
    print()
    print("⚠️  TO ROLLBACK (if update fails):")
    print(f"   python restore-from-backup.py --backup \"{backup_path}\"")
    print()

    sys.exit(0)

if __name__ == '__main__':
    main()
