#!/bin/bash
declare -A material_darker

# Uses ARGB format
# Material Darker
md_bg="0xcc212121"
md_fg="0xffB0BEC5"
md_text="0xff727272"
md_sel_bg="0xcc404040"
md_sel_fg="0xffFFFFFF"
md_btn="0xff2a2a2a"
md_bg_alt="0xff292929"
md_disabled="0xff474747"
md_contrast="0xff1a1a1a"
md_active="0xff323232"
md_border="0xff292929"
md_highlight="0xff3f3f3f"
md_tree="0xc0323232"
md_notif="0xff1a1a1a"
md_accent="0xffff9800"
md_excluded_files="0xff323232"

md_green="0xffc3e88db"
md_yellow="0xffffcb6b"
md_blue="0xff82aaff"
md_red="0xfff07178"
md_purple="0xffc792ea"
md_orange="0xfff78c6c"
md_cyan="0xff89ddff"
md_gray="0xff616161"
md_white="0xffeeffff"
md_error="0xffff5370"

# Colors

TEXT=$md_sel_fg
ACTIVE=$md_cyan
BACKGROUND=$md_bg
GREEN=$md_green
YELLOW=$md_yellow
ORANGE=$md_orange
CYAN=$md_cyan
GRAY=$md_gray
WHITE=$md_white
ERROR=$md_error

# Icons
NET_AIRPLANE="󰀝"
NET_WIFI=""         # Wi-Fi connected
NET_HOTSPOT=􀉤        # iPhone Wi-Fi hotspot connected
NET_USB="󰕓"          # iPhone USB hotspot connected
NET_THUNDERBOLT=􀒗    # Thunderbolt bridge connected
NET_DISCONNECTED="󰌙" # Network disconnected, but Wi-Fi turned on
NET_OFF=􀙈            # Network disconnected, Wi-Fi turned off
