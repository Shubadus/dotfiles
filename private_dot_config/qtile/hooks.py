import subprocess

from libqtile import hook
from libqtile.lazy import lazy

from apps import apps
from groups import floating_types


@hook.subscribe.startup_once
def start_once():
    subprocess.call(apps['autostart'])
    subprocess.call('waybar')


@hook.subscribe.startup
def start_always():
    subprocess.call(apps['set-gtk-theme'])
    subprocess.call(apps['wayland']['monitors'])


@hook.subscribe.client_new
def keep_dock_on_top(window):
    if "plank" in window.get_wm_class():
        window.floating = True
        window.window.keep_above(True)


@hook.subscribe.client_new
def fullscreen_logout(window):
    if "wlogout" in window.get_wm_class():
        # window.floating = True
        window.fullscreen = True


@hook.subscribe.client_new
def xwayland_video_bridge(window):
    if "pwbypass" in window.get_wm_class():
        # window.floating = True
        # window.cmd_toggle_minimize()
        window.togroup("scratchpad")


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

