from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Paintings
from . serializers import PaintingsSerializer
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsReadOnly
from django.contrib.auth.models import User


# get all pantings
class AllPaintings(APIView):

    permission_classes = [IsReadOnly]

    # get the user by  uid
    def getUserObject(self, uid):
        try:
            return User.objects.get(id=uid)
        except User.DoesNotExist:
            return None


    # get paintings
    def get(self, request):
        # Get all paintings as per the user id
        # QUERY: user
        if request.GET.get('user'):
            uid = request.GET.get('user')
            user = self.getUserObject(uid)
            
            if not user:
                response_data = {
                    "success": False,
                    "errors": "User doesn't exist"
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)

            paintings = Paintings.objects.filter(owner=user)

        else:
            # Get all paintings
            paintings = Paintings.objects.all()

        serializer = PaintingsSerializer(paintings, many=True)

        response_data = {
            "success": True,
            "message": "Successfully fetched",
            "data": {
                "total": len(serializer.data),
                "paintings": serializer.data
            }
        }
        return Response(response_data)

    # add new painting

    def post(self, request):
        serializer = PaintingsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)

            response_data = {
                "success": True,
                "message": "Added Successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            "success": False,
            "errors": serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class Painting(APIView):
    permission_classes = [IsReadOnly]

    # get the painting by painting id
    def getPaintingObject(self, painting_id):
        try:
            return Paintings.objects.get(id=painting_id)
        except Paintings.DoesNotExist:
            return None

    # get painting by id
    # PARAM: painting_id

    def get(self, request, painting_id):
        # check if painting is exist or not
        painting = self.getPaintingObject(painting_id)

        if not painting:
            response_data = {
                "success": False,
                "errors": "Painting doesn't exist"
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serializer = PaintingsSerializer(painting)

        response_data = {
            "success": True,
            "message": "Fetched Successfully",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    # update painting data
    # PARAM: painting_id

    def put(self, request, painting_id):
        # get_object_or_404(Paintings, id=painting_id)
        painting = self.getPaintingObject(painting_id)

        if not painting:
            response_data = {
                "success": False,
                "errors": "Painting doesn't exist"
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serializer = PaintingsSerializer(painting, data=request.data)

        if serializer.is_valid():
            serializer.save()

            response_data = {
                "success": True,
                "message": "Update Successfully",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        response_data = {
            "success": False,
            "errors": serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    # delete painting data

    def delete(self, request, painting_id):
        painting = self.getPaintingObject(painting_id)

        if not painting:
            response_data = {
                "success": False,
                "errors": "Painting doesn't exist"
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        painting.delete()

        response_data = {
            "success": True,
            "message": "Deleted Successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
