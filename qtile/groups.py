from libqtile.config import Group, Match
from libqtile import layout

class GroupDefaults(Group):
    """Creates Default settings that can be passed to the Qtile Group class"""

    def __init__(self, name: str, layout: str = "monadtall",
                 label: str = None, matches: list = None, **kwargs):
        self.name = name
        self.layout = layout
        self.label = label if label else name
        self.matches = matches if matches else []
        super().__init__(name=self.name, layout=self.layout,
                         label=self.label, matches=self.matches, **kwargs)

def init_groups2(workspaces: list[dict]) -> list[Group]:
    groups = []
    for workspace in workspaces:
        groups.append(
            Group(
                name=workspace.get("Name", None),
                matches=workspace.get("matches", None),
                layouts=workspace.get("layouts", ["monadtall"])
            )
        )
    return groups

def init_groups() -> list[Group]:
    """Creates Dynamic Groups used for qtile's workspaces"""
    # Find wm_class value using "xprop WM_CLASS"
    # TODO: Look at including subscript to labels  
    return [
        # Internet
        GroupDefaults(name="1", label="", matches=[
            Match(wm_class=["chromium", "firefox", "qutebrowser"])
        ]),
        # Remote / Virtual Desktops
        GroupDefaults(name="2", label="", matches=[
            Match(wm_class=["remmina", "virt-manager", "vmrc"])
        ]),
        # File Browsers
        GroupDefaults(name="3", label="", matches=[
            Match(wm_class=["pcmanfm", "thunar"])
        ]),
        # Terminals
        GroupDefaults(name="4", label="", matches=[
            Match(wm_class=["urxvt", "termite", "Alacritty"])
        ]),
        # Code/Text Editors
        GroupDefaults(name="5", label="", matches=[
            Match(
                title=['vim', 'nvim'],
                wm_class=["vscodium", "mousepad", "vim"]
            )
        ]),
        # Office Suites
        GroupDefaults(name="6", label="", matches=[
            Match(wm_class=["libreoffice"])
        ]),
        # Music
        GroupDefaults(name="7", label="", matches=[
            Match(wm_class=["Spotify","pavucontrol"])
        ]),
        # Communications
        GroupDefaults(name="8", label="", layout="monadtall", matches=[
            Match(
                wm_class=["microsoft teams - preview", "zoom", "discord"])
        ]),
        # TODO: Figure out how implement Qtile's ScratchPad and DropDown
        # GroupDefaults(name="8"),
        # ScratchPad("scratchpad", dropdowns=[
        #    DropDown("term", "Alacritty", on_focus_lost_hide=True),
        #    DropDown("git", "gitg", opacity=0.9, on_focus_lost_hide=True)
        # ]),
    ]

def init_float_exceptions() -> layout.Floating:
    return layout.Floating(float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='Arcolinux-welcome-app.py'),
        Match(wm_class='Arcolinux-tweak-tool.py'),
        Match(wm_class='Arcolinux-calamares-tool.py'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='arcolinux-logout'),
        Match(wm_class='xfce4-terminal'),
        Match(wm_class='Variety'),
        Match(wm_class='ksnip'),
        Match(wm_class='cairo-dock'),
        Match(wm_class='RAIL'),
    ],  fullscreen_border_width = 0, border_width = 0)

def init_float_types():
    return ["notification", "toolbar", "splash", "dialog"]

