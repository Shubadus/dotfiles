#!/bin/bash
wallpaper_cache=$XDG_CACHE_HOME/wallpaper
mkdir -p $wallpaper_cache
selected_wallpaper=$(alacritty --class float -e ranger --choosefile=/tmp/selected_wallpaper ~/Pictures/Wallpapers/ && cat /tmp/selected_wallpaper)
cp $selected_wallpaper $wallpaper_cache/wallpaper -f
swww img $wallpaper_cache/wallpaper
