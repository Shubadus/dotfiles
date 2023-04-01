#!/bin/bash

# This script requires dnsutils aka bind to fetch the WAN IP address

# Shows the connections names
# nmcli connection show --active | grep 'ethernet' | awk '{ print $1 }' FS='  '
# nmcli connection show --active | grep 'wifi' | awk '{ print $1 }' FS='  '

# Show ethernet interface name
# nmcli connection show --active | grep 'ethernet' | awk '{ print $6 }' FS=' '

# Show wifi interface name
# nmcli connection show --active | grep 'wifi' | awk '{ print $4 }' FS=' '
function getEth {
  echo "$(nmcli connection show --active | grep 'ethernet')"
}

function getWifi {
  echo "$(nmcli connection show --active | grep 'wifi')"
}

function ShowInfo {
	if [ "$(nmcli connection show --active | grep -oh "\w*ethernet\w*")" == "ethernet" ]; then
		wan="$(dig +short myip.opendns.com @resolver1.opendns.com)"
		connection="Interface: $(getEth | awk '{ print $6 }' FS=' ')
    SSID: $(getEth | awk '{ print $1 }' FS='  ') 
    IP Address: $(nmcli -t -f IP4.ADDRESS dev show $(getEth | awk '{ print $6 }' FS=' ') | awk '{print $2}' FS='[:/]')
    WAN IP: $wan"
	elif [ "$(nmcli connection show --active | grep -oh "\w*wifi\w*")" == "wifi" ]; then
		wan="$(dig +short myip.opendns.com @resolver1.opendns.com)"
		connection="Interface: $(getWifi | awk '{ print $4 }' FS=' ')
    SSID:       $(getWifi | awk '{ print $1 }' FS='  ') 
    IP Address: $(nmcli -t -f IP4.ADDRESS dev show $(getWifi | awk '{ print $4 }' FS=' ') | awk '{print $2}' FS='[:/]')
    WAN IP:     $wan"
	else
		connection="No active connection."
	fi
	dunstify -i "network-idle" "$connection" -r 1234
}

function IconUpdate() {
	if [ "$(nmcli connection show --active | grep -oh "\w*ethernet\w*")" == "ethernet" ]; then
		icon=" "
	elif [ "$(nmcli connection show --active | grep -oh "\w*wifi\w*")" == "wifi" ]; then
    sigstr=$(nmcli -f IN-USE,SIGNAL,SSID device wifi | awk '/^\*/{if (NR!=1) {print $2}}')
    if [ sigstr > 0 && sigstr =< 25]; then
      icon="󰤯" 
    elif [ sigstr > 25 && sigstr =< 50]; then
      icon="󰤢"
    elif [ sigstr > 50 && sigstr =< 75]; then
      icon="󰤥"
    elif [ sigstr > 75 ]; then
      icon="󰤨 "
    fi
	else
		icon=" "
	fi
	printf "%s" "$icon"
}

if [ "$1" = "ShowInfo" ]; then
	ShowInfo
else
	IconUpdate	
fi
