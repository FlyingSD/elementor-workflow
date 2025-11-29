<?php
/**
 * Standalone script to update Elementor homepage
 * Run via: php update-elementor-home.php
 */

// Load WordPress
require_once(__DIR__ . '/wp-load.php');

$page_id = 19;

// Define the Elementor structure
$elementor_data = [
    [
        'id' => 'hero_' . uniqid(),
        'elType' => 'section',
        'settings' => [
            'background_background' => 'classic',
            'background_color' => 'var(--e-global-color-background)',
            'padding' => [
                'unit' => 'px',
                'top' => '80',
                'right' => '20',
                'bottom' => '80',
                'left' => '20',
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => 'col_' . uniqid(),
                'elType' => 'column',
                'settings' => [
                    '_column_size' => 100,
                    '_inline_size' => null
                ],
                'elements' => [
                    [
                        'id' => 'heading_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Развивайте Математические Умения на Вашего Дете',
                            'align' => 'center',
                            'header_size' => 'h1',
                            'title_color' => 'var(--e-global-color-primary)'
                        ]
                    ],
                    [
                        'id' => 'text_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<p style="text-align: center; font-size: 18px; margin: 20px 0;">Професионален обучен персонал развиват математични умения на детето Вашего в ласкава среда</p>'
                        ]
                    ],
                    [
                        'id' => 'stats_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<div style="display: flex; justify-content: center; gap: 40px; margin: 30px 0; flex-wrap: wrap;"><div style="text-align: center;"><strong style="font-size: 32px; color: var(--e-global-color-secondary); display: block;">500+</strong><span>ученици</span></div><div style="text-align: center;"><strong style="font-size: 32px; color: var(--e-global-color-secondary); display: block;">8+</strong><span>години</span></div></div>'
                        ]
                    ],
                    [
                        'id' => 'button_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'button',
                        'settings' => [
                            'text' => 'ЗАПАЗИ СЕ СЕГА',
                            'align' => 'center',
                            'size' => 'lg',
                            'button_background_color' => 'var(--e-global-color-secondary)',
                            'button_text_color' => '#ffffff',
                            'link' => [
                                'url' => '#contact',
                                'is_external' => false,
                                'nofollow' => false
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ],
    [
        'id' => 'why_' . uniqid(),
        'elType' => 'section',
        'settings' => [
            'background_background' => 'classic',
            'background_color' => '#ffffff',
            'padding' => [
                'unit' => 'px',
                'top' => '60',
                'right' => '20',
                'bottom' => '60',
                'left' => '20',
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => 'col_' . uniqid(),
                'elType' => 'column',
                'settings' => ['_column_size' => 100],
                'elements' => [
                    [
                        'id' => 'heading_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Защо да изберете "Светлинки"?',
                            'align' => 'center',
                            'header_size' => 'h2',
                            'title_color' => 'var(--e-global-color-primary)'
                        ]
                    ],
                    [
                        'id' => 'text_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<div style="max-width: 800px; margin: 30px auto;"><div style="padding: 15px; margin: 10px 0; border-left: 4px solid var(--e-global-color-secondary);">✓ Професионални педагози с дългогодишен опит</div><div style="padding: 15px; margin: 10px 0; border-left: 4px solid var(--e-global-color-secondary);">✓ Индивидуален подход към всяко дете</div><div style="padding: 15px; margin: 10px 0; border-left: 4px solid var(--e-global-color-secondary);">✓ Малки групи за максимално внимание</div><div style="padding: 15px; margin: 10px 0; border-left: 4px solid var(--e-global-color-secondary);">✓ Доказани методики за развитие на математическото мислене</div><div style="padding: 15px; margin: 10px 0; border-left: 4px solid var(--e-global-color-secondary);">✓ Уютна и стимулираща среда за учене</div></div>'
                        ]
                    ]
                ]
            ]
        ]
    ],
    [
        'id' => 'program_' . uniqid(),
        'elType' => 'section',
        'settings' => [
            'background_background' => 'classic',
            'background_color' => 'var(--e-global-color-background)',
            'padding' => [
                'unit' => 'px',
                'top' => '60',
                'right' => '20',
                'bottom' => '60',
                'left' => '20',
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => 'col_' . uniqid(),
                'elType' => 'column',
                'settings' => ['_column_size' => 100],
                'elements' => [
                    [
                        'id' => 'heading_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Нашата 5-степенна програма',
                            'align' => 'center',
                            'header_size' => 'h2',
                            'title_color' => 'var(--e-global-color-primary)'
                        ]
                    ],
                    [
                        'id' => 'text_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 40px;"><div style="background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid var(--e-global-color-secondary);"><h3 style="color: var(--e-global-color-primary); margin-bottom: 10px;">Ниво 1: Начална Група</h3><p style="color: var(--e-global-color-accent); font-weight: 600;">Възраст: 4-5 години</p><ul style="margin-top: 15px;"><li>Основи на броенето</li><li>Разпознаване на числа</li><li>Прости математически игри</li><li>Развитие на логическото мислене</li></ul></div><div style="background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid var(--e-global-color-secondary);"><h3 style="color: var(--e-global-color-primary); margin-bottom: 10px;">Ниво 2: Средна Група</h3><p style="color: var(--e-global-color-accent); font-weight: 600;">Възраст: 5-6 години</p><ul style="margin-top: 15px;"><li>Събиране и изваждане</li><li>Сравнение на числа</li><li>Геометрични фигури</li><li>Решаване на задачи</li></ul></div><div style="background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid var(--e-global-color-secondary);"><h3 style="color: var(--e-global-color-primary); margin-bottom: 10px;">Ниво 3: Напреднала Група</h3><p style="color: var(--e-global-color-accent); font-weight: 600;">Възраст: 6-7 години</p><ul style="margin-top: 15px;"><li>Умножение и деление</li><li>Работа с дроби</li><li>Сложни задачи</li><li>Пространствено мислене</li></ul></div><div style="background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid var(--e-global-color-secondary);"><h3 style="color: var(--e-global-color-primary); margin-bottom: 10px;">Ниво 4: Майсторска Група</h3><p style="color: var(--e-global-color-accent); font-weight: 600;">Възраст: 7-8 години</p><ul style="margin-top: 15px;"><li>Алгебра и уравнения</li><li>Геометрия</li><li>Логически задачи</li><li>Подготовка за състезания</li></ul></div><div style="background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid var(--e-global-color-secondary);"><h3 style="color: var(--e-global-color-primary); margin-bottom: 10px;">Ниво 5: Олимпиадна Група</h3><p style="color: var(--e-global-color-accent); font-weight: 600;">Възраст: 8+ години</p><ul style="margin-top: 15px;"><li>Олимпиадни задачи</li><li>Комбинаторика</li><li>Математически доказателства</li><li>Участие в състезания</li></ul></div></div>'
                        ]
                    ]
                ]
            ]
        ]
    ],
    [
        'id' => 'testimonials_' . uniqid(),
        'elType' => 'section',
        'settings' => [
            'background_background' => 'classic',
            'background_color' => '#ffffff',
            'padding' => [
                'unit' => 'px',
                'top' => '60',
                'right' => '20',
                'bottom' => '60',
                'left' => '20',
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => 'col_' . uniqid(),
                'elType' => 'column',
                'settings' => ['_column_size' => 100],
                'elements' => [
                    [
                        'id' => 'heading_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Какво казват родителите',
                            'align' => 'center',
                            'header_size' => 'h2',
                            'title_color' => 'var(--e-global-color-primary)'
                        ]
                    ],
                    [
                        'id' => 'text_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;"><div style="background: var(--e-global-color-background); padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"><p style="font-style: italic; color: var(--e-global-color-text); margin-bottom: 20px; font-size: 16px;">"Детето ми се развива невероятно! Преди се страхуваше от математиката, а сега с нетърпение чака часовете в Светлинки. Благодарим на прекрасния екип!"</p><p style="color: var(--e-global-color-primary); font-weight: 600;">- Мария П., майка на ученик от Ниво 2</p></div><div style="background: var(--e-global-color-background); padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"><p style="font-style: italic; color: var(--e-global-color-text); margin-bottom: 20px; font-size: 16px;">"Индивидуалният подход и професионализмът на учителите са изключителни. Синът ми подобри значително резултатите си в училище."</p><p style="color: var(--e-global-color-primary); font-weight: 600;">- Георги И., баща на ученик от Ниво 4</p></div><div style="background: var(--e-global-color-background); padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"><p style="font-style: italic; color: var(--e-global-color-text); margin-bottom: 20px; font-size: 16px;">"Малките групи позволяват на всяко дете да получи нужното внимание. Дъщеря ми обича математиката благодарение на Светлинки!"</p><p style="color: var(--e-global-color-primary); font-weight: 600;">- Елена Д., майка на ученик от Ниво 3</p></div></div>'
                        ]
                    ]
                ]
            ]
        ]
    ],
    [
        'id' => 'contact_' . uniqid(),
        'elType' => 'section',
        'settings' => [
            'background_background' => 'classic',
            'background_color' => 'var(--e-global-color-background)',
            'padding' => [
                'unit' => 'px',
                'top' => '60',
                'right' => '20',
                'bottom' => '60',
                'left' => '20',
                'isLinked' => false
            ]
        ],
        'elements' => [
            [
                'id' => 'col_' . uniqid(),
                'elType' => 'column',
                'settings' => ['_column_size' => 100],
                'elements' => [
                    [
                        'id' => 'heading_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Свържете се с нас',
                            'align' => 'center',
                            'header_size' => 'h2',
                            'title_color' => 'var(--e-global-color-primary)'
                        ]
                    ],
                    [
                        'id' => 'text_' . uniqid(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px;"><div><h3 style="color: var(--e-global-color-primary); margin-bottom: 20px;">Контактна информация</h3><p style="margin: 15px 0;"><strong>Телефон:</strong> +359 XXX XXX XXX</p><p style="margin: 15px 0;"><strong>Email:</strong> info@svetlinki.bg</p><p style="margin: 15px 0;"><strong>Адрес:</strong> София, България</p><p style="margin: 15px 0;"><strong>Работно време:</strong><br>Понеделник - Петък: 9:00 - 18:00<br>Събота: 10:00 - 14:00</p></div><div><h3 style="color: var(--e-global-color-primary); margin-bottom: 20px;">Форма за контакт</h3><p style="color: var(--e-global-color-text); font-style: italic;">Моля, свържете се с нас чрез телефон или email. Очакваме Вашето запитване!</p></div></div>'
                        ]
                    ]
                ]
            ]
        ]
    ]
];

