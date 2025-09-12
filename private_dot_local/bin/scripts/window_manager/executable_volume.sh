#!/usr/bin/env bash

while getopts "uds:t" opt; do
  case "$opt" in
  "u") wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ ;;
  "d") wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- ;;
  "s") wpctl set-volume @DEFAULT_AUDIO_SINK@ "$OPTARG" ;;
  "t") wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle ;;
  esac
done

volume=$(echo "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print $2}')*100/ 1" | bc)
if [[ "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print $3}')" ]]; then
  volume=0
fi
notify-send \
  "Volume: " \
  -r 5556 \
  -i audio-speakers \
  -a volume \
  -h int:value:$volume
