#!/usr/bin/env bash

options="  Shutdown\n󰒲  Suspend\n   Restart\n󰌾   Lock\n   Logout\n󰤄   Hibernate\n   Cancel"
rofi_command="fuzzel --dmenu -w 11 --minimal-lines -a top-right --hide-prompt"
case "$(echo -e "$options" | $rofi_command)" in
*Shutdown*) exec systemctl poweroff ;;
*Suspend*)
  exec systemctl suspend
  exec loginctl lock-session
  ;;
*Restart*) exec systemctl reboot ;;
*Logout*) exec loginctl terminate-user $USER ;;
*Lock*) exec loginctl lock-session ;;
*Hibernate*) exec systemctl hibernate ;;
*Cancel*) exec killall fuzzel ;;
*) exit 1 ;;
esac
