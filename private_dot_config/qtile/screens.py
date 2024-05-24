import subprocess
# import os

from libqtile import bar, layout, widget
from libqtile.lazy import lazy
from libqtile.config import Screen
# from qtile_extras import widget
# from qtile_extras.popup.templates.mpris2 import DEFAULT_LAYOUT # Needs ver 0.23

from apps import apps
from style import icons, theme, clock_fmt


@lazy.function
def update_flatpak(qtile):
    qtile.groups_map["scratchpad"].dropdown_toggle("dropdown_term")
    # lazy.spawn(apps['update_flatpak'])


@lazy.function
def update_package_manager(qtile):
    qtile.groups_map["scratchpad"].dropdown_toggle("dropdown_term")
    # qtile.lazy.spawn(apps['update_pkg_mngr'])


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


def remove_text(text):
    return ''


sep = widget.Sep()


widgets = [
    widget.CurrentLayoutIcon(
        scale=0.67
    ),
    sep,
    widget.GroupBox(
        disable_drag=True,
        highlight_method="text",
        urgent_alert_method="text",
        padding=0,
        fontsize=22
    ),
    # widget.TaskList(
    #     fontsize=12,
    #     margin_y=4,
    #     margin_x=0,
    #     max_title_width=300,
    #     padding=5,
    #     rounded=False,
    #     theme_path="/usr/share/icons/Tela-dark",
    #     theme_mode="fallback",
    #     title_width_method='uniform',
    #     txt_floating=icons['restore'],
    #     txt_maximized=icons['maximize'],
    #     txt_minimized=icons['minimize'],
    #     # window_name_location=True
    #     # window_name_location_offset=150,
    #     # parse_text=remove_text
    # ),
    # widget.WindowName(
    # ),
    widget.Spacer(),
    widget.Mpris2(
        display_metadata=['xesam:title', 'xesam:artist'],
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
    # widget.Spacer(),
    widget.CheckUpdates(
        distro="Arch_yay",
        display_format=f"{icons['arch']}" + " {updates}",
        mouse_callbacks={
            # 'Button1': lazy.function(update_package_manager)
            'Button1': update_package_manager(),
        },
        fmt="{}",
        no_update_string="",
        update_interval=1800,
    ),
    widget.CheckUpdates(
        custom_command='flatpak remote-ls --updates',
        display_format=f"{icons['flathub']}" + " {updates}",
        mouse_callbacks={
            'Button1': update_flatpak(), #lazy.function(update_flatpak)
        },
        fmt="{}",
        no_update_string="",
        update_interval=1800,
    ),
    # Idle Inhibitor
    widget.GenPollText(
        update_interval=1,
        func=lambda: subprocess.check_output(
            f"{apps['idle_inhibit']}").decode(),
        mouse_callbacks={
            'Button1': lazy.spawn(f"{apps['idle_toggle']}"),
        },
        fontsize=20,
        padding=4
    ),
    widget.Memory(
        format=f"{icons['memory']}" + " {MemPercent:02.0f}%",
        update_interval=1,
    ),
    # widget.StatusNotifier(
    #     icon_size=20,
    #     padding=8,
    # ),
    widget.Systray(
        icon_size=20,
        padding=8,
    ),
    widget.TextBox(
        " ",
        padding=0
    ),
    # widget.WiFiIcon(
    #     mouse_callbacks={
    #         "Button3": lazy.group["scratchpad"].dropdown_toggle("network_manager")
    #     },
    #     padding_y=8,
    #     padding_x=2
    # ),
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
    # widget.UPowerWidget(
    #     margin=6
    # ),
    sep,
    widget.Clock(
        format=f"{icons['calendar']} {clock_fmt}",
        mouse_callbacks={
            'Button1': lazy.spawn(f"{apps['cal_show']}"),
        }
    ),
    # widget.AnalogueClock(
    #     face_shape='circle',
    #     face_border_color=theme.get('border', ''),
    #     margin=4,
    #     mouse_callbacks={
    #         'Button1': lazy.spawn(f"{apps['cal_show']}"),
    #     }
    # ),
]


screens = [
    Screen(
        # top=bar.Gap(size=28),
        top=bar.Bar(
            widgets=widgets,
            background=f"{theme.get('dark', '000000')}",
            size=28
        ),
        wallpaper="~/.local/share/wallpaper/wallpaper",
        wallpaper_mode="fill"
    ),
    Screen(
        # top=bar.Gap(size=28),
        # top=bar.Bar(
        #     widgets=widgets,
        #     background=f"{theme.get('dark', '000000')}",
        #     size=32
        # )
        wallpaper="~/.local/share/wallpaper/wallpaper",
        wallpaper_mode="fill"
    )
]


layouts = [
    layout.MonadTall(
        single_border_width=0,
        single_margin=0,
        # ratio=0.6,
        **LAYOUT_DEFAULTS
    ),
    layout.MonadThreeCol(
        single_border_width=0,
        single_margin=0,
        **LAYOUT_DEFAULTS
    ),
    # layout.MonadWide(**LAYOUT_DEFAULTS),
    layout.Floating(**LAYOUT_DEFAULTS),
    layout.VerticalTile(
        single_border_width=0,
        single_margin=0,
        **LAYOUT_DEFAULTS
    )
]
