<?php
/**
 * Add Full Header with Logo, Nav Menu, and CTA Button
 * Creates a complete header section with all three elements
 */

require_once(__DIR__ . '/wp-load.php');

if (!isset($_GET['key']) || $_GET['key'] !== 'full_header_2025') {
    die('Unauthorized. Add ?key=full_header_2025');
}

echo "<pre>\n";
echo "============================================================\n";
echo "  ADD COMPLETE HEADER TO ALL PAGES\n";
echo "============================================================\n\n";

// Function to create complete header section
function create_complete_header_section() {
    return [
        'id' => uniqid(),
        'elType' => 'section',
        'settings' => [
            'stretch_section' => 'section-stretched',
            'layout' => 'full_width',
            'background_background' => 'classic',
            'background_color' => '#FFFFFF',
            'padding' => [
                'unit' => 'px',
                'top' => 20,
                'right' => 40,
                'bottom' => 20,
                'left' => 40,
                'isLinked' => false
            ],
            'border_border' => 'solid',
            'border_width' => [
                'unit' => 'px',
                'top' => 0,
                'right' => 0,
                'bottom' => 1,
                'left' => 0,
                'isLinked' => false
            ],
            'border_color' => '#E5E5E5'
        ],
        'elements' => [
            // Column 1: Logo (30% width)
            [
                'id' => uniqid(),
                'elType' => 'column',
                'settings' => [
                    '_column_size' => 30,
                    'content_position' => 'center'
                ],
                'elements' => [
                    [
                        'id' => uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => '<a href="/" style="text-decoration: none; color: #4F9F8B;">Светлинки</a>',
                            'header_size' => 'h2',
                            'title_color' => '#4F9F8B',
                            'typography_typography' => 'custom',
                            'typography_font_size' => [
                                'unit' => 'px',
                                'size' => 28
                            ],
                            'typography_font_weight' => '700',
                            'align' => 'left'
                        ]
                    ]
                ]
            ],
            // Column 2: Navigation Menu (40% width)
            [
                'id' => uniqid(),
                'elType' => 'column',
                'settings' => [
                    '_column_size' => 40,
                    'content_position' => 'center'
                ],
                'elements' => [
                    [
                        'id' => uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'html',
                        'settings' => [
                            'html' => '<nav style="display: flex; justify-content: center; align-items: center; gap: 30px; height: 100%;">
    <a href="/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Начало</a>
    <a href="/about/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">За Нас</a>
    <a href="/programs/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Програми</a>
    <a href="/contact/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Контакти</a>
    <a href="/faq/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">FAQ</a>
</nav>'
                        ]
                    ]
                ]
            ],
            // Column 3: CTA Button (30% width)
            [
                'id' => uniqid(),
                'elType' => 'column',
                'settings' => [
                    '_column_size' => 30,
                    'content_position' => 'center'
                ],
                'elements' => [
                    [
                        'id' => uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'button',
                        'settings' => [
                            'text' => 'ЗАПАЗИ СЕ СЕГА',
                            'link' => [
                                'url' => '/contact/',
                                'is_external' => '',
                                'nofollow' => ''
                            ],
                            'align' => 'right',
                            'size' => 'md',
                            'button_type' => 'default',
                            'typography_typography' => 'custom',
                            'typography_font_size' => [
                                'unit' => 'px',
                                'size' => 16
                            ],
                            'typography_font_weight' => '600',
                            'button_text_color' => '#000000',
                            'background_color' => '#FABA29',
                            'button_background_hover_color' => '#E0A820',
                            'hover_color' => '#FFFFFF',
                            'border_radius' => [
                                'unit' => 'px',
                                'size' => 5
                            ],
                            'button_padding' => [
                                'unit' => 'px',
                                'top' => 15,
                                'right' => 30,
                                'bottom' => 15,
                                'left' => 30,
                                'isLinked' => false
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ];
}

$pages = [
    ['id' => 23, 'name' => 'About'],
    ['id' => 25, 'name' => 'Programs'],
    ['id' => 27, 'name' => 'Contact'],
    ['id' => 29, 'name' => 'FAQ']
];

foreach ($pages as $page) {
    echo "[PAGE] Processing {$page['name']} (ID {$page['id']})...\n";

    $current_data = get_post_meta($page['id'], '_elementor_data', true);

    if (empty($current_data)) {
        echo "  [ERROR] No Elementor data for {$page['name']}\n";
        continue;
    }

    $page_structure = json_decode($current_data, true);

    if (!is_array($page_structure)) {
        echo "  [ERROR] Invalid data for {$page['name']}\n";
        continue;
    }

    // Remove first section if it's the simple nav menu we added earlier
    if (isset($page_structure[0]['elements'][0]['elements'][0])) {
        $first_widget = $page_structure[0]['elements'][0]['elements'][0];
        if (isset($first_widget['widgetType']) && $first_widget['widgetType'] === 'html') {
            if (isset($first_widget['settings']['html']) && strpos($first_widget['settings']['html'], '<nav') !== false) {
                array_shift($page_structure);
                echo "  [INFO] Removed old simple nav menu\n";
            }
        }
    }

    // Add complete header section
    $header_section = create_complete_header_section();
    array_unshift($page_structure, $header_section);

    // Update page
    $result = update_post_meta($page['id'], '_elementor_data', wp_slash(json_encode($page_structure)));

    if ($result !== false) {
        echo "  [OK] Complete header added to {$page['name']}\n";
        update_post_meta($page['id'], '_elementor_css', '');
    } else {
        echo "  [ERROR] Failed to update {$page['name']}\n";
    }
}

echo "\n[CACHE] Clearing cache...\n";
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
    echo "[OK] Cache cleared\n";
}

echo "\n============================================================\n";
echo "[SUCCESS] COMPLETE HEADER ADDED!\n";
echo "============================================================\n\n";

echo "Header includes:\n";
echo "  - Logo 'Светлинки' (left, clickable, teal color)\n";
echo "  - Navigation menu (center, 5 links)\n";
echo "  - CTA button 'ЗАПАЗИ СЕ СЕГА' (right, golden yellow)\n\n";

echo "IMPORTANT: Open each page in Elementor and click 'Update':\n";
echo "  1. http://svetlinkielementor.local/wp-admin/post.php?post=23&action=elementor\n";
echo "  2. http://svetlinkielementor.local/wp-admin/post.php?post=25&action=elementor\n";
echo "  3. http://svetlinkielementor.local/wp-admin/post.php?post=27&action=elementor\n";
echo "  4. http://svetlinkielementor.local/wp-admin/post.php?post=29&action=elementor\n\n";

echo "============================================================\n";
echo "</pre>";
?>
