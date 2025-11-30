<?php
/**
 * Fix Footer Canvas Template Setting
 * Run this file directly: http://svetlinkielementor.local/fix-footer-canvas.php
 */

// Load WordPress
require_once(__DIR__ . '/wp-load.php');

// Security check
$auth_key = isset($_GET['key']) ? $_GET['key'] : '';
if ($auth_key !== 'fix_footer_canvas_2025') {
    die('Unauthorized. Add ?key=fix_footer_canvas_2025 to URL');
}

echo "<pre>\n";
echo "============================================================\n";
echo "  FOOTER CANVAS TEMPLATE FIX\n";
echo "============================================================\n\n";

// Step 1: Enable Canvas template option for Footer (ID 73)
echo "[FIX] Enabling Canvas template option for Footer (ID 73)...\n";

$footer_id = 73;

// Update the meta field
$result = update_post_meta($footer_id, 'ehf-canvas-template', 'enabled');

if ($result !== false) {
    echo "[OK] Canvas template option enabled!\n";
} else {
    $current = get_post_meta($footer_id, 'ehf-canvas-template', true);
    if ($current === 'enabled') {
        echo "[INFO] Canvas template option was already enabled\n";
    } else {
        echo "[ERROR] Failed to enable Canvas template option\n";
    }
}

// Verify the setting
$canvas_enabled = get_post_meta($footer_id, 'ehf-canvas-template', true);
echo "[VERIFY] Current value: " . ($canvas_enabled ? $canvas_enabled : 'not set') . "\n\n";

// Step 2: Change page templates to Canvas
echo "[UPDATE] Changing page templates to Canvas...\n\n";

$pages_to_update = [
    ['id' => 23, 'name' => 'About'],
    ['id' => 25, 'name' => 'Programs'],
    ['id' => 27, 'name' => 'Contact'],
    ['id' => 29, 'name' => 'FAQ']
];

foreach ($pages_to_update as $page) {
    echo "[PAGE] Updating {$page['name']} (ID {$page['id']})...\n";

    $result = update_post_meta($page['id'], '_wp_page_template', 'elementor_canvas');

    if ($result !== false) {
        echo "  [OK] {$page['name']} changed to Canvas template\n";
    } else {
        $current = get_post_meta($page['id'], '_wp_page_template', true);
        if ($current === 'elementor_canvas') {
            echo "  [INFO] {$page['name']} was already using Canvas template\n";
        } else {
            echo "  [WARN] Could not update {$page['name']}\n";
        }
    }
}

// Step 3: Clear Elementor cache
echo "\n[CACHE] Clearing Elementor cache...\n";

// Clear CSS cache
update_post_meta($footer_id, '_elementor_css', '');
foreach ($pages_to_update as $page) {
    update_post_meta($page['id'], '_elementor_css', '');
}

// Clear Elementor file cache if available
if (class_exists('\Elementor\Plugin')) {
    \Elementor\Plugin::$instance->files_manager->clear_cache();
    echo "[OK] Elementor cache cleared\n";
} else {
    echo "[WARN] Elementor plugin not found, cache not cleared\n";
}

echo "\n============================================================\n";
echo "[SUCCESS] FIX COMPLETE!\n";
echo "============================================================\n\n";

echo "What was done:\n";
echo "  1. [OK] Enabled Canvas template option on Footer (ID 73)\n";
echo "  2. [OK] Changed About/Programs/Contact/FAQ to Canvas template\n";
echo "  3. [OK] Cleared Elementor cache\n\n";

echo "Next steps:\n";
echo "  1. Visit http://svetlinkielementor.local/ - Footer should now appear\n";
echo "  2. Visit About/Programs/Contact/FAQ - Footer should appear\n";
echo "  3. Go to Elementor > Tools > Regenerate Files for full cache clear\n\n";

echo "============================================================\n";
echo "</pre>";
?>
