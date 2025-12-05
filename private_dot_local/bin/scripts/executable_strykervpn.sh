#!/bin/sh
url="vpn.stryker.com"
site="USA Michigan"

while getopts "st" opt; do
  case $opt in
  s)
    vpn=$(pgrep gpclient)
    if [[ $vpn ]]; then
      echo "On"
    else
      echo "Off"
    fi
    ;;
  t)
    vpn=$(pgrep gpclient)
    if [ -z $vpn ]; then
      # INFO: Launch browser for SAML Auth
      notify-send -a "GlobalProtect VPN" "GlobalProtect VPN Starting" "Opening SAML Authentication in browser window.\nURL: ${url}\nSite: ${site}"
      cookie=$(gpauth --fix-openssl "$url" 2>/dev/null)
      # INFO: Pass SAML token to gpclient and disown process
      if [ -z "$cookie" ]; then
        notify-send -a "GlobalProtect VPN" "GlobalProtect VPN Cancelled" "SAML Authentication was cancelled, exiting."
        exit 1
      else
        echo "$cookie" | pkexec gpclient --fix-openssl \
          connect "$url" -g "$site" --cookie-on-stdin \
          --csd-wrapper "/usr/lib/openconnect/hipreport.sh"
        if [ $? -ne 0 ]; then
          notify-send -a "GlobalProtect VPN" "GlobalProtect VPN Failed" "Failed to connect"
        else
          notify-send -a "GlobalProtect VPN" "GlobalProtect VPN Connected" "Connected to ${url} via ${site}"
        fi
      fi
    else
      # INFO: Kill existing gpclient process
      notify-send -a "GlobalProtect VPN" "GlobalProtect VPN Disconnect" "Closing connection to ${url}"
      pkexec pkill gpclient
    fi
    ;;
  *) ;;
  esac
done
exit 0
