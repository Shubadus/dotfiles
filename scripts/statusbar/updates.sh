#! /bin/bash
#TODO: Look at moving icons to waybar config
update_icon="󰚰"
reboot_icon="󰜉"
# Classes: updates, no_updates, reboot

function check_updates {
  dnf_updates="$(($(dnf list updates -q | wc -l) - 1))"
  reboot=$(dnf needs-restarting -r | grep "Reboot is required")
  if [ "$(($dnf_updates + 0))" -gt 0 ]; then
    # Subtract one to account for the first line in dnf which isn't an application with an update.
    printf '{"text":"%s","tooltip":"DNF Updates: %s","class":"updates", "percentage": 50}' "$update_icon $dnf_updates" "$dnf_updates"
    notify-send "DNF reports that you have ${dnf_updates} update(s) available."
  elif [ ! -z "$reboot" ]; then
    printf '{"text":"%s","tooltip":"A reboot is required to complete this update","class":"reboot", "percentage": 100}' "$reboot_icon"
    notify-send "A reboot is required to complete your updates."
  else
    printf '{"text":"","tooltip":"","class":"no_updates", "percentage": 0}'
  fi
}

function update_dnf {
  # Start DNF update
  notify-send "Beginning software updates."
  sudo dnf update -y
  notify-send "Software updates complete. Checking if a reboot is required."
}

function update_flatpak {
  notify-send "Beginning flatpak software updates."
  flatpak update -y 
  notify-send "Flatpak updates complete."
}

case "$1" in
  --update-dnf)
    update_dnf
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
