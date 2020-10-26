from django.urls import path
from . import views

urlpatterns = [
    path('', views.decidePage, name="decide page"),
]
