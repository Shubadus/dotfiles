from pathlib import Path


GTK_THEME=Path.home().joinpath('.config','gtk-3.0','settings.ini')
SYSTEM_THEME_PATH=Path('/usr/share/themes/')


#NOTE: This function fails with the Adwaita GTK 3 Themes and will cause Qtile to crash
def get_gtk3_theme() -> dict[str,str]:
    colors = {}
    with open(GTK_THEME) as f:
        current_theme = f.readlines()
    theme_name = [x.lstrip('gtk-theme-name=').rstrip('\n') for x in current_theme if x.startswith('gtk-theme-name')][0]
    with open(SYSTEM_THEME_PATH.joinpath(theme_name,'gtk-3.0','gtk.css')) as f:
        color_list = [x.replace('@define-color ','').replace(';\n ','') for x in f.readlines() if x.startswith('@define-color')]
    
    for color in color_list:
        if color.startswith('@import'):
            pass
        k, v = color.split(' ', 1)
        v = v.strip().replace(';', '')
        if v.startswith('rgba'):
            rgba_list = v.replace('rgba(','').replace(')','').split(',')
            rgba_list = list(int(x.strip()) for x in rgba_list if not x.strip().startswith('0.'))
            v = "#{:02x}{:02x}{:02x}".format(*rgba_list)
        colors.update({k:v})

    for x,y in colors.items():
        if y.startswith('@'):
            try:
                y = colors[y.lstrip('@')]
            except KeyError:
                y = None
        colors.update({x:y})

    # return colors
    return dict(
        background=colors.get('theme_base_color'),
        foreground=colors.get('theme_text_color'),
        this_current_screen_border=colors.get('theme_selected_bg_color'),
        inactive=colors.get('theme_bg_color'),
        active=colors.get('theme_fg_color'),
        border=colors.get('theme_selected_bg_color'),
        border_focus=colors.get('theme_selected_bg_color'),
        border_normal=colors.get('theme_bg_color'),
        urgent_text=colors.get('error_color'), #foreground_negative
        tooltip_background=colors.get('theme_bg_color'),
        tooltip_color=colors.get('theme_fg_color'),
    )


if __name__ == '__main__':
    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    pp.pprint(get_gtk3_theme())
