from rest_framework import serializers
from citibike.models import Station, Bike, UpdateTime


class StationSerializer(serializers.ModelSerializer):

        class Meta:
                model = Station
                fields = ('id', 'name', 'availableDocks', 'latitude', 'longitude')


class UpdateTimeSerializer(serializers.ModelSerializer):

        class Meta:
                model = UpdateTime

