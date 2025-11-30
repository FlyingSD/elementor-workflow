<?php
require_once(__DIR__ . '/wp-load.php');

$post_id = 21;
echo "🔥 NUCLEAR CSS FIX for page {$post_id}...\n\n";

// Step 1: Force post modification update
wp_update_post(array(
    'ID' => $post_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
));
echo "✓ Post modification time updated\n";

// Step 2: Delete ALL Elementor CSS
global $wpdb;
$wpdb->query("DELETE FROM {$wpdb->postmeta} WHERE meta_key LIKE '_elementor_css%'");
echo "✓ All Elementor CSS meta deleted\n";

// Step 3: Clear ALL caches
wp_cache_flush();
if (function_exists('wp_cache_delete')) {
    wp_cache_delete($post_id, 'posts');
    wp_cache_delete($post_id, 'post_meta');
}
echo "✓ WordPress cache flushed\n";

// Step 4: Elementor regeneration
if (did_action('elementor/loaded')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
    
    $document = \Elementor\Plugin::$instance->documents->get($post_id);
    $data = $document->get_elements_data();
    $document->save($data);
    
    echo "✓ Elementor document saved\n";
}

// Step 5: Force CSS file creation
$css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
$css_file->delete();
$css_file->update();
$css_file->enqueue();
echo "✓ CSS file regenerated\n";

echo "\n✅ DONE! Now:\n";
echo "1. Open NEW incognito/private window\n";
echo "2. Visit: http://svetlinkielementor.local/home\n";
echo "3. Check if borders show\n";
?>
