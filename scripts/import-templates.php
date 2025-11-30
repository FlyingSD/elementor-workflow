<?php
/**
 * Import Elementor Templates - Header and Footer
 *
 * This script imports the header and footer JSON templates into the Elementor database
 * Run this via: wp eval-file scripts/import-templates.php
 */

// Template data
$header_json = file_get_contents(__DIR__ . '/templates/header-template.json');
$footer_json = file_get_contents(__DIR__ . '/templates/footer-template.json');

// Decode JSON
$header_data = json_decode($header_json, true);
$footer_data = json_decode($footer_json, true);

// Header Template ID
$header_id = 69;
$footer_id = 73;

/**
 * Import template data into Elementor post
 */
function import_elementor_template($post_id, $template_data) {
    if (!$template_data || !is_array($template_data)) {
        WP_CLI::error("Invalid template data for post ID: $post_id");
        return false;
    }

    // Update the _elementor_data post meta
    $json_data = wp_slash(wp_json_encode($template_data));
    update_post_meta($post_id, '_elementor_data', $json_data);

    // Mark as edit mode
    update_post_meta($post_id, '_elementor_edit_mode', 'builder');

    // Set Elementor version
    update_post_meta($post_id, '_elementor_version', '3.33.2');

    // Set page template to Elementor Canvas (optional for headers/footers)
    update_post_meta($post_id, '_wp_page_template', 'elementor_canvas');

    WP_CLI::success("Template imported successfully for post ID: $post_id");
    return true;
}

// Import Header
WP_CLI::log("Importing Header Template (ID: $header_id)...");
import_elementor_template($header_id, $header_data);

// Import Footer
WP_CLI::log("Importing Footer Template (ID: $footer_id)...");
import_elementor_template($footer_id, $footer_data);

WP_CLI::success("All templates imported successfully!");
WP_CLI::log("Header Editor URL: http://svetlinkielementor.local/wp-admin/post.php?post=$header_id&action=elementor");
WP_CLI::log("Footer Editor URL: http://svetlinkielementor.local/wp-admin/post.php?post=$footer_id&action=elementor");
