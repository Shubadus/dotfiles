#!/bin/bash
notification_normal="󰂚"
notification_alert="󰵙"
notification_dnd="󰂛"

for arg in "$@"; do
  [[ "${arg:0:1}" = '-' ]] || continue

  case "$1" in

    -c | --count)
      printf '{"text":"%s"}' "$(swaync-client --count)"
      ;;
    -t | --toggle-panel)
      swaync-client --toggle
      ;;
    -d | --toggle-dnd)
      swaync-client --toggle-dnd
      ;;
  esac
done

exit 0
