<?php
/**
 * Fix Programs Section Cards - Apply proper styling and containment
 */

require_once(__DIR__ . '/wp-load.php');

$page_id = 21;
$data = get_post_meta($page_id, '_elementor_data', true);
$decoded = json_decode($data, true);

if (!$decoded) {
    die("ERROR: Could not decode Elementor data\n");
}

echo "Fixing Programs section cards...\n";

$programs_updated = false;

foreach ($decoded as $section_index => &$section) {
    if ($section['elType'] !== 'section') continue;

    // Look for "Нашите програми" heading
    $is_programs_section = false;
    foreach ($section['elements'] as $col) {
        foreach ($col['elements'] as $widget) {
            if ($widget['widgetType'] === 'heading' &&
                isset($widget['settings']['title']) &&
                strpos($widget['settings']['title'], 'програм') !== false) {
                $is_programs_section = true;
                echo "Found Programs section at index $section_index\n";
                break 2;
            }
        }
    }

    if (!$is_programs_section) continue;

    // Update section settings
    $decoded[$section_index]['settings']['background_background'] = 'classic';
    $decoded[$section_index]['settings']['background_color'] = '#FFFFFF';
    $decoded[$section_index]['settings']['padding'] = [
        'unit' => 'px',
        'top' => '80',
        'right' => '20',
        'bottom' => '80',
        'left' => '20'
    ];

    // Update section layout to contain cards better
    $decoded[$section_index]['settings']['gap'] = 'default';
    $decoded[$section_index]['settings']['column_gap'] = ['size' => 30, 'unit' => 'px'];

    $card_count = 0;
    foreach ($decoded[$section_index]['elements'] as $col_index => &$column) {
        if ($col_index === 0) {
            // First column is the title - ensure full width
            $column['settings']['_column_size'] = 100;
            continue;
        }

        $card_count++;
        echo "  Updating card $card_count...\n";

        // Set column width properly
        $column['settings']['_column_size'] = 33;
        $column['settings']['_inline_size'] = null; // Remove any custom width

        // Apply card styling
        $column['settings']['background_background'] = 'classic';
        $column['settings']['background_color'] = '#FFFFFF';

        // Top colored border
        $column['settings']['border_border'] = 'solid';
        $column['settings']['border_width'] = [
            'unit' => 'px',
            'top' => '5',
            'right' => '0',
            'bottom' => '0',
            'left' => '0',
            'isLinked' => false
        ];

        // Different border color per card
        if ($card_count === 1) {
            $column['settings']['border_color'] = '#FABA29'; // Yellow
        } elseif ($card_count === 2) {
            $column['settings']['border_color'] = '#FF8C7A'; // Coral
        } else {
            $column['settings']['border_color'] = '#46b19d'; // Teal
        }

        // Rounded corners
        $column['settings']['border_radius'] = [
            'unit' => 'px',
            'top' => '20',
            'right' => '20',
            'bottom' => '20',
            'left' => '20',
            'isLinked' => true
        ];

        // Padding
        $column['settings']['padding'] = [
            'unit' => 'px',
            'top' => '40',
            'right' => '30',
            'bottom' => '40',
            'left' => '30',
            'isLinked' => false
        ];

        // Box shadow
        $column['settings']['box_shadow_box_shadow_type'] = 'yes';
        $column['settings']['box_shadow_box_shadow'] = [
            'horizontal' => 0,
            'vertical' => 10,
            'blur' => 35,
            'spread' => 0,
            'color' => 'rgba(0, 0, 0, 0.08)'
        ];

        // Update button styling inside cards
        foreach ($column['elements'] as &$widget) {
            if ($widget['widgetType'] === 'button') {
                $widget['settings']['text'] = 'Прочети повече';
                $widget['settings']['button_text_color'] = '#1d3234'; // Dark teal text
                $widget['settings']['background_color'] = 'transparent';
                $widget['settings']['border_border'] = 'solid';
                $widget['settings']['border_width'] = [
                    'unit' => 'px',
                    'top' => '2',
                    'right' => '2',
                    'bottom' => '2',
                    'left' => '2',
                    'isLinked' => true
                ];
                $widget['settings']['border_color'] = '#FABA29'; // Yellow border
                $widget['settings']['border_radius'] = [
                    'unit' => 'px',
                    'top' => '12',
                    'right' => '12',
                    'bottom' => '12',
                    'left' => '12',
                    'isLinked' => true
                ];
                $widget['settings']['button_padding'] = [
                    'unit' => 'px',
                    'top' => '12',
                    'right' => '30',
                    'bottom' => '12',
                    'left' => '30',
                    'isLinked' => false
                ];

                // Hover effects
                $widget['settings']['hover_animation'] = 'none';
                $widget['settings']['button_background_hover_color'] = '#FABA29';
                $widget['settings']['hover_color'] = '#FFFFFF';

                echo "    Button updated\n";
            }

            // Update heading spacing
            if ($widget['widgetType'] === 'heading') {
                $widget['settings']['_margin'] = [
                    'unit' => 'px',
                    'top' => '0',
                    'bottom' => '20'
                ];
            }

            // Update text editor spacing
            if ($widget['widgetType'] === 'text-editor') {
                $widget['settings']['_margin'] = [
                    'unit' => 'px',
                    'bottom' => '20'
                ];
            }
        }
    }

    $programs_updated = true;
    break; // Only update first Programs section found
}

if ($programs_updated) {
    $success = update_post_meta($page_id, '_elementor_data', wp_slash(json_encode($decoded)));

    if ($success) {
        echo "\n✅ SUCCESS! Programs section cards fixed.\n";
        echo "Applied: White backgrounds, colored borders, rounded corners, shadows, proper spacing\n";
        echo "\nNEXT: Open Elementor editor and click 'Update'\n";
        echo "URL: http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor\n";
    } else {
        echo "\n❌ ERROR: Could not save updates\n";
    }
} else {
    echo "\n⚠️ WARNING: Could not find Programs section\n";
}
