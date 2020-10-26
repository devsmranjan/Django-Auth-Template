from django.urls import path
from . import views

urlpatterns = [
    path('', views.allPaintings, name="all paintings"),
    path('<str:painting_id>', views.painting, name="painting"),
]