// Convert to JSON for Elementor
$elementor_data_json = json_encode($elementor_data, JSON_UNESCAPED_UNICODE);

// Update the post meta
update_post_meta($page_id, '_elementor_data', $elementor_data_json);
update_post_meta($page_id, '_elementor_edit_mode', 'builder');
update_post_meta($page_id, '_elementor_template_type', 'wp-page');

// Clear Elementor cache if available
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
}

echo "SUCCESS!\n";
echo "Page ID: $page_id\n";
echo "Page URL: http://svetlinkielementor.local/home/\n";
echo "Elementor Editor URL: http://svetlinkielementor.local/wp-admin/post.php?post=$page_id&action=elementor\n";
echo "\nAll 5 sections created:\n";
echo "1. Hero Section (with heading, text, stats, CTA button)\n";
echo "2. Why Choose Us Section\n";
echo "3. 5-Level Program Section\n";
echo "4. Testimonials Section\n";
echo "5. Contact Section\n";
echo "\nGlobal Colors used:\n";
echo "- var(--e-global-color-primary) for headings\n";
echo "- var(--e-global-color-secondary) for accents and buttons\n";
echo "- var(--e-global-color-background) for section backgrounds\n";
echo "- var(--e-global-color-text) for text content\n";
echo "- var(--e-global-color-accent) for highlights\n";
?>
