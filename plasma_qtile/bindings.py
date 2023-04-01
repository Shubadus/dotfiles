import subprocess

from libqtile import qtile
from libqtile.command import lazy
from libqtile.config import Key, Drag

from apps import apps

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

@lazy.function
def close(qtile):
    current_window = lazy.window
    if not current_window.info().get('name').startswith("Desktop"):
        current_window.kill()

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod_keys["mod"]], "f", lazy.window.toggle_fullscreen(),
        desc="Fullscreen current window"),
    Key([mod_keys["mod"]], "m", lazy.window.toggle_maximize(),
        desc="Maximize current window"),
    Key([mod_keys["mod"]], "Return", lazy.spawn(apps["terminal"]),
        desc=f"Launch {apps['terminal']} terminal"),
    Key([mod_keys["mod2"], "shift"], "escape", lazy.spawn(apps["sysmonitor"]),
        desc=f"Launch {apps['terminal']} terminal"),

    # SUPER + SHIFT KEYS
    Key([mod_keys["mod"], "shift"], "q", lazy.window.kill(),
        desc="Close current window"),
    Key([mod_keys["mod"], "shift"], "r", lazy.restart(),
        desc="Restart qtile"),
    Key([mod_keys["mod"], "shift"], "p", lazy.spawn(apps['picom_toggle']),
        desc="Toggle Picom"),

    # Applications
    Key([mod_keys["mod"], "shift"], "d", lazy.spawn(apps['launcher']),
        desc="Launch app launcher"),
    Key([mod_keys["mod"], "shift"], "Return", lazy.spawn(apps["filemanager"])),
    Key([mod_keys["mod"], "shift"], "b", lazy.spawn(apps["browser"]),
        desc=f"Launch {apps['browser']} web browser"),

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
        ),
    Key([mod_keys["mod"], "control"], "j",
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
    Key([mod_keys["mod2"], "shift"], "escape",
        lazy.group["scratchpad"].dropdown_toggle("sysmonitor")),
]

mouse = [
    Drag([mod_keys["mod"]], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod_keys["mod"]], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

