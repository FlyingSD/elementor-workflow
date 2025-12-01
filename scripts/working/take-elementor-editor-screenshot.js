const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();

  console.log('Navigating to Elementor editor for page 21...');

  // Navigate to Elementor editor
  await page.goto('http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor', {
    waitUntil: 'networkidle',
    timeout: 60000
  });

  console.log('Waiting for editor to load...');

  // Wait for Elementor editor to load (look for the panel)
  try {
    await page.waitForSelector('#elementor-panel-header', { timeout: 30000 });
    console.log('Editor panel loaded');
  } catch (e) {
    console.log('Editor panel not found, trying alternative selector...');
    await page.waitForTimeout(5000);
  }

  // Wait a bit more for full load
  await page.waitForTimeout(3000);

  console.log('Taking full editor screenshot...');
  await page.screenshot({
    path: 'screenshots/elementor-editor-full.png',
    fullPage: false
  });

  console.log('Taking screenshot of bottom left (where Update button is)...');
  // Take a screenshot of the bottom-left corner where Update button should be
  await page.screenshot({
    path: 'screenshots/elementor-editor-update-button.png',
    clip: { x: 0, y: 800, width: 400, height: 280 }
  });

  console.log('✅ Screenshots saved:');
  console.log('   - screenshots/elementor-editor-full.png (full editor)');
  console.log('   - screenshots/elementor-editor-update-button.png (bottom left panel)');

  await browser.close();
})();
