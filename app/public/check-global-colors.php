<?php
/**
 * Check and display current Global Colors configuration
 */

require_once(__DIR__ . '/wp-load.php');

echo "<!DOCTYPE html><html><head><title>Global Colors Check</title><style>
body { font-family: monospace; padding: 20px; }
.color-box { width: 50px; height: 50px; display: inline-block; margin-right: 10px; border: 2px solid #ccc; vertical-align: middle; }
table { border-collapse: collapse; margin: 20px 0; }
td, th { padding: 10px; border: 1px solid #ccc; text-align: left; }
</style></head><body>";
echo "<h1>Global Colors Configuration</h1>";

// Get Elementor kit settings (where Global Colors are stored)
$kit_id = get_option('elementor_active_kit');
echo "<p><strong>Active Kit ID:</strong> $kit_id</p>";

if ($kit_id) {
    // Get custom colors
    $custom_colors = get_post_meta($kit_id, '_elementor_page_settings', true);

    if (isset($custom_colors['custom_colors'])) {
        echo "<h2>Custom Colors (Available in Color Picker)</h2>";
        echo "<table>";
        echo "<tr><th>Color</th><th>ID</th><th>Title</th><th>Hex Value</th></tr>";
        foreach ($custom_colors['custom_colors'] as $color) {
            $color_value = isset($color['color']) ? $color['color'] : '#000000';
            $color_id = isset($color['_id']) ? $color['_id'] : 'N/A';
            $color_title = isset($color['title']) ? $color['title'] : 'Untitled';

            echo "<tr>";
            echo "<td><div class='color-box' style='background-color: $color_value;'></div></td>";
            echo "<td>$color_id</td>";
            echo "<td>$color_title</td>";
            echo "<td>$color_value</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "<p style='color: orange;'>⚠️ No Custom Colors defined yet!</p>";
        echo "<p><strong>To add Custom Colors:</strong></p>";
        echo "<ol>";
        echo "<li>Edit any page with Elementor</li>";
        echo "<li>Click hamburger menu (☰) in top-left</li>";
        echo "<li>Go to: Site Settings > Global Colors</li>";
        echo "<li>Under 'Custom Colors', click '+ Add Color'</li>";
        echo "<li>Set: Yellow (#FABA29), Coral (#FF8C7A), Teal (#4F9F8B)</li>";
        echo "</ol>";
    }

    // Get system colors (Primary, Secondary, Text, Accent)
    if (isset($custom_colors['system_colors'])) {
        echo "<h2>System Colors (Global Color Variables)</h2>";
        echo "<table>";
        echo "<tr><th>Color</th><th>ID</th><th>Title</th><th>Hex Value</th></tr>";
        foreach ($custom_colors['system_colors'] as $color) {
            $color_value = isset($color['color']) ? $color['color'] : '#000000';
            $color_id = isset($color['_id']) ? $color['_id'] : 'N/A';
            $color_title = isset($color['title']) ? $color['title'] : 'Untitled';

            echo "<tr>";
            echo "<td><div class='color-box' style='background-color: $color_value;'></div></td>";
            echo "<td>$color_id</td>";
            echo "<td>$color_title</td>";
            echo "<td>$color_value</td>";
            echo "</tr>";
        }
        echo "</table>";
    }
}

echo "<h2>How to Use These Colors in Widgets:</h2>";
echo "<ol>";
echo "<li><strong>System Colors:</strong> Use <code>var(--e-global-color-primary)</code> in JSON</li>";
echo "<li><strong>Custom Colors:</strong> Reference by ID in color picker UI (not available via REST API)</li>";
echo "<li><strong>For icon-box:</strong> May need to use direct hex values (#FABA29) instead of variables</li>";
echo "</ol>";

echo "</body></html>";
?>
