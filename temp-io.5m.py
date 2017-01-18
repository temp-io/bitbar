#!/usr/bin/python
# -*- coding: utf-8 -*-

# <bitbar.title>Temp-io</bitbar.title>
# <bitbar.version>v1.0.0</bitbar.version>
# <bitbar.author>Ten Wong</bitbar.author>
# <bitbar.author.github>awong1900</bitbar.author.github>
# <bitbar.desc>TODO</bitbar.desc>
# <bitbar.image>TODO</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

import json
import urllib2
from datetime import datetime

# set temp-io device config, you can set multi
temp_list = [
    {
        "user_id": "qjRCYdbxNLZf335KxUW6TGNEbf03",
        "temp_id": "9098af0dfb31f2e1a84cbdbb3c2450bd"
    },
    {
        "user_id": "qjRCYdbxNLZf335KxUW6TGNEbf03",
        "temp_id": "cc7bcfa0ebc97044068553831d5f92b4"
    }
]

# set to si for metric, leave blank for imperial
units = 'si'


def get_temps(json_temps=None):
    if json_temps is None:
        return None
    temps = []
    for t in json_temps:
        temp = json.load(urllib2.urlopen('https://api.temp-io.life/v1/users/{}/temps/{}'
                                         .format(t['user_id'], t['temp_id'])))
        temps.append(temp)
    return temps


def get_unit():
    if units == 'si':
        unit = 'C'
    else:
        unit = 'F'
    return unit


def get_temp_string(temp):
    unit = get_unit()
    if unit == 'C':
        temp_string = '{}°C'.format(temp['temperature'])
    else:
        temp_string = '{}°F'.format(temp['temperature_f'])
    return temp_string


def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"


def main():
    temps = get_temps(temp_list)
    temp_string_list = [get_temp_string(temp) for temp in temps]
    title = ' - '.join(temp_string_list)
    print(title)
    print("---")
    str1 = ' - '.join([temp['name'] for temp in temps])
    print("{} | size=16".format(str1))
    
    str2 = ' - '.join([pretty_date(datetime.strptime(temp['temperature_updated_at'], '%Y-%m-%dT%H:%M:%SZ')) for temp in temps])
    print(str2)

    # print("---")
    # print("About - Temp-io| size=16")
    # print("A useful IOT device to obtain the current temperature. | size=14 href=https://develops.temp-io.life")

if __name__ == '__main__':
    main()
