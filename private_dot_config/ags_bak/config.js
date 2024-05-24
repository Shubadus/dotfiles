"use strict";

import Gdk from "gi://Gdk"
import Bar from "./modules/bar.js";
import { NotificationPopups } from "./modules/bar_widgets/notification.js";
import { powerbar } from "./modules/powerbar.js";
import { applauncher } from "./modules/applauncher.js";

// TODO: Move into separate place
const range = (length, start = 1) => Array.from({ length }, (_, i) => i + start);
function forMonitors(widget) {
  const n = Gdk.Display.get_default()?.get_n_monitors() || 1;
  return range(n, 0).map(widget).flat(1);
}

App.config({
  style: "./style.css",
  windows: [
    forMonitors(Bar),
    powerbar,
    applauncher,
    NotificationPopups(0)
  ],
});

export { };
