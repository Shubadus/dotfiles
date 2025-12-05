#!/usr/bin/env python
import argcomplete
import argparse
import itertools
import json
import subprocess

from typing import Optional


class Ansi:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'


icons = {
    'pacman': '󰏕',
    'aur': '󰏕',
    'flatpak': ''
}


def output_result(update_count, update_body: str):
        module = {}
        if subprocess.run(('pgrep', 'hyprpanel'), capture_output=True).stdout.strip():
            module.update({
                'updates': f'{update_body}',
                'count': f'{update_count}'
            })
        elif subprocess.run(('pgrep', 'waybar'), capture_output=True).stdout.strip():
            module.update({
                'text': f'{update_count}',
                'tooltip': f'{update_body}',
                'class': '',
                'percentage': ''
            })
        else:
            module = update_count
        print(json.dumps(module))


def check_updates(package_manager: str) -> list[str]:
    match package_manager:
        case 'dnf':
            # return subprocess.run(['checkupdates'], text=True, capture_output=True).stdout
            return ['']
        case 'flatpak':
            result = subprocess.run(('flatpak', 'remote-ls', '--updates', '--app'), text=True, capture_output=True).stdout.strip()
            return [x.split('\t')[0] for x in result.split('\n')]
        case 'pacman':
            result = subprocess.run(['checkupdates'], text=True, capture_output=True).stdout.strip()
            return [x.split(' ')[0] for x in result.split('\n')]
        case 'aur':
            result = subprocess.run(['yay', '-Qua'], text=True, capture_output=True).stdout.strip()
            return [x.split('')[0] for x in result.split('\n')]
        case _:
            return ['']



def main():
    # NOTE: For some reason, this outputs nothing, needs investigated
    arch_updates = []
    flatpak_updates = []
    final_updates = []
    update_body = ""
    update_count = 0
    max_count = 10

    flatpak_updates= check_updates(package_manager='flatpak')
    flatpak_updates_count=len(flatpak_updates)

    arch_updates = check_updates(package_manager='pacman')
    arch_updates_count=len(arch_updates)

    # TODO: There is a bug in this logic where an empty return from the check updates function
    # is counted towards the value and gives a false positive on updates being available.
    # Right now, it's waiting until there's at least 2 package updates before anything will show.
    if flatpak_updates_count > 1 or arch_updates_count > 1:
        update_count += arch_updates_count + flatpak_updates_count
        if flatpak_updates_count > max_count:
            flatpak_updates = flatpak_updates[:max_count+1]
            flatpak_updates.append(f'+ {flatpak_updates_count-max_count} more...')
        if arch_updates_count > max_count:
            arch_updates = arch_updates[:max_count+1]
            arch_updates.append(f'+ {arch_updates_count-max_count} more...')

        package_updates = list(itertools.zip_longest(flatpak_updates, arch_updates, fillvalue="  "))

        updates = [
            ['Flatpak Updates', 'Pacman Updates'],
            ['---------------', '--------------'],
        ]
        for update in package_updates:
            updates.append(list(update))

        col_widths = [max(len(str(item)) for item in col) for col in zip(*updates)]

        for row in updates:
            final_updates.append(f" | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row)))
        update_body = '\n'.join(final_updates)

    else:
        update_body = ""
        update_count = ""

    output_result(update_count, update_body)


if __name__ == '__main__':
    main()
