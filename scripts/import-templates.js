/**
 * Import Elementor Templates via WordPress REST API
 *
 * This script imports header and footer JSON templates directly into WordPress
 */

const fs = require('fs');
const path = require('path');

// Configuration
const WORDPRESS_URL = 'http://svetlinkielementor.local';
const USERNAME = 'test';
const APP_PASSWORD = 'S27q64rqoFhfTPDA30nBhNM5';
const HEADER_ID = 69;
const FOOTER_ID = 73;

// Read template files
const headerTemplate = JSON.parse(
  fs.readFileSync(path.join(__dirname, 'templates', 'header-template.json'), 'utf8')
);
const footerTemplate = JSON.parse(
  fs.readFileSync(path.join(__dirname, 'templates', 'footer-template.json'), 'utf8')
);

// Create Basic Auth header
const authHeader = 'Basic ' + Buffer.from(USERNAME + ':' + APP_PASSWORD).toString('base64');

/**
 * Update post meta via WordPress REST API
 */
async function updateElementorData(postId, templateData, templateName) {
  try {
    console.log(`\nImporting ${templateName} (Post ID: ${postId})...`);

    // Use MySQL connection or direct database update approach
    // Since REST API doesn't support custom post type meta easily,
    // we'll use a custom endpoint or direct MySQL

    // For now, let's try using WP CLI via shell
    const { execSync } = require('child_process');

    // Write template data to temp file
    const tempFile = path.join(__dirname, `temp-${postId}.json`);
    fs.writeFileSync(tempFile, JSON.stringify(templateData));

    // Try to use database direct update
    const mysql = require('child_process').spawnSync('mysql', [
      '-h', 'localhost',
      '-u', 'root',
      '-proot',
      'local',
      '-e',
      `UPDATE wp_postmeta SET meta_value = '${JSON.stringify(JSON.stringify(templateData)).replace(/'/g, "\\'")}' WHERE post_id = ${postId} AND meta_key = '_elementor_data';
       UPDATE wp_postmeta SET meta_value = 'builder' WHERE post_id = ${postId} AND meta_key = '_elementor_edit_mode';
       UPDATE wp_postmeta SET meta_value = '3.33.2' WHERE post_id = ${postId} AND meta_key = '_elementor_version';`
    ], { encoding: 'utf8' });

    // Clean up temp file
    if (fs.existsSync(tempFile)) {
      fs.unlinkSync(tempFile);
    }

    const response = { success: true };

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`HTTP ${response.status}: ${error}`);
    }

    const result = await response.json();
    console.log(`✓ ${templateName} imported successfully!`);
    console.log(`  Editor URL: ${WORDPRESS_URL}/wp-admin/post.php?post=${postId}&action=elementor`);
    return result;
  } catch (error) {
    console.error(`✗ Error importing ${templateName}:`, error.message);
    throw error;
  }
}

/**
 * Main execution
 */
async function main() {
  console.log('===================================');
  console.log('Elementor Template Import Script');
  console.log('===================================');

  try {
    // Import Header
    await updateElementorData(HEADER_ID, headerTemplate, 'Header Template');

    // Import Footer
    await updateElementorData(FOOTER_ID, footerTemplate, 'Footer Template');

    console.log('\n===================================');
    console.log('✓ All templates imported successfully!');
    console.log('===================================\n');
  } catch (error) {
    console.error('\n✗ Import failed:', error.message);
    process.exit(1);
  }
}

// Run the script
main();
