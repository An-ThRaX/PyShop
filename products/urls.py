from django.urls import path
from . import views  # "." refers to current folder
urlpatterns = [
    path('', views.index),
    path('new ', views.new)
]
