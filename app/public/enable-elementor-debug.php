<?php
/**
 * Enable Elementor Debug Bar
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Enable Debug</title></head><body>";
echo "<h1>Enabling Elementor Debug Mode...</h1>";

// Enable Elementor Debug Bar
update_option('elementor_enable_inspector', 'yes');
update_option('elementor_enable_debug_bar', 'yes');

echo "<p>SUCCESS: Elementor Debug Bar enabled</p>";

// Also enable WordPress debug mode
$config_file = __DIR__ . '/wp-config.php';
if (file_exists($config_file)) {
    echo "<p>Note: To enable full WordPress debug, add to wp-config.php:</p>";
    echo "<pre>define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', true);</pre>";
}

echo "<h2>How to Use Elementor Debugger:</h2>";
echo "<ol>";
echo "<li>Go to any page on the frontend: <a href='http://svetlinkielementor.local' target='_blank'>http://svetlinkielementor.local</a></li>";
echo "<li>Look for the Debug Bar next to 'Edit with Elementor' button</li>";
echo "<li>Click it to see CSS files loaded, errors, and performance info</li>";
echo "</ol>";

echo "<h2>To View Global Colors:</h2>";
echo "<ol>";
echo "<li>Edit any page with Elementor</li>";
echo "<li>Click hamburger menu (top left)</li>";
echo "<li>Go to: Site Settings > Global Colors</li>";
echo "<li>Add Custom Colors there</li>";
echo "</ol>";

echo "</body></html>";
?>
