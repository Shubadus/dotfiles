#!/bin/bash

source "$CONFIG_DIR/plugins/resources.sh"

# IS_VPN=$(/usr/local/bin/piact)
CURRENT_WIFI="$(ipconfig getsummary en0)"
IP_ADDRESS="$(echo "$CURRENT_WIFI" | grep -o "yiaddr = .*" | sed 's/^yiaddr = //')"
SSID="$(echo "$CURRENT_WIFI" | grep -o "SSID : .*" | sed 's/^SSID : //' | tail -n 1)"

sketchybar --set "$NAME" \
  icon="$NET_WIFI" \
  label="$SSID"
