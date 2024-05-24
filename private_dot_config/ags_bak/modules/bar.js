  // import { notification } from "./modules/bar_widgets/notification.js"
  import ClientTitle from "./bar_widgets/hyprland/window_title.js";
  import Clock from "./bar_widgets/clock.js";
  import Network from "./bar_widgets/network_indicator.js";
  import Volume from "./bar_widgets/volume.js";
  import Workspaces from "./bar_widgets/hyprland/workspaces.js";

  // const notifications = await Service.import("notifications")
  const mpris = await Service.import("mpris")
  const battery = await Service.import("battery")
  const systemtray = await Service.import("systemtray")


  // we don't need dunst or any other notification daemon
  // because the Notifications module is a notification daemon itself
//   function Notification() {
//     const popups = notifications.bind("popups")
//     return Widget.Box({
//       class_name: "notification",
//       visible: popups.as(p => p.length > 0),
//       children: [
//         Widget.Icon({
//           icon: "preferences-system-notifications-symbolic",
//         }),
//         Widget.Label({
//           label: popups.as(p => p[0]?.summary || ""),
//         }),
//       ],
//     })
// }


function Media() {
  const label = Utils.watch("", mpris, "player-changed", () => {
    if (mpris.players[0]) {
      const { track_artists, track_title } = mpris.players[0]
      return `${track_artists.join(", ")} - ${track_title}`
    } else {
      return "Nothing is playing"
    }
  })

  return Widget.Button({
    class_name: "media",
    on_primary_click: () => mpris.getPlayer("")?.playPause(),
    on_scroll_up: () => mpris.getPlayer("")?.next(),
    on_scroll_down: () => mpris.getPlayer("")?.previous(),
    child: Widget.Label({ label }),
  })
}



// TODO: Make Battery Bar reveal on hover
function BatteryLabel() {
  const value = battery.bind("percent").as(p => p > 0 ? p / 100 : 0)
  const icon = battery.bind("percent").as(p =>
    `battery-level-${Math.floor(p / 10) * 10}-symbolic`)

  return Widget.Box({
    class_name: "battery",
    visible: battery.bind("available"),
    children: [
      Widget.Button({
        onHover: () => { 
          // battery-reveal.reveal_child = !battery-reveal.reveal_child;
        },
        child: Widget.Icon({
          icon: icon,
          // tooltip-text: value
        }),
      }),
      Widget.Revealer({
        class_name: 'battery-reveal',
        transition: 'slide_right',
        reveal_child: false,
        child: Widget.LevelBar({
          widthRequest: 100,
          bar_mode: "discrete",
          vpack: "center",
          // visible: false,
          value,
        }),
      }),
    ],
  })
}


function SysTray() {
  const items = systemtray.bind("items")
    .as(items => items.map(item => Widget.Button({
      child: Widget.Icon({ icon: item.bind("icon") }),
      on_primary_click: (_, event) => item.activate(event),
      on_secondary_click: (_, event) => item.openMenu(event),
      tooltip_markup: item.bind("tooltip_markup"),
    })))

  return Widget.Box({
    children: items,
  })
}



// layout of the bar
function Left() {
  return Widget.Box({
    spacing: 8,
    children: [
      Workspaces(),
      ClientTitle(),
    ],
  })
}

function Center() {
  return Widget.Box({
    spacing: 8,
    children: [
      Media(),
      // notification
      // NotificationPopups(),
    ],
  })
}

function Right() {
  return Widget.Box({
    hpack: "end",
    spacing: 8,
    children: [
      SysTray(),
      Volume(),
      Network(),
      // WifiIndicator(), 
      BatteryLabel(),
      Clock(),
    ],
  })
}

export default (monitor = 0) => Widget.Window({
  name: `bar-${monitor}`, // name has to be unique
  class_name: "bar",
  monitor,
  layer: 'top',
  anchor: ["top", "left", "right"],
  // margins: [4, 4],
  exclusivity: "exclusive",
  child: Widget.CenterBox({
    start_widget: Left(),
    center_widget: Center(),
    end_widget: Right(),
  }),
})
