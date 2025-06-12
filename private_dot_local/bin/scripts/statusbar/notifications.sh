#!/bin/bash
notification_normal="󰂚"
# notification_alert="󰂚"
notification_dnd="󰂛"

function get_notifications {
  dnd=$(dunstctl get-pause-level)
  msg_count=$(dunstctl count history)
  if [[ $dnd -eq 100 ]]; then
    icon=$notification_dnd
    printf '{"text":"%s", "tooltip":"%s Notifications", "alt":"%s", "class": "dnd"}' "$icon" "$msg_count" "$notification_alert"
  elif [[ $msg_count -gt 0 ]]; then
    icon=$notification_normal
    printf '{"text":"%s %s", "tooltip":"%s Notifications", "alt":"%s", "class": "alert"}' "$icon" "$msg_count" "$msg_count" "$notification_alert"
  else
    icon=$notification_normal
    printf '{"text":"%s", "tooltip":"%s Notifications", "alt":"%s"}' "$icon" "$msg_count" "$notification_alert"
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
