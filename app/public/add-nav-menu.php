<?php
/**
 * Add Navigation Menu to All Pages
 * Copies the nav menu HTML widget from homepage to other pages
 */

require_once(__DIR__ . '/wp-load.php');

// Security
if (!isset($_GET['key']) || $_GET['key'] !== 'add_nav_2025') {
    die('Unauthorized. Add ?key=add_nav_2025');
}

echo "<pre>\n";
echo "============================================================\n";
echo "  ADD NAVIGATION MENU TO ALL PAGES\n";
echo "============================================================\n\n";

// Navigation menu HTML (from homepage)
$nav_html = '<nav style="display: flex; justify-content: center; align-items: center; gap: 30px; height: 100%;">
    <a href="/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Начало</a>
    <a href="/about/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">За Нас</a>
    <a href="/programs/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Програми</a>
    <a href="/contact/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">Контакти</a>
    <a href="/faq/" style="text-decoration: none; color: #2C2C2C; font-weight: 500; transition: color 0.3s;">FAQ</a>
</nav>';

// Create navigation section structure
function create_nav_section($nav_html) {
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
            [
                'id' => uniqid(),
                'elType' => 'column',
                'settings' => [
                    '_column_size' => 100,
                    '_inline_size' => null
                ],
                'elements' => [
                    [
                        'id' => uniqid(),
                        'elType' => 'widget',
                        'settings' => [
                            'html' => $nav_html
                        ],
                        'elements' => [],
                        'widgetType' => 'html'
                    ]
                ]
            ]
        ]
    ];
}

// Pages to update
$pages = [
    ['id' => 23, 'name' => 'About'],
    ['id' => 25, 'name' => 'Programs'],
    ['id' => 27, 'name' => 'Contact'],
    ['id' => 29, 'name' => 'FAQ']
];

foreach ($pages as $page) {
    echo "[PAGE] Processing {$page['name']} (ID {$page['id']})...\n";

    // Get current page data
    $current_data = get_post_meta($page['id'], '_elementor_data', true);

    if (empty($current_data)) {
        echo "  [ERROR] No Elementor data found for {$page['name']}\n";
        continue;
    }

    $page_structure = json_decode($current_data, true);

    if (!is_array($page_structure)) {
        echo "  [ERROR] Invalid Elementor data for {$page['name']}\n";
        continue;
    }

    // Check if first section already has navigation
    $has_nav = false;
    if (isset($page_structure[0]['elements'][0]['elements'][0])) {
        $first_widget = $page_structure[0]['elements'][0]['elements'][0];
        if (isset($first_widget['widgetType']) && $first_widget['widgetType'] === 'html') {
            if (isset($first_widget['settings']['html']) && strpos($first_widget['settings']['html'], '<nav') !== false) {
                $has_nav = true;
            }
        }
    }

    if ($has_nav) {
        echo "  [INFO] {$page['name']} already has navigation menu\n";
        continue;
    }

    // Add navigation section at the beginning
    $nav_section = create_nav_section($nav_html);
    array_unshift($page_structure, $nav_section);

    // Update page
    $result = update_post_meta($page['id'], '_elementor_data', wp_slash(json_encode($page_structure)));

    if ($result !== false) {
        echo "  [OK] Navigation menu added to {$page['name']}\n";

        // Clear CSS cache
        update_post_meta($page['id'], '_elementor_css', '');
    } else {
        echo "  [ERROR] Failed to update {$page['name']}\n";
    }
}

echo "\n[CACHE] Clearing Elementor cache...\n";
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
    echo "[OK] Cache cleared\n";
}

echo "\n============================================================\n";
echo "[SUCCESS] NAVIGATION MENU ADDED!\n";
echo "============================================================\n\n";

echo "What was done:\n";
echo "  - Added navigation menu to About, Programs, Contact, FAQ pages\n";
echo "  - Navigation menu placed at top of each page\n";
echo "  - Elementor cache cleared\n\n";

echo "IMPORTANT:\n";
echo "  You MUST open each page in Elementor editor and click 'Update'\n";
echo "  to trigger Elementor's internal hooks!\n\n";

echo "Pages to update:\n";
echo "  1. http://svetlinkielementor.local/wp-admin/post.php?post=23&action=elementor\n";
echo "  2. http://svetlinkielementor.local/wp-admin/post.php?post=25&action=elementor\n";
echo "  3. http://svetlinkielementor.local/wp-admin/post.php?post=27&action=elementor\n";
echo "  4. http://svetlinkielementor.local/wp-admin/post.php?post=29&action=elementor\n\n";

echo "============================================================\n";
echo "</pre>";
?>
