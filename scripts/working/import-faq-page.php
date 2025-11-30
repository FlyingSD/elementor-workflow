<?php
/**
 * Import FAQ Page Elementor Data (ID: 29)
 * Run via: wp eval-file scripts/working/import-faq-page.php
 */

$page_id = 29;

// Read the JSON file created by the Python script
$json_file = __DIR__ . '/faq-page-data.json';

if (!file_exists($json_file)) {
    WP_CLI::error("JSON file not found: $json_file");
    exit(1);
}

$json_content = file_get_contents($json_file);
$elementor_data = json_decode($json_content, true);

if (!$elementor_data || !is_array($elementor_data)) {
    WP_CLI::error("Invalid JSON data in file");
    exit(1);
}

WP_CLI::log("Importing FAQ page data to post ID: $page_id");
WP_CLI::log("Sections count: " . count($elementor_data));

// Update the _elementor_data post meta
$json_data = wp_slash(wp_json_encode($elementor_data));
update_post_meta($page_id, '_elementor_data', $json_data);

// Mark as edit mode
update_post_meta($page_id, '_elementor_edit_mode', 'builder');

// Set Elementor version
update_post_meta($page_id, '_elementor_version', '3.0.0');

// Clear Elementor cache
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
    WP_CLI::success("Elementor cache cleared");
}

WP_CLI::success("FAQ page imported successfully!");
WP_CLI::log("View page: http://svetlinkielementor.local/faq/");
WP_CLI::log("Edit page: http://svetlinkielementor.local/wp-admin/post.php?post=$page_id&action=elementor");
