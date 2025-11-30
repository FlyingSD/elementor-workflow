<?php
/**
 * NUCLEAR CACHE CLEARING - Clear EVERYTHING
 */

require_once(__DIR__ . '/wp-load.php');

echo "💣 NUCLEAR CACHE CLEARING...\n\n";

// 1. Clear WordPress transients
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");
echo "✅ WordPress transients cleared\n";

// 2. Clear WordPress object cache
wp_cache_flush();
echo "✅ Object cache flushed\n";

// 3. Clear Elementor cache
if (did_action('elementor/loaded')) {
    \Elementor\Plugin::instance()->files_manager->clear_cache();
    echo "✅ Elementor cache cleared\n";
}

// 4. Delete Elementor CSS files manually
$upload_dir = wp_upload_dir();
$elementor_css_dir = $upload_dir['basedir'] . '/elementor/css/';
if (is_dir($elementor_css_dir)) {
    $files = glob($elementor_css_dir . 'post-21*.css');
    foreach ($files as $file) {
        if (is_file($file)) {
            unlink($file);
            echo "🗑️  Deleted: " . basename($file) . "\n";
        }
    }
}

// 5. Force regenerate CSS for page 21
$css_file = \Elementor\Core\Files\CSS\Post::create(21);
$css_file->update();
echo "✅ CSS regenerated for page 21\n\n";

// 6. Update post modified time to force cache bust
wp_update_post(array(
    'ID' => 21,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
));
echo "✅ Post 21 timestamp updated\n\n";

echo "🔄 HARD REFRESH YOUR BROWSER (Ctrl+Shift+R or Ctrl+F5)\n";
echo "🌐 Visit: http://svetlinkielementor.local\n";
?>
