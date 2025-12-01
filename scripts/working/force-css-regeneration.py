#!/usr/bin/env python3
"""
Force Elementor CSS Regeneration - Python Wrapper

This script calls the PHP solution to force CSS regeneration
after REST API or programmatic updates.

Usage:
    python force-css-regeneration.py 21
    python force-css-regeneration.py 21 23 25 27 29

Research: Elementor GitHub Issues #4464, #7237, #27300, #31594
"""

import subprocess
import sys
import os
import requests
from pathlib import Path

# Configuration
SITE_ROOT = Path(__file__).parent / "app" / "public"
PHP_SCRIPT = SITE_ROOT / "force-css-regeneration.php"
SITE_URL = "http://svetlinkielementor.local"

# Local by Flywheel PHP path (adjust if needed)
PHP_PATHS = [
    "php",  # Try system PHP first
    r"C:\Program Files\PHP\php.exe",
    r"C:\xampp\php\php.exe",
    # Local by Flywheel uses Docker, so we'll use wp-cli which has PHP
]

def find_php():
    """Find PHP executable"""
    for php_path in PHP_PATHS:
        try:
            result = subprocess.run(
                [php_path, "-v"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return php_path
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue

    return None

def regenerate_css_via_php(post_ids):
    """Call PHP script to regenerate CSS"""
    php_exe = find_php()

    if not php_exe:
        print("ERROR: PHP executable not found!")
        print("\nTrying alternative method via HTTP request...")
        return regenerate_css_via_http(post_ids)

    print(f"Using PHP: {php_exe}\n")

    cmd = [php_exe, str(PHP_SCRIPT)] + [str(pid) for pid in post_ids]

    result = subprocess.run(
        cmd,
        cwd=str(SITE_ROOT),
        capture_output=True,
        text=True,
        timeout=60
    )

    print(result.stdout)

    if result.stderr:
        print("STDERR:", result.stderr)

    return result.returncode == 0

def regenerate_css_via_http(post_ids):
    """Alternative: Visit pages to trigger CSS regeneration"""
    print("\n" + "="*50)
    print("Alternative Method: HTTP Page Visits")
    print("="*50 + "\n")

    print("This method visits each page to trigger CSS regeneration.\n")

    success_count = 0

    for post_id in post_ids:
        print(f"Processing post {post_id}...")

        try:
            # Get the page URL
            # You'll need to adjust this based on your page slugs
            page_urls = {
                21: f"{SITE_URL}/home/",
                23: f"{SITE_URL}/about/",
                25: f"{SITE_URL}/programs/",
                27: f"{SITE_URL}/contact/",
                29: f"{SITE_URL}/faq/",
            }

            page_url = page_urls.get(post_id, f"{SITE_URL}/?p={post_id}")

            print(f"  - Visiting: {page_url}")

            # Visit the page to trigger CSS regeneration
            response = requests.get(page_url, timeout=10)

            if response.status_code == 200:
                print(f"  [OK] Page loaded (Status: {response.status_code})")

                # Check if CSS file is accessible
                css_url = f"{SITE_URL}/wp-content/uploads/elementor/css/post-{post_id}.css"
                css_response = requests.get(css_url, timeout=5)

                if css_response.status_code == 200:
                    css_size = len(css_response.content)
                    has_global_colors = b'var(--e-global-color-' in css_response.content

                    print(f"  [OK] CSS file accessible (Size: {css_size} bytes)")
                    print(f"     Global Colors: {'YES' if has_global_colors else 'NO'}")
                    success_count += 1
                else:
                    print(f"  [ERROR] CSS file not accessible (Status: {css_response.status_code})")
            else:
                print(f"  [ERROR] Page failed to load (Status: {response.status_code})")

        except Exception as e:
            print(f"  [ERROR] Error: {e}")

        print()

    print("="*50)
    print(f"Summary: {success_count}/{len(post_ids)} pages processed successfully")
    print("="*50)

    return success_count == len(post_ids)

def main():
    if len(sys.argv) < 2:
        print("Usage: python force-css-regeneration.py <post_id> [post_id2] ...")
        print("\nExamples:")
        print("  python force-css-regeneration.py 21")
        print("  python force-css-regeneration.py 21 23 25 27 29")
        sys.exit(1)

    try:
        post_ids = [int(pid) for pid in sys.argv[1:]]
    except ValueError:
        print("[ERROR] Post IDs must be integers")
        sys.exit(1)

    print("\n" + "="*50)
    print("Elementor CSS Regeneration Tool")
    print("="*50 + "\n")

    print(f"Post IDs to process: {', '.join(str(p) for p in post_ids)}\n")

    # Try PHP method first
    if not PHP_SCRIPT.exists():
        print(f"[ERROR] PHP script not found at {PHP_SCRIPT}")
        print("Using HTTP method instead...\n")
        success = regenerate_css_via_http(post_ids)
    else:
        success = regenerate_css_via_php(post_ids)

    if success:
        print("\n[SUCCESS] CSS regeneration completed.")
        print("\nNext steps:")
        print("1. Clear browser cache")
        print("2. Visit your pages on frontend")
        print("3. Verify styles are showing correctly")
        sys.exit(0)
    else:
        print("\n[FAILED] CSS regeneration encountered errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
