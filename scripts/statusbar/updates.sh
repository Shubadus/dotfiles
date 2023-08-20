#! /bin/bash
#TODO: Look at moving icons to waybar config
update_icon="󰚰"
reboot_icon="󰜉"
# Classes: updates, no_updates, reboot
function check_pkg_mngr {
  if [ -x "$(command -v apt)" ]; then echo "apt"
  elif [ -x "$(command -v dnf)" ]; then echo "dnf"
  elif [ -x "$(command -v pacman)" ]; then echo "pacman"
}

function check_updates {
  reboot=$(reboot_check)
  pkg_mng_updates="$(($(dnf list updates -q | wc -l) - 1))"
  if [ "$(($pkg_mng_updates + 0))" -gt 0 ]; then
    # Subtract one to account for the first line in dnf which isn't an application with an update.
    printf '{"text":"%s","tooltip":"DNF Updates: %s","class":"updates", "percentage": 50}' "$update_icon $pkg_mng_updates" "$pkg_mng_updates"
    notify-send "You have ${pkg_mng_updates} update(s) available."
  elif [ ! -z "$reboot" ]; then
    printf '{"text":"%s","tooltip":"A reboot is required to complete this update","class":"reboot", "percentage": 100}' "$reboot_icon"
    notify-send "A reboot is required to complete your updates."
  else
    printf '{"text":"","tooltip":"","class":"no_updates", "percentage": 0}'
  fi
}

function reboot_check {
  if [ $pkg_mngr == "apt" ]; then
    # [ -f /var/run/reboot-required ] && cat /var/run/reboot-required
    echo $() 
  elif [ $pkg_mngr == "dnf" ]; then
    echo $(dnf needs-restarting -r | grep "Reboot is required")
  elif [ $pkg_mngr == "pacman" ]; then
    # $(pacman -Q linux | cut -d " " -f 2) > $(uname -r)
    echo $()
}

function update_system {
  # Start DNF update
  notify-send "Beginning software updates."
  if [ $pkg_mngr == "apt" ]; then
    pkexec apt upgrade -y
  elif [ $pkg_mngr == "dnf" ]; then
    pkexec dnf update -y
  elif [ $pkg_mngr == "pacman" ]; then
    yes | pkexec pacman -Syu
  notify-send "Software updates complete."
}

function update_flatpak {
  notify-send "Beginning flatpak software updates."
  flatpak update -y 
  notify-send "Flatpak updates complete."
}

pkg_mngr=$(check_pkg_mngr)

case "$1" in
  --update-system)
    update_system
  ;;
  --update-flatpak)
    update_flatpak
  ;;
  --check-updates)
    check_updates
  ;;
esac
# done
exit 0
