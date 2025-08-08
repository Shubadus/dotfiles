#! /usr/bin/env python3
import re


from dataclasses import dataclass
from enum import Enum, auto
import subprocess


class WifiMode(Enum):
    infra = auto()
    mesh = auto()


@dataclass
class WifiConnection:
    in_use: bool
    icon: str
    bssid: str
    ssid: str
    mode: str
    channel: int 
    rate: str
    signal_strength: int 
    security: str

    def __repr__(self):
        if self.ssid == "--":
            self.ssid = "(Hidden Network)"
        return f'{self.ssid}\0icon\x1f{self.icon}'

    def __str__(self):
        return self.__repr__()


def get_network_icon(signal_strength: int) -> str:
    if signal_strength > 80:
        return "network-wireless-100"
    if signal_strength > 60:
        return "network-wireless-80"
    if signal_strength > 40:
        return "network-wireless-60"
    if signal_strength > 20:
        return "network-wireless-40"
    if signal_strength > 0:
        return "network-wireless-20"
    return ""


def remove_duplicate_connections(connection_list):
    existing_connections = set()
    final_connection_list = []
    for connection in connection_list:
        if connection.ssid == "(Hidden Network)":
            final_connection_list.append(connection)
        elif connection.ssid not in existing_connections:
            final_connection_list.append(connection)
            existing_connections.add(connection.ssid)
    return final_connection_list


def main():
    connection_list = []
    wifi_list = subprocess.check_output(['nmcli', 'd', 'wifi', 'list']).decode().split("\n")[1:]
    in_use = False
    for connection in wifi_list:
        connection_items = re.split(r"\s{2,}", connection.strip())

        if connection_items[0] == '*':
            in_use = bool(connection_items.pop(0))

        if len(connection_items) < 2:
            continue

        connection_list.append(
            WifiConnection(
                in_use=in_use,
                bssid=connection_items[0],
                ssid=connection_items[1],
                mode=connection_items[2],
                channel=int(connection_items[3]),
                rate=connection_items[4],
                signal_strength=int(connection_items[5]),
                icon=get_network_icon(int(connection_items[5])),
                security=connection_items[7]
            )
        )
    connection_list.sort(key=lambda x: x.signal_strength)
    connection_list.reverse()

    final_connection_list = remove_duplicate_connections(connection_list)

    # ssid_list = list(set([f'{x.ssid}\0icon\x1f{x.icon}' for x in connection_list]))
    fuzzel = subprocess.run(['fuzzel', '--dmenu'], input="\n".join(str(x) for x in final_connection_list), text=True, capture_output=True)
    if fuzzel.returncode == 1:
        print(fuzzel.returncode)
        print(f"An error occurred when running fuzzel:\n\t{fuzzel.stderr}")
        exit(1)
    print(fuzzel.stdout)
    selected = [x for x in final_connection_list if x.ssid == fuzzel.stdout.strip()][0]
    print(f'{selected.ssid}\n{selected.bssid}\n{selected.signal_strength}\n{selected.security}')
    if selected.security != "--":
        password = subprocess.run(['fuzzel',])
        subprocess.run(['nmcli', 'd', 'wifi', 'connect', selected.bssid, f'password '])

    # print(connection_list)

if __name__ == "__main__":
    main()
