# import hooks
import hooks
from groups import floating_layout, groups
from bindings import keys, mouse
from layouts import layouts
from libqtile.backend.wayland import InputConfig

screens = []

wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout='us',
    ),
}

follow_mouse_focus = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

wmname = "LG3D"

