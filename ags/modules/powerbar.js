const restartButton = Widget.Button({
  child: Widget.Label("Restart"),
  onClicked: () => Utils.exec('reboot')
})

const buttonBox = Widget.Box({
  spacing: 8,
  children: [
    restartButton,
  ],
})

export const powerBar = Widget.Window({
  name: 'PowerBar',
  keymode: 'on-demand',
  child: buttonBox,
  monitor: 0,
})
