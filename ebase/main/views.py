from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from main.models import Climb

def main(request):
    return HttpResponse("this is the main page :)")

def climbs(request):
    climbs = Climb.objects.all()

    context = { 'climbs': climbs, }
    return HttpResponse(render(request, 'main/climbs.html', context))

# Create your views here.
