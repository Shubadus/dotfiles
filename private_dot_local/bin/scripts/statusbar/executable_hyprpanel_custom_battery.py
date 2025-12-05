#!/usr/bin/env python3
import argparse
import json

from pathlib import Path


battery_states = {
    'battery_high'
}


def main(device: str):
    battery_path = Path('/sys/class/power_supply/').resolve()
    for bat in battery_path.glob("hidpp_battery_*"):
        if device in bat.joinpath('model_name').read_text().lower() and 'unknown' not in bat.joinpath('status').read_text().lower():
            battery_percent = bat.joinpath('capacity').read_text().strip()
            battery_status = bat.joinpath('status').read_text().strip()
            battery_device = bat.joinpath('model_name').read_text().strip()
            manufacturer = bat.joinpath('manufacturer').read_text().strip()

            tooltip = f'{manufacturer} {battery_device.split()[0]}\n{battery_status.capitalize()} {battery_percent}%'

            match int(battery_percent):
                case t if t < 15:
                    battery_state = 'critical'
                case t if t < 30:
                    battery_state = 'low'
                case t if t > 30:
                    battery_state = 'normal'
                case _:
                    battery_state = 'unknown'


            waybar_module = {
                'text': battery_device,
                'alt': battery_status.lower(),
                'tooltip': tooltip,
                'class': battery_state,
                'percentage': int(battery_percent)
            }
            print(json.dumps(waybar_module))
            exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('device', help='Specify the type of device to search for', type=str)
    args  = parser.parse_args()
    main(args.device)
