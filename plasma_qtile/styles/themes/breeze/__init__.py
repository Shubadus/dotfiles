breeze = dict(
    background_alternate="#4d4d4d",
    background_normal="#232629",#"#31363b",
    decoration_focus="#3daee9",
    decoration_hover="#3daee9",
    foreground_active="#3daee9",
    foreground_inactive="#bdc3c7",
    foreground_link="#2980b9",
    foreground_negative="#804453",
    foreground_neutral="#f67400",
    foreground_normal="#eff0f1",
    foreground_positive="27ae60",
    foreground_visited="#7f8c8d",
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

def get_icons():
    return icons

def get_theme():
    return dict(
        background=breeze['background_normal'],
        foreground=breeze['foreground_normal'],
        this_current_screen_border=breeze['foreground_active'],
        inactive=breeze['background_alternate'],
        active=breeze['foreground_normal'],
        border_focus=breeze['foreground_active'],
        border_normal=breeze['background_normal'],
        urgent_text=breeze['foreground_negative']
    )
