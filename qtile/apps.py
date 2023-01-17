from pathlib import Path

# rofi_path = Path.home().joinpath(".config","rofi","bin")
qtile_scripts = Path.home().joinpath('.config','qtile','scripts')
apps = dict(
    audio = "pavucontrol",
    autostart = f"{qtile_scripts}/autostart.sh",
    browser = "qutebrowser",
    terminal = "alacritty", #"kitty",
    launcher = "rofi -show drun",
    lock = f"{qtile_scripts}/lock.sh",
    network_manager = "nm-connection-editor",
    suspend = f"{qtile_scripts}/suspend.sh",
    screenshot = "flameshot gui"
)
apps['filemanager'] = f"{apps['terminal']} -e ranger"
apps['sysmonitor'] = f"{apps['terminal']} -e btop"

 
