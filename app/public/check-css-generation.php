<?php
/**
 * Check CSS Generation Status
 */

require_once(__DIR__ . '/wp-load.php');

$post_id = 21;

echo "=== CSS FILE CHECK ===\n";
$upload_dir = wp_upload_dir();
$css_path = $upload_dir['basedir'] . '/elementor/css/post-21.css';

if (file_exists($css_path)) {
    echo "✅ CSS file exists\n";
    echo "Path: " . $css_path . "\n";
    echo "Size: " . filesize($css_path) . " bytes\n";
    echo "Modified: " . date('Y-m-d H:i:s', filemtime($css_path)) . "\n\n";

    echo "=== CSS CONTENT (First 500 chars) ===\n";
    echo substr(file_get_contents($css_path), 0, 500) . "...\n\n";

    // Check if our specific classes are in the CSS
    $css_content = file_get_contents($css_path);
    $has_benefits = strpos($css_content, 'benefits') !== false;
    $has_box_shadow = strpos($css_content, 'box-shadow') !== false;
    $has_border = strpos($css_content, 'border') !== false;

    echo "=== CSS CONTENT CHECK ===\n";
    echo "Contains 'benefits': " . ($has_benefits ? "YES" : "NO") . "\n";
    echo "Contains 'box-shadow': " . ($has_box_shadow ? "YES" : "NO") . "\n";
    echo "Contains 'border': " . ($has_border ? "YES" : "NO") . "\n\n";
} else {
    echo "❌ CSS file does NOT exist\n";
    echo "Expected path: " . $css_path . "\n\n";
}

echo "=== ELEMENTOR SETTINGS ===\n";
$css_method = get_option('elementor_css_print_method');
echo "CSS Print Method: " . ($css_method ?: 'default') . "\n";
?>
