import os
import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def about(request):
        return render(request, 'about.html')


def contact(request):
        return render(request, 'contact.html')


def boroughs(request):
        return JsonResponse(json.loads(open(os.path.join(settings.STATIC_ROOT, 'js', 'nyc.json')).read()))
