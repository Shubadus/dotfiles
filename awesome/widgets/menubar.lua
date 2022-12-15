local awful = require("awful")

awful.wibar({ position = "top", screen = s, height = dpi(theme.menu_height), bg = theme.wibar_bg_normal,
  fg = theme.fg_normal })
