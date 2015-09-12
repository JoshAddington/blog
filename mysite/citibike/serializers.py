from rest_framework import serializers
from .models import Station, Bike, UpdateTime

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('station_id', 'name', 'available_docks', 'latitude', 'longitude')


class StationBikeSerializer(serializers.ModelSerializer):
    bike_count = serializers.SerializerMethodField('station_bike_count')
    bike_update = serializers.SerializerMethodField('station_bike_update')

    class Meta:
        model = Station
        fields = ('station_id', 'name', 'available_docks', 'latitude', 'longitude', 'bike_count', 'bike_update')

    def station_bike_count(self, obj):
        bikes = Bike.objects.filter(station=obj).order_by('update')
        return bikes.values_list('number_of_bikes', flat=True)

    def station_bike_update(self, obj):
        bikes = Bike.objects.filter(station=obj).order_by('update')
        updates = bikes.values_list('created_at', flat=True)
        update_list = [update.strftime("%A, %B %d, %Y %I:%M %p") for update in updates]
        return update_list
