<?php
/**
 * Switch Elementor CSS Print Method to Internal Embedding
 * This forces Elementor to output CSS directly in HTML (no external files)
 */

require_once(__DIR__ . '/wp-load.php');

echo "🔧 Switching Elementor CSS Print Method...\n\n";

// Get current method
$current_method = get_option('elementor_css_print_method');
echo "📋 Current method: " . ($current_method ?: 'external') . "\n";

// Switch to internal embedding
update_option('elementor_css_print_method', 'internal');
echo "✅ Switched to: internal\n\n";

// Clear all caches
if (did_action('elementor/loaded')) {
    \Elementor\Plugin::instance()->files_manager->clear_cache();
    echo "✅ Elementor cache cleared\n";
}

// Force regenerate CSS for page 21
$css_file = \Elementor\Core\Files\CSS\Post::create(21);
$css_file->update();
echo "✅ CSS regenerated for page 21\n\n";

echo "🌐 Visit: http://svetlinkielementor.local\n";
echo "   Changes should now be visible!\n";
?>
