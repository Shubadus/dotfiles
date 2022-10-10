#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
# Use Autorandr to autodetect layout
autorandr -c

run cassowary
run nm-applet
run xfce4-power-manager
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
run numlockx on
run picom --config $HOME/.config/qtile/scripts/picom.conf &
