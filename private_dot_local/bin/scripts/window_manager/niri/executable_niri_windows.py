#!/usr/bin/env python
from re import sub
import subprocess
import pprint

def main():
    result = subprocess.run(['niri', 'msg', 'windows'], capture_output=True, text=True)
    windows = []
    for window in result.stdout.split('\n\n'):
        try:
            window_values = {}
            for value in window.split('\n'):
                value = value.strip().replace('"', '')
                # We assume it's the Niri Window ID
                try:
                    if "Window ID" in value:
                        k = " ".join(value.split(" ", 2)[:2])
                        v = value.split(" ", 2)[2].split(':')[0]
                    else:
                        k,v = value.split(':', 1)
                        v = v.strip()
                    window_values.update({k:v})
                except Exception as e:
                    print(e)
                    print(value)
            if window_values:
                windows.append(window_values)
        except Exception as e:
            print(e)
            print(window)

    pp = pprint.PrettyPrinter()
    pp.pprint(windows)
    window_titles = [x['Title'] for x in windows]

    result = subprocess.run(['fuzzel', '--dmenu', '--prompt','Niri Windows: '], input='\n'.join(window_titles), capture_output=True, text=True)
    result.check_returncode()
    selected_title = result.stdout.strip()

    # for x in windows:
    #     if x['Title'] == selected_title:
    #         id = x['Window ID']
    #         print(id)

    id = [x['Window ID'] for x in windows if selected_title  == x['Title']]
    print(id)

    subprocess.run(['niri', 'msg', 'action', 'focus-window', '--id', id[0]], text=True)

    pass

if __name__ == '__main__':
    main()
