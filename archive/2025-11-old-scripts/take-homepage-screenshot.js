/**
 * Take full-page screenshot of homepage
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function takeScreenshot() {
    const screenshotsDir = path.join(__dirname, 'screenshots');
    if (!fs.existsSync(screenshotsDir)) {
        fs.mkdirSync(screenshotsDir, { recursive: true });
    }

    const browser = await chromium.launch();
    const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });

    console.log('Navigating to homepage...');
    await page.goto('http://svetlinkielementor.local/home');
    await page.waitForLoadState('networkidle');

    const screenshotPath = path.join(screenshotsDir, 'homepage-current-full.png');
    console.log('Taking full-page screenshot...');
    await page.screenshot({ path: screenshotPath, fullPage: true });

    await browser.close();
    console.log(`Screenshot saved to: ${screenshotPath}`);
}

takeScreenshot().catch(console.error);
