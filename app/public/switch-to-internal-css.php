<?php
require_once(__DIR__ . '/wp-load.php');

echo "Switching CSS Print Method to INTERNAL...\n";

// Switch to internal embedding
update_option('elementor_css_print_method', 'internal');

echo "✓ CSS Print Method set to: internal\n\n";

// Now force save
$post_id = 21;
$document = \Elementor\Plugin::$instance->documents->get($post_id);
$data = $document->get_elements_data();
$document->save($data);

echo "✓ Page saved with internal CSS\n";

// Clear caches
\Elementor\Plugin::$instance->files_manager->clear_cache();
wp_cache_flush();

echo "✓ Caches cleared\n\n";
echo "🌐 Visit: http://svetlinkielementor.local/home\n";
echo "🔄 Hard refresh: Ctrl+Shift+R\n";
?>
