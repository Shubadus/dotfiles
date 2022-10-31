--[[ TODO: Create Tokyo Night Theme
--]]

local gears = require("gears")
local lain  = require("lain")
local awful = require("awful")
local wibox = require("wibox")
local dpi   = require("beautiful.xresources").apply_dpi

local math, string, os = math, string, os
local my_table = awful.util.table or gears.table -- 4.{0,1} compatibility

local theme                                     = {}
theme.dir                                       = os.getenv("HOME") .. "/.config/awesome/themes/custom"
theme.wallpaper                                 = theme.dir .. "/wallpaper.jpg"
theme.font                                      = "Noto Sans Regular 11"
theme.taglist_font                              = "Noto Sans Regular 14"
theme.fg_normal                                 = "#FEFEFE"
theme.fg_focus                                  = "#889FA7"
theme.fg_urgent                                 = "#b74822"
theme.bg_focus                                  = "#1E2320"
theme.bg_urgent                                 = "#3F3F3F"
theme.tasklist_bg_focus                         = "#000000"
theme.tasklist_fg_focus                         = "#889FA7"
theme.border_width                              = dpi(1)
theme.border_normal                             = "#3F3F3F"
theme.border_focus                              = "#6F6F6F"
theme.border_marked                             = "#CC9393"
theme.shape                                     = gears.shape.rounded_rect
theme.titlebar_bg_focus                         = theme.bg_focus
theme.titlebar_bg_normal                        = theme.bg_normal
theme.titlebar_fg_focus                         = theme.fg_focus
theme.wibar_bg_normal                           = "#000000"
theme.wibar_widgets_bg_normal                   = "#000000A0"
theme.menu_height                               = dpi(25)
theme.menu_width                                = dpi(260)
theme.menu_submenu_icon                         = theme.dir .. "/icons/submenu.png"
theme.awesome_icon                              = theme.dir .. "/icons/awesome.png"
theme.taglist_squares_sel                       = theme.dir .. "/icons/square_sel.png"
theme.taglist_squares_unsel                     = theme.dir .. "/icons/square_unsel.png"
theme.layout_tile                               = theme.dir .. "/icons/tile.png"
theme.layout_tileleft                           = theme.dir .. "/icons/tileleft.png"
theme.layout_tilebottom                         = theme.dir .. "/icons/tilebottom.png"
theme.layout_tiletop                            = theme.dir .. "/icons/tiletop.png"
theme.layout_fairv                              = theme.dir .. "/icons/fairv.png"
theme.layout_fairh                              = theme.dir .. "/icons/fairh.png"
theme.layout_spiral                             = theme.dir .. "/icons/spiral.png"
theme.layout_dwindle                            = theme.dir .. "/icons/dwindle.png"
theme.layout_max                                = theme.dir .. "/icons/max.png"
theme.layout_fullscreen                         = theme.dir .. "/icons/fullscreen.png"
theme.layout_magnifier                          = theme.dir .. "/icons/magnifier.png"
theme.layout_floating                           = theme.dir .. "/icons/floating.png"
theme.widget_ac                                 = theme.dir .. "/icons/ac.png"
theme.widget_battery                            = theme.dir .. "/icons/battery.png"
theme.widget_battery_low                        = theme.dir .. "/icons/battery_low.png"
theme.widget_battery_empty                      = theme.dir .. "/icons/battery_empty.png"
theme.widget_mem                                = theme.dir .. "/icons/mem.png"
theme.widget_cpu                                = theme.dir .. "/icons/cpu.png"
theme.widget_temp                               = theme.dir .. "/icons/temp.png"
theme.widget_net                                = theme.dir .. "/icons/net.png"
theme.widget_hdd                                = theme.dir .. "/icons/hdd.png"
theme.widget_music                              = theme.dir .. "/icons/note.png"
theme.widget_music_on                           = theme.dir .. "/icons/note.png"
theme.widget_music_pause                        = theme.dir .. "/icons/pause.png"
theme.widget_music_stop                         = theme.dir .. "/icons/stop.png"
theme.widget_vol                                = theme.dir .. "/icons/vol.png"
theme.widget_vol_low                            = theme.dir .. "/icons/vol_low.png"
theme.widget_vol_no                             = theme.dir .. "/icons/vol_no.png"
theme.widget_vol_mute                           = theme.dir .. "/icons/vol_mute.png"
theme.widget_mail                               = theme.dir .. "/icons/mail.png"
theme.widget_mail_on                            = theme.dir .. "/icons/mail_on.png"
theme.widget_task                               = theme.dir .. "/icons/task.png"
theme.widget_scissors                           = theme.dir .. "/icons/scissors.png"
theme.widget_weather                            = theme.dir .. "/icons/dish.png"
theme.tasklist_plain_task_name                  = true
theme.tasklist_disable_icon                     = true
theme.useless_gap                               = 2
theme.titlebar_close_button_focus               = theme.dir .. "/icons/titlebar/close_focus.png"
theme.titlebar_close_button_normal              = theme.dir .. "/icons/titlebar/close_normal.png"
theme.titlebar_ontop_button_focus_active        = theme.dir .. "/icons/titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active       = theme.dir .. "/icons/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive      = theme.dir .. "/icons/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive     = theme.dir .. "/icons/titlebar/ontop_normal_inactive.png"
theme.titlebar_sticky_button_focus_active       = theme.dir .. "/icons/titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active      = theme.dir .. "/icons/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive     = theme.dir .. "/icons/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive    = theme.dir .. "/icons/titlebar/sticky_normal_inactive.png"
theme.titlebar_floating_button_focus_active     = theme.dir .. "/icons/titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active    = theme.dir .. "/icons/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive   = theme.dir .. "/icons/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive  = theme.dir .. "/icons/titlebar/floating_normal_inactive.png"
theme.titlebar_maximized_button_focus_active    = theme.dir .. "/icons/titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active   = theme.dir .. "/icons/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive  = theme.dir .. "/icons/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = theme.dir .. "/icons/titlebar/maximized_normal_inactive.png"

