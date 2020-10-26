from django.shortcuts import render
from django.http import HttpResponse


# get user
def user(request, uid):
    # TODO: Get user as per the uid
    return HttpResponse("User details of " + uid)
