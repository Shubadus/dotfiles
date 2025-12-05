#!/usr/bin/env bash
dmenu() {
  local anchor=${2:-"top"}
  local width=${3:-"14"}
  local namespace=${4:-"menu"}
  printf "$1" | fuzzel \
    --dmenu \
    --minimal-lines \
    --anchor=$anchor \
    --namespace=$namespace
}

terminal() {
  if [[ $(whereis foot) ]]; then
    exec foot --app-id=float -e bash -c "$@"
  elif [[ $(whereis alacritty) ]]; then
    exec alacritty --class=float -e bash -c "$@"
  elif [[ $(whereis ghostty) ]]; then
    exec ghostty --class=float -e bash -c "$@"
  fi
}

arch_packages() {
  case $(dmenu "Pacman Add\nAUR Add\nRemove\n") in
  *Pacman*Add*) terminal ~/.local/bin/scripts/window_manager/packages/pacman_install ;;
  *AUR*Add*) terminal ~/.local/bin/scripts/window_manager/packages/aur_install ;;
  *Remove*) terminal ~/.local/bin/scripts/window_manager/packages/pacman_remove ;;
  *) packages ;;
  esac
}

flatpak_packages() {
  case $(dmenu "Add\nRemove\n") in
  *Pacman*Add*) terminal ~/.local/bin/scripts/window_manager/packages/pacman_install ;;
  *AUR*Add*) terminal ~/.local/bin/scripts/window_manager/packages/aur_install ;;
  *Remove*) terminal ~/.local/bin/scripts/window_manager/packages/pacman_remove ;;
  *) packages ;;
  esac
}

packages() {
  # case $(dmenu "󰣇  Pacman - List\n󰣇  Pacman - Update\n  Flatpak - List\n  Flatpak - Update\n  Flatpak - Repos") in
  case $(dmenu "󰣇  Arch\n  Flatpak\n󰣇  Update\n") in
  *Arch*) arch_packages ;;
  *Flatpak*) flatpak_packages ;;
  *Update*)
    result=$(terminal ~/.local/bin/scripts/update.sh)
    if [[ "$?" -ne 0 ]]; then
      packages
    fi
    ;;
  *) menu ;;
  esac
}

power_menu() {
  result=$(exec $HOME/.local/bin/scripts/window_manager/powermenu.sh)
  if [[ "$?" -ne 0 ]]; then
    echo "powermenu script manually exited, returning back to main menu"
    menu
  fi
}

web_search_menu() {
  result="$(dmenu "󰗃  Youtube\n󰗵  Google Maps")"
  case "$result" in
  *Youtube*)
    result=$(fuzzel --dmenu --prompt-only="󰗃 " | sed "s/ /+/")
    if [[ "$result" ]]; then
      xdg-open "https://youtube.com/results?search_query=$result"
    else
      web_search_menu
    fi
    ;;
  *Maps*)
    result=$(fuzzel --dmenu --prompt-only="󰗵 " | sed "s/,/%2C/")
    if [[ "$result" ]]; then
      xdg-open "https://google.com/maps/dir/?api=1&destination=$result"
    else
      web_search_menu
    fi
    ;;
  "") util_menu ;;
  *) xdg-open "https://google.com/search?q=$(echo "$result" | sed "s/ /+/g")" ;;
  esac
}
niri_menu() {
  case $(dmenu " Focus Window\n List Windows\n󰍺 List Monitors") in
  *Focus*Window*)
    result=$(~/.local/bin/scripts/window_manager/niri/niri_windows.py)
    if [[ "$?" -ne 0 ]]; then
      niri_menu
    fi
    ;;
  *List*Windows*)
    terminal "niri msg windows | less"
    ;;
  *List*Monitors*)
    terminal "niri msg outputs | less"
    ;;
  *) menu ;;
  esac
}

util_menu() {
  prompt="󰃬  Calculator\n󰜏  Web Search"
  result=$(dmenu "$prompt")
  case $result in
  *Calculator*)
    result=$(notify-send $(echo "$(fuzzel --dmenu --prompt-only="Calc: ")" | bc -l))
    if [[ "$?" -ne 0 ]]; then
      util_menu
    fi
    ;;
  *Web*Search*)
    web_search_menu
    if [[ "$?" -ne 0 ]]; then
      util_menu
    fi
    ;;
  *) menu ;;
  esac
}

menu() {
  if [[ "$XDG_CURRENT_DESKTOP" -eq "niri" ]]; then
    prompt="󰏓  Packages\n  Niri\n󰸉  Set Background\n  Utils"
  elif [[ "$XDG_CURRENT_DESKTOP" -eq "hyprland" ]]; then
    prompt="󰏓  Packages\n  Hyprland\n󰸉  Set Background\n  Utils"
  fi
  result=$(dmenu "$prompt")
  case $result in
  *Packages*)
    result=$(packages)
    if [[ "$?" -ne 0 ]]; then
      menu
    fi
    ;;
  *Background*)
    result=$(exec $HOME/.local/bin/scripts/window_manager/set-background.sh)
    if [[ "$?" -ne 0 ]]; then
      menu
    fi
    ;;
  *Settings*)
    result=$(settings_menu)
    if [[ "$?" -ne 0 ]]; then
      menu
    fi
    ;;
  *Niri*) niri_menu ;;
  *Hyprland*)
    result=$(~/.local/bin/scripts/window_manager/niri/niri_windows.py)
    if [[ "$?" -ne 0 ]]; then
      menu
    fi
    ;;
  *Utils*) util_menu ;;
  *=*)
    calc=${result/"="/""}
    calc_result=$(echo "$calc" | bc -l)
    wl-copy "$calc_result"
    notify-send -a "Menu" "Calculator Result: $calc_result" "Saved to clipboard."
    ;;
  !*)
    web_search=${result/"!"/""}
    web_search=${web_search/" "/"+"}
    xdg-open "https://google.com/search?q=$web_search"
    ;;
  esac
}

menu
