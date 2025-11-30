<?php
/**
 * Web-accessible CSS Regeneration Endpoint
 * Visit: http://svetlinkielementor.local/regenerate-css-web.php
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>CSS Regeneration</title></head><body>";
echo "<h1>🔄 Regenerating Elementor CSS...</h1>";

// Clear Elementor cache
if (did_action('elementor/loaded')) {
    $elementor = \Elementor\Plugin::instance();

    // Clear cache
    $elementor->files_manager->clear_cache();
    echo "<p>✅ Elementor cache cleared</p>";

    // Force CSS regeneration for page 21
    $css_file = \Elementor\Core\Files\CSS\Post::create(21);
    $css_file->delete();
    echo "<p>✅ Old CSS deleted</p>";

    $css_file->update();
    echo "<p>✅ New CSS generated</p>";
}

// Clear WordPress caches
wp_cache_flush();
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");
echo "<p>✅ WordPress caches cleared</p>";

// Update post modified time to bust cache
wp_update_post(array(
    'ID' => 21,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
));
echo "<p>✅ Post timestamp updated</p>";

echo "<h2>✅ DONE!</h2>";
echo "<p><strong>Now do a hard refresh:</strong> Ctrl+Shift+R</p>";
echo "<p><a href='http://svetlinkielementor.local' target='_blank' style='font-size:20px; color:blue;'>→ VIEW HOMEPAGE</a></p>";
echo "</body></html>";
?>
