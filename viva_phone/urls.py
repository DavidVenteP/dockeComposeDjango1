from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('features', views.Features),
    path('download', views.Download),
]