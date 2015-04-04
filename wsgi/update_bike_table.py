import requests
import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openshift.settings")

import django
django.setup()

from citibike.models import Station, Bike, UpdateTime


# CRON job to update bike table
# request feed and convert to JSON
res = requests.get('http://www.citibikenyc.com/stations/json')
json_response = res.json()
station_info = json_response['stationBeanList']
# postgres needs 24 hour time, citibike supplies 12 w/ am/pm
execution_time = datetime.datetime.strptime(json_response['executionTime'], "%Y-%m-%d %I:%M:%S %p").strftime("%Y-%m-%d %H:%M:%S")
# split datetime into date and time
date = execution_time[0:10]
time = execution_time[11:]


def add_stations(json_file):
        for row in json_file:
                s = Station.objects.get_or_create(
                    id=row['id'],
                    name=row['stationName'],
                    availableDocks=(row['availableDocks'] + row['availableBikes']),
                    latitude=row['latitude'],
                    longitude=row['longitude'])


def add_bikes(json_file):
        update = UpdateTime.objects.get_or_create(
            time=time,
            date=date)
        for row in json_file:
                station_id = Station.objects.get(id=row['id'])
                bike = Bike.objects.get_or_create(
                    station=station_id,
                    update=update[0],
                    number_of_bikes=int(row['availableBikes']))


if __name__ == '__main__':
        add_bikes(station_info)
