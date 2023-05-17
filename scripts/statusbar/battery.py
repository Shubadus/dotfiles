#!/usr/bin/env python3

import argparse
import math
import pathlib
import subprocess

import psutil

from dataclasses import dataclass
from enum import auto, Enum

BATTERY_ICONS = {
    'Charging': {
        '100': '',
        '90': '',
        '80': '',
        '70': '',
        '60': '',
        '50': '',
        '40': '',
        '30': '',
        '20': '',
        '10': '',
        '0': ''
    },
    'Discharging': {
        '100': '',
        '90': '',
        '80': '',
        '70': '',
        '60': '',
        '50': '',
        '40': '',
        '30': '',
        '20': '',
        '10': '',
        '0': ''
    },
    'Full': {
        '100': ''
    }
}
PRIMARY_BATTERY = list(pathlib.Path('/sys/class/power_supply/').glob('BAT*'))[0]
POWER_PROFILES = (
    'balanced',
    'performance',
    'power-saver'
)


def send_notification(message: str):
    subprocess.call(['notify-send', '-r', '55555', '-u', 'normal', message])


class PowerProfiles(Enum):
    """Battery power profiles provided by powerprofilesctl"""
    Balanced = 'balanced'
    Performance = 'performance'
    PowerSaver = 'power-saver'


@dataclass
class Battery:
    path: pathlib.Path
    health: str = 'Unknown'
    name: str = 'Unknown'
    percent: int = 0
    time_left: str = 'Unknown'
    profile: PowerProfiles = PowerProfiles.Balanced
    status: str = 'Unknown'

    def __str__(self) -> str:
        message = '\n'.join([
            '{:<18} {}'.format('Name:', self.name),
            '{:<18} {}'.format('Status:', self.status),
            '{:<18} {}%'.format('Battery Percent:', self.percent),
            '{:<18} {}%'.format('Battery Health:', self.health),
            '{:<18} {}'.format('Power Profile:', self.profile.capitalize())
        ])
        if self.status == "Discharging":
            message += '\n{:18} {}'.format('Time Remaining:', self.time_left)
        return message

    def get_icon(self):
        icon_percentage = str(math.floor(self.percent/10)*10)
        return BATTERY_ICONS[self.status][icon_percentage]

    #TODO: Try to convert from the profile list to the Enum
    def next_power_plan(self):
        next_index = POWER_PROFILES.index(self.profile) + 1
        if next_index > len(POWER_PROFILES) - 1:
            next_index = 0
        self.set_power_plan(POWER_PROFILES[next_index])
        # power_profiles = PowerProfiles
        # power_profile_list = list(power_profiles)
        # next_index = power_profile_list.index(self.profile.value) + 1
        # if next_index > len(power_profile_list) - 1:
        #     next_index = 0
        #     power_profiles.Balanced
        # self.set_power_plan(PowerProfiles(power_profile_list[next_index]))

    @staticmethod
    def get_time_remaining(seconds: int) -> str: 
        mm, ss = divmod(seconds, 60)
        hh, mm = divmod(mm, 60)
        return '{}:{:02d}'.format(hh, mm)

    @staticmethod
    def get_power_plan():
        return subprocess.check_output(['powerprofilesctl', 'get']).decode().strip("\n")

    @staticmethod
    def set_power_plan(plan: str):
        subprocess.call(['powerprofilesctl', 'set', plan])

    @staticmethod
    def get_health(battery_path: pathlib.Path):
        orig_full_cap = int(battery_path.joinpath('charge_full_design').read_text())
        full_cap = int(battery_path.joinpath('charge_full').read_text())
        return int(full_cap / orig_full_cap * 100)

    @classmethod
    def new(cls, battery: dict, battery_path: pathlib.Path):
        return Battery(
            health=cls.get_health(battery_path),
            name=battery_path.name,
            path=battery_path,
            percent=int(battery.percent),
            profile=cls.get_power_plan(),
            status=battery_path.joinpath('status').read_text().strip('\n'),
            time_left=cls.get_time_remaining(battery.secsleft),
        )


def main(args):
    battery = Battery.new(battery=psutil.sensors_battery(), battery_path=PRIMARY_BATTERY)

    if args.command == 'status':
        return battery.get_icon()

    if args.command == 'left-click':
        send_notification(str(battery))

    if args.command == 'middle-click':
        # next_index = POWER_PROFILES.index(battery.profile) + 1
        # if next_index > len(POWER_PROFILES) - 1:
        #     next_index = 0
        # battery.set_power_plan(POWER_PROFILES[next_index])
        battery.next_power_plan()
        battery.profile = battery.get_power_plan()
        send_notification(f'New Power Profile: {battery.profile.capitalize()}')

    if args.command == 'right-click':
        send_notification(f'Current Power Profile: {battery.profile.capitalize()}')

    # if battery.status == 'Discharging':
    #     battery.set_power_plan('power-saver')
    # else:
    #     battery.set_power_plan('performance')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--c',
        choices=('status', 'left-click', 'middle-click', 'right-click'),
        dest='command',
        default='status',
        help='Allowed values are status, left-click, middle-click and right-click'
    )
    args = parser.parse_args()
    print(main(args), end='')
