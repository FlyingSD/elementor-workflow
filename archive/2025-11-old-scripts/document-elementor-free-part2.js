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

async function documentElementorFreePart2() {
    const browser = await chromium.launch({
        headless: false,
        slowMo: 800
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

        console.log('📋 Phase 2: Navigate to Elementor Editor');
        await page.goto('http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor');

        // Wait for Elementor to load
        await page.waitForSelector('#elementor-preview-iframe', { timeout: 30000 });
        await delay(5000);

        console.log('📋 Phase 3: Document Color Picker and Global Colors');

        // Click on a section in the iframe
        const iframe = page.frameLocator('#elementor-preview-iframe');
        const section = iframe.locator('.elementor-section').first();
        await section.click();
        await delay(2000);

        // Go to Style tab
        const styleTab = page.locator('#elementor-panel-content').getByText('Style', { exact: true });
        if (await styleTab.isVisible()) {
            await styleTab.click();
            await delay(1500);
        }

        // Click Background
        const backgroundControl = page.locator('.elementor-control-section_background');
        if (await backgroundControl.isVisible()) {
            await backgroundControl.click();
            await delay(1000);
        }

        // Try gradient
        const gradientBtn = page.locator('[data-setting="background_background"]').locator('[data-value="gradient"]');
        if (await gradientBtn.isVisible()) {
            await gradientBtn.click();
            await delay(1500);
            await takeScreenshot(page, '10-section-background-gradient.png');
        }

        // Click on gradient color picker to show Global Colors
        const colorInput = page.locator('.elementor-control-background_color').locator('.pcr-button').first();
        if (await colorInput.isVisible()) {
            await colorInput.click();
            await delay(2000);
            await takeScreenshot(page, '12-color-picker-global-colors.png');

            // Close color picker
            await page.keyboard.press('Escape');
            await delay(500);
        }

        console.log('📋 Phase 4: Document Advanced Section Options');

        // Click Advanced tab
        const advancedTab = page.locator('#elementor-panel-content').getByText('Advanced', { exact: true });
        if (await advancedTab.isVisible()) {
            await advancedTab.click();
            await delay(1500);
            await takeScreenshot(page, '13-section-advanced-layout.png');

            // Scroll to see spacing
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 300;
            });
            await delay(1000);
            await takeScreenshot(page, '14-section-advanced-spacing.png');

            // Scroll to see border
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 600;
            });
            await delay(1000);
            await takeScreenshot(page, '15-section-advanced-border.png');
        }

        console.log('📋 Phase 5: Add and Document Widgets');

        // Close current panel - click on Navigator icon
        const navigatorBtn = page.locator('#elementor-panel-footer-navigator');
        if (await navigatorBtn.isVisible()) {
            await navigatorBtn.click();
            await delay(1000);
        }

        // Now click on empty space in iframe to deselect
        const emptySpace = iframe.locator('body');
        await emptySpace.click({ position: { x: 100, y: 100 } });
        await delay(1000);

        // Open widgets panel using footer button
        const widgetsFooterBtn = page.locator('#elementor-panel-footer-add-button');
        if (await widgetsFooterBtn.isVisible()) {
            await widgetsFooterBtn.click();
            await delay(2000);
        }

        // Search for Image Carousel
        const searchInput = page.locator('#elementor-panel-elements-search-input');
        await searchInput.fill('carousel');
        await delay(1500);

        await takeScreenshot(page, '16-search-carousel.png');

        // Click Image Carousel widget
        const carouselWidget = page.locator('.elementor-element').filter({ hasText: 'Image Carousel' }).first();
        if (await carouselWidget.isVisible()) {
            // Drag to section
            const firstSection = iframe.locator('.elementor-section').first();
            await carouselWidget.dragTo(firstSection, {
                force: true,
                targetPosition: { x: 400, y: 200 }
            });
            await delay(3000);

            await takeScreenshot(page, '17-carousel-content-options.png');

            // Scroll to see navigation options
            await page.evaluate(() => {
                const panel = document.querySelector('#elementor-panel-content-wrapper');
                if (panel) panel.scrollTop = 400;
            });
            await delay(1000);
            await takeScreenshot(page, '18-carousel-navigation-options.png');

            // Click Style tab
            const carouselStyleTab = page.locator('#elementor-panel-content').getByText('Style');
            if (await carouselStyleTab.isVisible()) {
                await carouselStyleTab.click();
                await delay(1500);
                await takeScreenshot(page, '19-carousel-style-options.png');
            }
        }

        console.log('📋 Phase 6: Document Button Widget');

        // Add button widget
        await widgetsFooterBtn.click();
        await delay(1000);

        await searchInput.fill('button');
        await delay(1500);

        const buttonWidget = page.locator('.elementor-element').filter({ hasText: 'Button' }).first();
        if (await buttonWidget.isVisible()) {
            const firstSection = iframe.locator('.elementor-section').first();
            await buttonWidget.dragTo(firstSection, {
                force: true,
                targetPosition: { x: 600, y: 200 }
            });
            await delay(3000);

            await takeScreenshot(page, '20-button-content-options.png');

            // Style tab
            const btnStyleTab = page.locator('#elementor-panel-content').getByText('Style');
            if (await btnStyleTab.isVisible()) {
                await btnStyleTab.click();
                await delay(1500);
                await takeScreenshot(page, '21-button-style-options.png');

                // Scroll for hover
                await page.evaluate(() => {
                    const panel = document.querySelector('#elementor-panel-content-wrapper');
                    if (panel) panel.scrollTop = 400;
                });
                await delay(1000);
                await takeScreenshot(page, '22-button-hover-options.png');
            }
        }

        console.log('📋 Phase 7: Document Icon Box Widget');

        await widgetsFooterBtn.click();
        await delay(1000);

        await searchInput.fill('icon box');
        await delay(1500);

        const iconBoxWidget = page.locator('.elementor-element').filter({ hasText: 'Icon Box' }).first();
        if (await iconBoxWidget.isVisible()) {
            const firstSection = iframe.locator('.elementor-section').first();
            await iconBoxWidget.dragTo(firstSection, {
                force: true,
                targetPosition: { x: 800, y: 200 }
            });
            await delay(3000);

            await takeScreenshot(page, '23-iconbox-content-options.png');

            // Style tab
            const iconBoxStyleTab = page.locator('#elementor-panel-content').getByText('Style');
            if (await iconBoxStyleTab.isVisible()) {
                await iconBoxStyleTab.click();
                await delay(1500);
                await takeScreenshot(page, '24-iconbox-style-icon.png');

                // Scroll to box settings
                await page.evaluate(() => {
                    const panel = document.querySelector('#elementor-panel-content-wrapper');
                    if (panel) panel.scrollTop = 600;
                });
                await delay(1000);
                await takeScreenshot(page, '25-iconbox-style-box.png');
            }

            // Advanced tab for border/shadow
            const iconBoxAdvancedTab = page.locator('#elementor-panel-content').getByText('Advanced');
            if (await iconBoxAdvancedTab.isVisible()) {
                await iconBoxAdvancedTab.click();
                await delay(1500);

                // Scroll to border section
                await page.evaluate(() => {
                    const panel = document.querySelector('#elementor-panel-content-wrapper');
                    if (panel) panel.scrollTop = 400;
                });
                await delay(1000);
                await takeScreenshot(page, '26-iconbox-advanced-border-shadow.png');
            }
        }

        console.log('📋 Phase 8: Document Responsive Controls');

        // Click responsive switcher in footer
        const responsiveBtn = page.locator('#elementor-panel-footer-responsive i');
        if (await responsiveBtn.isVisible()) {
            await responsiveBtn.click();
            await delay(1000);
            await takeScreenshot(page, '27-responsive-switcher.png');

            // Switch to tablet
            const tabletMode = page.locator('[data-device="tablet"]').first();
            if (await tabletMode.isVisible()) {
                await tabletMode.click();
                await delay(2000);
                await takeScreenshot(page, '28-responsive-tablet-view.png');
            }

            // Switch to mobile
            const mobileMode = page.locator('[data-device="mobile"]').first();
            if (await mobileMode.isVisible()) {
                await mobileMode.click();
                await delay(2000);
                await takeScreenshot(page, '29-responsive-mobile-view.png');
            }
        }

        console.log('✅ Part 2 screenshots captured successfully!');

    } catch (error) {
        console.error('❌ Error during documentation:', error.message);
        await takeScreenshot(page, 'error-state-part2.png');
    } finally {
        await delay(3000);
        await browser.close();
    }
}

documentElementorFreePart2();
