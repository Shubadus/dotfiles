local awful = require("awful")
local beautiful = require("beautiful")

local clientkeys = require("config.keys").client
local clientbuttons = require("config.buttons").client

return {
  -- All clients will match this rule.
  { rule = {},
    properties = { border_width = beautiful.border_width,
      border_color = beautiful.border_normal,
      focus = awful.client.focus.filter,
      raise = true,
      keys = clientkeys,
      buttons = clientbuttons,
      screen = awful.screen.preferred,
      placement = awful.placement.no_overlap + awful.placement.no_offscreen,
      size_hints_honor = false
    }
  },
  -- Prevent YouTube fullscreen from going underneath windows
  { rule = { instance = "plugin-container" },
    properties = { floating = true } },
  -- Same rule but for Chromium
  { rule = { instance = "exe" },
    properties = { floating = true } },


  -- Titlebars
  { rule_any = { type = { "dialog", "normal" } },
    properties = { titlebars_enabled = false } },
  { rule = { class = "1password" },
    properties = { titlebars_enabled = false } },
  -- Set applications to always map on the tag 2 on screen 1.

  { rule = { class = "Xfce4-settings-manager" },
    properties = { floating = false } },

  -- Floating clients.
  { rule_any = {
    instance = {
      "DTA", -- Firefox addon DownThemAll.
      "copyq", -- Includes session name in class.
    },
    class = {
      "Arandr",
      "Arcolinux-welcome-app.py",
      "Blueberry",
      "Galculator",
      "Gnome-font-viewer",
      "Gpick",
      "Imagewriter",
      "Font-manager",
      "Kruler",
      "MessageWin", -- kalarm.
      "archlinux-logout",
      "Peek",
      "Skype",
      "System-config-printer.py",
      "Sxiv",
      "Unetbootin.elf",
      "Wpa_gui",
      "Remmina",
      "1password",
      "pinentry",
      "veromix",
      "xtightvncviewer",
      "Xfce4-terminal"
    },

    name = {
      "Event Tester", -- xev.
    },
    role = {
      "AlarmWindow", -- Thunderbird's calendar.
      "pop-up", -- e.g. Google Chrome's (detached) Developer Tools.
      "Preferences",
      "setup",
    }
  }, properties = { floating = true } },

  -- Floating clients but centered in screen
  { rule_any = {
    class = {
      "Polkit-gnome-authentication-agent-1",
    },
  },
    properties = { floating = true },
    callback = function(c)
      awful.placement.centered(c, nil)
    end }
}
