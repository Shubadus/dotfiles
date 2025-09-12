#!/usr/bin/env python
import argcomplete
import argparse
import json
import subprocess


class Ansi:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'


icons = {
    'pacman': '󰏕',
    'flatpak': ''
}


def check_updates(package_manager: str) -> list[str]:
    match package_manager:
        # case 'dnf':
            # return subprocess.run(['checkupdates'], text=True, capture_output=True).stdout
            # return ['']
        case 'flatpak':
            result = subprocess.run(('flatpak', 'remote-ls', '--updates', '--app'), text=True, capture_output=True).stdout.strip()
            return [x.split('\t')[0] for x in result.split('\n')]
        case 'pacman':
            result = subprocess.run(['checkupdates'], text=True, capture_output=True).stdout.strip() #.split('\n')
            return [x.split(' ')[0] for x in result.split('\n')]
        case _:
            return ['']


def run_updates(package_manager: str, terminal: str) -> None:
    process_args = terminal.split()
    match package_manager:
        case 'dnf':
            return
        case 'flatpak':
            process_args.extend(['flatpak', 'update'])
        case 'pacman':
            process_args.extend(['yay'])
    result = subprocess.run(process_args)
    result.check_returncode()


def send_notification(app_name: str, summary: str, message: str) -> None:
    result = subprocess.run((
        'notify-send',
        '-a', app_name,
        '-c', 'update',
        '-u', 'normal',
        summary,
        message
    ))
    result.check_returncode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p, --package_manager', dest='package_manager', choices=['flatpak', 'pacman'], help="Which package manager to run this script against")
    parser.add_argument('-c, --check', dest='check', action='store_true', help="Check only for updates and exit")
    parser.add_argument('-u, --update', dest='update', action='store_true', help="Run updates via your terminal of choice and exit")
    parser.add_argument('-t, --terminal', dest='terminal', type=str, nargs='?', help="Specify the command for the terminal you want to run this script")

    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if args.check:
        updates = check_updates(package_manager=args.package_manager)
        if updates and len(updates) == 1 and '' in ['']:
            return
        update_count = len(updates)
        updates.insert(0, "Updates:")
        update_body = '\n - '.join(updates)
        module = {}
        if subprocess.run(('pgrep', 'hyprpanel'), capture_output=True).stdout.strip():
            module.update({
                'updates': f'{update_body}',
                'count': f'{update_count}'
            })
        elif subprocess.run(('pgrep', 'waybar'), capture_output=True).stdout.strip():
            module.update({
                # 'text': f'{icons.get(args.package_manager)} {update_count}',
                'text': f'{update_count}',
                'tooltip': f'{update_body}',
                'class': '',
                'percentage': ''
            })
        print(json.dumps(module))
    if args.update:
        if not args.terminal:
            print(f'{Ansi.RED}error{Ansi.RESET}: cannot run updates without a {Ansi.UNDERLINE}{Ansi.BOLD}terminal{Ansi.RESET} specified')
            parser.print_help()
        run_updates(package_manager=args.package_manager, terminal=args.terminal)



if __name__ == '__main__':
    main()
