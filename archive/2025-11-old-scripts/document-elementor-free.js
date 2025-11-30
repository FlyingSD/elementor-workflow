const { chromium } = require('playwright');
const path = require('path');

async function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function takeScreenshot(page, name, fullPage = false) {
    const screenshotPath = path.join(__dirname, 'screenshots', 'elementor-free-capabilities', name);
    await page.screenshot({
        path: screenshotPath,
        fullPage: fullPage
    });
    console.log(`✅ Screenshot saved: ${name}`);
}

async function documentElementorFree() {
    const browser = await chromium.launch({
        headless: false,
        slowMo: 500
    });

    const context = await browser.newContext({
        viewport: { width: 1920, height: 1080 }
    });

    const page = await context.newPage();

    try {
        console.log('📋 Phase 1: Login to WordPress Admin');
        await page.goto('http://svetlinkielementor.local/wp-admin/');
        await delay(2000);

        // Login
        await page.fill('#user_login', 'test');
        await page.fill('#user_pass', 'test');
        await page.click('#wp-submit');
        await delay(3000);

        console.log('✅ Logged in successfully');

        console.log('📋 Phase 2: Navigate to Elementor Editor (Page 21)');
        await page.goto('http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor');

        // Wait for Elementor to load completely
        await page.waitForSelector('#elementor-preview-iframe', { timeout: 30000 });
        await delay(5000); // Extra wait for full initialization

        await takeScreenshot(page, '01-elementor-editor-homepage.png', true);

        console.log('📋 Phase 3: Document Widget Panel');

        // Click Add Section button to open widget panel
        const addSectionButton = await page.locator('.elementor-add-section-button').first();
        if (await addSectionButton.isVisible()) {
            await addSectionButton.click();
            await delay(1500);
        }

        // Try to open panel if not already open
        const panelButton = await page.locator('#elementor-panel-header-add-button');
        if (await panelButton.isVisible()) {
            await panelButton.click();
            await delay(1500);
        }

        await takeScreenshot(page, '02-widget-panel-opened.png');

        // Document BASIC widgets
        console.log('📸 Documenting BASIC widgets...');
        const basicCategory = await page.locator('.elementor-element-wrapper').filter({ hasText: 'Basic' }).first();
        if (await basicCategory.isVisible()) {
            await basicCategory.scrollIntoViewIfNeeded();
            await delay(1000);
            await takeScreenshot(page, '03-widgets-basic.png');
        }

        // Document GENERAL/MEDIA widgets
        console.log('📸 Documenting GENERAL widgets...');
        await page.evaluate(() => {
            const panel = document.querySelector('#elementor-panel-content-wrapper');
            if (panel) panel.scrollTop = 300;
        });
        await delay(1000);
        await takeScreenshot(page, '04-widgets-general.png');

        // Scroll more to see PRO widgets
        console.log('📸 Documenting PRO widgets...');
        await page.evaluate(() => {
            const panel = document.querySelector('#elementor-panel-content-wrapper');
            if (panel) panel.scrollTop = 800;
        });
        await delay(1000);
        await takeScreenshot(page, '05-widgets-pro-locked.png');

        // Scroll to bottom
        await page.evaluate(() => {
            const panel = document.querySelector('#elementor-panel-content-wrapper');
            if (panel) panel.scrollTop = panel.scrollHeight;
        });
        await delay(1000);
        await takeScreenshot(page, '06-widgets-bottom.png');

        console.log('📋 Phase 4: Document Section Background Options');

        // Close widget panel and select a section
        const closeButton = await page.locator('#elementor-panel-header-menu-button');
        if (await closeButton.isVisible()) {
            await closeButton.click();
            await delay(500);
        }

        // Switch to preview iframe and click on a section
        const iframe = page.frameLocator('#elementor-preview-iframe');
        const section = iframe.locator('.elementor-section').first();
        await section.click();
        await delay(2000);

        await takeScreenshot(page, '07-section-selected.png');

        // Click Style tab
        const styleTab = await page.locator('#elementor-panel-content').locator('text=Style');
        if (await styleTab.isVisible()) {
            await styleTab.click();
            await delay(1500);
            await takeScreenshot(page, '08-section-style-tab.png');
        }

        // Click Background section
        const backgroundSection = await page.locator('.elementor-control-section_background');
        if (await backgroundSection.isVisible()) {
            await backgroundSection.click();
            await delay(1000);
        }

        await takeScreenshot(page, '09-section-background-classic.png');

        // Test Gradient background
        const gradientButton = await page.locator('[data-setting="background_background"]').locator('[data-value="gradient"]');
        if (await gradientButton.isVisible()) {
            await gradientButton.click();
            await delay(1500);
            await takeScreenshot(page, '10-section-background-gradient.png');

            // Scroll to see more gradient options
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 300;
            });
            await delay(1000);
            await takeScreenshot(page, '11-section-background-gradient-options.png');
        }

        console.log('📋 Phase 5: Document Color Picker (Global Colors)');

        // Click on a color picker to show Global Colors
        const colorPicker = await page.locator('.elementor-control-background_color input').first();
        if (await colorPicker.isVisible()) {
            await colorPicker.click();
            await delay(1500);
            await takeScreenshot(page, '12-color-picker-global-colors.png');

            // Click outside to close
            await page.locator('#elementor-panel-header').click();
            await delay(500);
        }

        console.log('📋 Phase 6: Document Advanced Section Options');

        // Click Advanced tab
        const advancedTab = await page.locator('#elementor-panel-content').locator('text=Advanced');
        if (await advancedTab.isVisible()) {
            await advancedTab.click();
            await delay(1500);
            await takeScreenshot(page, '13-section-advanced-layout.png');

            // Scroll to see spacing options
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 200;
            });
            await delay(1000);
            await takeScreenshot(page, '14-section-advanced-spacing.png');

            // Scroll to see border options
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 500;
            });
            await delay(1000);
            await takeScreenshot(page, '15-section-advanced-border.png');
        }

        console.log('📋 Phase 7: Document Widget Options - Image Carousel');

        // Add Image Carousel widget
        await page.locator('#elementor-panel-header-add-button').click();
        await delay(1000);

        // Search for Image Carousel
        const searchBox = await page.locator('#elementor-panel-elements-search-input');
        if (await searchBox.isVisible()) {
            await searchBox.fill('image carousel');
            await delay(1000);
        }

        await takeScreenshot(page, '16-search-image-carousel.png');

        // Drag carousel widget (or click it)
        const carouselWidget = await page.locator('.elementor-element').filter({ hasText: 'Image Carousel' }).first();
        if (await carouselWidget.isVisible()) {
            await carouselWidget.click();
            await delay(2000);
        }

        // Widget should be added and settings panel open
        await takeScreenshot(page, '17-carousel-content-tab.png');

        // Scroll to see autoplay and navigation options
        await page.evaluate(() => {
            const panel = document.querySelector('#elementor-panel-content-wrapper');
            if (panel) panel.scrollTop = 400;
        });
        await delay(1000);
        await takeScreenshot(page, '18-carousel-navigation-options.png');

        // Click Style tab for carousel
        const carouselStyleTab = await page.locator('#elementor-panel-content').locator('text=Style');
        if (await carouselStyleTab.isVisible()) {
            await carouselStyleTab.click();
            await delay(1500);
            await takeScreenshot(page, '19-carousel-style-tab.png');
        }

        console.log('📋 Phase 8: Document Button Widget Options');

        // Clear search and find Button widget
        await page.locator('#elementor-panel-header-add-button').click();
        await delay(500);
        await searchBox.fill('button');
        await delay(1000);

        const buttonWidget = await page.locator('.elementor-element').filter({ hasText: 'Button' }).first();
        if (await buttonWidget.isVisible()) {
            await buttonWidget.click();
            await delay(2000);
        }

        await takeScreenshot(page, '20-button-content-tab.png');

        // Button Style tab
        const buttonStyleTab = await page.locator('#elementor-panel-content').locator('text=Style');
        if (await buttonStyleTab.isVisible()) {
            await buttonStyleTab.click();
            await delay(1500);
            await takeScreenshot(page, '21-button-style-tab.png');

            // Scroll to see hover options
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 300;
            });
            await delay(1000);
            await takeScreenshot(page, '22-button-style-hover.png');
        }

        console.log('📋 Phase 9: Document Icon Box Widget Options');

        // Clear search and find Icon Box widget
        await page.locator('#elementor-panel-header-add-button').click();
        await delay(500);
        await searchBox.fill('icon box');
        await delay(1000);

        const iconBoxWidget = await page.locator('.elementor-element').filter({ hasText: 'Icon Box' }).first();
        if (await iconBoxWidget.isVisible()) {
            await iconBoxWidget.click();
            await delay(2000);
        }

        await takeScreenshot(page, '23-iconbox-content-tab.png');

        // Icon Box Style tab
        const iconBoxStyleTab = await page.locator('#elementor-panel-content').locator('text=Style');
        if (await iconBoxStyleTab.isVisible()) {
            await iconBoxStyleTab.click();
            await delay(1500);
            await takeScreenshot(page, '24-iconbox-style-icon.png');

            // Scroll to see box styling
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 500;
            });
            await delay(1000);
            await takeScreenshot(page, '25-iconbox-style-box.png');
        }

        console.log('📋 Phase 10: Document Responsive Controls');

        // Click responsive mode switcher
        const responsiveButton = await page.locator('#elementor-panel-footer-responsive');
        if (await responsiveButton.isVisible()) {
            await responsiveButton.click();
            await delay(1000);
            await takeScreenshot(page, '26-responsive-switcher.png');
        }

        // Switch to tablet view
        const tabletButton = await page.locator('[data-device-mode="tablet"]');
        if (await tabletButton.isVisible()) {
            await tabletButton.click();
            await delay(2000);
            await takeScreenshot(page, '27-responsive-tablet-view.png');
        }

        // Switch to mobile view
        const mobileButton = await page.locator('[data-device-mode="mobile"]');
        if (await mobileButton.isVisible()) {
            await mobileButton.click();
            await delay(2000);
            await takeScreenshot(page, '28-responsive-mobile-view.png');
        }

        console.log('✅ All screenshots captured successfully!');
        console.log('📁 Screenshots saved to: screenshots/elementor-free-capabilities/');

    } catch (error) {
        console.error('❌ Error during documentation:', error.message);
        await takeScreenshot(page, 'error-state.png');
    } finally {
        await delay(3000);
        await browser.close();
    }
}

documentElementorFree();
