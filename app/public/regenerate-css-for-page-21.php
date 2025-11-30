<?php
/**
 * Force CSS Regeneration for Page 21 (Homepage)
 * Fixes Issue #3 - CSS not regenerating after REST API updates
 */

// Load WordPress
require_once(__DIR__ . '/wp-load.php');

// Check if Elementor is active
if (!did_action('elementor/loaded')) {
    die('ERROR: Elementor is not active!');
}

$post_id = 21; // Homepage

echo "Starting CSS regeneration for page {$post_id}...\n\n";

// Method 1: Delete CSS file (forces regeneration on next load)
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css_file->delete();
echo "✓ CSS file deleted\n";

// Method 2: Force regeneration immediately
$css_file->update();
echo "✓ CSS file regenerated\n";

// Method 3: Clear Elementor cache
\Elementor\Plugin::$instance->files_manager->clear_cache();
echo "✓ Elementor cache cleared\n";

// Method 4: Clear WordPress transients
delete_transient('elementor_activation_redirect');
delete_transient('elementor_activation_redirect_count');
echo "✓ WordPress transients cleared\n";

echo "\n✅ CSS REGENERATION COMPLETE!\n";
echo "→ Visit http://svetlinkielementor.local/home to see changes\n";
echo "→ Hard refresh browser: Ctrl+Shift+R\n";
?>
