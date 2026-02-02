#!/usr/bin/env bash
color="{{ colors.surface.default.red }}, {{ colors.surface.default.green}}, {{ colors.surface.default.blue}}"
chromium --no-startup-window --set-theme-color="$color" >/dev/null 2>&1
