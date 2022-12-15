local awful = require("awful")
local beautiful = require("beautiful")
local gears = require("gears")
local lain = require("lain")
local hotkeys_popup = require("awful.hotkeys_popup")
require("awful.hotkeys_popup.keys")

local apps = require("config.apps")
local modkeys = require("config.keys.mod")
local key = awful.key

local awesome, client, screen = awesome, client, screen

--
-- Client Keybindings
--
local client_keys = gears.table.join(
  key({ modkeys.mod, "Shift" }, "q", function(c) c:kill() end,
    { description = "Close window", group = "hotkeys" }),
  key({ modkeys.mod, "Shift" }, "space", function(c)
    awful.client.floating.toggle()
  end,
    { description = "Toggle floating", group = "client" }),
  key({ modkeys.mod, "Shift" }, "m", function(c)
    c.maximized = not c.maximized
  end,
    { description = "Toggle window maximized status", group = "client" }),

  key({ modkeys.mod }, "f", function(c)
    c.fullscreen = not c.fullscreen
  end,
    { description = "Fullscreen Window", group = "client" }),

  -- TODO: Change the keys for this
  key({ modkeys.mod, "Shift" }, "h", function(c) c:move_to_screen() end,
    { description = "move to screen", group = "client" }),
  key({ modkeys.mod, "Shift" }, "l", function(c) c:move_to_screen() end,
    { description = "move to screen", group = "client" })
)

