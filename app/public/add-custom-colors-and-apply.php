<?php
/**
 * Add Custom Colors to Elementor Kit and Apply to Icon-Box Widgets
 *
 * This script:
 * 1. Adds 3 Custom Colors to Elementor Kit (Yellow, Coral, Teal)
 * 2. Updates icon-box widgets with correct background colors
 * 3. Clears Elementor cache
 */

require_once(__DIR__ . '/wp-load.php');

// Colors to add
$colors_to_add = [
    [
        '_id' => 'custom_yellow',
        'title' => 'Yellow',
        'color' => '#FABA29'
    ],
    [
        '_id' => 'custom_coral',
        'title' => 'Coral',
        'color' => '#FF8C7A'
    ],
    [
        '_id' => 'custom_teal',
        'title' => 'Teal',
        'color' => '#4F9F8B'
    ]
];

echo "<!DOCTYPE html><html><head><title>Add Custom Colors</title>";
echo "<style>body{font-family:monospace;padding:20px;background:#f5f5f5;}";
echo ".success{color:green;font-weight:bold;}.error{color:red;font-weight:bold;}</style>";
echo "</head><body>";
echo "<h1>Adding Custom Colors & Applying to Icons</h1>";

// Step 1: Get Elementor Kit ID
$kit_id = get_option('elementor_active_kit');
if (!$kit_id) {
    echo "<p class='error'>ERROR: No active Elementor kit found!</p>";
    exit;
}

echo "<p>Active Kit ID: <strong>$kit_id</strong></p>";

// Step 2: Get current kit settings
$kit_settings = get_post_meta($kit_id, '_elementor_page_settings', true);
if (!is_array($kit_settings)) {
    $kit_settings = [];
}

echo "<h2>Step 1: Adding Custom Colors to Kit</h2>";

// Add custom_colors array if it doesn't exist
if (!isset($kit_settings['custom_colors']) || !is_array($kit_settings['custom_colors'])) {
    $kit_settings['custom_colors'] = [];
}

// Check if colors already exist
$existing_colors = array_column($kit_settings['custom_colors'], 'title');
echo "<p>Existing Custom Colors: " . (empty($existing_colors) ? 'None' : implode(', ', $existing_colors)) . "</p>";

// Add new colors
foreach ($colors_to_add as $color) {
    // Check if color already exists
    $exists = false;
    foreach ($kit_settings['custom_colors'] as $existing) {
        if ($existing['title'] === $color['title']) {
            $exists = true;
            echo "<p>⚠️ Color '{$color['title']}' already exists, skipping...</p>";
            break;
        }
    }

    if (!$exists) {
        $kit_settings['custom_colors'][] = $color;
        echo "<p class='success'>✅ Added Custom Color: {$color['title']} ({$color['color']})</p>";
    }
}

// Update kit settings
update_post_meta($kit_id, '_elementor_page_settings', $kit_settings);
echo "<p class='success'>✅ Kit settings updated!</p>";

// Step 3: Update icon-box widgets on homepage
echo "<h2>Step 2: Updating Icon-Box Widgets</h2>";

$page_id = 21;
$elementor_data = get_post_meta($page_id, '_elementor_data', true);

if (empty($elementor_data)) {
    echo "<p class='error'>ERROR: No Elementor data found on page $page_id</p>";
    exit;
}

// Decode JSON
$data = json_decode($elementor_data, true);
if (!$data) {
    echo "<p class='error'>ERROR: Failed to decode Elementor data</p>";
    exit;
}

// Icon color mapping
$icon_colors = [
    // Benefits section
    'benefits006' => '#FABA29',  // Brain - Yellow
    'benefits008' => '#FF8C7A',  // Lightbulb - Coral
    'benefits010' => '#4F9F8B',  // Star - Teal
    // Programs section
    'programs006' => '#FABA29',  // Book - Yellow
    'programs008' => '#FF8C7A',  // Gift - Coral
    'programs010' => '#4F9F8B',  // Question - Teal
];

