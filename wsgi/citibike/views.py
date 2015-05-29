from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from citibike.models import Station, UpdateTime
from citibike.serializers import StationSerializer, UpdateTimeSerializer


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


@api_view(['GET'])
def timeline_collection(request):
        if request.method == 'GET':
                timeline = UpdateTime.objects.all()
                serializer = UpdateTimeSerializer(timeline, many=True)
                return Response({'timeline': serializer.data})


@api_view(['GET'])
def timeline_date(request, date):
        try:
                timeline = UpdateTime.objects.filter(date=date).order_by('time')
        except UpdateTime.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
                serializer = UpdateTimeSerializer(timeline, many=True)
                return Response({'timeline': serializer.data})


@api_view(['GET'])
def data_collection(request):
        if request.method == 'GET':
                stations = Station.objects.all()
                station_serializer = StationSerializer(stations, many=True)
                timeline = UpdateTime.objects.all()
                return Response({'stations': station_serializer.data})
