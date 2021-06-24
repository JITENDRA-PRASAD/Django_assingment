from django.urls import path
from . import views

urlpatterns = [
    path("jan/",views.index),
    path("feb/",views.index)
]