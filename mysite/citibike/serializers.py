from datetime import datetime
from rest_framework import serializers
from .models import Station, Bike, UpdateTime


class BikeInStationField(serializers.RelatedField):
        def to_representation(self, value):
                return value.number_of_bikes


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('station_id',
                  'name',
                  'available_docks',
                  'latitude',
                  'longitude')


class StationBikeSerializer(serializers.ModelSerializer):
    bikes = BikeInStationField(many=True, read_only=True)
    bike_update = serializers.SerializerMethodField('station_bike_update')

    class Meta:
        model = Station
        fields = ('station_id',
                  'name',
                  'available_docks',
                  'latitude',
                  'longitude',
                  'bike_update',
                  'bikes')

    def station_bike_update(self, obj):
        bikes = Bike.objects.filter(station=obj).order_by('update')
        updates = bikes.values_list('created_at', flat=True)
        update_list = [update.strftime("%A, %B %d, %Y %I:%M %p") for update in updates]
        return update_list


class StationMapSerializer(serializers.ModelSerializer):
    bikes = BikeInStationField(many=True, read_only=True)

    class Meta:
        model = Station
        fields = ('station_id',
                  'name',
                  'available_docks',
                  'latitude',
                  'longitude',
                  'bikes')
