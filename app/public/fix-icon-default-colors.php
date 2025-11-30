<?php
/**
 * Fix Icon-Box Default State Colors
 *
 * Since hover colors work, let's try different property combinations
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Fix Icon Default Colors</title>";
echo "<style>body{font-family:monospace;padding:20px;background:#f5f5f5;}</style>";
echo "</head><body>";
echo "<h1>Fixing Icon Default State Colors</h1>";

$page_id = 21;
$elementor_data = get_post_meta($page_id, '_elementor_data', true);
$data = json_decode($elementor_data, true);

// Icon color mapping
$icon_colors = [
    'benefits006' => '#FABA29',  // Brain - Yellow
    'benefits008' => '#FF8C7A',  // Lightbulb - Coral
    'benefits010' => '#4F9F8B',  // Star - Teal
    'programs006' => '#FABA29',  // Book - Yellow
    'programs008' => '#FF8C7A',  // Gift - Coral
    'programs010' => '#4F9F8B',  // Question - Teal
];

$updated_count = 0;

function update_icon_widgets_v2(&$elements, $icon_colors, &$updated_count) {
    foreach ($elements as &$element) {
        if (isset($element['widgetType']) && $element['widgetType'] === 'icon-box' &&
            isset($element['id']) && isset($icon_colors[$element['id']])) {

            $widget_id = $element['id'];
            $color = $icon_colors[$widget_id];

            if (!isset($element['settings'])) {
                $element['settings'] = [];
            }

            // Try different property combinations
            // In Elementor stacked view:
            // - primary_color might control the background
            // - secondary_color might control the icon
            // Let's try swapping them

            $element['settings']['primary_color'] = $color;  // Background
            $element['settings']['secondary_color'] = '#FFFFFF';  // Icon itself

            // Also keep the old properties for backward compatibility
            $element['settings']['icon_color'] = $color;
            $element['settings']['icon_secondary_color'] = $color;
            $element['settings']['icon_primary_color'] = $color;

            // Keep hover working
            $element['settings']['hover_primary_color'] = $color;
            $element['settings']['hover_secondary_color'] = $color;

            // Ensure stacked view
            $element['settings']['view'] = 'stacked';
            $element['settings']['shape'] = 'circle';

            echo "<p>✅ Updated widget $widget_id with primary_color=$color</p>";
            $updated_count++;
        }

        if (isset($element['elements']) && is_array($element['elements'])) {
            update_icon_widgets_v2($element['elements'], $icon_colors, $updated_count);
        }
    }
}

update_icon_widgets_v2($data, $icon_colors, $updated_count);

echo "<p><strong>Total widgets updated: $updated_count</strong></p>";

// Save updated data
$json_data = wp_slash(json_encode($data));
update_post_meta($page_id, '_elementor_data', $json_data);

// Clear cache
if (did_action('elementor/loaded')) {
    $elementor = \Elementor\Plugin::instance();
    $elementor->files_manager->clear_cache();

    $css_file = \Elementor\Core\Files\CSS\Post::create($page_id);
    $css_file->delete();
    $css_file->update();
}

wp_cache_flush();
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");

wp_update_post([
    'ID' => $page_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
]);

echo "<p>✅ All caches cleared and CSS regenerated</p>";
echo "<h3>Test:</h3>";
echo "<p><a href='http://svetlinkielementor.local' target='_blank'>Visit Homepage</a> and check if default state colors now appear</p>";
echo "</body></html>";
?>
