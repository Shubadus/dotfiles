import subprocess

from libqtile import hook

from apps import apps
from groups import floating_types


@hook.subscribe.startup_once
def start_once():
    subprocess.call(apps['autostart'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(('xsetroot', '-cursor_name', 'left_ptr'))


# @hook.subscribe.screen_change
# def update_wallpaper(qtile, ev):
#     qtile.cmd_restart()
#     subprocess.call(apps['wallpaper_restore'])
#

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

