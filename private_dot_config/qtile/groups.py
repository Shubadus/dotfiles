from libqtile import layout
from libqtile.lazy import lazy
from libqtile.config import DropDown, Group, Match, Key, ScratchPad

from apps import apps
from bindings import keys, mod_keys
from workspaces import workspaces
from style import theme


groups = [Group(**x) for x in workspaces]


for i in groups:
    if isinstance(i, Group):
        group_keys = [
            # CHANGE WORKSPACES
            Key([mod_keys["mod"]], i.name, lazy.group[i.name].toscreen(),
                desc=f"Switch to screen {i.name}"),
            Key([mod_keys["mod1"]], "Tab", lazy.screen.next_group(),
                desc="Cycle through screens"),
            Key([mod_keys["mod1"], "shift"], "Tab", lazy.screen.prev_group(),
                desc="Cycle through screens in reverse"),

            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod_keys["mod"], "shift"], i.name, lazy.window.togroup(i.name),
                desc=f"Move window to screen {i.name}"),
        ]
        # Extend
        keys.extend(group_keys)


dropdown_conf = {
    'on_focus_lost_hide': False
}


dropdowns = [
    DropDown("sysmonitor", apps['sysmonitor'], height=0.7, opacity=1, **dropdown_conf),
    DropDown("dropdown_term", apps['terminal'], height=0.7, opacity=0.9, **dropdown_conf),
    DropDown("dropdown_ranger", apps['filemanager'], height=0.7, opacity=0.9, **dropdown_conf),
    DropDown("network_manager", apps['network_manager'], height=0.7, opacity=1, **dropdown_conf),
    DropDown("vpn", apps['vpn'], height=0.7, opacity=1, **dropdown_conf),
    DropDown("audio", apps['audio_gui'], height=0.7, opacity=1, **dropdown_conf),
    DropDown("spotify", apps['spotify'], match=Match(wm_class='Spotify'), height=0.7, opacity=1, **dropdown_conf),
    # DropDown("pass_man", apps['pass_man_launcher'], match=Match(wm_class='1Password'), height=0.7, opacity=1, **dropdown_conf),
    # DropDown("xwaylandvideobridge", apps['videobridge'], match=Match(wm_class='xwaylandvideobridge'), height=0.7, opacity=1, **dropdown_conf),
    DropDown("calendar", apps['cal'], match=Match(wm_class='gsimplecal'), x=0.95),
]


scratchpad = ScratchPad("scratchpad", dropdowns)


groups.append(scratchpad)


floating_layout = layout.Floating(float_rules=(
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='Spotify'),
        Match(wm_class='feh'),
        Match(wm_class='plank'),
        Match(wm_class='Galculator'),
        Match(wm_class='arcolinux-logout'),
        Match(wm_class='archlinux-logout.py'),
        Match(wm_class='wlogout'),
        Match(wm_class='xfce4-terminal'),
        Match(wm_class='1Password'),
        Match(wm_class='tlp-ui'),
        Match(wm_class='Variety'),
        Match(wm_class='gsimplecal'),
        Match(wm_class='ksnip'),
        Match(wm_class='RAIL'),
        Match(wm_class='xdg-desktop-portal-gnome'),
    ), auto_fullscreen=True, fullscreen_border_width=0, border_width=2, **theme)

floating_types = ("notification", "toolbar", "splash", "dialog")

