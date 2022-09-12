# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from libqtile import hook
from libqtile.command import lazy
from groups import init_float_exceptions, init_groups, init_float_types
from bindings import init_keys, init_mouse_bindings, SpecialKeys
from style import calendars, colors, init_layouts
from widgets import init_screens

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

@hook.subscribe.startup_once
def start_once():
    subprocess.call([f"{Path.home()}/.config/qtile/scripts/autostart.sh"])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

apps = dict(
    browser = "qutebrowser",
    terminal = "alacritty",
    filemanager = "alacritty -e ranger",
    sysmonitor = "alacritty -e btop"
)

mod_keys = dict(
    mod = "mod4",
    mod1 = "mod1",
    mod2 = "control"
)

theme = colors["tokyo_night"]

config = dict(
    apps = apps,
    mod_keys = mod_keys,
    theme = theme,
)

groups = init_groups()
keys = init_keys(
    mod_keys,
    apps,
    groups
)
mouse = init_mouse_bindings(mod_keys)
screens = init_screens(1, calendars["ymd"], apps, theme)
layouts = init_layouts(theme)
floating_types = init_float_types()
floating_layout = init_float_exceptions()

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

wmname = "LG3D"
