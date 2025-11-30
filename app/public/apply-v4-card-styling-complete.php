<?php
/**
 * Apply Complete V4 Card Styling
 *
 * Based on design-mockup-v4.html:
 * - Icon colors with correct property names (primary_color, secondary_color)
 * - Card styling: white background, borders, shadows, padding
 * - Top border accents matching icon colors
 * - Proper spacing and alignment
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Apply V4 Complete Styling</title>";
echo "<style>body{font-family:monospace;padding:20px;background:#f5f5f5;}.success{color:green;font-weight:bold;}</style>";
echo "</head><body>";
echo "<h1>Applying Complete V4 Card Styling</h1>";

$page_id = 21;
$elementor_data = get_post_meta($page_id, '_elementor_data', true);
$data = json_decode($elementor_data, true);

// Complete widget configurations based on V4 HTML
$widget_configs = [
    // Benefits section
    'benefits006' => [
        'icon_bg' => '#FABA29',  // Yellow
        'icon_color' => '#FFFFFF',
        'border_color' => '#FABA29',
        'icon_size' => 38
    ],
    'benefits008' => [
        'icon_bg' => '#FF8C7A',  // Coral
        'icon_color' => '#FFFFFF',
        'border_color' => '#FF8C7A',
        'icon_size' => 38
    ],
    'benefits010' => [
        'icon_bg' => '#4F9F8B',  // Teal
        'icon_color' => '#FFFFFF',
        'border_color' => '#4F9F8B',
        'icon_size' => 38
    ],
    // Programs section
    'programs006' => [
        'icon_bg' => '#FABA29',  // Yellow
        'icon_color' => '#FFFFFF',
        'border_color' => '#FABA29',
        'icon_size' => 38
    ],
    'programs008' => [
        'icon_bg' => '#FF8C7A',  // Coral
        'icon_color' => '#FFFFFF',
        'border_color' => '#FF8C7A',
        'icon_size' => 38
    ],
    'programs010' => [
        'icon_bg' => '#4F9F8B',  // Teal
        'icon_color' => '#FFFFFF',
        'border_color' => '#4F9F8B',
        'icon_size' => 38
    ],
];

$updated_count = 0;

function apply_v4_styling(&$elements, $widget_configs, &$updated_count) {
    foreach ($elements as &$element) {
        if (isset($element['widgetType']) && $element['widgetType'] === 'icon-box' &&
            isset($element['id']) && isset($widget_configs[$element['id']])) {

            $widget_id = $element['id'];
            $config = $widget_configs[$widget_id];

            if (!isset($element['settings'])) {
                $element['settings'] = [];
            }

            // === ICON COLORS (Correct Property Names) ===
            $element['settings']['primary_color'] = $config['icon_bg'];  // Background circle
            $element['settings']['secondary_color'] = $config['icon_color'];  // Icon itself
            $element['settings']['hover_primary_color'] = $config['icon_bg'];  // Hover background
            $element['settings']['hover_secondary_color'] = $config['icon_color'];  // Hover icon

            // === ICON SIZE & SPACING ===
            $element['settings']['icon_size'] = ['unit' => 'px', 'size' => $config['icon_size']];
            $element['settings']['icon_space'] = ['unit' => 'px', 'size' => 22];  // From HTML

            // === VIEW SETTINGS ===
            $element['settings']['view'] = 'stacked';
            $element['settings']['shape'] = 'circle';

            // === CARD BACKGROUND ===
            $element['settings']['background_background'] = 'classic';
            $element['settings']['background_color'] = '#FFFFFF';  // White background

            // === CARD BORDER (Top accent) ===
            $element['settings']['border_border'] = 'solid';
            $element['settings']['border_width'] = [
                'unit' => 'px',
                'top' => '5',  // 5px top border accent
                'right' => '0',
                'bottom' => '0',
                'left' => '0',
                'isLinked' => false
            ];
            $element['settings']['border_color'] = $config['border_color'];
            $element['settings']['border_radius'] = [
                'unit' => 'px',
                'top' => '20',
                'right' => '20',
                'bottom' => '20',
                'left' => '20',
                'isLinked' => true
            ];

            // === CARD SHADOW (From HTML: 0 10px 35px rgba(0, 0, 0, 0.1)) ===
            $element['settings']['_box_shadow_box_shadow'] = [
                'horizontal' => 0,
                'vertical' => 10,
                'blur' => 35,
                'spread' => 0,
                'color' => 'rgba(0, 0, 0, 0.1)'
            ];

            // === CARD PADDING (From HTML: 45px 35px) ===
            $element['settings']['padding'] = [
                'unit' => 'px',
                'top' => '45',
                'right' => '35',
                'bottom' => '45',
                'left' => '35',
                'isLinked' => false
            ];

            // === TEXT COLORS ===
            $element['settings']['title_color'] = 'var(--e-global-color-text)';  // Dark teal
            $element['settings']['description_color'] = '#5a6c6d';  // From HTML

            // === TEXT ALIGNMENT ===
            $element['settings']['title_text_align'] = 'center';
            $element['settings']['description_text_align'] = 'center';

            // Remove old incorrect properties
            unset($element['settings']['icon_primary_color']);
            unset($element['settings']['icon_secondary_color']);
            unset($element['settings']['icon_color']);

            echo "<p class='success'>✅ Updated widget $widget_id with COMPLETE V4 styling</p>";
            $updated_count++;
        }

        if (isset($element['elements']) && is_array($element['elements'])) {
            apply_v4_styling($element['elements'], $widget_configs, $updated_count);
        }
    }
}

apply_v4_styling($data, $widget_configs, $updated_count);

echo "<p><strong>Total widgets updated: $updated_count</strong></p>";

// Save updated data
$json_data = wp_slash(json_encode($data));
update_post_meta($page_id, '_elementor_data', $json_data);
echo "<p class='success'>✅ Page data saved with COMPLETE V4 styling!</p>";

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
echo "<p><strong>What Was Applied:</strong></p>";
echo "<ul>";
echo "<li>✅ Icon colors (primary_color + secondary_color)</li>";
echo "<li>✅ Icon size: 38px with 22px spacing</li>";
echo "<li>✅ Stacked circular view</li>";
echo "<li>✅ White card backgrounds</li>";
echo "<li>✅ Top border accent (5px, colored)</li>";
echo "<li>✅ Border radius: 20px</li>";
echo "<li>✅ Box shadow: 0 10px 35px rgba(0, 0, 0, 0.1)</li>";
echo "<li>✅ Padding: 45px 35px</li>";
echo "<li>✅ Text colors and alignment</li>";
echo "</ul>";
echo "<h3>Test Now:</h3>";
echo "<p><a href='http://svetlinkielementor.local' target='_blank'>Visit Homepage</a> - Cards should now match V4 HTML!</p>";
echo "</body></html>";
?>
