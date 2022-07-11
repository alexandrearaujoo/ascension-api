from django.urls import path

from . import views

urlpatterns =[
    path('missions/', views.ListCreateMission.as_view())
]