#!/usr/bin/env python3
import argcomplete
import argparse
import subprocess


STEP = 5


def show(body='Volume: ', ):
    volume = subprocess.run('wpctl get-volume @DEFAULT_AUDIO_SINK@', capture_output=True, shell=True).stdout.decode().split()[-1]
    if volume == '[MUTED]':
        volume = 0
    else:
        volume = int(float(volume)*100)
            
    if volume > 66:
        icon="audio-volume-high"
    elif volume > 34 and volume < 65:
        icon="audio-volume-medium"
    elif volume > 0:
        icon = "audio-volume-low"
    else:
        icon = 'audio-volume-off'
        body="Volume Muted: "
        volume = 0

    command = [
        'notify-send',
        '-r', '5556',
        '-u', 'normal',
        f'-i', f'{icon}',
        '-a', 'volume',
        '-c', 'volume',
        '-h', f'int:value:{volume}',
        f'{body}'
    ]
    print(' '.join(command))
    subprocess.run(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v, --volume", dest='volume', choices=['up', 'down', 'mute', 'set'])

    args = parser.parse_args()

    if args.volume == 'up':
        subprocess.run(f'wpctl set-volume @DEFAULT_AUDIO_SINK@ {STEP}%+', shell=True).check_returncode()
    elif args.volume == 'down':
        subprocess.run(f'wpctl set-volume @DEFAULT_AUDIO_SINK@ {STEP}%-', shell=True).check_returncode()
    elif args.volume == 'mute':
        subprocess.run(f'wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle', shell=True).check_returncode()
    show()


if __name__ == "__main__":
    main()
