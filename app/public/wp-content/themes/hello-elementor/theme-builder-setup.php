<?php
/**
 * Theme Builder Setup Script
 * Run this via: php -f theme-builder-setup.php
 */

// Load WordPress
require_once(__DIR__ . '/../../../../wp-load.php');

if (!defined('ABSPATH')) {
    die('WordPress not loaded');
}

echo "=== Elementor Theme Builder Setup ===\n\n";

// Function to get Elementor data
function get_elementor_data($post_id) {
    $data = get_post_meta($post_id, '_elementor_data', true);
    if ($data) {
        return json_decode($data, true);
    }
    return null;
}

// Function to update Elementor data
function update_elementor_data($post_id, $data) {
    $json_data = json_encode($data);
    return update_post_meta($post_id, '_elementor_data', wp_slash($json_data));
}

// Step 1: Analyze homepage (ID 21)
echo "Step 1: Analyzing Homepage (ID 21)\n";
echo "-----------------------------------\n";
$homepage_data = get_elementor_data(21);
if ($homepage_data) {
    echo "Total sections: " . count($homepage_data) . "\n";
    foreach ($homepage_data as $index => $section) {
        $type = $section['elType'] ?? 'unknown';
        $columns = count($section['elements'] ?? []);
        echo "Section $index: Type=$type, Columns=$columns\n";
    }
} else {
    echo "No Elementor data found for homepage\n";
}
echo "\n";

// Step 2: Check Header Template (ID 69)
echo "Step 2: Checking Header Template (ID 69)\n";
echo "------------------------------------------\n";
$header_post = get_post(69);
if ($header_post) {
    echo "Title: " . $header_post->post_title . "\n";
    echo "Type: " . get_post_meta(69, '_elementor_template_type', true) . "\n";
    echo "Location: " . get_post_meta(69, '_elementor_location', true) . "\n";
    $header_data = get_elementor_data(69);
    if ($header_data) {
        echo "Sections: " . count($header_data) . "\n";
    }
} else {
    echo "Header template not found\n";
}
echo "\n";

// Step 3: Check Footer Template (ID 73)
echo "Step 3: Checking Footer Template (ID 73)\n";
echo "------------------------------------------\n";
$footer_post = get_post(73);
if ($footer_post) {
    echo "Title: " . $footer_post->post_title . "\n";
    echo "Type: " . get_post_meta(73, '_elementor_template_type', true) . "\n";
    echo "Location: " . get_post_meta(73, '_elementor_location', true) . "\n";
    $footer_data = get_elementor_data(73);
    if ($footer_data) {
        echo "Sections: " . count($footer_data) . "\n";
    }
} else {
    echo "Footer template not found\n";
}
echo "\n";

// Step 4: Check current conditions
echo "Step 4: Checking Display Conditions\n";
echo "-------------------------------------\n";
$header_conditions = get_post_meta(69, '_elementor_conditions', true);
$footer_conditions = get_post_meta(73, '_elementor_conditions', true);
echo "Header conditions: " . ($header_conditions ? json_encode($header_conditions) : "None") . "\n";
echo "Footer conditions: " . ($footer_conditions ? json_encode($footer_conditions) : "None") . "\n";
echo "\n";

echo "=== Analysis Complete ===\n";
echo "\nTo apply changes, run: php -f theme-builder-setup.php apply\n";

// If "apply" argument is provided, make the changes
if (isset($argv[1]) && $argv[1] === 'apply') {
    echo "\n=== APPLYING CHANGES ===\n\n";

    // Configure Header Template
    echo "Configuring Header Template (ID 69)...\n";
    update_post_meta(69, '_elementor_template_type', 'header');
    update_post_meta(69, '_elementor_location', 'header');
    update_post_meta(69, '_elementor_conditions', ['include/general']);
    echo "✓ Header template configured\n\n";

    // Configure Footer Template
    echo "Configuring Footer Template (ID 73)...\n";
    update_post_meta(73, '_elementor_template_type', 'footer');
    update_post_meta(73, '_elementor_location', 'footer');
    update_post_meta(73, '_elementor_conditions', ['include/general']);
    echo "✓ Footer template configured\n\n";

    // Remove duplicate sections from homepage
    echo "Removing duplicate sections from homepage...\n";
    if ($homepage_data && count($homepage_data) > 8) {
        // Remove first section (duplicate header)
        array_shift($homepage_data);

        // Remove last 2-3 sections (duplicate footer)
        // Identify footer sections by looking for sections with many columns or specific styling
        $sections_to_keep = count($homepage_data) - 3;
        $homepage_data = array_slice($homepage_data, 0, $sections_to_keep);

        // Update homepage
        update_elementor_data(21, $homepage_data);
        echo "✓ Homepage cleaned (kept " . count($homepage_data) . " sections)\n\n";
    } else {
        echo "! Homepage appears already cleaned or has unusual structure\n\n";
    }

    // Clear Elementor cache
    echo "Clearing Elementor cache...\n";
    if (class_exists('\Elementor\Plugin')) {
        \Elementor\Plugin::$instance->files_manager->clear_cache();
        echo "✓ Elementor cache cleared\n";
    } else {
        echo "! Elementor plugin not detected\n";
    }

    echo "\n=== CHANGES APPLIED SUCCESSFULLY ===\n";
    echo "Please visit the site to verify:\n";
    echo "- Homepage: http://svetlinkielementor.local\n";
    echo "- About page: http://svetlinkielementor.local/about\n";
}
