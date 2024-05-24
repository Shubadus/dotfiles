const WINDOW_NAME = "powerbar"

function generateButton(action, label) {
  return Widget.Button({
    on_clicked: () => {
      App.closeWindow(WINDOW_NAME)
      Utils.exec(action)
    },
    child: Widget.Box({
      children: [
        Widget.Icon(),
        Widget.Label({
          label
        })
      ]
    })
  })
}

const buttonBox = Widget.Box({
  spacing: 12,
  children: [
    generateButton('loginctl terminate-user $USER', 'Logout'),
    generateButton('systemctl suspend', 'Suspend'),
    generateButton('systemctl hibernate', 'Hibernate'),
    generateButton('shutdown', 'Shutdown'),
    generateButton('reboot', 'Restart'),
    generateButton('swaylock', 'Lock'),
  ],
  vertical: true
})

export const powerbar = Widget.Window({
  name: WINDOW_NAME,
    anchor: ["top", "right"],
  setup: self => self.keybind("Escape", () => {
      App.closeWindow(WINDOW_NAME)
  }),
  keymode: 'exclusive',
  child: buttonBox,
  visible: false,
  className: WINDOW_NAME,
})
