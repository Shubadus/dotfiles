import { Bar } from "./modules/bar.js";
import { powerBar } from "./modules/powerbar.js";

App.config({
  style: "./style.css",
  windows: [
    Bar(0),
    Bar(1),
    powerBar
  ],
});

export { };
