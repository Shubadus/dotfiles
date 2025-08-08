#! /usr/bin/env python3
import subprocess
import json


# TODO: Display list of objects from dunst history, show the selected message using 'dunstctl history-pop'


def main():
    history = json.loads(subprocess.run(["dunstctl", "history"], capture_output=True).stdout.decode()).get('data')[0]
    print(history)
    summaries = [f'{x.get('appname').get('data')}:  {x.get('summary').get('data')}' for x in history]
    print([len(x) for x in summaries])
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
            f'{len('No notification history') - 6}'
        ])
    else:
        longest_name = len(max(summaries, key=len))
        print(longest_name)
        process.extend([
            '--width',
            f'{longest_name - 4}',
            '--hide-prompt'
        ])
    selection = subprocess.run(process, input="\n".join(summaries), capture_output=True, text=True).stdout
    if selection:
        print(selection)
        subprocess.run(['dunstctl', 'history-pop', f'{history[int(selection)].get('id').get('data')}'])


if __name__ == "__main__":
    main()
