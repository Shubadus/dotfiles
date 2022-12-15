import subprocess

from libqtile import bar, widget, qtile
from libqtile.config import Screen

from style import Theme, icons 
from screens import get_active_screens


def check_process_status() -> str:
   result = subprocess.Popen(
       ['pgrep openconnect'],
       stdout=subprocess.PIPE,
       shell=True
   ).stdout.read().decode('utf-8')
   return 'VPN Active' if result else ''

def widget_list(apps: dict, calendar: str, theme: Theme):
    return [
        widget.CurrentLayoutIcon(scale=0.65, **theme.dict),
        widget.Sep(**theme.dict),
        widget.GroupBox(
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            margin_y=1,
            **theme.dict
        ),
        widget.Sep(**theme.dict),
        widget.Spacer(**theme.dict),
        widget.Clock(
            format=calendar,
            **theme.dict
        ),
        widget.Spacer(**theme.dict),
        widget.Wallpaper(
            fmt='',
            **theme.dict
        ),
        # TODO: Add Volume WIDGET
        # widget.Volume(emoji=True,**theme.dict),
        widget.GenPollText(
            func=check_process_status,
            update_interval=120,
            **theme.dict
        ),
        widget.Mpris2(
            name='spotify',
            no_metadata_text="No data",
            paused_text="{track} " + icons['pause'],
            playing_text="{track} " + icons['play'],
            objname="org.mpris.MediaPlayer2.spotify",
            display_metadata=['xesam:title', 'xesam:artist'],
            scroll_chars=None,
            stop_pause_text='',
            fmt= icons['spotify'] + ' {}',
            **theme.dict
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Fedora",
            display_format=" " + icons['alert'] + " {updates} Update(s)",
            no_update_string="",
            execute=f"{apps['terminal'] + ' -e sudo dnf update'}",
            # mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
            #     apps["terminal"] + ' -e sudo dnf update')},
            **theme.dict
        ),
        widget.WidgetBox(
            widgets=[
                # CPU Usage
                widget.TextBox(
                    text=f" {icons['cpu']}",
                    **theme.dict,
                ),
                widget.CPU(
                    format="{load_percent}%",
                    **theme.dict
                ),
                # Memory Usage
                widget.TextBox(
                    text=f" {icons['memory']}",
                    **theme.dict
                ),
                widget.Memory(
                    format="{MemUsed:.0f}MB ",
                    update_interval=1,
                    **theme.dict
                ),
                widget.Wallpaper(
                    label=icons['picture'],
                    **theme.dict
                )
            ],
            close_button_location="right",
            text_closed=f" {icons['open']} ",
            text_open=f" {icons['close']} ",
            mouse_callbacks={
                'Button3': lambda: qtile.cmd_spawn(apps["sysmonitor"])
            },
            **theme.dict
        ),
        widget.Battery(
            charge_char=icons['battery']['vertical']['charging']['100'],
            discharge_char=icons['battery']['vertical']['discharging']['100'],
            empty_char=icons['battery']['vertical']['unknown'],
            full_char=icons['battery']['vertical']['charging']['100'],

            format="{char} {percent:2.0%} ",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                "xfce4-power-manager-settings"
            )},
            show_short_text=False,
            update_interval=10,
            **theme.dict
        ),
        # TODO: Add Dropdown to attach to clock widget
    ]


def main_widget_list(apps: dict, calendar: str, theme: Theme):
    widgets = widget_list(apps=apps,calendar=calendar,theme=theme)
    widgets.extend([
        widget.Systray(
            icon_size=24,
            padding=4,
            **theme.dict
        ),
    ])
    return widgets


def init_screens(main_screen: int, calendar:str, apps: dict, theme: Theme) -> list[Screen]:
    """Initializes the screens for Qtile to render on the desktop"""
    # TODO: Dynamically return screens
    # based on the number of active screens.
    generated_screens = []
    for i in range(get_active_screens()):
        if i+1 == main_screen:
            generated_screens.append(main_widget_list(theme=theme, calendar=calendar, apps=apps))
        else:
            generated_screens.append(widget_list(theme=theme, calendar=calendar, apps=apps))
    return [Screen(top=bar.Bar(widgets=screen, size=30, opacity=1, margin=[0,0,0,0]))
            for screen in generated_screens]

