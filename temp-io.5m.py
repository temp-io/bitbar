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
user_id = 'OCbl1hXpURcGp1s8MvyDxA27P5P2'

# temp id
temp_id = '50f7fa7ab532a9538fd1386d17b016c4'

# token, if public, could not fill
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjI0MTE2NWVlYTAzOGFmYmZjOWE4Mjc3YmUzODJhNjQ4MTY3YzAyMGEifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vd2lvYXBwLWM3MGE4IiwibmFtZSI6IldvbmcgVGVuIiwicGljdHVyZSI6Imh0dHBzOi8vc2NvbnRlbnQueHguZmJjZG4ubmV0L3YvdDEuMC0xL3MxMDB4MTAwLzExMjIyNDYzXzEwNjg0MTIxMzAxMzA4OF8xMDgxNzE3OTQxOTcwNzM3NDk1X24uanBnP29oPTYwMzg3NmYxMTQ3MWE0YTU2YTI1NWM5NmQ3MDQxYjJiJm9lPTU4OTg4MEE3IiwiYXVkIjoid2lvYXBwLWM3MGE4IiwiYXV0aF90aW1lIjoxNDgwMzI4NTUwLCJ1c2VyX2lkIjoiT0NibDFoWHBVUmNHcDFzOE12eUR4QTI3UDVQMiIsInN1YiI6Ik9DYmwxaFhwVVJjR3AxczhNdnlEeEEyN1A1UDIiLCJpYXQiOjE0ODE3NjYwNTQsImV4cCI6MTQ4MTc2OTY1NCwiZW1haWwiOiJhd29uZzE5MDBAaG90bWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZmFjZWJvb2suY29tIjpbIjI2ODAzNjEwMzU2MDI2NCJdLCJlbWFpbCI6WyJhd29uZzE5MDBAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJmYWNlYm9vay5jb20ifX0.WFWqPYaKVTqn68nA15g2kJ7zTq9mDGmShoHPIz3hq-6FGmqjVPx08K87Eev0x7FXYcTL_u-AT8yc69KYKvAdw8lqC5BdWGRoF5OOzSLyXIK3sVtXM9rQwqccHjrPBUadRp414-wHMNG3KcRJPa3NYJ9tdqKeIkx0kTiT32ZMbEMUvb686TiQmDrp6QthORe7ETj23NX0hrOFldLYR2oV_vOzi0UVMbsNIWHGomHHaVD4i5_UlY08W5K46XSf4Sp1NUzsc3149oQ8J2sSCIUSk5jGIVqj6pltDf0GaGFkjBwp-vc0NHF6HraYyyO59VxI2rpHahCoc9-MOITmXdOgsg'

# set to si for metric, leave blank for imperial
units = ''

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

if __name__ == '__main__':
    main()
