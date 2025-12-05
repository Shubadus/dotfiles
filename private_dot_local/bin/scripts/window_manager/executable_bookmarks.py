#!/usr/bin/env python
import argparse
import json
import subprocess


from pathlib import Path


def main(file_path: str, runner: str, browser: str):
    # Using a dictionary for quick lookup of the bookmark URL after a bookmark is selected
    new_bookmarks = dict()

    # Fuck it, we ball recursively
    def parse_bookmarks(bookmark_data: dict, folder_name = None):
        for bookmark in bookmark_data:
            if bookmark.get('type') == 'folder':
                parse_bookmarks(bookmark.get('children'), folder_name=bookmark.get('name'))
            elif bookmark.get('type') == 'url':
                if folder_name: 
                    new_bookmarks.update({f'[{folder_name}] {bookmark['name']}': bookmark['url']})
                else:
                    new_bookmarks.update({f'{bookmark['name']}': bookmark['url']})
            else:
                pass

    with open(Path(file_path).resolve()) as file:
        bookmarks=json.load(file)

    parse_bookmarks(bookmarks.get('roots').get('other').get('children'))

    options='\n'.join(new_bookmarks.keys())
    result = subprocess.run(runner, input=options, capture_output=True, text=True, shell=True).stdout.strip()
    if result:
        subprocess.run(browser + f' {new_bookmarks[result]}', text=True, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='File path of the Chromium-based bookmark file to read')
    parser.add_argument('-r,--runner', dest='runner', help='dmenu launcher/runner command to use', default='fuzzel --dmenu --prompt=Bookmarks: ')
    parser.add_argument('-b,--browser', dest='browser', help='browser command to use', default='chromium')

    args = parser.parse_args()

    main(file_path=args.file_path, runner=args.runner, browser=args.browser)
