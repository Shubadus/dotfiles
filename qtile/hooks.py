import subprocess

from libqtile import hook
from libqtile.lazy import lazy

from apps import apps
from groups import floating_types


@hook.subscribe.startup_once
def start_once():
    subprocess.call(apps['autostart'])


@hook.subscribe.startup
def start_always():
    subprocess.call(apps['set-gtk-theme'])


# @hook.subscribe.screen_change
# def update_wallpaper(qtile, ev):
#     qtile.cmd_restart()
#     subprocess.call(apps['wallpaper_restore'])
#
@hook.subscribe.client_new
def keep_dock_on_top(window):
    if "plank" in window.get_wm_class():
        window.window.keep_above(True)


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

