--[[ TODO: Create Tokyo Night Theme
--]]

local gears = require("gears")
local lain  = require("lain")
local awful = require("awful")
local wibox = require("wibox")
local dpi   = require("beautiful.xresources").apply_dpi

local os    = os
-- local my_table = awful.util.table or gears.table -- 4.{0,1} compatibility
local color = require("theme.colors")
local theme = {}

local buttons = require("config.buttons")
local tasklist = require("widgets.tasklist")

theme.dir          = os.getenv("HOME") .. "/.config/awesome/theme/"
theme.wallpaper    = theme.dir .. "wallpaper.jpg" --"cat.png"
theme.font         = "Noto Sans Regular 11"
theme.taglist_font = "Noto Sans Regular 14"

theme.bg_normal   = color['mantle']
theme.bg_focus    = color['sapphire']
theme.bg_urgent   = color['sapphire']
theme.bg_minimize = color['mantle']
theme.bg_systray  = color['crust']

theme.fg_normal   = color['text']
theme.fg_focus    = color['text']
theme.fg_urgent   = color['text']
theme.fg_minimize = color['text']

theme.border_normal = color['crust']
theme.border_focus  = color['sapphire']
theme.border_marked = color['sapphire']

theme.taglist_bg_focus = color['crust']
theme.taglist_fg_focus = color['sapphire']

theme.tasklist_bg_normal = color['crust']
theme.tasklist_bg_focus  = color['crust']
theme.tasklist_fg_focus  = color['sapphire']

--theme.wibar_widgets_bg_normal = color['sapphire']

