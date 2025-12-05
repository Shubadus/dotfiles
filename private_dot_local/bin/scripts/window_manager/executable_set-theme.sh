#!/usr/bin/env bash
theme_list=$(wallust -s theme list | sed "s/- //;s/\s\(.*\)//;s/^.*\w\:.*//;s/list//")
selection=$(printf "$theme_list" | fuzzel --dmenu --minimal-lines --anchor="top" --namespace="menu")
echo "$selection"
if [[ -z "$selection" ]]; then
  exit 1
fi

notify-send "Setting new theme: $selection"

niri msg do-screen-transistion

echo "Setting Wallust Theme"
wallust -s theme "$selection"

echo "Generating GTK theme from wallust-gtk tmp file"
oomox-cli /tmp/wallust-gtk >/dev/null 2>&1

echo "Re-Applying GTK theme"
nwg-look -a >/dev/null 2>&1

# echo "Apply GTK theme to flatpak"
# flatpak override --user --filesystem=$HOME/.themes
# gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
# flatpak override --user --env=GTK_THEME=oomox-wallust-gtk

echo "Applying theme to Omarchy Chromium fork"
source ~/.local/bin/scripts/window_manager/chromium_colors.sh
chromium --no-startup-window --set-theme-color="$color" >/dev/null 2>&1

echo "Applying Dunst theme"
dunstctl reload >/dev/null 2>&1 &

echo "Restarting Waybar"
pkill waybar
waybar >/dev/null 2>&1 &
disown

# TODO:
