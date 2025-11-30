"""
Take full-page screenshot of homepage
"""
from playwright.sync_api import sync_playwright
import os

def take_screenshot():
    screenshots_dir = r"C:\Users\denit\Local Sites\svetlinkielementor\screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        print("Navigating to homepage...")
        page.goto('http://svetlinkielementor.local/home')
        page.wait_for_load_state('networkidle')

        screenshot_path = os.path.join(screenshots_dir, 'homepage-current-full.png')
        print("Taking full-page screenshot...")
        page.screenshot(path=screenshot_path, full_page=True)

        browser.close()
        print(f"Screenshot saved to: {screenshot_path}")

if __name__ == "__main__":
    take_screenshot()
