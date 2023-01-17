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
    volume = '',
    web = '爵',
    wifi = '',
)

colors = dict(
    catppuccin = dict(
        macchiato = dict(
            rosewater = '#f4dbd6',
            flamingo = '#f0c6c6',
            pink = '#f5bde6',
            mauve = '#c6a0f6',
            red = '#ed8796',
            maroon = '#ee99a0',
            peach = '#f5a97f',
            yellow = '#eed49f',
            green = '#a6da95',
            teal = '#8bd5ca',
            sky = '#91d7e3',
            sapphire = '#7dc4e4',
            blue = '#8aadf4',
            lavender = '#b7bdf8',
            text = '#cad3f5',
            subtext1 = '#b8c0e0',
            subtext0 = '#a5adcb',
            overlay2 = '#939ab7',
            overlay1 = '#8087a2',
            overlay0 = '#6e738d',
            surface2 = '#5b6078',
            surface1 = '#494d64',
            surface0 = '#363a4f',
            base = '#24273a',
            mantle = '#1e2030',
            crust = '#181926'
        ),
    ),

    breeze = dict(
        background_alternate="#4d4d4d",
        background_normal="#31363b",
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
)

# theme = dict(
#     active=breeze['foreground_normal'],
#     background=breeze['background_normal'],
#     border_focus=breeze['decoration_focus'],
#     border_normal=breeze['background_normal'],
#     foreground=breeze['foreground_normal'],
#     inactive=breeze['foreground_visited'],
#     this_current_screen_border=breeze['decoration_focus'],
#     urgent_text=breeze['foreground_negative']
# )

theme = dict(
    background=colors['catppuccin']['macchiato']['crust'],
    foreground=colors['catppuccin']['macchiato']['text'],
    this_current_screen_border=colors['catppuccin']['macchiato']['sapphire'],
    inactive=colors['catppuccin']['macchiato']['base'],
    active=colors['catppuccin']['macchiato']['text'],
    border_focus=colors['catppuccin']['macchiato']['sapphire'],
    border_normal=colors['catppuccin']['macchiato']['crust'],
    urgent_text=colors['catppuccin']['macchiato']['red'],
)


widget_defaults = dict(
        border_width = 2,
        font = "NotoSans Nerd Font, Regular",
        fontsize = 20,
        margin_y = 3,
        **theme
    )

