const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    slowMo: 500
  });

  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });

  const page = await context.newPage();

  console.log('📸 SCREENSHOT COLLECTION STARTING...\n');

  try {
    console.log('🏠 Step 1: Navigating to homepage...');

    // Navigate to homepage
    await page.goto('http://svetlinkielementor.local/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    console.log('⏳ Waiting for page to fully load...');
    await page.waitForTimeout(3000);
    console.log('✅ Homepage loaded!\n');

    console.log('📸 Step 2: Taking full page screenshots...\n');

    // Desktop screenshot
    console.log('  📱 Desktop (1920x1080)...');
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.waitForTimeout(1000); // Wait for reflow
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-desktop.png'),
      fullPage: true
    });
    console.log('  ✅ Desktop screenshot saved!');

    // Tablet screenshot
    console.log('  📱 Tablet (768x1024)...');
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.waitForTimeout(1000);
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-tablet.png'),
      fullPage: true
    });
    console.log('  ✅ Tablet screenshot saved!');

    // Mobile screenshot
    console.log('  📱 Mobile (375x812)...');
    await page.setViewportSize({ width: 375, height: 812 });
    await page.waitForTimeout(1000);
    await page.screenshot({
      path: path.join(__dirname, '../../screenshots/v4-homepage-mobile.png'),
      fullPage: true
    });
    console.log('  ✅ Mobile screenshot saved!\n');

    console.log('📸 Step 3: Taking section screenshots (desktop)...\n');

    // Reset to desktop for section screenshots
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.waitForTimeout(1000);

    // Reload page to ensure proper layout
    await page.goto('http://svetlinkielementor.local/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });
    await page.waitForTimeout(2000);

    // Try to find and screenshot each section
    const sections = [
      { name: 'Hero', selector: 'section.elementor-section:first-of-type', filename: 'v4-hero-section.png' },
      { name: 'Blog', selector: 'section.elementor-section:nth-of-type(2)', filename: 'v4-blog-section.png' },
      { name: 'Benefits', selector: 'section.elementor-section:nth-of-type(3)', filename: 'v4-benefits-section.png' },
      { name: 'Programs', selector: 'section.elementor-section:nth-of-type(4)', filename: 'v4-programs-section.png' }
    ];

    for (const section of sections) {
      try {
        console.log(`  📷 ${section.name} section...`);
        const element = await page.$(section.selector);
        if (element) {
          await element.screenshot({
            path: path.join(__dirname, `../../screenshots/${section.filename}`)
          });
          console.log(`  ✅ ${section.name} section screenshot saved!`);
        } else {
          console.log(`  ⚠️ ${section.name} section not found`);
        }
      } catch (e) {
        console.log(`  ⚠️ Error capturing ${section.name} section: ${e.message}`);
      }
    }

    console.log('\n📊 Step 4: Gathering page structure info...\n');

    // Get section count
    const sectionCount = await page.$$eval('section.elementor-section', sections => sections.length);
    console.log(`  Total sections found: ${sectionCount}`);

    // Get headings
    const headings = await page.$$eval('h1, h2, h3', elements =>
      elements.map(el => ({ tag: el.tagName, text: el.textContent.trim().substring(0, 50) }))
    );
    console.log(`  Headings found: ${headings.length}`);
    headings.slice(0, 5).forEach((h, i) => {
      console.log(`    ${i + 1}. <${h.tag}> ${h.text}${h.text.length > 50 ? '...' : ''}`);
    });

    // Get button count
    const buttonCount = await page.$$eval('a.elementor-button, button.elementor-button', buttons => buttons.length);
    console.log(`  Buttons found: ${buttonCount}`);

    console.log('\n✅ ALL SCREENSHOTS COMPLETED SUCCESSFULLY!\n');

    console.log('📁 Screenshots saved to:');
    console.log('  - screenshots/v4-homepage-desktop.png');
    console.log('  - screenshots/v4-homepage-tablet.png');
    console.log('  - screenshots/v4-homepage-mobile.png');
    console.log('  - screenshots/v4-hero-section.png');
    console.log('  - screenshots/v4-blog-section.png');
    console.log('  - screenshots/v4-benefits-section.png');
    console.log('  - screenshots/v4-programs-section.png');

  } catch (error) {
    console.error('\n❌ Error:', error.message);

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
    console.log('\n🔒 Browser closed');
  }
})();
