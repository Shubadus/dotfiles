import re

from libqtile.config import Match  

from style import icons

workspaces = [
  dict(
      name="1",
      label=f"{icons['web']}",
      matches=[
          Match(wm_class=["chromium", "firefox", "qutebrowser"])
  ]),
  dict(
      name="2",
      label=f"{icons['remote']}",
      matches=[
          Match(wm_class=["org.remmina.Remmina", "virt-manager", "vmrc"]),
          Match(wm_class=re.compile("Cisco AnyConnect*"))
  ]),
  dict(
      name="3",
      label=f"{icons['code']}",
      matches=[
          Match(
              title=['vim', 'nvim'],
              wm_class=["vscodium", "mousepad", "vim"]
          )
  ]),
  dict(
      name="4",
      label=f"{icons['file']}",
      matches=[
          Match(wm_class=["libreoffice","obsidian"])
  ]),
  dict(
      name="5",
      label=f"{icons['message']}",
      matches=[
          Match(wm_class=["microsoft teams - preview", "zoom", "discord"]),
          Match(wm_class=["Spotify","pavucontrol"]),
          Match(wm_class=re.compile("WebApp-Outlook*"))
  ])
]

