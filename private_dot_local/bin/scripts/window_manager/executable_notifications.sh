#!/usr/bin/env bash
dmenu() {
  printf "$1" | fuzzel \
    --dmenu \
    --minimal-lines \
    --anchor=top-left \
    --namespace=notification-history
  # --width=$2
}

_print_waybar_message() {
  json="{\"alt\":\"$1\", \
    "\"text\":\"$2"\", \
    "\"tooltip\":\"$3"\", \
    "\"class\":\"$4"\", \
    "\"percentage\":\"$5"\"}"
  printf "%s\n" "$json"
}

count-history() {
  dnd_level="$(dunstctl get-pause-level)"
  count="$(dunstctl count history)"
  if [[ "$dnd_level" -gt 0 && "$count" -gt 0 ]]; then
    _print_waybar_message "dnd-none" "" "$count" "alert" ""
  elif [[ "$dnd_level" -gt 0 ]]; then
    _print_waybar_message "dnd-none" "" "$count" "none" ""
  elif [[ "$count" -gt 0 ]]; then
    _print_waybar_message "notification" "$count" "$count Notifications" "alert" ""
  else
    _print_waybar_message "none" "" "$count Notifications" "none" ""
  fi
}

show-history() {
  dunst_history=$(dunstctl history)
  history=($(echo "$dunst_history" | jq '.data[][] | .summary.data, .id.data'))
  options=""
  longest_string=""
  # printf "${history[@]}"
  for ((i = 0; i < ${#history[@]}; i += 2)); do
    if [[ "${#history}" -gt "$longest_string" ]]; then
      longest_string="${#history}"
    fi
    options+="${history[$i]} ${history[$1 + 1]}\n"
  done
  width=$(echo "$longest_string-40" | bc)
  printf "$options"
  echo "Running Fuzzel"
  result=$(dmenu "$options" "$width")
  printf "Result:\n$result\n"
  if [[ -z "$result" ]]; then
    dunstctl history-pop "$(echo $result | awk "{print $NF}")"
  fi
  # dunstctl history-pop "${history[$1 + 1]}"
}

toggle-dnd() {
  dnd_level="$(dunstctl get-pause-level)"
  if [[ "$dnd_level" -gt 0 ]]; then
    echo "DND is active, turning off"
    dunstctl set-pause-level 0
  else
    echo "DND is not active, turning on"
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
