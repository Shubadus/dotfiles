local awful = require("awful")
local beautiful = require("beautiful")
local gears = require("gears")

local client, screen = client, screen

-- Re-set wallpaper when a screen's geometry changes (e.g. different resolution)
screen.connect_signal("property::geometry", function(s)
  -- Wallpaper
  if beautiful.wallpaper then
    local wallpaper = beautiful.wallpaper
    -- If wallpaper is a function, call it with the screen
    if type(wallpaper) == "function" then
      wallpaper = wallpaper(s)
    end
    gears.wallpaper.maximized(wallpaper, s, true)
  end
end)

-- No borders when rearranging only 1 non-floating or maximized client
screen.connect_signal("arrange", function(s)
  local only_one = s.tiled_clients == 1
  for _, c in pairs(s.clients) do
    if only_one and not c.floating or c.maximized or c.fullscreen then
      c.border_width = 1
    else
      c.border_width = beautiful.border_width
    end
  end
end)

-- Enable sloppy focus, so that focus follows mouse.
client.connect_signal("mouse::enter", function(c)
  c:emit_signal("request::activate", "mouse_enter", { raise = false })
end)

client.connect_signal("focus", function(c) c.border_color = beautiful.border_focus end)
client.connect_signal("unfocus", function(c) c.border_color = beautiful.border_normal end)

-- No Border for maximized clients
client.connect_signal("focus",
  function(c)
    if c.maximized then -- no borders if only 1 client visible
      c.border_width = 0
    elseif #awful.screen.focused().clients > 1 then
      c.border_width = beautiful.border_width
      c.border_color = beautiful.border_focus
    end
  end)
client.connect_signal("unfocus", function(c) c.border_color = beautiful.border_normal end)