$updated_count = 0;

// Function to recursively update widgets
function update_icon_widgets(&$elements, $icon_colors, &$updated_count) {
    foreach ($elements as &$element) {
        // Check if this is an icon-box widget we need to update
        if (isset($element['widgetType']) && $element['widgetType'] === 'icon-box' &&
            isset($element['id']) && isset($icon_colors[$element['id']])) {

            $widget_id = $element['id'];
            $color = $icon_colors[$widget_id];

            // Update widget settings
            if (!isset($element['settings'])) {
                $element['settings'] = [];
            }

            // Set icon colors - try multiple properties
            $element['settings']['icon_color'] = $color;
            $element['settings']['icon_secondary_color'] = $color;
            $element['settings']['hover_secondary_color'] = $color;
            $element['settings']['icon_primary_color'] = '#FFFFFF';
            $element['settings']['hover_primary_color'] = '#FFFFFF';

            // Ensure stacked view
            $element['settings']['view'] = 'stacked';
            $element['settings']['shape'] = 'circle';

            echo "<p class='success'>✅ Updated widget $widget_id with color $color</p>";
            $updated_count++;
        }

        // Recursively update child elements
        if (isset($element['elements']) && is_array($element['elements'])) {
            update_icon_widgets($element['elements'], $icon_colors, $updated_count);
        }
    }
}

// Update widgets
update_icon_widgets($data, $icon_colors, $updated_count);

echo "<p><strong>Total widgets updated: $updated_count</strong></p>";

// Save updated data
$json_data = wp_slash(json_encode($data));
update_post_meta($page_id, '_elementor_data', $json_data);
update_post_meta($page_id, '_elementor_edit_mode', 'builder');

echo "<p class='success'>✅ Page data updated!</p>";

// Step 4: Clear Elementor cache
echo "<h2>Step 3: Clearing Elementor Cache</h2>";

if (did_action('elementor/loaded')) {
    $elementor = \Elementor\Plugin::instance();

    // Clear all cache
    $elementor->files_manager->clear_cache();
    echo "<p class='success'>✅ Elementor files cache cleared</p>";

    // Regenerate CSS for page
    $css_file = \Elementor\Core\Files\CSS\Post::create($page_id);
    $css_file->delete();
    $css_file->update();
    echo "<p class='success'>✅ Page CSS regenerated</p>";
}

// Clear WordPress cache
wp_cache_flush();
echo "<p class='success'>✅ WordPress cache cleared</p>";

// Clear transients
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");
echo "<p class='success'>✅ Transients cleared</p>";

// Update post timestamp
wp_update_post([
    'ID' => $page_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
]);
echo "<p class='success'>✅ Post timestamp updated</p>";

echo "<hr>";
echo "<h2>✅ COMPLETE!</h2>";
echo "<p><strong>What was done:</strong></p>";
echo "<ul>";
echo "<li>Added 3 Custom Colors to Elementor Kit (Yellow, Coral, Teal)</li>";
echo "<li>Updated $updated_count icon-box widgets with colors</li>";
echo "<li>Cleared all Elementor and WordPress caches</li>";
echo "<li>Regenerated CSS for page $page_id</li>";
echo "</ul>";

echo "<h3>Next Steps:</h3>";
echo "<ol>";
echo "<li>Visit homepage: <a href='http://svetlinkielementor.local' target='_blank'>http://svetlinkielementor.local</a></li>";
echo "<li>Hard refresh (Ctrl+Shift+R)</li>";
echo "<li>Check icon colors</li>";
echo "<li>If still gray, try editing one widget in Elementor editor and apply Custom Color via UI color picker</li>";
echo "</ol>";

echo "<h3>View Custom Colors:</h3>";
echo "<p><a href='check-global-colors.php' target='_blank'>Check Global Colors Configuration</a></p>";

echo "</body></html>";
?>
