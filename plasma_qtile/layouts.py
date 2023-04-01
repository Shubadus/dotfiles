from libqtile import layout

from style import theme


LAYOUT_DEFAULTS = dict(
    margin=4,
    **theme
)


layouts = [
    layout.MonadTall(**LAYOUT_DEFAULTS),
    layout.MonadThreeCol(**LAYOUT_DEFAULTS),
    layout.MonadWide(**LAYOUT_DEFAULTS),
    layout.Floating(**LAYOUT_DEFAULTS),
    layout.VerticalTile(**LAYOUT_DEFAULTS)
]
