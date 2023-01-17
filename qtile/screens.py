from libqtile import bar, qtile, layout
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

from apps import apps
from style import colors, icons, theme


LAYOUT_DEFAULTS = dict(
    margin=4,
    **theme
)


group_colors = [
    colors['catppuccin']['macchiato']['teal'],
    colors['catppuccin']['macchiato']['lavender'],
    colors['catppuccin']['macchiato']['sky'],
    colors['catppuccin']['macchiato']['pink'],
]


groups = [
    dict(
        decorations = [
            BorderDecoration(
                colour = x,
                group=True,
                border_width=[2,0,0,0],
            ),
        ]
    ) for x in group_colors
]


separator = widget.TextBox(
    " ",
    padding=0,
    **groups[0]
)


widgets = [
    widget.TextBox(
        icons['fedora'],
        fmt=" {} ",
        # fontsize=18,
        mouse_callbacks={
            'Button1': lambda : qtile.cmd_spawn(apps['launcher'])
        },
        padding=4,
        **groups[0],
    ),
    separator,
    widget.GroupBox(
        disable_drag=True,
        highlight_method="text",
        urgent_alert_method="text",
        padding=0,
        rounded=True,
        **groups[0],
    ),
    widget.Spacer(),
    widget.Systray(
        icon_size = 24
    ),
    widget.Spacer(),
    widget.Mpris2(
        display_metadata=['xesam:title', 'xesam:artist'],
        fmt= f"{icons['spotify']}" + ' {}',
        max_chars=20,
        name='spotify',
        no_metadata_text="No data",
        objname="org.mpris.MediaPlayer2.spotify",
        paused_text="{track} " + f"{icons['pause']}",
        playing_text="{track} " + f"{icons['play']}",
        stop_pause_text='',
        **groups[3]
    ),
    widget.CheckUpdates(
        distro="Fedora",
        display_format= f"{icons['alert']}" + " {updates} Update(s)",
        fmt = " {} ",
        no_update_string="",
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e sudo dnf update'),
            'Button3': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e flatpak update')
        },
        update_interval=1800,
        **groups[3]
    ),
    widget.Memory(
        format=f"{icons['memory']}" + " {MemUsed:02.1f} GB",
        measure_mem="G",
        update_interval=1,
        **groups[1]
    ),
    widget.Battery(
        charge_char=f"{icons['plug']}",
        discharge_char=f"{icons['battery']['vertical']['100']}",
        empty_char=f"{icons['battery']['vertical']['unknown']}",
        full_char=f"{icons['plug']}",
        format="{char} {percent:2.0%}",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
            "xfce4-power-manager-settings"
        )},
        show_short_text=False,
        update_interval=10,
        **groups[1]
    ),
    widget.Volume(
        fmt=f" {icons['volume']}" + " {} ",
        mouse_callbacks={
            'Button3': lambda : qtile.cmd_spawn(apps['audio'])
        },
        step=5,
        **groups[1]
    ),
    widget.CurrentLayout(
        **groups[2]
    ),
    widget.Clock(
        fmt = "{}",
        **groups[2]
    ),
    widget.QuickExit(
        countdown_format="{}",
        default_text=f"{icons['power']}",
        **groups[2]
    ),
]


screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets,
            background=f"{theme.get('background')}",
            size=34,
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

