#!/usr/bin/env python3
"""
Restore page from Pre-Flight Snapshot backup

EMERGENCY ROLLBACK PROCEDURE:
If page update goes wrong, use this script to restore from backup.

Usage:
    python restore-from-backup.py --backup "backups/page_21_before_hero-fix_20251129_143052.json"
    python restore-from-backup.py --page-id 21 --latest  # Restore from latest backup

Exit codes:
    0 - Success (page restored)
    1 - Failure (see error message)
"""

import json
import os
import sys
import argparse
import glob
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
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON in {CONFIG_FILE}")
        print(f"   {e}")
        sys.exit(1)

def load_backup(backup_path):
    """Load backup JSON from file"""
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"❌ ERROR: Backup file not found: {backup_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON in backup file")
        print(f"   {e}")
        return None

def find_latest_backup(page_id):
    """Find latest backup for given page_id"""
    pattern = f"backups/page_{page_id}_before_*.json"
    backups = glob.glob(pattern)

    if not backups:
        print(f"❌ ERROR: No backups found for page {page_id}")
        print(f"   Search pattern: {pattern}")
        return None

    # Sort by modification time (latest first)
    backups.sort(key=os.path.getmtime, reverse=True)
    return backups[0]

def restore_page_data(page_id, data, config):
    """
    Restore page data to WordPress via REST API

    Returns: (success, message)
    """
    base_url = config['wordpress']['base_url']
    username = config['wordpress']['auth']['user']
    password = config['wordpress']['auth']['password']

    # WordPress REST API endpoint
    url = f"{base_url}/wp-json/wp/v2/pages/{page_id}"

    # Prepare data (slash-escape JSON for WordPress)
    if isinstance(data, (list, dict)):
        elementor_data = json.dumps(data)
    else:
        elementor_data = data

    # WordPress expects slash-escaped JSON
    elementor_data_escaped = elementor_data.replace('\\', '\\\\').replace('"', '\\"')

    payload = {
        'meta': {
            '_elementor_data': elementor_data_escaped
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            auth=HTTPBasicAuth(username, password),
            timeout=30
        )
        response.raise_for_status()

        return True, "Page restored successfully via REST API"

    except requests.exceptions.RequestException as e:
        return False, f"REST API request failed: {e}"

def verify_restoration(page_id, config):
    """Verify that page was restored by fetching it again"""
    base_url = config['wordpress']['base_url']
    username = config['wordpress']['auth']['user']
    password = config['wordpress']['auth']['password']

    url = f"{base_url}/wp-json/wp/v2/pages/{page_id}"

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password),
            timeout=10
        )
        response.raise_for_status()

        page = response.json()

        if 'meta' in page and '_elementor_data' in page['meta']:
            return True, "Verification successful"
        else:
            return False, "Page has no _elementor_data after restore"

    except requests.exceptions.RequestException as e:
        return False, f"Verification failed: {e}"

def main():
    parser = argparse.ArgumentParser(
        description='Restore page from Pre-Flight Snapshot backup'
    )
    parser.add_argument(
        '--backup',
        type=str,
        help='Path to backup file (e.g., backups/page_21_before_hero-fix_20251129_143052.json)'
    )
    parser.add_argument(
        '--page-id',
        type=int,
        help='WordPress page ID (used with --latest to find latest backup)'
    )
    parser.add_argument(
        '--latest',
        action='store_true',
        help='Restore from latest backup (requires --page-id)'
    )

    args = parser.parse_args()

    # Validation
    if not args.backup and not (args.page_id and args.latest):
        print("❌ ERROR: Must specify either --backup or (--page-id + --latest)")
        parser.print_help()
        sys.exit(1)

    print("=" * 80)
    print("🚨 EMERGENCY ROLLBACK - RESTORE FROM BACKUP")
    print("=" * 80)
    print()

    # Determine backup file
    if args.latest:
        print(f"🔍 Finding latest backup for page {args.page_id}...")
        backup_path = find_latest_backup(args.page_id)
        if not backup_path:
            sys.exit(1)
        print(f"✅ Found: {backup_path}")
        page_id = args.page_id
    else:
        backup_path = args.backup
        # Extract page_id from filename
        try:
            filename = os.path.basename(backup_path)
            page_id = int(filename.split('_')[1])
        except (IndexError, ValueError):
            print(f"❌ ERROR: Could not extract page_id from filename: {backup_path}")
            print(f"   Expected format: page_{{id}}_before_{{task}}_{{timestamp}}.json")
            sys.exit(1)

    print()
    print(f"📁 Backup file: {backup_path}")
    print(f"📄 Page ID: {page_id}")
    print()

    # Load config
    print("📋 Loading configuration...")
    config = load_config()
    print(f"✅ Config loaded: {config['wordpress']['base_url']}")
    print()

    # Load backup
    print("📂 Loading backup data...")
    data = load_backup(backup_path)
    if data is None:
        sys.exit(1)
    print(f"✅ Backup loaded successfully")

    # Show backup info
    if isinstance(data, list):
        num_sections = len(data)
        print(f"   Sections: {num_sections}")
    print()

    # Confirm with user
    print("⚠️  WARNING: This will OVERWRITE current page content!")
    print(f"   Page {page_id} will be restored to state from backup.")
    print()
    confirm = input("Type 'yes' to proceed with rollback: ")

    if confirm.lower() != 'yes':
        print("❌ CANCELLED: Rollback aborted by user")
        sys.exit(1)

    print()
    print("🔄 Restoring page data...")

    # Restore
    success, message = restore_page_data(page_id, data, config)

    if not success:
        print(f"❌ RESTORE FAILED: {message}")
        sys.exit(1)

    print(f"✅ {message}")
    print()

    # Verify
    print("🔍 Verifying restoration...")
    success, message = verify_restoration(page_id, config)

    if not success:
        print(f"⚠️  VERIFICATION WARNING: {message}")
        print(f"   Page may not have been restored correctly")
    else:
        print(f"✅ {message}")

    print()
    print("=" * 80)
    print("✅ ROLLBACK COMPLETE")
    print("=" * 80)
    print()
    print("⚠️  IMPORTANT: Open page in Elementor editor and click 'Update'")
    print(f"   URL: {config['wordpress']['base_url']}/wp-admin/post.php?post={page_id}&action=elementor")
    print()
    print("   This triggers Elementor's internal hooks and ensures changes appear on frontend.")
    print()

    sys.exit(0)

if __name__ == '__main__':
    main()
