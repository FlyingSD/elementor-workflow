<?php
/**
 * Elementor Global Colors Polyfill for FREE version
 *
 * Problem: Elementor FREE doesn't generate global.css with CSS custom properties
 * Solution: Manually output Global Colors as CSS variables in <head>
 *
 * @package Svetlinki
 * @since 1.0.0
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Output Svetlinki Global Colors as CSS custom properties
 *
 * Since Elementor FREE doesn't store colors in a retrievable way via API,
 * we hardcode the design system colors here as a centralized source of truth.
 *
 * This allows:
 * - Using CSS variables in Elementor JSON: var(--e-global-color-primary)
 * - Client can update colors by editing this file (better than scattered hardcoding)
 * - Single source of truth for design system
 */
add_action('wp_head', 'svetlinki_elementor_global_colors_polyfill', 1);

function svetlinki_elementor_global_colors_polyfill() {
    // Only output on frontend pages
    if (is_admin()) {
        return;
    }

    // Svetlinki Design System Colors (from SSOT documentation)
    $colors = array(
        'primary'   => '#FABA29',  // Yellow/Gold - Buttons, counters, accents
        'secondary' => '#4F9F8B',  // Teal/Green - Headings, primary text highlights
        'text'      => '#2C2C2C',  // Dark Gray - Body text
        'accent'    => '#FEFCF5',  // Warm Cream - Backgrounds, sections
        'coral'     => '#FF8C7A',  // Coral - Subtle accents in modern design
    );

    // Output CSS variables
    echo "\n<!-- Elementor Global Colors Polyfill (FREE version) -->\n";
    echo '<style id="elementor-global-colors-polyfill">';
    echo ':root {';

    foreach ($colors as $name => $value) {
        echo "--e-global-color-{$name}: {$value};";
    }

    echo '}';
    echo '</style>';
    echo "\n<!-- /Elementor Global Colors Polyfill -->\n";
}

/**
 * Future Enhancement: If we upgrade to Elementor Pro, replace this with:
 *
 * $kit_id = get_option('elementor_active_kit');
 * $kit_settings = get_post_meta($kit_id, '_elementor_page_settings', true);
 * $custom_colors = isset($kit_settings['custom_colors']) ? $kit_settings['custom_colors'] : [];
 *
 * Then loop through $custom_colors to output CSS variables dynamically.
 */
