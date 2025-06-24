#!/bin/bash
function get_notifications {
  dnd=$(dunstctl get-pause-level)
  msg_count=$(dunstctl count history)
  if [[ $dnd -eq 100 ]]; then
    printf '{"text":"%s", "tooltip":"%s Notifications", "alt":"dnd-none", "class": "dnd"}' "$msg_count" "$msg_count"
  elif [[ $msg_count -gt 0 ]]; then
    printf '{"text":"%s","tooltip":"%s Notifications", "alt":"notification", "class": "alert"}' "$msg_count" "$msg_count"
  else
    printf '{"text":"%s","tooltip":"%s Notifications", "alt":"none"}' "$msg_count" "$msg_count"
  fi
}
for arg in "$@"; do
  [[ "${arg:0:1}" = '-' ]] || continue

  case "$1" in

  -c | --count)
    get_notifications
    ;;
  -t | --toggle-panel)
    # swaync-client --toggle
    dunstctl history-pop
    ;;
  -d | --toggle-dnd)
    # swaync-client --toggle-dnd
    dunstctl set-paused toggle
    ;;
  -r | --remove-history)
    dunstctl history-clear
    ;;
  esac
done

exit 0
