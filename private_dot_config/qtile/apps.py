from pathlib import Path

from libqtile import lazy

qtile_scripts = Path.home().joinpath('.local','bin','scripts')
statusbar_scripts = Path.home().joinpath('.local','bin','scripts','statusbar')

apps = dict()

apps['pkg_mngr']            = "yay"
apps['pkg_mngr_update']     = f"{apps['pkg_mngr']} -Syu"


# Audio
apps['audio_gui']           = "pavucontrol"
apps['audio_player_cli']    = "playerctl"
apps['audio_player_toggle'] = f"{apps['audio_player_cli']} play-pause"
apps['audio_player_next']   = f"{apps['audio_player_cli']} next"
apps['audio_player_prev']   = f"{apps['audio_player_cli']} previous"
apps['audio_cli']           = f"{statusbar_scripts}/volumecontrol"
apps['audio_down']          = f"{apps['audio_cli']} down"
apps['audio_up']            = f"{apps['audio_cli']} up"
apps['audio_mute']          = f"{apps['audio_cli']} mute"

# Assorted CLI apps
apps['autostart']           = f"{qtile_scripts}/autostart"

# Brightness
apps['brightness']          = f"{statusbar_scripts}/brightnesscontrol"
apps['brightness_up']       = f"{apps['brightness']} up"
apps['brightness_down']     = f"{apps['brightness']} down"

apps['pass_man']            = "1password"
apps['pass_man_main']       = f"{apps['pass_man']} --toggle"
apps['pass_man_launcher']   = f"{apps['pass_man']} --quick-access"

apps['xorg']                = {}
apps['wayland']             = {}

# Gui Applications
apps['browser']             = "qutebrowser"
# apps['terminal']            = "alacritty"
apps['terminal']            = "foot"
apps['network_manager']     = "nm-connection-editor"
apps['vpn']                 = "/opt/cisco/anyconnect/bin/vpnui"

apps['wayland']['launcher']   = 'wofi'
apps['wayland']['logout']     = "wlogout"
# apps['wayland']['screenshot'] = 'grim -g "$(slurp)"'
apps['wayland']['screenshot'] = f"{qtile_scripts}/screenshot"
apps['wayland']['lock']       = "swaylock"
apps['wayland']['monitors']   = 'pkill kanshi; kanshi'

apps['xorg']['launcher']    = 'rofi -show drun'
apps['xorg']['logout']      = 'archlinux-logout'
apps['xorg']['screenshot']  = "flameshot gui"
apps['xorg']['lock']        = "i3lock"
apps['xorg']['monitors']    = 'autorandr -c'

# Flatpak Applications
apps['power_manager']       = "flatpak run com.github.d4nj1.tlpui"
apps['spotify']             = "flatpak run com.spotify.Client"

# Terminal Applications
apps['filemanager']         = f"{apps['terminal']} -e ranger"
apps['sysmonitor']          = f"{apps['terminal']} -e btop"

# Scripts
# apps['lock']                = f"{qtile_scripts}/lock -s 5"
# apps['lock']                = "loginctl lock-session"
apps['picom_toggle']        = f"{qtile_scripts}/picom-toggle"
apps['suspend']             = f"{qtile_scripts}/suspend"

# Qtile bar polling
apps['bat']                 = f"{statusbar_scripts}/battery.py"
apps['bat_right']           = f"{apps['bat']} right-click"

# apps['cal']                 = f"{statusbar_scripts}/calendar.sh"
# apps['cal_show']            = f"{apps['cal']} show"
apps['cal']                 = "gsimplecal"
apps['cal_show']            = f"{apps['cal']}"

apps['net']                 = f"{statusbar_scripts}/network.sh"
apps['net_show']            = f"{apps['net']} ShowInfo"

apps['vol']                 = f"{statusbar_scripts}/volumecontrol"
apps['vol_show']            = f"{apps['vol']} show"
apps['vol_down']            = f"{apps['vol']} down"
apps['vol_mute']            = f"{apps['vol']} mute"
apps['vol_up']              = f"{apps['vol']} up"

apps['idle_inhibit']        = f"{statusbar_scripts}/idle-inhibit"
apps['idle_toggle']         = f"{apps['idle_inhibit']} toggle"

# apps['videobridge']         = "flatpak run xwaylandvideobridge"

# Updates
apps['update_flatpak']      = f"{apps['terminal']} -e flatpak update -y"
apps['update_pkg_mngr']     = f"{apps['terminal']} -e {apps['pkg_mngr_update']}"

