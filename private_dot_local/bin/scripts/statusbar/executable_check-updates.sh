#!/bin/bash
package_manager_icon='󰏕'
flatpak_icon=''

case "$1" in
  check-packageman)
    count=$(dnf check-update -q | grep -c '^[a-z0-9]')
    # count=$(yay -Qu | wc -l)
    if [ $count -gt 0 ]; then
      printf '{ "text": "%s", "tooltip": "%s", "class": "", "percentage": "" }' "$package_manager_icon $count" "$count updates available"
    else
      printf '{ "text": "", "tooltip": "", "class": "", "percentage": "" }'
    fi
  ;;
  check-flatpak)
    count=$(flatpak remote-ls --updates --app | wc -l)

    if [ $count -gt 0 ]; then
      printf '{ "text": "%s", "tooltip": "%s", "class": "", "percentage": "" }' "$flatpak_icon $count" "$count updates available"
    else
      printf '{ "text": "", "tooltip": "", "class": "", "percentage": "" }'
    fi
  ;;
  update-packageman)
    notify-send \
      -a "Package-manager-updates" \
      -c update \
      -u normal \
      "Package manager updates" \
      "Starting Package manager updates"

    $TERM -e sudo dnf update
  ;;
  update-flatpak)
    notify-send \
      -a "flatpak-updates" \
      -c update \
      -u normal \
      "Flatpak updates" \
      "Starting Flatpak updates"

    $TERM -e flatpak update
  ;;
esac
# done
exit 0
