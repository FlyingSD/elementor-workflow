const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({
    headless: false, // Show browser for debugging
    slowMo: 500 // Slow down actions for visibility
  });

  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });

  const page = await context.newPage();

  console.log('🔐 Step 1: Login to WordPress...');

  try {
    // Navigate to login page
    await page.goto('http://svetlinkielementor.local/wp-login.php', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    // Fill login credentials
    await page.fill('#user_login', 'test');
    await page.fill('#user_pass', 'test');

    // Click login button
    await page.click('#wp-submit');

    // Wait for dashboard
    await page.waitForLoadState('networkidle');
    console.log('✅ Login successful!');

    console.log('🎨 Step 2: Opening Elementor editor for page 21...');

    // Navigate to Elementor editor - use 'load' instead of 'networkidle' for faster loading
    await page.goto('http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor', {
      waitUntil: 'load',
      timeout: 90000 // Elementor can take longer to load
    });

    console.log('⏳ Waiting for Elementor to load (can take 15-30 seconds)...');

    // Wait for Elementor iframe to appear
    await page.waitForSelector('#elementor-preview-iframe', { timeout: 90000 });
    console.log('✅ Elementor iframe appeared!');

    // Wait for panel to be ready
    await page.waitForSelector('#elementor-panel-saver-button-publish, button:has-text("Publish")', {
      timeout: 90000,
      state: 'visible'
    });
    console.log('✅ Elementor editor fully loaded!');

    // Wait a bit more for all UI elements to render
    await page.waitForTimeout(3000);

    console.log('🔘 Step 3: Looking for Update/Publish button...');

    // Try different selectors for Update/Publish button
    let updateButton = null;
    const selectors = [
      'button#elementor-panel-saver-button-publish',
      '#elementor-panel-saver-button-publish',
      'button:has-text("Publish")',
      'button:has-text("Update")',
      '.elementor-button-success',
      '#elementor-panel-saver-button-save-options',
      '[data-bind*="publish"]'
    ];

    for (const selector of selectors) {
      try {
        const button = await page.$(selector);
        if (button) {
          const isVisible = await button.isVisible();
          if (isVisible) {
            updateButton = button;
            console.log(`✅ Found Update/Publish button with selector: ${selector}`);
            break;
          }
        }
      } catch (e) {
        // Continue to next selector
      }
    }

    if (!updateButton) {
      console.log('⚠️ Update button not found with standard selectors');
      console.log('📸 Taking screenshot of editor to debug...');
      await page.screenshot({
        path: path.join(__dirname, '../../screenshots/editor-update-button-not-found.png'),
        fullPage: false
      });

      // Try to find any button with "Publish" or "Update" text
      console.log('🔍 Searching for any button with Publish/Update text...');
      const allButtons = await page.$$('button');
      for (const btn of allButtons) {
        const text = await btn.textContent();
        if (text && (text.includes('Publish') || text.includes('Update'))) {
          console.log(`✅ Found button with text: ${text}`);
          updateButton = btn;
          break;
        }
      }

      if (!updateButton) {
        throw new Error('Update button not found');
      }
    }

    console.log('🖱️ Clicking Update/Publish button...');
    await updateButton.click();

    // Wait for save confirmation
    console.log('⏳ Waiting for save confirmation...');
    await page.waitForTimeout(5000);

    // Look for success message
    try {
      await page.waitForSelector('.elementor-panel-saver-button-success, .elementor-button-success', {
        timeout: 10000
      });
      console.log('✅ Update successful!');
    } catch (e) {
      console.log('⚠️ Could not confirm success message, but continuing...');
    }

    console.log('📸 Step 4: Taking screenshot of editor after update...');
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/elementor-editor-after-update.png'),
      fullPage: false
    });
    console.log('✅ Editor screenshot saved!');

    console.log('🏠 Step 5: Navigating to homepage...');

    // Navigate to homepage
    await page.goto('http://svetlinkielementor.local/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    console.log('⏳ Waiting for page to fully load...');
    await page.waitForTimeout(3000);

    console.log('✅ Homepage loaded!');

    console.log('📸 Step 6: Taking homepage screenshots...');

    // Desktop screenshot
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-desktop.png'),
      fullPage: true
    });
    console.log('✅ Desktop screenshot saved!');

    // Tablet screenshot
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-tablet.png'),
      fullPage: true
    });
    console.log('✅ Tablet screenshot saved!');

    // Mobile screenshot
    await page.setViewportSize({ width: 375, height: 812 });
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-mobile.png'),
      fullPage: true
    });
    console.log('✅ Mobile screenshot saved!');

    console.log('📸 Step 7: Taking section screenshots (desktop)...');

    // Reset to desktop for section screenshots
    await page.setViewportSize({ width: 1920, height: 1080 });

    // Try to find and screenshot each section
    const sections = [
      { name: 'hero', selector: 'section.elementor-section:first-of-type', filename: 'v4-hero-section.png' },
      { name: 'blog', selector: 'section.elementor-section:nth-of-type(2)', filename: 'v4-blog-section.png' },
      { name: 'benefits', selector: 'section.elementor-section:nth-of-type(3)', filename: 'v4-benefits-section.png' },
      { name: 'programs', selector: 'section.elementor-section:nth-of-type(4)', filename: 'v4-programs-section.png' }
    ];

    for (const section of sections) {
      try {
        const element = await page.$(section.selector);
        if (element) {
          await element.screenshot({
            path: path.join(__dirname, `../../screenshots/${section.filename}`)
          });
          console.log(`✅ ${section.name} section screenshot saved!`);
        } else {
          console.log(`⚠️ ${section.name} section not found`);
        }
      } catch (e) {
        console.log(`⚠️ Error capturing ${section.name} section: ${e.message}`);
      }
    }

    console.log('✅ All screenshots completed!');

  } catch (error) {
    console.error('❌ Error:', error.message);

    // Take error screenshot
    try {
      await page.screenshot({
        path: path.join(__dirname, '../../screenshots/error-screenshot.png'),
        fullPage: true
      });
      console.log('📸 Error screenshot saved');
    } catch (e) {
      console.error('Could not save error screenshot');
    }
  } finally {
    await browser.close();
    console.log('🔒 Browser closed');
  }
})();
