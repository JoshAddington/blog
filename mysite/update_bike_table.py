import requests
import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

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


def update_table(json_file):
    update, create_update = UpdateTime.objects.get_or_create(
            time=time,
            date=date
    )
    for row in json_file:
        station = check_stations(row)
        add_bikes_row(row, station, update)


# checks JSON stations against DB stations.
# Citibike sometimes changes the ID number of stations,
# this is to ensure that bike data is staying consistent when
# compared to station data
def check_stations(row):
    station, create_station = Station.objects.get_or_create(
            name=row['stationName'], defaults={'station_id': row['id'],
            'availableDocks': (row['availableDocks'] + row['availableBikes']),
            'latitude': row['latitude'],
            'longitude': row['longitude']})
    return station


# take in a json file row
# parse and add to Bike Model
def add_bikes_row(row, station, update):
    bike, create_bike = Bike.objects.get_or_create(
            station=station,
            update=update,
            number_of_bikes=row['availableBikes'])


if __name__ == '__main__':
    update_table(station_info)
