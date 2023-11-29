#!/bin/bash
app_dir=~/.local/share/applications/

flatpak run com.microsoft.Edge &
./$app_dir/webapp-Outlook3579 &
flatpak run com.github.IsmaelMartinez.teams_for_linux &
