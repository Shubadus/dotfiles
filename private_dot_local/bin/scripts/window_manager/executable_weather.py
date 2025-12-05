#!/usr/bin/env python
import argparse
import json
from typing import Optional
import urllib.request
import urllib.error
import subprocess

icons = {
    "Unknown": "󰨹",
    "Cloudy": "",
    "Clear": "󰖔",
    "Fog": "",
    "HeavyRain": "",
    "HeavyShowers": "",
    "HeavySnow": "",
    "HeavySnowShowers": "",
    "LightRain": "",
    "LightShowers": "",
    "LightSleet": "",
    "LightSleetShowers": "",
    "LightSnow": "",
    "LightSnowShowers": "",
    "PartlyCloudy": "",
    "Sunny": "",
    "ThunderyHeavyRain": "",
    "ThunderyShowers": "",
    "ThunderySnowShowers": "",
    "VeryCloudy": "",
    "Overcast": "",
}


def web_request(url: str) -> dict:
    # NOTE: This inserts https:// in front of url if present. We don't care about other request types
    if not url.startswith('https://'):
        url=f'https://{url}'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            reply = html.decode('utf-8')
            # NOTE: We'll assume any response that starts with { is JSON
            if reply.startswith('{'):
                return json.loads(reply)
            return reply
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e.reason}")
        exit(1)


def forecast():
    subprocess.run(['pkill weather || foot --app-id weather -e bash -c "curl wttr.in; read"'], shell=True)


def current_weather(location: Optional[str] = None):
    weather_site="wttr.in"
    if location:
        weather_site=f"wttr.in/{location}"

    response = web_request(f'{weather_site}?format=j1')

    current_location = response.get('nearest_area')
    if current_location:
        current_location = current_location[0]

    current_weather = response.get('current_condition')
    if current_weather:
        current_weather = current_weather[0]

        final_tooltip = []
        tooltip = [
            [f" {current_weather.get('temp_F')} °F",           f"󰖎 {current_weather.get('humidity')} %"],
            [f"󰈈 {current_weather.get('visibilityMiles')} mph", f" {current_weather.get('windspeedMiles')} mph"],
            [f"󱣖 {current_weather.get('uvIndex')}",             f" {current_weather.get('pressureInches')} in"]
        ]
        title = f"{current_location.get('areaName')[0].get('value')}, {current_location.get('region')[0].get('value')}"
        col_widths = [max(len(str(item)) for item in col) for col in zip(*tooltip)]
        final_tooltip.append(title)
        final_tooltip.append(current_weather.get('weatherDesc')[0].get('value'))
        for row in tooltip:
            final_tooltip.append(f" | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row)))


        weather_icon = icons.get(current_weather.get('weatherDesc')[0].get('value'), icons['Unknown'])
        # print(current_weather.get('weatherDesc')[0].get('value'))

        json_reply = {
            'text': f'{current_weather.get('temp_F', 'Unknown')}',
            'alt': f'{weather_icon}',
            'tooltip': "\n".join(final_tooltip)
        }
        print(json.dumps(json_reply))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l, --location', dest='location', help='Location to pull weather info from')
    parser.add_argument('-F, --forecast', dest='forecast', action='store_true', help='Pull weather forecast on terminal')
    args = parser.parse_args()

    if args.forecast:
        forecast()
        exit(0)

    if args.location:
        current_weather(args.location)
    else:
        current_weather()

