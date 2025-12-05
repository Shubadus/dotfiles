#! /usr/bin/env python3
import argparse
import argcomplete
import subprocess
import json


from PIL import ImageFont


def _print_waybar(alt: str = '', text: str = '', tooltip: str = '', class_text: str = '', percentage: str = ''):
    print(json.dumps({
        'alt': f'{alt}',
        'text': f'{text}',
        'tooltip': f'{tooltip}',
        'class': f'{class_text}',
        'percentage': f'{percentage}'
    }))


def get_history_count():
    dnd = bool(int(subprocess.run(['dunstctl', 'get-pause-level'], capture_output=True).stdout))
    message_count = int(subprocess.run(['dunstctl', 'count', 'history'], capture_output=True).stdout)
    if dnd and message_count > 0:
        _print_waybar(tooltip=f'{message_count} Notifications', alt='dnd-notification', class_text='alert')
    elif dnd:
        _print_waybar(tooltip=f'{message_count} Notifications', alt='dnd-none', class_text='dnd')
    elif message_count > 0:
        _print_waybar(text=f'{message_count}',tooltip=f'{message_count} Notifications', alt='notification', class_text='alert')
    else:
        _print_waybar(tooltip=f'{message_count} Notifications', alt='none')


def toggle_dnd():
    dnd_level = int(subprocess.run(['dunstctl', 'get-pause-level'], capture_output=True).stdout)
    if dnd_level > 0:
        subprocess.run(['dunstctl', 'set-pause-level', '0']).check_returncode()
    else:
        subprocess.run(['dunstctl', 'set-pause-level', '1']).check_returncode()


def clear_history():
    subprocess.run(['dunstctl', 'history-clear']).check_returncode()


# TODO: May be useful to create config file to handle this
# TODO: Display list of objects from dunst history, show the selected message using 'dunstctl history-pop'
def display_notifications():
    history = json.loads(subprocess.run(["dunstctl", "history"], capture_output=True).stdout.decode()).get('data')[0]
    summaries = [f'{x.get('appname').get('data')}:  {x.get('summary').get('data')}' for x in history]
    process = [
        'fuzzel',
        '--dmenu',
        '--anchor', 'top-left',
        '--index',
        '-n', 'notification-history',
        '-l', f'{len(summaries)}',
    ]
    if len(summaries) < 1:
        process.extend([
            '-p',
            'No notification history',
            '--width',
            f'{len('No notification history') - 5}'
        ])
    else:
        longest_name = len(max(summaries, key=len))
        print(longest_name)
        process.extend([
            '--width',
            f'50',
            '--hide-prompt'
        ])
    selection = subprocess.run(process, input="\n".join(summaries), capture_output=True, text=True).stdout
    if selection:
        subprocess.run(['dunstctl', 'history-pop', f'{history[int(selection)].get('id').get('data')}'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s, --show-history', dest='show_history', action='store_true', help='Show dunst history as app launcher selections')
    parser.add_argument('-c, --count', dest='count', action='store_true', help='Display a count of notifications and exit')
    parser.add_argument('-d, --toggle-dnd', dest='toggle_dnd', action='store_true', help='Toggle Do Not Disturb mode for dunst')
    parser.add_argument('-r, --remove-history', dest='remove_history', action='store_true', help='Clear dunst\'s history')
    # TODO: Create more agnostic option to show no notifications
    # parser.add_argument('-l, --launcher', dest='launcher', help='Specify launcher with arguments in space delimited format')
    #
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    # print(args)
    if args.show_history:
        display_notifications()
    elif args.count:
        get_history_count()
    elif args.toggle_dnd:
        toggle_dnd()
    elif args.remove_history:
        clear_history()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
