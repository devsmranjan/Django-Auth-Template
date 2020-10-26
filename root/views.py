from django.shortcuts import render
from django.http import HttpResponse


def decidePage(request):
    # TODO: Check authntication and redirect to page accordingly
    return HttpResponse("If authenticated user, then redirect to paintings, otherwise redirect to login screen")
