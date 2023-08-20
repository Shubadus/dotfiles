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
    alert = '𥉉',
    close = '',
    code = '',
    cpu = '',
    fedora = '',
    file = '',
    folder = '',
    headphones = '',
    home = "",
    music = '',
    memory = '',
    message = '',
    open = '',
    pause = '',
    picture = '',
    play = '',
    power = '',
    plug = '',
    remote = '',
    spotify = '',
    terminal = '',
    battery = dict( 
        horizontal = { 
            '100' : '',
            '75' : '',
            '50' : '',
            '25' : '',
            '0' : '',
        },
        vertical = { 
            '10': '',
            '20': '',
            '30': '',
            '40': '',
            '50': '',
            '60': '',
            '70': '',
            '80': '',
            '90': '',
            '100': '',
            'alert': '',
            'unknown': '',
        },
    ),
    update = '󰚰',
    volume = '',
    web = '爵',
    wifi = '',
)

theme = gtk_helper.get_gtk3_theme()
clock_fmt = "%a, %b %d  %H:%M"

