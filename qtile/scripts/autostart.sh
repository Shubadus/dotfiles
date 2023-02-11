#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Find out your monitor name with xrandr or arandr (save and you get this line)
autorandr -c

# Run fehbg to restore background image
run $HOME/.fehbg

#starting utility applications at boot time
run nm-applet # Run Network Manager applet
run xfce4-power-manager # Run Power Manager
# run variety
# run remmina -i
# run 1password --silent
run picom --config $HOME/.config/qtile/scripts/picom.conf # Run compositor
run /usr/libexec/polkit-gnome-authentication-agent-1 # Polkit for authentication
run /usr/bin/dunst -conf $HOME/.config/dunst/dunstrc # Notifications

if pgrep packagekitd;
  then
    pkill packagekitd
fi
