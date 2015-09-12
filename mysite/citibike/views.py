import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Station
from .serializers import StationSerializer, StationBikeSerializer

# Create your views here.
def boroughs(request):
        return JsonResponse(json.loads(open(os.path.join(settings.STATIC_ROOT, 'citibike', 'nyc.json')).read()))


@api_view(['GET'])
def station_collection(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def station_detail(request, pk):
    if request.method == 'GET':
        station = get_object_or_404(Station, station_id=pk)
        serializer = StationSerializer(station)
        return Response(serializer.data)

@api_view(['GET'])
def station_bikes(request, pk):
    if request.method == 'GET':
        station = get_object_or_404(Station, station_id=pk)
        serializer = StationBikeSerializer(station)
        return Response(serializer.data)
