from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('<str:uid>', views.GetUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
