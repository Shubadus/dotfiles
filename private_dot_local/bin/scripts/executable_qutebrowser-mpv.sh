#!/bin/bash
mpv_location=(command -v mpv)

Link="$1"

Launch_Opts=" --really-quiet --fs=no --force-window"
Launch_Opts+=" --volume=60"
Launch_Opts+=" --title=Picture-in-Picture"

Launch_cmd=($mpv_location $Launch_Opts $Link)

"${Launch_cmd[@]}" &
