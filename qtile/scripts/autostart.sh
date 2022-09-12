#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
autorandr -c

# feh --bg-fill $HOME/Pictures/2029165.jpg &

#starting utility applications at boot time
run cassowary &
run variety &
run nm-applet &
run lxsession --session=qtile &
run volumeicon &
numlockx on &
blueberry-tray &
run picom --config $HOME/.config/qtile/scripts/picom.conf &
run /usr/libexec/polkit-gnome-authentication-agent-1 &

