import os
import subprocess

def get_wayland_active_screens() -> int:
    raise NotImplementedError()

def get_xrandr_active_screens() -> int:
    xrandr_output = subprocess.run(
        ["xrandr", "--listactivemonitors"], stdout=subprocess.PIPE
    ).stdout.decode('utf-8').splitlines()
    return int(xrandr_output[0].split(':')[1].strip())

def get_active_screens() -> int:
    session_type = os.environ.get("XDG_SESSION_TYPE", None)
    if session_type == "x11":
        return get_xrandr_active_screens()
    # We'll assume if the session type isn't x11 that it is Wayland instead
    else:
        return get_wayland_active_screens()

