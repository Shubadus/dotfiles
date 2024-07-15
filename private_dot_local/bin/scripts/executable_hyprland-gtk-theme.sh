#!/bin/bash
active_border=$(grep -oP -m 1 'accent_bg_color \K.*\)' .config/gtk-3.0/gtk.css)
inactive_border=$(grep -oP -m 1 'view_bg_color \K.*\)' .config/gtk-3.0/gtk.css)
hyprctl keyword general:col.active_border $active_border # $active_border 45deg
hyprctl keyword general:col.inactive_border $inactive_border # $inactive_border 45deg
