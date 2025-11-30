<?php
/**
 * Force Elementor Save - Simulates clicking Update/Publish button
 */

require_once(__DIR__ . '/wp-load.php');

if (!did_action('elementor/loaded')) {
    die('ERROR: Elementor not loaded!');
}

$post_id = 21;

echo "🔄 Forcing Elementor save for page {$post_id}...\n\n";

// Get the document instance
$document = \Elementor\Plugin::$instance->documents->get($post_id);

if (!$document) {
    die("❌ ERROR: Could not get document\n");
}

echo "✓ Document loaded\n";

// Get current data
$data = $document->get_elements_data();

if (empty($data)) {
    die("❌ ERROR: No Elementor data found\n");
}

echo "✓ Elementor data found (" . count($data) . " elements)\n";

// SAVE (this is what Update/Publish button does)
$document->save($data);

echo "✓ Document saved (CSS auto-generated)\n";

// Also regenerate CSS manually
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css_file->update();

echo "✓ CSS regenerated\n";

// Clear caches
\Elementor\Plugin::$instance->files_manager->clear_cache();
wp_cache_flush();

echo "✓ All caches cleared\n";

// Verify
$upload_dir = wp_upload_dir();
$css_path = $upload_dir['basedir'] . '/elementor/css/post-21.css';

if (file_exists($css_path)) {
    echo "\n✅ SUCCESS! CSS file exists\n";
    echo "   Size: " . filesize($css_path) . " bytes\n";
    echo "   Modified: " . date('Y-m-d H:i:s', filemtime($css_path)) . "\n";
} else {
    echo "\n⚠️  CSS file not found\n";
}

echo "\n🌐 Visit: http://svetlinkielementor.local/home\n";
echo "🔄 Hard refresh: Ctrl+Shift+R\n";
?>
