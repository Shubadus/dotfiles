#!/bin/bash

sketchybar --set "$NAME" icon="" \
           --set "$NAME" click_script="sketchybar --set $NAME popup.drawing=toggle" \
           --add item logout popup."$NAME" \
           --set logout label="󰍃" \
                 click_script="osascript -e 'tell app \"System Events\" to log out'" \
           --add item sleep popup."$NAME" \
           --set sleep label="󰒲" \
                 click_script="osascript -e 'tell app \"System Events\" to sleep'" \
           --add item shutdown popup."$NAME" \
           --set shutdown label="" \
                 click_script="osascript -e 'tell app \"loginwindow\" to «event aevtrsdn»'" \
           --add item restart popup."$NAME" \
           --set restart label="󰜉" \
                 click_script="osascript -e 'tell app \"System Events\" to «event aevtrrst»'"
           # # --set calendar text.drawing=true \
           # --set calendar text.string="$(cal)"
