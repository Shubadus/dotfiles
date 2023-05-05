import subprocess

from libqtile import bar, qtile, layout
from libqtile.command import lazy
from libqtile.config import Screen
from qtile_extras import widget

from apps import apps
from style import icons, theme, clock_fmt
from widgets import memory, clock


LAYOUT_DEFAULTS = dict(
    margin=4,
    **theme
)

widget_defaults = dict(
    border_width=2,
    font="NotoSans Nerd Font",
    fontsize=20,
    tooltip_font="NotoSansMono Nerd Font",
    tooltip_fontsize=20,
    padding=8,
    **theme
)

widgets = [
    widget.GroupBox(
        disable_drag=True,
        highlight_method="text",
        urgent_alert_method="text",
        padding=0,
        rounded=True,
    ),
    widget.Sep(),
    widget.CurrentLayoutIcon(
        padding=4,
        scale=0.7
    ),
    widget.Spacer(),
    clock.ClockTooltip(
        format=clock_fmt,
        mouse_callbacks={

            'Button1': lazy.spawn(f"{apps['qtile_cal_show']}"),
        }
    ),
    widget.Spacer(),
    widget.Mpris2(
        display_metadata=['xesam:title', 'xesam:artist'],
        fmt= f"{icons['spotify']}" + ' {}',
        scroll_chars=20,
        name='spotify',
        no_metadata_text="No data",
        objname="org.mpris.MediaPlayer2.spotify",
        paused_text="{track} " + f"{icons['pause']}",
        playing_text="{track} " + f"{icons['play']}",
        stop_pause_text='',
        scroll=True,
    ),
    widget.CheckUpdates(
        distro="Fedora",
        display_format= f"{icons['update']}" + " {updates}",
        fmt = " {} ",
        no_update_string="",
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e sudo dnf update'),
            'Button3': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e flatpak update')
        },
        update_interval=1800,
    ),
    # widget.StatusNotifier(
    #     icon_size=24,
    # ),
    widget.Systray(
        icon_size=24,
    ),
    widget.TextBox(
        " ",
        padding=2
    ),
    memory.MemoryTooltip(
        format=f"{icons['memory']}" + " {MemPercent:02.0f}%",
        measure_mem="G",
        update_interval=1,
    ),
    # widget.Memory(
    #     format=f"{icons['memory']}" + " {MemPercent:02.0f}%",
    #     measure_mem="G",
    #     update_interval=1,
    # ),
    # Volume Widget
    widget.GenPollText(
        update_interval=1, func=lambda: subprocess.check_output(f"{apps['qtile_vol']}").decode(),
        mouse_callbacks={
            'Button1': lazy.spawn(f"{apps['qtile_vol_show']}"),
            'Button2': lazy.spawn(f"{apps['qtile_vol_mute']}"),
            'Button3': lazy.group['scratchpad'].dropdown_toggle("audio"),
            'Button4': lazy.spawn(f"{apps['qtile_vol_up']}"),
            'Button5': lazy.spawn(f"{apps['qtile_vol_down']}"),
        }),
    # Network Widget
    widget.GenPollText(update_interval=5, func=lambda: subprocess.check_output(str(apps['qtile_net'])).decode(),
                        mouse_callbacks={
                            'Button1': lazy.spawn(f"{apps['qtile_net']} ShowInfo", shell=True),
                            'Button3': lazy.group["scratchpad"].dropdown_toggle("network_manager")}),
    # Battery Widget
    widget.GenPollText(update_interval=1, func=lambda: subprocess.check_output(str(apps['qtile_bat'])).decode(),
                       mouse_callbacks={
                           'Button1': lazy.spawn(f"{apps['qtile_bat']} --c left-click", shell=True),
                           'Button2': lazy.spawn(f"{apps['qtile_bat']} --c middle-click", shell=True),
                           'Button3': lazy.spawn(f"{apps['qtile_bat']} --c right-click", shell=True),
                           }),
    widget.TextBox(
        f"{icons['power']}",
        mouse_callbacks={
            'Button1': lazy.spawn(apps['logout']),
        }
    ),
]

screens = [
    Screen(
        top=bar.Bar(
            # wallpaper=
            widgets=widgets,
            background=f"{theme.get('background')}",
            size=26,
        )
    )
]


layouts = [
    layout.MonadTall(**LAYOUT_DEFAULTS),
    layout.MonadThreeCol(**LAYOUT_DEFAULTS),
    layout.MonadWide(**LAYOUT_DEFAULTS),
    layout.Floating(**LAYOUT_DEFAULTS),
    layout.VerticalTile(**LAYOUT_DEFAULTS)
]
