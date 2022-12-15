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

#starting utility applications at boot time
run cassowary &
# run variety &
run nm-applet & # Run Network Manager applet
# run lxsession --session=qtile &
run volumeicon &
# TODO: Look at changing this to a builtin qtile widget
run xfce4-power-manager & # Run Power Manager
numlockx on &
# blueberry-tray &
run 1password --silent &
run picom --config $HOME/.config/qtile/scripts/picom.conf & # Run compositor
run /usr/libexec/polkit-gnome-authentication-agent-1 & # Polkit for authentication
run /usr/bin/dunst -conf $HOME/.config/dunst/dunstrc & # Notifications

# if pgrep packagekitd;
#   then
#     pkill packagekitd
# fi
