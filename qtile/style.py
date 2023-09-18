import gtk_helper

themes = dict(
    breeze = dict(
        background="#232629", #background_normal
        foreground="#eff0f1",#foreground_normal
        this_current_screen_border="#3daee9", #foreground_active
        inactive="#4d4d4d",#background_alternate
        active="#eff0f1",#foreground_normal
        border="#3daee9", #foreground_active
        border_focus="#3daee9", #foreground_active
        border_normal="#232629", #background_normal
        urgent_text="#804453", #foreground_negative
        tooltip_background="#232629", #background_normal
        tooltip_color="#eff0f1",#foreground_normal
    ),
    default = dict(
        this_current_screen_border="#3daee9", #foreground_active
        border_focus="#3daee9", #foreground_active
    )
)

icons = dict( 
    alert = '󰀦',
    arch = '󰣇',
    calendar = '󰃭',
    close = '󰅙',
    code = '󱃖',
    cpu = '',
    clock = '󰥔',
    email = '󰴃',
    fedora = '',
    file = '',
    folder = '',
    headphones = '󰋌',
    home = "",
    music = '󰎄',
    memory = '',
    message = '󰍩',
    open = '',
    pause = '',
    presentation='󰈩',
    picture = '',
    play = '',
    power = '',
    plug = '',
    remote = '',
    spotify = '',
    terminal = '',
    text = '󰈚',
    battery = {
        '100' : '',
        '75' : '',
        '50' : '',
        '25' : '',
        '0' : '',
    },
    update = '󰚰',
    volume = '',
    volume_low = '󰕿',
    volume_med = '󰖀',
    volume_high = '󰕾',
    volume_mute = '󰝟',
    web = '󰾔',
    wifi = '',
)

# theme = gtk_helper.get_gtk3_theme()
theme = themes['breeze']
clock_fmt = "%a, %b %d  %H:%M"

