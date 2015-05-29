from rest_framework import serializers
from citibike.models import Station, UpdateTime


class StationSerializer(serializers.ModelSerializer):

        class Meta:
                model = Station
                fields = ('id', 'name', 'availableDocks', 'latitude', 'longitude')


class UpdateTimeSerializer(serializers.ModelSerializer):

        class Meta:
                model = UpdateTime
                fields = ('id', 'time', 'date')

