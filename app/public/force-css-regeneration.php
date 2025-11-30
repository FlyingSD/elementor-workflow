<?php
/**
 * Force Elementor CSS Regeneration After REST API Updates
 *
 * PROBLEM: CSS changes work in editor but don't show on frontend
 * CAUSE: REST API updates don't trigger wp_enqueue_scripts
 * SOLUTION: Force frontend rendering to regenerate CSS
 *
 * Usage:
 *   php force-css-regeneration.php 21
 *   php force-css-regeneration.php 21 23 25  (multiple pages)
 *
 * Research: Elementor GitHub Issues #4464, #7237, #27300, #31594
 */

require_once(__DIR__ . '/wp-load.php');

/**
 * Force Elementor CSS regeneration for a specific post
 *
 * @param int $post_id The post ID to regenerate CSS for
 * @return array|WP_Error Success data or error
 */
function force_elementor_css_regeneration($post_id) {
    if (!did_action('elementor/loaded')) {
        return new WP_Error('elementor_not_loaded', 'Elementor plugin not loaded');
    }

    // Verify post exists and has Elementor data
    $elementor_data = get_post_meta($post_id, '_elementor_data', true);
    if (empty($elementor_data)) {
        return new WP_Error('no_elementor_data', "Post {$post_id} has no Elementor data");
    }

    echo "Processing post {$post_id}...\n";

    // Step 1: Clear CSS cache (deletes CSS files)
    echo "  - Clearing CSS cache...\n";
    \Elementor\Plugin::$instance->files_manager->clear_cache();

    // Step 2: Force frontend rendering to regenerate CSS
    // This triggers wp_enqueue_scripts which regenerates CSS
    echo "  - Forcing CSS regeneration...\n";
    $frontend = \Elementor\Plugin::$instance->frontend;
    $content = $frontend->get_builder_content_for_display($post_id, true);

    // Step 3: Verify CSS file was created
    $uploads_dir = wp_upload_dir();
    $css_file = $uploads_dir['basedir'] . "/elementor/css/post-{$post_id}.css";

    if (file_exists($css_file)) {
        $file_size = filesize($css_file);
        $modified_time = date('Y-m-d H:i:s', filemtime($css_file));

        // Read first few lines to verify it's not empty/corrupt
        $css_content = file_get_contents($css_file);
        $line_count = substr_count($css_content, "\n");

        // Check if Global Colors are present
        $has_global_colors = strpos($css_content, 'var(--e-global-color-') !== false;

        echo "  ✅ CSS regenerated successfully!\n";
        echo "     File: {$css_file}\n";
        echo "     Size: {$file_size} bytes\n";
        echo "     Lines: {$line_count}\n";
        echo "     Modified: {$modified_time}\n";
        echo "     Global Colors: " . ($has_global_colors ? 'YES ✅' : 'NO ❌') . "\n";

        return [
            'success' => true,
            'post_id' => $post_id,
            'file' => $css_file,
            'size' => $file_size,
            'lines' => $line_count,
            'modified' => $modified_time,
            'has_global_colors' => $has_global_colors
        ];
    } else {
        echo "  ❌ ERROR: CSS file not created!\n";
        return new WP_Error('css_not_generated', "CSS file not created for post {$post_id}");
    }
}

/**
 * Verify CSS is accessible via HTTP
 *
 * @param int $post_id The post ID
 * @return bool True if CSS is accessible
 */
function verify_css_accessible($post_id) {
    $site_url = get_site_url();
    $css_url = "{$site_url}/wp-content/uploads/elementor/css/post-{$post_id}.css";

    echo "  - Verifying CSS URL: {$css_url}\n";

    $response = wp_remote_get($css_url);

    if (is_wp_error($response)) {
        echo "  ❌ HTTP Error: " . $response->get_error_message() . "\n";
        return false;
    }

    $status_code = wp_remote_retrieve_response_code($response);
    $body = wp_remote_retrieve_body($response);

    if ($status_code === 200 && !empty($body)) {
        echo "  ✅ CSS accessible via HTTP (Status: {$status_code})\n";
        return true;
    } else {
        echo "  ❌ CSS not accessible (Status: {$status_code})\n";
        return false;
    }
}

// ============================================================================
// CLI Execution
// ============================================================================

if (php_sapi_name() === 'cli') {
    echo "\n";
    echo "==================================================\n";
    echo "Elementor CSS Regeneration Tool\n";
    echo "==================================================\n";
    echo "\n";

    // Get post IDs from command line arguments
    $post_ids = array_slice($argv, 1);

    if (empty($post_ids)) {
        echo "Usage: php force-css-regeneration.php <post_id> [post_id2] [post_id3] ...\n";
        echo "\n";
        echo "Examples:\n";
        echo "  php force-css-regeneration.php 21\n";
        echo "  php force-css-regeneration.php 21 23 25 27 29\n";
        echo "\n";
        exit(1);
    }

    $success_count = 0;
    $error_count = 0;
    $results = [];

    foreach ($post_ids as $post_id) {
        $post_id = (int)$post_id;

        if ($post_id <= 0) {
            echo "❌ Invalid post ID: {$post_id}\n\n";
            $error_count++;
            continue;
        }

        $result = force_elementor_css_regeneration($post_id);

        if (is_wp_error($result)) {
            echo "❌ ERROR: " . $result->get_error_message() . "\n";
            $error_count++;
        } else {
            // Verify HTTP accessibility
            verify_css_accessible($post_id);
            $success_count++;
            $results[] = $result;
        }

        echo "\n";
    }

    // Summary
    echo "==================================================\n";
    echo "Summary\n";
    echo "==================================================\n";
    echo "Total posts: " . count($post_ids) . "\n";
    echo "Successful: {$success_count} ✅\n";
    echo "Failed: {$error_count} ❌\n";
    echo "\n";

    if ($success_count > 0) {
        echo "Next steps:\n";
        echo "1. Clear browser cache\n";
        echo "2. Visit your pages on frontend\n";
        echo "3. Verify styles are showing correctly\n";
        echo "\n";
    }

    exit($error_count > 0 ? 1 : 0);
}

// ============================================================================
// Function API (for use in other scripts)
// ============================================================================

// If included from another PHP file, functions are available:
// - force_elementor_css_regeneration($post_id)
// - verify_css_accessible($post_id)
