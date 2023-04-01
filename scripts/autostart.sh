#!/bin/bash
OpenPlasmaWindows=$(wmctrl -l Plasma | wc -l)
for i in $OpenPlasmaWindows
do
  wmctrl -c Plasma
done

nitrogen --restore
