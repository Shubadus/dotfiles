const audio = await Service.import("audio")

const icons = {
  101: "overamplified",
  67: "high",
  34: "medium",
  1: "low",
  0: "muted",
}

function getIcon() {
  const icon = audio.speaker.is_muted ? 0 : [101, 67, 34, 1, 0].find(
    threshold => threshold <= audio.speaker.volume * 100)

  return `audio-volume-${icons[icon]}-symbolic`
}

const AudioIconButton = Widget.Button({
  child: Widget.Icon({
    icon: Utils.watch(getIcon(), audio.speaker, getIcon),
})
,
})

const AudioSlider = Widget.Slider({
  hexpand: true,
  draw_value: false,
  on_change: ({ value }) => audio.speaker.volume = value,
  setup: self => self.hook(audio.speaker, () => {
    self.value = audio.speaker.volume || 0
  }),
})

export default () => Widget.Box({
  class_name: "volume",
  // css: "min-width: 180px",
  children: [
    AudioIconButton,
    Widget.Revealer({
      revealChild: false,
      // class_name: "wifi_revealer",
      // transistionDuration: 1000,
      transition: 'slide_right',
      child: AudioSlider,
    })
  ],
})


