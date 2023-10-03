#!/bin/bash

function ShowCalendar() {
  dunstify -i " " " Calendar" "$(cal)"
}

function EditCalendar() {
  echo ""
}

case "$1" in
  show)
      ShowCalendar
      ;;
   
  edit)
      EditCalendar
      ;;
   
  *)
      echo $"Usage: ${0##*/} {show|edit}"
      exit 1
esac

