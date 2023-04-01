from pathlib import Path

from libqtile import lazy

qtile_scripts = Path.home().joinpath('.local','bin')
statusbar_scripts = Path.home().joinpath('.local','bin','statusbar')

apps = dict()

# Audio
apps['audio_gui']           = "pavucontrol"
apps['audio_cli']           = "pactl"
apps['audio_player_cli']    = "playerctl"
apps['audio_player_toggle'] = f"{apps['audio_player_cli']} play-pause"
apps['audio_player_next']   = f"{apps['audio_player_cli']} next"
apps['audio_player_prev']   = f"{apps['audio_player_cli']} previous"
apps['audio_mute']          = f"{apps['audio_cli']} set-sink-mute @DEFAULT_SINK@ toggle"
apps['audio_up']            = f"{apps['audio_cli']} set-sink-volume @DEFAULT_SINK@ +5%"
apps['audio_down']          = f"{apps['audio_cli']} set-sink-volume @DEFAULT_SINK@ -5%"

# Assorted CLI apps
apps['autostart']           = f"{qtile_scripts}/autostart"

# Brightness
apps['brightness']          = "light"
apps['brightness_up']       = f"{apps['brightness']} -A 10"
apps['brightness_down']     = f"{apps['brightness']} -U 10"

apps['pass_man']            = "flatpak run com.onepassword.OnePassword"
apps['pass_man_main']       = f"{apps['pass_man']} --toggle"
apps['pass_man_launcher']   = f"{apps['pass_man']} --quick-access"

# Gui Applications
apps['browser']             = "qutebrowser"
apps['terminal']            = "alacritty"
apps['launcher']            = "krunner"
apps['launcher']            = "rofi -show drun"
apps['logout']              = "archlinux-logout"
apps['network_manager']     = "nm-connection-editor"
apps['screenshot']          = "flameshot gui"
apps['wallpaper']           = "nitrogen"
apps['wallpaper_restore']   = f"{apps['wallpaper']} --restore"

# Flatpak Applications
apps['power_manager']       = "flatpak run com.github.d4nj1.tlpui"

# Terminal Applications
apps['filemanager']         = f"{apps['terminal']} -e ranger"
apps['sysmonitor']          = f"{apps['terminal']} -e btop"

# Scripts
apps['lock']                = f"{qtile_scripts}/lock -s 5"
apps['picom_toggle']        = f"{qtile_scripts}/picom-toggle"
apps['suspend']             = f"{qtile_scripts}/suspend"

# Qtile bar polling
apps['qtile_bat']           = f"{statusbar_scripts}/battery.py"
apps['qtile_cal']           = f"{statusbar_scripts}/calendar.sh"
apps['qtile_cal_show']      = f"{apps['qtile_cal']} show"
apps['qtile_net']           = f"{statusbar_scripts}/network.sh"
apps['qtile_net_show']      = f"{apps['qtile_net']} ShowInfo"
apps['qtile_vol']           = f"{statusbar_scripts}/volumecontrol"
apps['qtile_vol_show']      = f"{apps['qtile_vol']} show"
apps['qtile_vol_down']      = f"{apps['qtile_vol']} down"
apps['qtile_vol_mute']      = f"{apps['qtile_vol']} mute"
apps['qtile_vol_up']        = f"{apps['qtile_vol']} up"

# Qtile bar apps
  
