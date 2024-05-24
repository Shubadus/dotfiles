import os
import subprocess

from libqtile import extension
from libqtile.lazy import lazy
from libqtile.config import Key, Drag

from apps import apps
from style import theme

# dmenu = extension.J4DmenuDesktop(
#     dmenu_ignorecase=True,
#     dmenu_lines=15,
#     dmenu_prompt=">",
#     # dmenu_font="NotoSans Nerd Font",
#     **theme
# )

DESKTOP_SESSION = os.environ['XDG_SESSION_TYPE']

@lazy.function
def cycle_windows(qtile, index=1):
    windows = extension.window_list(qtile) # get the list of windows
    if windows: # check if the list is not empty
        current = qtile.current_window # get the current window
        next_index = (windows.index(current) + index) % len(windows) # get the index of the next window
        next_window = windows[next_index] # get the next window
        next_window.focus(warp=True) # focus the next window and warp the pointer to it

mod_keys = dict(
    mod = "mod4",
    mod1 = "mod1",
    mod2 = "control"
)

@lazy.function
def next_screen(qtile):
    qtile.cmd_next_screen()

@lazy.function
def prev_screen(qtile):
    qtile.cmd_prev_screen()

@lazy.function
def spawn_with_cmds(command):
    subprocess.call(command)

@lazy.function
def cmd_spawn(qtile, command):
    qtile.cmd_spawn(command)

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod_keys["mod"]], "f", lazy.window.toggle_fullscreen(),
        desc="Fullscreen current window"),
    Key([], "F11", lazy.window.toggle_fullscreen(),
        desc="Fullscreen current window"),
    Key([mod_keys["mod"]], "m", lazy.window.toggle_maximize(),
        desc="Maximize current window"),
    Key([mod_keys["mod"]], "q", lazy.window.kill(),
        desc="Close current window"),
    Key([mod_keys["mod"]], "Return", lazy.spawn(apps["terminal"]),
        desc=f"Launch {apps['terminal']} terminal"),
    Key([mod_keys["mod2"], "shift"], "escape", lazy.spawn(apps["sysmonitor"]),
        desc=f"Launch {apps['terminal']} terminal"),
    Key([mod_keys["mod2"], "shift"], "l", lazy.spawn(apps['wayland']["lock"]),
        desc="Lock the screen"),

    # SUPER + SHIFT KEYS
    Key([mod_keys["mod"], "shift"], "q", lazy.window.kill(),
        desc="Close current window"),
    Key([mod_keys["mod"], "shift"], "r", lazy.reload_config(),
        desc="Reload qtile config"),
    Key([mod_keys["mod"], "shift"], "p", lazy.spawn(apps['picom_toggle']),
        desc="Toggle Picom"),

    Key([mod_keys["mod1"]], "Tab", lazy.group.next_window()),
    Key([mod_keys["mod1"], "shift"], "Tab", lazy.group.prev_window()),

    # Applications
    Key([mod_keys["mod"], "shift"], "d", lazy.spawn(apps['wayland']['launcher']),
        desc="Launch app launcher"),
    # Key([mod_keys["mod"], "shift"], "d", lazy.run_extension(dmenu)),
    Key([mod_keys["mod"], "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle("dropdown_ranger")),
    Key([mod_keys["mod"], "shift"], "b", lazy.spawn(apps["browser"]),
        desc=f"Launch {apps['browser']} web browser"),
    Key([mod_keys["mod"], "shift"], "s", lazy.spawn(apps['wayland']["screenshot"]),
        desc=f"Take a screenshot"),
    Key([mod_keys["mod"]], "x", lazy.spawn(apps['wayland']["logout"]),
        desc=f"Logout"),
    Key([mod_keys["mod2"], "shift"], "space", lazy.spawn(apps['pass_man_launcher']),
        desc=f"Launch {'pass_man'} --quick access"),
    # Key([mod_keys["mod2"], "shift"], "space", lazy.group['scratchpad'].dropdown_toggle('pass_man'),
    #     desc=f"Launch {'pass_man'} --quick access"),

    # QTILE LAYOUT KEYS
    Key([mod_keys["mod"]], "n", lazy.layout.normalize()),
    Key([mod_keys["mod"]], "space", lazy.next_layout(),
        desc="Cycle next layout"),

    # CHANGE FOCUS
    Key([mod_keys["mod"]], "k", lazy.layout.up()),
    Key([mod_keys["mod"]], "j", lazy.layout.down()),
    Key([mod_keys["mod"]], "h", lazy.layout.left()),
    Key([mod_keys["mod"]], "l", lazy.layout.right()),

    # Move between screens
    Key([mod_keys["mod1"]], "l", next_screen()),
    Key([mod_keys["mod1"]], "h", prev_screen()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod_keys["mod"], "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod_keys["mod"], "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod_keys["mod"], "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ), Key([mod_keys["mod"], "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # FLIP LAYOUT FOR MONADTALL/MONADWIDE

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod_keys["mod"], "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod_keys["mod"], "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod_keys["mod"], "shift"], "h", lazy.layout.swap_left()),
    Key([mod_keys["mod"], "shift"], "l", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod_keys["mod"], "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle floating layout"),

    # Audio and Media controls
    Key([], 'XF86AudioMute', lazy.spawn(apps['audio_mute'])),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn(apps['audio_up'])),
    Key([], 'XF86AudioLowerVolume', lazy.spawn(apps['audio_down'])),
    Key([], 'XF86AudioPlay', lazy.spawn(apps['audio_player_toggle'])),
    Key([], 'XF86AudioNext', lazy.spawn(apps['audio_player_next'])),
    Key([], 'XF86AudioPrev', lazy.spawn(apps['audio_player_prev'])),

    # Brightness control
    Key([], 'XF86MonBrightnessUp', lazy.spawn(apps['brightness_up'])),
    Key([], 'XF86MonBrightnessDown', lazy.spawn(apps['brightness_down'])),

    # Scratchpads
    Key([], "F12",
        lazy.group["scratchpad"].dropdown_toggle("dropdown_term")),
    Key([], "F10", lazy.group["scratchpad"].dropdown_toggle("network_manager")),
    Key([], "F9", lazy.group["scratchpad"].dropdown_toggle("audio")),
    Key([], "F8", lazy.group["scratchpad"].dropdown_toggle("vpn")),
    Key([], "F7", lazy.group["scratchpad"].dropdown_toggle("spotify")),
    Key([mod_keys["mod2"], "shift"], "escape",
        lazy.group["scratchpad"].dropdown_toggle("sysmonitor")),
]

mouse = [
    Drag([mod_keys["mod"]], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod_keys["mod"]], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