--
-- Global Keybindings
--
local global_keys = gears.table.join(
  key({ modkeys.mod, "Shift" }, "d", function() awful.spawn("rofi -show drun") end,
    { description = "Show Launcher", group = "Applications" }),

  key({ modkeys.mod, "Shift" }, "Return", function() awful.util.spawn(apps.filemanager) end,
    { description = "Launch " .. apps.filemanager, group = "Applications" }),

  key({ modkeys.mod }, "Return", function() awful.spawn(apps.terminal) end,
    { description = "Launch " .. apps.terminal, group = "Applications" }),

  key({ modkeys.ctrl, "Shift" }, "Escape",
    function() awful.util.spawn(apps.taskmanager) end,
    { description = "Launch taskmanager", group = "Applications" }),

  -- TODO: Replace this with better lockscreen appearance
  key({ modkeys.ctrl, "Shift" }, "l", function()
    awful.spawn(apps.lock)
  end,
    { description = "Launch lockscreen", group = "system" }),

  key({ modkeys.mod }, "k",
    function()
      awful.client.focus.global_bydirection("up")
      if client.focus then client.focus:raise() end
    end,
    { description = "focus down", group = "client" }),
  key({ modkeys.mod }, "j",
    function()
      awful.client.focus.global_bydirection("down")
      if client.focus then client.focus:raise() end
    end,
    { description = "focus down", group = "client" }),
  key({ modkeys.mod }, "h",
    function()
      awful.client.focus.global_bydirection("left")
      if client.focus then client.focus:raise() end
    end,
    { description = "focus left", group = "client" }),
  key({ modkeys.mod }, "l",
    function()
      awful.client.focus.global_bydirection("right")
      if client.focus then client.focus:raise() end
    end,
    { description = "focus right", group = "client" }),

  -- Layout manipulation
  key({ modkeys.mod, modkeys.ctrl }, "l", function() awful.client.swap.byidx(1) end,
    { description = "swap with next client by index", group = "client" }),
  key({ modkeys.mod, modkeys.ctrl }, "h", function() awful.client.swap.byidx(-1) end,
    { description = "swap with previous client by index", group = "client" }),
  key({ modkeys.alt, }, "l", function() awful.screen.focus_relative(1) end,
    { description = "Focus the next screen", group = "screen" }),
  key({ modkeys.alt, }, "h", function() awful.screen.focus_relative(-1) end,
    { description = "Focus the previous screen", group = "screen" }),
  key({ modkeys.mod }, "u", awful.client.urgent.jumpto,
    { description = "Jump to urgent client", group = "client" }),

  -- Show/Hide Wibox
  key({ modkeys.mod }, "b", function()
    for s in screen do
      s.mywibox.visible = not s.mywibox.visible
      if s.mybottomwibox then
        s.mybottomwibox.visible = not s.mybottomwibox.visible
      end
    end
  end,
    { description = "toggle wibox", group = "awesome" }),

  -- Show/Hide Systray
  key({ modkeys.mod }, "-", function()
    awful.screen.focused().systray.visible = not awful.screen.focused().systray.visible
  end, { description = "Toggle systray visibility", group = "awesome" }),

  -- On the fly useless gaps change
  key({ modkeys.alt, modkeys.ctrl }, "j", function() lain.util.useless_gaps_resize(1) end,
    { description = "increment useless gaps", group = "tag" }),
  key({ modkeys.alt, modkeys.ctrl }, "k", function() lain.util.useless_gaps_resize(-1) end,
    { description = "decrement useless gaps", group = "tag" }),

  -- Standard program
  key({ modkeys.mod, "Shift" }, "r", awesome.restart,
    { description = "reload awesome", group = "awesome" }),

  key({ modkeys.alt, "Shift" }, "l", function() awful.tag.incmwfact(0.05) end,
    { description = "increase master width factor", group = "layout" }),
  key({ modkeys.alt, "Shift" }, "h", function() awful.tag.incmwfact(-0.05) end,
    { description = "decrease master width factor", group = "layout" }),
  key({ modkeys.alt, "Shift" }, "j", function() awful.tag.incnmaster(1, nil, true) end,
    { description = "increase the number of master clients", group = "layout" }),
  key({ modkeys.alt, "Shift" }, "k", function() awful.tag.incnmaster(-1, nil, true) end,
    { description = "decrease the number of master clients", group = "layout" }),
  key({ modkeys.mod }, "space", function() awful.layout.inc(1) end,
    { description = "select next", group = "layout" }),

  key({}, "XF86MonBrightnessUp", function() os.execute("xbacklight -inc 10") end,
    { description = "+10%", group = "hotkeys" }),
  key({}, "XF86MonBrightnessDown", function() os.execute("xbacklight -dec 10") end,
    { description = "-10%", group = "hotkeys" }),

  -- ALSA volume control
  key({}, "XF86AudioRaiseVolume",
    function()
      os.execute(string.format("amixer -q set %s 1%%+", beautiful.volume.channel))
      beautiful.volume.update()
    end),
  key({}, "XF86AudioLowerVolume",
    function()
      os.execute(string.format("amixer -q set %s 1%%-", beautiful.volume.channel))
      beautiful.volume.update()
    end),
  key({}, "XF86AudioMute",
    function()
      os.execute(string.format("amixer -q set %s toggle", beautiful.volume.togglechannel or beautiful.volume.channel))
      beautiful.volume.update()
    end),

  key({ modkeys.mod, "Shift" }, "/", hotkeys_popup.show_help),

  --Media keys supported by mpd.
  key({}, "XF86AudioPlay", function() awful.util.spawn("mpc toggle") end),
  key({}, "XF86AudioNext", function() awful.util.spawn("mpc next") end),
  key({}, "XF86AudioPrev", function() awful.util.spawn("mpc prev") end),
  key({}, "XF86AudioStop", function() awful.util.spawn("mpc stop") end)
)

--
-- Add the keys for each tag
--
for i, _ in ipairs(awful.util.tagnames) do
  -- Hack to only show tags 1 and 9 in the shortcut window (mod+s)
  local descr_view, descr_move
  if i == 1 or i == awful.util.tagnames[-1] then
    descr_view = { description = "view tag #", group = "tag" }
    descr_move = { description = "move focused client to tag #", group = "tag" }
  end
  global_keys = gears.table.join(
    global_keys,
    -- View tag only.
    key({ modkeys.mod }, "#" .. i + 9,
      function()
        local tag = awful.screen.focused().tags[i]
        if tag then
          tag:view_only()
        end
      end,
      descr_view),
    -- Move client to tag.
    key({ modkeys.mod, "Shift" }, "#" .. i + 9,
      function()
        if client.focus then
          local tag = client.focus.screen.tags[i]
          if tag then
            client.focus:move_to_tag(tag)
            -- tag:view_only() -- Uncomment this to follow window moved to tag
          end
        end
      end,
      descr_move)
  )
end
--
-- Return the Client, Global and Mod keys.
--
return {
  mod = modkeys,
  client = client_keys,
  global = global_keys
}
