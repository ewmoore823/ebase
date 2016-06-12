from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from main.models import climb_models


def login(request):
    return HttpResponse(render(request, 'main/login.html', {}))


@login_required
def main(request):
    return HttpResponse("this is the main page :)")


@login_required
def climbs(request):
    climbs = climb_models.Climb.objects.all()

    context = {'climbs': climbs, }
    return HttpResponse(render(request, 'main/climbs.html', context))


@login_required
def site(request):
    context = {}
    return HttpResponse(render(request, 'main/site.html', context))


# Views for Testing package installations

@login_required
def foundation(request):
    return HttpResponse(render(request, 'main/foundation.html', {}))


@login_required
def test(request):
    return HttpResponse(render(request, 'main/test.html', {}))
