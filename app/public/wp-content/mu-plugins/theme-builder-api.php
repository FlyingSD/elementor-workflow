<?php
/**
 * Plugin Name: Theme Builder API
 * Description: Custom REST API endpoints for Theme Builder setup
 */

add_action('rest_api_init', function () {
    // Get post meta endpoint
    register_rest_route('theme-builder/v1', '/meta/(?P<id>\d+)/(?P<key>[a-zA-Z0-9_-]+)', [
        'methods' => 'GET',
        'callback' => 'tb_get_post_meta',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
        'args' => [
            'id' => [
                'validate_callback' => function($param) {
                    return is_numeric($param);
                }
            ],
        ],
    ]);

    // Update post meta endpoint
    register_rest_route('theme-builder/v1', '/meta/(?P<id>\d+)', [
        'methods' => 'POST',
        'callback' => 'tb_update_post_meta',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
    ]);

    // Analyze homepage endpoint
    register_rest_route('theme-builder/v1', '/analyze/(?P<id>\d+)', [
        'methods' => 'GET',
        'callback' => 'tb_analyze_page',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
    ]);

    // Remove duplicates endpoint
    register_rest_route('theme-builder/v1', '/remove-duplicates/(?P<id>\d+)', [
        'methods' => 'POST',
        'callback' => 'tb_remove_duplicates',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
    ]);

    // Setup Theme Builder endpoint
    register_rest_route('theme-builder/v1', '/setup', [
        'methods' => 'POST',
        'callback' => 'tb_setup_theme_builder',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
    ]);

    // Clear cache endpoint
    register_rest_route('theme-builder/v1', '/clear-cache', [
        'methods' => 'POST',
        'callback' => 'tb_clear_cache',
        'permission_callback' => function() {
            return current_user_can('edit_posts');
        },
    ]);
});

function tb_get_post_meta($request) {
    $post_id = $request['id'];
    $meta_key = $request['key'];

    $value = get_post_meta($post_id, $meta_key, true);

    return [
        'success' => true,
        'post_id' => $post_id,
        'meta_key' => $meta_key,
        'value' => $value,
    ];
}

function tb_update_post_meta($request) {
    $post_id = $request['id'];
    $body = $request->get_json_params();

    $updated = [];
    foreach ($body as $key => $value) {
        $result = update_post_meta($post_id, $key, $value);
        $updated[$key] = $result;
    }

    return [
        'success' => true,
        'post_id' => $post_id,
        'updated' => $updated,
    ];
}

function tb_analyze_page($request) {
    $post_id = $request['id'];

    $elementor_data = get_post_meta($post_id, '_elementor_data', true);

    if (empty($elementor_data)) {
        return [
            'success' => false,
            'message' => 'No Elementor data found',
        ];
    }

    $data = json_decode($elementor_data, true);

    $analysis = [
        'total_sections' => count($data),
        'sections' => [],
    ];

    foreach ($data as $index => $section) {
        $section_info = [
            'index' => $index,
            'type' => $section['elType'] ?? 'unknown',
            'id' => $section['id'] ?? '',
            'columns' => count($section['elements'] ?? []),
        ];

        // Try to identify section by content
        if (isset($section['elements']) && is_array($section['elements'])) {
            $widgets = [];
            foreach ($section['elements'] as $column) {
                if (isset($column['elements']) && is_array($column['elements'])) {
                    foreach ($column['elements'] as $widget) {
                        $widgets[] = $widget['widgetType'] ?? $widget['elType'] ?? 'unknown';
                    }
                }
            }
            $section_info['widgets'] = $widgets;
        }

        $analysis['sections'][] = $section_info;
    }

    return [
        'success' => true,
        'post_id' => $post_id,
        'analysis' => $analysis,
    ];
}

function tb_remove_duplicates($request) {
    $post_id = $request['id'];
    $body = $request->get_json_params();
    $sections_to_remove = $body['sections_to_remove'] ?? [];

    $elementor_data = get_post_meta($post_id, '_elementor_data', true);

    if (empty($elementor_data)) {
        return [
            'success' => false,
            'message' => 'No Elementor data found',
        ];
    }

    $data = json_decode($elementor_data, true);
    $original_count = count($data);

    // Remove sections by index (reverse order to maintain indices)
    rsort($sections_to_remove);
    foreach ($sections_to_remove as $index) {
        if (isset($data[$index])) {
            array_splice($data, $index, 1);
        }
    }

    // Update the post meta
    $updated = update_post_meta($post_id, '_elementor_data', wp_slash(json_encode($data)));

    return [
        'success' => $updated !== false,
        'post_id' => $post_id,
        'original_sections' => $original_count,
        'remaining_sections' => count($data),
        'removed_count' => $original_count - count($data),
    ];
}

function tb_setup_theme_builder($request) {
    $body = $request->get_json_params();
    $header_id = $body['header_id'] ?? 69;
    $footer_id = $body['footer_id'] ?? 73;

    $results = [];

    // Configure Header
    update_post_meta($header_id, '_elementor_template_type', 'header');
    update_post_meta($header_id, '_elementor_location', 'header');
    update_post_meta($header_id, '_elementor_conditions', ['include/general']);
    $results['header'] = [
        'id' => $header_id,
        'configured' => true,
    ];

    // Configure Footer
    update_post_meta($footer_id, '_elementor_template_type', 'footer');
    update_post_meta($footer_id, '_elementor_location', 'footer');
    update_post_meta($footer_id, '_elementor_conditions', ['include/general']);
    $results['footer'] = [
        'id' => $footer_id,
        'configured' => true,
    ];

    return [
        'success' => true,
        'message' => 'Theme Builder configured successfully',
        'results' => $results,
    ];
}

function tb_clear_cache($request) {
    $results = [];

    // Clear Elementor cache
    if (class_exists('\Elementor\Plugin')) {
        \Elementor\Plugin::$instance->files_manager->clear_cache();
        $results['elementor'] = 'Cache cleared';
    } else {
        $results['elementor'] = 'Elementor not found';
    }

    // Clear WordPress transients
    delete_transient('elementor_remote_info_api_data_');

    return [
        'success' => true,
        'results' => $results,
    ];
}
