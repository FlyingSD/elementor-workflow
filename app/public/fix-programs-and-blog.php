<?php
/**
 * Fix Benefits, Programs and Blog sections on Homepage (Page 21)
 * - Benefits: Build 3 cards without emojis
 * - Programs: Build 3 cards without emojis
 * - Blog: Replace Image Carousel with styled blog card
 */

require_once(__DIR__ . '/wp-load.php');

$page_id = 21;
$data = get_post_meta($page_id, '_elementor_data', true);
$decoded = json_decode($data, true);

if (!$decoded) {
    die("ERROR: Could not decode Elementor data\n");
}

echo "Found " . count($decoded) . " sections on page 21\n";

// Find and update sections
$programs_updated = false;
$blog_updated = false;

foreach ($decoded as $section_index => &$section) {
    if ($section['elType'] !== 'section') continue;

    // Check each column for section titles
    foreach ($section['elements'] as $col_index => &$column) {
        if ($column['elType'] !== 'column') continue;

        foreach ($column['elements'] as $widget_index => $widget) {
            if ($widget['elType'] !== 'widget') continue;

            // Check if this is section title
            if ($widget['widgetType'] === 'heading') {
                $heading_text = $widget['settings']['title'] ?? '';

                // PROGRAMS SECTION - "Нашите програми"
                if (strpos($heading_text, 'програм') !== false && !$programs_updated) {
                    echo "\n✅ Found Programs section at index $section_index\n";

                    // Clear existing columns and rebuild with 3 cards
                    $decoded[$section_index]['elements'] = [
                        // Column for section title (full width)
                        [
                            'id' => bin2hex(random_bytes(4)),
                            'elType' => 'column',
                            'settings' => [
                                '_column_size' => 100,
                                'background_background' => 'classic',
                                'background_color' => '#fff9e6'
                            ],
                            'elements' => [
                                [
                                    'id' => bin2hex(random_bytes(4)),
                                    'elType' => 'widget',
                                    'widgetType' => 'heading',
                                    'settings' => [
                                        'title' => 'Нашите програми',
                                        'header_size' => 'h2',
                                        'align' => 'center',
                                        'title_color' => 'var(--e-global-color-text)',
                                        '_margin' => [
                                            'unit' => 'px',
                                            'top' => '0',
                                            'right' => '0',
                                            'bottom' => '40',
                                            'left' => '0'
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ];

                    // CARD 1: 5 Нива
                    $decoded[$section_index]['elements'][] = [
                        'id' => bin2hex(random_bytes(4)),
                        'elType' => 'column',
                        'settings' => [
                            '_column_size' => 33,
                            'background_background' => 'classic',
                            'background_color' => '#FFFFFF',
                            'border_border' => 'solid',
                            'border_width' => ['unit' => 'px', 'top' => '5', 'right' => '0', 'bottom' => '0', 'left' => '0'],
                            'border_color' => 'var(--e-global-color-primary)',
                            'border_radius' => ['unit' => 'px', 'top' => '20', 'right' => '20', 'bottom' => '20', 'left' => '20'],
                            'padding' => ['unit' => 'px', 'top' => '45', 'right' => '35', 'bottom' => '45', 'left' => '35'],
                            'box_shadow_box_shadow_type' => 'yes',
                            'box_shadow_box_shadow' => [
                                'horizontal' => 0,
                                'vertical' => 10,
                                'blur' => 35,
                                'spread' => 0,
                                'color' => 'rgba(0, 0, 0, 0.08)'
                            ]
                        ],
                        'elements' => [
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'heading',
                                'settings' => [
                                    'title' => '5 нива на обучение',
                                    'header_size' => 'h3',
                                    'title_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'top' => '0', 'bottom' => '20']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'text-editor',
                                'settings' => [
                                    'editor' => '<ul>
<li><strong>Ниво 1:</strong> Основи с абакус</li>
<li><strong>Ниво 2:</strong> Ментална визуализация</li>
<li><strong>Ниво 3:</strong> Сложни операции</li>
<li><strong>Ниво 4:</strong> Майсторско ниво</li>
<li><strong>Ниво 5:</strong> Състезателна група</li>
</ul>',
                                    'text_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'bottom' => '25']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'button',
                                'settings' => [
                                    'text' => 'Прочети повече',
                                    'link' => ['url' => '/programs/'],
                                    'button_text_color' => 'var(--e-global-color-text)',
                                    'background_color' => 'transparent',
                                    'border_border' => 'solid',
                                    'border_width' => ['unit' => 'px', 'top' => '2', 'right' => '2', 'bottom' => '2', 'left' => '2'],
                                    'border_color' => 'var(--e-global-color-primary)',
                                    'border_radius' => ['unit' => 'px', 'top' => '12', 'right' => '12', 'bottom' => '12', 'left' => '12'],
                                    'button_padding' => ['unit' => 'px', 'top' => '12', 'right' => '30', 'bottom' => '12', 'left' => '30']
                                ]
                            ]
                        ]
                    ];

                    // CARD 2: Промоции
                    $decoded[$section_index]['elements'][] = [
                        'id' => bin2hex(random_bytes(4)),
                        'elType' => 'column',
                        'settings' => [
                            '_column_size' => 33,
                            'background_background' => 'classic',
                            'background_color' => '#FFFFFF',
                            'border_border' => 'solid',
                            'border_width' => ['unit' => 'px', 'top' => '5', 'right' => '0', 'bottom' => '0', 'left' => '0'],
                            'border_color' => 'var(--e-global-color-accent)',
                            'border_radius' => ['unit' => 'px', 'top' => '20', 'right' => '20', 'bottom' => '20', 'left' => '20'],
                            'padding' => ['unit' => 'px', 'top' => '45', 'right' => '35', 'bottom' => '45', 'left' => '35'],
                            'box_shadow_box_shadow_type' => 'yes',
                            'box_shadow_box_shadow' => [
                                'horizontal' => 0,
                                'vertical' => 10,
                                'blur' => 35,
                                'spread' => 0,
                                'color' => 'rgba(0, 0, 0, 0.08)'
                            ]
                        ],
                        'elements' => [
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'heading',
                                'settings' => [
                                    'title' => 'Специални промоции',
                                    'header_size' => 'h3',
                                    'title_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'top' => '0', 'bottom' => '20']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'text-editor',
                                'settings' => [
                                    'editor' => '<p><strong>Безплатен пробен урок</strong><br>за всяко ново дете!</p>
<p><strong>10% отстъпка</strong><br>при записване на второ дете от семейството</p>
<p style="font-size: 0.85em; font-style: italic; margin-top: 20px;">* Промоциите са валидни за нови записвания до края на месеца. Не се комбинират с други оферти.</p>',
                                    'text_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'bottom' => '25']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'button',
                                'settings' => [
                                    'text' => 'Прочети повече',
                                    'link' => ['url' => '/programs/#pricing'],
                                    'button_text_color' => 'var(--e-global-color-text)',
                                    'background_color' => 'transparent',
                                    'border_border' => 'solid',
                                    'border_width' => ['unit' => 'px', 'top' => '2', 'right' => '2', 'bottom' => '2', 'left' => '2'],
                                    'border_color' => 'var(--e-global-color-primary)',
                                    'border_radius' => ['unit' => 'px', 'top' => '12', 'right' => '12', 'bottom' => '12', 'left' => '12'],
                                    'button_padding' => ['unit' => 'px', 'top' => '12', 'right' => '30', 'bottom' => '12', 'left' => '30']
                                ]
                            ]
                        ]
                    ];

                    // CARD 3: FAQ
                    $decoded[$section_index]['elements'][] = [
                        'id' => bin2hex(random_bytes(4)),
                        'elType' => 'column',
                        'settings' => [
                            '_column_size' => 33,
                            'background_background' => 'classic',
                            'background_color' => '#FFFFFF',
                            'border_border' => 'solid',
                            'border_width' => ['unit' => 'px', 'top' => '5', 'right' => '0', 'bottom' => '0', 'left' => '0'],
                            'border_color' => 'var(--e-global-color-secondary)',
                            'border_radius' => ['unit' => 'px', 'top' => '20', 'right' => '20', 'bottom' => '20', 'left' => '20'],
                            'padding' => ['unit' => 'px', 'top' => '45', 'right' => '35', 'bottom' => '45', 'left' => '35'],
                            'box_shadow_box_shadow_type' => 'yes',
                            'box_shadow_box_shadow' => [
                                'horizontal' => 0,
                                'vertical' => 10,
                                'blur' => 35,
                                'spread' => 0,
                                'color' => 'rgba(0, 0, 0, 0.08)'
                            ]
                        ],
                        'elements' => [
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'heading',
                                'settings' => [
                                    'title' => 'Имате въпроси?',
                                    'header_size' => 'h3',
                                    'title_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'top' => '0', 'bottom' => '20']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'text-editor',
                                'settings' => [
                                    'editor' => '<p>Отговорихме на най-честите въпроси на родителите:</p>
<p><strong>•</strong> Колко струва обучението?<br>
<strong>•</strong> Колко деца има в група?<br>
<strong>•</strong> Колко време трае програмата?<br>
<strong>•</strong> Какви са резултатите?</p>
<p>...и още 16 въпроса!</p>',
                                    'text_color' => 'var(--e-global-color-text)',
                                    '_margin' => ['unit' => 'px', 'bottom' => '25']
                                ]
                            ],
                            [
                                'id' => bin2hex(random_bytes(4)),
                                'elType' => 'widget',
                                'widgetType' => 'button',
                                'settings' => [
                                    'text' => 'Прочети повече',
                                    'link' => ['url' => '/faq/'],
                                    'button_text_color' => 'var(--e-global-color-text)',
                                    'background_color' => 'transparent',
                                    'border_border' => 'solid',
                                    'border_width' => ['unit' => 'px', 'top' => '2', 'right' => '2', 'bottom' => '2', 'left' => '2'],
                                    'border_color' => 'var(--e-global-color-primary)',
                                    'border_radius' => ['unit' => 'px', 'top' => '12', 'right' => '12', 'bottom' => '12', 'left' => '12'],
                                    'button_padding' => ['unit' => 'px', 'top' => '12', 'right' => '30', 'bottom' => '12', 'left' => '30']
                                ]
                            ]
                        ]
                    ];

                    $programs_updated = true;
                    echo "✅ Programs section rebuilt with 3 cards (no emojis)\n";
                }

                // BLOG SECTION - "Нашият блог" or similar
                if ((strpos($heading_text, 'блог') !== false || strpos($heading_text, 'Блог') !== false) && !$blog_updated) {
                    echo "\n✅ Found Blog section at index $section_index\n";

                    // Rebuild blog section with styled card
                    $decoded[$section_index]['elements'] = [
                        // Column for section title
                        [
                            'id' => bin2hex(random_bytes(4)),
                            'elType' => 'column',
                            'settings' => [
                                '_column_size' => 100,
                                'background_background' => 'classic',
                                'background_color' => '#FFFFFF'
                            ],
                            'elements' => [
                                [
                                    'id' => bin2hex(random_bytes(4)),
                                    'elType' => 'widget',
                                    'widgetType' => 'heading',
                                    'settings' => [
                                        'title' => 'От нашия блог',
                                        'header_size' => 'h2',
                                        'align' => 'center',
                                        'title_color' => 'var(--e-global-color-text)',
                                        '_margin' => [
                                            'unit' => 'px',
                                            'top' => '0',
                                            'right' => '0',
                                            'bottom' => '40',
                                            'left' => '0'
                                        ]
                                    ]
                                ]
                            ]
                        ],
                        // Column for blog card
                        [
                            'id' => bin2hex(random_bytes(4)),
                            'elType' => 'column',
                            'settings' => [
                                '_column_size' => 100,
                                'background_background' => 'classic',
                                'background_color' => '#FEFCF5',
                                'border_border' => 'solid',
                                'border_width' => ['unit' => 'px', 'top' => '5', 'right' => '0', 'bottom' => '0', 'left' => '0'],
                                'border_color' => 'var(--e-global-color-primary)',
                                'border_radius' => ['unit' => 'px', 'top' => '20', 'right' => '20', 'bottom' => '20', 'left' => '20'],
                                'padding' => ['unit' => 'px', 'top' => '45', 'right' => '40', 'bottom' => '45', 'left' => '40'],
                                'box_shadow_box_shadow_type' => 'yes',
                                'box_shadow_box_shadow' => [
                                    'horizontal' => 0,
                                    'vertical' => 10,
                                    'blur' => 35,
                                    'spread' => 0,
                                    'color' => 'rgba(0, 0, 0, 0.08)'
                                ],
                                'width' => ['unit' => '%', 'size' => 80],
                                'width_tablet' => ['unit' => '%', 'size' => 90],
                                'width_mobile' => ['unit' => '%', 'size' => 100]
                            ],
                            'elements' => [
                                [
                                    'id' => bin2hex(random_bytes(4)),
                                    'elType' => 'widget',
                                    'widgetType' => 'heading',
                                    'settings' => [
                                        'title' => 'Не, това не е просто "бързо смятане"',
                                        'header_size' => 'h3',
                                        'title_color' => 'var(--e-global-color-text)',
                                        '_margin' => ['unit' => 'px', 'top' => '0', 'bottom' => '15']
                                    ]
                                ],
                                [
                                    'id' => bin2hex(random_bytes(4)),
                                    'elType' => 'widget',
                                    'widgetType' => 'text-editor',
                                    'settings' => [
                                        'editor' => '<p>Ментална аритметика не е само изчисления - това е цялостна тренировка на мозъка, която развива концентрация, памет и увереност. Открийте истинската магия зад методиката...</p>',
                                        'text_color' => 'var(--e-global-color-text)',
                                        '_margin' => ['unit' => 'px', 'bottom' => '20']
                                    ]
                                ],
                                [
                                    'id' => bin2hex(random_bytes(4)),
                                    'elType' => 'widget',
                                    'widgetType' => 'button',
                                    'settings' => [
                                        'text' => 'Прочети повече →',
                                        'link' => ['url' => '/blog/'],
                                        'button_text_color' => 'var(--e-global-color-text)',
                                        'background_color' => 'transparent',
                                        'border_border' => 'solid',
                                        'border_width' => ['unit' => 'px', 'top' => '2', 'right' => '2', 'bottom' => '2', 'left' => '2'],
                                        'border_color' => 'var(--e-global-color-primary)',
                                        'border_radius' => ['unit' => 'px', 'top' => '12', 'right' => '12', 'bottom' => '12', 'left' => '12'],
                                        'button_padding' => ['unit' => 'px', 'top' => '12', 'right' => '30', 'bottom' => '12', 'left' => '30']
                                    ]
                                ]
                            ]
                        ]
                    ];

                    $blog_updated = true;
                    echo "✅ Blog section rebuilt with styled card\n";
                }
            }
        }
    }
}

// Save updates
if ($programs_updated || $blog_updated) {
    $success = update_post_meta($page_id, '_elementor_data', wp_slash(json_encode($decoded)));

    if ($success) {
        echo "\n✅ SUCCESS! Page 21 updated.\n";
        echo "Updated sections: ";
        echo $programs_updated ? "Programs ✅ " : "";
        echo $blog_updated ? "Blog ✅ " : "";
        echo "\n\nNEXT STEP: Open Elementor editor and click 'Update' button\n";
        echo "URL: http://svetlinkielementor.local/wp-admin/post.php?post=21&action=elementor\n";
    } else {
        echo "\n❌ ERROR: Could not save updates\n";
    }
} else {
    echo "\n⚠️ WARNING: Could not find Programs or Blog sections\n";
    echo "Check section titles in Elementor.\n";
}