local markup = lain.util.markup


-- Textclock
local clock = awful.widget.watch(
  "date +'%a %d %b %R'", 60,
  function(widget, stdout)
    widget:set_markup(" " .. markup.font(theme.font, stdout))
  end
)

-- Calendar
theme.cal = lain.widget.cal({
  attach_to = { clock },
  notification_preset = {
    font = "Noto Sans Mono Medium 10",
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
      if bat_now.ac_status == 1 then
        widget:set_markup(markup.font(theme.font, " AC "))
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
      baticon:set_image(theme.widget_ac)
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
  -- Quake application
  -- s.quake = lain.util.quake({ app = awful.util.terminal })
  s.quake = lain.util.quake({ app = "urxvt", height = 0.50, argname = "--name %s" })

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
  s.mylayoutbox:buttons(my_table.join(
    awful.button({}, 1, function() awful.layout.inc(1) end),
    awful.button({}, 3, function() awful.layout.inc(-1) end),
    awful.button({}, 4, function() awful.layout.inc(1) end),
    awful.button({}, 5, function() awful.layout.inc(-1) end)))

  s.taglist_buttons = gears.table.join(
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
    end),
    awful.button({}, 4, function()
      awful.client.focus.byidx(1)
    end),
    awful.button({}, 5, function()
      awful.client.focus.byidx(-1)
    end)
  )

  -- Create a taglist widget
  s.mytaglist = awful.widget.taglist(s, awful.widget.taglist.filter.all, awful.util.taglist_buttons)
  s.mytasklist = awful.widget.tasklist {
    screen          = s,
    filter          = awful.widget.tasklist.filter.currenttags,
    buttons         = tasklist_buttons,
    style           = {
      border_width = 1,
      border_color = "#777777",
      shape        = gears.shape.rounded_bar,
    },
    layout          = {
      spacing        = 10,
      spacing_widget = {
        {
          forced_width = 5,
          shape        = gears.shape.circle,
          widget       = wibox.widget.separator
        },
        valign = "center",
        halign = "center",
        widget = wibox.container.place,
      },
      layout         = wibox.layout.flex.horizontal
    },
    -- Notice that there is *NO* wibox.wibox prefix, it is a template,
    -- not a widget instance.
    widget_template = {
      {
        {
          {
            {
              id     = "icon_role",
              widget = wibox.widget.imagebox,
            },
            margins = 2,
            widget  = wibox.container.margin,
          },
          {
            id     = "text_role",
            widget = wibox.widget.textbox,
          },
          layout = wibox.layout.fixed.horizontal,
        },
        left   = 10,
        right  = 10,
        widget = wibox.container.margin
      },
      id     = "background_role",
      widget = wibox.container.background,
    },
  }
  -- s.mytasklist = awful.widget.tasklist {
  --   screen          = s,
  --   filter          = awful.widget.tasklist.filter.currenttags,
  --   buttons         = s.tasklist_buttons,
  --   layout          = {
  --     spacing_widget = {
  --       {
  --         forced_width  = 5,
  --         forced_height = 24,
  --         thickness     = 1,
  --         color         = "#777777",
  --         widget        = wibox.widget.separator
  --       },
  --       valign = "center",
  --       halign = "center",
  --       widget = wibox.container.place,
  --     },
  --     spacing        = 1,
  --     layout         = wibox.layout.fixed.horizontal
  --   },
  --   -- Notice that there is *NO* wibox.wibox prefix, it is a template,
  --   -- not a widget instance.
  --   widget_template = {
  --     {
  --       wibox.widget.base.make_widget(),
  --       forced_height = 5,
  --       id            = "background_role",
  --       widget        = wibox.container.background,
  --     },
  --     {
  --       awful.widget.clienticon,
  --       margins = 5,
  --       widget  = wibox.container.margin
  --     },
  --     nil,
  --     layout = wibox.layout.align.vertical,
  --   },
  -- }

  -- Create a tasklist widget
  --   s.mytasklist = awful.widget.tasklist(s, awful.widget.tasklist.filter.currenttags, awful.util.tasklist_buttons)
  -- Create the wibox
  s.mywibox = awful.wibar({ position = "top", screen = s, height = dpi(22), bg = theme.wibar_bg_normal,
    fg = theme.fg_normal })

  -- Add widgets to the wibox
  s.mywibox:setup {
    layout = wibox.layout.align.horizontal,
    { -- Left widgets
      layout = wibox.layout.fixed.horizontal,
      --spr,
      wibox.container.background(wibox.container.margin(wibox.widget { s.mytaglist,
        layout = wibox.layout.align.horizontal }, dpi(0), dpi(0)), theme.wibar_widgets_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(wibox.widget { s.mypromptbox,
        layout = wibox.layout.align.horizontal }, dpi(0), dpi(0)), theme.wibar_widgets_bg_normal,
        theme.shape),
      spr,
    },
    s.mytasklist,
    -- wibox.container.background(wibox.container.margin(wibox.widget { s.mytasklist,
    --   layout = wibox.layout.align.horizontal }, dpi(0), dpi(0)), theme.wibar_widgets_bg_normal),
    -- Middle widget
    { -- Right widgets
      layout = wibox.layout.fixed.horizontal,
      wibox.widget.systray(),
      -- wibox.container.background(wibox.container.margin(wibox.widget {
      --   volicon,
      --   theme.volume.widget,
      --   cpuicon,
      --   cpu.widget,
      --   memicon,
      --   mem.widget,
      --   baticon,
      --   bat.widget,
      --   clock,
      --   s.mylayoutbox,
      --   layout = wibox.layout.align.horizontal
      -- }, dpi(0), dpi(0)), theme.wibar_widgets_bg_normal,
      --   theme.shape),
      wibox.container.background(wibox.container.margin(wibox.widget { volicon, theme.volume.widget,
        layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
        theme.shape),
      -- [[
      -- wibox.container.background(wibox.container.margin(wibox.widget { cpuicon, cpu.widget,
      --   layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
      --   theme.shape),
      -- wibox.container.background(wibox.container.margin(wibox.widget { memicon, mem.widget,
      --   layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
      --   theme.shape),
      -- ]]
      wibox.container.background(wibox.container.margin(wibox.widget { baticon, bat.widget,
        layout = wibox.layout.align.horizontal }, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(clock, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
        theme.shape),
      wibox.container.background(wibox.container.margin(s.mylayoutbox, dpi(2), dpi(2)), theme.wibar_widgets_bg_normal,
        theme.shape),
    },
  }
end

return theme
