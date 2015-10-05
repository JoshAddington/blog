import json
import os

from django.conf import settings
from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Station, UpdateTime, Bike
from .serializers import StationSerializer, StationBikeSerializer, StationMapSerializer


# Create your views here.
def boroughs(request):
    return JsonResponse(
        json.loads(open(
            os.path.join(settings.STATIC_ROOT, 'citibike', 'nyc.json')).read()
            )
        )


@api_view(['GET'])
def citibike_map(request):
    if request.method == 'GET':
        stations = Station.objects.all().prefetch_related(Prefetch('bikes', queryset=Bike.objects.order_by('update')))
        station_serializer = StationMapSerializer(stations, many=True)
        updates = UpdateTime.objects.values_list('datetime', flat=True)
        return Response({'stations': station_serializer.data,
                         'updates': updates})


@api_view(['GET'])
def station_collection(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response({'stations': serializer.data})


@api_view(['GET'])
def station_detail(request, pk):
    if request.method == 'GET':
        station = get_object_or_404(Station, station_number=pk)
        serializer = StationSerializer(station)
        return Response({'station': serializer.data})


@api_view(['GET'])
def station_bikes(request, pk):
    if request.method == 'GET':
        station = get_object_or_404(Station.objects.all().prefetch_related(Prefetch('bikes', queryset=Bike.objects.order_by('update'))), station_number=pk)
        serializer = StationBikeSerializer(station)
        return Response({'station': serializer.data})


@api_view(['GET'])
def updates(request):
    if request.method == 'GET':
        updates = UpdateTime.objects.values_list('datetime', flat=True)
        return Response({'updates': updates})
