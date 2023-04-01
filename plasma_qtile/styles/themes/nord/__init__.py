nord=dict(
    #Polar Night
    nord0="#2e3440",
    nord1="#3b4252",
    nord2="#434c5e",
    nord3="#4c566a",
    #Snow Storm
    nord4="#d8dee9",
    nord5="#e5e9f0",
    nord6="#eceff4",
    #Frost
    nord7="#8fbcbb",
    nord8="#88c0d0",
    nord9="#81a1c1",
    nord10="#5e81ac",
    #Aurora
    nord11="#bf616a",
    nord12="#d08770",
    nord13="#3bcb8b",
    nord14="#aebe8c",
    nord15="b48ead"
)

def get_theme():
    return dict(
        background=nord['nord0'],
        foreground=nord['nord4'],
        this_current_screen_border=nord['nord8'],
        inactive=nord['nord3'],
        active=nord['nord4'],
        border_focus=nord['nord8'],
        border_normal=nord['nord0'],
        urgent_text=nord['nord11']
    )
