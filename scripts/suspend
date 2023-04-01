#!/bin/bash
#
lock_command="i3lock -B 10 -kn --time-color=ffffff --date-color=ffffff"

get_suspend_cmd () {
  if [[ $XDG_SESSION_TYPE == "x11" ]]; then
    systemctl suspend
    # echo "xset dpms force suspend"
  else
    echo ""
  fi
}

$lock_command & sleep 5 && systemctl suspend &
