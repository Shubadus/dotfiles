#!/usr/bin/env bash
color="{{ colors.surface_container_low.default.red }}, {{ colors.surface_container_low.default.green}}, {{ colors.surface_container_low.default.blue}}"
chromium --no-startup-window --set-theme-color="$color" >/dev/null 2>&1
