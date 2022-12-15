-- {{{ Required libraries
local awesome, client, mouse, screen, tag = awesome, client, mouse, screen, tag
local string, os = string, os

--https://awesomewm.org/doc/api/documentation/05-awesomerc.md.html
-- Standard awesome library
local gears       = require("gears") --Utilities such as color parsing and objects
local awful       = require("awful") --Everything related to window managment
local wibox       = require("wibox") -- Widget and layout library
local beautiful   = require("beautiful") -- Theme handling library
local naughty     = require("naughty") -- Notification library
local freedesktop = require("freedesktop")
local my_table    = awful.util.table or gears.table -- 4.{0,1} compatibility
local theme_path  = string.format("%s/.config/awesome/theme/theme.lua", os.getenv("HOME"))

beautiful.init(theme_path)
beautiful.systray_icon_spacing = 2

-- TagNames are required by buttons
awful.util.tagnames = { "", "", "", "", "", "", "", "" }
local buttons       = require("config.buttons")
local keys          = require("config.keys")
local globalkeys    = keys.global
local hotkeys_popup = require("awful.hotkeys_popup")
require("awful.hotkeys_popup.keys")
-- {{{ Error handling
require("awful.autofocus")
require("awful.hotkeys_popup.keys")
require("config.error_handling")
require("config.signals")

-- Add Garbage Collection to reduce memory footprint
gears.timer {
  timeout = 30,
  autostart = true,
  callback = function() collectgarbage() end
}

-- awesome variables
awful.rules.rules = require("config.rules")
awful.layout.suit.tile.left.mirror = true
awful.layout.layouts = {
  awful.layout.suit.spiral,
  awful.layout.suit.tile,
  awful.layout.suit.floating,
  awful.layout.suit.tile.bottom,
}
-- TODO: Implement Shared Tags between screens
-- Use Charitable Tags system
awful.util.taglist_buttons = buttons.taglist
awful.util.mymainmenu = freedesktop.menu.build({
  after = {
    { "Log out", function() awesome.quit() end },
    { "Sleep", "systemctl suspend" },
    { "Restart", "systemctl reboot" },
    { "Shutdown", "systemctl poweroff" },
    -- other triads can be put here
  }
})

-- Create a wibox for each screen and add it
awful.screen.connect_for_each_screen(function(s)
  beautiful.at_screen_connect(s)
  s.systray = wibox.widget.systray()
  s.systray.visible = true
end)

naughty.config.defaults['icon_size'] = 100
-- Set mouse bindings
root.buttons(my_table.join(
  awful.button({}, 3, function() awful.util.mymainmenu:toggle() end),
  awful.button({}, 4, awful.tag.viewnext),
  awful.button({}, 5, awful.tag.viewprev)
))
-- Set keys
root.keys(globalkeys)
-- }}}

-- Autostart applications
awful.spawn.with_shell(os.getenv("HOME") .. "/.config/awesome/scripts/autostart.sh")
