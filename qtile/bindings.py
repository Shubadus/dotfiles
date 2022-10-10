from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from libqtile import extension
from libqtile.command import lazy
from libqtile.config import Key, Drag

from style import Theme

# TODO: Move mod_keys["mod"] keys to being defined in the main config file and passed here
@dataclass
class SpecialKeys:
    MOD: str
    MOD1: Optional[str] = None
    MOD2: Optional[str] = None

MOD1 = "alt"
MOD2 = "control"

Rofi_path = Path.home().joinpath(".config","rofi","bin")

@lazy.function
def next_screen(qtile):
    qtile.cmd_next_screen()

@lazy.function
def prev_screen(qtile):
    qtile.cmd_prev_screen()

# TODO: allow init_keys to take a list of items to create keybindings with
# TODO: add keybindings to shift focus between multiple screens
def init_keys(
    mod_keys: dict,
    apps: dict,
    groups: list[dict]
) -> list[Key]:
    """
    Creates the keybindings for qtile

    Parameters
    ----------
    groups : list
        List of Group objects required to create individual
        keybinds for each group
    -------
    list
        Returns a list of Key objects used by qtile for
        keybindings
    """
    keys = [
        # SUPER + FUNCTION KEYS
        Key([mod_keys["mod"]], "f", lazy.window.toggle_fullscreen(),
            desc="Fullscreen current window"),
        Key([mod_keys["mod"]], "q", lazy.window.kill(),
            desc="Close current window"),
        Key([mod_keys["mod"]], "Return", lazy.spawn(apps["terminal"]),
            desc=f"Launch {apps['terminal']} terminal"),
        #Key([mod_keys["mod"]], "x", lazy.spawn("arcolinux-logout"),
        Key([mod_keys["mod"]], "x", lazy.spawn(f"{Rofi_path}/applet_powermenu"),
            desc="Launch ArcoLinux logout screen"),

        # SUPER + SHIFT KEYS
        Key([mod_keys["mod"], "shift"], "q", lazy.window.kill(),
            desc="Close current window"),
        Key([mod_keys["mod"], "shift"], "r", lazy.restart(),
            desc="Restart qtile"),

        # Applications
        Key([mod_keys["mod"], "shift"], "d", lazy.spawn(
            #" ".join(dmenu)),
            "rofi -show drun"),
            desc="Launch Rofi app launcher"),
        Key([mod_keys["mod"], "shift"], "Return", lazy.spawn(apps["filemanager"])),

        Key([mod_keys["mod"], "shift"], "b", lazy.spawn(apps["browser"]),
            desc=f"Launch {apps['browser']} web browser"),

        #Key(["control", "shift"], "escape", lazy.spawn(apps["sysmonitor"])),

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
        Key([mod_keys["mod"], "shift"], "f", lazy.layout.flip(),
            desc="Flip Layout (MonadTall/MonadWide)"),

        # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
        Key([mod_keys["mod"], "shift"], "k", lazy.layout.shuffle_up()),
        Key([mod_keys["mod"], "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod_keys["mod"], "shift"], "h", lazy.layout.swap_left()),
        Key([mod_keys["mod"], "shift"], "l", lazy.layout.swap_right()),

        # TOGGLE FLOATING LAYOUT
        Key([mod_keys["mod"], "shift"], "space", lazy.window.toggle_floating(),
            desc="Toggle floating layout")

        # Key([mod_keys["mod"]], "F12",
        #     lazy.group["scratchpad"].dropdown_toggle("git")),
        # Key([], "F12", lazy.group["scratchpad"].dropdown_toggle("term")),
    ]

    for i in groups:
        group_keys = [
            # CHANGE WORKSPACES
            Key([mod_keys["mod"]], i.name, lazy.group[i.name].toscreen(),
                desc=f"Switch to screen {i.name}"),
            Key([mod_keys["mod1"]], "Tab", lazy.screen.next_group(),
                desc="Cycle through screens"),
            Key([mod_keys["mod1"], "shift"], "Tab", lazy.screen.prev_group(),
                desc="Cycle through screens in reverse"),

            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod_keys["mod"], "shift"], i.name, lazy.window.togroup(i.name),
                desc=f"Move window to screen {i.name}"),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED
            # WINDOW TO WORKSPACE
            # Key([mod_keys["mod"], "shift"], i.name, lazy.window.togroup(
            #     i.name), lazy.group[i.name].toscreen()),
        ]
        # Extend
        keys.extend(group_keys)
    return keys


def init_mouse_bindings(mod_keys: dict) -> list[Drag]:
    """Creates keybindings for mouse"""
    return [
        Drag([mod_keys["mod"]], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod_keys["mod"]], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size())
    ]

