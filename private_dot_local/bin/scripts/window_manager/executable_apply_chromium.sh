#!/usr/bin/env bash
source ~/.local/bin/scripts/window_manager/chromium_colors.sh
chromium --no-startup-window --set-theme-color="$color" >/dev/null 2>&1
