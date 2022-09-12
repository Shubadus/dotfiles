from dataclasses import dataclass
from typing import Optional

from libqtile import layout

@dataclass
class Theme:
    background: Optional[str] = None
    foreground: Optional[str] = None
    this_current_screen_border: Optional[str] = None
    inactive: Optional[str] = None
    active: Optional[str] = None
    border_focus: Optional[str] = None
    border_normal: Optional[str] = None
    margin: int = 2
    border_width: int = 1
    font: str = "FontAwesome"
    fontsize: int = 16

    @property
    def dict(self):
        return self.__dict__

colors: dict[str, Theme] = {
    "dracula" : Theme(
        background="#282a36",
        foreground="#f8f8f2",
        this_current_screen_border="#bd93f9",
        inactive="#6272a4",
        active="#f8f8f2",
        border_focus="#bd93f9",
        border_normal="#282a36"
    ),
    "aqua": Theme(
        background="#000000",
        foreground="#f8f8f2",
        this_current_screen_border="#00ffff",
        inactive="#6272a4",
        active="#f8f8f2",
        border_focus="#00ffff",
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
    "ymd": "%a %Y-%m-%d [%H:%M]",
    # Wed, Month DD [HH:MM]
    "wmd": "%a, %B %d [%H:%M]",
    # Wed, DD-MM-YYYY [HH:MM]
    "dmy": "%a %d-%m-%Y [%H:%M]",
}

def init_layouts(theme: Theme) -> list:
    """
    Creates layouts used for qtile
    """
    return [
        layout.MonadTall(**theme.dict),
        layout.MonadWide(**theme.dict),
        layout.Max(**theme.dict),
        layout.Floating(**theme.dict),
    ]

