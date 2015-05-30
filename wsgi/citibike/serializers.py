from rest_framework import serializers
from citibike.models import Station, Bike, UpdateTime


# return an array of the number of bikes at a station
class BikeInStationSerializer(serializers.RelatedField):
        def to_representation(self, value):
                return value.number_of_bikes


class BikeUpdateSerializer(serializers.RelatedField):
        def to_representation(self, value):
                return value.__str__


class UpdateTimeSerializer(serializers.ModelSerializer):

        class Meta:
                model = UpdateTime
                fields = ('id', 'time', 'date')


class BikeSerializer(serializers.ModelSerializer):
        bike_update = BikeUpdateSerializer(many=True, read_only=True)

        class Meta:
                model = Bike
                fields = ('update', 'station', 'number_of_bikes')


class StationSerializer(serializers.ModelSerializer):

        class Meta:
                model = Station


class StationBikeSerializer(serializers.ModelSerializer):
        bikes =  BikeInStationSerializer(many=True, read_only=True)

        class Meta:
                model = Station
                fields = ('id', 'name', 'availableDocks', 'latitude',
                             'longitude', 'bikes')

