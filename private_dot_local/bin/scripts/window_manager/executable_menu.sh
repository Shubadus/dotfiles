#!/usr/bin/env bash
dmenu() {
  local anchor=${2:-"top"}
  local width=${3:-"14"}
  local namespace=${4:-"menu"}
  printf "$1" | fuzzel \
    --dmenu \
    --minimal-lines \
    --anchor=$anchor \
    --width=$width \
    --namespace=$namespace
  # --hide-prompt \
}

browser() {
  chromium $@
}
terminal() {
  case "$TERMINAL" in
  *foot*) exec foot --app-id=float -e bash -c "$@" ;;
  *alacritty*) exec alacritty --class=float -e bash -c "$@" ;;
  *ghostty*) exec ghostty --class=float -e bash -c "$@" ;;
  esac
}

audio_menu() {
  result=$(dmenu "Toggle Mute\nVolume Up\nVolume Down\nPavucontrol")
  case "$result" in
  *Mute*) $HOME/.local/bin/scripts/statusbar/volume.py -v mute ;;
  *Set*) $HOME/.local/bin/scripts/statusbar/volume.py -v up ;;
  *Pavucontrol*) exec pavucontrol ;;
  *) menu ;;
  esac
}

flatpak_menu() {
  case $(dmenu "Update\nList Installed\nList Repos") in
  *Update*) terminal "flatpak update; read -p 'Press Enter to Close'" ;;
  *Installed*) terminal "flatpak list --app --columns=name,version; read -p 'Press Enter to Close'" ;;
  *Repos*) terminal "flatpak remotes --columns=title,url | less" ;;
  *) packages_menu ;;
  esac
}

packages_menu() {
  case $(dmenu "Pacman\AUR\nFlatpak") in
  *Pacman*) pacman_menu ;;
  *Flatpak*) flatpak_menu ;;
  *) menu ;;
  esac
}

pacman_menu() {
  case $(dmenu "Update\nList Installed") in
  *Update*) terminal "yay; read -p 'Press Enter to Close'" ;;
  *Installed*) terminal "yay -Qe | less" ;;
  *) packages_menu ;;
  esac
}

power_menu() {
  result=$(exec $HOME/.local/bin/scripts/powermenu)
  if [[ "$?" -ne 0 ]]; then
    echo "powermenu script manually exited, returning back to main menu"
    menu
  fi
}

network_menu() {
  case $(dmenu "Settings\n") in
  *) menu ;;
  esac
}

theme_menu() {
  case $(dmenu "Set Theme\nSet Background") in
  *Theme*)
    local theme_list=$(wallust -s theme list | sed "s/- //;s/\s\(.*\)//;s/^.*\w\:.*//;s/list//")
    selection=$(dmenu "$theme_list")
    echo "$selection"
    if [[ $selection ]]; then
      exec wallust -s theme "$selection"
    fi
    ;;
  *Background*) exec $HOME/.local/bin/scripts/window_manager/set-background.sh ;;
  *) menu ;;
  esac
}

web_search_menu() {
  result=$(dmenu "Youtube\nMaps")
  case $result in
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
  *) xdg-open "https://google.com/search?q=$(echo "$result" | sed "s/ /+/")" ;;
  esac
}

menu() {
  case "$(dmenu "Audio\nCalc\nNetwork\nPackages\nPower\nTheme\nWeb Search")" in
  *Audio*) audio_menu ;;
  *Packages*) packages_menu ;;
  *Power*) power_menu ;;
  *Network*) network_menu ;;
  *Theme*) theme_menu ;;
  *Web*) web_search_menu ;;
  *Calc*) notify-send $(echo "$(fuzzel --dmenu --prompt-only="Calc: ")" | bc -l) ;;
  esac
}

menu
