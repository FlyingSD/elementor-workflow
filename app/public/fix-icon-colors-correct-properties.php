<?php
/**
 * Fix Icon-Box Colors with CORRECT Property Names
 *
 * Based on Elementor source code:
 * - primary_color = background color in stacked view
 * - secondary_color = icon color in stacked view
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Fix Icon Colors - Correct Properties</title>";
echo "<style>body{font-family:monospace;padding:20px;background:#f5f5f5;}.success{color:green;font-weight:bold;}</style>";
echo "</head><body>";
echo "<h1>Fixing Icon Colors with Correct Property Names</h1>";
echo "<p><strong>KEY DISCOVERY:</strong> The properties are <code>primary_color</code> and <code>secondary_color</code>, NOT <code>icon_primary_color</code>!</p>";

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

function update_icon_widgets_correct(&$elements, $icon_colors, &$updated_count) {
    foreach ($elements as &$element) {
        if (isset($element['widgetType']) && $element['widgetType'] === 'icon-box' &&
            isset($element['id']) && isset($icon_colors[$element['id']])) {

            $widget_id = $element['id'];
            $bg_color = $icon_colors[$widget_id];  // Background color
            $icon_color = '#FFFFFF';  // Icon itself (white)

            if (!isset($element['settings'])) {
                $element['settings'] = [];
            }

            // CORRECT PROPERTY NAMES (from Elementor source):
            // For stacked view, these control:
            // - primary_color = background-color of circle
            // - secondary_color = color of icon itself

            $element['settings']['primary_color'] = $bg_color;  // Background circle
            $element['settings']['secondary_color'] = $icon_color;  // Icon color (white)

            // Hover states
            $element['settings']['hover_primary_color'] = $bg_color;  // Background on hover
            $element['settings']['hover_secondary_color'] = $icon_color;  // Icon on hover

            // Remove old incorrect properties
            unset($element['settings']['icon_primary_color']);
            unset($element['settings']['icon_secondary_color']);
            unset($element['settings']['icon_color']);

            // Ensure stacked view
            $element['settings']['view'] = 'stacked';
            $element['settings']['shape'] = 'circle';

            echo "<p class='success'>✅ Updated widget $widget_id: primary_color=$bg_color, secondary_color=$icon_color</p>";
            $updated_count++;
        }

        if (isset($element['elements']) && is_array($element['elements'])) {
            update_icon_widgets_correct($element['elements'], $icon_colors, $updated_count);
        }
    }
}

update_icon_widgets_correct($data, $icon_colors, $updated_count);

echo "<p><strong>Total widgets updated: $updated_count</strong></p>";

// Save updated data
$json_data = wp_slash(json_encode($data));
update_post_meta($page_id, '_elementor_data', $json_data);
echo "<p class='success'>✅ Page data saved with CORRECT property names!</p>";

// Clear cache
if (did_action('elementor/loaded')) {
    $elementor = \Elementor\Plugin::instance();
    $elementor->files_manager->clear_cache();

    $css_file = \Elementor\Core\Files\CSS\Post::create($page_id);
    $css_file->delete();
    $css_file->update();
    echo "<p class='success'>✅ CSS regenerated</p>";
}

wp_cache_flush();
global $wpdb;
$wpdb->query("DELETE FROM $wpdb->options WHERE option_name LIKE '_transient_%'");

wp_update_post([
    'ID' => $page_id,
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => current_time('mysql', 1)
]);

echo "<p class='success'>✅ All caches cleared</p>";
echo "<hr>";
echo "<h2>✅ COMPLETE!</h2>";
echo "<p><strong>What Changed:</strong></p>";
echo "<ul>";
echo "<li>Used <code>primary_color</code> instead of <code>icon_primary_color</code></li>";
echo "<li>Used <code>secondary_color</code> instead of <code>icon_secondary_color</code></li>";
echo "<li>Removed incorrect property names</li>";
echo "</ul>";
echo "<h3>Test Now:</h3>";
echo "<p><a href='http://svetlinkielementor.local' target='_blank'>Visit Homepage</a> - Icons should now have colored backgrounds!</p>";
echo "</body></html>";
?>
