#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
# Use Autorandr to autodetect  t-1
run autorandr -c
run numlockx on
run unclutter -root
run nm-applet
run xfce4-power-manager
run /usr/libexec/polkit-gnome-authentication-agent-1
run picom --config $HOME/.config/awesome/scripts/picom.conf

