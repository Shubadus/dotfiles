#!/bin/bash
clients=$(hyprctl clients)
# for i v in $clients; do
#   echo "${i%:} $v";
# done
selection=$(echo "$clients" | grep "Window" | fuzzel --dmenu | awk '{print $2}')
echo "$clients" | grep -A 24 "$selection" #| awk '{print $2}'
