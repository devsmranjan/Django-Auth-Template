from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.AllPaintings.as_view()),
    path('<str:painting_id>', views.Painting.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
