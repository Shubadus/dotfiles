#!/usr/bin/env bash

while getopts "uds:t" opt; do
  case "$opt" in
  "u") wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ ;;
  "d") wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- ;;
  "s")
    new_volume="$OPTARG"
    if [[ "$new_volume" -gt 100 ]]; then
      new_volume=1
    elif [[ "$new_volume" -lt 0 ]]; then
      new_volume=0
    else
      new_volume=$(echo "scale=2; $new_volume/100" | bc)
    fi
    wpctl set-volume @DEFAULT_AUDIO_SINK@ "$new_volume"
    ;;
  "t") wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle ;;
  esac
done

volume=$(echo "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print $2}')*100/ 1" | bc)
if [[ "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print $3}')" ]]; then
  volume=0
fi
if [[ "$volume" -gt 66 ]]; then
  icon="audio-volume-high"
elif [[ "$volume" -gt 33 && "$volume" -lt 66 ]]; then
  icon="audio-volume-medium"
elif [[ "$volume" -gt 0 && "$volume" -lt 33 ]]; then
  icon="audio-volume-low"
else
  icon="audio-volume-muted"
fi
notify-send \
  "Volume: " \
  -r 5556 \
  -i $icon \
  -a volume \
  -h int:value:$volume
