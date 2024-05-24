const network = await Service.import('network')

const WiredIndicator = () => Widget.Icon({
    icon: network.wired.bind('icon_name'),
})

const WifiIndicator = () => Widget.Icon({
    icon: network.wifi.bind('icon_name'),
})

const NetworkIndicator = () => Widget.Stack({
    children: {
        wifi: WifiIndicator(),
        wired: WiredIndicator(),
    },
    shown: network.bind('primary').as(p => p || 'wifi'),
})

export default () => Widget.Box({
    children: [
        Widget.Button({
          child: NetworkIndicator()
        }),
        Widget.Revealer({
          revealChild: false,
          class_name: "wifi_revealer",
          // transistionDuration: 1000,
          transition: 'slide_right',
          child: Widget.Label({
            label: network.wifi.bind('ssid')
            .as(ssid => ssid || 'Unknown'),
        }),
      })
    ],
    // on_primary_click: () => child.wifi_revealer.revealChild =!child.wifi_revealer.revealChild,
})

