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

browser() {
  xdg-open $@
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

packages_menu() {
  case $(dmenu "Pacman - List\nPacman - Update\nFlatpak - List\nFlatpak - Update\nFlatpak - Repos") in
  *Pacman*List*) terminal "yay -Qe | less" ;;
  *Pacman*Update*) terminal "yay; read -p 'Press Enter to Close'" ;;
  *Flatpak*Update*) terminal "flatpak update; read -p 'Press Enter to Close'" ;;
  *Flatpak*List*) terminal "flatpak list --app --columns=name,version | less -R" ;; #; read -p 'Press Enter to Close'" ;;
  *Flatpak*Repos*) terminal "flatpak remotes --columns=title,url | less -R" ;;
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

theme_menu() {
  case $(dmenu "Set Theme\nSet Background") in
  *) menu ;;
  esac
}

web_search_menu() {
  result="$(dmenu "Youtube\nMaps")"
  case "$result" in
  *Youtube*)
    result=$(fuzzel --dmenu --prompt-only="YT Videos: " | sed "s/ /+/")
    if [[ "$result" ]]; then
      xdg-open "https://youtube.com/results?search_query=$result"
    fi
    ;;
  *Maps*)
    result=$(fuzzel --dmenu --prompt-only="Destination: " | sed "s/,/%2C/")
    if [[ "$result" ]]; then
      xdg-open "https://google.com/maps/dir/?api=1&destination=$result"
    fi
    ;;
  "") menu ;;
  *) xdg-open "https://google.com/search?q=$(echo "$result" | sed "s/ /+/g")" ;;
  esac
}

menu() {
  case $(dmenu "Calculator\nPackages\nSet Theme\nSet Background\nWeb Search") in
  *Packages*) packages_menu ;;
  *Theme*)
    result=$(exec $HOME/.local/bin/scripts/window_manager/set-theme.sh)
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
  # *Theme*) theme_menu ;;
  *Web*) web_search_menu ;;
  *Calculator*) notify-send $(echo "$(fuzzel --dmenu --prompt-only="Calc: ")" | bc -l) ;;
  esac
}

menu
