from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from citibike.models import Station
from citibike.serializers import StationSerializer


@api_view(['GET'])
def station_collection(request):
        if request.method == 'GET':
                stations = Station.objects.all()
                serializer = StationSerializer(stations, many=True)
                return Response({'stations': serializer.data})


@api_view(['GET'])
def station_element(request, pk):
        try:
                station = Station.objects.get(pk=pk)
        except Station.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
                serializer = StationSerializer(station)
                return Response(serializer.data)
