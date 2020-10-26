from django.urls import path
from . import views

urlpatterns = [
    path('<str:uid>', views.user, name="user"),
]
