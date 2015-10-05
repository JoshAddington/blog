from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

import requests

def about(request):
        return render(request, 'about.html')


def contact(request):
        return render(request, 'contact.html')


def resume(request):
        resume = requests.get(settings.MEDIA_URL + 'JoshAddington.pdf', stream=True)
        response = HttpResponse(resume.raw, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="JoshAddington.pdf"'
        return response
