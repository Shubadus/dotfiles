import subprocess

from libqtile import bar, qtile, layout
from libqtile.lazy import lazy
from libqtile.config import Screen
from qtile_extras import widget

from apps import apps
from style import icons, theme, clock_fmt


LAYOUT_DEFAULTS = dict(
    margin=4,
    **theme
)

widget_defaults = dict(
    border_width=2,
    font="NotoSans Nerd Font",
    fontsize=18,
    tooltip_font="NotoSansMono Nerd Font",
    tooltip_fontsize=20,
    padding=6,
    **theme
)
sep = widget.Sep()

widgets = [
    widget.CurrentLayoutIcon(
        # padding=2,
        scale=0.67
    ),
    sep,
    widget.GroupBox(
        disable_drag=True,
        highlight_method="text",
        urgent_alert_method="text",
        padding=0,
        rounded=True,
        fontsize=22
    ),
    widget.WindowName(
    ),
    # widget.Spacer(),
    widget.Mpris2( display_metadata=['xesam:title', 'xesam:artist'],
        fmt=f"{icons['spotify']}" + ' {}',
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
        distro="Arch_yay",
        display_format=f"{icons['update']}" + " {updates}",
        fmt=" {} ",
        no_update_string="",
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e yay -Syu'),
            'Button3': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e flatpak update')
        },
        update_interval=1800,
    ),
    widget.Memory(
        format=f"{icons['memory']}" + " {MemPercent:02.0f}%",
        measure_mem="G",
        update_interval=1,
    ),
    widget.Systray(
        icon_size=20,
        padding=8,
    ),
    widget.TextBox(
        " ",
        padding=0
    ),
    widget.WiFiIcon(padding=6),
    # Volume Widget
    widget.GenPollText(
        update_interval=1, func=lambda: subprocess.check_output(
            f"{apps['vol']}").decode(),
        mouse_callbacks={
            'Button1': lazy.spawn(f"{apps['vol_show']}"),
            'Button2': lazy.spawn(f"{apps['vol_mute']}"),
            'Button3': lazy.group['scratchpad'].dropdown_toggle("audio"),
            'Button4': lazy.spawn(f"{apps['vol_up']}"),
            'Button5': lazy.spawn(f"{apps['vol_down']}"),
        },
        fontsize=20,
        padding=4
    ),
    # widget.ALSAWidget(
    #     mode='bar',
    #     update_interval=0.25
    # ),
    widget.UPowerWidget(
        margin=6
    ),
    sep,
    widget.Clock(
        format=f"{icons['calendar']} {clock_fmt}",
        mouse_callbacks={
            'Button1': lazy.spawn(f"{apps['cal_show']}"),
        }
    ),
    widget.AnalogueClock(
        face_shape='circle',
        face_border_color=theme.get('border', ''),
        padding=0
    ),
]

screens = [
    Screen(
        top=bar.Bar(
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
