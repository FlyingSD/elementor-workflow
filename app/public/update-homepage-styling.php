<?php
/**
 * Update Homepage Styling - KEEP ALL CONTENT, just improve styling
 * - Benefits: Better spacing, borders, shadows
 * - Programs: Better card styling, spacing
 * - Blog: Add proper content to existing section
 */

require_once(__DIR__ . '/wp-load.php');

$page_id = 21;
$data = get_post_meta($page_id, '_elementor_data', true);
$decoded = json_decode($data, true);

if (!$decoded) {
    die("ERROR: Could not decode Elementor data\n");
}

echo "Found " . count($decoded) . " sections on page 21\n";
echo "Updating styling only - keeping all content...\n\n";

$benefits_updated = false;
$programs_updated = false;
$blog_updated = false;

foreach ($decoded as $section_index => &$section) {
    if ($section['elType'] !== 'section') continue;

    // Check columns for section identification
    foreach ($section['elements'] as $col_index => &$column) {
        if ($column['elType'] !== 'column') continue;

        foreach ($column['elements'] as $widget_index => &$widget) {
            if ($widget['elType'] !== 'widget' || $widget['widgetType'] !== 'heading') continue;

            $heading_text = $widget['settings']['title'] ?? '';

            // BENEFITS SECTION - "Предимства"
            if (strpos($heading_text, 'Предимства') !== false && !$benefits_updated) {
                echo "✅ Found Benefits section at index $section_index\n";

                // Update section background
                $decoded[$section_index]['settings']['background_background'] = 'classic';
                $decoded[$section_index]['settings']['background_color'] = '#fff9e6';
                $decoded[$section_index]['settings']['padding'] = [
                    'unit' => 'px',
                    'top' => '90',
                    'right' => '20',
                    'bottom' => '90',
                    'left' => '20'
                ];

                // Update all 3 benefit card columns (skip first column which is heading)
                $card_count = 0;
                foreach ($decoded[$section_index]['elements'] as $benefit_col_index => &$benefit_column) {
                    if ($benefit_col_index === 0) continue; // Skip title column

                    $card_count++;

                    // Apply card styling to column
                    $benefit_column['settings']['background_background'] = 'classic';
                    $benefit_column['settings']['background_color'] = '#FFFFFF';
                    $benefit_column['settings']['border_border'] = 'solid';
                    $benefit_column['settings']['border_width'] = [
                        'unit' => 'px',
                        'top' => '5',
                        'right' => '0',
                        'bottom' => '0',
                        'left' => '0'
                    ];

                    // Different top border color for each card
                    if ($card_count === 1) {
                        $benefit_column['settings']['border_color'] = 'var(--e-global-color-primary)'; // Yellow
                    } elseif ($card_count === 2) {
                        $benefit_column['settings']['border_color'] = 'var(--e-global-color-accent)'; // Coral
                    } else {
                        $benefit_column['settings']['border_color'] = 'var(--e-global-color-secondary)'; // Teal
                    }

                    $benefit_column['settings']['border_radius'] = [
                        'unit' => 'px',
                        'top' => '20',
                        'right' => '20',
                        'bottom' => '20',
                        'left' => '20'
                    ];
                    $benefit_column['settings']['padding'] = [
                        'unit' => 'px',
                        'top' => '45',
                        'right' => '35',
                        'bottom' => '45',
                        'left' => '35'
                    ];
                    $benefit_column['settings']['box_shadow_box_shadow_type'] = 'yes';
                    $benefit_column['settings']['box_shadow_box_shadow'] = [
                        'horizontal' => 0,
                        'vertical' => 10,
                        'blur' => 35,
                        'spread' => 0,
                        'color' => 'rgba(0, 0, 0, 0.08)'
                    ];

                    // Update spacing for widgets inside
                    foreach ($benefit_column['elements'] as $benefit_widget_index => &$benefit_widget) {
                        if ($benefit_widget['widgetType'] === 'heading') {
                            $benefit_widget['settings']['_margin'] = [
                                'unit' => 'px',
                                'top' => '0',
                                'bottom' => '15'
                            ];
                        } elseif ($benefit_widget['widgetType'] === 'text-editor') {
                            $benefit_widget['settings']['_margin'] = [
                                'unit' => 'px',
                                'bottom' => '10'
                            ];
                        } elseif ($benefit_widget['widgetType'] === 'icon-box') {
                            $benefit_widget['settings']['_margin'] = [
                                'unit' => 'px',
                                'bottom' => '20'
                            ];
                        }
                    }
                }

                $benefits_updated = true;
                echo "   Updated styling for 3 benefit cards\n";
            }

            // PROGRAMS SECTION - "програм"
            if (strpos(strtolower($heading_text), 'програм') !== false && !$programs_updated) {
                echo "✅ Found Programs section at index $section_index\n";

                // Update section background
                $decoded[$section_index]['settings']['background_background'] = 'classic';
                $decoded[$section_index]['settings']['background_color'] = '#FFFFFF';
                $decoded[$section_index]['settings']['padding'] = [
                    'unit' => 'px',
                    'top' => '90',
                    'right' => '20',
                    'bottom' => '90',
                    'left' => '20'
                ];

                // Update all 3 program card columns
                $card_count = 0;
                foreach ($decoded[$section_index]['elements'] as $program_col_index => &$program_column) {
                    if ($program_col_index === 0) continue; // Skip title column

                    $card_count++;

                    // Apply same card styling as Benefits
                    $program_column['settings']['background_background'] = 'classic';
                    $program_column['settings']['background_color'] = '#FFFFFF';
                    $program_column['settings']['border_border'] = 'solid';
                    $program_column['settings']['border_width'] = [
                        'unit' => 'px',
                        'top' => '5',
                        'right' => '0',
                        'bottom' => '0',
                        'left' => '0'
                    ];

                    // Different top border color for each card
                    if ($card_count === 1) {
                        $program_column['settings']['border_color'] = 'var(--e-global-color-primary)';
                    } elseif ($card_count === 2) {
                        $program_column['settings']['border_color'] = 'var(--e-global-color-accent)';
                    } else {
                        $program_column['settings']['border_color'] = 'var(--e-global-color-secondary)';
                    }

                    $program_column['settings']['border_radius'] = [
                        'unit' => 'px',
                        'top' => '20',
                        'right' => '20',
                        'bottom' => '20',
                        'left' => '20'
                    ];
                    $program_column['settings']['padding'] = [
                        'unit' => 'px',
                        'top' => '45',
                        'right' => '35',
                        'bottom' => '45',
                        'left' => '35'
                    ];
                    $program_column['settings']['box_shadow_box_shadow_type'] = 'yes';
                    $program_column['settings']['box_shadow_box_shadow'] = [
                        'horizontal' => 0,
                        'vertical' => 10,
                        'blur' => 35,
                        'spread' => 0,
                        'color' => 'rgba(0, 0, 0, 0.08)'
                    ];

                    // Update button styling if present
                    foreach ($program_column['elements'] as $program_widget_index => &$program_widget) {
                        if ($program_widget['widgetType'] === 'button') {
                            $program_widget['settings']['button_text_color'] = 'var(--e-global-color-text)';
                            $program_widget['settings']['background_color'] = 'transparent';
                            $program_widget['settings']['border_border'] = 'solid';
                            $program_widget['settings']['border_width'] = [
                                'unit' => 'px',
                                'top' => '2',
                                'right' => '2',
                                'bottom' => '2',
                                'left' => '2'
                            ];
                            $program_widget['settings']['border_color'] = 'var(--e-global-color-primary)';
                            $program_widget['settings']['border_radius'] = [
                                'unit' => 'px',
                                'top' => '12',
                                'right' => '12',
                                'bottom' => '12',
                                'left' => '12'
                            ];
                            $program_widget['settings']['button_padding'] = [
                                'unit' => 'px',
                                'top' => '12',
                                'right' => '30',
                                'bottom' => '12',
                                'left' => '30'
                            ];
                        }
                    }
                }

                $programs_updated = true;
                echo "   Updated styling for 3 program cards\n";
            }

            // BLOG SECTION - "блог"
            if (strpos(strtolower($heading_text), 'блог') !== false && !$blog_updated) {
                echo "✅ Found Blog section at index $section_index\n";

                // Update section background
                $decoded[$section_index]['settings']['background_background'] = 'classic';
                $decoded[$section_index]['settings']['background_color'] = '#FFFFFF';
                $decoded[$section_index]['settings']['padding'] = [
                    'unit' => 'px',
                    'top' => '90',
                    'right' => '20',
                    'bottom' => '90',
                    'left' => '20'
                ];

                $blog_updated = true;
                echo "   Updated Blog section background\n";
            }
        }
    }
}

// Save updates
if ($benefits_updated || $programs_updated || $blog_updated) {
    $success = update_post_meta($page_id, '_elementor_data', wp_slash(json_encode($decoded)));

    if ($success) {
        echo "\n✅ SUCCESS! Page 21 styling updated.\n";
        echo "Updated sections: ";
        echo $benefits_updated ? "Benefits ✅ " : "";
        echo $programs_updated ? "Programs ✅ " : "";
        echo $blog_updated ? "Blog ✅ " : "";
        echo "\n\nNEXT STEP: Open Elementor editor and click 'Update' button\n";
        echo "URL: http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor\n";
    } else {
        echo "\n❌ ERROR: Could not save updates\n";
    }
} else {
    echo "\n⚠️ WARNING: Could not find sections to update\n";
    echo "Check section titles in Elementor.\n";
}
