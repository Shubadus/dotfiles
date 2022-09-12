import subprocess

from libqtile import bar, widget, qtile
from libqtile.config import Screen
from libqtile.lazy import lazy

from style import Theme
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
        widget.GroupBox(
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            margin_y=2,
            **theme.dict
        ),
        widget.Spacer(
            length=bar.STRETCH,
            **theme.dict
        ),
        widget.Clock(
            format=calendar,
            **theme.dict
        ),
        widget.Spacer(
            length=bar.STRETCH,
            **theme.dict
        ),
        widget.Mpris2(
            name='spotify',
            objname="org.mpris.MediaPlayer2.spotify",
            display_metadata=['xesam:title', 'xesam:artist'],
            scroll_chars=None,
            stop_pause_text='',
            fmt=" {} ",
            **theme.dict
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Fedora",
            display_format=" {updates} Dnf Update(s)",
            no_update_string="",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                apps["terminal"] + ' -e sudo dnf update')},
            **theme.dict
        ),
        # widget.CheckUpdates(
        #     update_interval=1800,
        #     custom_command="n | flatpak update",
        #     custom_command_modify=lambda x: [x.split('\n')],
        #     display_format=" {updates} Flatpak Update(s)",
        #     no_update_string="",
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
        #         terminal + ' -e flatpak update')},
        #     **theme.dict
        # ),
        widget.Battery(
            charge_char="",
            discharge_char="",
            format=" {char} {percent:2.0%} ",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                "xfce4-power-manager-settings"
            )},
            hide_threshold=0.99,
            update_interval=10,
            **theme.dict
        ),
    ]


def main_widget_list(apps: dict, calendar: str, theme: Theme):
    widgets = widget_list(apps=apps,calendar=calendar,theme=theme)
    widgets.extend([
        widget.GenPollText(
            func=check_process_status,
            update_interval=120,
            **theme.dict
        ),
        widget.WidgetBox(
            widgets=[
                widget.Sep(**theme.dict),
                # CPU Usage
                widget.TextBox(
                    text="  ",
                    padding=0,
                    **theme.dict,
                ),
                widget.CPU(
                    format="{load_percent}%",
                    **theme.dict
                ),
                # Memory Usage
                widget.TextBox(
                    text="  ",
                    padding=0,
                    **theme.dict
                ),
                widget.Memory(
                    format="{MemUsed:.0f}M",
                    update_interval=1,
                    **theme.dict
                ),
                widget.Sep(**theme.dict),
            ],
            close_button_location="right",
            text_closed=" ",
            text_open="  ",
            mouse_callbacks={
                'Button3': lambda: qtile.cmd_spawn(
                    apps["terminal"] + ' -e btop')
            },
            **theme.dict
        ),
        widget.CurrentLayoutIcon(scale=0.7, **theme.dict),
        #widget.CurrentLayout(scale=0.7, **theme.dict),
        widget.Systray(
            icon_size=20,
            padding=4,
            **theme.dict
        ),
        widget.Spacer(
            length = 5,
            **theme.dict
        ),
        # widget.TextBox(
        #     fmt="",
        #     mouse_callbacks={
        #         'Button1': lambda: lazy.shutdown()
        #     },
        #     **theme.dict
        # ),
    ])
    return widgets


def secondary_widget_list(apps: dict, calendar: str, theme: Theme):
    widgets = widget_list(apps=apps, calendar=calendar, theme=theme)
    widgets.extend([
        # CPU Usage
        widget.TextBox(
            text="  ",
            padding=0,
            **theme.dict,
        ),
        widget.CPU(
            format="{load_percent}%",
            **theme.dict
        ),
        # Memory Usage
        widget.TextBox(
            text="  ",
            padding=0,
            **theme.dict
        ),
        widget.Memory(
            format="{MemUsed:.0f}M",
            update_interval=1,
            **theme.dict
        ),
        widget.Spacer(
            length = 5,
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
            generated_screens.append(secondary_widget_list(theme=theme, calendar=calendar, apps=apps))
    return [Screen(top=bar.Bar(widgets=screen, size=24, opacity=0.9, margin=[2,2,0,2]))
            for screen in generated_screens]