-- {{{ Colors
theme.shape                 = gears.shape.rounded_rect
theme.border_width          = 1
theme.menu_height           = dpi(22)
theme.menu_width            = dpi(260)
theme.menu_submenu_icon     = theme.dir .. "/icons/submenu.png"
theme.awesome_icon          = theme.dir .. "/icons/awesome.png"
theme.taglist_squares_sel   = theme.dir .. "/icons/square_sel.png"
theme.taglist_squares_unsel = theme.dir .. "/icons/square_unsel.png"
theme.layout_tile           = theme.dir .. "/icons/layouts/tilew.png"
theme.layout_tilebottom     = theme.dir .. "/icons/layouts/tilebottomw.png"
theme.layout_spiral         = theme.dir .. "/icons/layouts/spiralw.png"
theme.layout_floating       = theme.dir .. "/icons/layouts/floatingw.png"
theme.widget_ac             = theme.dir .. "/icons/ac.png"
theme.widget_battery        = theme.dir .. "/icons/battery.png"
theme.widget_battery_low    = theme.dir .. "/icons/battery_low.png"
theme.widget_battery_empty  = theme.dir .. "/icons/battery_empty.png"
theme.widget_mem            = theme.dir .. "/icons/mem.png"
theme.widget_cpu            = theme.dir .. "/icons/cpu.png"
theme.widget_temp           = theme.dir .. "/icons/temp.png"
theme.widget_net            = theme.dir .. "/icons/net.png"
theme.widget_hdd            = theme.dir .. "/icons/hdd.png"
theme.widget_music          = theme.dir .. "/icons/note.png"
theme.widget_music_on       = theme.dir .. "/icons/note.png"
theme.widget_music_pause    = theme.dir .. "/icons/pause.png"
theme.widget_music_stop     = theme.dir .. "/icons/stop.png"
theme.widget_vol            = theme.dir .. "/icons/vol.png"
theme.widget_vol_low        = theme.dir .. "/icons/vol_low.png"
theme.widget_vol_no         = theme.dir .. "/icons/vol_no.png"
theme.widget_vol_mute       = theme.dir .. "/icons/vol_mute.png"
theme.widget_mail           = theme.dir .. "/icons/mail.png"
theme.widget_mail_on        = theme.dir .. "/icons/mail_on.png"
theme.widget_task           = theme.dir .. "/icons/task.png"
theme.widget_scissors       = theme.dir .. "/icons/scissors.png"
theme.widget_weather        = theme.dir .. "/icons/dish.png"
theme.useless_gap           = 2

local markup = lain.util.markup

-- Textclock
local clock = awful.widget.watch(
--"date +'%a %d %b %R'"
  "date +'%R'", 60,
  function(widget, stdout)
    widget:set_markup(" " .. markup.font(theme.font, stdout))
  end
)

-- Calendar
theme.cal = lain.widget.cal({
  attach_to = { clock },
  notification_preset = {
    font = "Noto Sans Mono Medium 16",
    fg   = theme.fg_normal,
    bg   = theme.bg_normal
  }
})

-- ALSA volume
theme.volume = lain.widget.alsabar({
  --togglechannel = "IEC958,3",
  notification_preset = { font = theme.font, fg = theme.fg_normal },
})
-- MEM
local memicon = wibox.widget.imagebox(theme.widget_mem)
local mem = lain.widget.mem({
  settings = function()
    widget:set_markup(markup.font(theme.font, " " .. mem_now.used .. "MB "))
  end
})

-- CPU
local cpuicon = wibox.widget.imagebox(theme.widget_cpu)
local cpu = lain.widget.cpu({
  settings = function()
    widget:set_markup(markup.font(theme.font, " " .. cpu_now.usage .. "% "))
  end
})

-- Battery
local baticon = wibox.widget.imagebox(theme.widget_battery)
local bat = lain.widget.bat({
  settings = function()
    if bat_now.status and bat_now.status ~= "N/A" then
      if bat_now.ac_status == 1 and tonumber(bat_now.perc) ~= 100 then
        widget:set_markup(markup.font(theme.font, " Charging " .. bat_now.perc .. "% "))
        baticon:set_image(theme.widget_ac)
        return
      elseif bat_now.ac_status == 1 and tonumber(bat_now.perc) == 100 then
        widget:set_markup(markup.font(theme.font, " Full "))
        baticon:set_image(theme.widget_ac)
        return
      elseif not bat_now.perc and tonumber(bat_now.perc) <= 5 then
        baticon:set_image(theme.widget_battery_empty)
      elseif not bat_now.perc and tonumber(bat_now.perc) <= 15 then
        baticon:set_image(theme.widget_battery_low)
      else
        baticon:set_image(theme.widget_battery)
      end
      widget:set_markup(markup.font(theme.font, " " .. bat_now.perc .. "% "))
    else
      widget:set_markup()
      baticon:set_image()
    end
  end
})

-- ALSA volume
local volicon = wibox.widget.imagebox(theme.widget_vol)
theme.volume = lain.widget.alsa({
  settings = function()
    if volume_now.status == "off" then
      volicon:set_image(theme.widget_vol_mute)
    elseif tonumber(volume_now.level) == 0 then
      volicon:set_image(theme.widget_vol_no)
    elseif tonumber(volume_now.level) <= 50 then
      volicon:set_image(theme.widget_vol_low)
    else
      volicon:set_image(theme.widget_vol)
    end

    widget:set_markup(markup.font(theme.font, " " .. volume_now.level .. "% "))
  end
})


function theme.at_screen_connect(s)
  s.quake = lain.util.quake({ app = awful.util.terminal })

  -- If wallpaper is a function, call it with the screen
  local wallpaper = theme.wallpaper
  if type(wallpaper) == "function" then
    wallpaper = wallpaper(s)
  end
  gears.wallpaper.maximized(wallpaper, s, true)

  -- All tags open with layout 1
  awful.tag(awful.util.tagnames, s, awful.layout.layouts[1])

  -- Create a promptbox for each screen
  s.mypromptbox = awful.widget.prompt()
  -- Create an imagebox widget which will contains an icon indicating which layout we're using.
  -- We need one layoutbox per screen.
  s.mylayoutbox = awful.widget.layoutbox(s)
  s.mylayoutbox:buttons(gears.table.join(
    awful.button({}, 1, function() awful.layout.inc(1) end),
    awful.button({}, 3, function() awful.layout.inc(-1) end)))

  s.mytaglist = awful.widget.taglist(
    s, awful.widget.taglist.filter.all, buttons.taglist
  )
  s.mytasklist = tasklist(s, theme.shape, buttons)
  -- Create the wibox
  s.mywibox = awful.wibar({ position = "top", screen = s, height = dpi(theme.menu_height), bg = theme.wibar_bg_normal,
    fg = theme.fg_normal })

  -- Add widgets to the wibox
  s.mywibox:setup {
    layout = wibox.layout.align.horizontal,
    { -- Left widgets
      layout = wibox.layout.fixed.horizontal,
      --spr,
      wibox.container.background(wibox.container.margin(wibox.widget { s.mytaglist,
        layout = wibox.layout.align.horizontal }, dpi(0), dpi(0)), theme.wibar_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(s.mylayoutbox, dpi(2), dpi(2)), theme.wibar_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(wibox.widget { s.mypromptbox,
        layout = wibox.layout.align.horizontal }, dpi(0), dpi(0)), theme.wibar_bg_normal,
        theme.shape),
    },
    s.mytasklist,
    -- Middle widget
    { -- Right widgets
      layout = wibox.layout.fixed.horizontal,
      wibox.widget.systray(),
      wibox.container.background(wibox.container.margin(wibox.widget { volicon, theme.volume.widget,
        layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(wibox.widget { baticon, bat.widget,
        layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(clock, dpi(2), dpi(2)), theme.wibar_bg_normal,
        theme.shape),
    },
  }
end

return theme
