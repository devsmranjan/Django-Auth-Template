from django.shortcuts import render
from django.http import HttpResponse


# get all pantings
def allPaintings(request):
    # get paintings of a specifuc user
    if request.GET.get('user'):
        # TODO: Get all paintings as per the user id
        return HttpResponse("Get All paintings from user " + request.GET.get('user'))

    # check request type, if post then add data
    if request.method == 'POST':
        # TODO: Check auth

        # TODO: Add new panting to database in Paintings Table and that Painting id in User Table
        return HttpResponse("Added new painting")

    # TODO: get all paintings
    return HttpResponse("Get All paintings")


# a single painting
def painting(request, painting_id):
    # update painting data
    if request.method == 'PUT':
        # TODO: Check auth
        # TODO: update painting data
        return HttpResponse("Update painting data to " + painting_id)

    # delete painting data
    if request.method == 'DELETE':
        # TODO: Check auth
        # TODO: delete painting data
        return HttpResponse("Delete painting data : " + painting_id)

    # TODO: get painting details from Pantings Table as per the painting_id
    return HttpResponse("Get painting details of " + painting_id)
