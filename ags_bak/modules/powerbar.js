function generateButton(action, label) {
  return Widget.Button({
    on_clicked: () => Utils.exec(action),
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
  spacing: 8,
  children: [
    generateButton('loginctl terminate-user $USER', 'Logout'),
    generateButton('systemctl suspend', 'Suspend'),
    generateButton('systemctl hibernate', 'Hibernate'),
    generateButton('shutdown', 'Shutdown'),
    generateButton('reboot', 'Restart'),
  ],
  vertical: true
})

export default () => Widget.Window({
  name: 'powerbar',
  keymode: 'exclusive',
  child: buttonBox,
  // visible: false,
  // className: "powerbar",
})
