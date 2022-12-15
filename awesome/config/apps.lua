local string = string

local apps = {}

apps.audiocontrol = "pavucontrol"
apps.browser = "firefox"
apps.terminal = "alacritty"
apps.filemanager = "pcmanfm"
apps.mediaplayer = "/var/lib/flatpak/exports/bin/com.spotify.Client"
apps.launcher = "rofi -show drun"
apps.taskmanager = string.format("%s -e btop", apps.terminal)
apps.lock = "i3lock -c 000000"

return apps
