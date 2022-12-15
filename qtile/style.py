from dataclasses import dataclass
from typing import Optional

from libqtile import layout

icons = {
    'alert': '𥉉',
    'close': '',
    'code': '',
    'cpu': '',
    'fedora': '',
    'file': '',
    'folder': '',
    'headphones': '',
    'music': '',
    'memory': '',
    'message': '',
    'open': '',
    'pause': '',
    'picture': '',
    'play': '',
    'remote': '  ',
    'spotify': '',
    'terminal': '',
    'battery': {
        'horizontal': {
            '100': '',
            '75': '',
            '50': '',
            '25': '',
            '0': '',
        },
        'vertical': {
            'discharging': {
                '10': '',
                '20': '',
                '30': '',
                '40': '',
                '50': '',
                '60': '',
                '70': '',
                '80': '',
                '90': '',
                '100': '',
            },
            'alert': '',
            'charging': {
                '20': '',
                '30': '',
                '40': '',
                '60': '',
                '80': '',
                '90': '',
                '100': '',
            },
            'unknown': '',
        },
    },
    'web': '爵',

}

@dataclass
class Theme:
    background: Optional[str] = None
    foreground: Optional[str] = None
    this_current_screen_border: Optional[str] = None
    inactive: Optional[str] = None
    active: Optional[str] = None
    border_focus: Optional[str] = None
    border_normal: Optional[str] = None
    border_width: int = 1
    font: str = "JetBrains-Mono-Nerd-Font-Complete"
    fontsize: Optional[int] = 24

    @property
    def dict(self):
        return self.__dict__

colors: dict[str, Theme] = {
    "aqua": Theme(
        background="#000000",
        foreground="#f8f8f2",
        this_current_screen_border="#00ffff",
        inactive="#6272a4",
        active="#f8f8f2",
        border_focus="#00ffff",
        border_normal="#282a36"
    ),
    "catppuccin-macchiato": Theme(
        background="#181926", #crust
        foreground="#cad3f5", #text
        this_current_screen_border="#7dc4e4", #sapphire
        inactive="#1e2030", #mantle
        active="#cad3f5", #text
        border_focus="#7dc4e4", #sapphire
        border_normal="#181926" #crust
    ),
    "dracula" : Theme(
        background="#282a36",
        foreground="#f8f8f2",
        this_current_screen_border="#bd93f9",
        inactive="#6272a4",
        active="#f8f8f2",
        border_focus="#bd93f9",
        border_normal="#282a36"
    ),
    "tokyo_night": Theme(
        background="#1a1b26",
        foreground="#a9b1d6",
        this_current_screen_border="#7aa2f7",
        inactive="#32344a",
        active="#a9b1d6",
        border_focus="#7aa2f7",
        border_normal="#1a1b26"
    )
}

calendars = {
    # Wed YYYY-MM-DD [HH:MM]
    "ymd": "%a %Y-%m-%d  %H:%M",
    # Wed, Month DD [HH:MM]
    "wmd": "%a, %B %d  %H:%M",
    # Wed, DD-MM-YYYY [HH:MM]
    "dmy": "%a %d-%m-%Y  %H:%M ",
}

def init_layouts(theme: Theme) -> list:
    """
    Creates layouts used for qtile
    """
    return [
        layout.Floating(margin=4, margin_on_single=0, **theme.dict),
        layout.MonadTall(margin=4, single_margin=0, **theme.dict),
        layout.MonadThreeCol(margin=4, single_margin=0, **theme.dict),
        layout.MonadWide(margin=4, single_margin=0, **theme.dict),
        layout.VerticalTile(margin=4, margin_on_single=0, **theme.dict)
    ]

