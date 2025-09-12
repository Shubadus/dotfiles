#!/usr/bin/env python
import json
import subprocess


from pathlib import Path


def main():
    new_bookmarks = dict()
    with open(Path.home().joinpath('.config/chromium/Default/Bookmarks')) as file:
        bookmarks=json.load(file)

    for bookmark_folder in bookmarks['roots']['other']['children']:
        for bookmark in bookmark_folder['children']:
                new_bookmarks.update({f'{bookmark_folder['name']} Folder - {bookmark['name']}': bookmark['url']})

    options='\n'.join(new_bookmarks.keys())
    result = subprocess.run(['fuzzel', '--dmenu', '--prompt=Bookmarks: '], input=options, capture_output=True, text=True).stdout.strip()
    if result:
        subprocess.run(['chromium', '--new-window', f'{new_bookmarks[result]}' ], text=True)


if __name__ == '__main__':
    main()
