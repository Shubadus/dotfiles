#!/usr/bin/env bash
_print_waybar_message() {
  json="{\"alt\":\"$1\", \
    "\"text\":\"$2"\", \
    "\"tooltip\":\"$3"\", \
    "\"class\":\"$4"\", \
    "\"percentage\":\"$5"\"}"
  printf "%s\n" "$json" | jq
}

count-history() {
  dnd_level="$(dunstctl get-pause-level)"
  count="$(dunstctl count history)"
  if [[ "$dnd_level" -gt 1 ]]; then
    _print_waybar_message "dnd-none" "" "$count" "dnd" ""
  elif [[ "$count" -gt 0 ]]; then
    _print_waybar_message "notification" "$count" "$count Notifications" "alert" ""
  else
    _print_waybar_message "none" "" "$count Notifications" "" ""
  fi
}

show-history() {
  dunst_history=$(dunstctl history)
  # readarray -t history <<<($(dunstctl history | jq '.data[][] | .summary.data, .id.data'))
  # history=()
  history=($(echo "$dunst_history" | jq '.data[][] | .summary.data, .id.data'))
  options=""
  # printf "${history[@]}"
  for ((i = 0; i < ${#history[@]}; i += 2)); do
    options+="${history[$i]} ${history[$1 + 1]}\n"
  done
  echo "$options"
  result=$(printf "$options" | fuzzel --dmenu --anchor top-left --index --minimal-lines -n notification-history)
  dunstctl history-pop "$(result | awk "{print $NF}")"
  dunstctl history-pop "${history[$1 + 1]}"
}

toggle-dnd() {
  dnd_level="$(dunstctl get-pause-level)"
  if [[ "$dnd_level" -gt 1 ]]; then
    dunstctl set-pause-level 0
  else
    dunstctl set-pause-level 1
  fi
}

while getopts "scdr" opt; do
  case "$opt" in
  s) show-history ;;
  c) count-history ;;
  r) dunstctl history-clear ;;
  d) toggle-dnd ;;
  esac

done
