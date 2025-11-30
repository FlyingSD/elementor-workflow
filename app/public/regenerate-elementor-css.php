<?php
/**
 * Force Elementor CSS Regeneration
 * Clears all cached CSS files and forces regeneration
 */

// Load WordPress (wp-load.php is in the same directory as this script)
// Check multiple possible locations
$wp_load_paths = [
    __DIR__ . '/wp-load.php',                    // Same directory
    dirname(__DIR__) . '/wp-load.php',           // Parent directory
    dirname(dirname(__DIR__)) . '/wp-load.php',  // Two levels up
];

$loaded = false;
foreach ($wp_load_paths as $path) {
    if (file_exists($path)) {
        require_once($path);
        $loaded = true;
        break;
    }
}

if (!$loaded) {
    echo "❌ ERROR: Could not find wp-load.php\n";
    echo "Searched in:\n";
    foreach ($wp_load_paths as $path) {
        echo "  - $path\n";
    }
    exit(1);
}

echo "🔄 Starting Elementor CSS regeneration...\n\n";

// Check if Elementor is loaded
if (!did_action('elementor/loaded')) {
    echo "❌ ERROR: Elementor plugin is not active or not loaded.\n";
    exit(1);
}

try {
    // Get Elementor plugin instance
    $elementor = \Elementor\Plugin::instance();

    // Clear all Elementor cache
    echo "🗑️  Clearing Elementor cache...\n";
    $elementor->files_manager->clear_cache();

    // Force regenerate CSS for specific page (21 - Homepage)
    echo "🎨 Regenerating CSS for page 21 (Homepage)...\n";

    // Get the page data
    $post = get_post(21);
    if (!$post) {
        echo "❌ ERROR: Page 21 not found.\n";
        exit(1);
    }

    // Trigger CSS regeneration by simulating post update
    // This calls Elementor's save hooks which regenerate CSS
    wp_update_post(array(
        'ID' => 21,
        'post_modified' => current_time('mysql'),
        'post_modified_gmt' => current_time('mysql', 1)
    ));

    // Explicitly regenerate CSS file for this post
    $css_file = \Elementor\Core\Files\CSS\Post::create(21);
    $css_file->update();

    echo "✅ SUCCESS! Elementor CSS regenerated.\n\n";
    echo "📋 Details:\n";
    echo "   - Cache cleared: YES\n";
    echo "   - Page ID: 21 (Homepage)\n";
    echo "   - CSS file regenerated: YES\n";
    echo "   - Timestamp: " . current_time('Y-m-d H:i:s') . "\n\n";
    echo "🌐 Visit: http://svetlinkielementor.local\n";
    echo "   Changes should now be visible!\n\n";

} catch (Exception $e) {
    echo "❌ ERROR: " . $e->getMessage() . "\n";
    exit(1);
}
?>
