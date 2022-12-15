local awful = require("awful")
local gears = require("gears")
local modkeys = require("config.keys.mod")

local client = client

local client_buttons = gears.table.join(
  awful.button({}, 1, function(c)
    c:emit_signal("request::activate", "mouse_click", { raise = true })
  end),
  awful.button({ modkeys.mod }, 1, function(c)
    c.floating = true
    c:emit_signal("request::activate", "mouse_click", { raise = true })
    --    c.maximized = false
    awful.mouse.client.move(c)

  end),
  awful.button({ modkeys.mod }, 3, function(c)
    c:emit_signal("request::activate", "mouse_click", { raise = true })
    awful.mouse.client.resize(c)
  end)
)

local tasklist_buttons = gears.table.join(
  awful.button({}, 1, function(c)
    if c == client.focus then
      c.minimized = true
    else
      c:emit_signal(
        "request::activate",
        "tasklist",
        { raise = true }
      )
    end
  end),
  awful.button({}, 3, function()
    awful.menu.client_list({ theme = { width = 250 } })
  end)
)

local taglist_buttons = gears.table.join(
  awful.button({}, 1, function(t) t:view_only() end),
  awful.button({ modkeys.mod }, 1, function(t)
    if client.focus then
      client.focus:move_to_tag(t)
    end
  end),
  awful.button({}, 3, awful.tag.viewtoggle),
  awful.button({ modkeys.mod }, 3, function(t)
    if client.focus then
      client.focus:toggle_tag(t)
    end
  end)
)

return {
  client = client_buttons,
  tasklist = tasklist_buttons,
  taglist = taglist_buttons
}
