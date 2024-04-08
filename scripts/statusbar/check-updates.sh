#!/bin/bash
arch_icon='󰣇'
flatpak_icon=''

get_arch_updates() {
  # yay -Sy
  # count=$(checkupdates | wc -l)
  count=$(dnf check-update -q | grep -c '^[a-z0-9]')
  # count=$(yay -Qu | wc -l)
  if [ $count -gt 0 ]; then
    printf '{ "text": "%s", "tooltip": "%s", "class": "", "percentage": "" }' "$arch_icon $count" "$count updates available"
  else
    printf '{ "text": "", "tooltip": "", "class": "", "percentage": "" }'
  fi
}

get_flatpak_updates() {
  count=$(flatpak remote-ls --updates | wc -l)

  if [ $count -gt 0 ]; then
    printf '{ "text": "%s", "tooltip": "%s", "class": "", "percentage": "" }' "$flatpak_icon $count" "$count updates available"
  else
    printf '{ "text": "", "tooltip": "", "class": "", "percentage": "" }'
  fi
}

start_arch_updates() {
  notify-send \
    -a "arch-updates" \
    -c update \
    -u normal \
    "Arch\AUR updates" \
    "Starting Arch and AUR updates" 

  alacritty -e yay -Syu

}

start_flatpak_updates() {
  notify-send \
    -a "flatpak-updates" \
    -c update \
    -u normal \
    "Flatpak updates" \
    "Starting Flatpak updates"

  alacritty -e flatpak update -y
}


case "$1" in
  check-arch)
    get_arch_updates
  ;;
  check-flatpak)
    get_flatpak_updates
  ;;
  update-arch)
    start_arch_updates
  ;;
  update-flatpak)
    start_flatpak_updates
  ;;
  *)
    get_arch_updates
  ;;
esac
# done
exit 0
