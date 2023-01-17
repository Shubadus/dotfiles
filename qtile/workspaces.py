import re

from libqtile.config import Match  

from style import icons

workspaces = [
  dict(
      name="1",
      label=f"{icons['web']}₁",
      matches=[
          Match(wm_class=["chromium", "firefox", "qutebrowser"])
  ]),
  dict(
      name="2",
      label=f"{icons['remote']}₂",
      matches=[
          Match(wm_class=["org.remmina.Remmina", "virt-manager", "vmrc"]),
          Match(wm_class=re.compile("Cisco AnyConnect*"))
  ]),
  dict(
      name="3",
      label=f"{icons['folder']}₃",
      matches=[
          Match(wm_class=["pcmanfm", "thunar"])
  ]),
  dict(
      name="4",
      label=f"{icons['terminal']}₄",
      matches=[
          Match(wm_class=["urxvt", "termite", "Alacritty", "org.wezfurlong.wezterm", "kitty"])
  ]),
  dict(
      name="5",
      label=f"{icons['code']}₅",
      matches=[
          Match(
              title=['vim', 'nvim'],
              wm_class=["vscodium", "mousepad", "vim"]
          )
  ]),
  dict(
      name="6",
      label=f"{icons['file']}₆",
      matches=[
          Match(wm_class=["libreoffice","obsidian"])
  ]),
  dict(
      name="7",
      label=f"{icons['headphones']}₇",
      matches=[
          Match(wm_class=["Spotify","pavucontrol"])
  ]),
  dict(
      name="8",
      label=f"{icons['message']}₈",
      matches=[
          Match(wm_class=["microsoft teams - preview", "zoom", "discord"]),
          Match(wm_class=re.compile("WebApp-Outlook*"))
  ])
]

