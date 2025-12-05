#!/usr/bin/env bash
batteries=()
readarray -d '' batteries < <(find /sys/class/power_supply/* -print0)

for battery in "${batteries[@]}"; do
  echo "Battery: $battery"
done
