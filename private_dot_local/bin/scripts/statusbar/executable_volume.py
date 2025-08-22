#!/usr/bin/env python3
import argcomplete
import argparse
import re
import subprocess

from math import floor


STEP = 5


def _call_amixer(args: list[str] | str) -> str:
    command = ['amixer']
    command.extend(args)
    result = subprocess.run(command, capture_output=True, text=True)
    result.check_returncode()
    return result.stdout


def _get_volume() -> int:
    volume_string = _call_amixer(['get', 'Master'])
    volumes = [re.sub('%', '', x) for x in re.findall(r"\d{2,3}%", volume_string)]
    return int(volumes[0])


def _is_mute():
    is_mute = _call_amixer(['get', 'Master'])
    return bool('[off]' in is_mute)


def toggle_mute():
    _call_amixer(['set', 'Master', '1+', 'toggle'])


def up():
    _call_amixer(['set', 'Master', 'on'])
    _call_amixer(['sset', 'Master', f'{STEP}%+'])


def down():
    _call_amixer(['set', 'Master', 'on'])
    _call_amixer(['sset', 'Master', f'{STEP}%-'])


def show(body='Volume: '):
    volume = _get_volume()
    if _is_mute():
        icon = 'audio-volume-off'
        bar = ''
        volume = ''
    else:
        bar = ''.join('─' for x in range(floor(volume/5)))
        icon = "audio-volume-low"
        if volume > 66:
            icon="audio-volume-high"
        elif volume > 34 and volume < 65:
            icon="audio-volume-medium"
    command = [
        'notify-send',
        '-r', '5556',
        '-u', 'normal',
        f'-i', f'{icon}',
        '-a', 'volume',
        '-c', 'volume',
        f'{body} {volume}',
        f'{bar}'
    ]
    print(' '.join(command))
    subprocess.run(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v, --volume", dest='volume', choices=['up', 'down', 'mute'])

    args = parser.parse_args()

    if args.volume == 'up':
        up()
        return show()
    elif args.volume == 'down':
        down()
        return show()
    elif args.volume == 'mute':
        toggle_mute()
        if _is_mute():
            return show(body='Volume: Muted ')
    show()


if __name__ == "__main__":
    main()
