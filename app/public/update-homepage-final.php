<?php
/**
 * Update homepage with v4 split sections structure
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Homepage Update</title></head><body>";
echo "<h1>Updating Homepage...</h1>";

// Read the JSON file
$json_file = __DIR__ . '/../../homepage-v4-split-sections.json';
$elementor_data = file_get_contents($json_file);

if (!$elementor_data) {
    echo "<p style='color:red;'>ERROR: Could not read JSON file</p>";
    exit;
}

// Validate JSON
$decoded = json_decode($elementor_data, true);
if (!$decoded) {
    echo "<p style='color:red;'>ERROR: Invalid JSON</p>";
    exit;
}

echo "<p>Found " . count($decoded) . " sections</p>";

// Update page 21
$page_id = 21;
update_post_meta($page_id, '_elementor_data', $elementor_data);
update_post_meta($page_id, '_elementor_edit_mode', 'builder');

echo "<p>SUCCESS: Page meta updated</p>";

// Clear Elementor cache
if (did_action('elementor/loaded')) {
    $elementor = \Elementor\Plugin::instance();
    $elementor->files_manager->clear_cache();
    echo "<p>SUCCESS: Elementor cache cleared</p>";

    // Force CSS regeneration
    $css_file = \Elementor\Core\Files\CSS\Post::create($page_id);
    $css_file->delete();
    $css_file->update();
    echo "<p>SUCCESS: CSS regenerated</p>";
}

// Clear WordPress caches
wp_cache_flush();
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");
echo "<p>SUCCESS: WordPress caches cleared</p>";

// Update post modified time
wp_update_post(array(
    'ID' => $page_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
));
echo "<p>SUCCESS: Post timestamp updated</p>";

echo "<h2>DONE!</h2>";
echo "<p><strong>Now do a hard refresh:</strong> Ctrl+Shift+R</p>";
echo "<p><a href='http://svetlinkielementor.local' target='_blank' style='font-size:20px; color:blue;'>VIEW HOMEPAGE</a></p>";
echo "</body></html>";
?>
