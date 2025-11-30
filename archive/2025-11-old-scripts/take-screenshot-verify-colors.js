const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    console.log('Launching browser...');
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--ignore-certificate-errors']
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });

    console.log('Navigating to homepage...');
    await page.goto('http://svetlinkielementor.local', {
        waitUntil: 'networkidle2',
        timeout: 30000
    });

    // Wait for Elementor content to load
    await page.waitForSelector('.elementor-section', { timeout: 10000 });

    // Take full page screenshot
    const screenshotPath = path.join(__dirname, 'screenshots', 'homepage-after-colors-update.png');
    await page.screenshot({
        path: screenshotPath,
        fullPage: true
    });

    console.log(`Screenshot saved: ${screenshotPath}`);

    // Check icon colors via JavaScript
    const iconColors = await page.evaluate(() => {
        const icons = document.querySelectorAll('.elementor-icon');
        const colors = [];

        icons.forEach((icon, index) => {
            const styles = window.getComputedStyle(icon);
            const bgColor = styles.backgroundColor;
            const color = styles.color;

            // Get parent widget to identify which icon
            const widget = icon.closest('.elementor-widget-icon-box');
            const widgetId = widget ? widget.dataset.id : 'unknown';

            colors.push({
                index: index,
                widgetId: widgetId,
                backgroundColor: bgColor,
                iconColor: color
            });
        });

        return colors;
    });

    console.log('\n=== ICON COLORS DETECTED ===');
    iconColors.forEach(icon => {
        console.log(`Icon ${icon.index} (Widget: ${icon.widgetId}):`);
        console.log(`  Background: ${icon.backgroundColor}`);
        console.log(`  Icon Color: ${icon.iconColor}`);
        console.log('');
    });

    // Save color data to JSON
    const colorDataPath = path.join(__dirname, 'icon-colors-detected.json');
    fs.writeFileSync(colorDataPath, JSON.stringify(iconColors, null, 2));
    console.log(`Color data saved: ${colorDataPath}`);

    await browser.close();
    console.log('\n✅ Complete!');
})();
