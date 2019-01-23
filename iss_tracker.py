from tkinter import *

import json
import urllib.request


class Tracker:
    def __init__(self, master):
        self.master = mastermaster.title("ISS Tracker")

        self.screen = 


root = Tk()
my_gui = Tracker(root)
root.mainloop()

atros_url = 'http://api.open-notify.org/astros.json'
astros_response = urllib.request.urlopen(atros_url)
astros_result = json.loads(astros_response.read())

location_url = 'http://api.open-notify.org/iss-now.json'
location_response = urllib.request.urlopen(location_url)
location_result = json.loads(location_response.read())

print('People in space: ', astros_result['number'])

people = astros_result['people']

for p in people:
    print(p['name'])

location = location_result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

# screen = turtle.Screen()
# screen.setup(720, 360)
# screen.setworldcoordinates(-180, -90, 180, 90)
# screen.bgpic('map.gif')