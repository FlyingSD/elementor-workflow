<?php
/**
 * Elementor Template Importer
 *
 * Access this file via: http://svetlinkielementor.local/import-elementor-templates.php
 * This will import the header and footer templates from JSON files
 */

// Load WordPress
require_once __DIR__ . '/wp-load.php';

// Security check - only allow logged-in administrators
if (!is_user_logged_in() || !current_user_can('administrator')) {
    die('Access denied. You must be logged in as an administrator.');
}

// Template configuration
$header_id = 69;
$footer_id = 73;
// Path: from /app/public/ go up to site root, then to scripts/templates/
$templates_dir = dirname(dirname(__DIR__)) . '/scripts/templates/';

echo '<!DOCTYPE html>
<html>
<head>
    <title>Elementor Template Importer</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        .success { color: green; padding: 10px; background: #e7f7e7; border-left: 4px solid green; margin: 10px 0; }
        .error { color: red; padding: 10px; background: #ffeaea; border-left: 4px solid red; margin: 10px 0; }
        .info { color: blue; padding: 10px; background: #e7f3ff; border-left: 4px solid blue; margin: 10px 0; }
        h1 { color: #333; }
        a { color: #0073aa; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Elementor Template Importer</h1>';

/**
 * Import template function
 */
function import_template($post_id, $json_file, $template_name) {
    // Check if file exists
    if (!file_exists($json_file)) {
        echo '<div class="error">❌ Error: Template file not found: ' . htmlspecialchars($json_file) . '</div>';
        return false;
    }

    // Read and decode JSON
    $json_content = file_get_contents($json_file);
    $template_data = json_decode($json_content, true);

    if (!$template_data || !is_array($template_data)) {
        echo '<div class="error">❌ Error: Invalid JSON in ' . htmlspecialchars(basename($json_file)) . '</div>';
        return false;
    }

    // Update Elementor data
    $json_string = wp_slash(wp_json_encode($template_data));
    update_post_meta($post_id, '_elementor_data', $json_string);
    update_post_meta($post_id, '_elementor_edit_mode', 'builder');
    update_post_meta($post_id, '_elementor_version', '3.33.2');
    update_post_meta($post_id, '_elementor_template_type', 'header');

    // Clear Elementor cache
    delete_post_meta($post_id, '_elementor_css');

    // Force update post to trigger regeneration
    wp_update_post(array('ID' => $post_id));

    echo '<div class="success">✅ ' . htmlspecialchars($template_name) . ' imported successfully!</div>';
    echo '<div class="info">📝 Post ID: ' . $post_id . '</div>';
    echo '<div class="info">🔗 <a href="/wp-admin/post.php?post=' . $post_id . '&action=elementor" target="_blank">Edit in Elementor →</a></div>';

    return true;
}

// Import Header
echo '<h2>Importing Header Template...</h2>';
$header_file = $templates_dir . 'header-template.json';
import_template($header_id, $header_file, 'Header Template');

// Import Footer
echo '<h2>Importing Footer Template...</h2>';
$footer_file = $templates_dir . 'footer-template.json';
import_template($footer_id, $footer_file, 'Footer Template');

echo '<hr>';
echo '<h2>Import Complete!</h2>';
echo '<div class="success">✅ All templates have been imported successfully.</div>';
echo '<div class="info">🔗 <a href="/wp-admin/edit.php?post_type=elementor-hf">View All Templates →</a></div>';

echo '</body></html>';
