from libqtile import bar, widget, qtile
from libqtile.config import Screen
from libqtile.lazy import lazy

from style import Theme
from screens import get_active_screens

def widget_list(terminal: str, calendar: str, theme: Theme):
    return [
        # widget.CurrentLayoutIcon(scale=0.7, **theme.dict),
        widget.GroupBox(
            borderwidth=0,
            disable_drag=True,
            rounded=False,
            highlight_method="text",
            margin_y=3,
            **theme.dict
        ),
        widget.Spacer(length=bar.STRETCH, **theme.dict),
        widget.Clock(
            format=calendar,
            **theme.dict
        ),
        widget.Spacer(length=bar.STRETCH, **theme.dict),
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
            display_format=" {updates} Update(s)",
            no_update_string="",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                terminal + ' -e sudo dnf update')},
            **theme.dict
        ),
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


def main_widget_list(terminal: str, calendar: str, theme: Theme):
    widgets = widget_list(terminal=terminal,calendar=calendar,theme=theme)
    widgets.extend([
        widget.WidgetBox(
            widgets=[
                widget.Sep(**theme.dict),
                # CPU Usage
#               widget.TextBox(
#                   text="  ",
#                   padding=0,
#                   **theme.dict,
#               ),
#               widget.CPU(
#                   format="{load_percent}%",
#                   **theme.dict
#               ),
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
                ), ],
            close_button_location="right",
            text_closed=" ",
            text_open="  ",
            mouse_callbacks={
                'Button3': lambda: qtile.cmd_spawn(
                    terminal + ' -e htop')
            },
            **theme.dict
        ),
        widget.CurrentLayout(scale=0.7, **theme.dict),
        widget.Systray(
            icon_size=20,
            padding=4,
            **theme.dict
        ),
        widget.TextBox(
            fmt="",
            mouse_callbacks={
                'Button1': lambda: lazy.shutdown()
            },
            **theme.dict
        ),
    ])
    return widgets


def secondary_widget_list(terminal: str, calendar: str, theme: Theme):
    widgets = widget_list(terminal=terminal,calendar=calendar,theme=theme)
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
        ])
    return widgets


def init_screens(main_screen: int, calendar:str, terminal: str, theme: Theme) -> list[Screen]:
    """Initializes the screens for Qtile to render on the desktop"""
    # TODO: Dynamically return screens
    # based on the number of active screens.
    generated_screens = []
    for i in range(get_active_screens()):
        if i+1 == main_screen:
            generated_screens.append(main_widget_list(theme=theme, calendar=calendar, terminal=terminal))
        else:
            generated_screens.append(secondary_widget_list(theme=theme, calendar=calendar, terminal=terminal))
    return [Screen(top=bar.Bar(widgets=screen, size=24, opacity=0.8, margin=[4,5,0,5]))
            for screen in generated_screens]

