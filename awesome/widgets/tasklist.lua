local awful = require("awful")
local wibox = require("wibox")

-- local buttons = require("config.buttons")

return function(s, shape, buttons)
  return awful.widget.tasklist {
    screen  = s,
    filter  = awful.widget.tasklist.filter.currenttags,
    buttons = buttons.tasklist,
    style   = {
      shape = shape
    },
    layout  = {
      spacing_widget = {
        {
          forced_width  = 5,
          forced_height = 24,
          thickness     = 1,
          color         = "#777777",
          widget        = wibox.widget.separator
        },
        valign = "center",
        halign = "center",
        widget = wibox.container.place,
      },
      spacing = 1,
      layout = wibox.layout.fixed.horizontal
    },
  }
end
