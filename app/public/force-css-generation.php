<?php
/**
 * Force CSS Generation - Complete Rebuild
 */

require_once(__DIR__ . '/wp-load.php');

if (!did_action('elementor/loaded')) {
    die('ERROR: Elementor not loaded!');
}

$post_id = 21;

echo "🔄 Forcing CSS generation for page {$post_id}...\n\n";

// Step 1: Get the CSS file instance
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);

// Step 2: Delete old CSS completely
$css_file->delete();
echo "✓ Old CSS deleted\n";

// Step 3: Force regeneration
$css_file->update();
echo "✓ CSS regenerated\n";

// Step 4: Manually trigger enqueue (forces creation)
$css_file->enqueue();
echo "✓ CSS enqueued\n";

// Step 5: Check if file was created
$upload_dir = wp_upload_dir();
$css_path = $upload_dir['basedir'] . '/elementor/css/post-21.css';
if (file_exists($css_path)) {
    echo "✅ CSS FILE CREATED!\n";
    echo "   Path: " . $css_path . "\n";
    echo "   Size: " . filesize($css_path) . " bytes\n";
    echo "   Modified: " . date('Y-m-d H:i:s', filemtime($css_path)) . "\n";
} else {
    echo "⚠️  CSS file still doesn't exist - trying alternative method...\n\n";

    // Alternative: Change CSS method temporarily
    update_option('elementor_css_print_method', 'external');
    echo "✓ Switched to external CSS method\n";

    $css_file->delete();
    $css_file->update();

    if (file_exists($css_path)) {
        echo "✅ CSS FILE CREATED (external method)!\n";
        echo "   Keeping external CSS method active\n";
    } else {
        echo "❌ CSS file creation failed\n";
    }
}

// Step 6: Clear all caches
\Elementor\Plugin::$instance->files_manager->clear_cache();
wp_cache_flush();
echo "\n✓ All caches cleared\n";

echo "\n🌐 Visit: http://svetlinkielementor.local/home\n";
echo "🔄 Hard refresh: Ctrl+Shift+R\n";
?>
