#!/bin/bash
active_border=$(grep -oP -m 1 'accent_bg_color \K.*\)' .config/gtk-3.0/gtk.css)
active_border_rgb_values=$(echo "$active_border" | sed -E 's/rgba\(([0-9]+), ([0-9]+), ([0-9]+), [0-9.]+\)/\1 \2 \3/')
active_border_hex=$(printf "rgba(%02x%02x%02xaa)" $active_border_rgb_values)
inactive_border=$(grep -oP -m 1 'view_bg_color \K.*\)' .config/gtk-3.0/gtk.css)
inactive_border_rgb_values=$(echo "$inactive_border" | sed -E 's/rgba\(([0-9]+), ([0-9]+), ([0-9]+), [0-9.]+\)/\1 \2 \3/')
inactive_border_hex=$(printf "rgba(%02x%02x%02xaa)" $inactive_border_rgb_values)
hyprctl keyword general:col.active_border $active_border_hex
hyprctl keyword general:col.inactive_border $inactive_border_hex
