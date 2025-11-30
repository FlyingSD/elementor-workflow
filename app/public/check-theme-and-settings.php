<?php
/**
 * Check Current Theme and Elementor Settings
 */

require_once(__DIR__ . '/wp-load.php');

echo "=== THEME CHECK ===\n";
$current_theme = wp_get_theme();
echo "Active Theme: " . $current_theme->get('Name') . "\n";
echo "Theme Version: " . $current_theme->get('Version') . "\n";
echo "Theme Folder: " . $current_theme->get_stylesheet() . "\n\n";

echo "=== ELEMENTOR SETTINGS ===\n";
if (did_action('elementor/loaded')) {
    $css_method = get_option('elementor_css_print_method');
    echo "CSS Print Method: " . ($css_method ?: 'external') . "\n";

    $global_colors = get_option('elementor_scheme_color-picker');
    echo "Global Colors Configured: " . (empty($global_colors) ? 'NO' : 'YES') . "\n";

    // Check if CSS file exists for page 21
    $upload_dir = wp_upload_dir();
    $css_path = $upload_dir['basedir'] . '/elementor/css/post-21.css';
    echo "CSS File Exists: " . (file_exists($css_path) ? 'YES' : 'NO') . "\n";
    if (file_exists($css_path)) {
        echo "CSS File Modified: " . date('Y-m-d H:i:s', filemtime($css_path)) . "\n";
        echo "CSS File Size: " . filesize($css_path) . " bytes\n";
    }
} else {
    echo "ERROR: Elementor not loaded!\n";
}

echo "\n=== PAGE 21 STATUS ===\n";
$post = get_post(21);
if ($post) {
    echo "Post Status: " . $post->post_status . "\n";
    echo "Post Modified: " . $post->post_modified . "\n";
    echo "Template: " . get_page_template_slug(21) . "\n";
    echo "Elementor Edit Mode: " . get_post_meta(21, '_elementor_edit_mode', true) . "\n";
}

echo "\n=== RECOMMENDATION ===\n";
if ($css_method !== 'internal') {
    echo "⚠️  CSS Print Method should be 'internal' for .local domains\n";
    echo "→ Go to Elementor > Settings > Advanced\n";
    echo "→ Change CSS Print Method to 'Internal Embedding'\n";
} else {
    echo "✅ CSS Print Method is correct (internal)\n";
}
?>
