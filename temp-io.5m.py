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

# user id
user_id = 'qjRCYdbxNLZf335KxUW6TGNEbf03'

# temp id
temp_id = '9098af0dfb31f2e1a84cbdbb3c2450bd'

# token, if public, could not fill
# token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImRiOWRiMmIwNmY4YjU0ZjZiNjRhYTM3ZjY2ODVmMzViYTRlODY1ODQifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vd2lvYXBwLWM3MGE4IiwibmFtZSI6IldvbmcgVGVuIiwicGljdHVyZSI6Imh0dHBzOi8vc2NvbnRlbnQueHguZmJjZG4ubmV0L3YvdDEuMC0xL3MxMDB4MTAwLzExMjIyNDYzXzEwNjg0MTIxMzAxMzA4OF8xMDgxNzE3OTQxOTcwNzM3NDk1X24uanBnP29oPTYwMzg3NmYxMTQ3MWE0YTU2YTI1NWM5NmQ3MDQxYjJiJm9lPTU4OTg4MEE3IiwiYXVkIjoid2lvYXBwLWM3MGE4IiwiYXV0aF90aW1lIjoxNDgwMzI4NTUwLCJ1c2VyX2lkIjoiT0NibDFoWHBVUmNHcDFzOE12eUR4QTI3UDVQMiIsInN1YiI6Ik9DYmwxaFhwVVJjR3AxczhNdnlEeEEyN1A1UDIiLCJpYXQiOjE0ODM5NDk0MTMsImV4cCI6MTQ4Mzk1MzAxMywiZW1haWwiOiJhd29uZzE5MDBAaG90bWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZmFjZWJvb2suY29tIjpbIjI2ODAzNjEwMzU2MDI2NCJdLCJlbWFpbCI6WyJhd29uZzE5MDBAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJmYWNlYm9vay5jb20ifX0.h7RcTERqGQAC1t23Qb9oQJNl3J36298PJ57PU2O5_pljiAXSKXRTnsQH-XnL-MDgqHHd6b1q4MII16a5_wgaJAgnVpY5wedhqkUbU9_OUeizLuozEEeO7S9OLCDoDzjmU1GrygSauP1wEIB1nCKu3UyMBWbL_FuwrR6qv0B-LDYNO9zeYbQNTZ-LVTOLCVvdPVetuhNts20rFKrNU6VQvlFNotNMLLMCaohWsSxkLzuj3jw34N6KE67m8g7oWN_FiXg4jz7pmkv3_DqgkBQk1A8jE8zNM-n6BUr94XNdjKsESut2WtnjQJyc30s7cOTAYFAgzK4UUnyb8NV0IsapXg'
token = ''

# set to si for metric, leave blank for imperial
units = 'si'

# print("25°C")
# print("---")
# print("Balcony | size=18 href=https://temp-io.life")
# print("A useful IOT device to obtain the current temperature. | size=14")


def get_temp():
    temp = json.load(urllib2.urlopen('https://api.temp-io.life/v1/users/{}/temps/{}?access_token={}'.format(
        user_id, temp_id, token)))
    return temp


def get_unit():
  if units == 'si':
    unit = 'C'
  else:
    unit = 'F'
  return unit
  
 
def gen_plot():
    import json
    from datetime import datetime

    with open('/Users/tenwong/Documents/Github/temp-io_bitbar/test_data.json') as f:
        json_data = json.loads(f.read())
        temps = json_data['temperatures']
        
    x = [datetime.strptime(temp['created_at'], '%Y-%m-%dT%H:%M:%SZ') for temp in temps]
    y = [temp['temperature'] for temp in temps]

    import matplotlib.pyplot as plt
    # plt.style.use('dark_background')
    plt.plot(x,y, '-')
    # plt.fill_between(x, 0, y, color='k')
    plt.axis([x[0], x[-1], 10, 30])
    plt.gcf().autofmt_xdate()
    plt.savefig('/Users/tenwong/Documents/Github/temp-io_bitbar/a.png', bbox_inches='tight')
    return '/Users/tenwong/Documents/Github/temp-io_bitbar/a.png'
    
def print_plot():
    file_name = gen_plot()
    import base64
    with open(file_name, "rb") as f:
        encoded_string = base64.b64encode(f.read())
        
    print("---")
    print("| image={}".format(encoded_string))

def main():
    temp = get_temp()
    unit = get_unit()
    if unit == 'C':
        print("{}°{}".format(temp['temperature'], unit))
    else:
        print("{}°{}".format(temp['temperature_f'], unit))
    print("---")
    print("{} | size=18 href=https://api.temp-io.life/v1/users/{}/temps/{}?access_token={}".format(
        temp['name'], user_id, temp_id, token))
    print("{} | size=14".format(temp['description']))

    print_plot()
if __name__ == '__main__':
    main()
