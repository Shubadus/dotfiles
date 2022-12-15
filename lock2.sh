#!/bin/bash
#TODO: Add swaylock support

function get_screen_shutoff()
{
  if [[ $session == "x11" ]]; then
    echo "xset s activate"
  else
    echo ""
  fi
}

lock_command="$(command -v 'i3lock') -B 10 -kn --time-color=ffffff --date-color=ffffff"
session=$(echo $XDG_SESSION_TYPE)
screen_off=$(get_screen_shutoff)

$lock_command 

