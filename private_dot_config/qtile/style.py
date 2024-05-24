# import gtk_helper

def get_theme(theme_name):
    return dict(
        background=themes[theme_name].get('dark', '000000'),
        foreground=themes[theme_name].get('light', 'ffffff'),
        this_current_screen_border=themes[theme_name].get('focus', '#8AB4F8'),
        inactive=themes[theme_name].get('inactive', 'A9A9A9'),
        active=themes[theme_name].get('active', 'ffffff'),
        border=themes[theme_name].get('focus', '#8AB4F8'),
        border_focus=themes[theme_name].get('focus', '#8AB4F8'),
        border_normal=themes[theme_name].get('dark', '000000'),
        urgent_text=themes[theme_name].get('urgent', 'FF0000'),
        selected_foreground=themes[theme_name].get('grey', 'A9A9A9'),
        selected_background=themes[theme_name].get('focus', '#8AB4F8'),
        tooltip_background=themes[theme_name].get('dark', '000000'),
        tooltip_color=themes[theme_name].get('light', 'ffffff'),
        face_border_colour=themes[theme_name].get('focus', '#8AB4F8'),
    )


themes = dict(
    breeze = dict(
        grey="#232629",#background_alternate
        dark="#232629",
        light="#eff0f1",
        focus="#3daee9",
        active="#eff0f1",
        inactive="#4d4d4d",
        urgent="#804453", #foreground_negative
    ),
    default = dict(
        focus="#8AB4F8"
    ),
    materia_darker = dict(
        dark="#212121", 
        grey="#353c4a",
        light="#f1ffff",
        text="#0f101a",
        focus="#8AB4F8",
        # focus="#a151d3",
        active="#f1ffff",
        inactive="#4c566a",
        urgent="#F07178",
        color1="#a151d3",
        color2="#F07178",
        color3="#fb9f7f",
        color4="#ffd47e",
    ),
    materia_ocean = { 
        "dark": "#0f101a",
        "grey": "#353c4a",
        "light": "#f1ffff",
        "text": "#0f101a",
        "focus": "#a151d3",
        "active": "#f1ffff",
        "inactive": "#4c566a",
        "urgent": "#F07178",
        "color1": "#a151d3",
        "color2": "#F07178",
        "color3": "#fb9f7f",
        "color4": "#ffd47e",
    }
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
    flathub = '',
    headphones = '󰋌',
    home = '',
    maximize = '  ',
    memory = '',
    message = '󰍩',
    minimize = '  ',
    music = '󰎄',
    open = '',
    pause = '',
    presentation = '󰈩',
    picture = '',
    play = '',
    power = '',
    plug = '',
    remote = '',
    restore = '  ',
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

theme = get_theme('materia_darker')

clock_fmt = "%a, %b %d  %H:%M"

