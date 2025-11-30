<?php
/**
 * FAQ Page Importer (ID: 29)
 *
 * Access this file via: http://svetlinkielementor.local/import-faq-page.php
 */

// Load WordPress
require_once __DIR__ . '/wp-load.php';

// Security check - simple key or logged-in admin
$auth_key = $_GET['key'] ?? '';
$is_authorized = ($auth_key === 'import_faq_29_temp') || (is_user_logged_in() && current_user_can('administrator'));

if (!$is_authorized) {
    die('Access denied. Use ?key=import_faq_29_temp or log in as administrator.');
}

// Page configuration
$page_id = 29;
$json_file = dirname(dirname(__DIR__)) . '/scripts/working/faq-page-data.json';

echo '<!DOCTYPE html>
<html>
<head>
    <title>FAQ Page Importer</title>
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
    <h1>FAQ Page Importer</h1>';

// Check if file exists
if (!file_exists($json_file)) {
    echo '<div class="error">Error: JSON file not found: ' . htmlspecialchars($json_file) . '</div>';
    exit;
}

// Read and decode JSON
$json_content = file_get_contents($json_file);
$elementor_data = json_decode($json_content, true);

if (!$elementor_data || !is_array($elementor_data)) {
    echo '<div class="error">Error: Invalid JSON data</div>';
    exit;
}

echo '<div class="info">JSON file loaded: ' . count($elementor_data) . ' sections found</div>';

// Update Elementor data
$json_string = wp_slash(wp_json_encode($elementor_data));
update_post_meta($page_id, '_elementor_data', $json_string);
update_post_meta($page_id, '_elementor_edit_mode', 'builder');
update_post_meta($page_id, '_elementor_version', '3.0.0');

// Clear Elementor cache
delete_post_meta($page_id, '_elementor_css');

// Force update post to trigger regeneration
wp_update_post(array('ID' => $page_id));

// Clear Elementor plugin cache if available
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
}

echo '<div class="success">SUCCESS! FAQ page imported successfully</div>';
echo '<div class="info">Page ID: ' . $page_id . '</div>';
echo '<div class="info">Sections imported: ' . count($elementor_data) . '</div>';
echo '<ul>';
echo '<li>Hero Section - "Често задавани въпроси"</li>';
echo '<li>FAQ Accordion - 10 Q&A pairs</li>';
echo '<li>CTA Section - Contact link</li>';
echo '</ul>';

echo '<hr>';
echo '<h2>Next Steps:</h2>';
echo '<div class="info"><a href="/faq/" target="_blank">View FAQ Page →</a></div>';
echo '<div class="info"><a href="/wp-admin/post.php?post=' . $page_id . '&action=elementor" target="_blank">Edit in Elementor →</a></div>';

echo '</body></html>';
