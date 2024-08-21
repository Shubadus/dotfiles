#!/bin/sh

# The $NAME variable is passed from sketchybar and holds the name of
# the item invoking this script:
# https://felixkratz.github.io/SketchyBar/config/events#events-and-scripting

sketchybar --set "$NAME" label="$(date '+%H:%M')" \
           --set "$NAME" click_script="sketchybar --set $NAME popup.drawing=toggle" \
           --add item calendar popup."$NAME" \
           --set calendar label="$(date '+%d/%m %H:%M')" 
           # # --set calendar text.drawing=true \
           # --set calendar text.string="$(cal)"

